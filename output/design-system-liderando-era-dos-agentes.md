# Design System — Liderando na Era dos Agentes

**Autora:** Fernanda Faria
**Design System por:** Iza (core — taste-judge, protect-restraint)
**Versão:** 1.0 — 15 de junho de 2026

---

## Sumário

1. [Princípios de Design](#1-princípios-de-design)
2. [Inventário de Frameworks — Diagramação](#2-inventário-de-frameworks--diagramação)
3. [Capa do Livro](#3-capa-do-livro)
4. [Tipografia e Layout Interno](#4-tipografia-e-layout-interno)
5. [Worksheets/Canvas — Linguagem Visual](#5-worksheetscanvas--linguagem-visual)
6. [Referências Visuais](#6-referências-visuais)
7. [Especificações Técnicas Finais](#7-especificações-técnicas-finais)

---

## 1. Princípios de Design

### 1.1 Voz visual em 5 palavras

| Palavra | O que significa no design |
|---------|--------------------------|
| **Direto** | Layout sem enfeite. Sem sombra desnecessária. Sem gradiente cosmético. Cada elemento tem função. |
| **Brasileiro** | A paleta respira Brasil sem ser caricata (não é verde-amarelo, não é tropical-kitsch). É a luz, a terra, a matéria. |
| **Executivo** | Precisão tipográfica, grid rigoroso, hierarquia clara. Quem pega o livro sente que foi feito para quem decide. |
| **Quente** | Apesar de executivo, o livro não é frio. Não é azul-corporativo-genérico. Tem calor de quem opera o chão de fábrica. |
| **Antipático com hype** | Nada de roxo-IA, nada de gradiente "futurista", nada de ícone de engrenagem com cérebro. IA é ferramenta, não identidade. |

### 1.2 Regras de ouro da Iza (traduzidas para o design)

1. **Menos é mais.** Se um framework cabe em meia página, não ocupe uma página inteira. Espaço em branco é generosidade com o leitor, não desperdício.
2. **Consistência > criatividade.** Todos os 13 frameworks devem parecer da mesma família. Mesma tipografia, mesma paleta, mesmas regras de grid.
3. **Brasileiro, não genérico.** As cores vêm da terra brasileira — argila, cerrado, concreto paulistano, céu de Brasília.
4. **O texto é o protagonista.** O design serve ao conteúdo. Diagramas existem para clarear, não para impressionar.

---

## 2. Inventário de Frameworks — Diagramação

Cada framework abaixo recebe: tipo de visualização, paleta específica (dentro da paleta-mestre), layout, orientação e dimensões sugeridas.

### Paleta-Mestre do Livro

```
┌─────────────────────────────────────────────────────────────┐
│  CORES PRIMÁRIAS                                            │
│                                                             │
│  Argila (principal)        #C44536  ████████  RGB(196,69,54)│
│  Concreto (base)           #2D2A26  ████████  RGB(45,42,38) │
│  Papel (fundo)             #FAF7F2  ████████  RGB(250,247,242)│
│  Cinza-quente (texto)      #4A4540  ████████  RGB(74,69,64) │
│                                                             │
│  CORES DE APOIO                                             │
│                                                             │
│  Cerrado (verde seco)      #7A8B3E  ████████  RGB(122,139,62)│
│  Terra (marrom)            #A67C52  ████████  RGB(166,124,82)│
│  Céu (azul apagado)        #6B8A9E  ████████  RGB(107,138,158)│
│  Alerta (âmbar)            #D4A24E  ████████  RGB(212,162,78)│
│                                                             │
│  ESCALA DE CINZAS (quentes)                                 │
│                                                             │
│  Cinza 100                 #F5F2ED  ████████                 │
│  Cinza 200                 #E8E3DC  ████████                 │
│  Cinza 300                 #D1CBC3  ████████                 │
│  Cinza 400                 #A9A29A  ████████                 │
│  Cinza 500                 #7A736B  ████████                 │
│  Cinza 600                 #4A4540  ████████                 │
│  Cinza 700                 #2D2A26  ████████                 │
│                                                             │
│  CORES FUNCIONAIS (para checklists ❌/✅)                     │
│                                                             │
│  ❌ Erro/Armadilha           #C44536  (mesma argila,         │
│                                        intenção diferente)   │
│  ✅ Acerto/Caminho           #5A8A4A  ████████  RGB(90,138,74)│
│  ⚠️ Alerta                   #D4A24E  (âmbar)               │
│  💡 Insight                  #7A8B3E  (cerrado)             │
│  📊 Dado                     #6B8A9E  (céu)                 │
└─────────────────────────────────────────────────────────────┘
```

---

### Framework 1: AI Trap — 5 Sinais com ❌/✅

**Localização:** Capítulo 1, Seção 3
**Descrição:** 5 sintomas da armadilha de IA, cada um com versão ❌ (errada) e ✅ (correta). Originalmente descrito com 3 sintomas no texto, expandido no livro para incluir mais dimensões de armadilha.

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | Tabela comparativa de duas colunas (❌ vs ✅) com 5 linhas |
| **Paleta** | ❌ = `#C44536` (argila, 15% de opacidade no fundo da célula). ✅ = `#5A8A4A` (verde-acerto, 15% de opacidade no fundo). Texto = `#2D2A26` |
| **Layout** | Orientação retrato. Título do sintoma em bold `#2D2A26` à esquerda, duas células lado a lado. Altura de cada linha: ~14mm. Largura total: coluna de texto. |
| **Dimensão** | Largura total da mancha de texto (~120mm). 5 linhas × 14mm = 70mm de altura + 10mm de cabeçalho = ~80mm total. Cabe em meia página. |
| **Hierarquia** | Título "AI Trap Framework" em argila. Subtítulo "5 sinais de que você está na armadilha" em cinza-quente 70%. Linhas alternadas com fundo Cinza 100 para leitura. |
| **Destaque** | Se o leitor marcar ≥3 ❌, callout box "⚠️ Você está na AI Trap. Vá para o Capítulo 2." |

**Conteúdo dos 5 sinais (extraídos do livro):**

| # | Sinal | ❌ Errado | ✅ Certo |
|---|-------|-----------|----------|
| 1 | Métricas | "Aumentamos accuracy de 89% para 92%!" | "O NPS melhorou? O churn diminuiu?" |
| 2 | Solução antes do problema | "Vamos colocar IA no chat. Depois a gente vê." | "Qual o maior problema de atendimento hoje?" |
| 3 | Ignorar contexto | "O modelo funciona nos dados de treino." | "Testamos com usuários reais? Em cenários reais?" |
| 4 | Feature factory | "Entregamos no prazo, mas ninguém usa." | "Validamos com 15 clientes antes de construir." |
| 5 | Celebrar lançamento | "Features shipped este mês: 12." | "Problemas resolvidos este mês: 3." |

---

### Framework 2: MATURE — Maturity Model (N1 → N5)

**Localização:** Capítulo 2
**Descrição:** Escada de 5 níveis de maturidade de produto, do Reativo (N1) ao AI-Native (N5). Cada nível descreve como o time decide, o sinal de alerta e o que acontece com IA.

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Escada ascendente** com 5 degraus. Não é uma pirâmide (não sugere que poucos chegam ao topo). É uma escada: você sobe degrau por degrau. |
| **Paleta** | Degraus em gradiente de terra: N1 = `#D1CBC3` (cinza 300, reativo), N2 = `#A9A29A` (cinza 400), N3 = `#A67C52` (terra), N4 = `#C44536` (argila), N5 = `#7A8B3E` (cerrado, excelência). Texto do nome do nível em branco `#FAF7F2` sobre o degrau. |
| **Layout** | Orientação paisagem (página dupla ou página inteira em formato largo). Degraus inclinados ~15° subindo da esquerda para a direita. Abaixo de cada degrau: 3 linhas de texto descritivo em Cinza 600. |
| **Dimensão** | Página dupla: 240mm × 170mm. Cada degrau: ~40mm de largura × 15mm de altura. Espaçamento entre degraus: 8mm. |
| **Hierarquia** | Nome do nível em destaque (bold, 11pt). Sigla do acrônimo M-A-T-U-R-E abaixo. Sinal de alerta em itálico. Caixa de "Exemplo real" em Cinza 100 com borda esquerda de 3px na cor do degrau. |
| **Detalhe** | Cada degrau tem um ícone minimalista (linha, não preenchido): N1 = ponto de interrogação, N2 = engrenagem, N3 = gráfico de barras, N4 = triângulo (play), N5 = círculo (ciclo). |

**Conteúdo dos 5 níveis:**

| Nível | Acrônimo | Nome | Como decide | Sinal de alerta |
|-------|----------|------|-------------|-----------------|
| N1 | M — Mapear | Reativo | Por instinto ou crise | "O CEO pediu, a gente faz" |
| N2 | A — Avaliar | Feature Factory | Por prioridade do stakeholder mais alto | "Entregamos no prazo, mas ninguém usa" |
| N3 | T — Testar | Data-Informed | Por dados quantitativos | "O dado diz X, mas o cliente diz Y" |
| N4 | U — Usar | Product Operating Model | Por experimentos com usuários reais | "Aprendemos mais com o fracasso do que com o sucesso" |
| N5 | R — Refinar | AI-Native | Por aprendizado contínuo do sistema | "O modelo aprende sozinho, mas o time não" |

**Elemento extra — Automation Matrix (2×2):**
Mesmo capítulo. Matriz 2×2 com eixos: "Capacidade de Automação" (X, Baixa→Alta) e "Desejo de Automação" (Y, Baixo→Alto). 4 zonas coloridas: Green (`#7A8B3E`), Yellow (`#D4A24E`), Red (`#C44536`), White (`#E8E3DC`). Tamanho: meia página (80mm × 80mm). Cada zona tem 1 exemplo de 1 linha.

---

### Framework 3: B³ Matrix — Build, Buy, Borrow

**Localização:** Capítulo 3
**Descrição:** Matriz de decisão com 5 eixos × 3 caminhos. Ajuda o leitor a decidir entre construir, comprar ou tomar emprestado (open-source/parceria).

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Matriz 5×3** (5 eixos como linhas, 3 caminhos como colunas) + **Radar/Spider opcional** para visualização rápida. A tabela é a peça principal; o radar é complemento. |
| **Paleta** | Build = `#C44536` (argila, construir exige coragem), Buy = `#6B8A9E` (céu, comprar é pragmático), Borrow = `#A67C52` (terra, tomar emprestado é híbrido). Cabeçalhos em branco sobre cor sólida. Células preenchidas com 10% de opacidade da cor da coluna. |
| **Layout** | Orientação paisagem (página inteira). Tabela com 6 linhas (cabeçalho + 5 eixos) × 4 colunas (eixo + 3 caminhos). Abaixo da tabela: 3 mini-cards com descrição de cada caminho. |
| **Dimensão** | Tabela: 160mm × 70mm. Mini-cards: 3 colunas de ~50mm cada × 40mm. Total: ~120mm de altura. |
| **Hierarquia** | Título "Matriz B³" em argila, 18pt. Subtítulo "5 eixos. 3 caminhos. 1 decisão." em Cinza 500, 11pt. |

**Conteúdo da tabela:**

| Eixo | Build | Buy | Borrow |
|------|-------|-----|--------|
| Diferenciação | Core | Commodity | Média |
| Velocidade | Baixa (meses) | Alta (semanas) | Média (1-3 meses) |
| Maturidade do time | Alta (nível 3+) | Baixa (nível 1-2) | Média (nível 2-3) |
| TCO | Alto no início, menor em escala | Baixo no início, maior em escala | Médio |
| Lock-in | Baixo | Alto | Médio |

---

### Framework 4: Custo Real Calculator — Worksheet

**Localização:** Capítulo 4
**Descrição:** Tabela preenchível com 9 linhas para o leitor calcular o custo real de um projeto de IA. Inclui versão preenchida como exemplo (chatbot de atendimento, 50k conversas/mês).

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Worksheet preenchível** — tabela com 3 colunas: Item, Fórmula, Seu número. Linhas de input com fundo branco e borda tracejada `#D1CBC3`. O exemplo preenchido fica em página separada ou em box destacada. |
| **Paleta** | Fundo da worksheet: `#FAF7F2` (papel). Linhas de input: borda tracejada `#A9A29A` (cinza 400), fundo branco `#FFFFFF`. Linha de resultado (CUSTO TOTAL): fundo `#C44536` com 10% opacidade, texto bold. Exemplo preenchido: selo "EXEMPLO" no canto superior direito em `#6B8A9E` (céu). |
| **Layout** | Orientação retrato. Worksheet ocupa ~70% da largura da mancha. À direita: mini callouts com dicas. Abaixo: box com exemplo preenchido em Cinza 100. |
| **Dimensão** | Worksheet: 100mm × 120mm. Exemplo: 100mm × 80mm. Total: ~210mm (cabe em uma página). |
| **Hierarquia** | Título "Custo Real Calculator" em argila. Subtítulo: "Preencha com seus números. É o que seu CFO vai pedir." em Cinza 500. Campos a preencher indicados com `________` (sublinhado pontilhado). |
| **Diferenciador visual** | Campos preenchíveis têm linha pontilhada cinza. Campos do exemplo têm fundo Cinza 100 e texto em Cinza 700. O leitor nunca confunde "preencha aqui" com "exemplo". |

---

### Framework 5: CFO Primer — Tabela Comparativa de Modelos

**Localização:** Capítulo 4, Seção 5
**Descrição:** Tabela comparando GPT-4o, Claude 3.5 Sonnet e DeepSeek V3 em custo por token, latência e casos de uso.

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Tabela comparativa 4×4** (Modelo × Preço entrada, Preço saída, Latência típica, Melhor para). Mini cards com "selo" de cada provedor. |
| **Paleta** | OpenAI = `#10A37F` (verde OpenAI brand, sutil), Anthropic = `#D4A24E` (âmbar), DeepSeek = `#6B8A9E` (céu). Cabeçalho neutro em Cinza 700. |
| **Layout** | Orientação retrato. Tabela em meia página (~80mm largura). Abaixo: 3 parágrafos sobre Tokens, Latência, Rate Limits e Inference vs Fine-tuning — diagramados como callouts laterais. |
| **Dimensão** | Tabela: 100mm × 55mm. Callouts: 3 boxes de ~55mm × 35mm cada em layout de 3 colunas. |
| **Hierarquia** | Título "O que seu CFO precisa saber sobre IA (em 5 minutos)" — tom direto, não técnico. |

---

### Framework 6: THA — Trio Humano-Agente

**Localização:** Capítulo 5
**Descrição:** Três papéis que todo time de produto com IA precisa ter: Explorador (Agente), Validador (Humano PM), Sintetizador (Híbrido).

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Diagrama de Venn com 3 círculos sobrepostos** no centro + **3 colunas descritivas** abaixo. Cada círculo representa um papel. A intersecção central é o Sintetizador. |
| **Paleta** | Explorador (Agente) = `#6B8A9E` (céu, azul apagado — tecnológico mas não frio). Validador (Humano) = `#C44536` (argila, humano, quente). Sintetizador (Híbrido) = `#7A8B3E` (cerrado, intersecção dos dois). |
| **Layout** | Topo: diagrama de Venn com 3 círculos (~60mm de diâmetro cada). Centro da intersecção rotulado "Sintetizador". Abaixo: 3 colunas de texto (~55mm cada) descrevendo cada papel em detalhe. |
| **Dimensão** | Diagrama: 120mm × 70mm. Colunas: 160mm × 80mm. Total: ~160mm (cabe em 2/3 de página). |
| **Hierarquia** | Título "THA — Trio Humano-Agente" em Cinza 700. Cada papel com nome, ícone e descrição de 3-4 linhas. |

**Ícones (linha, minimalistas):**
- Explorador: lupa ou radar
- Validador: escudo com check
- Sintetizador: dois losangos se sobrepondo (decisão)

---

### Framework 7: Gerente-Informante — Checklist de 4 Sinais

**Localização:** Capítulo 5, Seção 5
**Descrição:** Checklist de autodiagnóstico para identificar se você é um "gerente-informante" (função que o THA elimina).

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Checklist vertical** com 4 itens, cada um com checkbox quadrado. Abaixo: medidor visual "Se 3 de 4 forem verdade..." |
| **Paleta** | Checkboxes vazados em `#C44536` (argila). Itens marcados com ❌ (se verdadeiro, problema). Medidor: barra horizontal com 4 segmentos, preenchendo da esquerda (0) para direita (4). Segmentos 1-2 = `#D4A24E` (âmbar, alerta), 3-4 = `#C44536` (argila, crítico). |
| **Layout** | Orientação retrato. Meia página (~80mm de largura). Caixa com fundo Cinza 100, borda esquerda argila 4px. |
| **Dimensão** | 90mm × 70mm total. |
| **Hierarquia** | Título "O gerente-informante acabou" em argila. Subtítulo "4 sinais de que sua função some em 6 meses." |

---

### Framework 8: Scale-Down — Time de 3 vs Time de 1

**Localização:** Capítulo 5, Seção 6
**Descrição:** Como aplicar o THA em times pequenos. Diagrama comparando time de 3 pessoas e founder solo.

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Dois diagramas de pizza/donut lado a lado** mostrando distribuição de papéis. Time de 3: 3 fatias rotuladas. Time de 1: fatia única com anotações de acúmulo. Abaixo: rituais enxutos em 3 linhas. |
| **Paleta** | Mesma paleta do THA: Explorador = `#6B8A9E`, Validador = `#C44536`, Sintetizador = `#7A8B3E`. Agente cobre áreas em tom mais claro (30% opacidade). |
| **Layout** | Orientação retrato. Dois diagramas lado a lado (~55mm cada). Abaixo: 3 boxes horizontais com rituais enxutos. |
| **Dimensão** | Diagramas: 120mm × 60mm. Rituais: 120mm × 40mm. Total: ~110mm. |
| **Hierarquia** | Título "THA para times pequenos". Subtítulo: "3 pessoas operam como 6. 1 founder opera como 3." |

---

### Framework 9: PM Brain OS — Kernel + Regras de Autonomia L0–L4 + Memória Compartilhada

**Localização:** Capítulo 6, Seção 4
**Descrição:** Sistema operacional do PM na era dos agentes. Três componentes: Kernel (regras invioláveis), Regras de Autonomia (L0 a L4), Memória Compartilhada (4 camadas).

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Diagrama de camadas concêntricas** (cebola). Camada externa: Memória Compartilhada. Camada média: Regras de Autonomia L0→L4. Núcleo: Kernel. Complementado por tabela L0-L4 em página adjacente. |
| **Paleta** | Kernel = `#C44536` (argila, inviolável). Regras = gradiente de `#D1CBC3` (L0) a `#7A8B3E` (L4). Memória = `#6B8A9E` (céu, permeia tudo). |
| **Layout** | Página dupla. Esquerda: diagrama de camadas concêntricas (~100mm de diâmetro). Direita: tabela L0-L4 com 5 linhas. Abaixo: 4 cards horizontais com as camadas da memória compartilhada. |
| **Dimensão** | Diagrama: 100mm × 100mm. Tabela: 100mm × 90mm. Cards: 180mm × 30mm. Total: usa página dupla completa. |
| **Hierarquia** | Título "PM Brain OS" em argila, 22pt (o maior título de framework do livro — é o sistema central). Subtítulo: "Seu sistema operacional de produto. Kernel + Autonomia + Memória." |
| **Destaque** | O Kernel recebe tratamento especial: moldura mais grossa (3px argila), fundo levemente texturizado (papel craft sutil). |

**Tabela L0-L4:**

| Nível | Nome | O agente... | Exemplo |
|-------|------|-------------|---------|
| L0 | Observador | Só coleta dados, não age | Monitora NPS, alerta se cair |
| L1 | Sugestor | Propõe ação, humano aprova | "Recomendo responder cliente X com template Y" |
| L2 | Executor com validação | Age, humano revisa depois | Responde cliente, PM vê relatório semanal |
| L3 | Executor autônomo | Age, reporta se anomalia | Responde cliente, só alerta se detecta raiva |
| L4 | Decisor delegado | Decide dentro de política, escala exceções | Define desconto até R$ 50, acima escala |

---

### Framework 10: O que o PM PARA de fazer

**Localização:** Capítulo 6, Seção 3
**Descrição:** Lista de 5 atividades que o PM deixa de fazer quando agentes entram no time.

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Coluna "ANTES" → Coluna "DEPOIS"** com 5 transformações. Visualmente: uma seta larga horizontal dividindo a página ao meio. Esquerda = papel antigo (riscado, cinza). Direita = papel novo (sólido, cor). |
| **Paleta** | ANTES = `#D1CBC3` (cinza 300, tachado com linha diagonal sutil). DEPOIS = `#2D2A26` (concreto, sólido). Seta de transição = `#C44536` (argila). Cada item tem número grande (1-5) em argila com 20% opacidade como marca d'água. |
| **Layout** | Orientação retrato. 5 blocos horizontais, cada um com ~18mm de altura. Total: 100mm. Cabe em 2/3 de página. |
| **Dimensão** | 120mm × 100mm. |
| **Hierarquia** | Título "O que o PM PARA de fazer" em argila. Sem subtítulo — o título já é forte o suficiente. |

**Conteúdo:**

| # | ANTES (você era...) | DEPOIS (você vira...) |
|---|---------------------|----------------------|
| 1 | Produtor de PRDs | Curador de outputs do agente |
| 2 | Gargalo de validação | Exceção (só escala quando há ambiguidade) |
| 3 | Decisor intuitivo | Decisor informado por dados do agente |
| 4 | Detetive de problemas | Investigador sênior (agente acha, você resolve) |
| 5 | Redator de tudo | Editor (agente gera draft, você edita) |

---

### Framework 11: HAT Model — 5 Papéis + 3 Princípios

**Localização:** Capítulo 6, Seção 5
**Descrição:** Human-Agent Team Model. 5 papéis que todo time híbrido precisa ter.

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Pentágono/Rosa** com 5 vértices (cada vértice = 1 papel). Centro = "HAT Model". Linhas conectando vértices ao centro. Cada vértice tem ícone e label (Humano ou Agente). Abaixo: 3 princípios em cards horizontais. |
| **Paleta** | Strategist (humano) = `#C44536`, Executor (agente) = `#6B8A9E`, Validator (humano) = `#A67C52`, Escalator (humano) = `#D4A24E`, Learner (ambos) = `#7A8B3E`. Centro = `#2D2A26`. |
| **Layout** | Topo: pentágono (~80mm de diâmetro). Abaixo: 5 mini-cards em linha descrevendo cada papel (~35mm cada). Abaixo: 3 princípios em destaque. |
| **Dimensão** | Pentágono: 80mm × 80mm. Cards: 160mm × 45mm. Princípios: 160mm × 35mm. Total: ~170mm (página inteira). |
| **Hierarquia** | Título "HAT Model — Human-Agent Team" em Cinza 700. Ícones: Strategist = bússola, Executor = engrenagem, Validator = lupa com check, Escalator = seta para cima, Learner = ciclo (duas setas circulares). |

---

### Framework 12: Operating System — O1 a O5 Rituais

**Localização:** Capítulo 7
**Descrição:** OS Framework com 5 rituais: Observe, Schedule, Escalate, Review, Iterate.

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Ciclo circular** com 5 estações. No centro: "OS". Cada estação tem: nome, pergunta-guia e mini-ícone. Complementado por tabela de rituais (Schedule) e matriz de escalação (Escalate). |
| **Paleta** | O1 = `#D4A24E` (âmbar, observar), O2 = `#6B8A9E` (céu, agendar), O3 = `#C44536` (argila, escalar — urgente), O4 = `#A67C52` (terra, revisar), O5 = `#7A8B3E` (cerrado, iterar — crescimento). Círculo central = `#2D2A26`. |
| **Layout** | Página dupla. Esquerda: ciclo circular com 5 estações (~120mm de diâmetro). Direita superior: tabela de rituais (Schedule). Direita inferior: matriz de escalação 2×2. |
| **Dimensão** | Ciclo: 120mm × 120mm. Tabela: 90mm × 60mm. Matriz: 90mm × 60mm. |
| **Hierarquia** | Título "OS — Operating System" em Cinza 700, 20pt. Subtítulo: "5 rituais de decisão para times com IA." |

**Tabela de Rituais (Schedule):**

| Ritual | Duração | Frequência | O que revisar |
|--------|---------|------------|---------------|
| Daily do agente | 5 min | Diário | Decisões anômalas, escalações pendentes |
| Weekly review | 30 min | Semanal | Top 10 erros, feedback de usuários |
| Monthly análise | 2h | Mensal | Análise de tendências, revisão de métricas |
| Quarterly audit | 4h | Trimestral | Revisão de casos-limite, alinhamento estratégico |

**Matriz de Escalação (Escalate):**

| | Baixo Risco | Alto Risco |
|---|---|---|
| **Baixa Complexidade** | Agente decide sozinho | Escala para humano |
| **Alta Complexidade** | Sugere, escala se dúvida | Escala imediatamente |

---

### Framework 13: Cultura 3 Fases + Culture-Ethics (8 componentes)

**Localização:** Capítulo 8
**Descrição:** Framework Culture-Ethics com 8 componentes formando o acrônimo C-U-L-T-U-R-E. Três fases de evolução cultural: experimentação → incorporação → aceleração.

| Parâmetro | Especificação |
|-----------|---------------|
| **Tipo de visualização** | **Linha do tempo horizontal com 3 fases** no topo + **8 cards em grid 4×2** com os componentes C-U-L-T-U-R-E abaixo. |
| **Paleta** | Fase 1 (Experimentação) = `#D4A24E` (âmbar), Fase 2 (Incorporação) = `#C44536` (argila), Fase 3 (Aceleração) = `#7A8B3E` (cerrado). Componentes: cada letra do acrônimo com sua cor. C = `#C44536`, U = `#6B8A9E`, L = `#D4A24E`, T = `#A67C52`, U = `#7A8B3E`, R = `#C44536`, E = `#D4A24E`. |
| **Layout** | Topo: linha do tempo horizontal com 3 marcadores e descrições curtas (~160mm). Abaixo: grid 4×2 com 8 cards (~75mm × 40mm cada). |
| **Dimensão** | Linha do tempo: 160mm × 40mm. Grid: 160mm × 100mm. Total: ~150mm (página inteira). |
| **Hierarquia** | Título "Cultura que Adota e Ética que Protege" em argila. Subtítulo: "8 componentes. 3 fases. 1 sistema." |

**8 Componentes C-U-L-T-U-R-E:**

| Letra | Componente | O que é |
|-------|------------|---------|
| C | Checklists de Deploy | Lista obrigatória antes de qualquer modelo ir para produção |
| U | User Feedback Loops | Sistema para coletar feedback sobre decisões do modelo |
| L | Learning Rituais | Rituais periódicos de aprendizado com modelos em produção |
| T | Transferência de Conhecimento | Processo para não depender de heróis |
| U | Unambiguous Metrics | Métricas claras que todo mundo usa |
| R | Revisão de Viés | Processo periódico, não só no lançamento |
| E | Ethical Escalation | Canal claro para escalar preocupações éticas |

---

### Frameworks Complementares (não listados no brief, mas presentes no livro)

#### Automation Matrix (Capítulo 2)

Matriz 2×2 com eixos "Capacidade de Automação" (X) e "Desejo de Automação" (Y). 4 zonas: Green (Implementar já), Yellow (Investir em R&D), Red (Evitar), White (Ignorar). Diagramada como matriz canônica de 4 quadrantes com cores sólidas a 20% opacidade.

#### Human Agency Scale (Capítulo 7)

5 níveis de autonomia do agente: N1 (Humano decide sozinho) a N5 (IA decide sozinha). Visualizada como régua horizontal com 5 marcadores. Cada marcador com cor progressiva de Cinza 300 (N1) a Argila (N5). Níveis 1-3 recomendados para maioria dos times.

#### AI Team Health Score (Capítulo 6)

3 dimensões × 3 métricas cada = 9 indicadores. Diagramado como dashboard visual: 3 colunas (Valor para Usuário, Valor para Negócio, Qualidade de Implementação) com 3 métricas cada. Formato de "scorecard" com mini-barras de progresso.

---

## 3. Capa do Livro

### 3.1 Especificações técnicas

| Parâmetro | Especificação |
|-----------|---------------|
| **Formato** | 16 × 23 cm (formato brasileiro clássico de negócios — maior que 14×21, mais presença) |
| **Acabamento** | Capa dura com sobrecapa em papel pólen soft 150g/m². Lombada quadrada. |
| **Cores** | 2 cores especiais + verniz localizado. Sem CMYK — cores especiais dão profundidade e sofisticação. |
| **Papel da capa** | Papelão cinza 2,5mm revestido com papel Colorplan cinza-quente. |
| **Verniz** | Verniz texturizado (soft-touch) na área do título. Toque aveludado — o livro pede para ser pego. |

### 3.2 Três direções conceituais

#### DIREÇÃO A: "Argila e Concreto" (Recomendada por Iza)

**Conceito:** O livro como ferramenta construída à mão. A capa evoca argila (matéria-prima brasileira, terra, construção) e concreto (cidade, decisão, execução). Nada de futurismo — é sobre fazer, não sobre imaginar.

**Descrição visual:**
- Fundo: cor sólida argila `#C44536` com textura sutil de papel artesanal (linho)
- Título "LIDERANDO" em branco `#FAF7F2`, caixa alta, tracking largo (+80), família tipográfica geométrica bold (DM Sans ou Outfit Bold), ~28pt
- "NA ERA DOS" em corpo menor (~14pt), mesmo branco, tracking normal, light
- "AGENTES" em branco, bold, ~36pt, tracking +40
- Nome da autora "Fernanda Faria" na base, alinhado à esquerda, Cinza 200, 10pt, tracking +120, caixa alta
- Detalhe: uma linha horizontal fina (0,5pt) em branco 30% opacidade separando título e autora
- Lombada: argila sólida com título em branco, vertical
- Quarta capa: fundo argila, texto de apresentação em branco 80% opacidade, 4 linhas
- **O que faz essa direção vencer:** É brasileira sem ser caricata. É executiva sem ser corporativa. A argila remete à terra, ao feito à mão, à construção. O título em branco sobre argila é impositivo mas acolhedor. Ninguém confunde com livro de tecnologia genérico.

#### DIREÇÃO B: "Tipografia Pura"

**Conceito:** Confiança total no texto. Capa tipográfica, sem imagem, sem ilustração. A força está na palavra. Referência: capas da editora Ubu, Cosac Naify, algumas edições da Penguin Classics.

**Descrição visual:**
- Fundo: `#FAF7F2` (papel) com moldura sutil (filete de 1pt em argila a 8mm da borda)
- Título composto em três linhas, alinhado à esquerda, com entrelinha apertada (leading = 0.9)
- "Liderando" em `#2D2A26`, light, ~32pt
- "na Era dos" em `#A9A29A` (Cinza 400), itálico, ~14pt
- "Agentes" em `#C44536` (argila), bold, ~48pt, transbordando ligeiramente para a direita
- Nome da autora: "Fernanda Faria" em Cinza 600, 9pt, tracking +200, no pé da página
- **Quando escolher:** Se o projeto priorizar máxima sobriedade. Funciona bem para livrarias de rua e públicos acadêmicos. Menos impacto em e-commerce (thumbnail pequena perde a sutileza).

#### DIREÇÃO C: "Mão na Massa"

**Conceito:** A capa mostra uma mão humana tocando uma superfície onde aparece um padrão de dados (abstrato, geométrico). A mão é real (fotografia), o padrão é gráfico. O encontro entre humano e máquina é físico, tátil.

**Descrição visual:**
- Fotografia PB de uma mão (enquadramento próximo, luz lateral dura) ocupando 60% da capa
- Sobre a mão: padrão geométrico minimalista (grade de pontos ou linhas) em argila `#C44536` com 40% opacidade
- Título sobre a metade inferior: "Liderando na Era dos Agentes" em Cinza 700 sobre fundo Papel `#FAF7F2`
- **Quando escolher:** Se o público for mais amplo que executivos de produto. A imagem de mão humaniza. Bom para e-commerce (thumbnail mais impactante que Direção B). Ruim: pode envelhecer mais rápido que as outras direções.

### 3.3 Recomendação final de Iza

**Direção A — "Argila e Concreto"** — com um ajuste: na quarta capa, incluir o framework MATURE em miniatura (versão simplificada da escada de 5 níveis) como convite visual. Quem pega o livro na livraria, vira, vê o framework e pensa "isso é ferramenta, não teoria".

---

## 4. Tipografia e Layout Interno

### 4.1 Família tipográfica

| Uso | Fonte | Peso | Tamanho | Leading | Tracking |
|-----|-------|------|---------|---------|----------|
| **Título do livro** (capa) | DM Sans | Bold | 28-36pt | — | +80 |
| **Títulos de parte** (PARTE I, II, III, IV) | DM Sans | Bold | 16pt | 20pt | +120 |
| **Títulos de capítulo** | DM Sans | Bold | 18pt | 22pt | +40 |
| **Subtítulos de capítulo** | DM Sans | Medium | 12pt | 16pt | +20 |
| **Aberturas de seção** (SEÇÃO 1, 2...) | DM Sans | Bold | 11pt | 14pt | +80 |
| **Corpo de texto** | **Lora** | Regular | 10pt | 15pt | 0 |
| **Citações/destaques** | Lora | Italic | 10.5pt | 16pt | +10 |
| **Callouts, boxes, tabelas** | **DM Sans** | Regular | 8.5pt | 12pt | +10 |
| **Cabeçalho de tabela** | DM Sans | Bold | 8pt | 10pt | +20 |
| **Notas de rodapé** | DM Sans | Regular | 7pt | 9pt | 0 |
| **Números de página** | DM Sans | Medium | 8pt | — | +40 |

**Justificativa da escolha:**

- **Lora** para corpo de texto: serifada contemporânea, desenhada para legibilidade em corpo pequeno. Tem calor (não é fria como uma Georgia, não é rígida como uma Times). As serifas são orgânicas, remetem a caligrafia. Disponível no Google Fonts (gratuita, licença OFL). Funciona bem em português (acentos, cedilha, diacríticos).
- **DM Sans** para títulos e elementos de design: geométrica, limpa, brasileira (desenhada por Colophon Foundry para o Google, mas com proporções que lembram a arquitetura modernista brasileira). Low-contrast, excelente legibilidade em tamanhos pequenos. Disponível no Google Fonts.

**Alternativas (se as fontes acima não estiverem disponíveis):**
- Corpo: **Merriweather** (Google Fonts, serifada, um pouco mais robusta que Lora) ou **Crimson Pro** (mais elegante, menor economia de espaço)
- Títulos: **Outfit** (similar a DM Sans, levemente mais larga) ou **Work Sans** (mais neutra)

### 4.2 Hierarquia visual

```
Nível 1 — TÍTULO DE PARTE
        └─ DM Sans Bold 16pt, tracking +120, cor: argila #C44536
        └─ Linha horizontal 1pt argila abaixo
        └─ Epígrafe da parte em Lora Italic 10pt, Cinza 500

Nível 2 — TÍTULO DE CAPÍTULO
        └─ DM Sans Bold 18pt, tracking +40, cor: concreto #2D2A26
        └─ Número do capítulo em DM Sans Bold 48pt, argila com 8% opacidade,
           como marca d'água atrás do título

Nível 3 — Abertura de seção (CENA DE ABERTURA, DEFINIÇÃO DO PROBLEMA...)
        └─ DM Sans Bold 11pt, tracking +80, cor: argila #C44536
        └─ Filete vertical 3px à esquerda em argila

Nível 4 — Subtítulo dentro de seção (###)
        └─ DM Sans Medium 10pt, cor: Cinza 600 #4A4540

Nível 5 — Corpo de texto
        └─ Lora Regular 10/15pt, cor: Cinza 600 #4A4540

Nível 6 — Callouts, boxes, tabelas
        └─ DM Sans Regular 8.5/12pt

Nível 7 — Notas, legendas
        └─ DM Sans Regular 7/9pt, Cinza 500
```

### 4.3 Tratamento de aberturas de capítulo

Cada capítulo abre com:

1. **Página de abertura (ímpar, direita):**
   - Número do capítulo como marca d'água gigante: DM Sans Bold, ~120pt, argila `#C44536` com 6% opacidade, ocupando 70% da mancha
   - Título do capítulo sobreposto em 2-3 linhas, DM Sans Bold 18pt, `#2D2A26`
   - Linha horizontal 2pt argila, 30mm de comprimento, alinhada à esquerda
   - Epígrafe do capítulo (se houver) em Lora Italic 10pt, Cinza 500, com 20mm de recuo à esquerda

2. **Página de continuação (par, esquerda):**
   - Fólio (número da página) no canto inferior esquerdo
   - Cabeço: nome do capítulo em DM Sans 7pt, Cinza 400, tracking +60
   - Início do texto sem capitular (não usar letra capitular — o design é direto)

3. **Aberturas de PARTE:**
   - Página dupla
   - Esquerda: número da parte em algarismo romano, DM Sans Bold 72pt, argila 8% opacidade
   - Direita: título da parte + epígrafe
   - Fundo: ligeiramente mais escuro (Cinza 100 `#F5F2ED` em vez de Papel `#FAF7F2`) para diferenciar

### 4.4 Sistema de grid

```
┌─────────────────────────────────────────────────────────┐
│  MANCHA DE TEXTO                                         │
│                                                          │
│  Formato da página: 160mm × 230mm                        │
│                                                          │
│  Margens:                                                │
│    Topo:       22mm                                      │
│    Externo:    20mm                                      │
│    Interno:    18mm (margem de lombada)                  │
│    Base:       24mm (mais generosa, respiro)             │
│                                                          │
│  Mancha resultante: 122mm × 184mm                        │
│                                                          │
│  Grid de colunas:                                        │
│    2 colunas para texto corrido (raro)                   │
│    1 coluna principal (92mm) + coluna lateral (30mm)     │
│      para callouts, notas e pequenos diagramas           │
│                                                          │
│  Coluna lateral (30mm):                                  │
│    - Callout boxes                                       │
│    - Ícones (⚠️, 💡, 📊, ❌, ✅)                           │
│    - Mini-diagramas                                      │
│    - Notas de margem                                     │
│                                                          │
│  Baseline grid: 5mm (leading de 15pt = ~5.3mm)           │
│    Todos os elementos alinham à grade de base            │
└─────────────────────────────────────────────────────────┘
```

### 4.5 Callout boxes — Sistema

Quatro tipos de callout, todos com a mesma estrutura base:

**Estrutura base:**
- Largura: coluna lateral (30mm) ou largura total da mancha (122mm)
- Fundo: Cinza 100 `#F5F2ED`
- Borda esquerda: 3px sólida
- Padding: 6mm 8mm
- Fonte: DM Sans Regular 8/11pt
- Arredondamento: 0 (cantos vivos — o design é direto)

| Tipo | Ícone | Cor da borda | Uso |
|------|-------|-------------|-----|
| ⚠️ Alerta | ⚠️ (triângulo) | `#D4A24E` (âmbar) | Avisos, armadilhas, "cuidado com..." |
| 💡 Insight | 💡 (lâmpada) | `#7A8B3E` (cerrado) | Dica prática, "bora aplicar", atalho |
| 📊 Dado | 📊 (gráfico) | `#6B8A9E` (céu) | Estatística, pesquisa, fonte de dados |
| ❌/✅ Script | ❌ ou ✅ | `#C44536` / `#5A8A4A` | Scripts de conversa "não diga" / "diga" |

**Exemplo visual (❌/✅ Script):**
```
┌──────────────────────────────────────────┐
│ ❌ NÃO DIGA:                              │
│ "Precisamos primeiro fazer um            │
│  diagnóstico de maturidade."             │
│                                          │
│ ✅ DIGA:                                  │
│ "Sua visão está certa. A pergunta        │
│  não é se vamos usar IA, é onde..."      │
└──────────────────────────────────────────┘
```
Borda esquerda: 3px `#C44536` para ❌, `#5A8A4A` para ✅. Fundo: `#F5F2ED`. Padding: 6mm.

---

## 5. Worksheets/Canvas — Linguagem Visual

### 5.1 Sistema de worksheet

Todo worksheet do livro segue estas regras:

**Moldura:**
- Borda: 1pt sólida `#A9A29A` (Cinza 400)
- Fundo: `#FAF7F2` (Papel) — mesmo fundo da página, mas com a borda demarcando
- Cantos: vivos (0 arredondamento)
- Padding interno: 8mm
- Margem externa: 4mm da mancha de texto

**Campos preenchíveis:**
- Indicados por sublinhado pontilhado: `_ _ _ _ _ _ _ _ _ _ _`
- Cor do sublinhado: `#A9A29A` (Cinza 400)
- Fonte: DM Sans Regular 9pt
- Label do campo em DM Sans Bold 7pt, Cinza 500, acima da linha

**Exemplos preenchidos:**
- Fundo: Cinza 100 `#F5F2ED`
- Texto: DM Sans Regular 8.5pt, Cinza 700
- Selo "EXEMPLO" no canto superior direito: DM Sans Bold 6pt, `#6B8A9E` (céu), tracking +120, caixa alta, com filete de 15mm abaixo
- Posição: sempre em página separada do worksheet em branco (ou abaixo, com divisória clara)

**Divisória entre worksheet em branco e exemplo:**
- Linha pontilhada horizontal, 0.5pt, `#D1CBC3`, com label "EXEMPLO PREENCHIDO →" na extremidade direita

### 5.2 Worksheet específico: Custo Real Calculator

**Diagramação:**
```
┌─────────────────────────────────────────────────┐
│  CUSTO REAL CALCULATOR                           │
│  Preencha com seus números.                      │
│  É o que seu CFO vai pedir.                      │
│                                                  │
│  Item                    │ Fórmula   │ Seu número│
│  ────────────────────────┼───────────┼───────────│
│  Volume mensal           │ Conv/mês  │ ________  │
│                          │ × Tokens  │           │
│  ────────────────────────┼───────────┼───────────│
│  Custo API (inference)   │ Vol × $   │ R$ _____  │
│                          │ ÷ 1M      │           │
│  ────────────────────────┼───────────┼───────────│
│  Custo API c/ margem     │ API × 1,5 │ R$ _____  │
│  cambial (dólar)         │           │           │
│  ────────────────────────┼───────────┼───────────│
│  Custo de engenharia     │ H/mês ×   │ R$ _____  │
│                          │ R$ 200    │           │
│  ────────────────────────┼───────────┼───────────│
│  Infraestrutura          │ Servers,  │ R$ _____  │
│                          │ cloud     │           │
│  ────────────────────────┼───────────┼───────────│
│  Manutenção (20%)        │ 20% total │ R$ _____  │
│  ────────────────────────┼───────────┼───────────│
│  CUSTO TOTAL MENSAL      │ SOMA      │ R$ _____  │
│  ────────────────────────┼───────────┼───────────│
│  Receita/Economia gerada │ Quanto    │ R$ _____  │
│                          │ economiza │           │
│  ────────────────────────┼───────────┼───────────│
│  Payback (meses)         │ Invest ÷  │ _____ mes │
│                          │ Economia  │           │
└─────────────────────────────────────────────────┘
```

### 5.3 Canvas de diagnóstico: MATURE Autoavaliação

Worksheet adicional (não explicitamente no livro, mas inferido como útil):

Autoavaliação de 5 perguntas, cada uma correspondendo a um nível. O leitor marca com ☐ (vazio) ou ☒ (marcado). Abaixo: "Seu nível é o mais alto com 3+ marcações."

**Diagramação:** mesmo sistema de worksheet, porém com checkboxes quadrados (8pt × 8pt, borda 1pt `#C44536`, preenchimento `#C44536` quando marcado).

---

## 6. Referências Visuais

### 6.1 "The Grid" — Allen Hurlburt (1978)
**Por que:** A bíblia do design de grid para publicações. Hurlburt foi diretor de arte da Look Magazine e professor em Yale. Este livro define os princípios de grid que sustentam o design proposto aqui: hierarquia, proporção, espaço negativo. Especificamente: o capítulo sobre "Grid de 2 colunas com coluna assimétrica" é a base da mancha de texto deste projeto. Não é inspiração estética — é fundamento técnico.

### 6.2 "Mais que Vencer" (Playing to Win) — A.G. Lafley & Roger Martin, edição brasileira (2013, Editora Portfolio-Penguin)
**Por que:** Exemplo de livro de negócios brasileiro que acertou no design. Capa com tipografia bold sobre fundo de cor sólida, interior com frameworks diagramados em 2 cores (preto + laranja corporativo). O que funciona: a diagramação dos frameworks é limpa, didática e consistente ao longo do livro. Referência direta para como tratar frameworks em página dupla. O que evitar: o laranja corporativo deles é genérico. Prefira argila.

### 6.3 Coleção Ubu Editora — identidade visual por Elaine Ramos
**Por que:** A Ubu define o padrão contemporâneo de design editorial brasileiro. Capas tipográficas, paletas restritas a 2-3 cores, grid rigoroso, papel de alta qualidade. Especificamente: o uso de cores planas com sobreposição de texto branco, as aberturas de capítulo minimalistas, o tratamento de notas e margens laterais. Referência para: abertura de capítulos, uso de cor especial, espaço negativo. O design system da Ubu prova que livro brasileiro pode ser sofisticado sem ser europeu.

### 6.4 "Ruído" (Noise) — Daniel Kahneman, Olivier Sibony & Cass Sunstein, edição brasileira (2021, Objetiva)
**Por que:** Exemplo de como diagramar frameworks complexos (matrizes, tabelas comparativas, escalas de julgamento) em um livro de negócios traduzido para o português. O design interno fez algo raro: manteve a precisão dos diagramas originais mas adaptou a tipografia para o texto em português (que é ~30% mais longo que o inglês). Referência para: tabelas comparativas, matrizes 2×2, escalas numéricas. O que evitar: o design é frio e genérico (azul + cinza corporate). Nosso livro é mais quente.

### 6.5 "O Ponto de Virada" (The Tipping Point) — edição comemorativa ilustrada por Cristina Guitian (Little, Brown, 2022)
**Por que:** Exemplo de como infográficos e diagramas podem ser integrados ao texto sem virar "livro ilustrado". A edição mantém o texto integral de Gladwell mas adiciona visualizações que realmente clareiam os conceitos. Referência para: integração de diagramas no fluxo de leitura, hierarquia entre texto e visualização. Atenção: nosso livro é mais contido visualmente que esta edição. Menos ilustração, mais diagramação.

---

## 7. Especificações Técnicas Finais

### 7.1 Resumo de cores (Hex)

```
Argila          #C44536    Títulos, call-to-action, gráficos, capa
Concreto        #2D2A26    Texto de títulos, elementos estruturais
Papel           #FAF7F2    Fundo da página
Cinza-quente    #4A4540    Corpo de texto
Cerrado         #7A8B3E    Dados, crescimento, N5 excelência
Terra           #A67C52    N3 maturidade, transições
Céu             #6B8A9E    Tecnologia, agente, dados
Âmbar           #D4A24E    Alertas, avisos, N2-N3 maturidade
Verde-acerto    #5A8A4A    ✅ Scripts, checklists positivos

Cinza 100       #F5F2ED    Fundo de callouts
Cinza 200       #E8E3DC    Fundo de exemplos
Cinza 300       #D1CBC3    Bordas, linhas
Cinza 400       #A9A29A    Ícones inativos
Cinza 500       #7A736B    Notas, legendas
Cinza 600       #4A4540    Corpo de texto
Cinza 700       #2D2A26    Títulos
```

### 7.2 Resumo de fontes

| Fonte | Uso | Licença |
|-------|-----|---------|
| DM Sans Bold | Títulos, capa, cabeçalhos de tabela | OFL (Google Fonts) |
| DM Sans Medium | Subtítulos, aberturas de seção | OFL |
| DM Sans Regular | Callouts, boxes, tabelas, notas | OFL |
| Lora Regular | Corpo de texto | OFL (Google Fonts) |
| Lora Italic | Citações, epígrafes, destaques | OFL |

### 7.3 Dimensões de frameworks (resumo para diagramação)

| Framework | Orientação | Largura × Altura | Ocupação |
|-----------|-----------|------------------|----------|
| AI Trap (5 sinais) | Retrato | 120 × 80mm | ½ página |
| MATURE (escada N1-N5) | Paisagem (pág dupla) | 240 × 170mm | Página dupla |
| Automation Matrix | Retrato | 80 × 80mm | ⅓ página |
| B³ Matrix (5×3) | Paisagem | 160 × 120mm | 1 página |
| Custo Real Calculator | Retrato | 100 × 210mm | 1 página |
| CFO Primer (tabela) | Retrato | 100 × 150mm | ¾ página |
| THA (Venn + colunas) | Retrato | 120 × 160mm | ⅔ página |
| Gerente-Informante | Retrato | 90 × 70mm | ⅓ página |
| Scale-Down (time 3 vs 1) | Retrato | 120 × 110mm | ½ página |
| PM Brain OS (camadas + tabela) | Paisagem (pág dupla) | 220 × 170mm | Página dupla |
| PM PARA de fazer (5 itens) | Retrato | 120 × 100mm | ⅔ página |
| HAT Model (pentágono + cards) | Retrato | 160 × 170mm | 1 página |
| OS Framework (ciclo + tabelas) | Paisagem (pág dupla) | 240 × 170mm | Página dupla |
| Cultura 3 Fases + CULTURE | Retrato | 160 × 150mm | 1 página |
| Human Agency Scale | Retrato | 120 × 50mm | ¼ página |
| AI Team Health Score | Retrato | 160 × 80mm | ½ página |

### 7.4 Checklist de consistência visual

Antes de finalizar qualquer diagrama, verificar:

- [ ] Fonte correta (DM Sans para elementos de design, Lora para texto corrido)
- [ ] Cor dentro da paleta-mestre (zero cores fora do sistema)
- [ ] Alinhamento à baseline grid de 5mm
- [ ] Bordas: 1pt ou 3pt, nunca 2pt, nunca 4pt+
- [ ] Espaçamento interno (padding): múltiplos de 2mm
- [ ] Números: sempre alinhados à direita em tabelas
- [ ] Labels: DM Sans Bold 7pt, Cinza 500
- [ ] Cantos: vivos (border-radius: 0)
- [ ] Ícones: traço (linha), nunca preenchidos
- [ ] Hierarquia: o olho do leitor encontra o título em < 1 segundo
- [ ] Sobrecarga: se o framework não couber em meia página, reavalie antes de expandir

### 7.5 Ferramentas recomendadas para execução

| Etapa | Ferramenta | Nota |
|-------|-----------|------|
| Grid e layout base | Adobe InDesign | Padrão editorial profissional |
| Diagramas vetoriais | Figma ou Adobe Illustrator | Figma para colaboração, Illustrator para precisão de saída |
| Tipografia | Google Fonts (DM Sans + Lora) | Gratuitas, licença OFL, já instaladas |
| Mockups de capa | Figma + Photoshop | Para apresentar ao cliente/autora |
| Revisão de cor | Prova de cor física (não digital) | Cores especiais (Pantone) precisam de prova física |
| Gráficos e tabelas | SVG exportado do Figma → InDesign | Manter edição não-destrutiva |
| Documentação | Este documento (Markdown) | Versionado, referência única |

---

## Nota final de Iza

Este design system foi construído com uma obsessão: o livro precisa parecer que foi feito por quem opera, não por quem teoriza. Cada decisão — da argila na capa ao grid de baseline de 5mm — serve a um propósito: fazer o conteúdo da Fernanda brilhar sem competir com ele.

A paleta respira Brasil porque a autora é brasileira, o mercado dela é brasileiro, e os cases são brasileiros. Mas não é Brasil de cartão-postal. É Brasil de concreto, terra batida, reunião às 9h da manhã e café frio na mesa. É o Brasil de quem faz.

Se tiver dúvida entre duas opções, volte aos princípios: **menos é mais, o texto é o protagonista, e design serve ao conteúdo — não o contrário.**

---

*Design System v1.0 — 15 de junho de 2026*
*Iza (core — taste-judge, protect-restraint)*
