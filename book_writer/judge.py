#!/usr/bin/env python3
"""judge.py — LLM-as-a-Judge para capítulos de livro.

Valida um capítulo com rubrica objetiva usando um modelo DIFERENTE do gerador
(Claude via OpenRouter por default — o pipeline gera com deepseek-chat) pra
evitar auto-preferência.

Uso:
  python3 judge.py <capitulo.md>                 # julga com o modelo default (OpenRouter/Claude)
  python3 judge.py <capitulo.md> --model deepseek  # força DeepSeek (mesmo vendor, menos ideal)
  python3 judge.py --selftest                     # valida parse sem chamar API
"""
import json, os, re, sys, urllib.request


def load_env(path):
    for line in open(path):
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        os.environ.setdefault(k, v.strip().strip('"').strip("'"))


RUBRIC = """Você é um editor-chefe imparcial avaliando um capítulo de livro de não-ficção
escrito por Fernanda Faria (líder de produto e IA, brasileira, voz anti-hype).

Avalie o capítulo em 10 dimensões, cada uma de 0 a 10:

1. TESE (0-10): tem uma tese central clara e a desenvolve sem divagar?
2. ESTRUTURA (0-10): segue a estrutura de não-ficção (cena de abertura -> problema -> framework -> casos reais -> guia prático -> fechamento com gancho)?
3. VOZ AUTORAL (0-10): soa como a autora (cena real com nome/cargo/data, coloquial, direta, anti-hype) e NÃO tem "cara de GPT" (clichês, em-dash, "é importante ressaltar", "em um mundo cada vez mais")?
4. CONCRETUDE (0-10): os casos e exemplos são reais e NOMEADOS (empresa + fonte verificável), ou anônimos/genéricos que parecem inventados? Caso composto é marcado como composto?
5. ATRIBUIÇÃO (0-10): frameworks, modelos e ideias de terceiros são creditados explicitamente? Não há plágio conceitual (usar o framework de outro autor sem citar)?
6. ADESÃO AO BRIEF (0-10): o capítulo segue a tese, o ângulo e a audiência pedidos no brief, sem divergir para outro tema?
7. RIGOR FACTUAL (0-10): dados e métricas têm fonte verificável? Há números redondos demais ou afirmações que parecem fabricadas?
8. APLICABILIDADE (0-10): o leitor sai com algo acionável (checklist, timeline, framework)?
9. ORIGINALIDADE (0-10): tem ideia original ou recicla conteúdo genérico de autoajuda?
10. CONCISÃO (0-10): sem enrolação, sem repetição, cada parágrafo puxa peso?

Depois dê:
- verdict: APPROVE | REVISE | REJECT (APPROVE apenas se TODAS as dimensões forem >= 9; REVISE se alguma entre 6 e 8; REJECT se alguma < 6)
- top_problems: 2-4 problemas concretos, cada um citando o trecho EXATO do capítulo (quote curto de até 60 chars) e por que é problema
- summary: 1-2 frases

Retorne APENAS JSON válido (sem markdown, sem comentários):
{
  "scores": {"tese": 9, "estrutura": 9, "voz_autoral": 9, "concretude": 8, "atribuicao": 9, "adesao_brief": 9, "rigor_factual": 8, "aplicabilidade": 9, "originalidade": 9, "concisao": 9},
  "total": 88,
  "verdict": "REVISE",
  "top_problems": [{"quote": "trecho exato", "problem": "por que é problema"}],
  "summary": "resumo de 1-2 frases"
}

CAPÍTULO:
{chapter}
"""


def call_openrouter(chapter):
    key = os.environ.get("OPENROUTER_API_KEY", "")
    body = json.dumps({
        "model": "openai/gpt-4o-mini",
        "temperature": 0,
        "messages": [{"role": "user", "content": RUBRIC.replace("{chapter}", chapter[:30000])}],
    }).encode()
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=300).read())
    return r["choices"][0]["message"]["content"]


def call_deepseek(chapter):
    key = os.environ.get("DEEPSEEK_API_KEY", "")
    body = json.dumps({
        "model": "deepseek-reasoner", "temperature": 0,
        "messages": [{"role": "user", "content": RUBRIC.replace("{chapter}", chapter[:30000])}],
    }).encode()
    req = urllib.request.Request("https://api.deepseek.com/chat/completions", data=body,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=300).read())
    return r["choices"][0]["message"]["content"]


def parse_json(content):
    m = re.search(r"\{.*\}", content, re.DOTALL)
    return json.loads(m.group(0)) if m else None


def render(result):
    s = result.get("scores", {})
    dims = ["tese", "estrutura", "voz_autoral", "concretude", "atribuicao", "adesao_brief",
            "rigor_factual", "aplicabilidade", "originalidade", "concisao"]
    lines = ["## Veredito do juiz (LLM)\n"]
    for d in dims:
        v = int(s.get(d, 0))
        bar = "█" * v + "░" * (10 - v)
        flag = "  ⚠ <9" if v < 9 else ""
        lines.append(f"  {d:16} {v:>2}/10  {bar}{flag}")
    lines.append(f"\n  TOTAL: {result.get('total', '?')}/100  ->  {result.get('verdict', '?')}")
    lines.append(f"\n  {result.get('summary', '')}")
    if result.get("top_problems"):
        lines.append("\n**Problemas:**")
        for p in result["top_problems"]:
            lines.append(f"  - \"{p.get('quote', '')}\" -> {p.get('problem', '')}")
    return "\n".join(lines)


def selftest():
    sample = '{"scores":{"tese":9,"estrutura":9,"voz_autoral":9,"concretude":8,"atribuicao":9,"adesao_brief":9,"rigor_factual":8,"aplicabilidade":9,"originalidade":9,"concisao":9},"total":88,"verdict":"REVISE","top_problems":[{"quote":"x","problem":"y"}],"summary":"ok"}'
    r = parse_json('```json\n' + sample + '\n```')
    assert r["verdict"] == "REVISE" and r["scores"]["concretude"] == 8
    assert parse_json("sem json") is None
    print("SELFTEST OK")


def main():
    if "--selftest" in sys.argv:
        selftest()
        return
    if len(sys.argv) < 2:
        print("Uso: python3 judge.py <capitulo.md> [--model openrouter|deepseek]  |  --selftest")
        sys.exit(1)
    load_env(os.path.expanduser("~/.hermes/.env"))
    chapter = open(sys.argv[1]).read()
    model = "openrouter" if "--model" in sys.argv and sys.argv[sys.argv.index("--model") + 1] == "openrouter" else "deepseek"
    print(f"Juiz: {model} ({len(chapter)} chars)...", file=sys.stderr)
    content = call_openrouter(chapter) if model == "openrouter" and os.environ.get("OPENROUTER_API_KEY") else call_deepseek(chapter)
    result = parse_json(content)
    if not result:
        print("Falha ao parsear. Resposta crua:\n" + content)
        sys.exit(1)
    json.dump(result, open("judge_verdict.json", "w"), ensure_ascii=False, indent=1)
    print(render(result))
    print("\nSalvo em judge_verdict.json")


if __name__ == "__main__":
    main()
