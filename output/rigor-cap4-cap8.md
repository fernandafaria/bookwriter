# Rigor factual — Capítulos 4 e 8 (Liderando na Era dos Agentes)

Levantado em 12/09/2026 por Theo. Verificação via web search (o actor Apify
crawlerbros/google-news-scraper falhou com exitCode 91 em 3 tentativas, proxy
zerado — usei busca nativa, mesmo resultado).

Legenda:
- OK = manter, fonte real confirmada
- NÚMERO ERRADO = corrigir com fonte real
- FABRICADO = fonte/estudo não existe, remover ou reescrever
- ILUSTRATIVO = número específico sem fonte pública, marcar como caso composto ou remover métrica

---

## Capítulo 4 — O Custo Oculto

1. [NÚMERO ERRADO] "McKinsey 2024, apenas 15% das empresas usam IA em múltiplas
   áreas de negócio de forma integrada"
   → Real (State of AI, McKinsey): 65% usam gen AI em ≥1 função (início 2024),
   71% (2025), 78% integram IA (2025). O "15% integrada" não existe como tal.
   Fonte: mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

2. [FABRICADO] "estudo de 2024 da Google: modelos perdem 15-25% ao sair do
   laboratório" (Google AI, "Production ML Degradation Patterns", 2024)
   → Não existe esse estudo/título. A literatura de model drift existe, mas não
   sob essa citação. Reescrever sem fonte fake, ou citar literatura real de
   MLops sobre degradação em produção.

3. [OK] Zillow Offers, prejuízo US$ 881 milhões (2021)
   → Confirmado. WSJ: "Zillow's Shuttered Home-Flipping Business Lost $881
   Million in 2021". Demissão ~2.000 (≈25%). Manter.

4. [OK] IBM Watson Health, "mais de US$ 5 bilhões"
   → Confirmado como "US$ 5 bilhões só em aquisições" (Slate, 2022). Manter,
   mas precisar a redação: "US$ 5 bilhões em aquisições" (não "investimentos
   e aquisições" vagos).

5. [DESATUALIZADO] Preços de token: GPT-4o US$2,50/$10, Claude 3.5 Sonnet
   US$3/$15, DeepSeek V3 US$0,27/$1,10
   → São preços de 2024. Num livro de 2026, remover nomes de versão/modelo ou
   atualizar. Melhor: dar ordem de grandeza sem versão específica.

6. [ILUSTRATIVO] Caso Nubank/Maria Silva: 67% redução em fraude, 72h→15min
   → Métricas específicas sem fonte pública. Marcar como caso ilustrativo
   (a abertura já é "reconstituição"). Remover os números exatos ou assumir
   o marcador.

---

## Capítulo 8 — Cultura que Adota e Ética que Protege

7. [NÃO CONFIRMADO] "McKinsey maio 2024, 21% têm métricas formais de
   governança (página 28)"
   → O "21%" específico não é verificável. Real e citável: 28% dizem que o CEO
   tem responsabilidade direta por governança de IA (Knostic citando McKinsey);
   "88% usam IA, poucos escalam"; "1% se consideram maduros". Substituir por
   número verificável.

8. [FABRICADO] "Gartner 2025, rotação de responsabilidades reduz 60% o tempo de
   recuperação" (Gartner, "Building Resilient AI Teams", 2025, pág. 12)
   → Não existe esse relatório Gartner. Busca retorna nada relevante. Remover a
   fonte e a métrica; se quiser manter a ideia, reformular sem atribuição.

9. [ILUSTRATIVO] Nubank: 45→12 dias deploy, rotatividade -40% (2022-2024),
   "Nubank Engineering Blog 2024"
   → Números específicos sem fonte pública confirmada. Marcar ilustrativo.

10. [ILUSTRATIVO] Magazine Luiza: 80 pessoas no time, 20%→65% produção,
    "Magazine Luiza Tech Talks 2024"
    → Idem. Marcar ilustrativo.

11. [ILUSTRATIVO] iFood: 12 modelos corrigidos (2024), satisfação +15%,
    "iFood Tech Blog 2025"
    → Idem. Marcar ilustrativo.

12. [NÃO CONFIRMADO] "artigo da Folha de S.Paulo sobre IA no varejo (2024)"
    → Não verificado. Remover a referência ou substituir por fonte real.

---

## Resumo do passe

- 2 claims OK (Zillow, IBM Watson) — manter.
- 2 fontes FABRICADAS (Google degradation, Gartner resilient teams) — remover.
- 2 números McKinsey errados/vagos (15%, 21%) — substituir por reais (65/71/78%, 28%).
- 4 casos brasileiros com métricas ilustrativas — marcar `*(caso ilustrativo/composto)*`.
- 1 tabela de preço desatualizada — atualizar.

## Nota sobre Apify

O actor Google News (crawlerbros) falha com exitCode 91 (proxy não alcança o
Google). Pra usar Apify no pipeline de rigor, precisa de actor com proxy
residencial (a maioria dos scrapers de Google News exige). Alternativa confiável
e sem custo: web_search nativo + web_extract, como usei aqui.
