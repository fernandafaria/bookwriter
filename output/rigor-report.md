# Relatório de verificação de fontes — Liderando na Era dos Agentes

Gerado 12/09/2026. Método: extração determinística (verify_sources.py) +
checagem de existência por título exato (busca web). 53 citações extraídas,
30 únicas verificadas.

## FABRICADO — título/fonte não existe (remover ou reescrever)

1. Google AI, "Production ML Degradation Patterns", 2024 — não existe esse estudo. (O dado real "91% dos modelos degradam" é de outra fonte, MIT/Fiddler, não Google.)
2. Slack Design Blog, "Why We Removed 30% of Settings", 2024 — não existe.
3. Nubank Engineering Blog, "How we scale ML at Nubank", 2024 — não existe.
4. iFood Tech Blog, "Ética em IA no iFood", 2025 — não existe.
5. Shopify Engineering Blog, "Using AI to Analyze Customer Support Patterns" — não existe.
6. Anthropic, "Agentic Workflows for Customer Support Analysis" — não existe.
7. 99 Tech Blog, "Using AI to Understand Ride Cancellation Patterns" — não existe.
8. iFood, "AI and the Future of Delivery" (AI Summit Brazil) — não existe.

## ATRIBUIÇÃO ERRADA — título existe, fonte está errada

9. "Building Resilient AI Teams", 2025 — atribuído a Gartner no livro. É um post do blog ideas2it. NÃO é Gartner. A métrica "rotação reduz 60%" não tem base.
10. "IA em Produto", 2024 — atribuído a "Magazine Luiza Tech Talks". É curso da PM3. Não é Magalu.
11. "The End of Software", 2024 — atribuído a "Martin Casado, a16z". O ensaio real é de Chris Paik (Pace Capital). Autor e veículo errados.
12. Hospital Israelita Albert Einstein, "AI in Emergency Triage: A Case Study" — não existe esse case study.

## NÚMERO ERRADO — fonte real, número divergente

13. "McKinsey 2024: 15% usam IA em múltiplas áreas integrada" → real: 65% (início 2024) → 71% (2025) usam gen AI em ≥1 função; 78% integram (2025).
14. "McKinsey: 21% têm métricas formais de governança (pág. 28)" → não verificável. Citável: 28% dizem CEO tem responsabilidade direta por governança; "88% usam IA, poucos escalam".

## DESATUALIZADO

15. Preços de token (GPT-4o, Claude 3.5 Sonnet, DeepSeek V3) — valores de 2024, livro é 2026. Atualizar ou remover versão de modelo.

## REAL — manter (fonte verificada)

- Peng et al., "The Impact of AI on Developer Productivity" (Copilot, GitHub) — estudo real.
- Zillow Offers, US$ 881M (2021) — WSJ confirma.
- IBM Watson Health, US$ 5 bilhões em aquisições — Slate confirma.
- Stack Overflow Developer Survey 2024 — real.
- Anthropic "Claude 3.5 Sonnet Model Card" — real.
- McKinsey State of AI (todas as edições) — real.

## ILUSTRATIVO — números específicos sem fonte pública (marcar caso composto)

Casos brasileiros com métricas exatas que não têm confirmação: Nubank
(67% fraude, 45→12 dias, rotatividade -40%), Magazine Luiza (20%→65%),
iFood (12 modelos, satisfação +15%), Loggi, 99. Manter como narrativa mas
marcar `*(caso ilustrativo/composto)*` ou remover as métricas exatas.

---

## Padrão que emergiu

- Fontes de elite (McKinsey, WSJ, Slate, papers acadêmicos reais) → reais.
- "Blog post" de empresa e "case brasileiro" com título específico → quase sempre fabricados.
- Título de estudo "com cara de real" (Google, Gartner) → fabricados ou com atribuição errada.

Ação recomendada: remover os 12 itens fabricados/atribuição errada, corrigir
os 2 números McKinsey, atualizar preços, marcar os casos brasileiros como
ilustrativos. Sobra ~10 pontos pra sua decisão final de edição.
