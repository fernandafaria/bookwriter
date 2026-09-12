"""digest.py — Memória do livro (digest chain determinístico).

Ao fechar um capítulo (APPROVE/MINOR), guarda a FactSheet dele. O Strategist
do capítulo seguinte recebe os digests dos capítulos anteriores pra não repetir
exemplo, não contradizer claim e não re-explicar conceito.

Não é RAG: é um resumo estruturado (factsheet + título), zero embedding.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent  # ~/code/feproduto


def _slug(title: str) -> str:
    import re
    s = re.sub(r"[^a-z0-9]+", "-", (title or "livro").lower()).strip("-")
    return s or "livro"


def digest_path(brief) -> Path:
    import re
    slug = _slug(brief.get("title", "livro")) if brief else "livro"
    return PROJECT_ROOT / "output" / f"digest-{slug}.json"


def write(brief, chapter_num: int, chapter_title: str, factsheet: str) -> None:
    """Append a chapter digest (title + factsheet) to the book's digest file."""
    p = digest_path(brief)
    data = {"chapters": []}
    if p.exists():
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            data = {"chapters": []}
    # idempotente: sobrescreve o digest do mesmo capítulo
    data["chapters"] = [c for c in data.get("chapters", []) if c.get("num") != chapter_num]
    data["chapters"].append({
        "num": chapter_num,
        "title": chapter_title,
        "factsheet": factsheet,
        "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    data["chapters"].sort(key=lambda c: c.get("num", 0))
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load_prior(brief, chapter_num: int) -> str:
    """Texto dos digests de capítulos ANTERIORES a chapter_num (pra injetar no Strategist)."""
    p = digest_path(brief)
    if not p.exists():
        return ""
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return ""
    prior = [c for c in data.get("chapters", []) if c.get("num", 0) < chapter_num]
    if not prior:
        return ""
    lines = ["## MEMÓRIA DO LIVRO (fatos/claims já estabelecidos em capítulos anteriores)"]
    for c in prior:
        lines.append(f"### Cap {c.get('num')}: {c.get('title', '')}")
        fs = c.get("factsheet", "")
        lines.append(fs if fs else "(sem factsheet)")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    b = {"title": "Livro Teste"}
    write(b, 1, "O Fim do Executor", '{"facts": [{"claim": "x", "source": "y"}]}')
    write(b, 1, "O Fim do Executor", '{"facts": [{"claim": "z", "source": "y"}]}')  # idempotente
    assert len(json.loads(digest_path(b).read_text())["chapters"]) == 1
    assert "O Fim do Executor" in load_prior(b, 2)
    assert load_prior(b, 1) == ""
    print("digest OK: idempotente + prior só capítulos anteriores")
