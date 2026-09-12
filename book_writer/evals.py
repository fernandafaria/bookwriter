"""
Evals Harness — Detecta "cara de AI" em texto gerado.

25 marcadores de AI voice, 24 métricas de densidade.
Threshold < 10 = passa, 10-20 = REVISE (AuthenticityFixer obrigatório),
> 20 = REJECT.

Uso:
    from book_writer.evals import run_eval, AI_THRESHOLD
    report = run_eval("arquivo.md")
    print(report["summary"])
"""

import re
from pathlib import Path
from typing import Dict, List, Optional

# ═══════════════════════════════════════════════════════════════
# THRESHOLD
# ═══════════════════════════════════════════════════════════════
AI_THRESHOLD = 10  # score > 10 → AuthenticityFixer obrigatório
AI_REJECT_THRESHOLD = 20  # score > 20 → REJECT (refazer do zero)

# ═══════════════════════════════════════════════════════════════
# 25 MARCADORES DE "CARA DE AI"
# ═══════════════════════════════════════════════════════════════
#
# Cada marcador = (nome, regex_pattern, peso, categoria, descrição)
# Peso: 1 (leve), 2 (médio), 3 (forte — indica texto 100% LLM)

AI_MARKERS = [
    # ── Conectivos mecânicos (peso 2) ──
    ("moreover", r"\bMoreover\b", 2, "conectivo_mecanico",
     "'Moreover' é construção de paper acadêmico, não de prosa brasileira"),
    ("furthermore", r"\bFurthermore\b", 2, "conectivo_mecanico",
     "'Furthermore' no mesmo balde de moreover"),
    ("in_addition", r"\bIn addition\b", 2, "conectivo_mecanico",
     "'In addition' → trocar por 'Além disso' ou cortar"),
    ("additionally", r"\bAdditionally\b", 1, "conectivo_mecanico",
     "'Additionally' em demasia é tique de LLM"),
    ("it_is_worth_noting", r"\bIt is worth noting\b", 3, "conectivo_mecanico",
     "'It is worth noting' é ASSINATURA de GPT-4. Corte sempre."),
    ("interestingly", r"\bInterestingly\b", 2, "conectivo_mecanico",
     "'Interestingly' — o LLM dizendo pro leitor o que sentir"),

    # ── Paralelismo forçado (peso 2) ──
    ("not_only_but_also", r"\bNot only\b.{0,60}\bbut also\b", 2, "paralelismo_forcado",
     "'Not only... but also' é sintaxe de LLM, não de humano"),

    # ── Qualificadores frouxos (peso 3 — alta gravidade) ──
    ("arguably", r"\bArguably\b", 3, "qualificador_frouxo",
     "'Arguably' → o autor não tem certeza mas não quer pesquisar"),
    ("widely_regarded", r"\bwidely regarded\b", 3, "qualificador_frouxo",
     "'Widely regarded' por quem? Sem fonte = sem credibilidade"),
    ("many_experts_believe", r"\bmany experts believe\b", 3, "qualificador_frouxo",
     "'Many experts believe' é a marca suprema de texto de IA"),
    ("research_shows", r"\bresearch shows\b", 3, "qualificador_frouxo",
     "'Research shows' sem fonte específica → cortar ou citar"),

    # ── Fecho de parágrafo previsível (peso 1) ──
    ("rhetorical_question_every_section", r"\?\n\n", 1, "fecho_previsivel",
     "Toda seção termina com pergunta retórica?"),

    # ── Falsa concretude (peso 2) ──
    ("organizations", r"\borganizations\b", 1, "falsa_concretude",
     "'Organizations' → que organizações? Citar nomes."),
    ("fast_paced_landscape", r"\b(in today'?s|fast-paced)\s+(landscape|environment|world)\b", 3, "falsa_concretude",
     "'In today's fast-paced landscape' — JARGÃO PURO DE LLM. Cortar sempre."),
    ("landscape", r"\bdigits?al landscape\b", 1, "falsa_concretude",
     "'Digital landscape' → trocar por 'mercado', 'setor' ou caso concreto"),

    # ── Voz passiva excessiva (peso 1) ──
    ("passive_voice_en", r"\b(is|are|was|were|has been|have been)\s+\w+ed\b", 1, "voz_passiva",
     "Voz passiva em inglês — ok em moderação, mas excesso é sinal de LLM"),

    # ── Travessão artificial (peso 3 — fortíssimo marcador de LLM) ──
    ("emdash_abuse", r"—", 3, "travessao_artificial",
     "Em-dash (—) é o marcador #1 de texto de GPT. Fernanda NUNCA usa."),

    # ── Adverbios de intensidade vagos (peso 1) ──
    ("profoundly", r"\bprofoundly\b", 1, "adverbio_vago",
     "'Profoundly' → fraco. Trocar por dado."),
    ("significantly", r"\bsignificantly\b", 1, "adverbio_vago",
     "'Significantly' sem número → cortar"),

    # ── Abertura de seção padronizada (peso 2) ──
    ("lets_dive_in", r"\bLet'?s dive in\b", 3, "abertura_padronizada",
     "'Let's dive in' — assinatura de LLM. Fernanda diz 'Bora'."),
    ("in_this_section", r"\bIn this (section|chapter|post)\b", 2, "abertura_padronizada",
     "'In this section' → didatismo de LLM. Cortar."),

    # ── Frases "molho" de LLM (peso 2) ──
    ("in_other_words", r"\bIn other words\b", 2, "frase_molho",
     "'In other words' → repetir conceito é tique de LLM"),
    ("what_does_this_mean", r"\bWhat does this mean\b", 2, "frase_molho",
     "'What does this mean?' → o autor fingindo que o leitor perguntou"),

    # ── Conclusão genérica (peso 2) ──
    ("in_conclusion", r"\bIn conclusion\b", 2, "conclusao_generica",
     "'In conclusion' → LLM closing pattern. Cortar."),
    ("to_sum_up", r"\bTo sum up\b", 2, "conclusao_generica",
     "'To sum up' → mesmo balde de 'In conclusion'"),
]

# Marcadores em português (detectam AI voice em PT-BR)
AI_MARKERS_PT = [
    ("alem_disso", r"\bAlém disso\b", 1, "conectivo_mecanico_pt",
     "'Além disso' repetido → 3+ ocorrências é sinal de LLM"),
    ("outro_ponto_importante", r"\bOutro ponto importante\b", 3, "abertura_padronizada_pt",
     "'Outro ponto importante' é ASSINATURA de texto de GPT em português. Cortar sempre."),
    ("e_importante_ressaltar", r"\bÉ importante ressaltar\b", 3, "qualificador_frouxo_pt",
     "'É importante ressaltar' → o texto dizendo o que é importante em vez de mostrar"),
    ("vale_destacar", r"\bVale destacar\b", 2, "abertura_padronizada_pt",
     "'Vale destacar' → clichê. Cortar."),
    ("em_um_mundo_cada_vez_mais", r"\bEm um mundo (cada vez mais |digital|conectado|globalizado)\b", 3, "abertura_padronizada_pt",
     "'Em um mundo cada vez mais...' — ABERTURA DE GPT EM PORTUGUÊS. Cortar sempre."),
    ("nao_apenas_mas_tambem", r"\bNão apenas\b.{0,60}\bmas também\b", 2, "paralelismo_forcado_pt",
     "'Não apenas... mas também' — construção de LLM em PT-BR"),
    ("concluindo", r"\bConcluindo\b|\bPara concluir\b", 2, "conclusao_generica_pt",
     "'Concluindo' → fechamento previsível de LLM"),
    ("podemos_afirmar", r"\bPodemos afirmar\b|\bPode-se afirmar\b", 3, "qualificador_frouxo_pt",
     "'Podemos afirmar' — Quem 'podemos'? O autor. Corte."),
]


# ═══════════════════════════════════════════════════════════════
# FERNANDA MARKERS (presença = texto autêntico)
# ═══════════════════════════════════════════════════════════════

FERNANDA_MARKERS = [
    ("bora", r"\bbora\b", 3, "voz_coloquial", "Marca registrada dela"),
    ("ta_certo", r"\btá\b|\bta\b", 2, "voz_coloquial", "Coloquial direto"),
    ("rs", r"\brs\b", 2, "humor_seco", "Humor seco em texto"),
    ("troco", r"\btroço\b", 3, "voz_coloquial", "Vocabulário autoral"),
    ("pera", r"\bpera\b|\bperaí\b", 2, "voz_coloquial", "Tom de conversa"),
    ("nego", r"\bnego\b", 3, "voz_coloquial", "Gíria paulistana"),
    ("a_gente", r"\ba gente\b", 2, "voz_coloquial", "Pronome coloquial"),
    ("nome_proprio_com_data", r"\b[A-Z][a-z]+ [A-Z][a-z]+, (head de|gerente de|diretora de|CEO da|CPO da)", 3, "estrutura_autoral", "Cena com pessoa nomeada + cargo"),
    ("dia_da_semana", r"\b(segunda|terça|quarta|quinta|sexta)-feira\b", 2, "estrutura_autoral", "Cena com dia da semana"),
    ("pergunta_no_ar", r"\?$", 1, "estrutura_autoral", "Fecha com pergunta no ar"),
    ("cara_vocativo", r"\bcara\b", 2, "voz_coloquial", "Vocativo coloquial"),
    ("ne", r"\bné\b", 2, "voz_coloquial", "Confirmação coloquial"),
    ("putz", r"\bputz\b", 2, "humor_seco", "Espanto/humor seco"),
    ("po", r"\bpô\b", 2, "voz_coloquial", "Interjeição"),
    ("caramba", r"\bcaramba\b", 2, "voz_coloquial", "Interjeição"),
    ("role", r"\brolê\b", 2, "voz_coloquial", "Gíria"),
    ("tipo", r"\btipo\b", 1, "voz_coloquial", "Muleta coloquial"),
    ("maluquice", r"\bmaluquice\b", 2, "voz_coloquial", "Vocabulário autoral"),
]


# ═══════════════════════════════════════════════════════════════
# FUNÇÕES DE AVALIAÇÃO
# ═══════════════════════════════════════════════════════════════

def count_markers(text: str, markers: list) -> Dict[str, int]:
    """Conta ocorrências de cada marcador no texto."""
    results = {}
    for name, pattern, weight, category, desc in markers:
        matches = len(re.findall(pattern, text, re.IGNORECASE))
        if matches > 0:
            results[name] = matches
    return results


def compute_ai_score(text: str) -> dict:
    """Calcula o score de AI voice (0-100, quanto menor melhor)."""
    if not text:
        return {"score": 0, "markers": {}, "fernanda_score": 0, "fernanda_markers": {},
                "total_ai_markers": 0, "total_fernanda_markers": 0}

    # Conta marcadores de AI (inglês + português)
    all_ai_markers = AI_MARKERS + AI_MARKERS_PT
    ai_matches = {}
    weighted_score = 0
    total_matches = 0

    for name, pattern, weight, category, desc in all_ai_markers:
        matches = len(re.findall(pattern, text, re.IGNORECASE))
        if matches > 0:
            ai_matches[name] = {
                "count": matches,
                "weight": weight,
                "category": category,
                "description": desc,
                "impact": weight * matches,
            }
            weighted_score += weight * matches
            total_matches += matches

    # Conta marcadores da Fernanda
    fernanda_matches = {}
    fernanda_weighted = 0
    fernanda_total = 0

    for name, pattern, weight, category, desc in FERNANDA_MARKERS:
        matches = len(re.findall(pattern, text, re.IGNORECASE))
        if matches > 0:
            fernanda_matches[name] = {
                "count": matches,
                "weight": weight,
                "category": category,
                "description": desc,
            }
            fernanda_weighted += weight * matches
            fernanda_total += matches

    # Score normalizado (max 51 pontos possíveis → normaliza pra 0-100)
    max_possible_score = sum(w for _, _, w, _, _ in all_ai_markers)
    normalized_score = min(100, int((weighted_score / max(51, 1)) * 100))

    # Fernanda score: quanto mais marcadores dela, melhor
    max_fernanda = sum(w for _, _, w, _, _ in FERNANDA_MARKERS)
    fernanda_presence = min(100, int((fernanda_weighted / max(12, 1)) * 100))

    return {
        "score": normalized_score,
        "markers": ai_matches,
        "fernanda_score": fernanda_presence,
        "fernanda_markers": fernanda_matches,
        "total_ai_markers": total_matches,
        "total_fernanda_markers": fernanda_total,
        "raw_weighted": weighted_score,
    }


def diagnose_ai_voice(text: str) -> dict:
    """Diagnóstico completo: AI score + recomendações + trechos problemáticos."""
    ai_result = compute_ai_score(text)

    # Busca trechos dos marcadores mais graves (peso 3)
    severe_markers = []
    lines = text.split("\n")
    for name, pattern, weight, category, desc in AI_MARKERS + AI_MARKERS_PT:
        if weight < 3:
            continue
        for i, line in enumerate(lines):
            if re.search(pattern, line, re.IGNORECASE):
                start = max(0, i - 1)
                end = min(len(lines), i + 2)
                context = "\n".join(lines[start:end])
                severe_markers.append({
                    "marker": name,
                    "line": i + 1,
                    "text": line.strip()[:120],
                    "context": context[:300],
                    "fix": desc,
                })

    # Decisão
    decision = "PASS"
    if ai_result["score"] > AI_REJECT_THRESHOLD:
        decision = "REJECT"
    elif ai_result["score"] > AI_THRESHOLD:
        decision = "FIX"

    return {
        "decision": decision,
        "ai_score": ai_result["score"],
        "fernanda_score": ai_result["fernanda_score"],
        "ai_markers": ai_result["markers"],
        "fernanda_markers": ai_result["fernanda_markers"],
        "severe_issues": severe_markers,
        "summary": f"AI Score: {ai_result['score']}/100 — "
                   f"Fernanda Score: {ai_result['fernanda_score']}/100 — "
                   f"{len(ai_result['markers'])} tipos de marcadores AI detectados — "
                   f"Decisão: {decision}",
    }


def run_eval(filepath: str) -> Optional[dict]:
    """Roda avaliação completa em um arquivo."""
    p = Path(filepath)
    if not p.exists():
        print(f"[Eval] Arquivo não encontrado: {filepath}")
        return None

    text = p.read_text(encoding="utf-8")

    result = diagnose_ai_voice(text)
    result["file"] = str(p)
    result["size_bytes"] = len(text)
    result["size_chars"] = len(text)

    print(f"[Eval] {p.name}: AI={result['ai_score']}/100, "
          f"Fernanda={result['fernanda_score']}/100, "
          f"Decisão={result['decision']}")

    if result["severe_issues"]:
        print(f"[Eval] {len(result['severe_issues'])} problemas graves:")
        for issue in result["severe_issues"][:5]:
            print(f"  L{issue['line']}: {issue['text'][:80]}")

    return result


def get_fixer_prompt(text: str, eval_result: dict) -> str:
    """Gera prompt para o AuthenticityFixer corrigir os problemas detectados."""
    if not eval_result or eval_result["ai_score"] <= AI_THRESHOLD:
        return ""

    issues = eval_result.get("ai_markers", {})
    severe = eval_result.get("severe_issues", [])

    prompt_parts = [
        "## PROBLEMAS DE AUTENTICIDADE DETECTADOS\n",
        f"AI Score: {eval_result['ai_score']}/100 (threshold: {AI_THRESHOLD})\n",
        f"Fernanda Score: {eval_result['fernanda_score']}/100\n\n",
        "### Marcadores de 'cara de AI' encontrados:\n",
    ]

    for name, info in sorted(issues.items(), key=lambda x: -x[1]["impact"]):
        prompt_parts.append(
            f"- **{name}** ({info['count']}x, peso {info['weight']}): "
            f"{info['description']}\n"
        )

    if severe:
        prompt_parts.append("\n### Trechos problemáticos:\n")
        for issue in severe[:10]:
            prompt_parts.append(f"- L{issue['line']}: `{issue['text'][:100]}`\n")
            prompt_parts.append(f"  → {issue['fix']}\n")

    prompt_parts.append("\n### REGRAS DE CORREÇÃO:\n")
    prompt_parts.append("1. CORRIJA apenas os trechos problemáticos — NÃO reescreva o texto inteiro\n")
    prompt_parts.append("2. NUNCA use: 'In today's fast-paced landscape', 'Not only... but also', "
                        "'It is worth noting', 'Let's dive in', 'Interestingly'\n")
    prompt_parts.append("3. NUNCA use em-dash (—). Substitua por vírgula ou dois-pontos\n")
    prompt_parts.append("4. NUNCA use ALL CAPS para ênfase\n")
    prompt_parts.append("5. 'Research shows' / 'Studies indicate' → ou cita fonte ESPECÍFICA, ou corta\n")
    prompt_parts.append("6. Troque: 'Furthermore' → corte; 'Additionally' → 'E mais:'; "
                        "'Moreover' → corte; 'In conclusion' → corte\n")
    prompt_parts.append("7. Troque: 'É importante ressaltar' → corte; 'Outro ponto importante' → corte; "
                        "'Em um mundo cada vez mais...' → corte\n")
    prompt_parts.append("8. Mantenha o texto com MESMO TAMANHO. NAO RESUMA.\n")
    prompt_parts.append("9. Use vocabulário coloquial: 'bora', 'tá', 'a gente', 'troço' onde apropriado\n")
    prompt_parts.append("10. Preserve TODOS os dados, fontes, frameworks, cases e estrutura do original\n")

    return "".join(prompt_parts)


# ═══════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        # Pega o artigo mais recente
        output_dir = Path(__file__).parent / "output" / "artigos"
        files = sorted(output_dir.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
        if not files:
            print("[Eval] Nenhum arquivo encontrado")
            sys.exit(1)
        path = str(files[0])

    result = run_eval(path)

    if result:
        print(f"\n{'='*60}")
        print(result["summary"])
        print(f"{'='*60}")

        if result["severe_issues"]:
            print(f"\nProblemas graves ({len(result['severe_issues'])}):")
            for issue in result["severe_issues"][:5]:
                print(f"  L{issue['line']}: {issue['text'][:100]}")
