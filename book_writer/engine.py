"""Book Writer — LangGraph Engine.

Pipeline multiagente para escrita de capitulos do livro "Liderando na Era dos Agentes".

Arquitetura:
  Researcher → FactSheet → Strategist → Writer → FactChecker → CopyEditor → AuthenticityFixer → Verifier → EditorChefe
                                                                                               ↑____________________|
                                                                                               REVISE loop (max Nx)

O FactSheet (novo) extrai a folha de fatos verificáveis antes de compor.
O Verifier (novo) lê a FONTE de cada claim e compara veracidade, registrando no ledger.
O AuthenticityFixer roda automaticamente apos CopyEditor.
Usa o evals.py pra medir marcadores de 'cara de AI' (25 marcadores).
Se AI score > 10, reescreve trechos problematicos. Se <= 10, passa direto.

Uso:
  python -m book_writer.run --chapter 6
  python -m book_writer.run --chapter 7 --max-revisions 2
"""

from __future__ import annotations

import operator
from typing import Annotated, Literal, TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.checkpoint.memory import MemorySaver

from book_writer.agents import (
    node_researcher,
    node_factsheet,
    node_strategist,
    node_writer,
    node_fact_checker,
    node_copy_editor,
    node_authenticity_fixer,
    node_verifier,
    node_editor_chefe,
)
from book_writer.knowledge_base import get_chapter_info


class BookWriterState(TypedDict, total=False):
    """Estado do pipeline com merge semantics.

    Antes era StateGraph(dict): um nó que retornava dict parcial APAGAVA as
    chaves não retornadas (target_chapter → 0, revision_count → reset → loop
    REVISE infinito). Com TypedDict, chave não retornada é PRESERVADA, então
    um nó novo que esqueça um campo é inofensivo (a causa raiz, não o sintoma).
    """
    target_chapter: int
    research_material: str
    factsheet: str
    chapter_outline: str
    chapter_draft: str
    draft_path: str
    factcheck_report: str
    copy_editor_report: str
    verifier_report: str
    eval_result: dict
    editor_decision: str
    editor_feedback: str
    revision_count: int
    max_revisions: int
    messages: list
    brief: dict


def route_after_editor(state: dict) -> Literal["end", "write"]:
    """Decide proximo passo apos EditorChefe.

    O EditorChefe ja incrementa revision_count no retorno do node
    (revision_count + 1 se REVISE). O LangGraph faz merge do output
    do node no state ANTES de executar conditional edges, entao este
    router ve o revision_count ja incrementado.
    """
    decision = state.get("editor_decision", "APPROVE")
    revision_count = state.get("revision_count", 0)
    max_revisions = state.get("max_revisions", 3)

    # Hard safety: force end after max_revisions regardless of decision
    if decision in ("APPROVE", "MINOR") or revision_count >= max_revisions:
        if revision_count >= max_revisions:
            print(f"[Router] Hard stop: revision_count={revision_count} >= max_revisions={max_revisions}. Forçando APPROVE.")
        return "end"
    else:
        return "write"


def build_book_writer_graph() -> StateGraph:
    """Constroi o StateGraph do pipeline de escrita.

    Pipeline: research → strategy → write → factcheck → copyedit → authfix → editor → [end|write]

    O AuthenticityFixer e execucao automatica (sempre roda apos CopyEditor).
    Se o texto passa no eval (AI score <= 10), e um no-op.
    """
    workflow = StateGraph(BookWriterState)

    workflow.add_node("research", node_researcher)
    workflow.add_node("factsheet", node_factsheet)
    workflow.add_node("strategy", node_strategist)
    workflow.add_node("write", node_writer)
    workflow.add_node("factcheck", node_fact_checker)
    workflow.add_node("copyedit", node_copy_editor)
    workflow.add_node("authfix", node_authenticity_fixer)
    workflow.add_node("verify", node_verifier)
    workflow.add_node("editor", node_editor_chefe)

    workflow.add_edge(START, "research")
    workflow.add_edge("research", "factsheet")
    workflow.add_edge("factsheet", "strategy")
    workflow.add_edge("strategy", "write")
    workflow.add_edge("write", "factcheck")
    workflow.add_edge("factcheck", "copyedit")
    workflow.add_edge("copyedit", "authfix")
    workflow.add_edge("authfix", "verify")
    workflow.add_edge("verify", "editor")

    workflow.add_conditional_edges(
        "editor",
        route_after_editor,
        {"end": END, "write": "write"},
    )

    return workflow


# Alias para compatibilidade
build_graph = build_book_writer_graph


def run_pipeline(
    chapter_num: int = 1,
    max_revisions: int = 3,
    verbose: bool = True,
    brief=None,
) -> dict:
    """Executa o pipeline completo para um capitulo.

    Args:
        chapter_num: Numero do capitulo (1-8)
        max_revisions: Maximo de ciclos REVISE antes de forcar APPROVE
        verbose: Se True, imprime progresso

    Returns:
        Estado final do grafo com chapter_draft, draft_path, eval_result, etc.
    """
    from datetime import datetime

    if brief:
        from book_writer.brief import get_chapter_info as _bci
        info = _bci(brief, chapter_num)
        book_title = brief.get("title", "Livro")
    else:
        info = get_chapter_info(chapter_num)
        book_title = "Liderando na Era dos Agentes"

    if verbose:
        print(f"\n{'='*60}")
        print(f"  BOOK WRITER — {book_title}")
        print(f"  Capitulo {chapter_num}: {info.get('chapter_title', '')}")
        print(f"  Max revisoes: {max_revisions}")
        print(f"{'='*60}\n")

    workflow = build_book_writer_graph()
    graph = workflow.compile(checkpointer=MemorySaver())

    initial_state = {
        "target_chapter": chapter_num,
        "research_material": "",
        "factsheet": "",
        "chapter_outline": "",
        "chapter_draft": "",
        "draft_path": "",
        "factcheck_report": "",
        "copy_editor_report": "",
        "verifier_report": "",
        "eval_result": {},
        "editor_decision": "",
        "editor_feedback": "",
        "revision_count": 0,
        "max_revisions": max_revisions,
        "messages": [],
        "brief": brief,
    }

    config = {"configurable": {"thread_id": f"book-chapter-{chapter_num}"}}

    # Ativa o modo "brief" no read_knowledge_base (não vaza conteúdo do livro antigo)
    if brief:
        import book_writer.tools as _tools
        _tools.ACTIVE_BRIEF = brief

    final_state = graph.invoke(initial_state, config)

    if verbose:
        decision = final_state.get("editor_decision", "?")
        path = final_state.get("draft_path", "?")
        revs = final_state.get("revision_count", 0)
        draft_len = len(final_state.get("chapter_draft", ""))
        eval_result = final_state.get("eval_result", {})
        ai_score = eval_result.get("ai_score", "?")
        fernanda_score = eval_result.get("fernanda_score", "?")
        print(f"\n{'='*60}")
        print(f"  PIPELINE CONCLUIDO")
        print(f"  Decisao: {decision}")
        print(f"  Revisoes: {revs}")
        print(f"  Tamanho do draft: {draft_len} caracteres")
        print(f"  AI Score: {ai_score}/100")
        print(f"  Fernanda Score: {fernanda_score}/100")
        print(f"  Arquivo: {path}")
        print(f"{'='*60}\n")

    return final_state


if __name__ == "__main__":
    import sys
    chapter = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    run_pipeline(chapter_num=chapter)
