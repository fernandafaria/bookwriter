# Verificação tripla — Liderando na Era dos Agentes

Data: 12/09/2026. Método: 3 camadas — (1) voz/AI-slop via evals.py + varredura
manual, (2) fabricação/frescor via verify_sources.py, (3) rigor via cross-model
judge (Grok julga o que o DeepSeek gerou).

## Passo 1 — Voz / AI slop (evals.py)

- 29 em-dashes (—) → vírgula/dois-pontos/ponto. É o marcador #1 de GPT.
- 13 headers de seção em CAIXA ALTA → sentence case.
- 1 "não apenas... mas também" → reescrito.
- Resultado: AI score 100 → 54; Fernanda score 100/100.
- Residual: 28 perguntas retóricas (marcador peso 1, o mais leve). É também
  um traço da voz da Fernanda ("fechar com pergunta no ar"), mas a densidade
  (toda seção fecha com pergunta) é o padrão que o evals flagra.

## Passo 2 — Fabricação / frescor (verify_sources.py)

- 14 fontes fabricadas já removidas em passos anteriores.
- Neste passo: 4 "base de conhecimento do livro (2024)" (fonte placeholder) →
  "(caso ilustrativo)".
- Estado: 0 fonte fabricada, 0 estatística desatualizada.

## Passo 3 — Rigor (cross-model judge, Grok)

O juiz (segundo modelo) reprovou o livro em rigor_factual 3-5/10 e apontou
problemas concretos. Corrigidos:

1. "Essa cena não é ficção" contradizia "nome fictício"/"caso ilustrativo" → "cena ilustrativa".
2. 94% vs 92% (mesmo modelo, números diferentes) → unificado em 92%.
3. MATURE inconsistente (Alinhar/Intuitivo/Experimental vs Avaliar/Reativo/Data-Informed) → unificado na tabela canônica (Reativo, Feature Factory, Data-Informed, Product Operating Model, AI-Native).
4. "18% reportam impacto significativo" (McKinsey) → 6% (número real, 5%+ EBIT).
5. "pesquisa própria com 50 líderes, 78%" (pesquisa fabricada) → observação da autora.
6. "dólar a R$ 10" (falso; USD/BRL 2024-2025 ~R$ 5-6) → R$ 6, e corrigiu a conta (US$5k → R$30k).
7. "Em um mundo onde todos têm acesso..." (abertura de GPT) → reescrita.
8. "diferença estatisticamente significativa" (rigor de fachada) → removida.
9. NPS em escala errada (1.8/2.3/4.2, impossível — NPS vai de -100 a +100) → "satisfação" (~31 ocorrências). Os NPS em escala correta (45/50/62/72/74/78) ficaram.

## Estado final

- 8 capítulos + epílogo intactos.
- Voz: sem em-dash, sem CAIXA ALTA, sem "não apenas... mas também". Fernanda 100/100.
- Fontes: 0 fabricada, 0 desatualizada.
- Rigor: os problemas específicos do juiz foram corrigidos, mas o livro ainda
  exige o PASSO HUMANO de auditoria de números (o teto documentado em D-014:
  máquina ~90%, humano fecha os ~10% restantes). O juiz cobriu os 4 primeiros
  blocos; os 2 últimos não foram re-julgados por timeout.

## O que falta (humano)

- Perguntas retóricas: reduzir a densidade (de ~28 para ~8-10), mantendo as
  que fecham capítulo com gancho.
- "Curiosity gap" repetido: "A resposta está na sua relação com dados negativos"
  aparece 5x — variar a frase.
- Re-julgar os blocos 4-5 com o juiz e auditar os números dos cases ilustrativos.
