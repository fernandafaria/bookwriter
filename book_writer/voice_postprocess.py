"""
Voice Post-Processor — deterministic cleanup layer.
Runs AFTER the AuthenticityFixer LLM rewrite.
Handles mechanical rules that don't require intelligence — just discipline.

All rules come from STYLE_GUIDE in style_guide.py.
"""

import re
from typing import Tuple


# ── Em-dash removal ──────────────────────────────────────────────────────
# Marcador #1 de texto de GPT. Fernanda NUNCA usa travessão.
# Substitui por vírgula (mid-phrase), ponto (fim de sentença), ou dois-pontos.

def _remove_emdashes(text: str) -> Tuple[str, int]:
    """Remove em-dashes, replacing with context-appropriate punctuation."""
    count = text.count("—")
    if count == 0:
        return text, 0

    # Mid-phrase: "X — Y" → "X, Y" or "X: Y"
    text = re.sub(r'(\w)\s*—\s*(\w)', r'\1, \2', text)
    # After sentence-ending punctuation: just remove
    text = re.sub(r'\.[ ]*—[ ]*', '. ', text)
    text = re.sub(r'\?[ ]*—[ ]*', '? ', text)
    text = re.sub(r'![ ]*—[ ]*', '! ', text)
    # At start of line or after newline
    text = re.sub(r'\n\s*—\s*', '\n', text)
    # Remaining isolated ones
    text = re.sub(r'\s*—\s*', ', ', text)

    return text, count


# ── Banned phrases ───────────────────────────────────────────────────────
# Do STYLE_GUIDE: "NUNCA usar: 'espero que esteja bem', 'é um prazer compartilhar',
# 'nessa jornada'"

BANNED_PHRASES = [
    # Remove the entire sentence containing these phrases
    (r'[^.]*espero que (você|vc|todos|tudo) (esteja|estejam) bem[^.]*\.', ''),
    (r'[^.]*é um prazer (compartilhar|estar|falar)[^.]*\.', ''),
    (r'[^.]*nessa jornada[^.]*\.', ''),
    (r'[^.]*fico à disposição[^.]*\.', ''),
    (r'[^.]*vamos mergulhar[^.]*\.', ''),
    (r'[^.]*let\'s dive in[^.]*\.', ''),
    (r'[^.]*In today\'s fast-paced (world|landscape|digital)[^.]*\.', ''),
]


# ── Banned words (jargão de consultoria) ─────────────────────────────────
# Do STYLE_GUIDE: "NUNCA: jargão de consultoria"

BANNED_WORDS = {
    'alavancar': 'usar',
    'alavancagem': 'ganho',
    'sinergia': 'combinação',
    'disruptivo': 'novo',
    'maximizar': 'aumentar',
    'solução robusta': 'solução sólida',
    'empoderar': 'dar autonomia',
    'ecossistema': 'ambiente',
    'dor do cliente': 'problema do cliente',
    'jornada do usuário': 'experiência do usuário',
    'ponta a ponta': 'completo',
    'holístico': 'completo',
    'value proposition': 'proposta de valor',
    'best in class': 'melhor do mercado',
    'game changer': 'mudança real',
    'bleeding edge': 'ponta',
    'circle back': 'voltar a falar',
    'deep dive': 'análise',
    'low hanging fruit': 'ganhos rápidos',
}


# ── ALL CAPS for emphasis ────────────────────────────────────────────────
# Do STYLE_GUIDE: "Zero ALL CAPS para ênfase"

def _remove_allcaps_emphasis(text: str) -> Tuple[str, int]:
    """Remove ALL CAPS words that appear to be for emphasis (isolated, mid-sentence)."""
    count = 0
    def replace_allcaps(match):
        nonlocal count
        word = match.group(1)
        # Skip: acronyms (3 letters or less, all consonants), Roman numerals
        if len(word) <= 3 and all(c.isupper() for c in word if c.isalpha()):
            return word
        count += 1
        return word.capitalize()

    # Match isolated ALL CAPS words (not part of longer ALL CAPS sections)
    text = re.sub(r'\b([A-ZÁÀÂÃÉÊÍÓÔÕÚÜÇ]{4,})\b', replace_allcaps, text)
    return text, count


# ── English words in PT-BR ───────────────────────────────────────────────
# Do STYLE_GUIDE: "NUNCA: 'very', 'really', 'quite' ou equivalentes em PT"
# Also: replace common English terms with PT-BR equivalents

ENGLISH_REPLACEMENTS = {
    'very': 'muito',
    'really': 'realmente',
    'quite': 'bastante',
    'actually': 'na verdade',
    'basically': 'basicamente',
    'literally': 'literalmente',
    'obviously': 'claramente',
    'absolutely': 'totalmente',
    'definitely': 'com certeza',
    'probably': 'provavelmente',
    'maybe': 'talvez',
    'anyway': 'de qualquer forma',
    'however': 'no entanto',  # But "entretanto" is fine — this catches standalone English
}

# ── Case Tagger + Source Enforcer (rigor factual determinístico) ──────────
# O Writer alucina casos anônimos e métricas sem fonte. Estas regras MARCAÇÃO
# (não corrigem) o que precisa de verificação humana — o juiz dá 9 quando o
# texto é honesto sobre o que é ilustrativo e o que tem fonte.

def _tag_anonymous_cases(text: str) -> Tuple[str, int]:
    """Marca cena de abertura como reconstituição e casos anônimos como ilustrativos."""
    count = 0
    # 1. Cena de abertura narrativa → marca reconstituição
    m = re.search(
        r'\b(Era uma (?:segunda|terça|quarta|quinta|sexta|s[áa]bado|domingo)-feira de [a-zçã]+ de \d{4})\b',
        text, re.IGNORECASE)
    if m and 'reconstitui' not in text[:m.end() + 40]:
        text = text[:m.end()] + ' *(reconstituição)*' + text[m.end():]
        count += 1
    # 2. Entidades anônimas (primeira menção de cada padrão)
    anon = [
        r'\buma (fintech|startup|empresa|healthtech|seguradora|varejista|ag[êe]ncia)\b',
        r'\bum (grande banco|banco|hospital|e-commerce|varejista)\b',
    ]
    for pat in anon:
        m = re.search(pat, text, re.IGNORECASE)
        if m and '(caso ilustrativo' not in text[max(0, m.end() - 20):m.end() + 40]:
            text = text[:m.end()] + ' *(caso ilustrativo/composto)*' + text[m.end():]
            count += 1
    return text, count


def _enforce_sources(text: str) -> Tuple[str, int]:
    """Invariante de rastreabilidade: REMOVE a sentença com métrica numérica sem fonte.

    Regra (paralelo do deepseek-harness 'model-visible means logged'): todo
    número do capítulo tem que ter fonte rastreável (URL ou '(Fonte, ano)') a
    até 120 chars. Sentença com métrica órfã = alucinação -> remove a sentença
    inteira (gramaticalmente limpo, sem resíduo de "consome de mídia").

    É a REDE DE SEGURANÇA determinística: o FactChecker (LLM) já reescreve as
    frases finas; aqui removem-se só as que escaparam.
    """
    count = 0
    metric = re.compile(
        r'\b\d{1,3}(?:[.,]\d+)?\s*%'
        r'|\b\d{1,3}(?:[.,]\d+)?\s*(?:milhões?|bilhões?|milhares?|mil|horas?|dias?|meses|semanas?|minutos?)\b'
        r'|\b\d{1,3}(?:[.,]\d+)?\s*x\b'
        r'|\bmilhares?\b'
        r'|\b(?:dezenas|centenas|milhares)\s+de\b',  # quantificador vago ("dezenas de milhões")
        re.IGNORECASE,
    )
    source_near = re.compile(r'\([^()]{1,60}?(?:20\d{2})\)')

    out = []
    for sent in re.split(r'(?<=[.!?])\s+', text):
        orphan = False
        for m in metric.finditer(sent):
            s = max(0, m.start() - 120)
            e = min(len(sent), m.end() + 120)
            window = sent[s:e]
            if 'http' not in window and not source_near.search(window):
                orphan = True
                break
        if orphan:
            count += 1  # sentença removida (contém métrica órfã)
            continue
        out.append(sent)

    return ' '.join(out), count


# ── Novos invariantes determinísticos de rigor (data, caso, capítulo) ─────

def _flag_future_dates(text: str) -> Tuple[str, int]:
    """Marca datas/anos no FUTURO (relativos a hoje) com [data/ano futuro?].

    Pega o bug documentado "Valor Econômico, 18/08/2026" — uma data que ainda
    não chegou é sinal de alucinação ou erro de transcrição.
    """
    from datetime import datetime
    today = datetime.now()
    count = 0

    def repl(m):
        nonlocal count
        try:
            if datetime(int(m.group(3)), int(m.group(2)), int(m.group(1))) > today:
                count += 1
                return m.group(0) + " [data futura?]"
        except ValueError:
            pass
        return m.group(0)

    text = re.sub(r'\b(\d{1,2})/(\d{1,2})/(\d{4})\b', repl, text)

    # ano sozinho no futuro (ex: "de 2027"); (?<!/) evita o ano de DD/MM/YYYY
    def repl_year(m):
        nonlocal count
        if int(m.group(1)) > today.year:
            count += 1
            return m.group(0) + " [ano futuro?]"
        return m.group(0)

    text = re.sub(r'(?<!/)\b(20\d{2})\b', repl_year, text)
    return text, count


def _resolve_double_case_tag(text: str) -> Tuple[str, int]:
    """Marca contradição 'caso real' vs 'caso ilustrativo/composto' na mesma sentença.

    Pega o bug documentado: o mesmo trecho dizia que era "caso real" E "caso
    ilustrativo". As duas tags na mesma frase = conflito.
    """
    count = 0
    out = []
    for sent in re.split(r'(?<=[.!?])\s+', text):
        has_real = re.search(r'caso real', sent, re.IGNORECASE)
        has_illus = re.search(r'(caso (ilustrativo|composto)|ilustrativo|composto)', sent, re.IGNORECASE)
        if has_real and has_illus and '[caso' not in sent:
            sent = sent + ' [caso: real ou ilustrativo?]'
            count += 1
        out.append(sent)
    return ' '.join(out), count


def _flag_chapter_leak(text: str, max_chapters=None) -> Tuple[str, int]:
    """Marca referência a capítulo que não existe no brief (vazamento).

    Pega o bug "Capítulo 8" num livro de 7 caps. Precisa do total de capítulos
    do brief (passado por post_process_voice(max_chapters=N)).
    """
    if not max_chapters:
        return text, 0
    count = 0

    def repl(m):
        nonlocal count
        if int(m.group(1)) > max_chapters:
            count += 1
            return m.group(0) + " [capítulo inexistente?]"
        return m.group(0)

    text = re.sub(r'\b[Cc]ap[íi]tulo\s+(\d+)\b', repl, text)
    return text, count


# ── Main post-processing pipeline ────────────────────────────────────────

def post_process_voice(text: str, max_chapters=None) -> Tuple[str, dict]:
    """Apply all deterministic voice rules to text.

    Args:
        text: Draft text after AuthenticityFixer LLM rewrite.

    Returns:
        (cleaned_text, stats_dict) with counts of each fix applied.
    """
    stats = {}

    # 1. Remove em-dashes
    text, count = _remove_emdashes(text)
    stats["emdashes_removed"] = count

    # 2. Remove banned phrases
    for pattern, replacement in BANNED_PHRASES:
        matches = len(re.findall(pattern, text, re.IGNORECASE))
        if matches:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
            stats[f"banned_phrase_{pattern[:30]}"] = matches

    # 3. Replace banned words
    for banned, replacement in BANNED_WORDS.items():
        pattern = re.compile(r'\b' + re.escape(banned) + r'\b', re.IGNORECASE)
        matches = len(pattern.findall(text))
        if matches:
            # Capitalize replacement if original was capitalized
            def repl(m):
                orig = m.group(0)
                if orig[0].isupper():
                    return replacement[0].upper() + replacement[1:]
                return replacement
            text = pattern.sub(repl, text)
            stats[f"banned_word_{banned}"] = matches

    # 4. Remove ALL CAPS emphasis
    text, count = _remove_allcaps_emphasis(text)
    stats["allcaps_fixed"] = count

    # 5. Replace English standalone words in PT-BR text
    # Only replace if word appears isolated (surrounded by PT-BR text)
    for eng, ptbr in ENGLISH_REPLACEMENTS.items():
        pattern = re.compile(r'\b' + re.escape(eng) + r'\b')
        matches = len(pattern.findall(text))
        if matches:
            text = pattern.sub(ptbr, text)
            stats[f"eng_to_ptbr_{eng}"] = matches

    # 6. Tag anonymous cases (reconstituição + caso ilustrativo)
    text, count = _tag_anonymous_cases(text)
    stats["anon_cases_tagged"] = count

    # 7. Invariante de rastreabilidade: remove sentenças com métrica sem fonte
    text, count = _enforce_sources(text)
    stats["sources_flagged"] = count

    # 8. Datas/anos no futuro
    text, count = _flag_future_dates(text)
    stats["future_dates_flagged"] = count

    # 9. Contradição caso real × caso ilustrativo
    text, count = _resolve_double_case_tag(text)
    stats["case_tag_conflicts"] = count

    # 10. Vazamento de capítulo inexistente
    text, count = _flag_chapter_leak(text, max_chapters)
    stats["chapter_leaks"] = count

    return text, stats


def get_diff_summary(stats: dict) -> str:
    """Generate a human-readable summary of what was fixed."""
    lines = []
    if stats.get("emdashes_removed", 0) > 0:
        lines.append(f"  — removidos: {stats['emdashes_removed']}")
    if stats.get("allcaps_fixed", 0) > 0:
        lines.append(f"  ALL CAPS corrigidos: {stats['allcaps_fixed']}")

    banned_words = {k: v for k, v in stats.items() if k.startswith("banned_word_") and v > 0}
    if banned_words:
        words = [k.replace("banned_word_", "") for k in banned_words]
        lines.append(f"  Jargão substituído: {', '.join(words)}")

    banned_phrases = {k: v for k, v in stats.items() if k.startswith("banned_phrase_") and v > 0}
    if banned_phrases:
        lines.append(f"  Frases banidas removidas: {len(banned_phrases)}")

    eng_words = {k: v for k, v in stats.items() if k.startswith("eng_to_ptbr_") and v > 0}
    if eng_words:
        words = [k.replace("eng_to_ptbr_", "") for k in eng_words]
        lines.append(f"  Inglês → PT-BR: {', '.join(words)}")

    if stats.get("anon_cases_tagged", 0) > 0:
        lines.append(f"  Casos anônimos marcados: {stats['anon_cases_tagged']}")

    if stats.get("sources_flagged", 0) > 0:
        lines.append(f"  Sentenças com número sem fonte removidas: {stats['sources_flagged']}")

    if stats.get("future_dates_flagged", 0) > 0:
        lines.append(f"  Datas/anos futuros marcados: {stats['future_dates_flagged']}")

    if stats.get("case_tag_conflicts", 0) > 0:
        lines.append(f"  Conflito caso real × ilustrativo: {stats['case_tag_conflicts']}")

    if stats.get("chapter_leaks", 0) > 0:
        lines.append(f"  Referências a capítulo inexistente: {stats['chapter_leaks']}")

    return "\n".join(lines) if lines else "  (nenhuma correção necessária)"


if __name__ == "__main__":
    # auto-teste do invariante de rastreabilidade
    t, n = _enforce_sources("Consome 13 horas de mídia por dia. Mantém 50% de DAU/MAU (McKinsey, 2024). Cai 5% conforme https://x.com/estudo.")
    assert n == 1, f"esperava 1 sentença removida, veio {n}"
    assert "13 horas" not in t and "50%" in t and "5%" in t, t

    # vague quantifier ("dezenas de") vira métrica órfã
    t2, n2 = _enforce_sources("Investiu dezenas de milhões no trimestre.")
    assert n2 == 1, f"esperava 1 remoção de 'dezenas de', veio {n2}"

    # data futura
    from datetime import datetime
    next_year = datetime.now().year + 1
    t3, n3 = _flag_future_dates(f"Lançou em 18/08/{next_year}.")
    assert n3 >= 1 and "[data futura?]" in t3, t3

    # conflito caso real × ilustrativo
    t4, n4 = _resolve_double_case_tag("É um caso real de uma fintech, um caso ilustrativo composto.")
    assert n4 == 1 and "[caso: real ou ilustrativo?]" in t4, t4

    # vazamento de capítulo
    t5, n5 = _flag_chapter_leak("Veremos no Capítulo 8 como isso se resolve.", 7)
    assert n5 == 1 and "[capítulo inexistente?]" in t5, t5

    print("invariante OK:", n, "sentença removida; novas regras OK:", n2, n3, n4, n5)
