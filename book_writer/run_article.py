"""Article Writer — CLI para gerar artigos no formato Substack.

Usa o mesmo pipeline multiagente (Researcher → Strategist → Writer → FactChecker → CopyEditor)
mas com prompts adaptados para artigo (1500-2000 palavras, tom Substack).

Uso:
  $ cd ~/code/feproduto
  $ python -m book_writer.run_article --topic julgamento-vs-dados
  $ python -m book_writer.run_article --topic lideranca-feminina
  $ python -m book_writer.run_article --topic maturidade-produto
  $ python -m book_writer.run_article --list
"""

from __future__ import annotations

import argparse
import sys
import re
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from book_writer.tools import _get_model, _invoke_with_tools, ALL_TOOLS
from book_writer.article_topics import get_topic, list_topics, get_research_context, get_writer_context
from book_writer.style_guides import ARTICLE_STYLE_GUIDE

CURRENT_YEAR = datetime.now().year

ARTICLE_SYSTEM = f"""Voce e parte do sistema multiagente de producao de artigos da Fernanda Faria
para o Substack The Product Compass Brasil. Ano corrente: {CURRENT_YEAR}.

Seu papel e pesquisar, estruturar e escrever artigos no tom caracteristico da autora:
direto, coloquial, com humor seco, antipatico com hype. Sem jargao de consultoria.

Regras:
- Sempre escreva em portugues do Brasil.
- NUNCA use em-dashes (—). Use virgula, dois-pontos ou ponto.
- NUNCA use ALL CAPS para enfase.
- Toda afirmacao factual precisa de fonte + ano entre parenteses.
- Paragrafo curto (max 3 linhas). Frase curta.
- Artigo completo: 1500-2000 palavras. Nao e resumo."""


def _sanitize_filename(s: str) -> str:
    """Converte string em nome de arquivo seguro."""
    return re.sub(r"[^a-z0-9_-]", "-", s.lower().strip())[:80]


def run_article_pipeline(topic_id: str, max_revisions: int = 2) -> str:
    """Roda o pipeline completo para gerar um artigo.

    Pipeline: research → strategy → write → factcheck → copyedit.
    Lightweight: sem grafo LangGraph (o artigo nao tem ciclo de revisao complexo).

    Returns path to output file.
    """
    topic = get_topic(topic_id)
    if not topic:
        raise ValueError(f"Topico '{topic_id}' nao encontrado. Use --list para ver disponiveis.")

    model_writer = _get_model(temperature=0.85)
    model_researcher = _get_model(temperature=0.3).bind_tools(ALL_TOOLS)
    model_cold = _get_model(temperature=0.1)

    print(f"\n{'='*60}")
    print(f"PIPELINE DE ARTIGO: {topic['title']}")
    print(f"Formato: {topic['format']} | Alvo: {topic['target_words']} palavras")
    print(f"{'='*60}\n")

    # ── FASE 1: RESEARCH ──────────────────────────────────────────────
    print("[Researcher] Coletando fontes e dados...")
    research_prompt = f"""{ARTICLE_SYSTEM}

TOPICO: {topic['title']}
TESE CENTRAL: {topic['core_thesis']}

{get_research_context(topic_id)}

Use search_web para buscar cada topico da lista acima.
Colete: estatisticas recentes, citacoes de especialistas, cases brasileiros,
dados de mercado, frameworks relevantes.

Seja minucioso: faca pelo menos 8 buscas. Extraia URL das fontes mais promissoras.
Retorne uma sintese organizada por tema, com fonte + ano para cada dado."""

    research_msgs = [
        SystemMessage(content=f"{ARTICLE_SYSTEM}\n\nUse SEMPRE as ferramentas de busca."),
        HumanMessage(content=research_prompt),
    ]
    
    try:
        research_result = _invoke_with_tools(model_researcher, research_msgs, max_tool_rounds=5)
    except Exception as e:
        print(f"[Researcher] Erro nas ferramentas: {e}. Usando conhecimento interno.")
        research_result = model_cold.invoke([
            SystemMessage(content=ARTICLE_SYSTEM),
            HumanMessage(content=f"Pesquise internamente sobre: {topic['core_thesis']}"),
        ])
        research_result = research_result.content if hasattr(research_result, "content") else str(research_result)

    research_text = research_result if isinstance(research_result, str) else (
        research_result.content if hasattr(research_result, "content") else str(research_result)
    )
    print(f"[Researcher] Coletado: {len(research_text)} caracteres\n")

    # ── FASE 2: OUTLINE ───────────────────────────────────────────────
    print("[Strategist] Estruturando o artigo...")
    outline_prompt = f"""{ARTICLE_SYSTEM}

Monte o outline para o artigo: **{topic['title']}**

{ARTICLE_STYLE_GUIDE}

MATERIAL DE PESQUISA:
{research_text[:10000]}

CONTEXTO DO TOPICO:
{get_writer_context(topic_id)}

INSTRUCOES:
1. Siga a estrutura de 6 secoes do Article Style Guide
2. Defina o hook (pergunta ou cena curta)
3. Mapeie quais dados entram em cada secao
4. Plante 2-3 perguntas que serao respondidas ao longo do artigo
5. Defina a pergunta final (gancho pro proximo artigo)

Retorne o outline estruturado em Markdown."""

    outline_result = model_cold.invoke([
        SystemMessage(content=ARTICLE_SYSTEM),
        HumanMessage(content=outline_prompt),
    ])
    outline_text = outline_result.content if hasattr(outline_result, "content") else str(outline_result)
    print(f"[Strategist] Outline: {len(outline_text)} caracteres\n")

    # ── FASE 3: WRITE ─────────────────────────────────────────────────
    print("[Writer] Escrevendo o artigo...")
    write_prompt = f"""{ARTICLE_SYSTEM}

{ARTICLE_STYLE_GUIDE}

ESCREVA O ARTIGO COMPLETO: **{topic['title']}**

MATERIAL DE PESQUISA:
{research_text[:8000]}

OUTLINE:
{outline_text[:4000]}

CONTEXTO DO TOPICO:
{get_writer_context(topic_id)}

INSTRUCOES CRITICAS:
1. Abra com hook forte (pergunta ou cena curta). Primeira frase = tensao.
2. Tom de Substack: coloquial, direto, como se estivesse falando com um amigo PM.
   Use "bora", "ta", "o negocio e o seguinte", "sabe quando..."
3. Paragrafo curto. Frase curta. Zero jargao de consultoria.
4. Dados com fonte + ano entre parenteses. Use os MAIS RECENTES ({CURRENT_YEAR}).
5. Inclua pelo menos 1 case brasileiro.
6. Inclua 2-3 citacoes de especialistas (Ravi Mehta, Pawel Huryn, Claire Vo).
7. Termine com pergunta no ar ou call to action.
8. Extensao: {topic['target_words']} palavras. ARTIGO COMPLETO, nao resumo.
9. Portugues brasileiro coloquial. Zero em-dashes. Zero ALL CAPS.

ESCREVA O ARTIGO COMPLETO EM MARKDOWN:"""

    writer_result = model_writer.invoke([
        SystemMessage(content=ARTICLE_SYSTEM),
        HumanMessage(content=write_prompt),
    ])
    draft = writer_result.content if hasattr(writer_result, "content") else str(writer_result)
    print(f"[Writer] Artigo: {len(draft)} caracteres (~{len(draft.split())} palavras)\n")

    # ── FASE 4: FACT-CHECK ────────────────────────────────────────────
    print("[FactChecker] Verificando claims...")
    fc_prompt = f"""{ARTICLE_SYSTEM}

Verifique as afirmacoes factuais deste artigo contra a pesquisa. Retorne JSON:

ARTIGO:
{draft[:8000]}

PESQUISA DE REFERENCIA:
{research_text[:6000]}

FORMATO JSON (apenas o JSON, sem explicacao):
{{"corrections": [{{"claim": "...", "issue": "...", "fix": "...", "source": "..."}}], "verified": true/false}}"""

    fc_result = model_cold.invoke([
        SystemMessage(content=ARTICLE_SYSTEM),
        HumanMessage(content=fc_prompt),
    ])
    fc_text = fc_result.content if hasattr(fc_result, "content") else str(fc_result)
    print(f"[FactChecker] Relatorio: {len(fc_text)} caracteres\n")

    # ── FASE 5: COPY EDIT ─────────────────────────────────────────────
    print("[CopyEditor] Revisando voz e clareza...")
    ce_prompt = f"""{ARTICLE_SYSTEM}

{ARTICLE_STYLE_GUIDE}

Revise este artigo para o Substack da Fernanda Faria.

CORRECOES FACTUAIS (JSON):
{fc_text[:2000]}

ARTIGO COMPLETO:
---
{draft}
---

INSTRUCOES:
1. Aplique as correcoes factuais do FactChecker
2. Revise gramatica, clareza, flow e voz
3. Verifique conformidade com o Style Guide do Substack
4. Garanta que o tom esta coloquial e direto
5. RETORNE O ARTIGO COMPLETO REVISADO. NAO RESUMA. MESMO TAMANHO.
6. Se o artigo encolher, voce falhou. Preserve toda a estrutura.

ARTIGO REVISADO (COMPLETO):"""

    ce_result = model_cold.invoke([
        SystemMessage(content=ARTICLE_SYSTEM),
        HumanMessage(content=ce_prompt),
    ])
    final = ce_result.content if hasattr(ce_result, "content") else str(ce_result)

    # Guard rail: se encolheu mais de 30%, usa o draft original
    shrink_ratio = len(final) / max(len(draft), 1)
    if shrink_ratio < 0.7:
        print(f"[CopyEditor] ALERTA: artigo encolheu {shrink_ratio:.0%}. Usando draft original.")
        final = draft
    else:
        print(f"[CopyEditor] Artigo revisado: {len(final)} caracteres (retencao {shrink_ratio:.0%})")

    # ── SAVE ──────────────────────────────────────────────────────────
    output_dir = Path(PROJECT_ROOT) / "book_writer" / "output" / "artigos"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    safe_name = _sanitize_filename(topic['title'][:50])
    output_path = output_dir / f"{safe_name}-{timestamp}.md"
    output_path.write_text(final, encoding="utf-8")

    # Save research for reference
    research_path = output_dir / f"{safe_name}-{timestamp}-pesquisa.md"
    research_path.write_text(research_text, encoding="utf-8")

    print(f"\n{'='*60}")
    print(f"ARTIGO PRONTO: {output_path}")
    print(f"Pesquisa salva: {research_path}")
    print(f"Palavras: ~{len(final.split())} | Caracteres: {len(final)}")
    print(f"{'='*60}")

    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Article Writer — Pipeline multiagente para artigos Substack"
    )
    parser.add_argument(
        "--topic", "-t",
        type=str,
        default="julgamento-vs-dados",
        help="ID do topico (ex: julgamento-vs-dados, lideranca-feminina)",
    )
    parser.add_argument(
        "--max-revisions", "-r",
        type=int,
        default=2,
        help="Maximo de ciclos de revisao. Default: 2",
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="Lista os topicos disponiveis e sai",
    )

    args = parser.parse_args()

    if args.list:
        print("\nTopicos disponiveis para artigos:\n")
        for t in list_topics():
            print(f"  {t['id']:<30} {t['title']}")
        print()
        return 0

    topic = get_topic(args.topic)
    if not topic:
        print(f"\nTopico '{args.topic}' nao encontrado.\n")
        print("Topicos disponiveis:\n")
        for t in list_topics():
            print(f"  {t['id']:<30} {t['title']}")
        print()
        return 1

    output_path = run_article_pipeline(args.topic, max_revisions=args.max_revisions)
    print(f"\nOutput: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
