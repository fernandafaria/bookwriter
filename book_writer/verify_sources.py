"""verify_sources.py — extrai citações, números e datas do manuscrito pra checagem.

Determinístico, offline, stdlib puro. Emite JSON: uma entrada por claim com
trecho original, query de verificação, anos e classificação de frescor.
A checagem de existência (busca web) roda separado, via execute_code.

Duas verificações determinísticas:
  1. Existência — citação "fabricada" (título/fonte que não existe).
  2. Frescor — estatística com ano antigo (default: < 2025), salvo caso histórico.

Uso:
  python3 verify_sources.py <manuscrito.md>   # emite JSON no stdout
  python3 verify_sources.py                    # self-check offline
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RE_FONTE_LINE = re.compile(r"^Fonte:\s*(.+)$", re.MULTILINE)
RE_PAREN_YEAR = re.compile(r"\(([^()]*\b(?:19|20)\d{2}[^()]*)\)")
RE_QUOTED_TITLE = re.compile(r'"([^"]{12,90})"')
RE_TITLE_HINT = re.compile(
    r"\b(study|survey|report|patterns|framework|index|state of|guide|paper|"
    r"degradation|resilient|outlook|benchmark|global)\b",
    re.IGNORECASE,
)
RE_YEAR = re.compile(r"\b(?:19|20)\d{2}\b")
# sinal de caso histórico (referência de história, não estatística): pode ser antigo
CASE_HINTS = re.compile(r"caso|case|zillow|watson|fundad|histórico|historico|10-K|filing", re.IGNORECASE)

FRESH_CUTOFF = 2025  # estatística mais antiga que isso = desatualizada


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip(" .,;:()[]\n\t")


def classify_freshness(claim: dict, cutoff: int = FRESH_CUTOFF) -> str:
    """Classifica frescor de uma claim. Caso histórico passa mesmo se antigo."""
    ys = claim.get("years", [])
    if not ys:
        return "sem_data"
    if min(ys) < cutoff and not CASE_HINTS.search(claim["source"]):
        return "desatualizada"
    return "ok"


def extract(text: str) -> list[dict]:
    claims: list[dict] = []
    seen: set[str] = set()

    def add(source: str, context: str, query: str, kind: str) -> None:
        key = source.strip().lower()
        if key and key not in seen:
            seen.add(key)
            years = sorted({int(y) for y in RE_YEAR.findall(source)})
            claims.append(
                {
                    "kind": kind,
                    "source": _clean(source),
                    "context": _clean(context),
                    "query": _clean(query),
                    "years": years,
                }
            )

    for m in RE_FONTE_LINE.finditer(text):
        add(m.group(1), m.group(0), m.group(1), "fonte_line")

    for m in RE_PAREN_YEAR.finditer(text):
        inner = m.group(1)
        ctx = text[max(0, m.start() - 160): m.end() + 40].replace("\n", " ")
        add(inner, ctx, inner, "paren_citation")

    for m in RE_QUOTED_TITLE.finditer(text):
        t = m.group(1)
        if RE_TITLE_HINT.search(t):
            ctx = text[max(0, m.start() - 120): m.end() + 60].replace("\n", " ")
            add(t, ctx, t, "quoted_title")

    return claims


def main(path: str) -> None:
    text = Path(path).read_text(encoding="utf-8")
    claims = extract(text)
    print(json.dumps(claims, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sample = (
            'De acordo com a McKinsey, apenas 15% (McKinsey, "The State of AI '
            'in 2024", maio de 2024).\n'
            'Fonte: Zillow 10-K Filing 2021; The Wall Street Journal, novembro 2021.\n'
            'Fonte: Gartner, "Building Resilient AI Teams", 2025, pág. 12.\n'
            'Um estudo da Google "Production ML Degradation Patterns" (Google AI, 2024).\n'
        )
        c = extract(sample)
        kinds = {x["kind"] for x in c}
        assert kinds == {"fonte_line", "paren_citation", "quoted_title"}, kinds
        by_year = {x["source"]: classify_freshness(x) for x in c}
        # estatística 2024 (McKinsey) deve ser desatualizada; caso 2021 (Zillow) passa
        assert any("State of AI" in s and v == "desatualizada" for s, v in by_year.items()), by_year
        assert any("Zillow" in s and v == "ok" for s, v in by_year.items()), by_year
        print(f"self-check OK: {len(c)} claims, frescor={by_year}")
