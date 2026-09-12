#!/usr/bin/env python3
"""fetch_newsletter.py — baixa o feed RSS do Substack e extrai os artigos em texto limpo.

Gera:
  corpus/newsletter_full.txt       — todos os textos concatenados (fonte de voz escrita)
  newsletter_articles.json         — metadados (título, data, url, slug)

Uso: python3 fetch_newsletter.py [url-do-feed]
"""
import html as _html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"}


def strip_html(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)          # remove tags
    s = _html.unescape(s)                    # &amp; &lt; etc
    s = re.sub(r"&#\d+;", " ", s)            # entidades numéricas
    s = re.sub(r"\s+", " ", s).strip()       # colapsa whitespace
    return s


def fetch(feed_url: str):
    xml = urllib.request.urlopen(urllib.request.Request(feed_url, headers=UA), timeout=30).read()
    root = ET.fromstring(xml)
    items = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        date = (item.findtext("pubDate") or "").strip()
        # corpo completo vem no content:encoded; description é só o resumo. Preferir encoded.
        content = None
        for child in item:
            tag = child.tag.split("}")[-1]
            if tag == "encoded":
                content = child.text or ""
                break
        if not content:
            content = item.findtext("description") or ""
        text = strip_html(content)
        slug = link.rstrip("/").split("/")[-1]
        items.append({"title": title, "url": link, "date": date, "slug": slug, "text": text})

    items.sort(key=lambda x: x["date"], reverse=True)
    full = "\n\n---\n\n".join(f"{i['title']}\n{i['text']}" for i in items if i["text"])
    meta = [{"title": i["title"], "date": i["date"], "url": i["url"], "slug": i["slug"],
             "chars": len(i["text"])} for i in items]
    return full, meta


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://fefaria.substack.com/feed"
    import os
    os.makedirs("corpus", exist_ok=True)
    full, meta = fetch(url)
    open("corpus/newsletter_full.txt", "w").write(full)
    json.dump(meta, open("newsletter_articles.json", "w"), ensure_ascii=False, indent=1)
    print(f"corpus/newsletter_full.txt: {len(full)} chars | {len(meta)} artigos")
    for m in meta[:10]:
        print(f"  {m['date'][:16]}  {m['title'][:55]}  ({m['chars']}c)")
