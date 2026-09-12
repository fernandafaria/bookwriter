# book_writer — Editora Agêntica

Pipeline multiagente (LangGraph) para escrever livros na voz da Fernanda,
com rigor factual em 5 camadas.

## Arquitetura

```
Researcher → FactSheet → Strategist → Writer → FactChecker → CopyEditor
            → AuthenticityFixer → Verifier → EditorChefe (loop REVISE)
```

9 nós. Um judge LLM-as-a-Judge (10 dimensões, gate 9/10) avalia cada capítulo.
Rigor factual tem teto ~7/10 — o que o judge sinaliza exige conferência humana (~5 min/cap).

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Chaves de API em `~/.hermes/.env` (`DEEPSEEK_API_KEY`, `OPENROUTER_API_KEY`, `XAI_API_KEY`).

## Rodar

```bash
# escrever um capítulo (15–30 min; rode em background)
python3 -u -m book_writer.run --brief book_writer/briefs/exemplo.json --chapter 1 --max-revisions 1

# avaliar o capítulo mais recente
cd book_writer && python3 judge.py "$(ls -t ../output/capitulo-*.md | head -1)"

# self-test do invariante de rastreabilidade (sem rede)
python3 -m book_writer.voice_postprocess
```

## Briefs

- `book_writer/briefs/exemplo.json`
- `book_writer/briefs/decisor-pos-ai.json`
- `book_writer/briefs/executivo-alta-performance.json`
- `book_writer/briefs/personas-sinteticas.json`

## Modelos

- Gerador: `deepseek-chat`
- Judge: `deepseek-reasoner` (vendor diferente do gerador)
- Grok: `BOOK_LLM_PROVIDER=grok` (via `XAI_API_KEY`)
