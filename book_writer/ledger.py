"""ledger.py — Claim ledger (fonte-de-verdade única de claims numéricas do livro).

Determinístico, sem LLM. Um JSON por livro em output/ledger-<slug>.json.

Cada claim registrada pelo Verifier com veredito; claims refutadas viram
regra permanente pro Writer (não repetir o mesmo erro em capítulos futuros).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent  # ~/code/feproduto


def _slug(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (title or "livro").lower()).strip("-")
    return s or "livro"


def ledger_path(brief) -> Path:
    slug = _slug(brief.get("title", "livro")) if brief else "livro"
    return PROJECT_ROOT / "output" / f"ledger-{slug}.json"


def load(brief) -> dict:
    p = ledger_path(brief)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {"claims": []}
    return {"claims": []}


def register(brief, claims) -> None:
    """Append claims (list of dicts). Verdicts: verified/unsupported/contradicted/refuted."""
    if not claims:
        return
    p = ledger_path(brief)
    data = load(brief)
    data["claims"].extend(claims)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def refuted(brief) -> list:
    data = load(brief)
    return [c for c in data.get("claims", [])
            if c.get("verdict") in ("wrong", "contradicted", "unsupported", "refuted")]


def refuted_text(brief) -> str:
    r = refuted(brief)
    if not r:
        return ""
    lines = ["CLAIMS JÁ REFUTADAS NESTE LIVRO (NÃO repita, NÃO reformule):"]
    for c in r:
        lines.append(f"- {c.get('claim', '')}  [veredito: {c.get('verdict', '')}]")
    return "\n".join(lines)


if __name__ == "__main__":
    # auto-teste: register + refuted round-trip num brief fake
    b = {"title": "Livro Teste"}
    register(b, [{"claim": "CBA é a maior produtora de alumínio", "verdict": "contradicted"},
                 {"claim": "82% de NRR", "source": "x", "url": "http://x", "verdict": "verified"}])
    assert len(refuted(b)) == 1
    assert "CBA" in refuted_text(b)
    print("ledger OK:", len(refuted(b)), "claim refutada")
