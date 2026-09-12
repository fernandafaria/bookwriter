"""
Book Writer — Agents
====================
Implementação dos agentes como nós do grafo LangGraph.

Pipeline: Researcher → Strategist → Writer → CopyEditor → EditorChefe

Cada agente é uma função que recebe BookWriterState e retorna BookWriterState.
Agentes com tool access usam _invoke_with_tools para pesquisar antes de responder.
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from book_writer.tools import ALL_TOOLS, _invoke_with_tools, _get_model
from book_writer.knowledge_base import get_chapter_info, FRAMEWORKS, BOOK_OUTLINE
from book_writer.curiosity_registry import (
    to_prompt_context, get_gaps_planted_in, get_gaps_to_resolve,
    get_outstanding_gaps, mark_resolved, escalate_gap,
)
from book_writer.style_guide import STYLE_GUIDE


# ── Brief resolution (editora agentica) ──────────────────────────────────────
# Um "brief" descreve qualquer livro. Se o state carrega um brief, os agentes
# o usam como fonte de verdade; senão, caem no BOOK_OUTLINE fixo (compat).

def _resolve_chapter_info(state):
    """(chapter_info, brief) — usa brief do state se presente, senão o livro fixo."""
    n = state.get("target_chapter", 1)
    brief = state.get("brief")
    if brief:
        from book_writer.brief import get_chapter_info as _bci
        return _bci(brief, n), brief
    return get_chapter_info(n), None


def _book_context_block(state, chapter_num):
    """Bloco 'CONTEXTO DO LIVRO + CAPÍTULOS ANTERIORES/POSTERIORES'."""
    _, brief = _resolve_chapter_info(state)
    if brief:
        from book_writer.brief import chapter_context
        prev, post = chapter_context(brief, chapter_num)
        prev_txt = "\n".join(f"- {p}" for p in prev) if prev else "- (primeiro capítulo)"
        post_txt = "\n".join(f"- {p}" for p in post) if post else "- (último capítulo)"
        return (
            f"CONTEXTO DO LIVRO:\n{brief.get('thesis', '')}\n\n"
            f"PÚBLICO: {brief.get('audience', '')}\n\n"
            f"CAPÍTULOS ANTERIORES (para contexto):\n{prev_txt}\n\n"
            f"CAPÍTULOS POSTERIORES (para plantar gaps):\n{post_txt}"
        )
    return """CONTEXTO DO LIVRO:
Este é o guia definitivo para Product Managers na era da IA.

CAPÍTULOS ANTERIORES (para contexto):
- Cap 1: A AI Trap (framework ESCAPE)
- Cap 2: O Momento de Inflexão (7 Sinais)
- Cap 3: Anatomia do AI PM (10 Competências)
- Cap 4: Technical Fluency
- Cap 5: O Novo Discovery — Experimentação em Mundo Não-Determinístico
- Cap 6: Data-Driven Decision Making 2.0
- Cap 7: Designing for AI — UX em Mundo Não-Determinístico

CAPÍTULOS POSTERIORES (para plantar gaps):
- Cap 9: AI Product Strategy
- Cap 10: Leading AI Transformation"""


def _research_block(state):
    """Diretrizes de pesquisa — do brief (research_angles) ou fallback fixo."""
    _, brief = _resolve_chapter_info(state)
    if brief:
        angles = brief.get("research_angles", [])
        angle_txt = "\n".join(f"{i+1}. **{a}**" for i, a in enumerate(angles)) if angles else \
            "Pesquise fontes atualizadas e casos reais relevantes ao tema do capítulo."
        return f"""PESQUISE USANDO AS FERRAMENTAS (temas do brief):

{angle_txt}

Para cada tema: use search_sources (fonte única — Perplexity com citação, cai pra OpenAlex/Google). Só cite número/claim que veio dela, com a fonte anexada.
Busque dados e estatísticas ATUALIZADOS ({CURRENT_YEAR}), cases reais (preferência por
Brasil) e frameworks de referência. Consulte read_knowledge_base('frameworks') para
entender frameworks já existentes que o capítulo referencia.

ORGANIZE SEU OUTPUT ASSIM:

## 1. PRINCIPAIS FONTES ENCONTRADAS
(tabela com fonte, URL, data, resumo do conteúdo)

## 2. DADOS QUANTITATIVOS ATUALIZADOS
(números, %, estatísticas com fonte e ano)

## 3. CASES REAIS
(3-5 cases com: empresa, problema, solução, resultados)

## 4. FRAMEWORKS DE REFERÊNCIA
(princípios e padrões relevantes ao tema)

## 5. MATÉRIA-PRIMA PARA O CURIOSITY SCHEDULER
(que perguntas intrigantes este capítulo deveria plantar ou responder?)
"""
    return """PESQUISE USANDO AS FERRAMENTAS:

1. **Product Compass (productcompass.pm):**
   Busque artigos do Pawel Huryn sobre:
   - AI agents e times de produto
   - Agentic Workflow Thinking
   - PM Brain OS e second brain
   - Multi-agent systems em produto
   - AI-native team structures
   - Product Operating Model com IA

2. **Casos reais de empresas** que implementaram agentes de IA no time:
   - Startups usando Cursor, Claude Code, Copilot como \"membros\" do time
   - Empresas com agentes internos de produto (ex: PRD generation, code review)
   - Times híbridos humano-agente

3. **Dados e estatísticas ATUALIZADOS ({CURRENT_YEAR}):**
   - Adoção de AI agents em times de desenvolvimento
   - Produtividade de times com agentes de IA
   - Impacto de agentes em qualidade e velocidade de produto
   - Mercado de AI agents (valuations, crescimento)

4. **Frameworks de team building com IA:**
   - Como montar times híbridos
   - Níveis de autonomia de agentes
   - Rituais e comunicação em times híbridos
   - Métricas de eficácia de time híbrido

5. **Referências e industry reports:**
   - Anthropic sobre AI agents
   - LangChain/LangGraph sobre agentic workflows
   - McKinsey/HBR sobre times com IA
   - Product Compass sobre Agentic Workflow Thinking

6. **Cases Brasil:**
   - Empresas brasileiras usando agentes de IA em times de produto
   - Comunidade de PMs brasileiros usando AI agents

Use search_web para buscar cada categoria. Extraia URLs promissoras com extract_urls.
Consulte a base de conhecimento local com read_knowledge_base('frameworks') para
entender frameworks já existentes que este capítulo referencia.

ORGANIZE SEU OUTPUT ASSIM:

## 1. PRINCIPAIS FONTES ENCONTRADAS
(tabela com fonte, URL, data, resumo do conteúdo)

## 2. DADOS QUANTITATIVOS ATUALIZADOS
(números, %, estatísticas com fonte e ano)

## 3. CASES REAIS
(3-5 cases com: empresa, problema, solução, resultados)

## 4. FRAMEWORKS DE REFERÊNCIA
(princípios e padrões para times híbridos humano-agente)

## 5. INSIGHTS DO PRODUCT COMPASS
(o que o Pawel Huryn diz sobre agentes de IA e times de produto)

## 6. MATÉRIA-PRIMA PARA O CURIOSITY SCHEDULER
(que perguntas intrigantes este capítulo deveria plantar ou responder?)
"""


LEGACY_TERMS = ["AI Trap", "ESCAPE", "7 Sinais", "10 Competências", "L.I.D.E.R.A.",
                "CLEAR", "INTELIGENTE", "Product Excellence Maturity Model", "AI Product Management",
                "Product Compass", "Pawel Huryn"]


def _scrub(text, brief):
    """Remove menções a frameworks/nomes do livro antigo quando há um brief novo."""
    if not brief:
        return text
    out = text
    for t in LEGACY_TERMS:
        out = out.replace(t, "")
    return out


def _style_guide_for(state):
    """STYLE_GUIDE sem os frameworks do livro antigo quando há brief."""
    _, brief = _resolve_chapter_info(state)
    return _scrub(STYLE_GUIDE, brief)


def _voice_postprocess(text, max_chapters=None):
    """Pós-processamento determinístico (voz + rigor factual). Roda SEMPRE."""
    from book_writer.voice_postprocess import post_process_voice, get_diff_summary
    if not isinstance(text, str):
        return text
    text, stats = post_process_voice(text, max_chapters=max_chapters)
    summary = get_diff_summary(stats)
    if summary != "  (nenhuma correção necessária)":
        print(f"[VoicePost] Deterministic fixes:\n{summary}")
    return text


def _apply_corrections_json(report: str, draft: str):
    """Aplica CORRECOES_JSON (formato do FactChecker/Verifier) no draft.

    Retorna (draft_corrigido, numero_de_correcoes). Parseia o bloco JSON e faz
    replace literal; é a mesma mecânica usada pelo CopyEditor Fase A.
    """
    corrections = []
    jm = re.search(r'## CORRECOES_JSON\s*(.*)', report, re.DOTALL)
    if jm:
        jarr = re.search(r'\[.*\]', jm.group(1), re.DOTALL)
        if jarr:
            try:
                corrections = json.loads(jarr.group(0))
            except Exception:
                corrections = []
    applied = 0
    for corr in corrections:
        if corr.get("old") and corr.get("new") and corr["old"] in draft:
            draft = draft.replace(corr["old"], corr["new"], 1)
            applied += 1
    return draft, applied


# ── Data freshness anchor ──────────────────────────────────────────────────
CURRENT_YEAR = datetime.now().year
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
FRESHNESS_CUTOFF = datetime.now().replace(year=CURRENT_YEAR - 1).strftime("%Y-%m-%d")


# ═══════════════════════════════════════════════════════════════════════════
# SYSTEM PROMPTS
# ═══════════════════════════════════════════════════════════════════════════

BOOK_SYSTEM = f"""Você é parte do sistema multiagente de escrita do livro "AI Product Management"
da autora Fernanda Faria. Ano corrente: {CURRENT_YEAR}.

Suas respostas serão usadas como parte do pipeline de produção do livro.
Seja preciso, direto e orientado à ação.

Regras:
- Sempre escreva em português do Brasil.
- NUNCA use em-dashes (—). Use vírgula, dois-pontos ou ponto.
- NUNCA use ALL CAPS para ênfase.
- Toda afirmação factual precisa de fonte verificável.
- Quando dados forem de anos anteriores a {CURRENT_YEAR}, busque os mais recentes."""


# ═══════════════════════════════════════════════════════════════════════════
# HELPERS — Substack & Voice Context Injection
# ═══════════════════════════════════════════════════════════════════════════

# Mapping: which Substack articles are most relevant to each chapter
SUBSTACK_CHAPTER_MAP = {
    # All chapters benefit from voice/style reference
    "_all": ["product_maturity", "product_vision", "future_teams", "judgment_taste"],
    # Chapter-specific relevance
    1: ["product_maturity"],                     # AI Trap ← maturidade de produto
    2: ["stanford_framework"],                   # Momento de Inflexão ← Supernovas/Shooting Stars
    3: ["future_teams", "judgment_taste"],       # Anatomia do AI PM ← habilidades essenciais, taste
    4: ["stanford_framework"],                   # Technical Fluency ← Human Agency Scale
    5: ["user_agency", "product_principles"],    # Discovery ← agência, princípios de decisão
    6: ["product_principles"],                   # Métricas ← princípios orientam métricas
    7: ["user_agency", "stanford_framework"],    # Designing for AI ← agência, HAS
    8: ["high_performance_teams", "future_teams", "technical_to_leadership", "stop_categorizing"],  # Times ← caos→excelência, times futuros, liderança
    9: ["product_principles", "judgment_taste"], # Strategy ← princípios, taste como moat
    10: ["technical_to_leadership", "stop_categorizing", "feminine_leadership_manifesto", "feminine_leadership_paradox"],  # Transformação ← liderança
    11: ["stanford_framework"],                  # Ethics ← HAS
    12: ["judgment_taste", "future_teams", "user_agency"],  # Futuro ← taste, times, agência
}


def _build_substack_context(chapter_num: int, chapter_details: dict) -> str:
    """Build a context section from relevant Substack articles for this chapter."""
    from book_writer.knowledge_base import SUBSTACK_ARTICLES

    relevant = set(SUBSTACK_CHAPTER_MAP.get("_all", []))
    relevant.update(SUBSTACK_CHAPTER_MAP.get(chapter_num, []))

    if not relevant:
        return ""

    lines = [
        "\n## CONTEÚDO AUTORAL DA AUTORA (SUBSTACK) — USE COMO FONTE PRIMÁRIA\n",
        "Estes artigos publicados pela Fernanda Faria no Substack (fefaria.substack.com) contêm",
        "frameworks autorais, voz, cases e citações que DEVEM ser incorporados ao capítulo.",
        "Pesquise dados externos para complementar, mas o núcleo intelectual é este:\n",
    ]

    for slug in sorted(relevant):
        article = SUBSTACK_ARTICLES.get(slug)
        if not article:
            continue
        lines.append(f"### {article['title']} ({article['date']})")

        # Frameworks
        if "frameworks" in article:
            for fw_name, fw_data in article["frameworks"].items():
                if isinstance(fw_data, dict):
                    lines.append(f"**Framework: {fw_name}**")
                    if "description" in fw_data:
                        lines.append(f"- {fw_data['description']}")
                    if "levels" in fw_data:
                        for lvl_name, lvl_data in fw_data["levels"].items():
                            if isinstance(lvl_data, dict):
                                lines.append(f"  - Nível {lvl_name}: {lvl_data.get('name', lvl_data.get('motto', ''))}")
                                if "traits" in lvl_data:
                                    for t in lvl_data["traits"][:2]:
                                        lines.append(f"    - {t}")
                    if "pillars" in fw_data:
                        for p in fw_data["pillars"][:3]:
                            lines.append(f"  - Pilar: {p}")
                    if "zones" in fw_data:
                        for zone_name, zone_desc in fw_data["zones"].items():
                            lines.append(f"  - Zona {zone_name}: {zone_desc}")

        # Framework (singular)
        if "framework" in article:
            fw = article["framework"]
            if isinstance(fw, dict):
                lines.append(f"**Framework: {fw.get('name', '')}**")
                if "components" in fw:
                    for k, v in fw["components"].items():
                        lines.append(f"- {k}: {str(v)[:150]}")

        # Cases
        if "cases" in article:
            lines.append("**Cases citados:**")
            for case_name, case_desc in article["cases"].items():
                lines.append(f"- {case_name}: {str(case_desc)[:200]}")

        # Core thesis
        if "core_thesis" in article:
            lines.append(f"**Tese:** {article['core_thesis'][:200]}")

        # Key insights
        if "key_insights" in article:
            lines.append("**Insights principais:**")
            for k, v in article["key_insights"].items():
                lines.append(f"- {k}: {str(v)[:150]}")

        if "key_concepts" in article:
            lines.append("**Conceitos-chave:**")
            for k, v in article["key_concepts"].items():
                lines.append(f"- {k}: {str(v)[:150]}")

        if "phases" in article:
            lines.append("**Fases:**")
            for k, v in article["phases"].items():
                lines.append(f"- Fase {k}: {v.get('name', '')} — {v.get('focus', '')[:120]}")

        # Key quotes (voice samples)
        if "key_quotes" in article:
            lines.append("**Citações autorais (voz da Fernanda):**")
            for q in article["key_quotes"][:3]:
                lines.append(f"> {q}")

        lines.append("")

    return "\n".join(lines)


def _build_voice_context(brief=None) -> str:
    """Build voice style reference that guides the Writer."""
    from book_writer.knowledge_base import FERNANDA_VOICE

    v = FERNANDA_VOICE
    lines = [
        "\n## GUIA DE VOZ E ESTILO (Fernanda Faria)\n",
        "**Aberturas características:**",
    ]
    for opening in v["signature_openings"]:
        lines.append(f"- {opening}")

    lines.append("\n**Marcadores de tom:**")
    for tone in v["tone_markers"]:
        lines.append(f"- {tone}")

    lines.append("\n**Estrutura de capítulo:**")
    for step in v["structural_pattern"]:
        lines.append(f"- {step}")

    lines.append(f"\n**Vocabulário que USA:** {', '.join(v['vocabulary']['uses'])}")
    lines.append(f"**Vocabulário que EVITA:** {', '.join(v['vocabulary']['avoids'])}")

    return _scrub("\n".join(lines), brief)


# ═══════════════════════════════════════════════════════════════════════════
# RESEARCHER
# ═══════════════════════════════════════════════════════════════════════════

def node_researcher(state: dict) -> dict:
    """Pesquisa fontes, dados, cases e Product Compass para o capítulo alvo.

    Output salvo em state['research_material'].
    """
    from book_writer.knowledge_base import CHAPTER_DETAILS, SUBSTACK_ARTICLES, FERNANDA_VOICE, PODCASTS

    model = _get_model(temperature=0.3).bind_tools(ALL_TOOLS)

    chapter_num = state.get("target_chapter", 7)
    chapter_info, _brief = _resolve_chapter_info(state)
    chapter_details = CHAPTER_DETAILS.get(chapter_num, {})
    book_block = _book_context_block(state, chapter_num)
    research_block = _research_block(state)

    # Literatura acadêmica já levantada (notas de pesquisa do livro), se o brief apontar
    notes_txt = ""
    notes_path = (state.get("brief") or {}).get("research_notes", "")
    if notes_path:
        _np = PROJECT_ROOT / notes_path
        if _np.exists():
            notes_txt = _np.read_text(encoding="utf-8")
            print(f"[Researcher] Literatura já levantada carregada: {notes_path} ({len(notes_txt)} caracteres)")
    notes_block = ""
    if notes_txt:
        notes_block = f"""LITERATURA ACADÊMICA JÁ LEVANTADA (fonte primária — pesquise só pra VERIFICAR números e COMPLETAR lacunas):
---
{notes_txt}
---
"""

    # Build chapter-specific research directives
    detail_sections = ""
    if chapter_details:
        detail_sections = "\n## DIRETRIZES ESPECÍFICAS DESTE CAPÍTULO\n"
        detail_sections += f"Premissa: {chapter_details.get('premise', '')}\n\n"
        for i, sec in enumerate(chapter_details.get("sections", []), 1):
            detail_sections += f"### Seção {i}: {sec['name']}\n{sec['focus']}\n"
            if sec.get("subsections"):
                for sub in sec["subsections"]:
                    detail_sections += f"- {sub}\n"
            detail_sections += "\n"
        if chapter_details.get("product_compass_refs"):
            detail_sections += "**Referências Product Compass a priorizar:**\n"
            for ref in chapter_details["product_compass_refs"]:
                detail_sections += f"- {ref}\n"
            detail_sections += "\n"

    # Build Substack content injection — relevant articles for book writing
    substack_context = _build_substack_context(chapter_num, chapter_details)

    # Build voice reference for the Writer (used later, but injected here for context continuity)
    voice_context = _build_voice_context(state.get("brief"))

    prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: RESEARCHER — Pesquisa de fontes para o livro

VOCÊ É O PESQUISADOR. Sua missão: coletar material bruto, verificável e ATUALIZADO
(ano {CURRENT_YEAR}, nada anterior a {FRESHNESS_CUTOFF} sem justificativa) para o capítulo:

**Capítulo {chapter_num}: {chapter_info.get('chapter_title', '')}**
**Parte {chapter_info.get('part')}: {chapter_info.get('part_title', '')}**
**Tema:** {chapter_info.get('part_epigraph', '')}
{detail_sections}
{substack_context}

{notes_block}

{book_block}

{research_block}
"""

    research_msgs = [
        SystemMessage(content=f"{BOOK_SYSTEM}\n\nUse SEMPRE search_sources (fonte única) e extract_urls para pesquisar antes de responder."),
        HumanMessage(content=prompt),
    ]

    research_result = _invoke_with_tools(model, research_msgs, max_tool_rounds=5)
    print(f"[Researcher] Pesquisa concluída ({len(research_result)} caracteres)")

    return {
        "research_material": research_result,
        "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
        "chapter_draft": state.get("chapter_draft", ""),
        "revision_count": state.get("revision_count", 0),
        "messages": [AIMessage(content=f"[Researcher] Material de pesquisa coletado para Capítulo {chapter_num}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# FACT SHEET
# ═══════════════════════════════════════════════════════════════════════════

def node_factsheet(state: dict) -> dict:
    """Extrai a folha de fatos (fatos verificáveis + fonte) do research.

    É o repositório ÚNICO de números/claims que o Writer pode usar (inversão:
    verifica ANTES de compor). Output em state['factsheet'].
    """
    model = _get_model(temperature=0.1)

    chapter_num = state.get("target_chapter", 1)
    research = state.get("research_material", "")
    chapter_info, _brief = _resolve_chapter_info(state)

    prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: FACT SHEET — Folha de fatos verificáveis

Transforme o material de pesquisa em uma FOLHA DE FATOS estruturada. Este é o
ÚNICO repositório de números, estatísticas, datas, cases nomeados e claims que
o Writer poderá usar no capítulo. Rigor nasce aqui: se não está na folha, não
entra no livro.

**Capítulo {chapter_num}: {chapter_info.get('chapter_title', '')}**

MATERIAL DE PESQUISA:
---
{research[:15000]}
---

REGRAS (OBRIGATÓRIAS):
1. Extraia TODO número, %, estatística, data, case nomeado (empresa + fonte) e claim verificável.
2. Cada fato com: claim (frase curta e exata), source (empresa/estudo/autor), url (se houver), year.
3. NÃO invente. NÃO arredonde. Só o que está literalmente no material de pesquisa.
4. Se o material NÃO tem número com fonte, deixe a lista MENOR — melhor 5 fatos sólidos que 20 soltos.
5. Marque como "vago" qualquer número por extenso ("dezenas", "centenas") em vez de incluí-lo como exato.

Retorne APENAS JSON válido (sem markdown, sem comentários):
{{"facts": [{{"claim": "...", "source": "...", "url": "...", "year": "..."}}]}}
"""

    result = model.invoke([
        SystemMessage(content=BOOK_SYSTEM),
        HumanMessage(content=prompt),
    ])
    factsheet = result.content if hasattr(result, "content") else str(result)

    print(f"[FactSheet] Folha de fatos criada ({len(factsheet)} caracteres)")

    return {
        "factsheet": factsheet,
        "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
        "chapter_draft": state.get("chapter_draft", ""),
        "revision_count": state.get("revision_count", 0),
        "messages": [AIMessage(content=f"[FactSheet] Folha de fatos extraída para Capítulo {chapter_num}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# STRATEGIST
# ═══════════════════════════════════════════════════════════════════════════

def node_strategist(state: dict) -> dict:
    """Analisa o research, define outline detalhado e Curiosity Schedule.

    Output salvo em state['chapter_outline'] e state['curiosity_plan'].
    """
    model = _get_model(temperature=0.3)

    chapter_num = state.get("target_chapter", 7)
    research = state.get("research_material", "")
    chapter_info, _brief = _resolve_chapter_info(state)

    # Pega contexto de curiosity
    curiosity_ctx = to_prompt_context(chapter_num)
    gaps_to_plant = get_gaps_planted_in(chapter_num)
    gaps_to_resolve = get_gaps_to_resolve(chapter_num)
    outstanding = get_outstanding_gaps(chapter_num - 1)

    # Memória do livro: digests dos capítulos anteriores (não repetir/contradizer)
    from book_writer import digest
    prior_digest = digest.load_prior(state.get("brief"), chapter_num)

    prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: STRATEGIST — Estrategista de Conteúdo e Curiosity Scheduler

VOCÊ É O ESTRATEGISTA. Sua missão: transformar pesquisa bruta em um outline
detalhado com agenda de revelação (Curiosity Schedule) para o capítulo.

**Capítulo {chapter_num}: {chapter_info.get('chapter_title', '')}**
**Parte {chapter_info.get('part')}: {chapter_info.get('part_title', '')}**

MATERIAL DE PESQUISA:
---
{research[:12000]}
---

{curiosity_ctx}

{prior_digest}

CURIOSITY SCHEDULER:
- Gaps a PLANTAR neste capítulo: {len(gaps_to_plant)} gaps
- Gaps a RESOLVER neste capítulo: {len(gaps_to_resolve)} gaps
- Gaps em aberto (NÃO resolver): {len(outstanding)} gaps

ESTRUTURA DE CAPÍTULO (obrigatória, conforme Style Guide):
1. CENA DE ABERTURA (200-400 palavras) — diálogo real, data, nome, contexto
2. DEFINIÇÃO DO PROBLEMA (300-500 palavras) — nomeia o conceito, conecta com caps anteriores
3. FRAMEWORK / COMPONENTES (800-1200 palavras) — framework autoral com nome próprio
4. CASOS REAIS (600-1000 palavras) — 3 casos: Situação → Problema → Solução → Resultados
5. GUIA PRÁTICO (400-600 palavras) — timeline 30/60/90 dias
6. MÉTRICAS DE SUCESSO (200-400 palavras) — KPIs específicos
7. FECHAMENTO COM GANCHO (200-300 palavras) — resume + planta gap próximo cap

SUA MISSÃO (crie um outline detalhado):

## 1. PREMISSA CENTRAL DO CAPÍTULO
Qual é a tese única deste capítulo que nenhum outro livro de produto aborda?
(1-2 frases)

## 2. CURIOSITY SCHEDULE
a) GAPS A RESOLVER: como cada gap pendente será respondido neste capítulo
b) GAPS A PLANTAR: 2-3 perguntas que este capítulo planta e responde depois
c) ESCALATION: após resolver um gap, qual pergunta MAIOR surge?

## 3. OUTLINE DETALHADO
Para cada uma das 7 seções:
- Gancho/tese da seção
- 3-5 bullet points de conteúdo
- Que dados/cases do research usar
- Onde entra Product Compass
- Onde plantar/resolver gaps

## 4. NOMEAÇÃO DE FRAMEWORKS
- Que framework autoral este capítulo introduz?
- Nome memorável + acrônimo (ex: ESCAPE, 7 Sinais)
- Quantos componentes/elementos?

## 5. PONTES ENTRE CAPÍTULOS
- Conexão com Cap {chapter_num - 1}: o que foi prometido que precisa ser entregue?
- Conexão com Cap {chapter_num + 1}: o que deixar em aberto como gancho?

## 6. GAPS EM ABERTO (NÃO RESOLVER)
Liste os gaps que estão em aberto de capítulos anteriores e que NÃO devem ser
resolvidos aqui (pertencem a capítulos futuros):
{chr(10).join(f'- {g.id}: {g.question}' for g in outstanding) if outstanding else '- Nenhum'}
"""

    prompt = _scrub(prompt, state.get("brief"))
    result = model.invoke([
        SystemMessage(content=BOOK_SYSTEM),
        HumanMessage(content=prompt),
    ])
    outline = result.content if hasattr(result, "content") else str(result)

    print(f"[Strategist] Outline criado ({len(outline)} caracteres)")

    return {
        "chapter_outline": outline,
        "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
        "chapter_draft": state.get("chapter_draft", ""),
        "revision_count": state.get("revision_count", 0),
        "messages": [AIMessage(content=f"[Strategist] Outline e Curiosity Schedule definidos para Capítulo {chapter_num}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# WRITER
# ═══════════════════════════════════════════════════════════════════════════

def node_writer(state: dict) -> dict:
    """Escreve o capítulo completo seguindo outline, style guide e curiosity registry.

    Output salvo em state['chapter_draft'] e state['draft_path'].
    """
    model = _get_model(temperature=0.8)
    research_model = _get_model(temperature=0.4).bind_tools(ALL_TOOLS)

    chapter_num = state.get("target_chapter", 7)
    research = state.get("research_material", "")
    outline = state.get("chapter_outline", "")
    revision_count = state.get("revision_count", 0)
    chapter_info, _brief = _resolve_chapter_info(state)

    # ── REVISION MODE ───────────────────────────────────────────────────
    if revision_count > 0:
        existing_draft = state.get("chapter_draft", "")
        editor_feedback = state.get("editor_feedback", "")

        print(f"[Writer] Modo REVISÃO (ciclo {revision_count})")

        # Fase 1: Pesquisa adicional para corrigir problemas
        research_prompt = f"""{BOOK_SYSTEM}

MODO: PESQUISA PARA REVISÃO.

FEEDBACK DO EDITOR-CHEFE:
{editor_feedback}

CAPÍTULO ATUAL (problemático):
{existing_draft[:4000]}

Busque fontes e dados que corrijam os problemas apontados pelo Editor-Chefe.
Use search_web para cada ponto específico. Seja cirúrgico."""

        research_msgs = [
            SystemMessage(content=f"{BOOK_SYSTEM}\n\nUse SEMPRE as ferramentas para pesquisar."),
            HumanMessage(content=research_prompt),
        ]
        research_result = _invoke_with_tools(research_model, research_msgs, max_tool_rounds=3)

        # Fase 2: Reescrever corrigindo
        write_prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: WRITER — Modo REVISÃO (ciclo {revision_count})

{_style_guide_for(state)[:2000]}

CAPÍTULO ATUAL:
---
{existing_draft}
---

PESQUISA ADICIONAL (dados corrigidos):
{research_result[:4000]}

FEEDBACK DO EDITOR-CHEFE:
{editor_feedback}

INSTRUÇÕES:
1. Corrija TODOS os problemas apontados pelo Editor-Chefe
2. Use os dados da pesquisa adicional onde necessário
3. Mantenha o que está bom — reescreva apenas o que precisa ser corrigido
4. Preserve estrutura, voz, frameworks e seções intactas
5. NÃO encurte — o capítulo deve continuar completo (~3000-4000 palavras)
6. O texto de saída deve ter aproximadamente o MESMO TAMANHO do original ({len(existing_draft)} caracteres)

Retorne o capítulo COMPLETO corrigido em Markdown."""

        write_prompt = _scrub(write_prompt, state.get("brief"))
        result = model.invoke([
            SystemMessage(content=BOOK_SYSTEM),
            HumanMessage(content=write_prompt),
        ])

        draft = result.content if hasattr(result, "content") else str(result)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        draft_path = f"output/capitulo-{chapter_num:02d}-r{revision_count}-{timestamp}.md"
        Path(f"{PROJECT_ROOT}/{draft_path}").parent.mkdir(parents=True, exist_ok=True)
        Path(f"{PROJECT_ROOT}/{draft_path}").write_text(draft, encoding="utf-8")

        print(f"[Writer] Revisão (ciclo {revision_count}) salva em {draft_path}")

        return {
            "chapter_draft": draft,
            "draft_path": draft_path,
            "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
            "revision_count": state.get("revision_count", 0),
            "messages": [AIMessage(content=f"[Writer] Capítulo {chapter_num} revisado (ciclo {revision_count}): {draft_path}")],
        }

    # ── FIRST DRAFT MODE ────────────────────────────────────────────────
    print(f"[Writer] Modo PRIMEIRA VERSÃO — Capítulo {chapter_num}")

    # Fase 1: Pesquisa rápida adicional para preencher lacunas
    research_prompt = f"""{BOOK_SYSTEM}

MODO: PESQUISA PRÉ-ESCRITA.

Capítulo {chapter_num}: {chapter_info.get('chapter_title', '')}

OUTLINE:
{outline[:3000]}

Pesquise dados e fatos adicionais para preencher lacunas no outline.
Use search_sources para buscar estatísticas recentes e casos de UX/design para IA.
Seja rápido: 2-3 buscas no máximo."""

    research_msgs = [
        SystemMessage(content=f"{BOOK_SYSTEM}\n\nUse SEMPRE as ferramentas para pesquisar."),
        HumanMessage(content=research_prompt),
    ]
    extra_research = _invoke_with_tools(research_model, research_msgs, max_tool_rounds=2)

    # ── Folha de fatos (repositório único de números) + claims já refutadas ──
    factsheet = state.get("factsheet", "")
    from book_writer import ledger
    refuted_block = ledger.refuted_text(state.get("brief"))

    # Fase 2: Escrever o capítulo
    write_prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: WRITER — Primeira versão do capítulo

{_style_guide_for(state)}

**Capítulo {chapter_num}: {chapter_info.get('chapter_title', '')}**
**Parte {chapter_info.get('part')}: {chapter_info.get('part_title', '')}**

FOLHA DE FATOS (repositório ÚNICO de números/claims — só use o que está aqui):
---
{factsheet[:8000]}
---

{refuted_block}

MATERIAL DE PESQUISA (contexto):
{research[:12000]}

PESQUISA ADICIONAL:
{extra_research[:3000]}

OUTLINE DETALHADO:
{outline[:6000]}

CONTEXTO DE CURIOSITY:
{to_prompt_context(chapter_num)}

INSTRUÇÕES CRÍTICAS:

1. **Siga EXATAMENTE a estrutura de 7 seções do Style Guide.**
   Não pule nenhuma. Não invente seções novas.

2. **Voz:** A cena de abertura DEVE seguir o padrão:
   "Era uma [dia] de [mês] de [ano], e [nome], [cargo] de [empresa REAL], ..."
   Empresa REAL nomeada, ou marque explicitamente "caso composto/ilustrativo".
   NUNCA apresente cena anônima como fato. NUNCA comece com definição.

3. **Frameworks:** Se o capítulo introduz um framework novo, CRIE um nome
   memorável + acrônimo + componentes numerados (próprio deste livro).

4. **RIGOR FACTUAL — DADOS-PRIMEIRO (OBRIGATÓRIO, reprova sem isso):**
   - TODO número/métrica deve vir LITERALMENTE da FOLHA DE FATOS acima, com fonte (empresa, relatório, ano). Você não inventa números.
   - Se um número NÃO está na FOLHA DE FATOS, NÃO o escreva. Escreva a frase sem o número (ex: "um percentual alto") ou omita o dado.
   - NUNCA invente número redondo. NUNCA troque a métrica (GRR ≠ NRR, MAU ≠ DAU, MRR ≠ receita).
   - CASOS: empresa REAL + fonte (URL, ano). Caso sem fonte = marque explicitamente "caso ilustrativo/composto".
   - SEMPRE cite fonte + ano entre parênteses.

5. **Product Compass:** Integre naturalmente os insights do Pawel Huryn onde
   forem relevantes (especialmente: Intelligent Interface Sense, Context Depth,
   AI prototyping stack).

6. **Curiosity:** Plante os gaps designados. Resolva os gaps pendentes.
   Após resolver um gap, crie um NOVO gap (escalate).

7. **Português brasileiro autêntico (CRÍTICO):**
   - Zero em-dashes (—). Use vírgula ou dois-pontos.
   - Zero ALL CAPS. Use **negrito** para ênfase.
   - Tom direto, executivo, sem autoajuda.
   - PROIBIDO: "In today's fast-paced landscape/environment", "Not only... but also"
   - PROIBIDO: "It is worth noting", "Interestingly", "Moreover", "Furthermore", "In addition"
   - PROIBIDO: "research shows" / "studies indicate" sem fonte específica
   - PROIBIDO: "In conclusion", "To sum up", "Let's dive in", "In this section"
   - PROIBIDO: "É importante ressaltar", "Outro ponto importante", "Em um mundo cada vez mais..."
   - PROIBIDO: "Podemos afirmar", "Vale destacar", "Concluindo"
   - USE vocabulário coloquial: "bora", "tá", "a gente", "troço", "pera"
   - USE perguntas diretas no ar em vez de fechamento previsível

8. **Extensão:** 3000-4000 palavras. Capítulo completo, não resumo.

ESCREVA O CAPÍTULO COMPLETO EM MARKDOWN:"""

    write_prompt = _scrub(write_prompt, state.get("brief"))
    result = model.invoke([
        SystemMessage(content=BOOK_SYSTEM),
        HumanMessage(content=write_prompt),
    ])

    draft = result.content if hasattr(result, "content") else str(result)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    draft_path = f"output/capitulo-{chapter_num:02d}-v1-{timestamp}.md"
    Path(f"{PROJECT_ROOT}/{draft_path}").parent.mkdir(parents=True, exist_ok=True)
    Path(f"{PROJECT_ROOT}/{draft_path}").write_text(draft, encoding="utf-8")

    print(f"[Writer] Primeira versão salva em {draft_path} ({len(draft)} caracteres)")

    return {
        "chapter_draft": draft,
        "draft_path": draft_path,
        "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
        "revision_count": state.get("revision_count", 0),
        "messages": [AIMessage(content=f"[Writer] Capítulo {chapter_num} escrito: {draft_path}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# FACT-CHECKER
# ═══════════════════════════════════════════════════════════════════════════

def node_fact_checker(state: dict) -> dict:
    """Verifica claims factuais do capitulo contra fontes e pesquisa.

    Output salvo em state['factcheck_report'].
    """
    model = _get_model(temperature=0.1).bind_tools(ALL_TOOLS)

    chapter_num = state.get("target_chapter", 7)
    draft = state.get("chapter_draft", "")
    research = state.get("research_material", "")

    print(f"[FactChecker] Verificando claims do Capitulo {chapter_num}...")

    prompt = f"""{BOOK_SYSTEM}

## FUNCAO: FACT-CHECKER — Verificacao factual do capitulo

Voce e o FactChecker. Sua unica funcao: verificar a exatidao factual de CADA
afirmacao verificavel no texto. Voce NAO avalia estilo, NAO sugere melhorias
de escrita. So fatos.

CAPITULO {chapter_num}:

{_style_guide_for(state)[:500]}

TEXTO PARA VERIFICAR (capitulo completo):
---
{draft[:20000]}
---

PESQUISA DE REFERENCIA:
{research[:3000]}

INSTRUCOES:
1. USE search_sources (fonte única: Perplexity com citação, cai pra OpenAlex/Google) para
   VERIFICAR na web cada claim com numero, ano, nome de empresa ou estatistica.
   NAO classifique sem verificar.
2. Para cada claim, classifique: verified / outdated / wrong / unverifiable
3. REGRA DESTRUTIVA (OBRIGATÓRIA — é a essência do seu trabalho):
   - NÚMERO SEM FONTE VERIFICÁVEL → REMOVA o número. Reescreva a frase sem ele,
     mantendo o sentido qualitativo (ex: "82% de NRR" → "patamar de NRR").
   - MÉTRICA ERRADA (wrong) → corrija com o dado real + fonte verificada.
   - MÉTRICA DESATUALIZADA (outdated) → atualize com o dado recente + fonte.
   - CASO/FONTE VAGA sem URL → remova o dado específico OU adicione a fonte real.
   - Ao final, NENHUM número pode ficar sem fonte rastreável.

FORMATO DA RESPOSTA:

## RESUMO
- Total de claims verificadas: N
- Verified: N / Outdated: N / Wrong: N / Unverifiable: N

## CORRECOES_JSON
[{{"old": "trecho EXATO do capitulo com numero sem fonte", "new": "trecho reescrito SEM o numero (ou corrigido + fonte)"}}]

REGRAS DO JSON:
- "old" = trecho UNICO que aparece literalmente no texto do capitulo.
- "new" = reescrita que remove o numero sem fonte OU corrige com fonte real.
- Sem correcoes = retorne [].
"""

    prompt = _scrub(prompt, state.get("brief"))
    msgs = [
        SystemMessage(content=f"{BOOK_SYSTEM}\n\nUse search_sources (fonte única com citação) e extract_urls para verificar cada claim antes de classificar."),
        HumanMessage(content=prompt),
    ]
    report = _invoke_with_tools(model, msgs, max_tool_rounds=5)
    print(f"[FactChecker] Relatorio gerado ({len(report)} caracteres)")

    return {
        "factcheck_report": report,
        "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
        "chapter_draft": state.get("chapter_draft", ""),
        "revision_count": state.get("revision_count", 0),
        "messages": [AIMessage(content=f"[FactChecker] Verificacao concluida para Capitulo {chapter_num}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# COPY EDITOR
# ═══════════════════════════════════════════════════════════════════════════

def node_copy_editor(state: dict) -> dict:
    """Revisa gramática, clareza, voz, flow e terminologia em 2 fases.

    FASE A (correções factuais): extrai old→new pairs do FactChecker e
    aplica via patch(), evitando que o modelo resuma o texto completo.

    FASE B (estilo): um ÚNICO passe combinado (Gramática + Clareza + Voz +
    Flow + Terminologia) com instrução explícita de não resumir.

    Output salvo em state['chapter_draft'] (atualizado) e
    state['copy_editor_report'].
    """
    chapter_num = state.get("target_chapter", 7)
    draft = state.get("chapter_draft", "")
    factcheck_report = state.get("factcheck_report", "")

    original_len = len(draft)
    print(f"[CopyEditor] Iniciando (original: {original_len} caracteres)...")

    # ── FASE A: Correções destrutivas do FactChecker (JSON direto) ─────
    if factcheck_report:
        draft, applied = _apply_corrections_json(factcheck_report, draft)
        print(f"[CopyEditor] FASE A: {applied} correcoes destrutivas aplicadas")

    # ── FASE B: Passe unico de estilo ──────────────────────────────────
    style_model = _get_model(temperature=0.2)

    combined_prompt = f"""{BOOK_SYSTEM}

## FUNCAO: COPY EDITOR — Revisao Completa (Gramatica + Clareza + Voz + Flow + Terminologia)

{_style_guide_for(state)[:2500]}

Voce e o Copy Editor do livro "AI Product Management". Sua funcao e revisar
o texto COMPLETO abaixo aplicando TODAS as seguintes dimensoes DE UMA VEZ:

1. GRAMATICA: concordancia, pontuacao, ortografia, acentuacao, crase
2. CLAREZA: frases >30 palavras → quebre; termos ambiguos → especifique;
   paragrafos longos (>6 frases) → quebre; jargao sem explicacao → defina
3. VOZ: tom direto e executivo; zero autoajuda; zero "espero que esteja bem",
   "jornada", "importante", "interessante"; frases fortes; sem bullshit
4. FLOW: cada secao conecta naturalmente; pontes explicitas; narrativa fluida;
   gancho final planta curiosidade; sem "alem disso" ou "outro ponto importante"
5. TERMINOLOGIA: consistencia de termos; siglas apos primeira mencao; italico
   na primeira ocorrencia de termos em ingles

TEXTO COMPLETO (CAPITULO {chapter_num}):
---
{draft}
---

CRITICO: RETORNE O TEXTO COMPLETO REVISADO. O texto de saida deve ter
aproximadamente o MESMO TAMANHO do texto de entrada ({len(draft)} caracteres).
NAO RESUMA. NAO OMITA SECOES. NAO CONDENSE. Cada secao, paragrafo e ideia
do original devem estar presentes na saida, apenas com as correcoes aplicadas.
Se o texto original tem 7 secoes, a saida deve ter as mesmas 7 secoes."""

    result = style_model.invoke([
        SystemMessage(content=BOOK_SYSTEM),
        HumanMessage(content=combined_prompt),
    ])
    reviewed = result.content if hasattr(result, "content") else str(result)

    # ── Guard rail: se o modelo encolheu o texto (>30% menor), usa o original ──
    if len(reviewed) < len(draft) * 0.5:
        print(f"[CopyEditor] ALERTA: texto encolheu {len(draft)} → {len(reviewed)} chars ({100*len(reviewed)//max(len(draft),1)}%). Usando original.")
        reviewed = draft
    else:
        print(f"[CopyEditor] FASE B concluida ({len(draft)} → {len(reviewed)} caracteres)")

    # Atualiza o draft
    draft_path = state.get("draft_path", "")
    if draft_path:
        Path(f"{PROJECT_ROOT}/{draft_path}").write_text(reviewed, encoding="utf-8")

    report = f"""Copy Editor Report — Capitulo {chapter_num}
Data: {CURRENT_DATE}
FASE A: correcoes factuais do FactChecker aplicadas
FASE B: passe unico Gramatica+Clareza+Voz+Flow+Terminologia
Original: {original_len} caracteres → Final: {len(reviewed)} caracteres
"""

    print(f"[CopyEditor] Revisao completa. {original_len} → {len(reviewed)} caracteres")

    return {
        "chapter_draft": reviewed,
        "copy_editor_report": report,
        "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
        "revision_count": state.get("revision_count", 0),
        "messages": [AIMessage(content=f"[CopyEditor] Revisao concluida para Capitulo {chapter_num}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# AUTHENTICITY FIXER
# ═══════════════════════════════════════════════════════════════════════════

def node_authenticity_fixer(state: dict) -> dict:
    """Pós-CopyEditor: detecta e corrige 'cara de AI' no texto.

    Usa o evaluator (evals.py) pra medir marcadores de AI voice.
    Se score > AI_THRESHOLD (10), reescreve trechos problemáticos.
    Se score <= 10, passa direto (texto OK).
    """
    from book_writer.evals import diagnose_ai_voice, get_fixer_prompt, AI_THRESHOLD

    chapter_num = state.get("target_chapter", 7)
    draft = state.get("chapter_draft", "")
    original_len = len(draft)

    # total de capítulos do brief, pra regra de vazamento de capítulo
    _brief = state.get("brief")
    max_chapters = len(_brief.get("chapters", [])) if _brief else None

    print(f"[AuthenticityFixer] Iniciando avaliação ({original_len} caracteres)...")

    # Roda o eval
    eval_result = diagnose_ai_voice(draft)

    ai_score = eval_result["ai_score"]
    fernanda_score = eval_result["fernanda_score"]
    decision = eval_result["decision"]

    print(f"[AuthenticityFixer] AI Score: {ai_score}/100, Fernanda: {fernanda_score}/100, Decision: {decision}")

    # Se passou, retorna sem mexer (mas aplica o pós-processamento determinístico)
    if decision == "PASS":
        print(f"[AuthenticityFixer] Texto passa no eval (score {ai_score} <= {AI_THRESHOLD}). Sem alterações.")
        draft = _voice_postprocess(draft, max_chapters)
        return {
            "chapter_draft": draft,
            "eval_result": eval_result,
            "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
            "revision_count": state.get("revision_count", 0),
            "messages": [AIMessage(content=f"[AuthenticityFixer] AI Score {ai_score}/100 — PASSOU")],
        }

    # Prepara o fixer prompt
    fixer_prompt = get_fixer_prompt(draft, eval_result)

    if not fixer_prompt:
        draft = _voice_postprocess(draft, max_chapters)
        return {
            "chapter_draft": draft,
            "eval_result": eval_result,
            "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
            "revision_count": state.get("revision_count", 0),
            "messages": [AIMessage(content=f"[AuthenticityFixer] AI Score {ai_score}/100 — sem prompt de correção")],
        }

    # Chama o modelo pra corrigir
    fix_model = _get_model(temperature=0.15)

    full_prompt = f"""{BOOK_SYSTEM}

## FUNCAO: AUTHENTICITY FIXER

{_style_guide_for(state)[:2000]}

Voce e o guardiao da voz autoral da Fernanda Faria. Sua funcao e eliminar
toda 'cara de AI' do texto abaixo, substituindo padroes de LLM por linguagem
autentica.

{fixer_prompt}

## TEXTO PARA CORRIGIR:

---
{draft[:15000]}
---

## INSTRUCOES CRITICAS:

- CORRIJA APENAS os trechos com problemas detectados
- PRESERVE todo o conteudo: dados, frameworks, cases, estrutura
- O texto de saida deve ter aproximadamente o MESMO TAMANHO ({original_len} caracteres)
- NAO RESUMA. NAO OMITA SECOES.
- Aplique as regras de correcao listadas acima
- Retorne o TEXTO COMPLETO corrigido

TEXTO CORRIGIDO:"""

    result = fix_model.invoke([
        SystemMessage(content=BOOK_SYSTEM),
        HumanMessage(content=full_prompt),
    ])

    fixed = result.content if hasattr(result, "content") else str(result)

    # Post-process determinístico (voz + rigor factual) — SEMPRE
    fixed = _voice_postprocess(fixed, max_chapters)
    
    # Guard rail: se encolheu >40%, usa o original
    if len(fixed) < original_len * 0.6:
        print(f"[AuthenticityFixer] ALERTA: texto encolheu {original_len} → {len(fixed)}. Usando original.")
        fixed = draft
    else:
        # Reavalia após o fix
        post_eval = diagnose_ai_voice(fixed)
        print(f"[AuthenticityFixer] Pós-fix: AI Score {post_eval['ai_score']}/100 "
              f"(era {ai_score}/100), Fernanda {post_eval['fernanda_score']}/100 "
              f"(era {fernanda_score}/100)")
        eval_result = post_eval

    print(f"[AuthenticityFixer] Concluído ({original_len} → {len(fixed)} caracteres)")

    return {
        "chapter_draft": fixed,
        "eval_result": eval_result,
        "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
        "revision_count": state.get("revision_count", 0),
        "messages": [AIMessage(content=f"[AuthenticityFixer] AI Score final: {eval_result['ai_score']}/100")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# VERIFIER
# ═══════════════════════════════════════════════════════════════════════════

def node_verifier(state: dict) -> dict:
    """Lê a FONTE de cada claim numérica do draft e compara com o que a fonte diz.

    Diferente do FactChecker (que julga "tem fonte?"), o Verifier pega a claim,
    a URL citada, faz FETCH (extract_urls) e compara o número com o texto real.
    Fecha o gap de veracidade: "CBA maior produtora" ou "mediana virou média".

    Output: state['verifier_report']; corrige o draft; registra claims no ledger.
    """
    from book_writer import ledger

    model = _get_model(temperature=0.1).bind_tools(ALL_TOOLS)

    chapter_num = state.get("target_chapter", 1)
    draft = state.get("chapter_draft", "")
    brief = state.get("brief")

    print(f"[Verifier] Verificando veracidade das claims do Capítulo {chapter_num}...")

    prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: VERIFIER — Verificação de veracidade contra a fonte real

Você NÃO julga se um número "tem fonte". Você LÊ a fonte citada e compara com o
que ela realmente diz. Seu trabalho: pegar cada claim numérica do capítulo,
buscar a fonte (URL ou '(Fonte, ano)') e confirmar se a fonte SUSTENTA o número.

CAPÍTULO {chapter_num}:
---
{draft[:20000]}
---

PROCEDIMENTO (obrigatório):
1. Liste cada claim numérica/percentual/estatística do texto.
2. Para cada uma, ache a fonte citada perto (URL ou '(Fonte, ano)').
3. Se há URL: use extract_urls para LER o que a página diz e compare o número.
4. Se não há URL mas há '(Fonte, ano)': use search_sources para achar o dado real.
5. Classifique CADA claim:
   - VERIFIED: a fonte sustenta o número (ou o número veio da Folha de Fatos com fonte).
   - UNSUPPORTED: a fonte não sustenta o número, ou não dá pra confirmar.
   - CONTRADICTED: a fonte diz OUTRO número (ex: média vs mediana, GRR vs NRR).

FORMATO DA RESPOSTA:

## RESUMO
- Claims verificadas: N (VERIFIED N / UNSUPPORTED N / CONTRADICTED N)

## VEREDICTOS_JSON
[{{"claim": "a claim exata", "verdict": "verified|unsupported|contradicted", "source": "fonte", "url": "url"}}]

## CORRECOES_JSON
[{{"old": "trecho EXATO do capítulo", "new": "trecho corrigido OU sem o número"}}]

REGRAS:
- UNSUPPORTED/CONTRADICTED → corrija em CORRECOES_JSON (remova o número ou corrija com o dado real + fonte).
- VERIFIED → não precisa de correção.
- "old" precisa aparecer LITERALMENTE no capítulo.
- Sem correções = retorne [].
"""

    prompt = _scrub(prompt, brief)
    msgs = [
        SystemMessage(content=f"{BOOK_SYSTEM}\n\nUse extract_urls (para LER a fonte citada) e search_sources (para achar o dado real)."),
        HumanMessage(content=prompt),
    ]
    report = _invoke_with_tools(model, msgs, max_tool_rounds=5)
    print(f"[Verifier] Relatório gerado ({len(report)} caracteres)")

    # Aplica correções destrutivas
    draft, applied = _apply_corrections_json(report, draft)
    print(f"[Verifier] {applied} correções aplicadas")

    # Registra veredictos no ledger
    verdicts = []
    vm = re.search(r'## VEREDICTOS_JSON\s*(.*)', report, re.DOTALL)
    if vm:
        varr = re.search(r'\[.*\]', vm.group(1), re.DOTALL)
        if varr:
            try:
                verdicts = json.loads(varr.group(0))
            except Exception:
                verdicts = []
    if verdicts:
        for v in verdicts:
            v.setdefault("chapter", chapter_num)
        ledger.register(brief, verdicts)
        print(f"[Verifier] {len(verdicts)} claims registradas no ledger")

    # Salva o draft corrigido
    draft_path = state.get("draft_path", "")
    if draft_path:
        Path(f"{PROJECT_ROOT}/{draft_path}").write_text(draft, encoding="utf-8")

    return {
        "chapter_draft": draft,
        "verifier_report": report,
        "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
        "revision_count": state.get("revision_count", 0),
        "messages": [AIMessage(content=f"[Verifier] Veracidade verificada para Capítulo {chapter_num}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# EDITOR-CHEFE
# ═══════════════════════════════════════════════════════════════════════════

def node_editor_chefe(state: dict) -> dict:
    """Gatekeeper final. Decide: APPROVE, MINOR, ou REVISE.

    Output: state['editor_decision'], state['editor_feedback'].
    """
    model = _get_model(temperature=0.2)

    chapter_num = state.get("target_chapter", 7)
    draft = state.get("chapter_draft", "")
    copy_report = state.get("copy_editor_report", "")
    revision_count = state.get("revision_count", 0)

    prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: EDITOR-CHEFE — Gatekeeper de Qualidade

{_style_guide_for(state)[:2000]}

Você é o Editor-Chefe do livro "AI Product Management". Sua função é aprovar
ou rejeitar capítulos baseado em critérios objetivos de qualidade.

CAPÍTULO {chapter_num} PARA AVALIAÇÃO:
---
{draft[:10000]}
---

COPY EDITOR REPORT:
{copy_report}

CRITÉRIOS DE AVALIAÇÃO (cada item: APROVADO ou REPROVADO):

1. ESTRUTURA (as 7 seções estão presentes?)
   - [ ] Cena de abertura com gancho autobiográfico
   - [ ] Definição do problema
   - [ ] Framework autoral com componentes
   - [ ] Casos reais (≥3)
   - [ ] Guia prático (30/60/90 dias)
   - [ ] Métricas de sucesso
   - [ ] Fechamento com gancho para próximo capítulo

2. VOZ (consistente com Style Guide?)
   - [ ] Tom direto, executivo, sem autoajuda
   - [ ] Zero em-dashes (—)
   - [ ] Zero ALL CAPS
   - [ ] Português brasileiro correto

3. CONTEÚDO
   - [ ] Framework autoral nomeado (com acrônimo)?
   - [ ] Dados atualizados ({CURRENT_YEAR}) com fontes?
   - [ ] Product Compass integrado onde relevante?
   - [ ] Curiosity gaps plantados/resolvidos corretamente?

4. EXTENSÃO E PROFUNDIDADE
   - [ ] 3000-4000 palavras?
   - [ ] Profundidade suficiente (não é resumo)?

DECISÃO FINAL:

Escolha UMA:

**APPROVE** — Capítulo está pronto. Todos os critérios atendidos.
**MINOR** — Pequenos ajustes. Listar correções pontuais (máx 3).
**REVISE** — Problemas estruturais. Devolver ao Writer com feedback detalhado.

Se REVISE (ciclo {revision_count + 1}/3):
- Descreva EXATAMENTE o que está errado (não "melhorar o tom" — diga qual frase, por que)
- Priorize: o que corrigir PRIMEIRO
- Se este é o ciclo 3, considere APPROVE com ressalvas (limite de revisões)

Se APPROVE:
- Destaque 1-2 pontos fortes do capítulo

FORMATO DA RESPOSTA:

DECISÃO: [APPROVE|MINOR|REVISE]
JUSTIFICATIVA: [1 parágrafo]
FEEDBACK: [específico e acionável]"""

    prompt = _scrub(prompt, state.get("brief"))
    result = model.invoke([
        SystemMessage(content=BOOK_SYSTEM),
        HumanMessage(content=prompt),
    ])

    feedback = result.content if hasattr(result, "content") else str(result)

    # Extrai decisão
    decision = "APPROVE"
    if "REVISE" in feedback.upper():
        decision = "REVISE"
    elif "MINOR" in feedback.upper():
        decision = "MINOR"

    # Se já revisou 3 vezes, força APPROVE
    if revision_count >= 3:
        decision = "APPROVE"
        feedback = f"[APROVADO AUTOMATICAMENTE após {revision_count} revisões]\n\n{feedback}"

    print(f"[EditorChefe] Decisão: {decision} (ciclo {revision_count + 1})")

    # Memória do livro: grava digest do capítulo quando aprovado (não em REVISE)
    if decision in ("APPROVE", "MINOR"):
        from book_writer import digest
        chapter_info, _ = _resolve_chapter_info(state)
        digest.write(state.get("brief"), chapter_num,
                     chapter_info.get("chapter_title", ""), state.get("factsheet", ""))
        print(f"[EditorChefe] Digest do Capítulo {chapter_num} gravado na memória do livro")

    return {
        "editor_decision": decision,
        "editor_feedback": feedback,
        "target_chapter": state.get("target_chapter", 0),
        "brief": state.get("brief"),
        "max_revisions": state.get("max_revisions", 3),
        "chapter_draft": state.get("chapter_draft", ""),
        "revision_count": revision_count + 1 if decision == "REVISE" else revision_count,
        "messages": [AIMessage(content=f"[EditorChefe] Decisão: {decision} para Capítulo {chapter_num}")],
    }
