#!/usr/bin/env python3
"""voice_ingest.py — extrai marcadores de voz de um transcript e gera delta pro FERNANDA_VOICE.

Parte do "voice pipeline": podcast/entrevista da Fernanda → transcript → marcadores → FERNANDA_VOICE.

Uso:
  python3 voice_ingest.py <transcript.txt>     # gera voice_delta.json + preview legível
  python3 voice_ingest.py --selftest           # valida parse/merge sem chamar API

A aplicação no knowledge_base.py é MANUAL (revisar o delta antes de patch). Voz é o ativo mais valioso.
"""
import os, re, json, sys, urllib.request


def load_env(path):
    for line in open(path):
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        os.environ.setdefault(k, v.strip().strip('"').strip("'"))


VOICE_KEYS = ("signature_openings", "tone_markers", "structural_pattern", "vocabulary")

PROMPT = """Você é um analista de estilo. Dado o transcript abaixo de uma pessoa (Fernanda Faria) falando em podcast/entrevista, extraia as características da voz DELA para escrever texto "com a cara dela".

Retorne APENAS um JSON válido (sem markdown, sem comentários) neste formato exato:
{
  "signature_openings": ["frase literal de abertura de história, 4-12 palavras", ...],
  "tone_markers": ["padrão de tom com frase de efeito, ex: 'Direta, sem pedir licença'", ...],
  "structural_pattern": ["passo 1 de como ela argumenta", "passo 2", ...],
  "vocabulary": {
    "uses": ["gíria/marca coloquial real dela (bora, tá, a gente, troço...)", ...],
    "avoids": ["jargão de consultoria ou clichê que ela critica/zoa", ...]
  }
}

Regras:
- Só inclua o que aparece EXPLICITAMENTE no transcript. Não invente.
- 3-6 itens por campo, no máximo. Prefira qualidade a quantidade.
- signature_openings = frases literais (não descreva, copie).
- vocabulary.avoids = o que ela rejeita/critica, não só o que ela não disse.

TRANSCRIPT:
{transcript}
"""


def call_deepseek(transcript: str) -> str:
    body = json.dumps({"model": "deepseek-chat", "temperature": 0, "messages": [
        {"role": "user", "content": PROMPT.replace("{transcript}", transcript[:60000])}
    ]}).encode()
    req = urllib.request.Request(
        "https://api.deepseek.com/chat/completions", data=body,
        headers={"Authorization": "Bearer " + os.environ["DEEPSEEK_API_KEY"],
                 "Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=300).read())
    return r["choices"][0]["message"]["content"]


def parse_json(content: str):
    m = re.search(r"\{.*\}", content, re.DOTALL)
    return json.loads(m.group(0)) if m else None


def merge_voice(current: dict, delta: dict) -> dict:
    """Adiciona itens do delta ao FERNANDA_VOICE, sem duplicar, preservando ordem."""
    out = json.loads(json.dumps(current))
    for key in VOICE_KEYS:
        if key not in delta or not delta[key]:
            continue
        val = delta[key]
        if isinstance(val, list):
            seen = list(out.get(key, []))
            for item in val:
                if item not in seen:
                    seen.append(item)
            out[key] = seen
        elif isinstance(val, dict):  # vocabulary
            sub = out.setdefault(key, {})
            for k, vals in val.items():
                if vals:
                    cur = list(sub.get(k, []))
                    for v in vals:
                        if v not in cur:
                            cur.append(v)
                    sub[k] = cur
    return out


def preview(delta: dict) -> str:
    lines = ["## Delta de voz extraído\n"]
    for key in ("signature_openings", "tone_markers", "structural_pattern"):
        if delta.get(key):
            lines.append(f"**{key}:**")
            for item in delta[key]:
                lines.append(f"  - {item}")
    if delta.get("vocabulary"):
        lines.append("**vocabulary.uses:** " + ", ".join(delta["vocabulary"].get("uses", [])))
        lines.append("**vocabulary.avoids:** " + ", ".join(delta["vocabulary"].get("avoids", [])))
    return "\n".join(lines)


def selftest():
    current = {
        "signature_openings": ["Era uma terça-feira..."],
        "tone_markers": ["Direta, sem pedir licença"],
        "structural_pattern": ["1. Gancho"],
        "vocabulary": {"uses": ["bora"], "avoids": ["sinergia"]},
    }
    delta = {
        "signature_openings": ["Era uma terça-feira...", "Quantas vezes você já..."],
        "tone_markers": ["Direta, sem pedir licença", "Antipática com hype"],
        "structural_pattern": ["1. Gancho", "2. Problema"],
        "vocabulary": {"uses": ["bora", "troço"], "avoids": ["sinergia", "alavancar"]},
    }
    out = merge_voice(current, delta)
    assert out["signature_openings"] == ["Era uma terça-feira...", "Quantas vezes você já..."]
    assert out["vocabulary"]["uses"] == ["bora", "troço"]
    assert out["vocabulary"]["avoids"] == ["sinergia", "alavancar"]
    # parse_json com resposta realista
    assert parse_json('```json\n{"a": 1}\n```') == {"a": 1}
    assert parse_json("sem json") is None
    print("SELFTEST OK: merge dedup + parse tolerante")


def main():
    if "--selftest" in sys.argv:
        selftest()
        return
    if len(sys.argv) < 2:
        print("Uso: python3 voice_ingest.py <transcript.txt>  |  --selftest")
        sys.exit(1)
    load_env(os.path.expanduser("~/.hermes/.env"))
    transcript = open(sys.argv[1]).read()
    print(f"Transcript: {len(transcript)} chars → DeepSeek...", file=sys.stderr)
    content = call_deepseek(transcript)
    delta = parse_json(content)
    if not delta:
        print("Falha ao parsear. Resposta crua:", file=sys.stderr)
        print(content)
        sys.exit(1)
    json.dump(delta, open("voice_delta.json", "w"), ensure_ascii=False, indent=1)
    print(preview(delta))
    print("\nSalvo em voice_delta.json. Revisar e aplicar manualmente no knowledge_base.py FERNANDA_VOICE.")


if __name__ == "__main__":
    main()
