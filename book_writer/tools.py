"""
Book Writer — Tools
===================
Ferramentas reais para pesquisa e verificação dos agentes.

Segue o padrão da Post AI Company (langgraph_engine.py):
- search_web: busca na web com múltiplos fallbacks
- extract_urls: extrai conteúdo de páginas
- read_knowledge_base: consulta os frameworks, datapoints e cases locais

Requer: pip install langgraph langchain-core langchain-openai
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path

from langchain_core.tools import tool

PROJECT_ROOT = Path(__file__).parent.parent  # ~/code/feproduto

# Flag global: quando um brief (livro novo) está ativo, o read_knowledge_base
# NÃO retorna o conteúdo do livro antigo (frameworks/datapoints/cases/outline).
# Setada pelo engine.run_pipeline antes de rodar o grafo.
ACTIVE_BRIEF = None


# ═══════════════════════════════════════════════════════════════════════════
# WEB SEARCH
# ═══════════════════════════════════════════════════════════════════════════

@tool
def search_web(query: str) -> str:
    """Busca na web informações atuais sobre qualquer tópico.

    Use para pesquisar fatos, estatísticas, cases de empresas, papers,
    notícias, e qualquer informação que precise ser verificada ou atualizada.

    Args:
        query: Termo de busca (ex: 'AI Product Management UX non-deterministic 2025')

    Returns:
        Resultados da busca em JSON com título, URL e descrição.
    """
    import requests

    # Fallback 1: Google search (HTML scraping)
    try:
        url = "https://www.google.com/search"
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            )
        }
        resp = requests.get(
            url, params={"q": query, "num": 10, "hl": "en"}, headers=headers, timeout=15
        )
        if resp.status_code == 200:
            results = []
            for match in re.finditer(
                r'<a[^>]*href="/url\?q=(https?://[^"&]+)[^"]*"[^>]*>(.*?)</a>',
                resp.text,
                re.DOTALL,
            ):
                href = re.sub(r'&amp;', '&', match.group(1))
                snippet = re.sub(r'<[^>]+>', '', match.group(2) or '')
                if any(skip in href for skip in ['google.com', 'googleadservices', '/search?', '/settings/']):
                    continue
                snippet = snippet[:300]
                results.append({
                    "title": snippet[:120] or href[:120],
                    "url": href,
                    "description": snippet,
                })
                if len(results) >= 5:
                    break
            if results:
                return json.dumps(results, ensure_ascii=False, indent=2)
    except Exception:
        pass

    # Fallback 2: DuckDuckGo Lite
    try:
        url = "https://lite.duckduckgo.com/lite/"
        resp = requests.post(url, data={"q": query}, timeout=15)
        if resp.status_code == 200:
            results = []
            for match in re.finditer(
                r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>.*?<span[^>]*>(.*?)</span>',
                resp.text,
                re.DOTALL,
            ):
                href = match.group(1)
                text = re.sub(r'<[^>]+>', '', match.group(2) or match.group(3) or '')
                if href.startswith("http") and "duckduckgo" not in href:
                    results.append({
                        "title": text[:120] or href,
                        "url": href,
                        "description": text[:300] if text else ""
                    })
                if len(results) >= 5:
                    break
            if results:
                return json.dumps(results, ensure_ascii=False, indent=2)
    except Exception:
        pass

    return json.dumps({"error": "Nenhum resultado encontrado", "query": query})


# ═══════════════════════════════════════════════════════════════════════════
# URL EXTRACTION
# ═══════════════════════════════════════════════════════════════════════════

@tool
def extract_urls(urls: list[str]) -> str:
    """Extrai o conteúdo completo de páginas web.

    Use para ler artigos, papers, reportagens referenciadas
    em resultados de busca. Permite verificar informações específicas.

    Args:
        urls: Lista de URLs para extrair (máximo 3)

    Returns:
        Conteúdo extraído em formato texto.
    """
    import requests

    results = {}
    for url in urls[:3]:
        try:
            resp = requests.get(url, timeout=20, headers={
                "User-Agent": "Mozilla/5.0 (compatible; BookWriter/1.0)"
            })
            if resp.status_code == 200:
                text = resp.text[:12000]
                # Remove HTML
                text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
                text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
                text = re.sub(r'<[^>]+>', ' ', text)
                text = re.sub(r'\s+', ' ', text).strip()
                results[url] = text[:5000]
            else:
                results[url] = f"HTTP {resp.status_code}: não foi possível acessar"
        except Exception as e:
            results[url] = f"Erro: {str(e)}"

    return json.dumps(results, ensure_ascii=False, indent=2)


# ═══════════════════════════════════════════════════════════════════════════
# KNOWLEDGE BASE ACCESS
# ═══════════════════════════════════════════════════════════════════════════

@tool
def read_knowledge_base(query: str) -> str:
    """Consulta a base de conhecimento do livro (frameworks, datapoints, cases).

    Use para acessar frameworks autorais (ESCAPE, AI Trap, 7 Sinais,
    10 Competências), dados quantitativos com fonte, cases de empresas,
    outline do livro, e style guide.

    Args:
        query: Tipo de informação desejada. Opções:
               'frameworks' - Todos os frameworks autorais
               'datapoints' - Dados quantitativos com fontes
               'cases' - Case studies de empresas
               'outline' - Estrutura completa do livro
               'curiosity_chapter_N' - Gaps de curiosidade para capítulo N
               'style_guide' - Guia de voz e tom da autora

    Returns:
        Conteúdo solicitado em formato JSON ou texto.
    """
    import sys
    sys.path.insert(0, str(PROJECT_ROOT))

    if ACTIVE_BRIEF and query in ("frameworks", "datapoints", "cases", "outline"):
        return json.dumps({"note": "brief ativo: pesquisar na web, não reutilizar frameworks/dados/cases de livro anterior"})

    from book_writer.knowledge_base import (
        FRAMEWORKS, DATAPOINTS, CASE_STUDIES, BOOK_OUTLINE,
        get_chapter_info, knowledge_summary,
    )
    from book_writer.curiosity_registry import to_prompt_context, registry_summary
    from book_writer.style_guide import STYLE_GUIDE

    if query == "frameworks":
        result = {}
        for key, fw in FRAMEWORKS.items():
            result[key] = {
                "name": fw.name,
                "acronym": fw.acronym,
                "chapter": fw.chapter,
                "definition": fw.definition,
                "components": fw.components,
                "examples": fw.examples,
            }
        return json.dumps(result, ensure_ascii=False, indent=2)

    elif query == "datapoints":
        dps = []
        for dp in DATAPOINTS:
            dps.append({
                "value": dp.value,
                "source": dp.source,
                "year": dp.year,
                "context": dp.context,
            })
        return json.dumps(dps, ensure_ascii=False, indent=2)

    elif query == "cases":
        cases = []
        for cs in CASE_STUDIES:
            cases.append({
                "company": cs.company,
                "chapter": cs.chapter,
                "sector": cs.sector,
                "problem": cs.problem,
                "solution": cs.solution,
                "results": cs.results,
            })
        return json.dumps(cases, ensure_ascii=False, indent=2)

    elif query == "outline":
        return json.dumps(BOOK_OUTLINE, ensure_ascii=False, indent=2)

    elif query == "style_guide":
        return STYLE_GUIDE

    elif query.startswith("curiosity_chapter_"):
        chapter = int(query.split("_")[-1])
        ctx = to_prompt_context(chapter)
        summary = registry_summary()
        return f"{summary}\n\n{ctx}"

    elif query == "summary":
        return knowledge_summary()

    else:
        return json.dumps({
            "error": f"Query '{query}' não reconhecida",
            "valid_options": [
                "frameworks", "datapoints", "cases", "outline",
                "curiosity_chapter_N", "style_guide", "summary"
            ]
        }, ensure_ascii=False, indent=2)


# ═══════════════════════════════════════════════════════════════════════════
# ACADEMIC PAPER SEARCH
# ═══════════════════════════════════════════════════════════════════════════

@tool
def search_papers(query: str) -> str:
    """Busca papers acadêmicos publicados (OpenAlex) — fonte verificável com DOI.

    Use para achar evidência acadêmica (título, autores, instituições como
    Stanford/MIT, ano, citações) em vez de fonte genérica de web.

    Args:
        query: termo de busca (ex: 'AI agents product management empirical study')

    Returns:
        JSON com papers: título, ano, autores, instituições, citações, DOI.
    """
    import urllib.request, urllib.parse
    q = urllib.parse.quote(query)
    url = ("https://api.openalex.org/works?search=" + q +
           "&per-page=5&select=title,publication_year,cited_by_count,doi,authorships")
    req = urllib.request.Request(url, headers={"User-Agent": "book-writer/1.0 (mailto:research@example.com)"})
    r = json.loads(urllib.request.urlopen(req, timeout=25).read())
    results = []
    for w in r.get("results", []):
        authors = ", ".join(a["author"]["display_name"] for a in w.get("authorships", [])[:3])
        insts = []
        for a in w.get("authorships", []):
            for i in a.get("institutions", [])[:1]:
                insts.append(i.get("display_name", ""))
        results.append({
            "title": w.get("title"),
            "year": w.get("publication_year"),
            "authors": authors,
            "institutions": ", ".join(insts[:4]),
            "citations": w.get("cited_by_count"),
            "doi": w.get("doi"),
        })
    return json.dumps(results, ensure_ascii=False, indent=2)


# ═══════════════════════════════════════════════════════════════════════════
# PERPLEXITY SEARCH (resposta com citações verificáveis)
# ═══════════════════════════════════════════════════════════════════════════

@tool
def search_perplexity(query: str) -> str:
    """Busca na web com Perplexity — resposta com CITAÇÕES verificáveis (URLs).

    Use para achar dados, estatísticas e claims com fonte confiável (substitui
    o scraping frágil do Google). A resposta vem com a lista de citações.

    Args:
        query: termo de busca (ex: 'AI adoption rate 2025 McKinsey statistic')

    Returns:
        JSON com a resposta e a lista de citações (URLs das fontes).
    """
    import urllib.request
    key = _load_key_from_env("PERPLEXITY_API_KEY")
    body = json.dumps({"model": "sonar", "messages": [{"role": "user", "content": query}]}).encode()
    req = urllib.request.Request("https://api.perplexity.ai/chat/completions", data=body,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=45).read())
    answer = r["choices"][0]["message"]["content"]
    citations = r.get("citations", [])
    return json.dumps({"answer": answer, "citations": citations}, ensure_ascii=False, indent=2)


# ═══════════════════════════════════════════════════════════════════════════
# SOURCE SEAM — fonte de dados única com fallback (paralelo do deepseek-harness)
# ═══════════════════════════════════════════════════════════════════════════

@tool
def search_sources(query: str) -> str:
    """Fonte de dados única (seam). PESQUISE SEMPRE POR AQUI, não pelas tools soltas.

    Tenta na ordem: Perplexity (resposta com URLs de citação), OpenAlex (papers
    com DOI), Google scraping. Retorna dados com fonte anexada.

    Use para QUALQUER dado, estatística, case ou claim. Um número só pode ser
    citado no livro se veio daqui (com fonte).

    Args:
        query: termo de busca (ex: 'AI adoption rate 2025 McKinsey statistic')

    Returns:
        JSON com a resposta e a fonte (citação/URL/DOI).
    """
    # 1. Perplexity (melhor: resposta + URLs de citação)
    if _load_key_from_env("PERPLEXITY_API_KEY"):
        try:
            return search_perplexity.invoke({"query": query})
        except Exception:
            pass
    # 2. OpenAlex (papers com DOI)
    try:
        return search_papers.invoke({"query": query})
    except Exception:
        pass
    # 3. Google scraping (último recurso)
    return search_web.invoke({"query": query})


# Todos os tools disponíveis para os agentes
ALL_TOOLS = [search_sources, search_web, extract_urls, read_knowledge_base, search_papers, search_perplexity]


# ═══════════════════════════════════════════════════════════════════════════
# MODEL FACTORY
# ═══════════════════════════════════════════════════════════════════════════

def _load_key_from_env(name: str) -> str:
    """Carrega uma chave do ambiente ou do ~/.hermes/.env (sem expor o valor)."""
    key = os.environ.get(name, "")
    if key:
        return key
    hermes_env = Path.home() / ".hermes" / ".env"
    if hermes_env.exists():
        for line in hermes_env.read_text().split("\n"):
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def _get_model(temperature: float = 0.7, max_tokens: int = 8192):
    """Cria o modelo LLM. Default DeepSeek; Grok/xAI se BOOK_LLM_PROVIDER=grok."""
    from langchain_openai import ChatOpenAI

    provider = os.environ.get("BOOK_LLM_PROVIDER", "deepseek").lower()

    if provider == "grok":
        return ChatOpenAI(
            model="grok-4.6",
            api_key=_load_key_from_env("XAI_API_KEY"),
            base_url="https://api.x.ai/v1",
            temperature=temperature,
            max_tokens=max_tokens,
        )

    return ChatOpenAI(
        model="deepseek-chat",
        api_key=_load_key_from_env("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com/v1",
        temperature=temperature,
        max_tokens=max_tokens,
    )


# ═══════════════════════════════════════════════════════════════════════════
# TOOL-CALLING HELPER
# ═══════════════════════════════════════════════════════════════════════════

def _invoke_with_tools(
    model,
    messages: list,
    max_tool_rounds: int = 3,
    verbose: bool = True,
) -> str:
    """Invoca o modelo com tool calling loop.

    O modelo pode chamar tools múltiplas vezes. Cada tool call é executada
    e o resultado é injetado como ToolMessage. O loop continua até o modelo
    responder sem tool calls ou atingir max_tool_rounds.

    Args:
        model: Modelo com tools bindadas (model.bind_tools(ALL_TOOLS))
        messages: Lista de mensagens (HumanMessage, SystemMessage, etc.)
        max_tool_rounds: Máximo de rounds de tool calling
        verbose: Se True, imprime tool calls no console

    Returns:
        Resposta final do modelo (string).
    """
    from langchain_core.messages import ToolMessage, HumanMessage

    current_messages = list(messages)

    for round_num in range(max_tool_rounds):
        response = model.invoke(current_messages)

        # Se não há tool calls, é a resposta final
        if not hasattr(response, "tool_calls") or not response.tool_calls:
            return response.content if hasattr(response, "content") else str(response)

        # Adiciona AIMessage com tool_calls
        current_messages.append(response)

        # Executa cada tool call
        for tc in response.tool_calls:
            tool_name = tc.get("name", "")
            tool_args = tc.get("args", {})
            tool_id = tc.get("id", "")

            if verbose:
                arg_preview = str(tool_args)[:120]
                print(f"  🔧 {tool_name}({arg_preview})")

            # Encontra e executa a tool
            tool_fn = {t.name: t for t in ALL_TOOLS}.get(tool_name)
            if tool_fn:
                try:
                    result = tool_fn.invoke(tool_args)
                except Exception as e:
                    result = f"Erro ao executar tool: {e}"
            else:
                result = f"Tool '{tool_name}' não encontrada"

            # Adiciona ToolMessage
            current_messages.append(ToolMessage(
                content=str(result),
                tool_call_id=tool_id,
                name=tool_name,
            ))

    # Se atingiu max_tool_rounds, força resposta final
    current_messages.append(HumanMessage(
        content="Agora responda com sua análise final, sem chamar mais ferramentas."
    ))
    final = model.invoke(current_messages)
    return final.content if hasattr(final, "content") else str(final)
