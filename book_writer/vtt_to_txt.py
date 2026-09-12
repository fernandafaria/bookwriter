#!/usr/bin/env python3
"""vtt_to_txt.py — limpa um .vtt (timestamps/tags) pra texto puro.

Uso: python3 vtt_to_txt.py <in.vtt> <out.txt>
"""
import re, sys


def clean(vtt: str) -> str:
    lines = []
    for line in vtt.splitlines():
        s = line.strip()
        if not s or s == "WEBVTT" or s.startswith(("NOTE", "Kind:", "Language:")):
            continue
        if re.match(r"^\d{2}:\d{2}:\d{2}[.,]\d{3}\s*-->", s):
            continue  # linha de timestamp
        s = re.sub(r"<[^>]+>", "", s)  # remove tags <c> e <00:00:00.000>
        s = re.sub(r"&amp;", "&", s).replace("&lt;", "<").replace("&gt;", ">")
        if s:
            lines.append(s)
    return " ".join(lines)


if __name__ == "__main__":
    text = clean(open(sys.argv[1]).read())
    open(sys.argv[2], "w").write(text)
    print(f"{sys.argv[2]}: {len(text)} chars")
