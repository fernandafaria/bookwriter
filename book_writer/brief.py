"""brief.py — brief de livro (editora agentica).

Um brief descreve QUALQUER livro. O pipeline lê o brief em vez do BOOK_OUTLINE fixo.
Formato: ver briefs/exemplo.json
"""
import json


def load_brief(path):
    with open(path) as f:
        return json.load(f)


def get_chapter_info(brief, n):
    """Info do capítulo n a partir do brief (mesma forma que knowledge_base.get_chapter_info)."""
    for ch in brief.get("chapters", []):
        if ch.get("num") == n:
            return {
                "chapter": n,
                "chapter_title": ch.get("title", ""),
                "premise": ch.get("premise", ""),
                "sections": ch.get("sections", []),
            }
    return {}


def chapter_context(brief, n):
    """Capítulos anteriores/posteriores como texto (pra plantar gaps e referenciar)."""
    chs = brief.get("chapters", [])
    prev = [f"Cap {c['num']}: {c['title']}" for c in chs if c["num"] < n]
    post = [f"Cap {c['num']}: {c['title']}" for c in chs if c["num"] > n]
    return prev, post


def research_angles(brief):
    """Temas de pesquisa do brief (ou lista vazia — o Researcher decide)."""
    return brief.get("research_angles", [])
