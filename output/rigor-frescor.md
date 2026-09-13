# Frescor de dados — substituições aplicadas

12/09/2026. Direcional: referências de estatística devem ser dos últimos 12
meses (2025+). Casos históricos (Zillow 2021, IBM Watson 2018) ficam.

## Substituições aplicadas ao manuscrito (8)

1. McKinsey "89% Fortune 500, 2023" → "78% integram IA (McKinsey State of AI, 2025)"
2. Peng/Copilot "Microsoft Research, 2022" → "2024" (correção de ano; estudo real)
3. BCG "2x chance de liderar, 2023" → "1,7x crescimento de receita, future-built (BCG, 2025)"
4. Datafolha/Bain "78% usaram IA, 2023" → "93% usam ferramenta de IA, 54% entendem (Datafolha/Fundação Itaú, 2025)"
5. Grand View "US$ 207,9 bi em 2023" → "US$ 390,9 bi em 2025, US$ 3,5 tri até 2033 (GVR, 2026)"
6. McKinsey "15% múltiplas áreas, 2024" → "71% usam gen AI em ≥1 função (McKinsey, 2025)"
7. Stack Overflow "76%, 2024" → "84% usam ferramentas de IA (SO Developer Survey, 2025)"
8. McKinsey "21% governança, 2024" → "28% CEO responsável por governança (McKinsey, 2025)"

## O que NÃO foi alterado (decisão sua)

- Casos históricos (Zillow 2021, IBM Watson 2018-2022, Loggi 2022): são história,
  ficam como referência de caso, não estatística.
- Peng et al. (Copilot 55,8%): estudo real e marco, mas é de 2024. Mantive com
  ano corrigido; se quiser estrito "12 meses", trocar por estudo 2025.
- Fontes FABRICADAS (Google degradation, Gartner resilient, blogs de caso
  brasileiro): não é questão de frescor, é remoção. Ver rigor-report.md.

## Gate determinístico

`book_writer/verify_sources.py` agora classifica cada citação também por
frescor: estatística com ano < 2025 vira `desatualizada` (salvo caso
histórico, detectado por sinal de caso/zillow/watson/filing). Rodar:

  python3 book_writer/verify_sources.py output/Liderando_na_Era_dos_Agentes.md > output/claims.json
