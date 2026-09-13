# Capítulo 3: Build, Buy ou Partner? A decisão que define tudo

---

### Seção 1: Cena de abertura

Era uma quinta-feira, e Carolina, diretora de produto de um banco digital brasileiro, estava sentada na ponta da cadeira. Na tela, uma videoconferência cheia de gente. Na pauta, uma decisão que já durava três meses: construir um chatbot de atendimento próprio ou comprar uma solução de terceiros.

O CTO abriu a reunião. "Construir nos dá controle total. Podemos fazer fine-tuning com nossos dados. É a escolha certa para um banco que quer ser referência em IA."

O CFO rebateu. "Controle total custa caro. A solução pronta custa uma fração disso por ano. Por que reinventar a roda?"

O CEO, que entrava e saía da reunião, mandou um áudio no grupo: "Faz os dois. Vai construindo enquanto compra. Depois a gente decide."

Silêncio.

Carolina olhou para o relógio. A reunião já tinha passado de uma hora. Zero decisão. Zero perguntas sobre o que os usuários realmente precisavam.

Uma semana depois, o banco comprou a solução pronta. Três meses depois, os clientes odiavam o chatbot. O time de engenharia culpou a ferramenta. O time de negócios culpou a implementação. E Carolina ficou com a sensação de que ninguém tinha feito a pergunta certa.

A decisão build vs buy não é técnica. É estratégica. E a maioria dos PMs não tem ferramentas para tomá-la.

---

### Seção 2: Definição do problema

"Fernanda, como a gente decide o que construir versus o que comprar? Cada reunião vira um ringue de boxe entre CTO e CFO."

Essa pergunta aparece em toda empresa que começa a levar IA a sério. E a resposta mudou completamente nos últimos dois anos.

**O falso dilema do software tradicional.** Antes, build vs buy era binário. Você construía um sistema ou comprava um SaaS. Na IA, o espectro é muito mais amplo: construir do zero com dados próprios, fazer fine-tuning de um modelo open-source, usar a API de um modelo proprietário, comprar uma solução completa de terceiros, ou fazer parceria com uma startup de IA. São pelo menos cinco caminhos, não dois.

**O custo invisível.** As empresas subestimam o custo de integração, manutenção e mudança cultural. Construir um protótipo com Cursor ou Claude Code leva dias. Colocar em produção, com governança, monitoramento e escalabilidade, leva meses. O custo de operar é sempre maior que o custo de desenvolver.

**A armadilha do "construir é mais barato".** Com agentes de IA, construir um MVP ficou mais rápido. Mas ganhar velocidade de desenvolvimento não é ganhar economia total. O custo de manutenção, de inferência, de fine-tuning contínuo, de governança de dados: tudo isso continua pesando. E pesa mais quando você constrói algo que não deveria ter construído.

**O lastro que faltava.** Anish Acharya, sócio da a16z, coloca o dedo na ferida: moats são descobertos, não projetados. Tradução: você não senta numa sala, desenha uma vantagem competitiva no papel e manda construir. Você roda o negócio, observa os loops e descobre onde a vantagem apareceu de verdade. Para Acharya, uma empresa é uma série de loops, e ganha quem aperta esses loops mais rápido, não quem projeta o moat mais bonito no slide (Anish Acharya, a16z, Lenny's Podcast, set/2026).

Isso muda a decisão build vs buy. A pergunta deixa de ser "onde eu quero ter vantagem?" e vira "onde a vantagem já está aparecendo?". Construir não cria moat. Construir só amplia um moat que já existe.

**Conexão com o Capítulo 2.** No capítulo anterior, vimos que a AI Trap acontece quando empresas focam na tecnologia e esquecem do usuário. A decisão build vs buy é o momento onde essa armadilha se materializa. É quando o CTO quer construir porque é legal, o CFO quer comprar porque é mais barato, e ninguém pergunta: "Isso resolve o problema do usuário?"

O problema não é falta de opções. É falta de um framework para decidir. E a Matriz B³ resolve isso. Mas antes de apresentá-la, uma pergunta: se construir ficou barato, por que a maioria das empresas ainda erra na decisão?

Porque elas usam um critério só. As que acertam usam cinco. E ainda assim, tem um detalhe: construir por construir é vaidade. Comprar por comprar é preguiça. A resposta certa está no meio, e ela depende de saber o que é core para o seu negócio.

---

### Seção 3: Framework: a Matriz B³

> **Matriz B³: Build, Buy, Borrow**
>
> A Matriz B³ organiza as decisões em três caminhos, avaliados em 5 eixos: **Build** (construir com time e dados próprios), **Buy** (comprar API/SaaS pronto), **Borrow** (pegar algo que já existe e adaptar ao seu contexto, seja open-source, parceria ou fine-tuning). Você não constrói do zero, não compra caixa-preta. Você toma emprestado e molda.

**Framework: Matriz B³ (Build, Buy, Borrow)**
**Autora:** Fernanda Faria, 2026
**Acrônimo:** B³ = Build, Buy, Borrow (Borrow = Partner + Open-Source)
**Componentes:** 5 eixos de decisão + 3 caminhos possíveis

#### Os 5 eixos de decisão

**1. Diferenciação Competitiva: A funcionalidade é core para seu negócio ou é commodity?**

Essa pergunta separa PMs de verdade de quem só empurra slide. Se a funcionalidade é *core*, ou seja, está no centro da sua proposta de valor para o cliente, você precisa construir ou, no mínimo, fazer fine-tuning de um modelo com seus dados. Porque se você comprar uma solução pronta, seu concorrente também compra. E aí cadê a vantagem?

Se a funcionalidade é *commodity*, algo que todo mundo precisa, mas ninguém usa como diferencial, compre. Use API. Não perca tempo construindo algo que não vai te diferenciar.

Aqui o Acharya funciona como freio. Moat é descoberto, não projetado. Então a pergunta certa não é "isso pode virar diferencial?", e sim "a vantagem já apareceu aqui?". Se ela ainda não apareceu, construir não vai criá-la. Vai só queimar dinheiro.

**Exemplo real:** O banco digital construiu o próprio motor de análise de crédito. É core para o negócio deles. Mas usa múltiplos provedores de nuvem, incluindo AWS e Google Cloud. Nuvem é commodity. Análise de crédito é diferencial.

**2. Velocidade de Mercado: Quão rápido você precisa chegar?**

Se você precisa de uma solução em *semanas*, não construa. Compre ou use API. O custo de atraso é maior que o custo de comprar.

Se você tem *meses* para desenvolver, construir ou fazer fine-tuning pode valer a pena. Mas só se os outros eixos também apontarem nessa direção.

**Exemplo real:** Um grande varejista lançou um assistente virtual usando uma plataforma de terceiros. Precisavam de velocidade para competir com o marketplace. Depois que o produto provou valor, começaram a migrar partes para solução própria.

A janela de oportunidade é curta. Esperar um ano para construir algo que poderia ser comprado em semanas é um erro estratégico.

**3. Maturidade do Time: Seu time sabe operar modelos de IA?**

Essa é a pergunta que ninguém quer fazer. Porque ninguém quer admitir que não sabe.

Se seu time *não tem experiência* com ML Ops, governança de modelos, fine-tuning e monitoramento de drift, não construa. Você vai gastar meses aprendendo o que poderia comprar em semanas.

Se seu time *tem experiência* (nível 3+ no Product Excellence Maturity Model), construir ou fazer fine-tuning pode ser viável. Mas ainda assim, avalie os outros eixos.

Aqui entra o segundo conceito do Acharya: o *model sommelier*. Na era dos agentes, o jogo deixou de ser construir o melhor modelo e passou a ser selecionar e combinar os modelos certos para cada tarefa, como um sommelier escolhe vinho. Um time que domina curadoria de modelos pode extrair mais valor de uma API do que um time mediano extrairia de um modelo próprio (Anish Acharya, a16z, Lenny's Podcast, set/2026). Maturidade, nesse eixo, é saber escolher, não necessariamente saber construir.

**Nota:** O Product Excellence Maturity Model, apresentado no Capítulo 2, classifica times de produto em 5 níveis de maturidade. Times nos níveis 1-2 devem evitar construir modelos do zero.

**Exemplo real:** Uma fintech brasileira tentou construir um sistema de detecção de fraudes do zero. O time era bom em engenharia de software, mas nunca tinha trabalhado com ML. Meses depois, o modelo próprio entregava menos que uma solução pronta de mercado. Compraram a solução em semanas e o resultado melhorou na hora.

**4. Custo Total de Propriedade (TCO): Não é só desenvolvimento. É manutenção + inferência + integração + pessoas.**

A maioria das empresas calcula só o custo de desenvolvimento. Esquece que construir um modelo é 20% do trabalho. Os outros 80% são manutenção, monitoramento, retreinamento, integração com sistemas legados, e pessoas para operar tudo isso.

**Fórmula sugerida:** TCO = (Custo de Desenvolvimento × 3) + (Custo de Manutenção Anual × 5) + Custo de Oportunidade

O fator 3 no desenvolvimento cobre o custo real de colocar em produção. O fator 5 na manutenção cobre o ciclo de vida do modelo (retreinamento, novos dados, mudanças de infraestrutura).

> **O fator câmbio (realidade brasileira):** Se sua decisão de Buy ou Borrow depende de API/SaaS precificada em dólar (OpenAI, Anthropic, Google), adicione uma margem de 30% a 100% no TCO para absorver variação cambial em 24 meses. Um custo de US$ 5.000/mês em API vira R$ 30.000/mês com o dólar a R$ 6. Isso não é exagero, é o que aconteceu entre 2024 e 2025. Se seu board não entende de câmbio, esse parágrafo é seu argumento.

O custo de ficar de fora também é real. Mas o custo de construir errado é maior.

**5. Risco de Vendor Lock-in: Quão dependente você fica do fornecedor?**

APIs proprietárias (OpenAI, Anthropic, Google) têm maior risco de lock-in. Se o preço subir, se a API mudar, se a empresa mudar de direção, você está refém.

Modelos open-source (Llama, Mistral, Gemma) reduzem o lock-in, mas aumentam o custo de operação. Você precisa de infraestrutura, time e governança.

**Exemplo real:** Uma startup de health tech construiu todo o produto em cima da API de um fornecedor. Quando o fornecedor mudou preços e termos de uso, a conta subiu forte em poucos meses. A startup teve que renegociar ou migrar, e perdeu semanas de desenvolvimento.

#### Tabela de decisão visual

| Eixo | Build | Buy | Borrow |
|------|-------|-----|--------|
| Diferenciação | Core | Commodity | Média |
| Velocidade | Baixa (meses) | Alta (semanas) | Média (1-3 meses) |
| Maturidade do time | Alta (nível 3+) | Baixa (nível 1-2) | Média (nível 2-3) |
| TCO | Alto no início, menor em escala | Baixo no início, maior em escala | Médio |
| Lock-in | Baixo | Alto | Médio |

#### Os 3 caminhos possíveis

Depois de avaliar os 5 eixos, você escolhe um caminho:

**Build:** Construir do zero ou fazer fine-tuning de modelo próprio.
- Quando: Alta diferenciação, time maduro, baixa urgência, TCO favorável, baixo lock-in.
- Exemplo: Recomendação de conteúdo do Spotify. É core, time maduro, vale o investimento.

**Buy:** Comprar solução completa ou usar API de terceiros.
- Quando: Baixa diferenciação, alta urgência, time imaturo, TCO desfavorável para construção.
- Exemplo: Chatbot de FAQ para um e-commerce. É commodity. Compre.

**Borrow:** Fazer parceria ou usar open-source com curadoria.
- Quando: Diferenciação média, velocidade média, time com capacidade de adaptação.
- Exemplo: Fazer fine-tuning de Llama para um caso de uso específico de uma empresa de logística. Você não constrói do zero, mas também não compra caixa-preta. É o caminho do model sommelier.

**Integração com o roadmap:** Use o mapa de oportunidades para avaliar o impacto de cada eixo no roadmap. Por exemplo, se a diferenciação é alta, o compasso aponta para build. Se a urgência é alta, aponta para buy.

---

### Seção 4: Casos e exemplos

#### Caso 1: O banco que projetou um moat que não existia

**Situação Inicial:** Banco digital brasileiro (história real; nome omitido a pedido). Decisão de construir chatbot de atendimento próprio. O time de engenharia convenceu a diretoria com o argumento de "controle total dos dados".

**O que estava errado:** O banco pulou a pergunta de diferenciação competitiva. Atendimento ao cliente é core? Sim. Mas chatbot de FAQ não é diferencial. É commodity. Todo banco tem. O que diferencia não é o chatbot, é a qualidade do atendimento humano quando o chatbot falha. O banco projetou um moat no papel e gastou meses e milhões para construí-lo. O moat nunca apareceu, porque nunca existiu.

É exatamente a lição do Acharya: moats são descobertos, não projetados. Ninguém descobriu vantagem nenhuma num chatbot de FAQ. O banco só projetou uma, e projetou errado.

**Como resolveu:** Depois de meses e uma satisfação de cliente baixa, o banco abandonou o chatbot próprio. Comprou uma solução de terceiros em semanas. Investiu a diferença em treinar a equipe de atendimento humano, que é onde a vantagem real estava.

**Resultados:** Satisfação subiu. Custo de operação caiu. O time de engenharia foi realocado para projetos core, como análise de crédito e prevenção a fraudes.

#### Caso 2: O e-commerce que construiu o que não devia

**Situação Inicial:** E-commerce brasileiro de médio porte. Precisa de um sistema de recomendações de produtos. O CEO, empolgado com IA, decide construir um modelo próprio do zero.

**O que estava errado:** O time de engenharia não tinha experiência com ML. Tentaram implementar um sistema baseado em regras que não escalava. As recomendações eram genéricas. A taxa de cliques caiu após o lançamento.

Faltou o eixo de maturidade do time. Faltou também a honestidade do Acharya: se a vantagem ainda não apareceu no seu produto, construir do zero não vai fazê-la aparecer. O CEO tratou recomendação como core quando, na verdade, era commodity para um e-commerce daquele porte.

**Como resolveu:** Depois de meses e um investimento alto, o e-commerce abandonou o modelo próprio. Contratou uma startup especializada em recomendações contextuais. Implementaram em semanas.

**Resultados:** A taxa de cliques e a conversão subiram. A recomendação passou a gerar receita relevante. E o custo recorrente ficou bem abaixo do que tinham gasto tentando construir.

#### Caso 3: A startup de mobilidade que acertou o equilíbrio

**Situação Inicial:** Startup brasileira de mobilidade (história real; nome omitido a pedido). Precisa de algoritmo de otimização de rotas para motoristas. Decisão: construir o core, mas usar API de mapas de terceiros.

**O que estava errado:** Nada. A startup fez a lição de casa. Otimização de rotas é core para o negócio. Mas mapas são commodity. Em vez de construir tudo do zero, fizeram uma parceria com provedor de APIs de mapas e construíram o algoritmo de otimização em cima.

É o caminho do meio do Acharya: descobriu onde estava a vantagem (o algoritmo próprio) e pegou emprestado o resto (mapas). Construir só o que diferencia, pegar emprestado o que não diferencia.

**Como resolveu:** Time pequeno de engenheiros de ML. Meses de desenvolvimento. Integração com API de mapas para dados de trânsito e clima.

**Resultados:** Adoção subiu de um patamar baixo para a maioria dos motoristas em poucos meses. Redução real no tempo de entrega e no consumo de combustível. O custo total de desenvolvimento ficou bem abaixo do que seria se construíssem tudo do zero.

---

### Seção 5: Guia prático 30/60/90 dias

#### Dias 1-30: Mapeamento

1. **Liste todas as funcionalidades de IA que você planeja.** Não importa se são 5 ou 50. Cada uma precisa de uma decisão separada.

2. **Para cada funcionalidade, colete três informações:**
   - Dados de usuário: qual o problema real que você está resolvendo?
   - Custo total estimado (TCO): use a fórmula do eixo 4.
   - Capacidade do time: qual o nível de maturidade no Product Excellence Maturity Model?

3. **Classifique cada funcionalidade como core ou commodity.** Seja honesto. Se você não sabe, pergunte: "Se meu concorrente tiver isso e eu não, perco clientes?" Se sim, é core. Mas antes de marcar core, pergunte de novo: "a vantagem já apareceu aqui, ou eu estou projetando ela?"

#### Dias 31-60: Aplicação da Matriz B³

4. **Para cada funcionalidade, pontue nos 5 eixos.** Use a tabela visual da Seção 3. Marque cada eixo como baixo, médio ou alto.

5. **Identifique 1 decisão para construir, 1 para comprar, 1 para fazer parceria.** Não tente resolver tudo de uma vez. Priorize.

6. **Documente a decisão.** Escreva por que cada funcionalidade foi classificada como build, buy ou borrow. Isso vira referência para o próximo ciclo.

#### Dias 61-90: Validação e Ajuste

7. **Para a decisão de build:** Entregue um protótipo funcional. Teste com usuários reais antes de escalar.

8. **Para a decisão de buy:** Implemente com métricas de sucesso definidas. NPS, tempo de resposta, taxa de resolução no primeiro contato.

9. **Para a decisão de partner:** Estabeleça SLA e governança. Defina quem responde por quê. Crie um canal de comunicação direto.

10. **Meça o resultado.** Volte ao TCO estimado e compare com o real. Se o custo real for muito maior que o estimado, seu processo de decisão tem um problema.

---

### Seção 6: Métricas de sucesso

| Métrica | O que mede | Benchmark |
|---|---|---|
| Tempo de implementação | Dias do go até produção | Build: meses. Buy: semanas |
| Satisfação do usuário final | Nota de 1 a 5 da experiência | Meta: > 4,0 |
| TCO (Total Cost of Ownership) | Custo total em 12 meses | Build: múltiplos do custo de buy |
| Time-to-value | Dias até primeiro valor entregue | Build: meses. Buy: semanas |
| Taxa de adoção | % do público-alvo usando | Meta: maioria no 3º mês |
| Custo por transação | Custo unitário de cada interação | Build: menor em escala. Buy: menor no início |

**Valor para o Usuário:**
- Satisfação da funcionalidade de IA (meta: > 4,0)
- Taxa de resolução no primeiro contato (para chatbots: alta)
- Tempo de resposta (rápido para interações síncronas)

**Valor para o Negócio:**
- Custo por transação de IA (comparar build vs buy vs borrow)
- Tempo de implementação (semanas para buy, meses para build)
- ROI em 12 meses (incluindo TCO real)

**Qualidade de Implementação:**
- Precisão do modelo (alta para casos de uso críticos)
- Taxa de downtime (baixa)
- Cobertura de casos de borda (testar cenários de exceção antes de lançar)

---

### Seção 7: Fechamento com gancho

A decisão build vs buy na era da IA não é sobre tecnologia. É sobre estratégia. É sobre ter coragem de dizer "isso não é core para a gente" e comprar. E ter coragem de dizer "isso é nosso diferencial" e construir.

O banco digital do começo do capítulo errou porque não fez a pergunta certa. Gastou meses e muito dinheiro para construir algo que não ia mudar a experiência do usuário. Se tivesse aplicado a Matriz B³, teria visto que chatbot de FAQ é commodity. O dinheiro deveria ter ido para o que realmente importa: o atendimento humano quando o chatbot falha.

Mas tem um problema. Mesmo com o framework certo, a decisão ainda depende de uma coisa que nenhum framework resolve: *julgamento*. A capacidade de olhar para os 5 eixos, pesar os trade-offs e decidir. E isso só vem com prática.

E tem o aviso do Acharya para não esquecer: moat é descoberto, não projetado. A Matriz B³ não é uma máquina de fabricar vantagem competitiva. Ela é um mapa para descobrir onde a vantagem já existe. Construir por construir é vaidade. Comprar por comprar é preguiça. A Matriz B³ não tira sua responsabilidade de decidir. Ela só te dá as perguntas certas para fazer antes de gastar o primeiro centavo.

Agora que você sabe o que construir, como garantir que o time está pronto para executar? É o que veremos no próximo capítulo sobre o Product Excellence Maturity Model. Porque não adianta tomar a decisão certa se o time não tem maturidade para entregar com excelência.

---
