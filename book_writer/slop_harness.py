"""slop_harness.py — Verifica todo e qualquer 'slop de AI' num texto.

Consolida num ponto único tudo que o livro já detecta + o que faltava:
  1. Marcadores de AI (evals.py — 25 EN + 8 PT, score + Fernanda markers)
  2. Regras determinísticas de voz (voice_postprocess.py — em-dash, ALL CAPS,
     jargão, frases banidas, inglês, número sem fonte, data futura, etc.)
  3. Title Case em PT (novo — o slop que a Fernanda pega: 'Calibrar, Não Inventar')
  4. GPT-ismos PT adicionais (novo — frases que o evals não cobre)

Uso:
  python3 -m book_writer.slop_harness <arquivo.md>
  python3 -m book_writer.slop_harness --selftest

É um VERIFICADOR: reporta e marca. Não reescreve texto (Title Case é ambíguo
com nome próprio, então fica pra revisão humana).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


# ── Title Case em PT ──────────────────────────────────────────────────────
# Em PT, título só capitaliza a 1ª palavra + nome próprio. 2+ palavras de
# CONTEÚDO capitalizadas num heading = Title Case (assinatura de LLM treinado
# em inglês). Palavras estruturais (artigos/preposições/conjunções) não contam.

_STOPWORDS = {
    'a', 'o', 'as', 'os', 'um', 'uma', 'uns', 'umas',
    'de', 'da', 'do', 'das', 'dos', 'e', 'em', 'na', 'no', 'nas', 'nos',
    'para', 'pra', 'pro', 'com', 'sem', 'por', 'pelo', 'pela', 'pelos', 'pelas',
    'ao', 'aos', 'à', 'às', 'que', 'ou', 'mas', 'como', 'até', 'ate',
    'após', 'apos', 'entre', 'sobre', 'sob', 'desde',
}


def _capitalized_content_words(line: str):
    """Palavras com inicial maiúscula (>=2 letras) que não são stopword."""
    return [w for w in re.findall(r'\b[A-ZÀ-Ú][a-zà-ú]+\b', line)
            if w.lower() not in _STOPWORDS]


def _looks_like_heading(line: str) -> bool:
    s = re.sub(r'^[\s#\-*•\d.]+\s*', '', line).strip()
    if not s or len(s) > 80:
        return False
    if re.search(r'[.!?;:]$', s):
        return False
    return bool(re.search(r'\b[A-ZÀ-Ú]', s))


def detect_title_case(text: str):
    """Linhas com Title Case (2+ palavras de conteúdo capitalizadas)."""
    hits = []
    for i, line in enumerate(text.split('\n'), 1):
        if not _looks_like_heading(line):
            continue
        caps = _capitalized_content_words(line)
        if len(caps) >= 2:
            hits.append({'line': i, 'text': line.strip()[:90], 'words': caps})
    return hits


# ── GPT-ismos PT adicionais (não cobertos pelo evals) ─────────────────────

EXTRA_GPT_PHRASES = [
    'é fundamental', 'é essencial', 'é crucial', 'é importante',
    'é preciso', 'é necessário', 'é inegável', 'não é apenas', 'não é só',
    'em suma', 'em resumo', 'em outras palavras', 'em última análise',
    'conforme mencionado', 'como dito anteriormente', 'como vimos',
    'nesse contexto', 'neste contexto', 'diante disso', 'diante desse cenário',
    'vale a pena', 'vale lembrar', 'dito isso', 'sem mais delongas',
    'no mundo de hoje', 'nos dias de hoje', 'na era atual',
    'cada vez mais', 'de forma cada vez mais',
]


def detect_extra_phrases(text: str):
    hits = []
    for phrase in EXTRA_GPT_PHRASES:
        matches = list(re.finditer(re.escape(phrase), text, re.IGNORECASE))
        if matches:
            hits.append({
                'phrase': phrase,
                'count': len(matches),
                'lines': sorted({text[:m.start()].count('\n') + 1 for m in matches}),
            })
    return hits


# ── Harness principal ─────────────────────────────────────────────────────

def run(text: str, max_chapters=None) -> dict:
    from book_writer.evals import diagnose_ai_voice
    from book_writer.voice_postprocess import post_process_voice, get_diff_summary

    report = {}

    # 1. marcadores de AI (evals)
    ai = diagnose_ai_voice(text)
    report['ai_score'] = ai['ai_score']
    report['fernanda_score'] = ai['fernanda_score']
    report['ai_markers'] = ai['ai_markers']
    report['fernanda_markers'] = ai['fernanda_markers']

    # 2. regras determinísticas de voz (o que seria corrigido)
    _, stats = post_process_voice(text, max_chapters=max_chapters)
    report['voice_fixes'] = stats
    report['voice_summary'] = get_diff_summary(stats)

    # 3. Title Case
    report['title_case'] = detect_title_case(text)

    # 4. GPT-ismos extra
    report['gpt_phrases'] = detect_extra_phrases(text)

    # veredito
    n_issues = 0
    if ai['ai_score'] > 10:
        n_issues += 1
    if stats.get('sources_flagged', 0):
        n_issues += 1
    if report['title_case']:
        n_issues += 1
    if report['gpt_phrases']:
        n_issues += 1
    report['verdict'] = 'CLEAN' if n_issues == 0 else ('WARN' if n_issues <= 2 else 'FAIL')

    return report


def render(r: dict) -> str:
    lines = ['## Slop check', '']
    lines.append(f"  AI score: {r['ai_score']}/100   Fernanda: {r['fernanda_score']}/100")
    if r['ai_markers']:
        top = sorted(r['ai_markers'].items(), key=lambda x: -x[1]['impact'])[:5]
        lines.append('  Marcadores de AI (top):')
        for name, info in top:
            lines.append(f"    - {name} ({info['count']}x): {info['description']}")
    lines.append('')
    lines.append('  Regras determinísticas: ' + r['voice_summary'].replace('\n', '\n    '))
    if r['title_case']:
        lines.append(f"\n  Title Case ({len(r['title_case'])} heading(s)):")
        for h in r['title_case']:
            lines.append(f"    L{h['line']}: \"{h['text']}\"  → caps: {', '.join(h['words'])}")
    if r['gpt_phrases']:
        lines.append(f"\n  GPT-ismos PT ({len(r['gpt_phrases'])} tipos):")
        for p in r['gpt_phrases']:
            lines.append(f"    - \"{p['phrase']}\" ({p['count']}x) — linhas {p['lines']}")
    lines.append('')
    lines.append(f"  VEREDITO: {r['verdict']}")
    return '\n'.join(lines)


def main():
    if '--selftest' in sys.argv:
        selftest()
        return
    if len(sys.argv) < 2:
        print('Uso: python3 -m book_writer.slop_harness <arquivo.md> | --selftest')
        sys.exit(1)
    text = Path(sys.argv[1]).read_text(encoding='utf-8')
    print(render(run(text)))


def selftest():
    # Title Case: pega
    tc = detect_title_case('Calibrar, Não Inventar\nGente que não existe\nA Anatomia de uma Pessoa')
    assert len(tc) == 2, f'esperava 2 Title Case, veio {len(tc)}: {tc}'
    assert 'Gente que não existe' not in [h['text'] for h in tc]

    # GPT-ismo
    gp = detect_extra_phrases('É fundamental entender isso. Em suma, funciona.')
    assert any(p['phrase'] == 'é fundamental' for p in gp)
    assert any(p['phrase'] == 'em suma' for p in gp)

    # run() agrega tudo num texto sujo
    r = run('Calibrar, Não Inventar\n\nÉ fundamental entender — de verdade — o impacto.')
    assert r['title_case'] and r['gpt_phrases'] and r['voice_fixes'].get('emdashes_removed', 0) > 0
    assert r['verdict'] in ('WARN', 'FAIL')

    print('SELFTEST OK — Title Case, GPT-ismos e agregação funcionando')


if __name__ == '__main__':
    main()
