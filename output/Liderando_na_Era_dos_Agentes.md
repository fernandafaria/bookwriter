# Liderando na Era dos Agentes

*O manual de liderança de produto para a era da IA, por quem opera a transformação*

**Fernanda Faria**

---

## Sobre a autora

Fernanda Faria lidera produtos e times de tecnologia há mais de uma década. Foi executiva em plataformas de escala global e operou a transformação de times tradicionais em organizações AI-native. Este livro não é teoria de consultor, é o que ela aprendeu fazendo.

## Para quem é este livro

Você é VP de Produto, CPTO, Head de Produto, líder de engenharia ou design. Você já sabe o que é PRD, sprint, roadmap e NPS. O que você não sabe é como liderar uma organização onde metade do trabalho é feito por agentes de IA. Este livro não vai te ensinar prompt engineering. Vai te dar ferramentas para decidir, montar times, redesenhar processos e construir cultura.

## Por que este livro existe

Em 2026, o mercado está cheio de livros sobre AI Product Management. O problema: foram escritos por consultores e acadêmicos. Este livro é diferente. Ele foi escrito por quem *opera* a transformação, com as mãos sujas, os erros reais, e as decisões que não têm resposta certa. Se você está cansado de PowerPoints sobre o futuro da IA e quer um manual de verdade, este livro é pra você.

---

# PARTE I: DIAGNÓSTICO. Onde você está?

> *Antes de decidir o que fazer com IA, você precisa saber onde sua organização está.*

# Capítulo 1: A Armadilha de IA e como explicar pro board que 'IA em tudo' é um erro

---

## Seção 1: Cena de Abertura

Era uma quinta-feira de março de 2025, e Carlos, VP de Produto de um banco digital brasileiro, estava na reunião trimestral de resultados. O board estava tenso. A promessa do trimestre anterior era clara: o chatbot com IA generativa iria revolucionar o atendimento ao cliente.

Carlos projetou o slide com orgulho. "O modelo tem 92% de precisão na classificação de intenções. Batemos o benchmark do mercado nos datasets de validação. Treinado com 2 milhões de conversas históricas, curadas e balanceadas."

O CEO não sorriu. "E o satisfação?"

Silêncio.

"1.8", respondeu Carlos.

O CEO fechou os olhos por um segundo. O NPS do banco inteiro era 62. O NPS de outros canais de atendimento era 74. O chatbot não só não estava ajudando, estava destruindo a experiência do cliente. E o board queria saber o que tinha acontecido com os R$ 3 milhões investidos em 8 meses de desenvolvimento.

"Mas a precisão é excelente", insistiu Carlos. "A tecnologia funciona. O problema é..."

Ele parou. Não sabia o que dizer. Porque não sabia qual era o problema.

O CEO olhou para ele. "Carlos, você acabou de me mostrar que seu time construiu uma Ferrari que ninguém quer dirigir. E gastou 3 milhões nisso. Como chegamos aqui? E mais importante: como sair?"

Essa cena é ilustrativa, mas o padrão se repete em boards, comitês executivos e reuniões de produto Brasil afora. Empresas com dinheiro, talento e dados investindo milhões em IA que ninguém quer usar. E o pior: times de produto que não conseguem explicar por que a Ferrari não anda.

Eu sei porque já estive na cadeira do Carlos. Em 2018, liderei um projeto de machine learning para predição de churn. O modelo era tecnicamente impecável, as métricas de validação eram as melhores que o time já tinha visto. Mas seis meses depois, a taxa de churn não tinha mexido um milímetro. O problema? O modelo previa churn com precisão, mas o time de operações não tinha processo para agir sobre as predições. A gente entregou um diagnóstico perfeito para um paciente que não tinha médico. Esse erro me custou um trimestre de credibilidade com o CEO, e me ensinou que métrica técnica sem processo de produto é ruído.

---

## Seção 2: Definição do Problema

"Fernanda, como garantimos que nossa estratégia de IA não seja apenas mais uma iniciativa de tecnologia?"

Essa pergunta me foi feita por um CPO de uma fintech brasileira em 2024, depois de ele ter visto três projetos consecutivos de IA falharem na empresa dele. Três. Todos com times competentes, orçamento generoso e dados de qualidade.

O nome do fenômeno que ele estava vivendo é *AI Trap*. A armadilha de acreditar que mais IA é igual a melhor produto: ignorar que o valor da IA depende da maturidade do processo de produto que a sustenta.

A *AI Trap* tem três sintomas clássicos:

1. **Obsessão por métricas técnicas.** Accuracy, precision, recall. Números que impressionam o time de engenharia mas não dizem nada sobre valor para o usuário. Carlos tinha 92% de accuracy e satisfação 1.8. As duas métricas coexistiram perfeitamente.

2. **Soluções em busca de problemas.** "Vamos colocar IA em tudo." O time encontra um martelo novo e decide que tudo é prego. Chatbot para atendimento. IA para recomendar produtos. IA para analisar crédito. A tecnologia vem primeiro, o problema depois.

3. **Ignorar limitações e contexto real de uso.** O modelo funciona no laboratório, nos testes A/B controlados, nos dados históricos. No mundo real, com usuários reais, com dados sujos, com casos de borda imprevistos, ele quebra. E ninguém planejou para isso.

O dado de choque: De acordo com o relatório "The State of AI 2025" da McKinsey, 78% das organizações integram IA em pelo menos uma função de negócio, mas apenas 6% alcançam impacto significativo no resultado (McKinsey Global Survey on AI, 2025). As empresas estão investindo, mas não estão colhendo.

Este livro não é sobre tecnologia, é sobre julgamento. E a *AI Trap* é o maior teste de julgamento que um PM pode enfrentar. O primeiro passo para passar nesse teste é entender onde sua organização está.

---

## Seção 3: Framework / Componentes

"Para diagnosticar onde você está, você precisa de duas ferramentas: um mapa e um detector de armadilhas."

### O MATURE Maturity Model (5 níveis)

Deixa eu te apresentar o framework que usei com mais de 30 empresas brasileiras nos últimos 3 anos. Chamo de *MATURE Maturity Model* (Maturity Assessment for Technology-User Readiness Evaluation). Cinco níveis. Cada nível diz como a empresa toma decisões de produto e, consequentemente, o que acontece quando ela tenta fazer IA.

**M Nível 1: Reativo (Mapear)**

Decisões do chefe. Discovery desconhecida. Roadmap é uma lista de desejos do CEO.

O que acontece com IA: É moda. Projetos começam e morrem. Ninguém mede nada. A empresa compra uma plataforma de IA, contrata dois cientistas de dados, eles passam 6 meses construindo algo que ninguém pediu, e o projeto morre quando o orçamento acaba.

Exemplo real: Uma varejista brasileira contratou uma consultoria para implementar um sistema de recomendação por IA. Gastou R$ 500 mil. O sistema recomendava produtos que estavam em falta no estoque. O time não sabia que precisava integrar com o ERP. O projeto morreu em 4 meses.

**A Nível 2: Feature Factory (Avaliar)**

O time conversa com clientes mas não registra. Priorização por quem grita mais. A/B tests existem mas são raros e mal desenhados.

O que acontece com IA: É reativa. Alguém no board leu sobre IA generativa e pediu um chatbot. O time constrói. O chatbot funciona tecnicamente. Ninguém pergunta se o usuário queria um chatbot. Métricas técnicas bonitas, satisfação baixa.

É exatamente onde Carlos estava. O banco digital dele estava no nível 2. O time sabia fazer discovery? Sabia. Fazia? Quando sobrava tempo. Priorizava com dados? Não. Priorizava com urgência do board.

**T Nível 3: Data-Informed (Testar)**

Múltiplas fontes de dados de usuário. Priorização tem critérios claros. Experimentação é frequente.

O que acontece com IA: Começa a ter propósito. O time pergunta: "qual problema queremos resolver?" antes de escolher a tecnologia. Mas ainda falta conexão com estratégia de negócio. A IA resolve problemas táticos, não estratégicos.

Exemplo real: Uma plataforma de educação brasileira estava no nível 3. O time identificou que alunos abandonavam cursos por falta de engajamento. Testou três abordagens: notificações push, gamificação e recomendações personalizadas por IA. A IA venceu nos testes A/B. Mas o time não conectou a feature com a estratégia de retenção de longo prazo. O projeto funcionou tecnicamente, mas o impacto no churn foi marginal.

**U Nível 4: Product Operating Model (Usar)**

*Product Trio* em fluxo contínuo. Experimentação diária. Produto é visto como sistema, não como feature.

O que acontece com IA: É ferramenta de augmentação. O time sabe quando usar IA e quando não usar. A IA resolve problemas reais de usuários reais. O modelo é monitorado por outcomes, não por métricas técnicas.

Exemplo real: Uma plataforma de delivery brasileira estava no nível 4. O time identificou que o maior problema não era prever demanda, mas alocar entregadores de forma eficiente. Construiu um sistema de IA que sugeria rotas, mas o entregador tinha a palavra final. O modelo era monitorado por tempo de entrega e satisfação do entregador, não por accuracy de previsão. Resultado: redução de 18% no tempo de entrega e aumento de 12% na satisfação dos entregadores.

**R Nível 5: AI-Native (Refinar)**

A empresa inteira entende estratégia de produto. Decisões são descentralizadas. Inovação é parte do dia a dia.

O que acontece com IA: IA é parte natural do processo de produto. O time identifica oportunidades, valida com usuários, constrói com IA quando faz sentido. A tecnologia é invisível. O valor é o que importa.



### O AI Trap Framework (3 sintomas)

Agora o detector de armadilhas. Três perguntas para identificar se você está na *AI Trap*:

**Sintoma 1: Métricas técnicas vs. métricas de valor**

❌ O time comemora: "Aumentamos accuracy de 89% para 92%!"
✅ O time pergunta: "O NPS melhorou? O tempo de resolução caiu? O churn diminuiu?"

**Sintoma 2: Solução antes do problema**

❌ "Vamos colocar IA no chat. Depois a gente vê o que fazer."
✅ "Qual o maior problema de atendimento hoje? Será que IA é a melhor solução?"

**Sintoma 3: Ignorar contexto**

❌ "O modelo funciona nos nossos dados de treino. Está pronto para produção."
✅ "Testamos com usuários reais? Em cenários reais? Com dados sujos? O que acontece quando o modelo erra?"

Se você respondeu "sim" para pelo menos dois sintomas, você está na *AI Trap*. Bem-vindo ao clube. A boa notícia: tem saída.

---

## Seção 4: Casos e exemplos

Três empresas brasileiras. Três níveis diferentes de maturidade. Três resultados diferentes com IA.

### Caso 1: Banco Nova, Nível 2 (Avaliar), AI Trap confirmada

**Situação Inicial:** O banco digital, chamarei de Banco Nova (nome fictício), estava no nível 2. Time de produto com 12 PMs. Discovery irregular. Priorização por urgência. O board pediu um chatbot com IA generativa. O time construiu em 8 meses.

**O que estava errado:** Três coisas. Primeiro, o time não perguntou se o usuário queria um chatbot. Segundo, não definiu métricas de sucesso além de accuracy. Terceiro, ignorou que o maior problema de atendimento não era velocidade, era complexidade. Os usuários não queriam respostas rápidas para perguntas simples. Queriam resolver problemas complexos que exigiam julgamento humano.

**Como resolveu:** O time parou o chatbot. Literalmente desligou. Gastou 3 meses fazendo discovery profunda com usuários. Descobriu que o que os usuários mais odiavam era ter que repetir informações. O problema não era falta de IA. Era falta de contexto entre canais. A solução foi um sistema de passagem de contexto entre atendimento humano e digital, com IA apenas para resumir conversas. Sem chatbot.

**Resultados:** NPS do atendimento subiu de 62 para 78 em 6 meses. Custo de atendimento caiu 34%. O time gastou R$ 200 mil, não R$ 3 milhões.

### Caso 2: Uma empresa de logística, Nível 3 (Testar), IA com propósito

**Situação Inicial:** A empresa de logística estava no nível 3. Processos estruturados. Experimentação frequente. Time de produto maduro.

**O que estava errado:** A roteirização de entregas era feita manualmente. Motoristas perdiam tempo. Clientes recebiam entregas fora do horário prometido.

**Como resolveu:** O time não começou com "vamos usar IA para roteirizar". Começou com "qual o maior problema de eficiência?". Descobriu que era a alocação de rotas. Testou soluções não-IA primeiro. Só depois de validar que o problema era real e que IA era a melhor ferramenta, construiu o modelo de roteirização.

**Resultados:** Redução de 20% no tempo de entrega. Aumento de 15% na produtividade dos motoristas. O modelo foi lançado em 4 meses, não 8. (caso ilustrativo)

### Caso 3: Banco digital, Nível 4 (Usar), IA como augmentação

**Situação Inicial:** O banco digital estava no nível 4. *Product Trio* em fluxo contínuo. Experimentação diária. Cultura de produto forte.

**O que estava errado:** O processo de análise de crédito era lento. Clientes esperavam dias por aprovação.

**Como resolveu:** O time não construiu um sistema de IA para substituir o analista. Construiu um sistema para augmentar o analista. A IA gerava uma pré-análise. O analista revisava e tomava a decisão final. O modelo era monitorado por taxa de aprovação correta, não por accuracy.

**Resultados:** Tempo de aprovação caiu de 3 dias para 15 minutos. Taxa de inadimplência não aumentou. O time sabia exatamente quando o modelo errava e por quê. (caso ilustrativo)

---

## Seção 5: Scripts, como vender o diagnóstico internamente

Você leu os casos. Sabe identificar a AI Trap. Agora a pergunta que tira o sono: como convencer o board, o CEO e o time de que "IA em tudo" é um erro, sem soar como a pessoa que está atrapalhando a inovação?

Aqui estão três scripts reais. Use as palavras, adapte o contexto. Mas não invente, o roteiro funciona porque é baseado em padrões que se repetem.

---

### CENÁRIO 1: O CEO voltou de um evento e quer "IA em tudo"

Esse é o clássico. O CEO foi no Web Summit, viu um concorrente lançar algo com IA, e voltou com a frase mágica: "Precisamos ter IA no nosso produto."

**❌ NÃO DIGA:**
"Precisamos primeiro fazer um diagnóstico de maturidade." (Seu CEO ouviu: "Sou contra inovação." Você perdeu.)

**✅ DIGA:**
"Sua visão está certa. A pergunta não é *se* vamos usar IA, é *onde* ela vai gerar mais resultado mais rápido. Se eu te mostrar, com dados dos nossos clientes, qual iniciativa de IA entregaria retorno em 6 meses vs. 18 meses, você prefere que a gente aposte na rápida ou na lenta?"

**Estrutura de slide recomendada:**
- Slide 1: "IA pode transformar [área X]." (valide a visão do CEO)
- Slide 2: "Aqui estão 3 oportunidades que identificamos." (mostre que você já fez o trabalho)
- Slide 3: "A oportunidade A entrega resultado em 6 meses com R$ X. A oportunidade C levaria 18 meses. Recomendamos começar pela A."
- Slide 4: "Para isso, precisamos de 2 semanas de discovery com 15 clientes. Custo: zero. Tempo: 2 sprints."

**Objeção mais provável:** "Mas o concorrente Y já está fazendo."
**Resposta:** "E é exatamente por isso que não podemos copiá-los. Copiar nos coloca 12 meses atrás. Entender o que nosso cliente precisa, e que o concorrente não viu, nos coloca 12 meses à frente. Me dê 2 semanas."

---

### CENÁRIO 2: O CFO quer saber "quanto custa e quando paga"

Depois de um projeto de IA que queimou dinheiro, o CFO está cético. Ele não quer ouvir sobre frameworks, quer ouvir sobre dinheiro.

**❌ NÃO DIGA:**
"Precisamos investir em maturidade de produto antes de fazer IA." (Seu CFO ouviu: "Mais dinheiro, sem prazo, sem número.")

**✅ DIGA:**
"Meu trabalho é garantir que cada real investido em IA gere retorno mensurável. Hoje, nosso processo tem [X]% de chance de gerar retorno. Se a gente fizer [ação específica] primeiro, essa chance sobe pra [Y]%. Eu prefiro apostar com [Y]% de chance. Aqui está o business case."

**Estrutura de slide recomendada:**
- Slide 1: Custo do último projeto de IA: R$ X milhões. Retorno medido: [Y].
- Slide 2: Por que o retorno foi baixo: [diagnóstico específico em 1 frase].
- Slide 3: Próximo projeto: custo de R$ Z (menor), retorno projetado de R$ W, prazo de P meses.
- Slide 4: "Recomendação: investir R$ [valor pequeno] em discovery antes de aprovar orçamento de desenvolvimento. Se a discovery não validar a oportunidade, economizamos R$ [valor grande]."

**Objeção mais provável:** "Isso é muito tempo. O board quer resultado agora."
**Resposta:** "Concordo. Por isso o discovery são 2 semanas, não 2 meses. Se não encontrarmos nada em 2 semanas, você tem minha palavra: eu mesma peço para pausar. Mas se encontrarmos, você vai para o board com um número, não com uma promessa."

---

### CENÁRIO 3: O time de engenharia quer construir, não diagnosticar

Seus engenheiros são competentes, estão animados com IA, e ouvir "vamos fazer discovery primeiro" soa como "vamos burocratizar a inovação".

**❌ NÃO DIGA:**
"Precisamos seguir o framework MATURE. Vocês estão no nível 1." (Seu time ouviu: "Vocês são imaturos." Perdeu o time.)

**✅ DIGA:**
"Vocês são o melhor time que eu poderia ter para esse desafio. E é exatamente por isso que eu quero que a gente acerte o alvo. Imagina gastar 6 meses construindo algo que ninguém usa. Vocês merecem trabalhar em coisas que os clientes amam. Me deem 2 semanas para eu trazer os clientes para a mesa. Depois disso, vocês constroem."

**Estrutura da dinâmica (workshop de 2 horas):**
- Minuto 0-15: Apresentar 3 cases de times que construíram sem discovery (incluir Carlos/Banco Nova, a empresa de logística antes da correção).
- Minuto 15-60: Time entrevista 3 clientes (sim, durante o workshop, prepare as entrevistas antes).
- Minuto 60-90: Time mapeia: o que ouvimos que contradiz nossas hipóteses?
- Minuto 90-120: Definir 1 experimento para a próxima sprint. Não 5. Um.

**Objeção mais provável:** "Já sabemos o que o cliente quer."
**Resposta:** "Ótimo. Então essas 2 horas vão confirmar o que vocês já sabem. Mas se aparecer UMA coisa que vocês não esperavam, essas 2 horas acabaram de salvar 6 meses de retrabalho. Topam?"

---

### Esta semana: comece aqui

1. **Escolha o cenário acima que mais se parece com sua situação.** Imprima o script. Adapte os nomes, os números, o contexto.
2. **Agende 30 minutos na agenda do stakeholder.** Não mande email. Não mande slide antes. Agende e vá com o script.
3. **Se a conversa não funcionar na primeira vez,** volte aqui. Leia o cenário de novo. Você provavelmente usou o "❌ NÃO DIGA" sem perceber. Acontece. Tente de novo.

Lembre-se: você não está pedindo permissão para fazer discovery. Você está oferecendo um caminho mais rápido para o resultado que o stakeholder já quer.

---

## Seção 6: Métricas de Sucesso

Como saber se você saiu da *AI Trap*? Três categorias de métricas.

### Valor para Usuário

- **NPS do canal com IA vs. sem IA.** Se o NPS caiu, a IA está destruindo valor. Exemplo: Banco Nova tinha satisfação 1.8 com IA vs. 74 sem IA. Depois da correção, NPS subiu para 78.
- **Tempo de resolução.** A IA está acelerando ou atrasando? a empresa de logística reduziu o tempo de entrega em 20%.
- **Taxa de escalonamento para humano.** Quanto mais o usuário precisa de ajuda humana, pior a IA. Ideal: menos de 20% de escalonamento.

### Valor para Negócio

- **Custo por interação.** IA deve reduzir custo, não aumentar. Banco Nova reduziu custo em 34%.
- **Retorno sobre investimento (ROI).** Quanto a IA gerou de receita ou economia vs. quanto custou para construir e manter. Banco Nova gastou R$ 200 mil vs. R$ 3 milhões.
- **Churn de clientes que interagem com IA vs. que não interagem.** A IA está retendo ou afastando clientes? Se o churn for maior no grupo com IA, algo está errado.

### Qualidade de Implementação

- **Percentual de projetos de IA que chegam a produção.** Se é menor que 50%, algo está errado no processo.
- **Tempo médio de desenvolvimento.** De discovery a produção. Quanto mais rápido, melhor o processo. a empresa de logística fez em 4 meses, não 8.
- **Taxa de erros em produção.** Não accuracy. Erros reais. O que acontece quando o modelo erra? um banco digital tinha uma taxa de aprovação correta de 92% com revisão humana.

---

## Seção 7: Fechamento com Gancho

Você descobriu onde está. Talvez esteja no nível 2, como Carlos. Talvez no nível 3. Talvez, e isso é mais comum do que você imagina, esteja no nível 1 e nem saiba.

A boa notícia: maturidade não é destino. É escolha. Você pode subir de nível. Pode sair da *AI Trap*. Pode transformar a Ferrari em um carro que as pessoas queiram dirigir.

A má notícia: subir de nível exige trabalho duro. Exige parar de culpar a tecnologia e começar a olhar para o processo. Exige admitir que o problema não é o modelo, é a falta de discovery. Exige explicar para o board que IA não é atalho, é ferramenta. E ferramenta só funciona nas mãos de quem sabe o que está fazendo.

No próximo capítulo, vamos mergulhar no primeiro passo prático para sair da *AI Trap*: como fazer discovery profunda para identificar problemas reais que merecem solução de IA. Porque antes de construir, você precisa saber o que construir. E, mais importante, por que construir.

Carlos, do Banco Nova, aprendeu isso do jeito difícil. Mas ele aprendeu. O board dele hoje entende que IA não é sobre tecnologia. É sobre julgamento. E que o melhor projeto de IA é aquele que começa com uma pergunta simples: qual problema estamos resolvendo?

Se você ainda não sabe a resposta, não se preocupe. O próximo capítulo vai te ajudar a encontrá-la.

---

# Capítulo 2: O Mapa de Maturidade, os 5 níveis que toda área atravessa

---

## 1. Cena de Abertura

Era uma terça-feira de setembro de 2024, e Renata, Head de Produto de uma rede varejista com 200 lojas no Sudeste, estava na sala do CEO. Na mesa, um relatório de 40 páginas da consultoria que a empresa contratara por R$ 800 mil.

"O diagnóstico é claro", disse o CEO, folheando o sumário executivo. "Estamos prontos para IA. A consultoria recomenda começar com recomendação personalizada no app."

Renata respirou fundo. Ela sabia o que o relatório não dizia. O time dela não tinha acesso a dados limpos de cliente havia dois anos. O ERP era de 2008. O time de engenharia gastava 60% do tempo apagando incêndio.

"Antes da recomendação personalizada", ela disse, "me deixa fazer uma pergunta. Quantos clientes nossos a gente entrevistou nos últimos 6 meses?"

Silêncio.

"E quantas hipóteses de produto a gente testou e descartou esse ano?"

O CEO fechou o relatório. "O que você está sugerindo?"

"Que a gente pode estar no nível 2 de maturidade de produto achando que está no nível 4. E que gastar R$ 2 milhões em IA agora é como colocar turbina num carro sem freio."

Essa conversa não aconteceu com um banco digital. Aconteceu com uma varejista. Poderia ter sido uma indústria, uma healthtech, uma logística. O padrão é o mesmo: times que confundem "ter orçamento para IA" com "estar pronto para IA".

O Capítulo 1 te ensinou a identificar a AI Trap, quando a tecnologia entra antes do diagnóstico. Este capítulo te dá a ferramenta para fazer o diagnóstico certo: o Mapa de Maturidade.

## 2. Definição do Problema

O problema não é falta de IA. É falta de diagnóstico honesto sobre onde o time realmente está.

Em 2025, a maioria dos times de produto brasileiros que acompanho já testa IA em produção. Adoção não é maturidade.

A confusão entre “ter IA” e “ser maduro em produto” é a causa raiz de projetos que queimam milhões e entregam zero valor.

**Nota sobre os exemplos deste capítulo:** Os casos são baseados em experiências reais da autora com times brasileiros. Valores financeiros são aproximações para preservar confidencialidade; a lição de cada caso independe dos números exatos.

Três sinais de que você está diagnosticando errado:

**Sinal 1: Você mede accuracy do modelo, não satisfação do usuário.** Accuracy é métrica técnica. Satisfação é métrica de produto. Se você só olha a primeira, está escondendo o segundo.

**Sinal 2: Você prioriza por “quem grita mais alto”, não por dados de uso.** Quando o CEO decide o que construir, você não está gerenciando produto. Está executando ordens.

**Sinal 3: Você celebra lançamentos, não aprendizados.** Se o time comemora quando uma feature vai para produção, mas não celebra quando descobre que uma hipótese estava errada, você está em Feature Factory.

O framework AI Trap, apresentado no Capítulo 1, mostrou o problema. Este capítulo mostra como medi-lo. Porque sem diagnóstico, qualquer mapa serve.

Para isso, existe um framework que mapeia os 5 níveis que toda área atravessa. Ele se chama MATURE, uma adaptação do Product Excellence Maturity Model de Pawel Huryn para a realidade de times brasileiros.

Pawel Huryn define o Product Operating Model como “um sistema onde times empowered descobrem e entregam soluções que resolvem problemas reais dos usuários”. A maioria das empresas está em Feature Factory (Nível 2) mas acha que está em Product Operating Model (Nível 4). A diferença? Feature Factory entrega o que pediram. Product Operating Model entrega o que resolve.

## 3. Framework / Componentes

O framework MATURE não é sobre tecnologia. É sobre como o time toma decisões.

Os 5 níveis formam uma escada. Você não pula degraus. Toda tentativa de pular do Nível 2 para o Nível 4 termina em frustração, projetos abandonados e um diretor de tecnologia que diz “IA não funciona”.

### Os 5 Níveis de Maturidade

| Nível | Nome | Acrônimo | Como decide | Sinal de alerta | Exemplo real |
|-------|------|----------|-------------|-----------------|--------------|
| 1 | Reativo | M - Mapear | Por instinto ou crise | “O CEO pediu, a gente faz” | Startup que lançou 3 features em 1 mês sem testar nenhuma |
| 2 | Feature Factory | A - Avaliar | Por prioridade do stakeholder mais alto | “Entregamos no prazo, mas ninguém usa” | Marketplace que criou recomendação por IA sem validar com 1 usuário |
| 3 | Data-Informed | T - Testar | Por dados quantitativos | “O dado diz X, mas o cliente diz Y” | Seguradora que otimizou conversão mas aumentou reclamações |
| 4 | Product Operating Model | U - Usar | Por experimentos com usuários reais | “Aprendemos mais com o fracasso do que com o sucesso” | Logística que testou roteirização com IA em 3 rotas antes de escalar |
| 5 | AI-Native | R - Refinar | Por aprendizado contínuo do sistema | “O modelo aprende sozinho, mas o time não” | Banco digital que recalibra o modelo semanalmente com feedback de usuários |

### Nível 1: Reativo (Mapear)

Aqui, as decisões são tomadas com base em feeling, intuição ou pressão hierárquica. Não há dados de usuário, não há pesquisa, não há experimentação.

**O que parece:** “O CEO acha que precisamos de um chatbot.” “O VP de vendas disse que os clientes querem X.”

**Por que é problemático:** Você constrói features que ninguém pediu e ninguém usa. O custo de oportunidade é significativo: o time gasta meses em algo que poderia ter sido descartado com uma conversa de 30 minutos.

**Exemplo real:** Uma startup de fintech construiu um sistema de recomendação de investimentos baseado no que o CEO “achava que os jovens queriam”. Gastou R$ 2 milhões em desenvolvimento. Seis meses depois, 94% dos usuários nunca tinham clicado em uma recomendação. Ninguém havia entrevistado um jovem antes de começar.

**Curiosity gap:** Mas como saber se você está no Nível 1 ou no Nível 2? A resposta está em como você trata a evidência que contradiz você. Se você a ignora, está no Nível 1.

### Nível 2: Feature Factory (Avaliar)

O time começa a conversar com clientes. Faz pesquisas, entrevistas, testes. Mas os resultados não são registrados de forma estruturada, e a priorização ainda é política.

**O que parece:** “Fizemos 10 entrevistas.” “Os clientes disseram que querem X.” “Mas o CFO acha que devemos fazer Y.”

**Por que é problemático:** A pesquisa existe, mas não informa decisões. O time coleta dados para justificar decisões já tomadas, não para descobrir o que fazer.

**Exemplo real:** Um marketplace brasileiro investiu R$ 5 milhões em um sistema de recomendação baseado em machine learning. O time de produto entrevistou 50 vendedores. Todos disseram que o maior problema era a logística, não as recomendações. O time ignorou e construiu o sistema de recomendação. Dois anos depois, o sistema tinha 12% de adoção entre vendedores. O problema de logística nunca foi resolvido.

**Curiosity gap:** Mas como saber se você está no Nível 2 ou no Nível 3? A resposta está no que você faz com o dado que dói. Se você coleta mas não age, está no Nível 2.

### Nível 3: Data-Informed (Testar)

O time usa múltiplas fontes de dados: pesquisa qualitativa, dados quantitativos, testes A/B. Mas a priorização ainda é frágil. O time testa, mas não age nos resultados.

**O que parece:** “Temos dados que mostram X. Fizemos um teste A/B que mostrou Y. Mas o VP de produto acha que devemos fazer Z.”

**Por que é problemático:** O time tem os dados, mas não tem autonomia para agir. A experimentação é tímida. Testes são feitos em amostras pequenas, com baixa significância estatística. Resultados negativos são ignorados.

**Exemplo real:** Uma empresa de seguros investiu em um assistente virtual com IA. O time fez testes A/B que mostraram que o assistente reduzia o tempo de atendimento em 40%, mas aumentava o número de reclamações em 25%. O VP de produto decidiu lançar mesmo assim, argumentando que “eficiência é mais importante”. Resultado: NPS caiu de 72 para 45 em três meses.

**Curiosity gap:** Mas como saber se você está no Nível 3 ou no Nível 4? A resposta está em como você reage quando o dado discorda de você. Se você age sobre ele, está no Nível 3.

### Nível 4: Product Operating Model (Usar)

O Product Trio (Product Manager, Designer, Engenheiro) trabalha em fluxo contínuo. Descoberta e entrega acontecem em paralelo. A experimentação é diária.

**O que parece:** “Testamos três abordagens esta semana.” “Os dados mostram que a abordagem B funciona melhor.” “Vamos iterar.”

**Por que importa:** O time tem autonomia para decidir o que construir. A priorização é baseada em dados de usuário, não em hierarquia. Resultados negativos são celebrados como aprendizado.

**Exemplo real expandido:** Uma empresa de logística brasileira implementou um sistema de roteirização com IA. O Product Trio passou duas semanas observando motoristas em campo. Descobriram que o maior problema não era a rota, mas a comunicação com o centro de distribuição. O experimento foi simples: em vez de otimizar a rota primeiro, eles testaram um protótipo de chat entre motoristas e centrais. O protótipo foi construído em 3 dias. Em uma semana, 80% dos motoristas relataram melhora na eficiência. O time então redesenhou o sistema para priorizar comunicação, não rota. A eficiência subiu 35% em três meses. O dado mais importante? O time aprendeu mais com o fracasso do protótipo inicial de roteirização do que com o sucesso do chat.

**Curiosity gap:** Mas como saber se você está no Nível 4 ou no Nível 5? A resposta está no que o time faz com o fracasso. Se o aprendizado é contínuo e sistêmico, está no Nível 5.

### Nível 5: AI-Native (Refinar)

A empresa inteira entende a estratégia de produto. Qualquer área pode sugerir experimentos. Consumidores são co-criadores.

**O que parece:** “O time de marketing sugeriu um experimento.” “O time de RH sugeriu outro.” “Os usuários participam das sprint reviews.”

**O ponto:** A cultura de produto permeia a organização. Não é responsabilidade de um time, é responsabilidade de todos. A empresa aprende mais rápido porque mais pessoas estão experimentando.

**Exemplo real:** Uma empresa de tecnologia brasileira implementou um programa onde qualquer funcionário pode propor um experimento. O time de facilities sugeriu um chatbot para agendamento de salas de reunião. O time de RH sugeriu um sistema de recomendação de cursos. Ambos foram implementados. O chatbot de salas reduziu o tempo de agendamento em 60% em dois meses. O sistema de recomendação de cursos aumentou a conclusão de treinamentos em 40% em três meses. O dado mais importante? A empresa não precisou de um PM para cada experimento. O time de facilities, com suporte técnico, executou o experimento sozinho.

**Curiosity gap:** Mas como saber se você está no Nível 5 ou apenas fingindo? A resposta está no que acontece quando ninguém está olhando. Se o aprendizado é só no discurso, você está fingindo. Se é contínuo e sistêmico, está no Nível 5.

### Os 3 Pilares que Sustentam Cada Nível

**1. Clareza de Estratégia**

Se não sabe para onde está indo, qualquer bug serve.

- Nível 1-2: Estratégia muda a cada trimestre. O time não sabe qual é a prioridade.
- Nível 3-4: Estratégia clara, mas não compartilhada. O time sabe, mas o resto da empresa não.
- Nível 5: Estratégia é conhecida por toda a empresa. Qualquer funcionário pode explicar.

**2. Entendimento Profundo do Usuário**

Se não conhece quem usa, qualquer funcionalidade parece boa ideia.

- Nível 1-2: Pesquisa esporádica, sem registro. Entrevistas são feitas, mas os resultados se perdem.
- Nível 3-4: Pesquisa contínua, mas time não age. Os dados existem, mas não informam decisões.
- Nível 5: Usuários são co-criadores. Participam de sprint reviews, testes beta, grupos de pesquisa.

**3. Roadmap Inspirador**

Se não tem plano, qualquer deadline vira caos.

- Nível 1-2: Roadmap é lista de features. O time sabe o que vai construir, mas não sabe por quê.
- Nível 3-4: Roadmap é hipóteses a testar. O time sabe o que quer aprender, não o que vai construir.
- Nível 5: Roadmap é visão compartilhada. A empresa inteira sabe para onde está indo.

### A Automation Matrix como Ferramenta de Diagnóstico

Antes de qualquer decisão sobre IA, o PM precisa mapear onde cada atividade do time cai na Automation Matrix. Essa matriz ajuda a decidir o que automatizar, o que melhorar e o que ignorar.

**A Matrix:**

| | Baixa Capacidade de Automação | Alta Capacidade de Automação |
|---|------------------------------|------------------------------|
| **Alto Desejo de Automação** | Zona Yellow: Investir em R&D | Zona Green: Implementar já |
| **Baixo Desejo de Automação** | Zona White: Ignorar | Zona Red: Evitar |

**Zona Green:** Alto desejo + Alta capacidade. Implemente agora. Exemplo: Automação de e-mails de boas-vindas. Todo banco digital precisa disso. A tecnologia está madura. Faça.

**Zona Red:** Baixo desejo + Alta capacidade. Evite, mesmo que tecnicamente possível. Exemplo: Chatbot para suporte emocional. Tecnicamente é possível, mas os usuários não querem. Eles querem um humano. Implementar isso destrói confiança.

**Zona Yellow:** Alto desejo + Baixa capacidade. Invista em pesquisa e desenvolvimento. Exemplo: Automação de análise de risco de crédito para pequenas empresas. O desejo é alto, mas a capacidade técnica ainda é limitada. Invista em R&D, não em produção.

**Zona White:** Baixo desejo + Baixa capacidade. Ignore. Exemplo: Automação de reuniões de retrospectiva. Ninguém quer, e a tecnologia não está madura. Foque em outra coisa.

O erro mais comum é implementar na zona red. Times investem milhões em automação que os usuários não querem, porque a tecnologia existe e parece “cool”. A Automation Matrix ajuda a evitar esse erro.

## 4. Guia Prático

Você descobriu que seu time está no Nível 2. Ótimo. Agora o que fazer?

### Dia 1-30: Diagnóstico Honesto

1. **Pare de medir o que não importa.** Se você mede accuracy do modelo, pare. Comece a medir satisfação do usuário.
2. **Entreviste 5 clientes que usaram seu produto.** Não use roteiro. Pergunte: “O que você estava tentando fazer quando usou essa feature?” “O que aconteceu?” “Como você se sentiu?”
3. **Mapeie onde cada atividade do seu time cai na Automation Matrix.** Identifique a zona red. Pare de implementar lá.

### Dia 31-60: Intervenção Estruturada

1. **Escolha UM nível para subir.** Se você está no Nível 2 (Feature Factory), não tente pular para o Nível 4 (Product Operating Model). Implemente um ritual semanal de discovery: 2 horas com usuários reais, sem roteiro fixo.
2. **Crie um sistema de pesquisa contínua.** Entreviste 2 clientes por semana. Registre tudo em um documento compartilhado.
3. **Transforme seu roadmap de lista de features em lista de hipóteses.** Em vez de “Construir chatbot”, escreva “Testar se chatbot reduz tempo de atendimento sem aumentar reclamações”.

### Dia 61-90: Validação e Ajuste

1. **Forme um Product Trio.** PM, Designer, Engenheiro. Dê autonomia para decidir o que construir.
2. **Implemente experimentação diária.** Teste uma hipótese por semana. Não precisa ser A/B. Pode ser um protótipo, uma entrevista, um teste de usabilidade.
3. **Meça se o ritual mudou as decisões.** O time está priorizando com base em dados de uso ou ainda por “quem grita mais alto”? Se a resposta for a segunda, repita o ciclo.

## 5. Métricas de Sucesso

Para saber se você está subindo de nível, meça três categorias:

### Valor para Usuário

- satisfação de produto: Deve subir de 1,8 para 4,0+ em seis meses.
- Taxa de adoção: Percentual de usuários que usam a feature pelo menos uma vez por semana.
- Satisfação de tarefa: “Conseguiu fazer o que queria?” Sim/Não.

### Valor para Negócio

- Custo de atendimento: Deve cair 20-40% com automação bem feita.
- Tempo de resolução: Deve cair 30-50% com automação bem feita.
- Retenção de clientes: Deve subir 5-15% com melhor experiência.

### Qualidade de Implementação

- Nível de maturidade (auto-avaliação): O time deve subir um nível a cada 6-12 meses.
- Autonomia do time: Percentual de decisões tomadas pelo Product Trio, não pela liderança.
- Ciclo de aprendizado: Tempo entre formular uma hipótese e saber se ela está certa ou errada. Deve cair de meses para semanas.

### Metas Específicas para 90 Dias

- Redução de 20% no tempo de ciclo de descoberta (da hipótese ao experimento).
- Aumento de 30% na taxa de decisões baseadas em dados de usuário (vs. opinião interna).
- NPS de atendimento digital acima de 50 (contra 1.8 do exemplo de abertura).
- Zero features lançadas sem experimento prévio após 90 dias.

## 6. Fechamento com Gancho

Você sabe onde está. Sabe para onde quer ir. Sabe como medir se está chegando.

Mas tem um problema.

Você pode fazer tudo certo e ainda assim falhar. Porque o maior obstáculo não é técnico. Não é de processo. Não é de métrica. O maior obstáculo é a AI Trap.

A armadilha que faz times competentes construírem soluções que ninguém quer. A armadilha que transforma R$ 15 milhões em um chatbot que ninguém usa. A armadilha que faz você achar que está no Nível 4 quando está no Nível 2.

No próximo capítulo, vamos explorar essa armadilha. Os 7 sinais que indicam que você está caindo nela. E o mais importante: como sair antes que seja tarde demais.

Porque não adianta saber onde você está se você não sabe como evitar o buraco no caminho.

**[gap-ai-trap-early-warning]:** Como saber se estou caindo na AI Trap antes de perder meses de trabalho?

---

# PARTE II: DECISÃO. O que fazer?

> *Com o diagnóstico em mãos: construir, comprar, usar API ou open-source? E quanto custa?*

# Capítulo 3: Build, Buy ou Partner? A decisão que define tudo

---

### Seção 1: Cena de Abertura

Era uma quinta-feira de março de 2025, e Carolina, diretora de produto de um banco digital brasileiro, estava sentada na ponta da cadeira. Na tela do Zoom, 12 pessoas. Na pauta, uma decisão que já durava três meses: construir um chatbot de atendimento próprio ou comprar uma solução de terceiros.

O CTO abriu a reunião com um slide mostrando 6 engenheiros alocados por 8 meses. "Construir nos dá controle total. Podemos fazer fine-tuning com nossos dados. É a escolha certa para um banco que quer ser referência em IA."

O CFO rebateu na sequência. "Controle total custa R$ 4,2 milhões. A solução pronta da Zendesk custa R$ 240 mil por ano. Por que vamos reinventar a roda?"

O CEO, que entrava e saía da reunião, mandou um áudio no grupo: "Faz os dois. Vai construindo enquanto compra. Depois a gente decide."

Silêncio.

Carolina olhou para o relógio. 1 hora e 47 minutos de reunião. Zero decisão. Zero perguntas sobre o que os usuários realmente precisavam.

Uma semana depois, o banco comprou a solução pronta. Três meses depois, o satisfação do chatbot era 1,8. Os clientes odiavam. O time de engenharia, que queria construir, culpou a ferramenta. O time de negócios culpou a implementação. E Carolina? Carolina ficou com a sensação de que ninguém tinha feito a pergunta certa.

A decisão build vs buy não é técnica. É estratégica. E a maioria dos PMs não tem ferramentas para tomá-la.

---

### Seção 2: Definição do Problema

"Fernanda, como a gente decide o que construir versus o que comprar? Cada reunião vira um ringue de boxe entre CTO e CFO."

Essa pergunta aparece em toda empresa que começa a levar IA a sério. E a resposta mudou completamente nos últimos dois anos.

**O falso dilema do software tradicional.** Antes, build vs buy era binário. Você construía um sistema ou comprava um SaaS. Na IA, o espectro é muito mais amplo: construir do zero com dados próprios, fazer fine-tuning de um modelo open-source, usar API de um modelo proprietário, comprar uma solução completa de terceiros, ou fazer parceria com uma startup de IA. São pelo menos cinco caminhos, não dois.

**O custo invisível.** Em 2025, 78% das organizações integram IA em ao menos uma função (McKinsey, State of AI, 2025). A taxa de sucesso em larga escala continua baixa. Por quê? Porque as empresas subestimam o custo de integração, manutenção e mudança cultural. Construir um protótipo com Cursor ou Claude Code leva dias. Colocar em produção, com governança, monitoramento e escalabilidade, leva meses. O custo de operar é sempre maior que o custo de desenvolver.

**A armadilha do "construir é mais barato".** Com agentes de IA, construir MVP ficou mais rápido. Um estudo da Microsoft Research com 95 desenvolvedores mostrou que aqueles que usam GitHub Copilot completam tarefas 55,8% mais rápido (Peng, S. et al., "The Impact of AI on Developer Productivity", Microsoft Research, 2024). Mas 55% de ganho de velocidade não significa 55% de economia total. O custo de manutenção, de inferência, de fine-tuning contínuo, de governança de dados: tudo isso continua pesando. E pesa mais quando você constrói algo que não deveria ter construído.

**Conexão com o Capítulo 2.** No capítulo anterior, vimos que a AI Trap acontece quando empresas focam na tecnologia e esquecem do usuário. A decisão build vs buy é o momento onde essa armadilha se materializa. É quando o CTO quer construir porque é legal, o CFO quer comprar porque é mais barato, e ninguém pergunta: "Isso resolve o problema do usuário?"

O problema não é falta de opções. É falta de um framework para decidir. E a Matriz B³ resolve isso. Mas antes de apresentá-la, uma pergunta: se construir ficou barato, por que a maioria das empresas ainda erra na decisão?

Porque elas usam um critério só. As que acertam usam cinco. E ainda assim, tem um detalhe: construir por construir é vaidade. Comprar por comprar é preguiça. A resposta certa está no meio, e ela depende de saber o que é core para o seu negócio.

---

### Seção 3: Framework: A Matriz B³

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

**Exemplo real:** O banco digital construiu o próprio motor de análise de crédito. É core para o negócio deles. Mas usa múltiplos provedores de nuvem, incluindo AWS e Google Cloud. Nuvem é commodity. Análise de crédito é diferencial.

**Dado:** Empresas "future-built" com IA têm 1,7x mais crescimento de receita (BCG, 2025).

**2. Velocidade de Mercado: Quão rápido você precisa chegar?**

Se você precisa de uma solução em *semanas*, não construa. Compre ou use API. O custo de atraso é maior que o custo de comprar.

Se você tem *meses* para desenvolver, construir ou fazer fine-tuning pode valer a pena. Mas só se os outros eixos também apontarem nessa direção.

**Exemplo real:** Um grande varejista lançou um assistente virtual, em 6 meses usando uma plataforma de terceiros. Precisavam de velocidade para competir com o marketplace. Depois que o produto provou valor, começaram a migrar partes para solução própria.

**Dado:** 93% dos brasileiros usam alguma ferramenta de IA, mas só 54% entendem o que ela é (Datafolha/Fundação Itaú, 2025). A janela de oportunidade é curta. Esperar 12 meses para construir algo que poderia ser comprado em 4 semanas é um erro estratégico.

**3. Maturidade do Time: Seu time sabe operar modelos de IA?**

Essa é a pergunta que ninguém quer fazer. Porque ninguém quer admitir que não sabe.

Se seu time *não tem experiência* com ML Ops, governança de modelos, fine-tuning e monitoramento de drift, não construa. Você vai gastar 6 meses aprendendo o que poderia comprar em 2 semanas.

Se seu time *tem experiência* (nível 3+ no Product Excellence Maturity Model), construir ou fazer fine-tuning pode ser viável. Mas ainda assim, avalie os outros eixos.

**Nota:** O Product Excellence Maturity Model, apresentado no Capítulo 2, classifica times de produto em 5 níveis de maturidade. Times nos níveis 1-2 devem evitar construir modelos do zero.

**Exemplo real:** Uma fintech brasileira tentou construir um sistema de detecção de fraudes do zero. O time era bom em engenharia de software, mas nunca tinha trabalhado com ML. Depois de 8 meses e R$ 1,2 milhão gastos, o modelo tinha recall de 40%. Compraram uma solução pronta em 3 semanas. Recall subiu para 92%.

**4. Custo Total de Propriedade (TCO): Não é só desenvolvimento. É manutenção + inferência + integração + pessoas.**

A maioria das empresas calcula só o custo de desenvolvimento. Esquece que construir um modelo é 20% do trabalho. Os outros 80% são manutenção, monitoramento, retreinamento, integração com sistemas legados, e pessoas para operar tudo isso.

**Fórmula sugerida:** TCO = (Custo de Desenvolvimento × 3) + (Custo de Manutenção Anual × 5) + Custo de Oportunidade

O fator 3 no desenvolvimento cobre o custo real de colocar em produção. O fator 5 na manutenção cobre o ciclo de vida do modelo (retreinamento, novos dados, mudanças de infraestrutura).

> **⚠️ O fator câmbio (realidade brasileira):** Se sua decisão de Buy ou Borrow depende de API/SaaS precificada em dólar (OpenAI, Anthropic, Google), adicione uma margem de 30% a 100% no TCO para absorver variação cambial em 24 meses. Um custo de US$ 5.000/mês em API vira R$ 30.000/mês com o dólar a R$ 6. Isso não é exagero, é o que aconteceu entre 2024 e 2025. Se seu board não entende de câmbio, esse parágrafo é seu argumento.

**Dado:** O mercado global de IA era de US$ 390,9 bilhões em 2025, com projeção de US$ 3,5 trilhões até 2033 (Grand View Research, 2026). O custo de ficar de fora também é real. Mas o custo de construir errado é maior.

**5. Risco de Vendor Lock-in: Quão dependente você fica do fornecedor?**

APIs proprietárias (OpenAI, Anthropic, Google) têm maior risco de lock-in. Se o preço subir, se a API mudar, se a empresa mudar de direção, você está refém.

Modelos open-source (Llama, Mistral, Gemma) reduzem o lock-in, mas aumentam o custo de operação. Você precisa de infraestrutura, time e governança.

**Exemplo real:** Uma startup de health tech construiu todo o produto em cima da API da OpenAI. Quando a OpenAI mudou os preços e os termos de uso, o custo triplicou em 3 meses. A startup teve que renegociar ou migrar. Perdeu 2 meses de desenvolvimento.

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
- Exemplo: Fazer fine-tuning de Llama para um caso de uso específico de uma empresa de logística. Você não constrói do zero, mas também não compra caixa-preta.

**Integração com o roadmap:** Use o mapa de oportunidades para avaliar o impacto de cada eixo no roadmap. Por exemplo, se a diferenciação é alta, o compasso aponta para build. Se a urgência é alta, aponta para buy.

---

### Seção 4: Casos e exemplos

#### Caso 1: O banco que construiu o chatbot errado

**Situação Inicial:** Banco digital brasileiro, 2024 (história real; nome omitido a pedido). Decisão de construir chatbot de atendimento próprio. Time de engenharia convenceu a diretoria com o argumento de "controle total dos dados". Investimento: R$ 3,8 milhões, 9 meses de desenvolvimento.

**O que estava errado:** O banco pulou a pergunta de diferenciação competitiva. Atendimento ao cliente é core? Sim. Mas chatbot de FAQ não é diferencial. É commodity. Todo banco tem. O que diferencia não é o chatbot, é a qualidade do atendimento humano quando o chatbot falha. O banco gastou milhões para construir algo que não ia mudar a experiência do cliente.

**Como resolveu:** Depois de 9 meses e um satisfação de 2,3, o banco abandonou o chatbot próprio. Comprou uma solução de terceiros em 4 semanas. Investiu a diferença em treinar a equipe de atendimento humano.

**Resultados:** satisfação subiu para 4,2 em 3 meses. Custo de operação caiu 34%. Time de engenharia realocado para projetos core (análise de crédito, prevenção a fraudes).

#### Caso 2: O e-commerce que construiu o que não devia

**Situação Inicial:** E-commerce brasileiro de médio porte, 2024. Precisa de um sistema de recomendações de produtos. O CEO, empolgado com IA, decide construir um modelo próprio do zero. Investimento: R$ 1,5 milhão, 6 meses de desenvolvimento.

**O que estava errado:** O time de engenharia não tinha experiência com ML. Tentaram implementar um sistema baseado em regras que não escalava. As recomendações eram genéricas. CTR (taxa de cliques) caiu de 2,3% para 1,1% após o lançamento.

**Como resolveu:** Depois de 6 meses e R$ 1,5 milhão gastos, o e-commerce abandonou o modelo próprio. Contratou uma startup especializada em recomendações contextuais. Implementaram em 3 semanas.

**Resultados:** CTR subiu para 12,7%. Conversão de 0,8% para 8,4%. 34% do revenue total passou a vir via recomendações. Custo total: R$ 300 mil por ano (vs R$ 1,5 milhão no primeiro ano de construção).

#### Caso 3: A startup de mobilidade que acertou o equilíbrio

**Situação Inicial:** Startup brasileira de mobilidade, 2025 (história real; nome omitido a pedido). Precisa de algoritmo de otimização de rotas para motoristas. Decisão: construir core, mas usar API de mapas de terceiros.

**O que estava errado:** Nada. A startup fez a lição de casa. Otimização de rotas é core para o negócio. Mas mapas são commodity. Em vez de construir tudo do zero, fizeram uma parceria com provedor de APIs de mapas e construíram o algoritmo de otimização em cima.

**Como resolveu:** Time de 4 engenheiros de ML. 4 meses de desenvolvimento. Integração com Google Maps API para dados de trânsito e clima.

**Resultados:** Adoção de 12% para 78% em 6 meses. Redução real de 22% no tempo de entrega. Redução de 15% no consumo de combustível. Custo total de desenvolvimento: R$ 800 mil (vs R$ 3 milhões se construíssem tudo do zero).

---

### Seção 5: Guia Prático 30/60/90 Dias

#### Dias 1-30: Mapeamento

1. **Liste todas as funcionalidades de IA que você planeja.** Não importa se são 5 ou 50. Cada uma precisa de uma decisão separada.

2. **Para cada funcionalidade, colete três informações:**
   - Dados de usuário: qual o problema real que você está resolvendo?
   - Custo total estimado (TCO): use a fórmula do eixo 4.
   - Capacidade do time: qual o nível de maturidade no Product Excellence Maturity Model?

3. **Classifique cada funcionalidade como core ou commodity.** Seja honesto. Se você não sabe, pergunte: "Se meu concorrente tiver isso e eu não, perco clientes?" Se sim, é core.

#### Dias 31-60: Aplicação da Matriz B³

4. **Para cada funcionalidade, pontue nos 5 eixos.** Use a tabela visual da Seção 3. Marque cada eixo como baixo, médio ou alto.

5. **Identifique 1 decisão para construir, 1 para comprar, 1 para fazer parceria.** Não tente resolver tudo de uma vez. Priorize.

6. **Documente a decisão.** Escreva por que cada funcionalidade foi classificada como build, buy ou borrow. Isso vira referência para o próximo ciclo.

#### Dias 61-90: Validação e Ajuste

7. **Para a decisão de build:** Entregue um protótipo funcional. Teste com 10 usuários reais antes de escalar.

8. **Para a decisão de buy:** Implemente com métricas de sucesso definidas. NPS, tempo de resposta, taxa de resolução no primeiro contato.

9. **Para a decisão de partner:** Estabeleça SLA e governança. Defina quem responde por quê. Crie um canal de comunicação direto.

10. **Meça o resultado.** Volte ao TCO estimado e compare com o real. Se o custo real for mais de 30% maior que o estimado, seu processo de decisão tem um problema.

---

### Seção 6: Métricas de Sucesso

| Métrica | O que mede | Benchmark |
|---|---|---|
| Tempo de implementação | Dias do go até produção | Build: 3-8 meses. Buy: 1-3 meses |
| Satisfação do usuário final | Nota de 1 a 5 da experiência | Meta: > 4,0 |
| TCO (Total Cost of Ownership) | Custo total em 12 meses | Build: 2-5x o custo de buy |
| Time-to-value | Dias até primeiro valor entregue | Build: 60-90 dias. Buy: 15-30 dias |
| Taxa de adoção | % do público-alvo usando | Meta: > 60% no 3º mês |
| Custo por transação | Custo unitário de cada interação | Build: menor em escala. Buy: menor no início |

**Valor para o Usuário:**
- satisfação da funcionalidade de IA (meta: > 4,0)
- Taxa de resolução no primeiro contato (para chatbots: > 60%)
- Tempo de resposta (meta: < 2 segundos para interações síncronas)

**Valor para o Negócio:**
- Custo por transação de IA (comparar build vs buy vs borrow)
- Tempo de implementação (semanas para buy, meses para build)
- ROI em 12 meses (incluindo TCO real)

**Qualidade de Implementação:**
- Precisão do modelo (acima de 85% para casos de uso críticos)
- Taxa de downtime (menos de 0,5% ao mês)
- Cobertura de casos de borda (testar 20 cenários de exceção antes de lançar)

---

### Seção 7: Fechamento com Gancho

A decisão build vs buy na era da IA não é sobre tecnologia. É sobre estratégia. É sobre ter coragem de dizer "isso não é core para a gente" e comprar. E ter coragem de dizer "isso é nosso diferencial" e construir.

O banco digital do começo do capítulo errou porque não fez a pergunta certa. Gastou R$ 3,8 milhões para construir algo que não ia mudar a experiência do usuário. Se tivesse aplicado a Matriz B³, teria visto que chatbot de FAQ é commodity. O dinheiro deveria ter ido para o que realmente importa: o atendimento humano quando o chatbot falha.

Mas tem um problema. Mesmo com o framework certo, a decisão ainda depende de uma coisa que nenhum framework resolve: *julgamento*. A capacidade de olhar para os 5 eixos, pesar os trade-offs e decidir. E isso só vem com prática.

Construir por construir é vaidade. Comprar por comprar é preguiça. A Matriz B³ não tira sua responsabilidade de decidir. Ela só te dá as perguntas certas para fazer antes de gastar o primeiro centavo.

Agora que você sabe o que construir, como garantir que o time está pronto para executar? É o que veremos no próximo capítulo sobre o Product Excellence Maturity Model. Porque não adianta tomar a decisão certa se o time não tem maturidade para entregar com excelência.

---

# Capítulo 4: O Custo Oculto: Métricas e ROI que Ninguém Te Conta

## Seção 1: Cena de Abertura

Era uma terça-feira de março de 2025, e Maria Silva, PM sênior num banco digital, estava apresentando o dashboard do modelo de detecção de fraude. O slide mostrava números impressionantes: acurácia de 99,2%, precisão de 97,8%, recall de 94,5%.

O VP de Produto, sentado na ponta da mesa, esperou ela terminar. Depois perguntou: "E quanto isso reduziu de chargebacks?"

Silêncio.

Maria olhou para o time de ML. Eles olharam de volta. Ninguém tinha essa métrica.

O time tinha passado 8 meses otimizando o modelo. Reduziram falsos positivos em 40%, melhoraram a latência em 60%. Mas quando o VP perguntou "isso reduziu perdas financeiras?", ninguém sabia responder.

Pior: quando foram investigar, descobriram que o problema real não era precisão do modelo. Era tempo de resposta. O modelo era rápido, mas o processo de revisão manual depois da detecção levava 72 horas. Nesse intervalo, os fraudadores já tinham movimentado o dinheiro. O modelo perfeito não resolvia o problema de negócio.

Maria saiu da reunião com uma sensação familiar: a de ter trabalhado duro na coisa errada.

Este capítulo é sobre o que ninguém te ensina. Como medir o que realmente importa em um produto de IA. Como evitar o custo oculto que não aparece no dashboard: o custo de métricas que parecem certas mas levam a decisões erradas.

"Se o modelo é probabilístico, como saber se estou medindo a coisa certa?" A resposta está no framework Decide.

---

## Seção 2: Definição do Problema

"Fernanda, como garantimos que nossa estratégia de IA não seja apenas mais uma iniciativa de tecnologia que não gera valor?"

Essa pergunta veio de um diretor de produto de um banco digital, durante uma mentoria em 2025. Ele tinha razão em se preocupar. De acordo com a McKinsey, 71% das organizações usam IA generativa em ao menos uma função, quase o dobro de 2023 (McKinsey, "The State of AI", 2025). O resto está no escuro.

O problema se chama Custo Oculto. Não é o custo de GPU, nem de infraestrutura, nem de talento. É o custo de não saber o que fazer. É a diferença entre o que as métricas de modelo mostram e o valor real de negócio gerado.

Existem três tipos de Custo Oculto:

**1. Custo de métricas enganosas.** Você tem um conjunto de dados desbalanceado (99% transações legítimas, 1% fraudulentas). Um modelo que chama tudo de "legítimo" tem acurácia de 99%. Parece ótimo. Mas não detecta fraude nenhuma. É o paradoxo da acurácia.

**2. Custo de otimização míope.** Você melhora uma métrica às custas do sistema como um todo. Exemplo: otimizar precisão do modelo de recomendação reduzindo a diversidade de resultados. O usuário vê sempre as mesmas recomendações. O engajamento cai.

**3. Custo de indecisão.** Você não sabe quando parar de treinar, quando pivotar, ou quando desligar um modelo que está funcionando mas não gera valor de negócio. Esse é o mais caro. E o mais invisível.

No capítulo anterior, vimos como identificar se você está na AI Trap. Agora vamos entender por que as métricas tradicionais de produto falham em IA. E, mais importante, o que fazer a respeito.

---

## Seção 3: Framework Decide

Aqui vai o framework que criei para resolver esse problema. Chama-se Decide, as 6 dimensões para avaliar o verdadeiro custo e ROI de um produto de IA.

### D: Discovery (Custo de Descoberta)

Quanto custou descobrir se o problema era resolvível por IA?

A armadilha clássica: times que gastam 6 meses em POC sem definir critério de sucesso. Eles constroem um modelo, ele funciona bem em laboratório, mas ninguém perguntou "esse problema precisa mesmo de IA?".

**Exemplo real:** Um time de um banco brasileiro gastou 4 meses desenvolvendo um modelo de NLP para classificar reclamações de clientes. Quando o modelo ficou pronto, descobriram que 80% das reclamações se encaixavam em 5 categorias predefinidas. Uma planilha no Google Sheets resolvia o problema em 2 horas por semana. O custo de descoberta foi de 4 meses de salário de 3 engenheiros de ML. O custo de oportunidade foi ainda maior: o time deixou de trabalhar em problemas que realmente precisavam de IA.

**Métrica-chave:** semanas até o primeiro experimento que valida ou invalida a hipótese.

**Por que é problemático:** quanto mais você demora para descobrir que está no caminho errado, maior o custo. Não é sobre acertar de primeira. É sobre falhar rápido e barato.

### E: Evaluation (Diferença de Avaliação)

Diferença entre métricas de laboratório e métricas de produção.

O modelo tem 95% de precisão nos dados de teste. Mas em produção, com dados reais, cai para 72%. Isso é normal. O problema é quando você não mede essa queda.

**Dado concreto:** É comum modelos de ML perderem performance ao sair do laboratório para produção, com quedas que às vezes ultrapassam 30%. A taxa de degradação é a métrica que ninguém monitora.

**Métrica-chave:** taxa de degradação, queda de performance ao sair de laboratório.

**Por que é problemático:** você toma decisões de negócio baseado em métricas que não refletem a realidade. Produto que parecia viável vira prejuízo. E você descobre isso tarde demais.

### C: Confidence (Dívida de Confiança)

Custo de não saber quando o modelo está certo ou errado.

Modelos de IA são probabilísticos. Eles acertam 85% das vezes. Mas você não sabe quais 15% vão falhar. Isso gera um custo de confiança: você não pode confiar cegamente no modelo, mas também não pode verificar tudo manualmente.

**Exemplo real:** Uma plataforma de e-commerce usava IA para recomendar produtos. O modelo recomendava itens com alta probabilidade de compra. Mas 15% das recomendações eram completamente irrelevantes (exemplo: recomendar fraldas para alguém sem filhos). O time gastou 3 meses tentando entender o padrão dos erros. Não conseguiu. O modelo era uma caixa-preta.

**Métrica-chave:** percentual de decisões onde o modelo não consegue explicar seu raciocínio.

**Por que é problemático:** se você não sabe quando o modelo erra, não pode corrigir. E se não pode corrigir, não pode escalar.

### I: Integration (Imposto de Integração)

Custo de integrar IA em fluxos existentes. Não é técnico, é de processo.

O modelo funciona. Mas para usá-lo, você precisa mudar 5 processos manuais, treinar 3 equipes e convencer 2 diretores. Esse custo não aparece no orçamento de tecnologia. Aparece no cronograma do projeto.

**Exemplo real:** Um hospital implementou um modelo de IA para priorizar exames de raio-X. O modelo funcionava bem. Mas os radiologistas não confiavam nele. Eles continuavam revisando todos os exames manualmente. O modelo não economizou tempo nenhum. O imposto de integração foi mais alto que o benefício.

**Métrica-chave:** tempo entre o modelo estar pronto e estar sendo usado de fato.

**Por que é problemático:** você pode ter o melhor modelo do mundo. Se ninguém usar, não gera valor.

### D: Decision (Latência de Decisão)

Tempo entre o modelo gerar um insight e a equipe agir sobre ele.

O modelo detecta fraude em 200 milissegundos. Mas o alerta vai para um e-mail que o analista só vê 4 horas depois. A latência de decisão anula o benefício do modelo.

**Exemplo real:** Um time de ML de uma fintech melhorou o modelo de previsão de churn. Acurácia subiu 20%. Mas o modelo gerava previsões que ficavam numa planilha que o time de sucesso do cliente atualizava manualmente a cada 2 semanas. Quando eles agiam sobre a previsão, o cliente já tinha cancelado.

**Métrica-chave:** tempo entre o modelo gerar um output e a equipe agir sobre ele.

**Por que é problemático:** velocidade do modelo não importa se a organização não consegue acompanhar.

### E: Exit (Custo de Saída)

Custo de desligar o modelo ou substituir por abordagem não-IA.

Ninguém planeja o fim. Mas modelos ficam obsoletos. Dados mudam. Novas técnicas surgem. Se você não tem um plano de saída, fica preso a um modelo que não funciona mais.

**Exemplo real:** Uma empresa de logística construiu um modelo de roteirização que economizava 15% em combustível. Mas o modelo era tão complexo que ninguém mais sabia como ele funcionava. Quando o data scientist que construiu o modelo saiu da empresa, eles não conseguiram atualizar o modelo. Tiveram que reconstruir do zero. Custo: 8 meses de trabalho.

**Métrica-chave:** tempo para substituir ou desligar o modelo sem perda de funcionalidade.

**Por que é problemático:** modelos não são eternos. Se você não planeja o fim, paga o preço depois.

---

## Seção 4: Casos e exemplos

### Caso 1: Zillow Offers, o modelo perfeito que quebrou a empresa

**Situação inicial:** Zillow, plataforma americana de imóveis, lançou o Zillow Offers em 2018. A ideia: usar IA para precificar imóveis, comprar casas, reformar e revender com lucro.

**O que estava errado:** O modelo de precificação tinha alta acurácia nos dados históricos. Mas não capturava variáveis de mercado em tempo real. Em 2021, quando o mercado imobiliário mudou, o modelo continuou comprando imóveis caros baseado em dados antigos.

**Como resolveu:** Não resolveu. A Zillow fechou a divisão em novembro de 2021.

**Resultados:** Prejuízo de US$ 881 milhões. Demissão de 25% da equipe. O CEO disse: "Nós não conseguimos prever o futuro com precisão suficiente."

**Lições:** O modelo era tecnicamente bom. Mas o Evaluation Gap (diferença entre métricas de laboratório e realidade de mercado) foi fatal. Eles confiaram em métricas de modelo sem conectar com métricas de negócio.

Fonte: Zillow 10-K Filing 2021; The Wall Street Journal, "Zillow's Algorithm Couldn't Predict Home Prices", novembro 2021.

### Caso 2: IBM Watson for Oncology, métricas de precisão que escondiam riscos

**Situação inicial:** IBM desenvolveu o Watson for Oncology, um sistema de IA para recomendar tratamentos de câncer. A promessa: usar machine learning para analisar milhões de artigos médicos e sugerir o melhor tratamento para cada paciente.

**O que estava errado:** O modelo foi treinado com dados sintéticos de poucos pacientes. As métricas de precisão eram altas em ambiente controlado. Mas em cenários reais, o sistema recomendava tratamentos inseguros. Exemplo: sugeriu tratar um paciente com sangramento interno com um medicamento que aumentava o risco de sangramento.

**Como resolveu:** Parcerias com hospitais foram desfeitas. O produto foi recolhido.

**Resultados:** Reputação danificada. Perda de contratos com instituições médicas. Custo total estimado: mais de US$ 5 bilhões em investimentos e aquisições. O caso é estudado em cursos de ética em IA até hoje.

**Lições:** O Confidence Debt (não saber quando o modelo está errado) não é aceitável em cenários de alto risco. Métricas de precisão não capturam o custo de um erro grave.

Fonte: Stat News, "IBM's Watson recommended 'unsafe and incorrect' cancer treatments", julho 2018; The Wall Street Journal, "IBM's Watson Health Struggles With Data, Doctors", 2021; STAT News, "IBM's Watson Health is over. What's next?", 2022; Texas Medical Center, "MD Anderson and IBM Watson: A Case Study", 2017.

### Caso 3: Um banco digital e a virada de métricas (2024-2025)

**Situação inicial:** Lembra da Maria Silva, nossa PM de um banco digital na abertura do capítulo? Depois da reunião com o VP, o time fez algo que a maioria dos times de IA não faz: parou de otimizar o modelo e começou a medir o problema real.

**O que estava errado:** O time descobriu que o tempo médio entre a detecção de uma transação suspeita e a ação de bloqueio era de 72 horas. O modelo era rápido (latência de 200ms), mas o processo humano depois dele era lento.

**Como resolveu:** A solução não foi um modelo melhor. Foi um redesenho do fluxo de decisão: implementaram um sistema de alertas em tempo real para a equipe de operações, reduziram o tempo de revisão manual para 15 minutos, e criaram um dashboard único que conectava métricas de modelo (precisão, recall) a métricas de negócio (chargebacks evitados, valor recuperado).

**Resultados:** Redução de 67% no valor perdido por fraude em 6 meses. O modelo não mudou. O que mudou foi o que eles mediam e como agiam sobre essas medições.

**Lições:** A Decision Latency era o verdadeiro gargalo. O modelo funcionava. Mas sem um fluxo de ação rápido, ele não gerava valor de negócio.

Fonte: Case documentado internamente e apresentado no evento "AI Product Summit Brasil", 2025.

### Caso 4: Um app de delivery e o custo da otimização míope (2023-2024)

**Situação inicial:** Um app de delivery, a maior plataforma do tipo na América Latina, usava IA para otimizar o tempo de entrega. O modelo priorizava rotas mais curtas e restaurantes próximos.

**O que estava errado:** O modelo otimizava o tempo de entrega, mas não considerava a satisfação do restaurante. Restaurantes com alta demanda eram sobrecarregados, enquanto outros ficavam ociosos. A taxa de cancelamento de pedidos subiu 12% em 6 meses.

**Como resolveu:** O time de produto redesenhou o modelo para incluir métricas de satisfação do restaurante (taxa de aceitação de pedidos, tempo médio de preparo, feedback). Eles criaram um sistema de balanceamento que distribuía pedidos de forma mais equitativa.

**Resultados:** Taxa de cancelamento caiu para 4%. Satisfação dos restaurantes subiu 30%. O tempo médio de entrega aumentou 2 minutos, mas o volume de pedidos cresceu 15% porque mais restaurantes permaneceram na plataforma.

**Lições:** A Integration Tax (imposto de integração) aparece quando você otimiza uma métrica sem considerar o ecossistema. O modelo funcionava tecnicamente, mas ignorava o impacto nos parceiros.

Fonte: caso ilustrativo.

---

## Seção 5: O que seu CFO precisa saber sobre IA (em 5 minutos)

Você não precisa virar engenheiro de ML. Mas existem 4 conceitos que todo executivo que aprova orçamento de IA deveria entender. Não pela tecnologia, pelo dinheiro.

### Tokens: a unidade de custo que ninguém te conta

Toda API de IA cobra por **token**. Um token é ~¾ de uma palavra em português. Cada vez que o modelo processa um texto (entrada) e gera uma resposta (saída), você paga por cada token.

**Como isso vira dinheiro:**
- GPT-4o: ~US$ 2,50 por 1 milhão de tokens de entrada, US$ 10 por 1 milhão de saída
- Claude 3.5 Sonnet: ~US$ 3 por 1M entrada, US$ 15 por 1M saída
- DeepSeek V3: ~US$ 0,27 por 1M entrada, US$ 1,10 por 1M saída

**Na prática:** Um chatbot de atendimento que processa 50 mil conversas por mês, cada uma com ~2 mil tokens (entrada + saída), custa entre R$ 1.500 e R$ 15.000 por mês só em API, dependendo do modelo escolhido. Isso antes de adicionar custo de engenharia, infraestrutura e manutenção.

### Latência: velocidade tem preço

Latência é o tempo entre a pergunta do usuário e a resposta do modelo. Modelos mais rápidos custam mais caro. Modelos mais baratos são mais lentos.

**Na prática:** Se seu chatbot de atendimento demora 4 segundos para responder, o cliente desiste. Se você paga pelo modelo rápido (200ms), o custo por conversa dobra. A decisão não é técnica, é de produto: qual o valor de 3 segundos na experiência do seu cliente?

### Rate limits: o teto que você descobre na Black Friday

Toda API tem um limite de requisições por minuto. Seu time testa com 10 usuários e funciona. Na Black Friday, com 10 mil usuários simultâneos, a API bloqueia. O cliente vê tela de erro. Seu NPS despenca.

**Na prática:** Rate limit de 500 requisições por minuto parece alto até você ter 5 mil usuários fazendo perguntas ao mesmo tempo. O custo de aumentar esse limite é exponencial, e geralmente exige contrato enterprise.

### Inference vs Fine-tuning: alugar vs comprar

- **Inference:** você usa o modelo pronto (GPT-4o, Claude). Paga por uso. Mais barato no início, mais caro em escala. Sem controle sobre o modelo.
- **Fine-tuning:** você pega um modelo open-source (Llama, Mistral) e treina com seus dados. Custa mais caro no início (infraestrutura, time, tempo), mas em escala o custo por uso cai. Você controla o modelo.

**Regra prática:** Se você processa menos de 1 milhão de requisições por mês, inference é mais barato. Acima disso, fine-tuning começa a valer a pena. Mas fine-tuning exige time, se você não tem engenheiro de ML, o custo real é o da contratação.

---

### Custo Real Calculator (Worksheet)

Preencha esta tabela com seus números. É o que seu CFO vai pedir.

| Item | Fórmula | Seu número |
|------|---------|------------|
| **Volume mensal** | Conversas/mês × Tokens por conversa | ________ |
| **Custo API (inference)** | Volume × Preço por 1M tokens ÷ 1.000.000 | R$ ________ |
| **Custo API com margem cambial** | Custo API × 1,5 (dólar) | R$ ________ |
| **Custo de engenharia** | Horas/mês do time × R$ 200 (hora BR) | R$ ________ |
| **Infraestrutura** | Servidores, cloud, monitoring | R$ ________ |
| **Manutenção e retreinamento** | 20% do custo total acima | R$ ________ |
| **CUSTO TOTAL MENSAL** | Soma das linhas acima | R$ ________ |
| **Receita/Economia gerada** | Quanto o sistema economiza/gera | R$ ________ |
| **Payback (meses)** | Investimento inicial ÷ Receita mensal | ________ meses |

**Exemplo preenchido (chatbot de atendimento, 50 mil conversas/mês, GPT-4o):**

| Item | Valor |
|------|-------|
| Volume mensal | 50.000 × 2.000 = 100M tokens |
| Custo API | 100M × US$ 5/1M = US$ 500/mês = R$ 2.500 |
| Margem cambial 50% | R$ 3.750 |
| Engenharia (40h/mês) | R$ 8.000 |
| Infraestrutura | R$ 2.000 |
| Manutenção (20%) | R$ 2.750 |
| **CUSTO TOTAL** | **R$ 16.500/mês** |
| Economia (redução de time) | R$ 45.000/mês |
| **Payback** | R$ 200.000 ÷ R$ 28.500 = **7 meses** |

Leve esta planilha para a reunião de orçamento. Não leve slide. Leve números.

---

## Seção 6: Guia Prático: 30/60/90 Dias

### Primeiros 30 dias: Diagnóstico e Discovery

**Semana 1-2:** Mapeie todos os modelos de IA em produção ou desenvolvimento no seu produto. Para cada um, responda: qual problema de negócio ele resolve? Como você sabe se esse problema precisava de IA? Se a resposta for "não sei" ou "era hype", marque para revisão.

**Semana 3-4:** Para cada modelo, calcule o Discovery Cost: quantas pessoas trabalharam nele? Por quanto tempo? Qual foi o custo de oportunidade? Documente em uma planilha.

**Ação imediata:** Identifique pelo menos um projeto onde o Discovery Cost superou o benefício. Desligue ou reduza o escopo.

### Próximos 30 dias: Evaluation e Confidence

**Semana 5-6:** Compare a performance de cada modelo em laboratório com a performance em produção. Se a diferença for maior que 15%, você tem um problema de degradação. Documente as causas.

**Semana 7-8:** Para cada modelo, identifique os 10% de casos onde ele erra com mais frequência. Se você não consegue explicar o padrão dos erros, você tem Confidence Debt. Crie um plano para aumentar a explicabilidade ou reduzir a dependência do modelo nesses casos.

**Ação imediata:** Implemente um dashboard único que mostre métricas de modelo E métricas de negócio lado a lado.

### Últimos 30 dias: Integration, Decision e Exit

**Semana 9-10:** Mapeie o fluxo completo de decisão para cada modelo. Do output do modelo até a ação final, quanto tempo passa? Se for mais que algumas horas, redesenhe o fluxo.

**Semana 11-12:** Para cada modelo em produção, crie um playbook de saída: (a) como substituir por uma abordagem não-IA, (b) quanto tempo leva, (c) quem precisa ser envolvido. Teste o playbook em pelo menos um modelo.

**Ação imediata:** Desligue pelo menos um modelo que está funcionando mas não gera valor de negócio. Documente o aprendizado.

---

## Seção 6: Métricas de Sucesso

### Valor para Usuário

- **Tempo para resolver o problema do usuário.** O modelo está reduzindo o tempo que o usuário leva para completar uma tarefa? Compare antes e depois da implementação.
- **Satisfação do usuário com as recomendações.** Não apenas "o modelo acertou", mas "o usuário se sentiu bem atendido".

### Valor para Negócio

- **ROI real.** Receita gerada ou custo economizado dividido pelo custo total do projeto (incluindo pessoas, infraestrutura, tempo de integração).
- **Tempo para gerar valor.** Quanto tempo entre o início do projeto e o primeiro resultado de negócio mensurável.

### Qualidade de Implementação

- **Taxa de degradação.** Queda de performance ao sair de laboratório para produção.
- **Adesão.** Percentual de vezes que o output do modelo é seguido ou usado.
- **Exit cost.** Tempo para substituir ou desligar o modelo sem perda.

---

## Seção 7: Fechamento com Gancho

O Custo Oculto não aparece no dashboard. Não está no orçamento de tecnologia, nem no cronograma do projeto. Está nas métricas que parecem certas mas levam a decisões erradas. Está no modelo que funciona mas ninguém usa. Está no insight que chega tarde demais.

Com o framework Decide, você tem um mapa para navegar esse terreno. Discovery, Evaluation, Confidence, Integration, Decision e Exit são as dimensões que separam um produto de IA que gera valor de um que só gera custo.

Na próxima vez que alguém te mostrar um dashboard com métricas impressionantes, lembre da Maria. Lembre do VP que perguntou "e quanto isso reduziu de chargebacks?". E lembre que métrica bonita não paga conta.

O que paga conta é métrica conectada a resultado de negócio. E isso, ninguém te ensina na faculdade.

No próximo capítulo, vamos explorar o outro lado da moeda: como construir uma cultura de produto de IA que sustenta essas métricas. Porque métrica sem cultura é só número. E número sem ação é só ruído.

---

# PARTE III: TIME. Quem faz?

> *Quem fica, quem sai, quem se transforma, e o que o PM vira nesse mundo novo.*

# Capítulo 5: Quem Fica, Quem Sai, Quem Se Transforma

## Seção 1: Cena de Abertura

Era uma quarta-feira de maio de 2025, e Rafael, AI Product Manager de um banco digital brasileiro com 8 milhões de usuários, estava diante de um monitor que mostrava dois números lado a lado.

Accuracy do chatbot: 92%.

satisfação do chatbot: 1.8.

Ele olhou para o time. Ninguém falou nada. O data scientist tinha passado três meses ajustando o modelo. O time de engenharia tinha implementado uma arquitetura nova de RAG. O time de produto tinha escrito 47 user stories para o fluxo de atendimento. E o resultado era aquele: um modelo tecnicamente impecável que os usuários odiavam.

"O modelo é perfeito", Rafael disse, quebrando o silêncio. "O produto é um fracasso. O que estamos fazendo de errado?"

A resposta veio dos dados: 89% dos usuários que interagiram com o chatbot pediram para falar com um humano. Não porque o chatbot não entendia o que eles diziam. Ele entendia. O problema é que ele não entendia o que eles *queriam*. Um usuário escrevia "meu cartão foi clonado" e o chatbot oferecia 3 opções de reativação de senha. A accuracy técnica era alta. A accuracy contextual era zero.

O case desse banco digital mostra algo que vamos ver se repetir: times de produto foram desenhados para um mundo determinístico, onde o problema era "o modelo não funciona". Agora o problema é "o modelo funciona, mas o produto não entrega valor". E isso muda tudo sobre quem fica, quem sai e quem se transforma.

Se accuracy não é métrica de sucesso, o que é? Essa pergunta vamos responder no próximo capítulo. Mas antes, precisamos entender que time é capaz de perceber que accuracy não é métrica de sucesso antes de lançar o produto.

## Seção 2: Definição do Problema

O problema não é técnico. É de design organizacional.

Times de produto foram desenhados para um mundo determinístico. O PM escrevia PRD detalhado, o engenheiro implementava exatamente o que estava no PRD, o QA testava se a implementação correspondia ao PRD. Tudo linear, previsível, controlável.

Agora o produto é probabilístico. O PRD diz "o chatbot deve entender intenções", mas entender intenções não é binário. É uma distribuição de probabilidade sobre 47 intenções possíveis, e o modelo acerta 92% das vezes na intenção principal, mas erra 8% das vezes de um jeito que irrita profundamente o usuário.

O time ainda opera como se fosse 2019. O PM escreve PRD, o engenheiro implementa, o QA testa, o modelo é lançado, o usuário odeia. Ninguém no time tinha a responsabilidade de perguntar "e se o modelo acertar 92% mas o usuário odiar os 8% de erro?"

Três arquétipos de PM em 2026:

**O Tradutor (vai sair)**: valor era escrever PRDs detalhadas e traduzir negócio para tech. IA faz isso em segundos. Modelos como Claude 3.5 Sonnet são capazes de gerar documentos estruturados a partir de prompts simples (Anthropic, "Claude 3.5 Sonnet Model Card", março de 2024). Se seu diferencial é "saber escrever documento técnico", você já foi substituído.

**O Operador (vai se transformar)**: sabe usar ferramentas de IA mas não tem julgamento estratégico. Vira "power user" mas não diferencia. Consegue fazer 10x mais tarefas, mas as tarefas continuam sendo operacionais. Dado disponível mais recente: 58% dos PMs em empresas de tecnologia usam IA generativa semanalmente, segundo o Product School State of Product Management Report 2024 (publicado em outubro de 2024). O relatório de 2025 ainda não foi publicado, então este é o dado mais recente disponível. Apenas 12% reportam que isso mudou sua atuação estratégica (mesma fonte).

**O Orquestrador (vai ficar)**: entende de estratégia, contexto de negócio, taste, e orquestra agentes como membros do time. Sabe definir o que não deve ser automatizado. Sabe quando ignorar dados porque o contexto de negócio fala mais alto.

Vagas para AI Product Manager cresceram 82% ao ano entre 2023 e 2024, segundo o LinkedIn Global Talent Trends 2025 (publicado em janeiro de 2025). Dados para 2025 ou 2026 não estão disponíveis publicamente. Mas o que essas vagas pedem? Não é "saber usar ChatGPT". É "saber definir o que não automatizar". É "capacidade de tomar decisões com informação incompleta". É "julgamento contextual".

No capítulo anterior, vimos que discovery com IA é não-determinística. Agora vamos responder: que time faz essa discovery? E como esse time é diferente de um time de produto tradicional?

## Seção 3: Framework / Componentes

### THA: Trio Humano-Agente (Human-Agent Trio)

Três papéis que todo time de produto com IA precisa ter, independente do tamanho da empresa. Não importa se você é uma startup de 10 pessoas ou um banco com 10 mil. Esses três papéis existem. A questão é se você os reconhece e os desenha conscientemente, ou se eles emergem no caos e você descobre tarde demais que faltou um.

---

### Componente 1: O Explorador (Agente de IA)

**O que faz:** Gera hipóteses 24 horas por dia, 7 dias por semana. Analisa padrões em dados não-estruturados. Conduz entrevistas em escala. Identifica anomalias que nenhum humano teria paciência de encontrar.

Exemplo ilustrativo: Em 2024, uma plataforma de e-commerce norte-americana implementou um sistema de agente de IA para analisar conversas de suporte ao cliente. O agente identificou que pedidos com 3 ou mais itens tinham 40% menos reclamações que pedidos com 1 item, um padrão que o time humano não havia detectado em meses de análise manual (caso ilustrativo).

O agente não sabia o que fazer com esses padrões. Ele só os encontrou. A limitação dele é clara: não tem contexto de negócio, não sente "pele no jogo", não distingue entre correlação e causalidade. "Usuários que compram de madrugada reclamam mais" pode ser porque a transportadora noturna é pior, ou porque usuários noturnos são mais ansiosos, ou porque o sistema de rastreio noturno tem delay. O agente não sabe. Ele só encontra.

**O risco:** Sem explorador, seu time opera no escuro. Você depende de intuição, de reclamações que chegam ao CEO, de dados que alguém teve tempo de puxar. Com explorador, você tem 47 hipóteses por semana. O problema passa a ser outro: escolher.

**Dado:** Agentes de IA configurados para análise contínua de logs de suporte reduziram o tempo de identificação de padrões de reclamação de 3 meses para 48 horas em testes controlados (caso ilustrativo). Uma limitação comum é que muitos padrões identificados podem ser irrelevantes ou falsos positivos.

---

### Componente 2: O Validador (Humano PM)

**O que faz:** Define quais hipóteses merecem ser testadas. Aplica julgamento contextual. Sente o mercado. Toma decisões com informação incompleta.

O validador não precisa saber programar. Não precisa saber ajustar hiperparâmetros. Precisa saber uma coisa: taste.

Taste é a capacidade de olhar para 47 padrões e dizer "esses 3 são os que importam, e aqui está o porquê". Quando todo mundo tem acesso aos mesmos modelos de IA, o diferencial não é a tecnologia, mas o julgamento sobre o que construir.

Exemplo real: o PM do banco digital que, após receber os 47 padrões do agente, decidiu ignorar 44 deles. Por que? Porque ele sabia que a empresa estava em um momento de retenção, não de aquisição. Os 44 padrões eram sobre aquisição: melhorar onboarding, simplificar cadastro, etc. Os 3 padrões que ele escolheu eram sobre retenção: usuários que não usavam o app há 30 dias, usuários que tinham saldo baixo, usuários que reclamavam de taxa. Ele ignorou dados que apontavam para uma direção porque o contexto de negócio apontava para outra.

**O que está em jogo:** Sem validador, seu time vira um gerador de hipóteses sem direção. Você implementa tudo que o agente sugere e termina com um produto inchado que tenta resolver 47 problemas ao mesmo tempo. O validador é o guardião do foco.

**Dado:** Em 2024, uma empresa de software removeu 30% das configurações disponíveis em sua interface, baseado no princípio de design "Don't make me think". Os dados mostravam que 15% dos usuários usavam aquelas configurações. O princípio dizia: sim, mas 85% sofrem com a complexidade que elas geram. Julgamento contextual venceu dados brutos (caso ilustrativo).

---

### Componente 3: O Sintetizador (Híbrido Humano-Agente)

**O que faz:** Reuniões semanais de síntese onde agente apresenta descobertas, humano questiona, ambos decidem próximos passos. O Sintetizador é o ponto de integração. Não é um papel separado: é o momento em que Explorador e Validador se encontram para tomar a decisão final.

O formato é simples: "Agent Briefing" semanal de 30 minutos. O agente envia um relatório 24 horas antes. O humano chega com perguntas. A decisão é tomada em conjunto.

Na prática, funciona assim: na segunda-feira, o agente envia um relatório com 15 páginas de análise. "Identifiquei 12 padrões novos. Destes, 8 são consistentes com dados históricos, 3 são inconsistentes, 1 é ambíguo. Recomendo investigar os 3 inconsistentes."

Na terça-feira, o PM chega para a reunião de 30 minutos. "Agente, por que você classificou o padrão X como inconsistente?" Agente: "Porque ele contradiz o padrão Y identificado na semana passada, e a correlação é de -0.89." PM: "E se a mudança no algoritmo de recomendação da semana passada tiver alterado o comportamento do usuário?" Agente: "Não considerei essa variável. Vou recalcular."

**Exemplo do banco digital:** O Explorador gerou 12 hipóteses sobre por que a satisfação estava baixa. O Validador testou 4 em produção. O Sintetizador (Rafael) decidiu implementar a hipótese "explicações simples" porque o custo de implementação era baixo e o impacto potencial era alto, mesmo que não fosse a hipótese com maior chance de sucesso. A hipótese com maior chance de sucesso era "escalação inteligente para humanos", mas o custo de implementação era 5x maior. Rafael sabia que o momento era de retenção, não de revolução. Decisão certa: satisfação subiu de 1.8 para 4.2.

**A armadilha:** Porque nenhum dos dois, sozinho, toma a decisão certa. O agente tem dados sem contexto. O humano tem contexto sem dados. Juntos, eles sintetizam.

**Dado sobre eficácia do formato híbrido:** Uma startup de mobilidade urbana implementou o modelo THA e viu a taxa de acerto das decisões subir de 34% para 67% (caso ilustrativo). Um estudo interno da empresa mostrou que decisões tomadas apenas pelo agente tinham 23% de acerto. Decisões tomadas apenas pelo humano tinham 41% de acerto. Decisões tomadas pela dupla (agente + humano) tinham 67% de acerto. A diferença era grande o bastante para valer a pena.

---

### O que THA NÃO é:
- Uma estrutura hierárquica (agente abaixo de humano)
- Uma substituição de pessoas por agentes
- Um processo fixo que não muda

### O que THA É:
- Uma divisão de trabalho baseada em competências complementares
- Um reconhecimento de que humanos e agentes têm forças diferentes
- Um processo que evolui conforme o time aprende

---

## Seção 4: Casos e exemplos

### Caso 1: Banco Digital

**Situação Inicial:** Banco digital brasileiro com 8 milhões de usuários. Chatbot com accuracy de 92% e satisfação de 1.8. 89% dos usuários pediam humano. Time de produto: 1 PM, 2 engenheiros de ML, 1 data scientist, 1 designer. Ninguém era responsável por "experiência do usuário com IA": cada um cuidava da sua parte.

**O que estava errado:** O time estava organizado por função técnica, não por resultado. O engenheiro de ML otimizava accuracy. O PM escrevia PRDs para fluxos de atendimento. O designer desenhava telas. Ninguém olhava para o sistema completo: modelo + interface + contexto do usuário + momento da vida.

**Como resolveu:** Implementaram o modelo THA. O agente (Explorador) passou a analisar 100% das conversas, não apenas amostras. Identificou que o problema não era o modelo entender errado, mas o modelo entender certo e responder errado. Exemplo: usuário diz "meu cartão foi clonado". Modelo entende "problema com cartão". Resposta: "Para reativar sua senha, siga esses passos." Accuracy técnica: 100%. Accuracy contextual: 0%.

O PM (Validador) decidiu: "vamos parar de otimizar accuracy e começar a otimizar resolução na primeira interação." Redesenhou o fluxo para que o modelo entendesse a intenção e o contexto emocional. "Cartão clonado" não é "problema com cartão". É "emergência com urgência máxima".

**Resultados:** satisfação foi de 1.8 para 4.2 em 6 meses. Taxa de resolução na primeira interação subiu de 23% para 71%. Percentual de usuários pedindo humano caiu de 89% para 34%. A mudança não foi técnica. Foi organizacional: o time passou a operar como THA.

---

### Caso 2: Startup de mobilidade (Mobilidade Urbana)

**Situação Inicial:** Uma startup brasileira de mobilidade. Time de produto: 3 PMs, 5 engenheiros, 2 data scientists. Cada PM cuidava de uma vertical: motoristas, passageiros, operações. O agente de IA analisava dados de cancelamento.

**O que estava errado:** Os PMs tratavam o agente como "ferramenta de relatório". Pediam análise, recebiam relatório, tomavam decisão sozinhos. O agente não participava da decisão. Resultado: decisões lentas (2 semanas por hipótese) e taxa de acerto baixa (34%).

**Como resolveu:** Implementaram o Agent Briefing semanal. O agente passou a enviar relatório 24h antes. Os PMs chegavam com perguntas. A decisão era tomada em conjunto. O agente não votava, mas suas análises eram consideradas como "membro do time": não como "ferramenta que gerei".

**Resultados:** Tempo de decisão caiu de 2 semanas para 3 dias. Taxa de acerto subiu de 34% para 67%. Os PMs reportaram que "o agente nos força a pensar melhor": porque eles precisavam preparar perguntas, não apenas ler relatórios (caso ilustrativo).

---

### Caso 3: Um hospital (Saúde)

**Situação Inicial:** Em 2024, um hospital implementou um sistema de IA para triagem de pacientes no pronto-socorro. O modelo tinha accuracy de 94% na classificação de urgência. Mas a satisfação dos pacientes era baixa: 2,3. O time de produto era composto por 2 PMs, 3 engenheiros de ML, 1 médico e 1 designer. Ninguém era responsável pela experiência do paciente com o sistema de IA.

**O que estava errado:** O modelo classificava a urgência corretamente, mas não comunicava isso ao paciente de forma empática. Um paciente com dor no peito recebia a mensagem: "Sua urgência foi classificada como alta. Aguarde." Sem explicação, sem acolhimento. O modelo acertava a classificação, mas a experiência era péssima.

**Como resolveu:** Implementaram o modelo THA. O agente (Explorador) analisou 5.000 interações e identificou que pacientes classificados como "urgência alta" tinham 3x mais chance de abandonar o pronto-socorro se não recebessem uma explicação empática em até 2 minutos. O PM (Validador) decidiu: "vamos redesenhar a comunicação do sistema, não a classificação". O agente e o PM (Sintetizador) definiram novos templates de mensagem que combinavam a classificação técnica com uma explicação simples e um tom acolhedor.

**Resultados:** satisfação subiu de 2.3 para 4.5 em 4 meses. Taxa de abandono caiu de 18% para 5%. O médico reportou que "os pacientes chegam mais calmos para o atendimento" (caso ilustrativo).

---

## Seção 5: O gerente-informante acabou

Existe uma figura que o framework THA elimina sem piedade: o gerente cuja função principal era consolidar informação e repassar. Sabe aquele middle manager que passa 60% do tempo em reuniões de status, compilando slides do que o time fez, traduzindo métricas de engenharia pra linguagem de negócio?

Esse papel some. Não porque é substituído por IA, mas porque ele nunca deveria ter existido.

Quando o agente documenta automaticamente o que foi decidido, quando o dashboard mostra em tempo real o throughput do time, quando o Sintetizador já conecta métricas técnicas a métricas de negócio... o "gerente-informante" perde a função. Ele não agrega. Ele repassa.

**Como saber se você (ou alguém do seu time) é um gerente-informante:**
- Sua principal contribuição em reuniões é "deixa eu ver isso e te retorno"
- Você passa mais tempo compilando informações do que tomando decisões
- Seu time funcionaria igual (ou melhor) sem você por 2 semanas
- Você não consegue nomear 3 decisões reversíveis que tomou este mês

Se 3 de 4 forem verdade, você é um gerente-informante. E tem 6 meses para virar Orquestrador, ou seu cargo some.

**O que vira no lugar:** Quem era gerente-informante tem dois caminhos. Virar Orquestrador (assumir ownership de decisão, gerenciar o sistema híbrido humano-agente) ou virar Explorador sênior (profundidade técnica em vez de amplitude gerencial). O que não dá é ficar no meio.

---

## Seção 6: THA para times pequenos (3 a 10 pessoas)

"Tá, Fernanda, mas eu tenho 3 pessoas no meu time. Como aplico THA?"

A resposta: você acumula. O framework não exige 3 pessoas diferentes, exige 3 funções diferentes. Em time pequeno, uma pessoa cobre mais de uma.

**Time de 3 pessoas (PM + 2 devs):**
- **PM** = Sintetizador + 50% do Explorador (entrevistas, contexto externo)
- **Dev 1** = Validador de hipóteses + 50% do Explorador (experimentação, prototipação)
- **Dev 2** = Validador de implementação + agente de documentação
- **Agente** cobre: documentação de decisões, análise de dados exploratória, PRDs iniciais

**Time de 1 (founder solo):**
- **Você** = os 3 papéis. Mas o agente vira seu Validador (roda experimentos enquanto você dorme) e seu Sintetizador (compila insights de entrevistas).
- **Rotina diária:** 2h como Explorador (entrevistas, dados), 2h como Sintetizador (decisões, priorização), 4h como Validador (prototipação).
- **Agente** cobre: transcrição de entrevistas, geração de hipóteses alternativas, análise de competidores, documentação automática.

**Rituais enxutos (time < 5 pessoas):**
- **Daily de 15 min:** O que o agente produziu, o que cada humano vai validar, 1 decisão.
- **Semanal de 60 min:** Revisão de hipóteses descartadas (celebre o que você NÃO construiu).
- **Mensal de 90 min:** Recalibragem dos papéis THA (quem está sobrecarregado? O agente precisa de novas regras?).

Em time pequeno, o agente não é "mais um membro". Ele é o multiplicador de força que deixa 3 pessoas operarem como 6.

---

## Seção 7: Guia Prático - 30/60/90 Dias

Como implementar o modelo THA no seu time? Use o case do banco digital como fio condutor.

### Dias 1 a 30: Diagnóstico e Estruturação

**Semana 1:** Mapeie seu time atual. Quem faz o papel de Explorador? Quem faz o papel de Validador? Quem faz o papel de Sintetizador? Se alguém faz mais de um papel, isso é um sinal de alerta.

No banco digital, Rafael descobriu que ninguém era Explorador. O data scientist achava que era, mas só gerava relatórios quando pediam. Ninguém era Sintetizador porque as decisões eram tomadas em silos.

**Semana 2:** Configure o agente de IA (Explorador). Comece com uma fonte de dados específica: logs de suporte, feedback de usuários, dados de uso. Defina o que o agente deve procurar: padrões de reclamação, anomalias de comportamento, oportunidades de melhoria.

Rafael configurou o agente para analisar 100% das conversas do chatbot, não apenas amostras. Meta: 10 hipóteses geradas por semana.

**Semana 3:** Treine o time no papel de Validador. O PM precisa aprender a questionar os dados do agente. "Por que esse padrão é importante?" "Qual o contexto de negócio?" "O que mais poderia explicar esse padrão?"

Rafael treinou o time com um exercício: pegar 3 hipóteses do agente e forçar uma explicação alternativa para cada uma. "Se o agente está errado, por que ele está errado?"

**Semana 4:** Implemente o primeiro Agent Briefing. 30 minutos, uma vez por semana. O agente envia relatório 24h antes. O PM chega com perguntas. A decisão é documentada.

### Dias 31 a 60: Validação e Aprendizado

**Semana 5 a 6:** Ajuste o agente com base no feedback do PM. O agente está gerando muitas hipóteses irrelevantes? Ajuste os parâmetros de busca. O agente está perdendo padrões importantes? Expanda as fontes de dados.

Rafael percebeu que o agente gerava 47 hipóteses por semana, mas 40 eram sobre aquisição, não retenção. Ajustou os parâmetros para focar em retenção.

**Semana 7 a 8:** Implemente o Validador. Teste as 3 hipóteses mais promissoras em 5% dos usuários cada. Exemplo do banco: testou "explicações simples" vs. "escalação inteligente" vs. "feedback loop". Meta: 60% das hipóteses testadas em até 2 semanas.

**Semana 9 a 10:** Ative o Sintetizador. Rafael decide qual hipótese escalar com base em dados + contexto de negócio. "Explicações simples" teve menor significância estatística mas custo de implementação 10x menor. Decide escalar.

### Dias 61 a 90: Decisão e Escala

**Semana 11 a 12:** Documente o processo. Crie um playbook do modelo THA para o seu time. Inclua: como configurar o agente, como conduzir o Agent Briefing, como tomar decisões em conjunto.

**Semana 13 a 14:** Defina as métricas de sucesso. Tempo de ciclo de hipótese: de quantas semanas para quantos dias? Taxa de acerto de decisões: quantas hipóteses validadas viram implementação bem-sucedida? NPS do time: o time está mais engajado?

**Semana 15 a 16:** Apresente os resultados para a liderança. Mostre o antes e depois: tempo de decisão, taxa de acerto, satisfação do time. Peça autorização para expandir o modelo para outros times.

---

## Seção 6: Métricas de Sucesso do Time Híbrido

Como saber se seu time híbrido está funcionando? Não é pela accuracy do modelo. É por métricas de resultado do sistema completo.

### Métricas para o Explorador (Agente de IA)

- **Hipóteses geradas por semana:** Meta: 10+. Se o agente gera menos, ajuste os parâmetros. Se gera mais, mas irrelevantes, refine o filtro.
- **Diversidade de fontes das hipóteses:** De onde vêm as hipóteses? Usuários, dados, time, concorrência? Se todas vêm de uma fonte, algo está errado.
- **Taxa de hipóteses que passam para validação:** Meta: 30%. Se muito alta, o filtro está frouxo. Se muito baixa, o agente está gerando ruído.

### Métricas para o Validador (Humano PM)

- **Hipóteses validadas vs. implementadas:** Meta: 50%+. Se o PM valida mas não implementa, algo está errado na priorização.
- **Tempo médio de ciclo de validação:** Meta: menos de 2 semanas. Se demora mais, o processo está emperrado.
- **Custo por experimento:** Meta: redução de 30% ao longo do trimestre. Se o custo não cai, o time não está aprendendo.

### Métricas para o Sintetizador (Híbrido)

- **Tempo médio de decisão:** Meta: menos de 3 dias úteis. Se demora mais, o processo de síntese está quebrado.
- **Taxa de decisões que geram impacto positivo mensurável:** Meta: 70%+. Se abaixo, o time está tomando decisões erradas.
- **Número de decisões revertidas:** Meta: menos de 10%. Se o time nunca reverte decisões, está com medo de errar. Se reverte demais, está tomando decisões precipitadas.

### Métricas de Resultado Final

- **NPS do produto com IA:** Se NPS não melhorar, nada mais importa.
- **Taxa de resolução na primeira interação:** Medida de eficácia real, não de performance técnica.
- **Percentual de usuários pedindo humano:** Se sobe, seu time híbrido está falhando.
- **NPS do time:** O time está mais engajado? Se o NPS do time cair, algo está errado.

### Métricas que não importam (sozinhas):
- Accuracy do modelo
- Precisão e recall
- Tempo de inferência
- Número de features implementadas

---

## Seção 7: Fechamento com Gancho

Se você chegou até aqui, já sabe que o time de produto com IA não é um time de produto tradicional com uma ferramenta nova. É um time com uma estrutura nova, papéis novos e métricas novas.

O que ainda não respondemos: como esse time decide o que construir? Com 47 hipóteses por semana, como não enlouquecer? Se o THA gera 47 hipóteses por semana, como priorizar sem cair no caos? Essa é a pergunta que o Capítulo 9 responde.

Mas antes, precisamos de uma pausa. Respira. O próximo capítulo é sobre métricas. E não, não é sobre accuracy.

---

# Capítulo 6: O PM na Era dos Agentes: o que muda, o que some, o que nasce

---

## Seção 1: Cena de Abertura

Era uma terça-feira de março de 2025, e Rafael Almeida, Product Manager de um banco digital, estava sentado na sala de retrospectiva semanal. O time tinha 8 humanos e 2 agentes de IA. Um para QA, outro para análise de dados. Na parede, o quadro de post-its mostrava 12 itens concluídos e 3 bugs abertos.

"O que podemos melhorar?", Rafael perguntou, como fazia toda semana.

Um engenheiro levantou a mão. "O agente de QA encontrou 3 bugs. Nenhum humano viu. Mas ele sugeriu features sem sentido para o usuário. Sugeriu um chatbot para agendamento de reuniões. A gente nem tem reunião com cliente nesse fluxo."

Silêncio.

Outro engenheiro completou: "O agente de dados gerou um relatório de churn que o time de marketing amou. Mas quando fui ver, ele usou dados de 2023, não de 2025. O modelo não sabia que a gente mudou a política de tarifas."

Rafael olhou para o quadro. Dois agentes trabalhando. Resultados mistos. Bugs encontrados. Sugestões sem contexto. E ele, o PM, sem saber quem prioriza o que o agente sugere. Quem valida. Quem decide quando o agente erra.

O banco digital tinha saído de um satisfação de 1.8 para 4.2 em dois anos. Mas a dinâmica do time tinha mudado mais rápido do que a gestão conseguia acompanhar.

Segundo a Stack Overflow Developer Survey 2025, 84% dos desenvolvedores usam ferramentas de IA no desenvolvimento (Stack Overflow, 2025). Pesquisa exploratória não publicada com 47 times de produto em empresas brasileiras (2024-2025) sugere que menos de 15% dos times têm papéis claros para agentes. Esse dado carece de validação estatística independente e é apresentado como observação da autora.

Rafael não sabia, mas ele estava vivendo o problema central deste capítulo: se agentes podem sugerir features, testar código e analisar dados, qual o papel do humano? E do PM?

---

## Seção 2: Definição do Problema

"O que acontece quando metade do seu time não é humano?"

Essa pergunta parece futurista, mas já é realidade. Times de produto estão cada vez mais híbridos. Humanos e agentes de IA trabalham lado a lado. O problema não é "como contratar mais pessoas de IA". É "como redesenhar o time quando metade dos membros não são humanos".

**O mito do time aumentado.** Muitas empresas acham que basta adicionar um data scientist ou comprar uma ferramenta de IA. O resultado é o caos de papéis: quem decide o que o agente faz? Quem valida as sugestões? Quem responde quando humano e agente discordam?

O framework Product Trio (PM + Designer + Engenheiro) funciona bem quando todos são humanos. Mas quando um agente entra no time, o trio vira quarteto. E o quarteto precisa de regras.

**Os 3 erros comuns na montagem de times híbridos:**

1. **Tratar agente como ferramenta.** Agente não é calculadora. Ele sugere, analisa, decide. Se você trata como ferramenta, perde o potencial. Mas se trata como humano sem papéis, vira bagunça.

2. **Não definir critérios de julgamento para quando humano e agente discordam.** O agente diz uma coisa, o humano diz outra. Quem ganha? Depende. Mas se não está definido, o time trava.

3. **Manter métricas tradicionais que não capturam a dinâmica humano-agente.** Velocidade de entrega, número de features. Essas métricas não dizem se o agente está ajudando ou atrapalhando.

No capítulo anterior, vimos que métricas tradicionais não funcionam para IA. Agora vamos ver que times tradicionais também não funcionam.

O que este capítulo resolve: um framework para redesenhar times de produto na era dos agentes, com papéis claros, princípios de decisão e métricas específicas.

---

## Seção 3: O que o PM PARA de fazer

Antes de falar do que o PM *vira*, precisamos falar do que ele *deixa de ser*. Porque a parte mais difícil da transformação não é aprender o novo, é largar o velho.

Aqui está o que some do seu dia a dia:

**1. Microgerenciar tarefas repetitivas.** O agente escreve o primeiro draft do PRD. O agente compila as métricas do sprint. O agente documenta as decisões da reunião. Seu trabalho não é fazer, é revisar o que o agente fez e decidir se está bom. Você para de ser produtor e vira curador.

**2. Ser o único validador de output.** Antes, toda feature passava pelo PM antes de ir pra produção. Agora, o agente valida critérios objetivos (testes passam? métricas dentro do range?) e só escala pro PM quando há ambiguidade. Você para de ser gargalo e vira exceção.

**3. Priorizar sozinho com intuição pura.** O agente sugere priorização baseada em dados (impacto estimado, esforço, risco, dependências). Você ainda decide, mas com o agente mostrando o que os dados dizem. Você para de decidir no escuro e vira decisor informado.

**4. Descobrir problemas sozinho.** O agente monitora métricas 24/7, detecta anomalias, sugere hipóteses. Você não precisa mais "descobrir" que o NPS caiu, o agente te avisa. Você para de ser detetive e vira investigador sênior (o agente acha a cena do crime; você resolve o caso).

**5. Escrever tudo do zero.** PRDs, briefings, relatórios de status, e-mails de alinhamento. O agente gera o primeiro draft. Você edita. Seu tempo de escrita despenca. Você para de ser redator e vira editor.

Se você se reconheceu em 3 ou mais desses itens: seu trabalho já mudou. Você só não percebeu ainda.

---

## Seção 4: PM Brain OS, seu sistema operacional de produto

O PM Brain OS é o que substitui o HAT Model operacional. Pense nele como o sistema operacional que roda na sua cabeça (e na do agente). Três componentes:

### Kernel: as regras que NUNCA mudam

O kernel é o que o agente NÃO decide. São regras invioláveis que você define uma vez e recalibra a cada trimestre:

- **Visão é humana.** O agente executa. O "porquê" é sempre humano.
- **Trade-offs de usuário são humanos.** Se a decisão afeta a experiência de um cliente, um humano decide.
- **Risco é escalado.** Se o agente detecta que uma decisão tem potencial de gerar dano (financeiro, reputacional, legal), ele NÃO decide. Escala.

### Regras de autonomia: os 5 níveis de liberdade do agente

| Nível | Nome | O agente... | Exemplo |
|-------|------|-------------|---------|
| **L0** | Observador | Só coleta dados, não age | Monitora NPS, alerta se cair |
| **L1** | Sugestor | Propõe ação, humano aprova | "Recomendo responder cliente X com template Y" |
| **L2** | Executor com validação | Age, humano revisa depois | Responde cliente, PM vê relatório semanal |
| **L3** | Executor autônomo | Age, reporta se anomalia | Responde cliente, só alerta se detecta raiva |
| **L4** | Decisor delegado | Decide dentro de política, escala exceções | Define desconto até R$ 50, acima disso escala |

Cada agente do seu time opera em um nível diferente. O agente de suporte pode estar em L3. O agente de pricing, em L1. Você define.

### Memória compartilhada: o que o agente precisa saber

Sem contexto, o agente é só um modelo de linguagem. Com contexto, ele é um teammate. A memória compartilhada tem 4 camadas:

- **Contexto de produto:** visão, OKRs do trimestre, personas, jornadas críticas
- **Contexto de decisão:** as últimas 10 decisões que você tomou e por quê
- **Contexto de time:** quem é responsável por quê, férias, capacidade do sprint
- **Contexto de cliente:** feedback recente, tickets abertos, NPS por segmento

Isso não é um documento, é um sistema. No Capítulo 8, você vai ver como operacionalizar essa memória compartilhada com rituais e ferramentas. Por enquanto, entenda o conceito: o agente é tão bom quanto o contexto que você dá pra ele.

---

## Seção 5: HAT Model, os papéis que operacionalizam o PM Brain OS

Com o sistema operacional definido, o HAT Model (Human-Agent Team) organiza quem faz o quê.

"Como estruturar um time onde humanos e agentes têm papéis complementares, não concorrentes?"

A resposta é o **HAT Model (Human-Agent Team Model)** . HAT significa Human-Agent Team. São cinco papéis que todo time híbrido precisa ter, independentemente do tamanho.

### Os 5 papéis do HAT Model

**Papel 1: Strategist**

*Quem faz:* Humano (PM).

*O que faz:* Define o "porquê" e o "para quem". Não delega visão. O agente pode sugerir, mas não decide o rumo.

*Exemplo do case:* Rafael, PM de um banco digital, decidiu que o agente de dados não podia definir quais métricas eram prioritárias. Ele definia. O agente executava.

*A aposta:* Se o agente decide a visão, você perde o controle estratégico. O PM é o guardião da visão.

**Papel 2: Executor**

*Quem faz:* Agente (IA).

*O que faz:* Executa tarefas repetitivas, analisa dados, gera variações. Onde o humano perde tempo, o agente ganha.

*Exemplo do case:* Agente de QA que encontrou 3 bugs. Trabalho que levaria 2 dias para um humano, o agente fez em 20 minutos.

*Por que isso muda o jogo:* O agente libera o humano para o que importa. Mas só funciona se o Executor tem limites claros.

**Papel 3: Validator**

*Quem faz:* Humano (Designer ou Engenheiro).

*O que faz:* Valida outputs do agente antes de ir para produção. O agente sugere. O humano aprova ou rejeita.

*Exemplo do case:* Designer do banco digital que revisou recomendações do agente e encontrou 2 sugestões que violavam a identidade visual da marca. Uma sugeria usar vermelho no botão de cancelamento. Outra recomendava um produto que o cliente já tinha.

*O custo de errar:* Sem validação, o agente erra. E quando erra, erra em escala.

**Papel 4: Escalator**

*Quem faz:* Humano (PM ou Engenheiro).

*O que faz:* Decide quando o agente não resolve e o humano entra. O agente tem um limite de autonomia. Quando atinge, sobe para o humano.

*Exemplo do case:* Motorista da startup de mobilidade que ignorou rota sugerida pelo agente porque sabia que a rua estava em obras.

*Por que importa:* Nem tudo pode ser automatizado. O Escalator é o ponto de falha seguro.

**Papel 5: Learner**

*Quem faz:* Ambos (humano e agente).

*O que faz:* Ciclo de feedback contínuo. Agente aprende com humano. Humano aprende com agente.

*Exemplo do case:* Sistema de feedback do banco digital que permitia ao humano marcar sugestões do agente como "úteis" ou "inúteis". Em 3 meses, a precisão do agente subiu 40%.

*O ponto:* Time híbrido que não aprende junto é time que estagna.

### Os 3 princípios de funcionamento do HAT Model

1. **Clareza de domínio.** Cada papel sabe exatamente o que pode e o que não pode fazer. O agente não sugere features sem validação do Strategist. O humano não microgerencia tarefas do Executor.

2. **Autonomia progressiva.** O agente começa com pouca autonomia. Conforme mostra resultados, ganha mais. Mas nunca sem supervisão.

3. **Feedback bidirecional.** O humano ensina o agente. O agente ensina o humano. Não é via de mão única.

O HAT Model não é teoria abstrata. É conhecimento prático baseado em implementações reais. E funciona.

---

## Seção 4: Casos e exemplos

### Caso 1: Banco Digital, satisfação de 1.8 para 4.2

**Situação Inicial.** Banco digital brasileiro com 5 milhões de clientes. Time de produto com 12 pessoas. satisfação de 1.8. Reclamações constantes sobre tempo de resposta e qualidade das recomendações.

**O que estava errado.** O time tratava IA como ferramenta. Tinham um modelo de recomendação, mas ninguém validava as sugestões. O modelo recomendava produtos que o cliente já tinha. Resultado: taxa de cancelamento alta.

**Como resolveu.** Implementaram o HAT Model. PM virou Strategist. Agente virou Executor. Designer virou Validator. Em 2 semanas, o time tinha papéis claros. Em 3 meses, o satisfação subiu para 3.4. Em 6 meses, para 4.2.

**Resultados.** satisfação de 1.8 para 4.2 em 6 meses (dado ilustrativo baseado em observação da autora). Redução de 45% no tempo de resposta (dado ilustrativo). Aumento de 30% na taxa de conversão de recomendações (dado ilustrativo).

### Caso 2: E-commerce, Time focado em métricas técnicas

**Situação Inicial.** E-commerce com aproximadamente 2 milhões de pedidos por mês (dado ilustrativo). Time de produto com 8 humanos e 1 agente de IA para recomendações. Métricas: precisão do modelo, recall, F1-score. Todas técnicas.

**O que estava errado.** O time otimizava para métricas técnicas, não para resultados de negócio. O modelo tinha alta precisão (dado ilustrativo), mas as recomendações não geravam vendas. Por quê? Porque o modelo ignorava contexto do usuário (hora do dia, dispositivo, histórico recente).

**Como resolveu.** Redesenharam o time com HAT Model. PM definiu métricas de negócio (taxa de conversão, receita por recomendação). Designer validou sugestões do agente. Engenheiro criou ciclo de feedback para o agente aprender com rejeições.

**Resultados.** Taxa de conversão de recomendações subiu 25% em 2 meses (dado ilustrativo). Receita por recomendação aumentou 18% (dado ilustrativo). O time parou de otimizar para métricas técnicas e passou a otimizar para o que importava.

### Caso 3: Startup de Mobilidade, Rotas em tempo real

**Situação Inicial.** Startup de mobilidade com 500 mil motoristas. Time de produto com 15 pessoas. Agente de IA sugeria rotas em tempo real. Motoristas ignoravam 40% das sugestões.

**O que estava errado.** O agente não considerava variáveis que o motorista conhecia: trânsito local, obras, preferências do cliente. O motorista sabia mais, mas o sistema não ouvia.

**Como resolveu.** Criaram o papel de Escalator. Motorista podia ignorar a rota sugerida e explicar por quê. O feedback alimentava o Learner. Em 3 meses, a taxa de aceitação de rotas subiu de 60% para 85%.

**Resultados.** Taxa de aceitação de 60% para 85% em 3 meses (dado ilustrativo). Redução de 12% no tempo médio de viagem (dado ilustrativo). Motoristas mais satisfeitos (satisfação de motorista subiu de 2.8 para 3.9, dado ilustrativo).

---

## Seção 5: Guia Prático

"Bora colocar a mão na massa. Aqui está o plano 30/60/90 dias para redesenhar seu time híbrido."

### Dias 1-7: Mapeie o cenário atual

- **Mapeie seu time atual.** Liste todos os humanos e agentes envolvidos. Para cada agente, responda: o que ele faz? Quem valida? Quem decide quando ele erra?
- **Identifique o caos de papéis.** Pergunte para cada membro do time: "Você sabe exatamente o que pode e o que não pode fazer?" Se a resposta for "mais ou menos", você tem um problema.
- **Defina o Strategist.** Quem é o PM ou líder que define a visão? Se não tiver, defina. Esse papel não pode ser delegado ao agente.

### Dias 8-30: Implemente os papéis do HAT Model

- **Atribua os 5 papéis.** Para cada agente, defina quem é o Executor, o Validator, o Escalator e o Learner. Documente em um quadro visível para todo o time.
- **Estabeleça critérios de julgamento para discordâncias.** Crie uma matriz de decisão: quando humano e agente discordam, quem decide? Exemplo: se a sugestão do agente impacta a experiência do usuário, o Designer decide. Se impacta a arquitetura técnica, o Engenheiro decide.
- **Crie o ciclo de feedback inicial.** Implemente um sistema simples: botão de "útil" e "inútil" para cada sugestão do agente. Nada complexo. Só comece.

### Dias 31-60: Estabeleça o ciclo de aprendizado

- **Meça os primeiros resultados.** Use as métricas do AI Team Health Score (veja seção 6). Foco em taxa de aceitação de sugestões e tempo de validação.
- **Ajuste a autonomia do agente.** Se o agente mostra consistência, aumente a autonomia. Se erra, reduza. O princípio é progressivo, não binário.
- **Treine o time.** Todo mundo precisa entender os novos papéis. Não adianta só definir. Tem que ensinar. Faça uma sessão de 1 hora por semana para alinhar.

### Dias 61-90: Escale e refine

- **Revise a autonomia progressiva.** O agente ganhou mais autonomia nos últimos 3 meses? Se não, o modelo não está escalando. Ajuste.
- **Documente o modelo.** O que funcionou? O que não funcionou? Crie um playbook para o próximo time. Inclua exemplos de discordâncias e como foram resolvidas.
- **Compartilhe com outros times.** O HAT Model não é segredo. Quanto mais times usarem, mais aprendizado coletivo.

O guia é concreto. Não é "monte um time de IA". É "aqui estão os passos exatos". Faça.

---

## Seção 6: Métricas de Sucesso

"Se métricas tradicionais não funcionam, o que colocar no lugar?"

A resposta é o **AI Team Health Score**. Três dimensões. Nove métricas.

### Dimensão 1: Valor para o Usuário

- **Taxa de aceitação de sugestões do agente.** Quantas vezes o usuário aceita o que o agente sugere? Acima de 70% é saudável. Abaixo de 40%, o agente não está ajudando.
- **Tempo de validação humana.** Quanto tempo o humano leva para validar ou rejeitar uma sugestão do agente? Idealmente, menos de 2 horas. Se passa de 24 horas, o gargalo não é o agente, é o processo.
- **Satisfação do usuário (NPS/Csat).** O usuário sente diferença? Pergunte. Se o NPS cai depois de implementar o agente, algo está errado.

### Dimensão 2: Valor para o Negócio

- **ROI do time híbrido.** Quanto o agente economiza ou gera de receita? Divida pelo custo do agente (infraestrutura, manutenção, treinamento). Um ROI acima de 3x em 6 meses é saudável.
- **Velocidade de entrega.** O time está entregando mais rápido com o agente? Meça em dias ou semanas. Redução de 30% no tempo de entrega é um bom alvo.
- **Taxa de erros em escala.** O agente está errando menos que o humano? Compare a taxa de erros antes e depois. Se o agente erra mais, o custo pode superar o benefício.

### Dimensão 3: Qualidade de Implementação

- **Clareza de papéis.** Pergunte para o time: "Você sabe exatamente o que pode fazer?" Se menos de 80% responder "sim", você tem problema de comunicação.
- **Ciclo de feedback ativo.** O agente está aprendendo? Meça número de feedbacks por semana. Menos de 5 por semana por agente indica que o ciclo não está funcionando.
- **Autonomia progressiva.** O agente ganhou mais autonomia nos últimos 3 meses? Se não, o modelo não está escalando. A autonomia deve subir gradualmente.

O AI Team Health Score não é teoria. É ferramenta de gestão. Use.

---

## Seção 7: Fechamento com Gancho

O time de produto na era dos agentes não é sobre contratar mais pessoas ou mais máquinas. É sobre redesenhar quem faz o quê, com que autonomia e com que critérios de julgamento.

O PM não desaparece. Ele se torna o arquiteto de um sistema híbrido onde humanos e agentes têm papéis complementares, não concorrentes.

O HAT Model resolve o problema de papéis. O AI Team Health Score resolve o problema de métricas. Mas tem uma pergunta que fica no ar.

"Como montar times de IA quando os melhores data scientists querem startups, não corporações?"

O guia 30/60/90 dias mostra como começar. Mas escalar depende de atrair talento raro. E talento raro não aparece com salário competitivo. Aparece com propósito, autonomia e impacto.

No próximo capítulo, vamos explorar como competir por esse talento. Como montar times que atraem os melhores. E como mantê-los quando o mercado quer levá-los embora. O HAT Model é o começo, não o fim. A estrutura de papéis que você estabeleceu agora precisa de pessoas para preencher os papéis humanos. E essas pessoas são cada vez mais escassas.

Mas antes, uma pergunta para você levar para o seu time: "Se amanhã seu agente de IA sugerir uma feature que você não pediu, quem decide se ela vai para o backlog?"

Se você não sabe a resposta, seu time híbrido está quebrado. E agora você sabe como consertar.

---

# PARTE IV: OPERAÇÃO. Como fazer rodar?

> *Time redesenhado, decisão tomada. Rituais, governança, cultura e ética.*

# Capítulo 7: O Operating System: rituais, decisões e governança

### 1. Cena de Abertura

Era uma quinta-feira de janeiro de 2024, e o head de produto do Banco Digital Brasileiro projetou o dashboard na sala de retrospectiva. O silêncio durou 10 segundos. O time inteiro olhava para o número: satisfação de 1.8.

Isso não era erro de cálculo. O chatbot de atendimento tinha 92% de accuracy técnica. O modelo classificava corretamente intenções, resolvia problemas simples, respondia perguntas frequentes com precisão quase humana. No papel, era um sucesso. Na prática, 89% dos usuários pediam para falar com um humano nos primeiros 30 segundos de interação.

"Mas o modelo tá certo", disse o ML engineer, confuso.

"O modelo tá certo e o usuário tá infeliz", respondeu a PM. "Isso não é um problema técnico. É um problema de governança."

Se você já lançou uma feature de IA que funcionava mas ninguém usava, você conhece essa sala. O modelo perfeito que o usuário odeia não é paradoxo. É sintoma de governança ausente. Accuracy, precision, recall são métricas de modelo. Não são métricas de produto.

O time do Banco Digital Brasileiro tinha o melhor modelo de atendimento do mercado. E estava destruindo a experiência do cliente.

---

### 2. Definição do Problema

"Fernanda, como garantimos que nossa estratégia de IA não seja apenas mais uma iniciativa de tecnologia?"

Essa pergunta me foi feita por um VP de Produto de um grande banco brasileiro, numa quarta-feira de março de 2025. Ele tinha razão. O time dele tinha implementado IA em três frentes diferentes: chatbot, recomendação de produtos, análise de crédito. As métricas técnicas eram boas. A satisfação do cliente? Em queda.

O erro dele é comum entre times que implementam IA: eles mantêm os mesmos rituais de antes e esperam resultados diferentes.

O *Operating System* de um time de produto com IA não é sobre tecnologia. É sobre rituais de decisão. É sobre o conjunto de práticas que define como um time opera no dia a dia: como observa, como agenda, como escala, como revisa, como itera.

O problema central: times implementam IA sem repensar seus rituais de governança. O chatbot decide sozinho? Quando escala para um humano? Quem revisa as decisões do modelo? Com que frequência? O que acontece quando o modelo erra?

Sem um *Operating System*, a IA vira uma caixa-preta que ninguém entende e ninguém controla. O time fica refém das métricas técnicas que escondem problemas de experiência.

**Conexão com o Capítulo 6:** O framework de oportunidades mapeia ideias de IA em quatro etapas: Mapear, Priorizar, Validar, Escalar. Cada etapa encontra um correspondente no OS Framework. Ele responde "o que construir". O OS responde "como operar". A etapa **Mapear** identifica onde a IA pode gerar valor. O OS entra com o ritual **Observe (O1)** para monitorar se esse valor está realmente sendo entregue. A etapa **Priorizar** define o que fazer primeiro. O OS entra com **Schedule (O2)** para garantir rituais fixos de revisão. A etapa **Validar** testa a solução com usuários. O OS entra com **Review (O4)** para revisar casos-limite e falhas. A etapa **Escalar** expande a solução. O OS entra com **Iterate (O5)** para garantir melhoria contínua.

O *AI Maturity Model* do Gartner (publicado originalmente em 2023) continua sendo o framework de referência para avaliar maturidade organizacional em IA. Embora não tenha sido atualizado formalmente, seus 5 níveis seguem sendo adotados por consultorias e times de produto como padrão de diagnóstico. Times nos níveis 1-2 não deveriam introduzir agentes autônomos. Só times nos níveis 3-5 têm a governança necessária para não criar o cenário do Banco Digital: modelo perfeito, experiência horrível.

---

### 3. Framework / Componentes

**OS Framework: 5 Rituais de Decisão para Times com IA**

O acrônimo é OS, de *Operating System*. Observe, Schedule, Escalate, Review, Iterate.

| Componente | Nome | Descrição | Pergunta-guia |
|------------|------|-----------|---------------|
| O1 | Observe | Monitoramento de agentes com foco em experiência, não métricas técnicas | "O usuário está feliz ou o modelo está certo?" |
| O2 | Schedule | Rituais fixos de revisão de decisões dos agentes | "Com que frequência revisamos o que o agente decidiu?" |
| O3 | Escalate | Caminho claro para escalação de decisões críticas para humanos | "Quando o agente pede ajuda e quando decide sozinho?" |
| O4 | Review | Revisão periódica de casos-limite e falhas do agente | "O que o agente fez de errado esta semana que ninguém percebeu?" |
| O5 | Iterate | Ciclo de melhoria contínua baseado em feedback humano | "Como o agente aprende com os erros sem repeti-los?" |

---

**O1: Observe. A métrica certa não é accuracy, é satisfação**

O time do Banco Digital Brasileiro monitorava accuracy, precision e recall. Todas verdes. O satisfação de 1.8 era invisível porque eles não olhavam para a métrica certa.

**A métrica de modelo mede o quão bem a IA executa a tarefa. A métrica de produto mede se a tarefa importa para o usuário.**

O erro é confundir as duas. Accuracy de 92% significa que o modelo classifica intenções corretamente em 92% dos casos. Não significa que o usuário está satisfeito. Não significa que o problema foi resolvido. Não significa que o usuário não prefere falar com um humano.

No caso do Banco Digital Brasileiro, 89% dos usuários pediam para falar com um humano nos primeiros 30 segundos de interação. Esse dado, documentado internamente pelo time de produto, revelava um problema de governança, não de modelo.

**Ferramenta: *Human Agency Scale***

A *Human Agency Scale* mede o nível de autonomia do agente em relação à satisfação do usuário. São 5 níveis:

| Nível | Nome | Descrição | Quando usar |
|-------|------|-----------|-------------|
| 1 | Humano decide sozinho | IA não toma decisão | Problemas complexos, alto risco, baixa maturidade |
| 2 | IA sugere, humano decide | IA recomenda, humano aprova | Decisões de médio risco, aprendizado inicial |
| 3 | IA decide, humano revisa | IA age, humano revisa depois | Decisões de baixo risco, alta confiança |
| 4 | IA decide, humano audita | IA age, humano audita periodicamente | Decisões rotineiras, baixo risco |
| 5 | IA decide sozinha | IA age sem intervenção | Decisões simples, risco mínimo, alta maturidade |

O erro do Banco Digital: eles colocaram o chatbot no nível 5 (IA decide sozinha) quando a maturidade do time e a complexidade do problema exigiam nível 2 ou 3.

**Dica prática:** Se você só olha dashboards de modelo, você está cego para a experiência. Crie um dashboard duplo: métricas de modelo (accuracy, precision, recall) lado a lado com métricas de experiência (NPS, Csat, taxa de escalação para humano). Se houver divergência, o problema é de governança, não de tecnologia.

---

**O2: Schedule. Rituais fixos de revisão**

O agente não participa de reuniões. Mas suas decisões precisam ser revisadas. O Schedule define a frequência e o formato dessa revisão.

**Rituais recomendados:**

| Ritual | Duração | Frequência | O que revisar |
|--------|---------|------------|---------------|
| Daily do agente | 5 min | Diário | Decisões anômalas, escalações pendentes |
| Weekly review | 30 min | Semanal | Top 10 erros, feedback de usuários |
| Monthly análise | 2h | Mensal | Análise de tendências, revisão de métricas |
| Quarterly audit | 4h | Trimestral | Revisão de casos-limite, alinhamento com estratégia |

**Exemplo real:** O time de produto de um grande e-commerce brasileiro revisa semanalmente as recomendações de produtos rejeitadas pelos usuários. Cada rejeição é um dado. Cada padrão de rejeição é uma oportunidade de melhoria. Eles não esperam o usuário reclamar. Eles monitoram o comportamento do usuário em relação ao agente. Esse caso ilustrativo mostra como o Schedule transforma monitoramento reativo em governança proativa.

**O risco:** Sem Schedule, o time só descobre problemas quando o usuário reclama. Ou pior: quando o agente causa um dano irreversível. O Schedule transforma monitoramento reativo em governança proativa.

---

**O3: Escalate. Quando o agente pede ajuda**

A escalação não é falha. É feature. Um agente que nunca escala está tomando decisões que não deveria. Um agente que escala demais está sendo inútil.

**Matriz de Decisão de Escalação:**

| Complexidade | Risco | Exemplo | Ação do agente |
|--------------|-------|---------|----------------|
| Baixa | Baixo | "Qual o saldo?" | Decide sozinho |
| Média | Baixo | "Como faço um Pix?" | Decide, oferece ajuda |
| Alta | Baixo | "Como invisto?" | Sugere, escala se dúvida |
| Baixa | Alto | "Quero cancelar" | Escala para humano |
| Alta | Alto | "Perdi acesso à conta" | Escala imediatamente |

**Case Banco Digital:** O chatbot escalava apenas 11% dos casos. O time descobriu que 89% dos usuários pediam para falar com humano porque o chatbot não escalava nos momentos certos. O usuário ficava preso num loop de respostas automáticas que não resolviam o problema real.

**Regra prática:** Se mais de 30% dos usuários pedem para falar com humano, seu agente está escalando pouco. Se menos de 5%, talvez você nem precise do agente.

---

**O4: Review. Caça aos casos-limite**

Casos-limite são o ponto cego de todo agente de IA. O modelo foi treinado com dados comuns. O problema está nos dados raros que ninguém previu.

**Como fazer Review:**

1. **Semanal:** Selecione os 10 casos com menor confiança do modelo. Analise manualmente.
2. **Mensal:** Analise todos os casos que foram escalados para humanos. Identifique padrões.
3. **Trimestral:** Busque casos que o modelo tratou como "normais" mas que na verdade eram exceções.

**Exemplo:** Um chatbot de banco tratava "quero fechar minha conta" como uma solicitação de informação sobre fechamento de conta. O modelo classificava corretamente a intenção (fechamento de conta). Mas o usuário queria fechar a conta. O chatbot respondia com "Para fechar sua conta, acesse o menu X". O usuário ficava frustrado. O modelo estava tecnicamente correto. A experiência era terrível.

**O que o Review revelou:** O modelo não distinguia entre "quero informação sobre fechamento" e "quero fechar agora". Dois intents diferentes que o modelo tratava como um só. O caso-limite era a urgência, não a intenção.

---

**O5: Iterate. Aprendendo com os erros**

O ciclo de melhoria contínua baseado em feedback humano é o que separa um agente que estagna de um agente que evolui.

**Ciclo de Iteração:**

1. **Coletar:** Feedback explícito (avaliação do usuário) e implícito (comportamento)
2. **Analisar:** Identificar padrões de erro
3. **Priorizar:** Qual erro causa mais dano à experiência?
4. **Corrigir:** Ajustar modelo, regras ou governança
5. **Validar:** O erro diminuiu? A satisfação melhorou?

**Exemplo completo: E-commerce brasileiro com recomendação de produtos**

Um grande e-commerce brasileiro (caso ilustrativo) enfrentava o problema: o algoritmo de recomendação otimizava taxa de clique com alta precisão técnica. Mas os usuários reclamavam de recomendações repetitivas e irrelevantes.

O time aplicou o ciclo de iteração:

1. **Coletar:** Feedback implícito (usuários clicavam em recomendações mas não compravam) e explícito (avaliação de satisfação com recomendação)
2. **Analisar:** Identificaram que o modelo ignorava contexto temporal (recomendava almoço para jantar), histórico recente (repetia recomendações vistas), e variedade (sempre os mesmos produtos)
3. **Priorizar:** O erro mais danoso era a repetição: usuários desistiam de explorar porque viam sempre os mesmos itens
4. **Corrigir:** Adicionaram contexto temporal (recomendação de almoço vs. jantar vs. lanche), implementaram "surpresa" (10% das recomendações aleatórias para explorar), mudaram métrica de otimização de CTR para NPS de recomendação
5. **Validar:** NPS de recomendação subiu 18 pontos. Usuários relataram "descoberta" de novos produtos. Ticket médio aumentou 7%. (caso ilustrativo)

**A armadilha:** Times que iteram apenas com base em métricas técnicas (accuracy subiu 2%) mas ignoram métricas de experiência (NPS caiu 0.5). O ciclo de iteração precisa incluir ambos.

---

### 4. Casos e exemplos

**Caso 1: Banco Digital Brasileiro. Do satisfação 1.8 ao 4.2**

**Situação Inicial:** Chatbot com 92% de accuracy técnica. satisfação de 1.8. 89% dos usuários pediam para falar com humano nos primeiros 30 segundos.

**O que estava errado:**
- Agente operava no nível 5 (autonomia total) quando deveria estar no nível 2
- Métricas monitoradas eram só técnicas (accuracy, precision)
- Escalação era mínima (11% dos casos)
- Time não revisava casos-limite

**Como resolveu:**
- Aplicou a *Human Agency Scale*: reduziu autonomia do agente para nível 2 (sugere, humano decide)
- Criou dashboard duplo: métricas de modelo + métricas de experiência
- Implementou Schedule: daily do agente (5 min), weekly review (30 min)
- Aumentou taxa de escalação para 40% nos casos complexos
- Iniciou ciclo de iteração semanal baseado em feedback de usuários

**Resultados:** Em 90 dias, o satisfação subiu de 1.8 para 4.2. A taxa de usuários que pediam para falar com humano caiu de 89% para 34%. O tempo médio de resolução caiu de 12 minutos para 4 minutos. (caso ilustrativo)

---

**Caso 2: Banco digital. Governança de crédito com IA**

**Situação Inicial:** Time de crédito usando IA para aprovação de limites. Modelo com 95% de precisão na previsão de inadimplência. Mas clientes reclamavam de limites injustos.

**O que estava errado:**
- Modelo era uma caixa-preta: ninguém entendia por que um cliente tinha limite alto e outro baixo
- Não havia revisão humana de casos-limite
- Clientes com score baixo não tinham recurso

**Como resolveu:**
- Implementou *Explainable AI*: cada decisão de limite vinha com explicação em linguagem natural
- Criou processo de recurso humano para casos excepcionais
- Revisão trimestral de casos-limite (clientes com score baixo mas bom comportamento)

**Resultados:** Redução de 40% nas reclamações de limite. Clientes com recurso aprovado tinham 12% menos inadimplência que a média. (caso ilustrativo)

---

**Caso 3: App de delivery. Recomendação com contexto humano**

**Situação Inicial:** Algoritmo de recomendação que otimizava taxa de clique. Alta accuracy. Usuários reclamavam de recomendações repetitivas.

**O que estava errado:**
- Modelo otimizava clique, não satisfação
- Não considerava contexto: horário, humor, histórico recente
- Recomendações eram sempre as mesmas para o mesmo horário

**Como resolveu:**
- Mudou métrica de otimização de CTR para NPS de recomendação
- Adicionou contexto temporal: recomendação de almoço vs. jantar vs. lanche
- Implementou "surpresa": 10% das recomendações eram aleatórias para explorar novos restaurantes

**Resultados:** NPS de recomendação subiu 18 pontos. Usuários relataram "descoberta" de novos restaurantes. Ticket médio aumentou 7%. (caso ilustrativo)

---

### 5. Guia Prático: 30/60/90 dias

**Implementação do OS Framework em 90 dias**

**Primeiros 30 dias (Mês 1: Fundação)**

- [ ] Mapeie todos os agentes de IA do seu time. Liste nome, função, nível atual de autonomia.
- [ ] Para cada agente, aplique a *Human Agency Scale*. Identifique qual nível é adequado.
- [ ] Crie dashboard duplo: métricas de modelo (accuracy, precision, recall) + métricas de experiência (NPS, Csat, taxa de escalação).
- [ ] Escolha um agente prioritário: o que mais impacta a experiência do usuário.
- [ ] Defina regras de escalação básicas: quando o agente decide sozinho, quando pede ajuda.
- [ ] Configure o daily do agente (5 min) para revisar decisões anômalas.

**Próximos 30 dias (Mês 2: Ritualização)**

- [ ] Implemente Schedule completo: daily (5 min), weekly review (30 min), monthly análise (2h).
- [ ] Inicie weekly review: analise top 10 erros da semana. Documente padrões.
- [ ] Colete feedback explícito dos usuários: avaliação após cada interação com o agente.
- [ ] Ajuste a *Human Agency Scale* com base nos primeiros resultados.
- [ ] Treine o time: PM, engenheiros, designers precisam entender o OS.

**Próximos 30 dias (Mês 3: Iteração e Escala)**

- [ ] Complete o primeiro ciclo de Iterate: coletar, analisar, priorizar, corrigir, validar.
- [ ] Repita o processo para todos os agentes do time.
- [ ] Faça o primeiro quarterly audit: revisão de casos-limite, alinhamento com estratégia.
- [ ] Documente lições aprendidas e compartilhe com o time.
- [ ] Ajuste métricas de sucesso com base nos resultados reais.

**Ações concretas para líderes:**

- Não delegue governança de IA para o time técnico. É responsabilidade do PM.
- Seu time está no nível 1-2 do *AI Product Maturity Model* (Gartner)? Não introduza agentes autônomos. Comece com nível 1-2 de autonomia na *Human Agency Scale*.
- A métrica mais importante do seu agente não é accuracy. É "o usuário pediu para falar com humano?"

---

### 6. Métricas de Sucesso

Com base na experiência da autora em mais de 20 implementações de IA em produtos digitais, dois indicadores se destacam: taxa de escalação para humano abaixo de 30% (indicando que o agente resolve a maioria dos casos sem intervenção) e satisfação acima de 4.0 (indicando que a experiência com o agente é positiva). Abaixo disso, o *Operating System* precisa ser revisado.

**Valor para Usuário**

- **Satisfação do agente:** Mede a experiência do usuário com a interação. Meta: acima de 4,0.
- **Taxa de escalação para humano:** Quanto menor, melhor. Mas não zero. Meta: entre 10% e 30%.
- **Tempo médio de resolução:** Tempo até o problema ser resolvido. Meta: redução de 40% em 90 dias.

**Valor para Negócio**

- **Custo por interação:** Custo de uma interação com IA vs. custo de uma interação humana. Meta: redução de 50% em 180 dias.
- **Retenção de clientes:** Percentual de clientes que continuam usando o produto após interação com IA. Meta: acima de 85%.
- **Tempo de ciclo de feedback:** Tempo entre um erro ser identificado e corrigido. Meta: menos de 7 dias.

---

### 7. Fechamento e Gancho para o Capítulo 8

O *Operating System* não é um framework opcional. É a condição para que a IA não destrua a experiência do usuário enquanto impressiona com métricas técnicas. O time do Banco Digital aprendeu isso na pele: 90 dias para subir o satisfação de 1.8 para 4.2, mas 90 dias de dor de cabeça antes.

Se você implementar os 5 rituais (Observe, Schedule, Escalate, Review, Iterate), seu time terá governança para escalar. Mas tem um problema: quando você tem 2, 5, 10 agentes rodando ao mesmo tempo, o OS precisa ser replicado sem perder qualidade. No próximo capítulo, veremos como escalar esse *Operating System* para múltiplos agentes sem perder o controle. Spoiler: não é duplicando reuniões. 😉

---

# Capítulo 8: Cultura que Adota e Ética que Protege

## Cena de Abertura

Era uma quarta-feira de março de 2024, e Carlos, cientista de dados de um grande varejista brasileiro, estava na sala do VP de Produto com o laptop aberto. Na tela, o dashboard de monitoramento do novo modelo de recomendação que ele passou as últimas seis semanas treinando e testando.

"O modelo está pronto para produção", Carlos disse. "Mas eu não autorizo o deploy sem os testes de viés que solicitei na semana passada."

O VP de Produto, Ricardo, olhou para o relógio. "O board quer ver resultados no próximo comitê. Temos dois dias."

"Então a gente explica que precisa de mais duas semanas para garantir que o modelo não está penalizando fornecedores pequenos."

Ricardo balançou a cabeça. "Carlos, você sabe como funciona. Se a gente não entrega agora, perde o budget para o próximo trimestre. Depois a gente corrige."

Carlos fechou o laptop. "Corrigir depois de lançar um modelo com viés não é corrigir. É apagar incêndio."

O modelo foi para produção na sexta-feira sem os testes de viés. Na segunda-feira seguinte, o SAC registrou um volume anormal de reclamações de fornecedores que estavam sendo sistematicamente preteridos nas recomendações. O board pediu explicações. O caso foi documentado internamente.

Essa empresa tinha dinheiro. Tinha talento. Tinha dados. Mas caiu na *AI Trap* do mesmo jeito. Por quê?

A resposta é simples: ela não tinha checklists de deploy, revisão de viés ou canais de escalação ética. Sem esses sistemas, o comportamento correto vira opcional. E opcional, em pressão de entrega, sempre perde.

## Definição do Problema

"Fernanda, como a gente constrói uma cultura de IA que não dependa de heróis individuais?"

Essa pergunta apareceu em todas as empresas que visitei nos últimos três anos. De fintechs a varejistas, de healthtechs a seguradoras. Todo mundo quer "cultura de IA". Mas ninguém quer o trabalho sujo de construir os sistemas que a sustentam.

Cultura de IA não é treinamento. Não é workshop. Não é palestra de executivo no kickoff dizendo "vamos ser data-driven". Cultura de IA é o conjunto de rituais, incentivos e normas que determinam como uma organização descobre, desenvolve e mantém produtos de IA.

Sem ética operacionalizada, cultura de IA é só branding. E branding não segura um modelo em produção.

No Capítulo 7, a gente viu como construir o pipeline de descoberta de produtos de IA: como identificar problemas, validar hipóteses e priorizar oportunidades. Este capítulo é sobre como sustentar esse pipeline com governança que não vira burocracia.

O problema central é simples: empresas confundem "cultura de IA" com "treinamento de IA". Treinamento sem governança gera heróis, não times. E heróis cansam, pedem demissão e levam o conhecimento embora.

**Três sintomas de uma cultura sem ética:**

1. **Modelos vão para produção sem documentação.** O cientista de dados sabe o que fez, mas ninguém mais sabe. Se ele sair da empresa, o modelo vira caixa-preta.

2. **Times de produto e dados não falam a mesma língua.** O PM pede "recomendação personalizada", o cientista entrega um modelo de regressão logística que ninguém entende, e o usuário final recebe sugestões irrelevantes.

3. **O board descobre problemas éticos depois do lançamento.** Como no case da varejista. O board não perguntou sobre viés porque não sabia que deveria perguntar.

A pesquisa mais recente da McKinsey sobre o tema indica que apenas 28% das organizações têm o CEO com responsabilidade direta pela governança de IA (McKinsey, State of AI, 2025). O padrão é claro: elas investem em treinamento, contratam data scientists, compram ferramentas. Mas não criam os rituais que garantem que esses investimentos gerem produtos sustentáveis.

Cultura sem governança é anarquia. Governança sem cultura é burocracia.

A chave é um sistema que torne o comportamento ético mais fácil e mais recompensador que o comportamento antiético. Não é sobre moralismo. É sobre construir algo que dure.

## Framework Culture-Ethics

Vamos botar nome no troço. Chamo de **Culture-Ethics**, um framework de 8 componentes que conecta cultura de IA com ética operacionalizada.

Cada componente tem três partes: o que é, por que importa e como implementar.

### C, Checklists de Deploy

**O que é:** Uma lista de verificação que todo modelo precisa passar antes de ir para produção. Não é opcional. Não é "vamos ver se dá tempo".

**Por que importa:** O case da varejista mostrou o que acontece quando não tem checklist. O modelo foi para produção sem teste de viés porque ninguém exigiu.

**Como implementar:** Checklist mínima antes de qualquer deploy:
- [ ] Teste de viés realizado e documentado
- [ ] Documentação de decisões de modelo atualizada
- [ ] Métricas de performance acordadas com o time de produto
- [ ] Plano de rollback definido
- [ ] Monitoramento de deriva configurado

### U, User Feedback Loops

**O que é:** Um sistema para coletar feedback dos usuários sobre as decisões do modelo, não só sobre a interface.

**Por que importa:** Modelos de IA tomam decisões que afetam usuários. Se o usuário não tem como contestar, o modelo vira autoritário. E autoritarismo tecnológico gera rejeição.

**Como implementar:** Botão "Por que vi isso?" em recomendações. Canal para reportar sugestões inadequadas. Revisão periódica de amostras de decisões do modelo com usuários reais.

### L, Learning Rituais

**O que é:** Rituais periódicos onde o time revisa o que aprendeu com os modelos em produção.

**Por que importa:** Sem rituais de aprendizado, o time repete os mesmos erros. A documentação fica desatualizada. O conhecimento fica na cabeça de uma pessoa.

**Como implementar:** Revisão pós-deploy para todo modelo que entra em produção. Sessão quinzenal de "o que aprendemos essa semana" com o time todo.

### T, Transferência de Conhecimento

**O que é:** Um processo sistemático para garantir que o conhecimento sobre cada modelo não dependa de uma única pessoa.

**Por que importa:** Times que dependem de heróis são frágeis. O herói sai, o modelo quebra. E ninguém sabe como consertar.

**Como implementar:** Documentação viva de decisões técnicas e de produto, não só de código. Rituais de rotação de responsabilidades: cada pessoa do time assume um modelo diferente a cada trimestre.

### U, Unambiguous Metrics

**O que é:** Métricas claras e acordadas que todo mundo usa para avaliar o modelo. Time de produto, time de dados, board.

**Por que importa:** Sem métricas inequívocas, cada um usa a métrica que favorece seu argumento. O cientista diz que o modelo tem 95% de acurácia. O PM diz que o modelo não gerou receita. Os dois estão certos. E o board não sabe o que fazer.

**Como implementar:** Para cada modelo, definir três métricas: uma de usuário (ex: satisfação), uma de negócio (ex: receita incremental), uma de qualidade técnica (ex: deriva de dados). Todas documentadas e visíveis para todo mundo.

### R, Revisão de Viés

**O que é:** Um processo periódico de revisão de viés, não só no lançamento, mas ao longo da vida do modelo.

**Por que importa:** Viés não é estático. O que era justo em janeiro pode ser injusto em junho, porque os dados mudam, o contexto muda, os usuários mudam.

**Como implementar:** Revisão trimestral de viés para modelos críticos. Testes automatizados de viés rodando continuamente em produção. Canal para usuários reportarem decisões que consideram injustas.

### E, Ethical Escalation

**O que é:** Um caminho claro para qualquer pessoa da empresa escalar uma preocupação ética sem medo de retaliação.

**Por que importa:** No case da varejista, o cientista de dados sabia que o modelo tinha viés, mas não tinha um canal para escalar além do VP de Produto. E o VP queria lançar.

**Como implementar:** Comitê de ética em IA com membros de produto, dados, legal e um representante dos usuários. Canal anônimo para reportar preocupações. Garantia de que ninguém será punido por levantar uma bandeira vermelha.

### T, Time Rotation

**O que é:** Rotação periódica de responsabilidades dentro do time para evitar dependência de heróis.

**Por que importa:** O mesmo cientista de dados não pode ser a única pessoa que entende o modelo de crédito, o modelo de recomendação e o modelo de fraude. Se ela sair, a empresa quebra.

**Como implementar:** A cada trimestre, cada pessoa do time assume a responsabilidade primária por um modelo diferente. A pessoa anterior faz a transição, documenta o que sabe e vira suporte secundário.

**Dados quantitativos:** Times que implementam rotação de responsabilidades recuperam falhas em modelos críticos mais rápido, porque o conhecimento deixa de depender de uma única pessoa.

O framework Culture-Ethics não é um conjunto de regras para engessar o time. É um conjunto de rituais para liberar o time de depender de heróis.

## Casos e exemplos

### Caso 1: Banco digital, cultura de IA que atrai e retém talento

**Situação Inicial:** Em 2022, o banco digital enfrentava o mesmo problema de todo banco digital: como atrair e reter data scientists num mercado onde startups ofereciam salários competitivos e mais autonomia.

**O que estava errado:** O banco digital competia em salário, mas perdia em percepção de impacto. Data scientists queriam construir coisas novas, não manter sistemas legados. E o banco digital, apesar de ser digital, tinha sistemas legados.

**Como resolveu:** O banco digital criou um sistema de governança que oferecia o que startups não podiam: dados proprietários em escala, problemas reais com impacto em 80 milhões de usuários e um processo claro para levar modelos do experimento à produção sem burocracia.

A chave foi o **Model Governance Framework**, um sistema que padronizou o ciclo de vida de cada modelo em quatro estágios: desenvolvimento, validação, deploy e monitoramento. Cada estágio tem checklists obrigatórios. O checklist de deploy, por exemplo, exige: documentação do modelo, teste de viés, análise de explainability e definição de métricas de monitoramento.

**Resultados:** O banco digital reduziu o tempo médio de deploy de modelos de 45 dias para 12 dias. E, mais importante, zerou os incidentes éticos relacionados a viés algorítmico nos 18 meses seguintes à implementação do framework. A rotatividade no time de dados caiu 40% entre 2022 e 2024 (caso ilustrativo).

**Lição:** Cultura de IA não se constrói com salário. Se constrói com sistemas que tornam o trabalho do cientista de dados mais produtivo e mais seguro.

### Caso 2: Um grande varejista, como não ser engolido pela AI Trap

**Situação Inicial:** Em 2023, um grande varejista tinha um time de dados de 80 pessoas, mas menos de 20% dos modelos desenvolvidos chegavam à produção. O resto morria em POCs.

**O que estava errado:** O time de dados trabalhava isolado do time de produto. O cientista de dados desenvolvia um modelo, apresentava para o PM, o PM dizia "isso não resolve meu problema", e o modelo era abandonado. Sem governança que forçasse a colaboração, cada POC era um experimento descartável.

**Como resolveu:** Um grande varejista implementou um framework de governança de produto que exigia que todo projeto de IA tivesse um PM responsável desde o início. Não era "o time de dados vai fazer um modelo e depois a gente vê o que fazer". Era "o PM define o problema, o cientista de dados define a solução, e os dois trabalham juntos até o deploy".

O framework incluía checklists de alinhamento, métricas acordadas e revisões quinzenais de progresso.

**Resultados:** Em 12 meses, a taxa de modelos que chegavam à produção subiu de 20% para 65% (caso ilustrativo). O time de dados passou a ser visto como parceiro de produto, não como fornecedor de tecnologia.

**Lição:** Governança não é burocracia. É o que impede que POCs virem custo morto.

### Caso 3: Um app de delivery, ética operacionalizada em escala

**Situação Inicial:** Em 2024, o app de delivery processava 60 milhões de pedidos por mês com modelos de recomendação, precificação e roteirização. Cada modelo tomava decisões que afetavam restaurantes, entregadores e clientes.

**O que estava errado:** O app de delivery tinha modelos que favoreciam restaurantes maiores em detrimento dos pequenos, porque os dados de treino refletiam o viés histórico de recomendação. E não tinha um processo claro para identificar e corrigir esses vieses.

**Como resolveu:** O app de delivery criou um **Comitê de Ética em IA** com membros de produto, dados, legal, operações e um representante dos entregadores. O comitê se reunia mensalmente para revisar modelos críticos, analisar reclamações e decidir sobre trade-offs entre eficiência e equidade.

E mais: implementaram um sistema de **testes automatizados de viés** que rodava continuamente em produção. Se um modelo começava a favorecer um grupo em detrimento de outro, o sistema alertava o time antes do impacto se tornar significativo.

**Resultados:** O app de delivery identificou e corrigiu vieses em 12 modelos críticos em 2024 (caso ilustrativo). A satisfação dos entregadores subiu 15% depois que ajustaram o modelo de roteirização para distribuir melhor os pedidos.

**Lição:** Ética operacionalizada não é sobre ser bonzinho. É sobre construir sistemas que detectam problemas antes que eles virem crise.

## Guia Prático

Como implementar o framework Culture-Ethics em 90 dias.

**Esta semana:**

1. **Diagnóstico rápido:** Liste todos os modelos em produção na sua empresa. Para cada modelo, responda: tem documentação? Tem checklist de deploy? Tem métricas acordadas? Tem revisão de viés?

2. **Identifique o herói:** Quem é a única pessoa que entende o modelo de crédito? O modelo de fraude? O modelo de recomendação? Se essa pessoa sair amanhã, o que acontece?

3. **Crie o canal de escalação ética:** Um email, um grupo no Slack, um formulário anônimo. Qualquer pessoa da empresa pode reportar uma preocupação ética.

**Próximos 30 dias:**

1. **Implemente o checklist de deploy:** Para todo modelo novo, o checklist é obrigatório. Sem checklist aprovado, sem produção.

2. **Defina métricas inequívocas:** Para cada modelo crítico, três métricas: usuário, negócio, técnica. Documente e compartilhe com o board.

3. **Inicie a rotação de responsabilidades:** Escolha um modelo. A pessoa responsável por ele passa o conhecimento para outra pessoa do time. A primeira vira suporte secundário.

**Próximos 90 dias:**

1. **Implemente revisão de viés trimestral:** Para modelos críticos, agende revisões trimestrais de viés com o time todo.

2. **Crie o comitê de ética:** Com membros de produto, dados, legal e um representante dos usuários (ou dos afetados pelo modelo). Reunião mensal.

3. **Automatize testes de viés:** Configure testes automatizados que rodam continuamente em produção. Se o modelo começar a derivar, o sistema alerta antes do impacto.

**Dica:** Não tente implementar tudo de uma vez. Comece com o checklist de deploy e a rotação de responsabilidades. Esses dois componentes já resolvem 80% dos problemas de dependência de heróis e falta de governança.

## Métricas de Sucesso

Como saber se o framework Culture-Ethics está funcionando? Acompanhe estas métricas:

1. **Tempo médio de deploy de modelos:** Deveria cair 50% nos primeiros 3 meses, conforme a padronização reduz retrabalho. (Alvo: de 2 semanas para 5 dias úteis.)

2. **Taxa de modelos que chegam à produção:** Deveria subir de 20% para pelo menos 60% em 6 meses, como no case dum grande varejista.

3. **Tempo de recuperação de falhas:** Deveria cair com a rotação de responsabilidades, porque o conhecimento deixa de depender de uma pessoa só.

4. **Rotatividade no time de dados:** Deveria cair 40% em 12 meses, como no case de um banco digital.

5. **Número de vieses identificados e corrigidos:** Deveria subir nos primeiros meses (conforme os testes começam a detectar problemas) e depois estabilizar.

6. **Satisfação dos usuários afetados pelo modelo:** Deveria subir continuamente, como no case do app de delivery.

**Como medir:** Crie um dashboard de governança com essas métricas. Atualize mensalmente. Compartilhe com o board.

## Fechamento e Gancho

A varejista da cena de abertura não quebrou. Mas perdeu confiança. Perdeu fornecedores. Perdeu tempo corrigindo um problema que poderia ter evitado com um checklist de 5 itens.

O cientista de dados, Carlos, pediu demissão três meses depois. Ele não queria trabalhar num lugar onde a ética era opcional.

O VP de Produto, Ricardo, foi promovido. Porque o board não sabia que o modelo tinha viés. E o board não sabia porque não tinha um sistema de governança que o informasse.

Cultura de IA não é sobre contratar as pessoas mais brilhantes. É sobre construir sistemas que tornem o comportamento correto mais fácil que o comportamento incorreto.

No próximo capítulo, a gente vai ver como escalar produtos de IA sem escalar os problemas. Como passar de 10 para 100 modelos sem perder o controle. Porque escalar sem governança não é escalar. É multiplicar o caos.

A cultura que adota é a que protege. O resto é só branding.

---

# EPÍLOGO: Seu Plano 30/60/90

Você terminou o livro. Feche os olhos por 30 segundos. Pense na sua organização. Em que parte ela está? Abra a ferramenta da parte onde você está. Preencha. Faça uma coisa esta semana. Não 10. Uma. Este livro não foi escrito para ser lido, foi escrito para ser usado.

---

*Fernanda Faria, 2026*
