#!/usr/bin/env python3
"""fetch_yt_transcript.py — baixa legendas (auto/manual) de um vídeo do YouTube e salva .txt.

Uso: python3 fetch_yt_transcript.py <video_id> <out.txt> [--lang pt]
"""
import json, re, sys, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
      "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8"}


def _get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20).read().decode("utf-8", "ignore")


def fetch_transcript(vid: str, lang: str = "pt") -> str:
    html = _get(f"https://www.youtube.com/watch?v={vid}")
    m = re.search(r'"captionTracks":(\[.*?\])', html)
    if not m:
        raise RuntimeError("sem captionTracks (vídeo sem legenda ou bloqueado)")
    tracks = json.loads(m.group(1))
    track = next((t for t in tracks if t.get("languageCode") == lang), tracks[0])
    base = track["baseUrl"]
    data = json.loads(_get(base + "&fmt=json3"))
    parts = []
    for ev in data.get("events", []):
        for seg in ev.get("segs", []):
            txt = seg.get("utf8", "").strip()
            if txt and txt != "\n":
                parts.append(txt)
    return " ".join(parts)


if __name__ == "__main__":
    vid = sys.argv[1]
    out = sys.argv[2]
    lang = sys.argv[sys.argv.index("--lang") + 1] if "--lang" in sys.argv else "pt"
    text = fetch_transcript(vid, lang)
    open(out, "w").write(text)
    print(f"{out}: {len(text)} chars")
