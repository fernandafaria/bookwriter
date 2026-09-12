"""voice_regression.py — Regressão de voz cross-chapter.

O cap 1 pode dar Fernanda-score 9 sozinho; isso NÃO garante que o cap 7 soa
igual. Aqui rodamos o eval (evals.py) em TODOS os capítulos concluídos e
medimos a variância do fernanda_score. Drift alto = o livro está perdendo a voz.

Uso:
  python3 -m book_writer.voice_regression [output_dir]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


def _chapter_num(name: str) -> int:
    m = re.search(r"capitulo-(\d+)", name)
    return int(m.group(1)) if m else 0


def latest_per_chapter(files) -> dict:
    """Pega o arquivo mais recente de cada capítulo (por mtime)."""
    latest = {}
    for f in files:
        n = _chapter_num(f.name)
        if n == 0:
            continue
        if n not in latest or f.stat().st_mtime > latest[n].stat().st_mtime:
            latest[n] = f
    return latest


def run(output_dir: str = "output", variance_cap: float = 15.0) -> dict:
    """Roda eval em cada capítulo e reporta drift de voz. Retorna o relatório."""
    from book_writer.evals import diagnose_ai_voice

    out = PROJECT_ROOT / output_dir
    files = sorted(out.glob("capitulo-*.md"))
    if not files:
        return {"error": f"nenhum capitulo-*.md em {out}"}

    latest = latest_per_chapter(files)
    scores = {}
    for n in sorted(latest):
        text = latest[n].read_text(encoding="utf-8")
        r = diagnose_ai_voice(text)
        scores[n] = {
            "file": latest[n].name,
            "fernanda": r["fernanda_score"],
            "ai": r["ai_score"],
        }

    f_vals = [s["fernanda"] for s in scores.values()]
    a_vals = [s["ai"] for s in scores.values()]
    f_min, f_max = min(f_vals), max(f_vals)
    a_min, a_max = min(a_vals), max(a_vals)
    spread = f_max - f_min

    lines = ["## Regressão de voz (cross-chapter)\n"]
    for n in sorted(scores):
        s = scores[n]
        flag = "  ⚠ drift" if s["fernanda"] < f_max - variance_cap else ""
        lines.append(f"  Cap {n:>2}  Fernanda={s['fernanda']:>3}/100  AI={s['ai']:>3}/100{flag}   {s['file']}")
    lines.append("")
    lines.append(f"  Fernanda: min {f_min} / max {f_max} / spread {spread}")
    lines.append(f"  AI:       min {a_min} / max {a_max}")
    verdict = "STABLE" if spread <= variance_cap else "DRIFT"
    lines.append(f"  Veredito: {verdict} (cap {variance_cap} pontos de spread)")

    return {"scores": scores, "spread": spread, "verdict": verdict,
            "report": "\n".join(lines)}


if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else "output"
    print(run(d)["report"])
