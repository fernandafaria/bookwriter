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

## Seção 1: Cena de abertura

Era uma quinta-feira de março, e Carlos, VP de Produto de um banco digital brasileiro, estava na reunião trimestral de resultados. O board estava tenso. A promessa do trimestre anterior era clara: o chatbot com IA generativa iria revolucionar o atendimento ao cliente.

Carlos projetou o slide com orgulho. "O modelo bateu o benchmark na classificação de intenções. Métricas de validação excelentes. Treinado com milhões de conversas históricas, curadas e balanceadas."

O CEO não sorriu. "E a satisfação do cliente?"

Silêncio.

"Despencou", respondeu Carlos, olhando para o slide.

O CEO fechou os olhos por um segundo. O atendimento humano do banco tinha nota alta. O chatbot não só não estava ajudando, estava destruindo a experiência do cliente. E o board queria saber o que tinha acontecido com o orçamento de quase um ano de desenvolvimento.

"Mas as métricas são excelentes", insistiu Carlos. "A tecnologia funciona. O problema é..."

Ele parou. Não sabia o que dizer. Porque não sabia qual era o problema.

O CEO olhou para ele. "Carlos, você acabou de me mostrar que seu time construiu uma Ferrari que ninguém quer dirigir. E gastou uma fortuna nisso. Como chegamos aqui? E mais importante: como sair?"

Carlos não existe. É um compósito de situações que já vi e ouvi em boards, comitês executivos e reuniões de produto Brasil afora. Empresas com dinheiro, talento e dados investindo milhões em IA que ninguém quer usar. E o pior: times de produto que não conseguem explicar por que a Ferrari não anda.

Essa cena tem nome. Elena Verna, que já liderou growth na Replit e na SurveyMonkey, chama de "AI Confidence Theater": o teatro da confiança em IA, em que a apresentação importa mais que o resultado (Elena Verna, elenaverna.com, jul/2026). A métrica técnica sobe, o slide fica bonito, e ninguém faz a pergunta óbvia: o cliente melhorou?

Eu sei porque já estive na cadeira do Carlos. Liderei um projeto de machine learning para predição de churn. O modelo era tecnicamente impecável, as métricas de validação eram as melhores que o time já tinha visto. Mas, meses depois, a taxa de churn não tinha mexido. O problema? O modelo previa churn com precisão, mas o time de operações não tinha processo para agir sobre as predições. A gente entregou um diagnóstico perfeito para um paciente que não tinha médico. Esse erro me custou um trimestre de credibilidade com o CEO, e me ensinou que métrica técnica sem processo de produto é ruído.

---

## Seção 2: Definição do problema

"Fernanda, como garantimos que nossa estratégia de IA não vire só mais uma iniciativa de tecnologia?"

Essa pergunta me foi feita por um CPO de uma fintech brasileira, depois de ele ver três projetos consecutivos de IA falharem na empresa dele. Três. Todos com times competentes, orçamento generoso e dados de qualidade.

O nome do fenômeno que ele estava vivendo é *AI Trap*. A armadilha de acreditar que mais IA é igual a melhor produto: ignorar que o valor da IA depende da maturidade do processo de produto que a sustenta.

A *AI Trap* tem três sintomas clássicos:

1. **Obsessão por métricas técnicas.** Accuracy, precision, recall. Números que impressionam o time de engenharia, mas não dizem nada sobre valor para o usuário. Carlos tinha accuracy alta e satisfação no chão. As duas coisas coexistiram perfeitamente.

2. **Soluções em busca de problemas.** "Vamos colocar IA em tudo." O time encontra um martelo novo e decide que tudo é prego. Chatbot para atendimento. IA para recomendar produtos. IA para analisar crédito. A tecnologia vem primeiro, o problema depois.

3. **Ignorar limitações e contexto real de uso.** O modelo funciona no laboratório, nos testes A/B controlados, nos dados históricos. No mundo real, com usuários reais, dados sujos e casos de borda imprevistos, ele quebra. E ninguém planejou para isso.

O dado de choque não vem de relatório de consultoria. Vem de quem vive o hype por dentro. Elena Verna trabalha numa empresa de IA e usa IA o dia inteiro, e mesmo assim se cansou do teatro: quando alguém diz que a IA mudou a vida, ela responde "legal, me mostra". E a lista de coisas realmente críticas, daquelas que fariam o trabalho desmoronar se sumissem amanhã, é curta (Elena Verna, elenaverna.com, jul/2026). As empresas anunciam muito e colhem pouco.

Este livro não é sobre tecnologia, é sobre julgamento. E a *AI Trap* é o maior teste de julgamento que um PM pode enfrentar. O primeiro passo para passar nesse teste é entender onde sua organização está.

---

## Seção 3: Framework, o mapa e o detector de armadilhas

"Para diagnosticar onde você está, você precisa de duas ferramentas: um mapa e um detector de armadilhas."

### O modelo de maturidade MATURE (5 níveis)

Deixa eu te apresentar o framework que usei com dezenas de empresas brasileiras nos últimos anos. Chamo de modelo de maturidade MATURE, sigla de Maturity Assessment for Technology-User Readiness Evaluation. Cinco níveis. Cada nível diz como a empresa toma decisões de produto e, na sequência, o que acontece quando ela tenta fazer IA.

**M, nível 1: reativo (mapear)**

Decisões do chefe. Discovery desconhecida. Roadmap é uma lista de desejos do CEO.

O que acontece com IA: é moda. Projetos começam e morrem. Ninguém mede nada. A empresa compra uma plataforma de IA, contrata dois cientistas de dados, eles passam meses construindo algo que ninguém pediu, e o projeto morre quando o orçamento acaba.

Elena Verna descreve esse nível com precisão: todo mundo precisa de um agente de IA agora, porque você estaria perdendo uma experiência transformadora se não tiver um. Só que quase ninguém sabe o que um agente de IA faz (Elena Verna, elenaverna.com, jul/2026). O FOMO compra, a empresa paga, e ninguém aprende.

**A, nível 2: feature factory (avaliar)**

O time conversa com clientes, mas não registra. Priorização por quem grita mais. A/B tests existem, mas são raros e mal desenhados.

O que acontece com IA: é reativa. Alguém no board leu sobre IA generativa e pediu um chatbot. O time constrói. O chatbot funciona tecnicamente. Ninguém pergunta se o usuário queria um chatbot. Métricas técnicas bonitas, satisfação baixa.

É exatamente onde Carlos estava. O banco digital dele estava no nível 2. O time sabia fazer discovery? Sabia. Fazia? Quando sobrava tempo. Priorizava com dados? Não. Priorizava com urgência do board.

**T, nível 3: data-informed (testar)**

Múltiplas fontes de dados de usuário. Priorização com critérios claros. Experimentação frequente.

O que acontece com IA: começa a ter propósito. O time pergunta "qual problema queremos resolver?" antes de escolher a tecnologia. Mas ainda falta conexão com a estratégia de negócio. A IA resolve problemas táticos, não estratégicos.

É o nível em que o time aprende o teste do "me mostra". Antes de aplaudir um número, pergunta o que aquilo mudou na vida real do usuário. Elena Verna faz exatamente isso com qualquer história de IA milagrosa: "legal, me mostra" (Elena Verna, elenaverna.com, jul/2026). Essa pergunta separa teatro de resultado.

**U, nível 4: product operating model (usar)**

Product trio em fluxo contínuo. Experimentação diária. Produto visto como sistema, não como feature.

O que acontece com IA: vira ferramenta de augmentação. O time sabe quando usar IA e quando não usar. O modelo é monitorado por outcomes, não por métricas técnicas.

É o nível em que a Anthropic opera. Dianne Penn, a primeira PM técnica da empresa, hoje lidera produto para os times de pesquisa e labs. Em vez de confiar em accuracy de laboratório, o time dirige o desenvolvimento por evals: testes que codificam o que "bom" significa no mundo real, antes de o modelo chegar ao usuário (Dianne Penn, Anthropic, Lenny's Podcast, jul/2026). O loop é dirigido por evals, não por vaidade de benchmark.

**R, nível 5: AI-native (refinar)**

A empresa inteira entende estratégia de produto. Decisões descentralizadas. Inovação no dia a dia.

O que acontece com IA: a IA é parte natural do processo. O time identifica oportunidades, valida com usuários, constrói com IA quando faz sentido. A tecnologia fica invisível. O valor é o que importa.

### O detector AI Trap (3 sintomas)

Agora o detector de armadilhas. Três perguntas para saber se você está na *AI Trap*:

**Sintoma 1: métrica técnica vs. métrica de valor**

❌ O time comemora: "subimos a accuracy!"
✅ O time pergunta: "o NPS melhorou? O tempo de resolução caiu? O churn diminuiu?"

**Sintoma 2: solução antes do problema**

❌ "Vamos colocar IA no chat. Depois a gente vê o que fazer."
✅ "Qual o maior problema de atendimento hoje? Será que IA é a melhor solução?"

**Sintoma 3: ignorar contexto**

❌ "O modelo funciona nos nossos dados de treino. Está pronto para produção."
✅ "Testamos com usuários reais? Em cenários reais? Com dados sujos? O que acontece quando o modelo erra?"

Se você respondeu "sim" para pelo menos dois sintomas, você está na *AI Trap*. Bem-vindo ao clube. A boa notícia: tem saída.

---

## Seção 4: Casos reais

Em vez de casos inventados, dois casos de quem vive isso por dentro. Um mostra a armadilha, o outro mostra a saída.

### Caso 1: Elena Verna e o teatro da confiança em IA

Elena Verna é head de growth, com passagem pela Replit e pela SurveyMonkey. Ela trabalha numa empresa de IA, usa IA o dia inteiro, constrói produtos com IA. E mesmo assim, quando alguém anuncia que a IA mudou a vida, ela responde com uma pergunta: "legal, me mostra."

O que ela viu: resumir Slack, responder e-mail, fazer varredura agendada. Útil? Sim. Mas quando ela pede algo tão crítico que o trabalho desmoronaria se sumisse amanhã, a lista fica curta (Elena Verna, elenaverna.com, jul/2026).

Ela chama o fenômeno de "AI Confidence Theater". O teatro da confiança em IA. Cinco anos atrás, as pessoas queriam parecer que trabalhavam mais que todo mundo. Hoje querem parecer que a IA faz tudo. A mesma performance, com acessórios diferentes.

O estrago é real. O marketing vende certeza onde não existe certeza. Os agentes dispararam só metade das vezes e só entregam algo decente quando alimentados com contexto muito específico (Elena Verna, elenaverna.com, jul/2026). E quando o comprador descobre que o super-agente não funciona, ele assume que toda IA é mentira e enterra a cabeça. O hype mata a inovação de verdade.

Esse é o custo da *AI Trap* em estado puro: promessa na frente, processo ausente atrás. Ninguém pergunta "me mostra o problema que isso resolve".

### Caso 2: Dianne Penn e o loop dirigido por evals

Dianne Penn foi a primeira PM técnica da Anthropic. Entrou quando o time de produto tinha cinco engenheiros, e hoje lidera produto para os times de pesquisa e labs, depois de ajudar a construir desde o Claude 2 até o Claude Code, o MCP e as Skills (Dianne Penn, Anthropic, Lenny's Podcast, jul/2026).

O que a Anthropic faz de diferente não é ter modelos melhores. É como decide o que é "melhor". Em vez de confiar em accuracy de laboratório, o time dirige o desenvolvimento por um loop de evals: testes que codificam o que "bom" significa no cenário real de uso. O número sobe quando o eval melhora, não quando o benchmark infla.

E há um segundo ponto que vale o capítulo inteiro: a fronteira irregular. Em inglês, "jagged edge". O modelo é sobre-humano numa tarefa e péssimo na tarefa do lado. Você não descobre isso olhando a média. Descobre testando, cenário por cenário, onde exatamente o modelo quebra.

Por isso, para Dianne, o que continua insubstituível é o julgamento humano: decidir onde confiar no modelo e onde ele erra de forma imprevisível (Dianne Penn, Anthropic, Lenny's Podcast, jul/2026). A empresa não tenta vender IA como certeza. Trata o modelo como uma ferramenta com uma borda irregular, e coloca gente exatamente nessa borda.

É o oposto do teatro da confiança. Em vez de "confie na IA", o recado é "teste a IA". Em vez de accuracy, evals. Em vez de promessa, prova.

---

## Seção 5: Scripts, como vender o diagnóstico internamente

Você leu os casos. Sabe identificar a *AI Trap*. Agora a pergunta que tira o sono: como convencer o board, o CEO e o time de que "IA em tudo" é um erro, sem soar como a pessoa que está atrapalhando a inovação?

Aqui estão três scripts reais. Use as palavras, adapte o contexto. O roteiro funciona porque é baseado em padrões que se repetem.

---

### Cenário 1: o CEO voltou de um evento e quer "IA em tudo"

Esse é o clássico. O CEO foi no Web Summit, viu um concorrente lançar algo com IA, e voltou com a frase mágica: "Precisamos ter IA no nosso produto."

**❌ Não diga:**
"Precisamos primeiro fazer um diagnóstico de maturidade." (Seu CEO ouviu: "Sou contra inovação." Você perdeu.)

**✅ Diga:**
"Sua visão está certa. A pergunta não é *se* vamos usar IA, é *onde* ela vai gerar mais resultado mais rápido. Se eu te mostrar, com dados dos nossos clientes, qual iniciativa de IA entregaria retorno em 6 meses vs. 18 meses, você prefere que a gente aposte na rápida ou na lenta?"

**Estrutura de slide recomendada:**
- Slide 1: "IA pode transformar [área X]." (valide a visão do CEO)
- Slide 2: "Aqui estão 3 oportunidades que identificamos." (mostre que você já fez o trabalho)
- Slide 3: "A oportunidade A entrega resultado em 6 meses com R$ X. A oportunidade C levaria 18 meses. Recomendamos começar pela A."
- Slide 4: "Para isso, precisamos de 2 semanas de discovery com 15 clientes. Custo: zero. Tempo: 2 sprints."

**Objeção mais provável:** "Mas o concorrente Y já está fazendo."
**Resposta:** "E é exatamente por isso que não podemos copiá-los. Copiar nos coloca 12 meses atrás. Entender o que nosso cliente precisa, e que o concorrente não viu, nos coloca 12 meses à frente. Me dê 2 semanas."

---

### Cenário 2: o CFO quer saber "quanto custa e quando paga"

Depois de um projeto de IA que queimou dinheiro, o CFO está cético. Ele não quer ouvir sobre frameworks, quer ouvir sobre dinheiro.

**❌ Não diga:**
"Precisamos investir em maturidade de produto antes de fazer IA." (Seu CFO ouviu: "Mais dinheiro, sem prazo, sem número.")

**✅ Diga:**
"Meu trabalho é garantir que cada real investido em IA gere retorno mensurável. Hoje, nosso processo tem [X]% de chance de gerar retorno. Se a gente fizer [ação específica] primeiro, essa chance sobe pra [Y]%. Eu prefiro apostar com [Y]% de chance. Aqui está o business case."

**Estrutura de slide recomendada:**
- Slide 1: Custo do último projeto de IA: R$ X milhões. Retorno medido: [Y].
- Slide 2: Por que o retorno foi baixo: [diagnóstico específico em 1 frase].
- Slide 3: Próximo projeto: custo de R$ Z (menor), retorno projetado de R$ W, prazo de P meses.
- Slide 4: "Recomendação: investir R$ [valor pequeno] em discovery antes de aprovar orçamento de desenvolvimento. Se a discovery não validar a oportunidade, economizamos R$ [valor grande]."

**Objeção mais provável:** "Isso é muito tempo. O board quer resultado agora."
**Resposta:** "Concordo. Por isso o discovery são 2 semanas, não 2 meses. Se não encontrarmos nada em 2 semanas, você tem minha palavra: eu mesma peço para pausar. Mas se encontrarmos, você vai para o board com um número, não com uma promessa."

---

### Cenário 3: o time de engenharia quer construir, não diagnosticar

Seus engenheiros são competentes, estão animados com IA, e ouvir "vamos fazer discovery primeiro" soa como "vamos burocratizar a inovação".

**❌ Não diga:**
"Precisamos seguir o framework MATURE. Vocês estão no nível 1." (Seu time ouviu: "Vocês são imaturos." Perdeu o time.)

**✅ Diga:**
"Vocês são o melhor time que eu poderia ter para esse desafio. E é exatamente por isso que eu quero que a gente acerte o alvo. Imagina gastar 6 meses construindo algo que ninguém usa. Vocês merecem trabalhar em coisas que os clientes amam. Me deem 2 semanas para eu trazer os clientes para a mesa. Depois disso, vocês constroem."

**Estrutura da dinâmica (workshop de 2 horas):**
- Minuto 0-15: apresentar 2 cases de quem construiu sem olhar o problema: o teatro da confiança em IA (Elena Verna) e o compósito do chatbot que afundou a satisfação.
- Minuto 15-60: time entrevista 3 clientes (sim, durante o workshop, prepare as entrevistas antes).
- Minuto 60-90: time mapeia o que ouvimos que contradiz nossas hipóteses.
- Minuto 90-120: definir 1 experimento para a próxima sprint. Não 5. Um.

**Objeção mais provável:** "Já sabemos o que o cliente quer."
**Resposta:** "Ótimo. Então essas 2 horas vão confirmar o que vocês já sabem. Mas se aparecer UMA coisa que vocês não esperavam, essas 2 horas acabaram de salvar 6 meses de retrabalho. Topam?"

---

### Esta semana: comece aqui

1. **Escolha o cenário acima que mais se parece com sua situação.** Imprima o script. Adapte os nomes, os números, o contexto.
2. **Agende 30 minutos na agenda do stakeholder.** Não mande email. Não mande slide antes. Agende e vá com o script.
3. **Se a conversa não funcionar na primeira vez,** volte aqui. Leia o cenário de novo. Você provavelmente usou o "❌ Não diga" sem perceber. Acontece. Tente de novo.

Lembre-se: você não está pedindo permissão para fazer discovery. Você está oferecendo um caminho mais rápido para o resultado que o stakeholder já quer.

---

## Seção 6: Métricas de sucesso

Como saber se você saiu da *AI Trap*? Três categorias de métricas. Nenhuma delas é accuracy.

### Valor para o usuário

- **NPS do canal com IA vs. sem IA.** Se o NPS caiu, a IA está destruindo valor. O teste é o do "me mostra": o cliente real melhorou ou a métrica de treino que melhorou? (Elena Verna, elenaverna.com, jul/2026)
- **Tempo de resolução.** A IA está acelerando ou atrasando a vida do usuário?
- **Taxa de escalonamento para humano.** Quanto mais o usuário precisa de ajuda humana, pior a IA. O objetivo é derrubar essa taxa, não escondê-la.

### Valor para o negócio

- **Custo por interação.** IA deve reduzir custo, não aumentar. Meça o custo inteiro, incluindo manutenção e retrabalho.
- **Retorno sobre o investimento (ROI).** Quanto a IA gerou de receita ou economia vs. quanto custou construir e manter.
- **Churn de clientes que interagem com IA vs. os que não interagem.** A IA está retendo ou afastando clientes? Se o churn for maior no grupo com IA, algo está errado.

### Qualidade de implementação

- **Percentual de projetos de IA que chegam a produção.** Se metade dos projetos morre antes de lançar, o problema é o processo, não a tecnologia.
- **Tempo médio de desenvolvimento.** De discovery a produção. Quanto mais rápido, melhor o processo.
- **Taxa de erros em produção.** Não accuracy. Erros reais, com usuários reais. O que acontece quando o modelo erra? Aqui vale a regra da fronteira irregular: o erro não aparece na média, aparece no caso de borda (Dianne Penn, Anthropic, Lenny's Podcast, jul/2026).

---

## Seção 7: Fechamento com gancho

Você descobriu onde está. Talvez esteja no nível 2, como Carlos. Talvez no nível 3. Talvez, e isso é mais comum do que você imagina, esteja no nível 1 e nem saiba.

A boa notícia: maturidade não é destino. É escolha. Você pode subir de nível. Pode sair da *AI Trap*. Pode transformar a Ferrari em um carro que as pessoas queiram dirigir.

A má notícia: subir de nível exige trabalho duro. Exige parar de culpar a tecnologia e começar a olhar para o processo. Exige admitir que o problema não é o modelo, é a falta de discovery. Exige explicar para o board que IA não é atalho, é ferramenta. E ferramenta só funciona nas mãos de quem sabe o que está fazendo.

No próximo capítulo, vamos mergulhar no primeiro passo prático para sair da *AI Trap*: como fazer discovery profunda para identificar problemas reais que merecem solução de IA. Porque antes de construir, você precisa saber o que construir. E, mais importante, por que construir.

Carlos aprendeu isso do jeito difícil. Mas ele aprendeu. O board dele hoje entende que IA não é sobre tecnologia. É sobre julgamento. E que o melhor projeto de IA é aquele que começa com uma pergunta simples: qual problema estamos resolvendo?

Dianne Penn diria: teste antes de confiar. Elena Verna diria: me mostra o que muda na vida real. As duas apontam para o mesmo lugar. IA sem julgamento humano é teatro. Com julgamento, é ferramenta.

Se você ainda não sabe a resposta, não se preocupe. O próximo capítulo vai te ajudar a encontrá-la.

---

# Capítulo 2: O Mapa de Maturidade, os 5 níveis que toda área atravessa

---

## 1. Cena de Abertura

Era uma terça-feira de setembro, e Renata, Head de Produto de uma rede varejista, estava na sala do CEO. Na mesa, um relatório pesado da consultoria que a empresa tinha contratado para dizer se estavam prontos para inteligência artificial.

"O diagnóstico é claro", disse o CEO, folheando o sumário executivo. "Estamos prontos para IA. A consultoria recomenda começar com recomendação personalizada no app."

Renata respirou fundo. Ela sabia o que o relatório não dizia. O time dela não tinha acesso a dados limpos de cliente havia anos. O ERP era antigo. O time de engenharia passava a maior parte do tempo apagando incêndio.

"Antes da recomendação personalizada", ela disse, "me deixa fazer uma pergunta. Quantos clientes nossos a gente entrevistou nos últimos meses?"

Silêncio.

"E quantas hipóteses de produto a gente testou e descartou esse ano?"

O CEO fechou o relatório. "O que você está sugerindo?"

"Que a gente pode estar no nível 2 de maturidade de produto achando que está no nível 4. E que gastar uma fortuna em IA agora é como colocar turbina num carro sem freio."

Essa conversa não aconteceu com um banco digital. Aconteceu com uma varejista. Poderia ter sido uma indústria, uma healthtech, uma logística. O padrão é o mesmo: times que confundem "ter orçamento para IA" com "estar pronto para IA".

O Capítulo 1 te ensinou a identificar a AI Trap, quando a tecnologia entra antes do diagnóstico. Este capítulo te dá a ferramenta para fazer o diagnóstico certo: o Mapa de Maturidade.

## 2. Definição do Problema

O problema não é falta de IA. É falta de diagnóstico honesto sobre onde o time realmente está.

Hoje, a maioria dos times de produto brasileiros que acompanho já testa IA em produção. Adoção não é maturidade.

A confusão entre "ter IA" e "ser maduro em produto" é a causa raiz de projetos que queimam orçamento e entregam zero valor.

**Nota sobre os exemplos deste capítulo:** Os casos são baseados em experiências reais da autora com times brasileiros. Números e detalhes identificáveis foram omitidos de propósito; a lição de cada caso não depende de precisão.

Três sinais de que você está diagnosticando errado:

**Sinal 1: Você mede accuracy do modelo, não satisfação do usuário.** Accuracy é métrica técnica. Satisfação é métrica de produto. Se você só olha a primeira, está escondendo o segundo.

**Sinal 2: Você prioriza por "quem grita mais alto", não por dados de uso.** Quando o CEO decide o que construir, você não está gerenciando produto. Está executando ordens.

**Sinal 3: Você celebra lançamentos, não aprendizados.** Se o time comemora quando uma feature vai para produção, mas não celebra quando descobre que uma hipótese estava errada, você está em Feature Factory.

O framework AI Trap, apresentado no Capítulo 1, mostrou o problema. Este capítulo mostra como medi-lo. Porque sem diagnóstico, qualquer mapa serve.

Para isso, existe um framework que mapeia os 5 níveis que toda área atravessa. Ele se chama MATURE, uma adaptação do Product Excellence Maturity Model de Pawel Huryn para a realidade de times brasileiros.

Pawel Huryn define o Product Operating Model como "um sistema onde times empowered descobrem e entregam soluções que resolvem problemas reais dos usuários". A maioria das empresas está em Feature Factory (Nível 2) mas acha que está em Product Operating Model (Nível 4). A diferença? Feature Factory entrega o que pediram. Product Operating Model entrega o que resolve.

## 3. Framework / Componentes

O framework MATURE não é sobre tecnologia. É sobre como o time toma decisões.

Os 5 níveis formam uma escada. Você não pula degraus. Toda tentativa de pular do Nível 2 para o Nível 4 termina em frustração, projetos abandonados e um diretor de tecnologia que diz "IA não funciona".

### Os 5 Níveis de Maturidade

| Nível | Nome | Acrônimo | Como decide | Sinal de alerta | Exemplo real |
|-------|------|----------|-------------|-----------------|--------------|
| 1 | Reativo | M - Mapear | Por instinto ou crise | "O CEO pediu, a gente faz" | Startup que lançou várias features seguidas sem testar nenhuma |
| 2 | Feature Factory | A - Avaliar | Por prioridade do stakeholder mais alto | "Entregamos no prazo, mas ninguém usa" | Marketplace que criou recomendação por IA sem validar com nenhum usuário |
| 3 | Data-Informed | T - Testar | Por dados quantitativos | "O dado diz X, mas o cliente diz Y" | Seguradora que otimizou conversão mas aumentou reclamações |
| 4 | Product Operating Model | U - Usar | Por experimentos com usuários reais | "Aprendemos mais com o fracasso do que com o sucesso" | Logística que testou roteirização com IA em poucas rotas antes de escalar |
| 5 | AI-Native | R - Refinar | Por aprendizado contínuo do sistema | "O modelo aprende sozinho, mas o time não" | Banco digital que recalibra o modelo semanalmente com feedback de usuários |

### Nível 1: Reativo (Mapear)

Aqui, as decisões são tomadas com base em feeling, intuição ou pressão hierárquica. Não há dados de usuário, não há pesquisa, não há experimentação.

**O que parece:** "O CEO acha que precisamos de um chatbot." "O VP de vendas disse que os clientes querem X."

**Por que é problemático:** Você constrói features que ninguém pediu e ninguém usa. O custo de oportunidade é alto: o time gasta meses em algo que poderia ter sido descartado com uma conversa de meia hora.

**Exemplo real:** Uma startup de fintech construiu um sistema de recomendação de investimentos baseado no que o CEO achava que os jovens queriam. Gastou um orçamento de produto inteiro no desenvolvimento. No fim, quase nenhum usuário tinha clicado em uma recomendação. Ninguém havia entrevistado um jovem antes de começar.

**Curiosity gap:** Mas como saber se você está no Nível 1 ou no Nível 2? A resposta está em como você trata a evidência que contradiz você. Se você a ignora, está no Nível 1.

### Nível 2: Feature Factory (Avaliar)

O time começa a conversar com clientes. Faz pesquisas, entrevistas, testes. Mas os resultados não são registrados de forma estruturada, e a priorização ainda é política.

**O que parece:** "Fizemos 10 entrevistas." "Os clientes disseram que querem X." "Mas o CFO acha que devemos fazer Y."

**Por que é problemático:** A pesquisa existe, mas não informa decisões. O time coleta dados para justificar decisões já tomadas, não para descobrir o que fazer.

**Exemplo real:** Um marketplace brasileiro investiu em um sistema de recomendação baseado em machine learning. O time de produto entrevistou dezenas de vendedores. Todos disseram que o maior problema era a logística, não as recomendações. O time ignorou e construiu o sistema de recomendação. Tempos depois, a adoção entre vendedores continuava baixa. O problema de logística nunca foi resolvido.

**Curiosity gap:** Mas como saber se você está no Nível 2 ou no Nível 3? A resposta está no que você faz com o dado que dói. Se você coleta mas não age, está no Nível 2.

### Nível 3: Data-Informed (Testar)

O time usa múltiplas fontes de dados: pesquisa qualitativa, dados quantitativos, testes A/B. Mas a priorização ainda é frágil. O time testa, mas não age nos resultados.

**O que parece:** "Temos dados que mostram X. Fizemos um teste A/B que mostrou Y. Mas o VP de produto acha que devemos fazer Z."

**Por que é problemático:** O time tem os dados, mas não tem autonomia para agir. A experimentação é tímida. Testes são feitos em amostras pequenas, com baixa significância estatística. Resultados negativos são ignorados.

**Exemplo real:** Uma empresa de seguros investiu em um assistente virtual com IA. O time fez testes A/B que mostraram que o assistente reduzia o tempo de atendimento, mas aumentava o número de reclamações. O VP de produto decidiu lançar mesmo assim, argumentando que "eficiência é mais importante". Resultado: o NPS caiu de forma consistente nos meses seguintes.

**Curiosity gap:** Mas como saber se você está no Nível 3 ou no Nível 4? A resposta está em como você reage quando o dado discorda de você. Se você age sobre ele, está no Nível 3.

### Nível 4: Product Operating Model (Usar)

O Product Trio (Product Manager, Designer, Engenheiro) trabalha em fluxo contínuo. Descoberta e entrega acontecem em paralelo. A experimentação é diária.

**O que parece:** "Testamos três abordagens esta semana." "Os dados mostram que a abordagem B funciona melhor." "Vamos iterar."

**Por que importa:** O time tem autonomia para decidir o que construir. A priorização é baseada em dados de usuário, não em hierarquia. Resultados negativos são celebrados como aprendizado.

**Exemplo real expandido:** Uma empresa de logística brasileira implementou um sistema de roteirização com IA. O Product Trio passou semanas observando motoristas em campo. Descobriram que o maior problema não era a rota, mas a comunicação com o centro de distribuição. O experimento foi simples: em vez de otimizar a rota primeiro, eles testaram um protótipo de chat entre motoristas e centrais. O protótipo foi construído em poucos dias. Logo a maioria dos motoristas relatou melhora na rotina. O time então redesenhou o sistema para priorizar comunicação, não rota. O dado mais importante? O time aprendeu mais com o fracasso do protótipo inicial de roteirização do que com o sucesso do chat.

**Curiosity gap:** Mas como saber se você está no Nível 4 ou no Nível 5? A resposta está no que o time faz com o fracasso. Se o aprendizado é contínuo e sistêmico, está no Nível 5.

### Nível 5: AI-Native (Refinar)

A empresa inteira entende a estratégia de produto. Qualquer área pode sugerir experimentos. Consumidores são co-criadores.

**O que parece:** "O time de marketing sugeriu um experimento." "O time de RH sugeriu outro." "Os usuários participam das sprint reviews."

**O ponto:** A cultura de produto permeia a organização. Não é responsabilidade de um time, é responsabilidade de todos. A empresa aprende mais rápido porque mais pessoas estão experimentando.

É o nível em que o diferencial deixa de ser planejado e passa a ser descoberto. Anish Acharya, sócio da a16z, resume: moats são descobertos, não projetados. A empresa vira uma série de loops de aprendizado, e a vantagem aparece de onde o time menos espera (Anish Acharya, a16z, Lenny's Podcast, set/2026).

**Exemplo real:** Uma empresa de tecnologia brasileira implementou um programa onde qualquer funcionário pode propor um experimento. O time de facilities sugeriu um chatbot para agendamento de salas de reunião. O time de RH sugeriu um sistema de recomendação de cursos. Ambos foram implementados. O chatbot de salas reduziu o tempo de agendamento de forma visível nas semanas seguintes. O sistema de recomendação de cursos aumentou a conclusão de treinamentos. O dado mais importante? A empresa não precisou de um PM para cada experimento. O time de facilities, com suporte técnico, executou o experimento sozinho.

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

O erro mais comum é implementar na zona red. Times investem em automação que os usuários não querem, porque a tecnologia existe e parece "cool". A Automation Matrix ajuda a evitar esse erro.

## 4. Guia Prático

Você descobriu que seu time está no Nível 2. Ótimo. Agora o que fazer?

### Dia 1-30: Diagnóstico Honesto

1. **Pare de medir o que não importa.** Se você mede accuracy do modelo, pare. Comece a medir satisfação do usuário.
2. **Entreviste 5 clientes que usaram seu produto.** Não use roteiro. Pergunte: "O que você estava tentando fazer quando usou essa feature?" "O que aconteceu?" "Como você se sentiu?"
3. **Mapeie onde cada atividade do seu time cai na Automation Matrix.** Identifique a zona red. Pare de implementar lá.

### Dia 31-60: Intervenção Estruturada

1. **Escolha um nível para subir.** Se você está no Nível 2 (Feature Factory), não tente pular para o Nível 4 (Product Operating Model). Implemente um ritual semanal de discovery: 2 horas com usuários reais, sem roteiro fixo.
2. **Crie um sistema de pesquisa contínua.** Entreviste 2 clientes por semana. Registre tudo em um documento compartilhado.
3. **Transforme seu roadmap de lista de features em lista de hipóteses.** Em vez de "Construir chatbot", escreva "Testar se chatbot reduz tempo de atendimento sem aumentar reclamações".

### Dia 61-90: Validação e Ajuste

1. **Forme um Product Trio.** PM, Designer, Engenheiro. Dê autonomia para decidir o que construir.
2. **Implemente experimentação diária.** Teste uma hipótese por semana. Não precisa ser A/B. Pode ser um protótipo, uma entrevista, um teste de usabilidade.
3. **Meça se o ritual mudou as decisões.** O time está priorizando com base em dados de uso ou ainda por "quem grita mais alto"? Se a resposta for a segunda, repita o ciclo.

## 5. Métricas de Sucesso

Para saber se você está subindo de nível, meça três categorias:

### Valor para Usuário

- satisfação de produto: deve subir de forma consistente, mês a mês.
- Taxa de adoção: Percentual de usuários que usam a feature pelo menos uma vez por semana.
- Satisfação de tarefa: "Conseguiu fazer o que queria?" Sim/Não.

### Valor para Negócio

- Custo de atendimento: deve cair conforme a automação amadurece.
- Tempo de resolução: deve cair conforme a automação amadurece.
- Retenção de clientes: deve subir conforme a experiência melhora.

### Qualidade de Implementação

- Nível de maturidade (auto-avaliação): o time deve subir de nível de forma sustentada, sem pular degraus.
- Autonomia do time: Percentual de decisões tomadas pelo Product Trio, não pela liderança.
- Ciclo de aprendizado: Tempo entre formular uma hipótese e saber se ela está certa ou errada. Deve encolher de meses para semanas.

### Metas Específicas para 90 Dias

- Redução no tempo de ciclo de descoberta (da hipótese ao experimento).
- Aumento na proporção de decisões baseadas em dados de usuário (versus opinião interna).
- NPS de atendimento digital em alta, comparado ao ponto de partida registrado no diagnóstico.
- Zero features lançadas sem experimento prévio após 90 dias.

## 6. Fechamento com Gancho

Você sabe onde está. Sabe para onde quer ir. Sabe como medir se está chegando.

Mas tem um problema.

Você pode fazer tudo certo e ainda assim falhar. Porque o maior obstáculo não é técnico. Não é de processo. Não é de métrica. O maior obstáculo é a AI Trap.

A armadilha que faz times competentes construírem soluções que ninguém quer. A armadilha que transforma orçamento de produto em um chatbot que ninguém usa. A armadilha que faz você achar que está no Nível 4 quando está no Nível 2.

No próximo capítulo, vamos explorar essa armadilha. Os 7 sinais que indicam que você está caindo nela. E o mais importante: como sair antes que seja tarde demais.

Porque não adianta saber onde você está se você não sabe como evitar o buraco no caminho.

**[gap-ai-trap-early-warning]:** Como saber se estou caindo na AI Trap antes de perder meses de trabalho?

---

# PARTE II: DECISÃO. O que fazer?

> *Com o diagnóstico em mãos: construir, comprar, usar API ou open-source? E quanto custa?*

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

Antes de seguir, um contraponto que pouca gente faz. A adoção dispara, mas o dinheiro ainda não apareceu. Daron Acemoglu, Nobel de Economia do MIT, aponta o que as manchetes escondem: a IA ainda não aparece nos números de produtividade agregada da economia. O podcast "AI Is Not Improving Productivity", da MIT Sloan Management Review, resume a tese dele. Todo mundo adota. Quase ninguém comprova ganho real. É nesse descompasso que o Custo Oculto nasce (Daron Acemoglu, Nobel de Economia, MIT Sloan, Me Myself and AI, 2026).

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

Exemplo fictício, retomando a cena de abertura deste capítulo.

### Caso 4: A otimização míope, padrão que se repete

Nem todo Custo Oculto vem de número errado. Às vezes vem de número certo medido no lugar errado. Um time otimiza uma métrica só, como tempo de entrega ou taxa de conversão, e esquece o resto do sistema. A métrica escolhida sobe. O negócio piora. Parceiro sobrecarregado de um lado, cliente abandonando do outro. É o custo de otimização míope que descrevi na definição do problema: você melhora uma dimensão e cobra do todo.

A lição é a mesma do imposto de integração. Otimizar uma métrica sem olhar o ecossistema inteiro não é otimizar. É transferir o custo para outro lugar, fora do dashboard. Antes de melhorar qualquer número, pergunte: que métrica eu estou ignorando de propósito? Se a resposta for "nenhuma", você ainda não está vendo o sistema.

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
| **Custo total mensal** | Soma das linhas acima | R$ ________ |
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
| **Custo total** | **R$ 16.500/mês** |
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

O que paga conta é métrica conectada a resultado de negócio. Enquanto a IA não aparecer nos números de produtividade que Acemoglu observa, toda promessa de ganho continua sendo promessa. E isso, ninguém te ensina na faculdade.

No próximo capítulo, vamos explorar o outro lado da moeda: como construir uma cultura de produto de IA que sustenta essas métricas. Porque métrica sem cultura é só número. E número sem ação é só ruído.

---

# PARTE III: TIME. Quem faz?

> *Quem fica, quem sai, quem se transforma, e o que o PM vira nesse mundo novo.*

# Capítulo 5: Quem Fica, Quem Sai, Quem Se Transforma

## Seção 1: Cena de Abertura

Tom Verrilli, CPO do Whatnot, soltou uma frase que todo PM deveria ouvir em pé: "we regret that product management exists". Arrependemo-nos de que product management exista. Não é provocação de quem despreza a função. É diagnóstico de quem recebeu 31.832 candidaturas para uma vaga de PM e percebeu que a função, do jeito que foi desenhada, não é mais o que o trabalho pede (Tom Verrilli, CPO do Whatnot, Lenny's Podcast, ago/2026).

Quando 31.832 pessoas disputam uma cadeira, o problema não é falta de talento. É sinal de que a cadeira está mal definida. Candidato demais para uma função que já não tem dono claro.

Do outro lado da mesa está Dianne Penn, primeira PM técnica da Anthropic. Ela descreve outra coisa: o desenvolvimento dirigido por evals, a jagged edge, o ponto em que o modelo é forte de um jeito e fraco de outro sem aviso prévio. E, no meio dessa irregularidade, o lugar onde o julgamento humano continua insubstituível (Dianne Penn, Anthropic, Lenny's Podcast, jul/2026).

Os dois estão falando da mesma mudança, de lados opostos. Verrilli aponta quem sai: a camada de PM que só intermedia. Penn aponta quem fica: o julgamento que nenhuma avaliação automática cobre.

O capítulo anterior mostrou que discovery com IA é não-determinística. Aqui a pergunta é outra: que time faz essa discovery? Quem fica, quem sai, quem se transforma.

## Seção 2: Definição do Problema

O problema não é técnico. É de design organizacional.

Times de produto foram desenhados para um mundo determinístico. O PM escrevia PRD detalhado, o engenheiro implementava exatamente o que estava no PRD, o QA testava se a implementação correspondia ao PRD. Tudo linear, previsível, controlável.

Agora o produto é probabilístico. O PRD diz "o chatbot deve entender intenções", mas entender intenções não é binário. É uma distribuição de probabilidade. E o modelo erra de um jeito que irrita profundamente, em pontos que ninguém previu. É a jagged edge da qual Penn fala: o modelo é ótimo numa tarefa e péssimo na tarefa vizinha, sem aviso.

O time ainda opera como se fosse 2019. Ninguém tem a responsabilidade de perguntar "e se o modelo acertar quase tudo e errar justamente onde dói?"

Três arquétipos de PM em 2026:

**O Tradutor (vai sair)**: o valor era escrever PRDs detalhadas e traduzir negócio para tech. IA faz isso em segundos. Modelos como Claude 3.5 Sonnet geram documentos estruturados a partir de prompts simples (Anthropic, "Claude 3.5 Sonnet Model Card", mar/2024). Se seu diferencial é "saber escrever documento técnico", você já foi substituído. Verrilli é mais duro: "we regret that product management exists", porque a versão intermediária dessa função virou uma camada que não agrega (Tom Verrilli, CPO do Whatnot, Lenny's Podcast, ago/2026).

**O Operador (vai se transformar)**: sabe usar ferramentas de IA mas não tem julgamento estratégico. Faz mais tarefas, mas as tarefas continuam operacionais. 58% dos PMs em empresas de tecnologia usam IA generativa semanalmente, segundo o Product School State of Product Management Report 2024 (out/2024). Só 12% dizem que isso mudou sua atuação estratégica (mesma fonte). Usar a ferramenta não é o diferencial. Decidir o que a ferramenta não deve tocar, é.

**O Orquestrador (vai ficar)**: entende de estratégia, contexto de negócio e taste, e orquestra agentes como membros do time. Sabe definir o que não automatizar. Sabe quando o julgamento humano continua insubstituível, exatamente o território que Penn mapeia (Dianne Penn, Anthropic, Lenny's Podcast, jul/2026).

Vagas para AI Product Manager cresceram 82% ao ano entre 2023 e 2024, segundo o LinkedIn Global Talent Trends 2025 (jan/2025). Mas o que essas vagas pedem? Não é "saber usar ChatGPT". É "saber definir o que não automatizar". É "tomar decisão com informação incompleta". É julgamento contextual.

E Verrilli recebeu 31.832 candidaturas para uma vaga desse tipo. A maioria não passaria. Por quê? Porque a maioria foi formada para o mundo determinístico que está acabando.

## Seção 3: Framework / Componentes

### THA: Trio Humano-Agente (Human-Agent Trio)

Três papéis que todo time de produto com IA precisa ter, independente do tamanho da empresa. Não importa se você é uma startup de 10 pessoas ou uma empresa com 10 mil. Esses três papéis existem. A questão é se você os reconhece e os desenha conscientemente, ou se eles emergem no caos e você descobre tarde demais que faltou um.

---

### Componente 1: O Explorador (Agente de IA)

**O que faz:** Gera hipóteses o tempo todo. Analisa padrões em dados não-estruturados. Conduz avaliações em escala. Identifica anomalias que nenhum humano teria paciência de encontrar.

O Explorador é a versão contínua do que Penn descreve como desenvolvimento dirigido por evals: em vez de esperar uma reclamação chegar, você roda avaliações de forma sistemática para achar onde o modelo falha (Dianne Penn, Anthropic, Lenny's Podcast, jul/2026). O agente não sabe o que fazer com esses padrões. Ele só os encontra. A limitação é clara: não tem contexto de negócio, não sente pele no jogo, não distingue correlação de causalidade. "Usuários que compram de madrugada reclamam mais" pode ser transportadora pior, usuário mais ansioso, ou delay no rastreio. O agente não sabe. Ele só encontra.

**O risco:** Sem Explorador, seu time opera no escuro. Você depende de intuição, de reclamações que chegam ao CEO, de dados que alguém teve tempo de puxar. Com Explorador, você tem hipóteses demais. O problema passa a ser outro: escolher.

**Dado:** O ponto fraco do Explorador é o mesmo da jagged edge que ele tenta mapear. Ele encontra padrões, mas não sabe quais importam. Muitos dos padrões identificados serão irrelevantes ou falsos positivos. É por isso que ele não decide sozinho.

---

### Componente 2: O Validador (Humano PM)

**O que faz:** Define quais hipóteses merecem ser testadas. Aplica julgamento contextual. Sente o mercado. Toma decisão com informação incompleta.

O Validador não precisa saber programar. Não precisa ajustar hiperparâmetros. Precisa saber uma coisa: taste.

Taste é a capacidade de olhar para dezenas de padrões e dizer "esses três importam, e aqui está o porquê". Quando todo mundo tem acesso aos mesmos modelos, o diferencial não é a tecnologia. É o julgamento sobre o que construir.

É aqui que Penn aponta o que continua insubstituível. A jagged edge significa que você não consegue prever onde o modelo vai falhar. Só testando, e só alguém com contexto julga se a falha importa ou não (Dianne Penn, Anthropic, Lenny's Podcast, jul/2026). O modelo acerta, o modelo erra, e decidir se o erro é tolerável é tarefa humana.

**O que está em jogo:** Sem Validador, seu time vira um gerador de hipóteses sem direção. Você implementa tudo que o agente sugere e termina com um produto inchado que tenta resolver dezenas de problemas ao mesmo tempo. O Validador é o guardião do foco.

**Dado:** Não existe métrica que substitua esse julgamento. Verrilli viu isso do ângulo do recrutamento: de 31.832 candidaturas, o que separa quem serve de quem não serve não é domínio de ferramenta, é julgamento (Tom Verrilli, CPO do Whatnot, Lenny's Podcast, ago/2026).

---

### Componente 3: O Sintetizador (Híbrido Humano-Agente)

**O que faz:** Reuniões de síntese onde o agente apresenta descobertas, o humano questiona, e os dois decidem os próximos passos. O Sintetizador não é um papel separado: é o momento em que Explorador e Validador se encontram para decidir.

O formato é simples: um Agent Briefing semanal de 30 minutos. O agente envia um relatório antes. O humano chega com perguntas. A decisão é tomada em conjunto.

Na prática, funciona assim: na segunda-feira, o agente envia a análise. "Identifiquei 12 padrões novos. Oito são consistentes com dados históricos, três são inconsistentes, um é ambíguo. Recomendo investigar os três inconsistentes."

Na terça-feira, o PM chega para a reunião. "Agente, por que você classificou o padrão X como inconsistente?" Agente: "Porque contradiz o padrão Y da semana passada." PM: "E se a mudança no algoritmo de recomendação da semana passada tiver alterado o comportamento do usuário?" Agente: "Não considerei essa variável. Vou recalcular."

**A armadilha:** Nenhum dos dois, sozinho, decide bem. O agente tem dados sem contexto. O humano tem contexto sem dados. Juntos, eles sintetizam. É o ponto em que o julgamento humano insubstituível de Penn se encontra com a varredura contínua de evals.

**Dado:** O que Verrilli quer dizer com senior ICs fazendo o trabalho de verdade é exatamente isso: o trabalho de verdade é a síntese e o julgamento, não a intermediação (Tom Verrilli, CPO do Whatnot, Lenny's Podcast, ago/2026).

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

### Caso 1: Whatnot (Tom Verrilli)

**Situação:** Tom Verrilli, CPO do Whatnot, recebeu 31.832 candidaturas para uma vaga de PM. A reação dele não foi satisfação. Foi "we regret that product management exists" (Tom Verrilli, CPO do Whatnot, Lenny's Podcast, ago/2026).

**O que estava errado:** A função PM acumulou uma camada de intermediação. Em vez de construir ou decidir, o PM passou a traduzir, repassar, consolidar. Verrilli aponta que o trabalho de verdade é feito por senior ICs, os profissionais que constroem e decidem, enquanto a camada de PM se ocupou de atividade que não agrega.

**A lição:** O cargo some quando a contribuição vira só intermediação. Quem faz o trabalho de verdade fica. Quem só repassa o trabalho de verdade, sai. É a versão recrutamento do THA: Explorador varre, Validador julga, e a camada do meio que só traduz não tem papel em nenhum dos três.

### Caso 2: Anthropic (Dianne Penn)

**Situação:** Dianne Penn, primeira PM técnica da Anthropic, descreve o desenvolvimento dirigido por evals. Antes de lançar, a equipe define avaliações que medem onde o modelo acerta e onde falha. O processo expõe a jagged edge: o modelo é forte numa tarefa e fraco na tarefa ao lado, sem que ninguém consiga prever de antemão (Dianne Penn, Anthropic, Lenny's Podcast, jul/2026).

**O que estava errado:** A suposição de que dá para prever o comportamento do modelo. Não dá. A irregularidade é a regra. Quem espera um modelo comportado se surpreende em produção.

**A lição:** É o Validador em estado puro. Os evals encontram onde o modelo erra. O julgamento humano decide se o erro importa. Nenhuma avaliação automática cobre essa decisão. É o que Penn marca como o lugar onde o julgamento continua insubstituível.

---

## Seção 5: O gerente-informante acabou

Existe uma figura que o THA elimina sem piedade: o gerente cuja função principal é consolidar informação e repassar. Aquele middle manager que passa boa parte do tempo em reuniões de status, compilando slides do que o time fez, traduzindo métrica de engenharia pra linguagem de negócio.

Esse papel some. Não porque é substituído por IA. Porque nunca deveria ter existido. Verrilli, com "we regret that product management exists", aponta para esse buraco: a função virou intermediação, e a intermediação é exatamente o que os agentes e os senior ICs já cobrem (Tom Verrilli, CPO do Whatnot, Lenny's Podcast, ago/2026).

Quando o agente documenta o que foi decidido, quando o dashboard mostra o throughput do time em tempo real, quando o Sintetizador já conecta métrica técnica a métrica de negócio, o gerente-informante perde a função. Ele não agrega. Ele repassa.

**Como saber se você (ou alguém do seu time) é um gerente-informante:**

- Sua principal contribuição em reuniões é "deixa eu ver isso e te retorno"
- Você passa mais tempo compilando informação do que tomando decisão
- Seu time funcionaria igual (ou melhor) sem você por duas semanas
- Você não consegue nomear três decisões reversíveis que tomou este mês

Se três de quatro forem verdade, você é um gerente-informante. E tem alguns meses para virar Orquestrador, ou seu cargo some.

**O que vira no lugar:** Quem era gerente-informante tem dois caminhos. Virar Orquestrador (assumir ownership de decisão, gerenciar o sistema híbrido humano-agente) ou virar Explorador sênior (profundidade técnica em vez de amplitude gerencial). O que não dá é ficar no meio. O meio é exatamente a camada que Verrilli lamenta que exista.

---

## Seção 6: THA para times pequenos (3 a 10 pessoas)

"Tá, Fernanda, mas eu tenho três pessoas no meu time. Como aplico THA?"

A resposta: você acumula. O framework não exige três pessoas diferentes, exige três funções diferentes. Em time pequeno, uma pessoa cobre mais de uma.

**Time de três pessoas (PM + dois devs):**

- **PM** = Sintetizador + metade do Explorador (entrevistas, contexto externo)
- **Dev 1** = Validador de hipóteses + metade do Explorador (experimentação, prototipação)
- **Dev 2** = Validador de implementação + agente de documentação
- **Agente** cobre: documentação de decisões, análise de dados exploratória, PRDs iniciais

**Time de uma pessoa (founder solo):**

- **Você** = os três papéis. Mas o agente vira seu Validador (roda experimentos enquanto você dorme) e seu Sintetizador (compila insights de entrevistas).
- **Rotina diária:** duas horas como Explorador (entrevistas, dados), duas horas como Sintetizador (decisões, priorização), quatro horas como Validador (prototipação).
- **Agente** cobre: transcrição de entrevistas, geração de hipóteses alternativas, análise de competidores, documentação automática.

**Rituais enxutos (time com menos de cinco pessoas):**

- **Daily de 15 min:** o que o agente produziu, o que cada humano vai validar, uma decisão.
- **Semanal de 60 min:** revisão de hipóteses descartadas (celebre o que você não construiu).
- **Mensal de 90 min:** recalibragem dos papéis THA (quem está sobrecarregado? o agente precisa de regras novas?).

Em time pequeno, o agente não é "mais um membro". É o multiplicador de força que deixa três pessoas operarem como seis.

---

## Seção 7: Guia prático, 30/60/90 dias

Como implementar o THA no seu time. Use a lógica que Verrilli e Penn apontam como fio condutor: corte a intermediação, reconstrua em volta do julgamento.

### Dias 1 a 30: Diagnóstico e Estruturação

**Semana 1:** Mapeie seu time. Quem faz o papel de Explorador? Quem faz o de Validador? Quem faz o de Sintetizador? Se alguém acumula mais de um papel, é sinal de alerta.

**Semana 2:** Configure o agente de IA (Explorador). Comece com uma fonte de dados específica: logs de suporte, feedback de usuários, dados de uso. Defina o que o agente deve procurar: padrões de reclamação, anomalias, oportunidades. É o desenvolvimento dirigido por evals que Penn descreve, aplicado ao seu produto.

**Semana 3:** Treine o time no papel de Validador. Aprenda a questionar os dados do agente. "Por que esse padrão importa?" "Qual o contexto de negócio?" "O que mais poderia explicar esse padrão?" Faça o exercício de pegar três hipóteses do agente e forçar uma explicação alternativa para cada uma.

**Semana 4:** Rode o primeiro Agent Briefing. Trinta minutos, uma vez por semana. O agente envia o relatório antes. O PM chega com perguntas. A decisão é documentada.

### Dias 31 a 60: Validação e Aprendizado

**Semana 5 a 6:** Ajuste o agente com base no feedback. Gerando hipótese irrelevante demais? Ajuste os parâmetros. Perdendo padrão importante? Expanda as fontes. O objetivo é estreitar a jagged edge: saber onde o agente é confiável e onde não é.

**Semana 7 a 8:** Ative o Validador. Teste as hipóteses mais promissoras numa amostra pequena antes de escalar.

**Semana 9 a 10:** Ative o Sintetizador. Decida o que escalar com dados + contexto de negócio. Nem sempre a hipótese de maior impacto é a certa, se o custo e o momento não ajudam.

### Dias 61 a 90: Decisão e Escala

**Semana 11 a 12:** Documente o processo. Crie um playbook do THA para o seu time. Inclua: como configurar o agente, como conduzir o Agent Briefing, como decidir em conjunto.

**Semana 13 a 14:** Defina as métricas de sucesso. Tempo de ciclo de hipótese. Taxa de hipóteses que viram implementação. Engajamento do time.

**Semana 15 a 16:** Apresente o antes e depois para a liderança. Peça autorização para expandir o modelo para outros times.

---

## Seção 8: Métricas de sucesso do time híbrido

Como saber se seu time híbrido funciona? Não é pela accuracy do modelo. É por métricas de resultado do sistema completo.

### Métricas para o Explorador (Agente de IA)

- **Hipóteses geradas por semana:** se o agente gera pouco, ajuste os parâmetros. Se gera muito mas irrelevante, refine o filtro.
- **Diversidade de fontes das hipóteses:** usuários, dados, time, concorrência? Se tudo vem de uma fonte, algo está errado.
- **Taxa de hipóteses que passam para validação:** se muito alta, o filtro está frouxo. Se muito baixa, o agente gera ruído.

### Métricas para o Validador (Humano PM)

- **Hipóteses validadas vs. implementadas:** se o PM valida mas não implementa, a priorização está errada.
- **Tempo médio de ciclo de validação:** se demora demais, o processo está emperrado.
- **Custo por experimento:** se o custo não cai, o time não está aprendendo.

### Métricas para o Sintetizador (Híbrido)

- **Tempo médio de decisão:** se demora demais, a síntese está quebrada.
- **Taxa de decisões com impacto positivo mensurável:** se baixa, as decisões estão erradas.
- **Número de decisões revertidas:** se nunca reverte, está com medo de errar. Se reverte demais, está precipitado.

### Métricas de resultado final

- **NPS do produto com IA:** se o NPS não melhorar, nada mais importa.
- **Taxa de resolução na primeira interação:** medida de eficácia real, não de performance técnica.
- **Percentual de usuários pedindo humano:** se sobe, seu time híbrido está falhando.
- **NPS do time:** se cair, algo está errado.

### Métricas que não importam (sozinhas):

- Accuracy do modelo
- Precisão e recall
- Tempo de inferência
- Número de features implementadas

---

## Seção 9: Fechamento com gancho

Se você chegou até aqui, já sabe que o time de produto com IA não é um time tradicional com uma ferramenta nova. É uma estrutura nova, com papéis novos e métricas novas.

Verrilli resumiu o lado de fora: "we regret that product management exists", porque a versão intermediária da função parou de agregar. Penn resumiu o lado de dentro: na jagged edge, onde o modelo falha sem avisar, o julgamento humano continua insubstituível. Os dois, juntos, desenham a fronteira exata de quem fica e quem sai.

O que ainda não respondemos: como esse time decide o que construir? Com dezenas de hipóteses por semana, como priorizar sem enlouquecer? Essa é a pergunta que o Capítulo 9 responde.

Mas antes, uma pausa. Respira. O próximo capítulo é sobre métricas. E não, não é sobre accuracy.

# Capítulo 6: O PM na Era dos Agentes: o que muda, o que some, o que nasce

---

## Seção 1: Abertura

Tom Verrilli, CPO do Whatnot, disse em público uma frase que PM nenhum quer ouvir: "we regret that product management exists" (Tom Verrilli, CPO do Whatnot, Lenny's Podcast, ago/2026).

A frase é provocação, mas esconde um problema real. O Whatnot recebeu 31.832 candidaturas de PM. Para Verrilli, o volume expõe o inchaço do cargo: gente demais escrevendo documento e de menos fazendo o trabalho de verdade. Quando ele olha para os senior ICs, vê quem entrega de fato. O cargo de PM, na leitura dele, sobrou.

Do outro lado, Tara Seshan, PM lead do ChatGPT Work na OpenAI, descreve a saída. A virada é de remar para dirigir (Tara Seshan, OpenAI, Lenny's Podcast, ago/2026). Quando executar vira commodity, o gargalo deixa de ser capacidade de fazer. Vira ambição. O PM deixa de ser quem empurra a tarefa e passa a elevar a ambição dos outros.

Os dois estão falando da mesma virada, de ângulos opostos. Verrilli ataca o PM que só rema. Seshan descreve o PM que aprendeu a dirigir.

A pergunta deste capítulo: se executar virou commodity, qual o papel do humano no time híbrido? E do PM?

---

## Seção 2: Definição do problema

"O que acontece quando metade do seu time não é humano?"

Essa pergunta parece futurista, mas já é realidade. Times de produto estão cada vez mais híbridos. Humanos e agentes trabalham lado a lado. O problema não é como contratar mais pessoas de IA. É como redesenhar o time quando metade dos membros não são humanos.

**O mito do time aumentado.** Muitas empresas acham que basta adicionar um data scientist ou comprar uma ferramenta de IA. O resultado é o caos de papéis: quem decide o que o agente faz? Quem valida as sugestões? Quem responde quando humano e agente discordam?

O framework Product Trio (PM, designer, engenheiro) funciona bem quando todos são humanos. Mas quando um agente entra no time, o trio vira quarteto. E o quarteto precisa de regras.

**Os 3 erros comuns na montagem de times híbridos:**

1. **Tratar agente como ferramenta.** Agente não é calculadora. Ele sugere, analisa, decide. Se você trata como ferramenta, perde o potencial. Mas se trata como humano sem papéis, vira bagunça.

2. **Não definir critérios de julgamento para quando humano e agente discordam.** O agente diz uma coisa, o humano diz outra. Quem ganha? Depende. Mas se não está definido, o time trava.

3. **Manter métricas tradicionais que não capturam a dinâmica humano-agente.** Velocidade de entrega, número de features. Essas métricas não dizem se o agente está ajudando ou atrapalhando.

No capítulo anterior, o THA (trio humano-agente) mostrou que humano e agente decidem melhor juntos do que separados. Agora o problema é outro: como escalar isso para um time inteiro. Métricas tradicionais não funcionam para IA. Times tradicionais também não funcionam.

O que este capítulo resolve: um framework para redesenhar times de produto na era dos agentes, com papéis claros, princípios de decisão e métricas específicas.

---

## Seção 3: O que o PM deixa de fazer

Antes de falar do que o PM vira, precisamos falar do que ele deixa de ser. A parte mais difícil da transformação não é aprender o novo. É largar o velho.

Aqui está o que some do seu dia a dia:

**1. Microgerenciar tarefas repetitivas.** O agente escreve o primeiro draft do PRD. O agente compila as métricas do sprint. O agente documenta as decisões da reunião. Seu trabalho não é fazer, é revisar o que o agente fez e decidir se está bom. Você para de ser produtor e vira curador.

**2. Ser o único validador de output.** Antes, toda feature passava pelo PM antes de ir para produção. Agora, o agente valida critérios objetivos (testes passam? métricas dentro do range?) e só escala para o PM quando há ambiguidade. Você para de ser gargalo e vira exceção.

**3. Priorizar sozinho com intuição pura.** O agente sugere priorização baseada em dados (impacto estimado, esforço, risco, dependências). Você ainda decide, mas com o agente mostrando o que os dados dizem. Você para de decidir no escuro e vira decisor informado.

**4. Descobrir problemas sozinho.** O agente monitora métricas o tempo todo, detecta anomalias, sugere hipóteses. Você não precisa mais descobrir que o NPS caiu, o agente te avisa. Você para de ser detetive e vira investigador sênior: o agente acha a cena do crime, você resolve o caso.

**5. Escrever tudo do zero.** PRDs, briefings, relatórios de status, e-mails de alinhamento. O agente gera o primeiro draft. Você edita. Seu tempo de escrita despenca. Você para de ser redator e vira editor.

Isso é exatamente a virada que Seshan descreve: de remar para dirigir (Tara Seshan, OpenAI, Lenny's Podcast, ago/2026). Se você se reconheceu em três ou mais desses itens, seu trabalho já mudou. Você só não percebeu ainda.

---

## Seção 4: PM Brain OS, seu sistema operacional de produto

O PM Brain OS é o que roda na sua cabeça e na do agente. Três componentes.

### Kernel: as regras que nunca mudam

O kernel é o que o agente não decide. São regras que você define uma vez e recalibra a cada trimestre:

- **Visão é humana.** O agente executa. O porquê é sempre humano.
- **Trade-offs de usuário são humanos.** Se a decisão afeta a experiência de um cliente, um humano decide.
- **Risco é escalado.** Se o agente detecta que uma decisão tem potencial de gerar dano (financeiro, reputacional, legal), ele não decide. Escala.

### Regras de autonomia: os 5 níveis de liberdade do agente

| Nível | Nome | O agente... | Exemplo |
|-------|------|-------------|---------|
| L0 | Observador | Só coleta dados, não age | Monitora NPS, alerta se cair |
| L1 | Sugestor | Propõe ação, humano aprova | "Recomendo responder cliente X com template Y" |
| L2 | Executor com validação | Age, humano revisa depois | Responde cliente, PM vê relatório semanal |
| L3 | Executor autônomo | Age, reporta se anomalia | Responde cliente, só alerta se detecta raiva |
| L4 | Decisor delegado | Decide dentro de política, escala exceções | Define desconto até R$ 50, acima disso escala |

Cada agente do seu time opera em um nível diferente. O agente de suporte pode estar em L3. O agente de pricing, em L1. Você define.

### Memória compartilhada: o que o agente precisa saber

Sem contexto, o agente é só um modelo de linguagem. Com contexto, ele é um teammate. A memória compartilhada tem quatro camadas:

- **Contexto de produto:** visão, OKRs do trimestre, personas, jornadas críticas.
- **Contexto de decisão:** as últimas dez decisões que você tomou e por quê.
- **Contexto de time:** quem é responsável por quê, férias, capacidade do sprint.
- **Contexto de cliente:** feedback recente, tickets abertos, NPS por segmento.

Isso não é um documento, é um sistema. No Capítulo 8, você vai ver como operacionalizar essa memória compartilhada com rituais e ferramentas. Por enquanto, entenda o conceito: o agente é tão bom quanto o contexto que você dá para ele.

---

## Seção 5: HAT Model, os papéis que operacionalizam o PM Brain OS

Com o sistema operacional definido, o HAT Model (Human-Agent Team) organiza quem faz o quê.

"Como estruturar um time onde humanos e agentes têm papéis complementares, não concorrentes?"

A resposta é o HAT Model. São cinco papéis que todo time híbrido precisa ter, independentemente do tamanho.

### Os 5 papéis do HAT Model

**Papel 1: Strategist**

*Quem faz:* humano (PM).

*O que faz:* define o porquê e o para quem. Não delega visão. O agente pode sugerir, mas não decide o rumo.

*Na prática:* é a ambição de que Seshan fala. O Strategist não empurra tarefa, eleva o nível do que o time quer construir.

*A aposta:* se o agente decide a visão, você perde o controle estratégico. O PM é o guardião da visão.

**Papel 2: Executor**

*Quem faz:* agente.

*O que faz:* executa tarefas repetitivas, analisa dados, gera variações. Onde o humano perde tempo, o agente ganha.

*Por que isso muda o jogo:* o agente libera o humano para o que importa. Mas só funciona se o Executor tem limites claros.

**Papel 3: Validator**

*Quem faz:* humano (designer ou engenheiro).

*O que faz:* valida outputs do agente antes de ir para produção. O agente sugere. O humano aprova ou rejeita.

*O custo de errar:* sem validação, o agente erra. E quando erra, erra em escala.

**Papel 4: Escalator**

*Quem faz:* humano (PM ou engenheiro).

*O que faz:* decide quando o agente não resolve e o humano entra. O agente tem um limite de autonomia. Quando atinge, sobe para o humano.

*Por que importa:* nem tudo pode ser automatizado. O Escalator é o ponto de falha seguro.

**Papel 5: Learner**

*Quem faz:* ambos (humano e agente).

*O que faz:* ciclo de feedback contínuo. O agente aprende com o humano. O humano aprende com o agente.

*O ponto:* time híbrido que não aprende junto é time que estagna.

### Os 3 princípios de funcionamento do HAT Model

1. **Clareza de domínio.** Cada papel sabe exatamente o que pode e o que não pode fazer. O agente não sugere features sem validação do Strategist. O humano não microgerencia tarefas do Executor.

2. **Autonomia progressiva.** O agente começa com pouca autonomia. Conforme mostra resultados, ganha mais. Mas nunca sem supervisão.

3. **Feedback bidirecional.** O humano ensina o agente. O agente ensina o humano. Não é via de mão única.

---

## Seção 6: Casos reais: Seshan e Verrilli

Dois pontos de vista reais sobre o mesmo cargo. Um de dentro da OpenAI, outro de um CPO que duvida do cargo.

### Caso 1: Tara Seshan, OpenAI, remar para dirigir

Tara Seshan é PM lead do ChatGPT Work na OpenAI. Ela descreve a virada que o cargo precisa dar: de remar para dirigir (Tara Seshan, OpenAI, Lenny's Podcast, ago/2026).

A lógica é simples. Quando a execução vira commodity, remar deixa de ser diferencial. Qualquer agente rema. O que falta é quem define para onde remar. É aí que entra o PM.

Na leitura dela, o gargalo do time muda de lugar. Antes era capacidade: não dava tempo de fazer tudo. Agora é ambição: não dá para subir o nível do que se quer construir. O PM deixa de ser quem faz e vira quem eleva a ambição dos outros.

Isso não é abstração. É o kernel do PM Brain OS: visão é humana. O agente executa, o porquê é sempre humano.

### Caso 2: Tom Verrilli, Whatnot, o CPO que duvida do cargo

Tom Verrilli é CPO do Whatnot. Ele é o contraponto duro. A frase dele: "we regret that product management exists" (Tom Verrilli, CPO do Whatnot, Lenny's Podcast, ago/2026).

A dor por trás da frase: o Whatnot recebeu 31.832 candidaturas de PM. Para Verrilli, isso é sintoma de um cargo inchado. Gente demais produzindo processo e documento, gente de menos fazendo o trabalho de verdade. Ele aponta para os senior ICs como quem entrega de fato.

Verrilli não está contra o PM em si. Está contra o PM que só rema, o PM que vira intermediário de informação, o PM que consolida slide. Esse cargo, para ele, não se justifica.

Junte os dois e o capítulo se resolve. Verrilli descreve o PM que morreu: o que rema. Seshan descreve o PM que nasce: o que dirige. O HAT Model é o mapa para sair de um e chegar ao outro.

---

## Seção 7: Guia prático 30/60/90

"Bora colocar a mão na massa. Aqui está o plano de 30, 60 e 90 dias para redesenhar seu time híbrido."

### Dias 1 a 7: mapeie o cenário atual

- **Mapeie seu time atual.** Liste todos os humanos e agentes envolvidos. Para cada agente, responda: o que ele faz? Quem valida? Quem decide quando ele erra?
- **Identifique o caos de papéis.** Pergunte para cada membro do time: "Você sabe exatamente o que pode e o que não pode fazer?" Se a resposta for "mais ou menos", você tem um problema.
- **Defina o Strategist.** Quem é o PM ou líder que define a visão? Se não tiver, defina. Esse papel não pode ser delegado ao agente.

### Dias 8 a 30: implemente os papéis do HAT Model

- **Atribua os 5 papéis.** Para cada agente, defina quem é o Executor, o Validator, o Escalator e o Learner. Documente em um quadro visível para todo o time.
- **Estabeleça critérios de julgamento para discordâncias.** Crie uma matriz de decisão: quando humano e agente discordam, quem decide? Exemplo: se a sugestão do agente impacta a experiência do usuário, o designer decide. Se impacta a arquitetura técnica, o engenheiro decide.
- **Crie o ciclo de feedback inicial.** Implemente um sistema simples: botão de "útil" e "inútil" para cada sugestão do agente. Nada complexo. Só comece.

### Dias 31 a 60: estabeleça o ciclo de aprendizado

- **Meça os primeiros resultados.** Use as métricas do AI Team Health Score (veja a seção 8). Foco em taxa de aceitação de sugestões e tempo de validação.
- **Ajuste a autonomia do agente.** Se o agente mostra consistência, aumente a autonomia. Se erra, reduza. O princípio é progressivo, não binário.
- **Treine o time.** Todo mundo precisa entender os novos papéis. Não adianta só definir. Tem que ensinar. Faça uma sessão de uma hora por semana para alinhar.

### Dias 61 a 90: escale e refine

- **Revise a autonomia progressiva.** O agente ganhou mais autonomia nos últimos três meses? Se não, o modelo não está escalando. Ajuste.
- **Documente o modelo.** O que funcionou? O que não funcionou? Crie um playbook para o próximo time. Inclua exemplos de discordâncias e como foram resolvidas.
- **Compartilhe com outros times.** O HAT Model não é segredo. Quanto mais times usarem, mais aprendizado coletivo.

O guia é concreto. Não é "monte um time de IA". É "aqui estão os passos exatos". Faça.

---

## Seção 8: Métricas de sucesso

"Se métricas tradicionais não funcionam, o que colocar no lugar?"

A resposta é o AI Team Health Score. Três dimensões. Nove métricas.

### Dimensão 1: valor para o usuário

- **Taxa de aceitação de sugestões do agente.** Quantas vezes o usuário aceita o que o agente sugere? Acima de 70% é saudável. Abaixo de 40%, o agente não está ajudando.
- **Tempo de validação humana.** Quanto tempo o humano leva para validar ou rejeitar uma sugestão do agente? Idealmente, menos de duas horas. Se passa de 24 horas, o gargalo não é o agente, é o processo.
- **Satisfação do usuário (NPS ou Csat).** O usuário sente diferença? Pergunte. Se o NPS cai depois de implementar o agente, algo está errado.

### Dimensão 2: valor para o negócio

- **ROI do time híbrido.** Quanto o agente economiza ou gera de receita? Divida pelo custo do agente (infraestrutura, manutenção, treinamento). Um ROI acima de 3x em seis meses é saudável.
- **Velocidade de entrega.** O time está entregando mais rápido com o agente? Meça em dias ou semanas. Redução de 30% no tempo de entrega é um bom alvo.
- **Taxa de erros em escala.** O agente está errando menos que o humano? Compare a taxa de erros antes e depois. Se o agente erra mais, o custo pode superar o benefício.

### Dimensão 3: qualidade de implementação

- **Clareza de papéis.** Pergunte para o time: "Você sabe exatamente o que pode fazer?" Se menos de 80% responder "sim", você tem problema de comunicação.
- **Ciclo de feedback ativo.** O agente está aprendendo? Meça o número de feedbacks por semana. Menos de cinco por semana por agente indica que o ciclo não está funcionando.
- **Autonomia progressiva.** O agente ganhou mais autonomia nos últimos três meses? Se não, o modelo não está escalando. A autonomia deve subir gradualmente.

O AI Team Health Score não é teoria. É ferramenta de gestão. Use.

---

## Seção 9: Fechamento com gancho

O time de produto na era dos agentes não é sobre contratar mais pessoas ou mais máquinas. É sobre redesenhar quem faz o quê, com que autonomia e com que critérios de julgamento.

O PM não desaparece. Ele muda de lugar: de remar para dirigir, como diz Seshan. Quem insistir em remar o tempo todo vira o PM que Verrilli descreve, o cargo que não se justifica.

O HAT Model resolve o problema de papéis. O AI Team Health Score resolve o problema de métricas. Mas tem uma pergunta que fica no ar.

"Como montar times de IA quando os melhores data scientists querem startups, não corporações?"

O guia de 30, 60 e 90 dias mostra como começar. Mas escalar depende de atrair talento raro. E talento raro não aparece com salário competitivo. Aparece com propósito, autonomia e impacto.

No próximo capítulo, vamos explorar como competir por esse talento. Como montar times que atraem os melhores. E como mantê-los quando o mercado quer levá-los embora. O HAT Model é o começo, não o fim. A estrutura de papéis que você estabeleceu agora precisa de pessoas para preencher os papéis humanos. E essas pessoas são cada vez mais escassas.

Mas antes, uma pergunta para você levar para o seu time: "Se amanhã seu agente sugerir uma feature que você não pediu, quem decide se ela vai para o backlog?"

Se você não sabe a resposta, seu time híbrido está quebrado. E agora você sabe como consertar.

---

# PARTE IV: OPERAÇÃO. Como fazer rodar?

> *Time redesenhado, decisão tomada. Rituais, governança, cultura e ética.*

# Capítulo 7: O Operating System: rituais, decisões e governança

### 1. Cena de Abertura

Simon Last, cofundador do Notion, disse uma frase que resume a virada deste capítulo: "sou gerente de agentes agora, não mais o programador". Ele não digita código desde o verão anterior. Desenha tarefas de ponta a ponta, entrega para os agentes e fica no final, verificando se o resultado está certo e monitorando quando a coisa sai dos trilhos (Simon Last, cofundador do Notion, No Priors, mar/2026).

Preste atenção no que ele não disse. Ele não disse que o agente faz tudo sozinho. Disse que ele virou o verificador. O trabalho de executar virou commodity. O trabalho de julgar é o que sobrou.

Essa é a diferença entre um time que adota IA e um time que opera IA. O primeiro pluga o modelo e torce. O segundo desenha um sistema operacional em volta dele: como observa, como agenda, como escala, como revisa, como itera.

O Notion aprendeu isso da forma dura. Simon é explícito sobre o que acontece quando você monta o loop de verificação errado: "se você faz bem, consegue ser muito mais ambicioso e muito mais robusto do que com humanos escrevendo. Se você faz mal, vira tudo slop" (Simon Last, No Priors, mar/2026).

Modelo bom e resultado ruim não é paradoxo. É governança ausente.

---

### 2. Definição do Problema

Tem uma armadilha clássica nas empresas que estão começando com IA agora. Elas lançam copilotos, as pessoas não usam, e a conclusão é que o modelo não presta. Quase nunca é isso.

A Kavak, plataforma de carros usados da América Latina, viveu exatamente esse ciclo. Eles construíram ferramentas de copiloto e os funcionários simplesmente não adotaram. Aí mudaram a aposta: em vez de copiloto que a pessoa ignora, agentes que assumem o trabalho de verdade. Hoje mais de 90% das interações com clientes passam por agentes (Carlos García Ottati, fundador da Kavak, no a16z Podcast, fev/2026).

O detalhe que importa aqui não é o número. É o que veio antes dele. Antes de soltar os agentes, a Kavak construiu ontologia, pipeline de dados e "freios" de segurança. A mudança foi de governança, não de modelo.

O erro comum é o mesmo do passado: manter os mesmos rituais de antes e esperar resultado diferente. O time adota o agente e não repensa como opera. O agente decide sozinho? Quando escala para um humano? Quem revisa as decisões do agente? Com que frequência? O que acontece quando ele erra?

Sem um Operating System, a IA vira caixa-preta. O time fica refém de métrica técnica que esconde problema de experiência.

**Conexão com o Capítulo 6:** O framework de oportunidades mapeia ideias de IA em quatro etapas: Mapear, Priorizar, Validar, Escalar. Cada etapa encontra um correspondente no OS Framework. O Capítulo 6 responde "o que construir". O OS responde "como operar". A etapa Mapear identifica onde a IA pode gerar valor; o OS entra com o ritual Observe para monitorar se esse valor está de fato sendo entregue. A etapa Priorizar define o que fazer primeiro; o OS entra com Schedule para garantir rituais fixos de revisão. A etapa Validar testa a solução com usuários; o OS entra com Review para revisar casos-limite e falhas. A etapa Escalar expande a solução; o OS entra com Iterate para garantir melhoria contínua.

O caso da a16z "From Copilots to Agents" captura essa mudança de regime: empresas que estavam na fase de copiloto estão reconstruindo a companhia inteira em volta de agentes. A conversa com Carlos García Ottati, mediada por Angela Strange e Gabriel Vasquez, mostra que essa reconstrução é um trabalho de fundação de engenharia, não de prompt (a16z, "From Copilots to Agents: Rebuilding the Company Around AI", fev/2026).

---

### 3. Framework / Componentes

**OS Framework: 5 rituais de decisão para times com IA**

O acrônimo é OS, de Operating System. Observe, Schedule, Escalate, Review, Iterate.

| Componente | Nome | Descrição | Pergunta-guia |
|------------|------|-----------|---------------|
| O1 | Observe | Monitoramento de agentes com foco em experiência, não métrica técnica | "O usuário está feliz ou o modelo está certo?" |
| O2 | Schedule | Rituais fixos de revisão das decisões dos agentes | "Com que frequência revisamos o que o agente decidiu?" |
| O3 | Escalate | Caminho claro para escalação de decisões críticas para humanos | "Quando o agente pede ajuda e quando decide sozinho?" |
| O4 | Review | Revisão periódica de casos-limite e falhas do agente | "O que o agente fez de errado esta semana que ninguém percebeu?" |
| O5 | Iterate | Ciclo de melhoria contínua baseado em feedback humano | "Como o agente aprende com os erros sem repeti-los?" |

---

**O1: Observe. A métrica certa não é accuracy, é adoção e experiência**

A Kavak mediu a métrica errada primeiro. As ferramentas de copiloto funcionavam no sentido técnico, mas os funcionários não usavam. A métrica que importava não era a qualidade da resposta, era se alguém queria usar aquilo.

**A métrica de modelo mede o quão bem a IA executa a tarefa. A métrica de produto mede se a tarefa importa para quem usa.**

Confundir as duas é o erro clássico. Um modelo pode classificar intenção corretamente e mesmo assim o cliente pedir para falar com humano. Um copiloto pode responder bem e mesmo assim ficar abandonado.

O Notion enfrenta o mesmo problema pelo lado da engenharia. Simon descreve o que ele chama de "loop de verificação": não basta o agente escrever o código, tem que verificar de ponta a ponta. A pergunta não é "o agente gerou algo", é "o resultado está certo e pode ir para produção com segurança" (Simon Last, No Priors, mar/2026).

**Ferramenta: Human Agency Scale**

A Human Agency Scale mede o nível de autonomia do agente em relação à satisfação de quem usa. São 5 níveis:

| Nível | Nome | Descrição | Quando usar |
|-------|------|-----------|-------------|
| 1 | Humano decide sozinho | IA não toma decisão | Problemas complexos, alto risco, baixa maturidade |
| 2 | IA sugere, humano decide | IA recomenda, humano aprova | Decisões de médio risco, aprendizado inicial |
| 3 | IA decide, humano revisa | IA age, humano revisa depois | Decisões de baixo risco, alta confiança |
| 4 | IA decide, humano audita | IA age, humano audita periodicamente | Decisões rotineiras, baixo risco |
| 5 | IA decide sozinha | IA age sem intervenção | Decisões simples, risco mínimo, alta maturidade |

A lição da Kavak está aqui. Eles não pularam do copiloto para autonomia total. Subiram funil por funil, com freios de segurança no meio do caminho. A escala de agência sobe junto com a confiança, não antes dela.

O Notion faz o mesmo no código. Mesmo com agentes escrevendo os pull requests, o time ainda revisa todos. Simon resume: "eu nunca mais produzo um PR que não tenha sido totalmente testado" (Simon Last, No Priors, mar/2026). Agente pode escrever, humano continua revisando.

**Dica prática:** Se você só olha dashboard de modelo, você está cego para a experiência. Monte um painel duplo: métrica de modelo de um lado, métrica de adoção e escalação do outro. Se as duas divergirem, o problema é de governança, não de tecnologia.

---

**O2: Schedule. Rituais fixos de revisão**

O agente não participa de reunião. Mas as decisões dele precisam ser revisadas. O Schedule define a frequência e o formato dessa revisão.

O melhor exemplo de ritual de Schedule que eu conheço vem do Notion. Eles reescrevem o harness de IA deles mais ou menos a cada seis meses. Não é por vaidade. É porque o estado dos modelos muda rápido, e o sistema tem que ser desenhado em volta do estado atual da tecnologia. Simon diz que o tempo de reescrita vem caindo justamente porque o progresso está acelerando (Simon Last, No Priors, mar/2026).

Isso é Schedule na prática. A reescrita do harness não é um evento de emergência. É um ritual fixo. O time já está trabalhando na próxima versão antes de terminar a atual.

A Kavak fez o equivalente no rollout: implantou os agentes funil por funil, cada etapa com sua infraestrutura de dados pronta antes de avançar (a16z, fev/2026).

**Rituais recomendados:**

| Ritual | Duração | Frequência | O que revisar |
|--------|---------|------------|---------------|
| Daily do agente | 5 min | Diário | Decisões anômalas, escalações pendentes |
| Weekly review | 30 min | Semanal | Top erros, feedback de usuários |
| Análise mensal | 2h | Mensal | Análise de tendências, revisão de métricas |
| Audit trimestral | 4h | Trimestral | Revisão de casos-limite, alinhamento com estratégia |

**O risco:** Sem Schedule, o time só descobre problema quando o usuário reclama. Ou pior, quando o agente já causou dano. O Schedule transforma monitoramento reativo em governança proativa.

---

**O3: Escalate. Quando o agente pede ajuda**

A escalação não é falha. É feature. Um agente que nunca escala está tomando decisões que não deveria. Um agente que escala demais está sendo inútil.

A Kavak chamou isso de "freios" de segurança. São os mecanismos que determinam quando o agente segue sozinho e quando para e chama um humano. Sem freio, o agente que atende cliente vira o agente que promete coisa errada no contrato (a16z, fev/2026).

**Matriz de decisão de escalação:**

| Complexidade | Risco | Exemplo | Ação do agente |
|--------------|-------|---------|----------------|
| Baixa | Baixo | "Resume este documento" | Decide sozinho |
| Média | Baixo | "Responde uma pergunta com fonte" | Decide, oferece a fonte |
| Alta | Baixo | "Escreve este trecho de código" | Sugere, escala se tiver dúvida |
| Baixa | Alto | "Mexe em dados de cliente" | Escala para humano |
| Alta | Alto | "Migra ou apaga conteúdo" | Escala imediatamente |

**Regra prática:** Se boa parte dos usuários pede para falar com humano, seu agente está escalando pouco. Se quase ninguém pede, talvez você nem precise do agente.

---

**O4: Review. Caça aos casos-limite**

Caso-limite é o ponto cego de todo agente. O modelo foi treinado com o caso comum. O problema mora no caso raro que ninguém previu.

Na Kavak, o caso-limite tem nome: fraude. Cerca de 40% das transações de carro usado na América Latina terminam em fraude (Carlos García Ottati, a16z Podcast, fev/2026). O agente não pode tratar uma transação comum e uma transação fraudulenta do mesmo jeito. O Review existe para garantir que o modelo sabe quando ele não sabe.

O Notion faz Review de outro jeito, e é instrutivo. Todos os PRs passam por revisão, mesmo os escritos por agentes. Simon descreve o trabalho dele como "verificador externo": confere no final se está certo e vigia quando o agente sai dos trilhos. A pergunta do Review não é "o agente terminou a tarefa", é "o resultado está certo" (Simon Last, No Priors, mar/2026).

**Como fazer Review:**

1. **Semanal:** Selecione os casos com menor confiança do modelo. Analise manualmente.
2. **Mensal:** Analise todos os casos que foram escalados para humanos. Identifique padrões.
3. **Trimestral:** Busque casos que o modelo tratou como "normais" mas que na verdade eram exceções.

A lição do Notion sobre verificação vale para qualquer domínio: você não está dando um prompt e torcendo. Está pensando em que mudança quer fazer, como verificar, e como colocar em produção com segurança, e aí usando o agente nesse processo (Simon Last, No Priors, mar/2026).

---

**O5: Iterate. Aprendendo com os erros**

O ciclo de melhoria contínua baseado em feedback humano é o que separa um agente que estagna de um agente que evolui.

O harness do Notion é o caso mais claro de Iterate que existe. Eles reescrevem a cada seis meses porque o que funcionava parou de funcionar, e o que era impossível virou possível. A iteração não é ajustar o prompt. É desenhar de novo o sistema em volta do estado atual dos modelos (Simon Last, No Priors, mar/2026).

A Kavak iterou num horizonte mais longo. Eles aceitaram cerca de um ano de crescimento parado enquanto reestruturavam a empresa em volta dos agentes. Os KPIs de curto prazo e a experiência do cliente caíram durante a transição. Eles persistiram, e aí veio a melhora de escala e rentabilidade (a16z, fev/2026).

**Ciclo de iteração:**

1. **Coletar:** Feedback explícito (avaliação do usuário) e implícito (comportamento)
2. **Analisar:** Identificar padrões de erro
3. **Priorizar:** Qual erro causa mais dano à experiência?
4. **Corrigir:** Ajustar modelo, regras ou governança
5. **Validar:** O erro diminuiu? A satisfação melhorou?

**A armadilha:** Times que iteram só com base em métrica técnica e ignoram métrica de experiência. O ciclo de iteração precisa incluir as duas. A Kavak descobriu isso quando percebeu que o copiloto funcionava tecnicamente e mesmo assim ninguém usava.

---

### 4. Casos e exemplos

**Caso 1: Kavak. De copiloto abandonado a agente que atende cliente**

**Situação inicial:** A Kavak, plataforma de carros usados com operação verticalizada em e-commerce, recondicionamento, financiamento e logística, tinha ferramentas de copiloto que os funcionários não adotavam. O problema não era o modelo. Era a adoção.

**O que estava errado:** O copiloto deixava o humano no comando, e o humano tinha trabalho demais para parar e usar. A automação parcial não resolvia casos complexos e de alta variação, que são a maioria no atendimento de carro usado.

**Como resolveu:** Em vez de insistir no copiloto, a Kavak reconstruiu a empresa em volta de agentes. Primeiro veio a fundação de engenharia: ontologia, pipelines de dados e freios de segurança. Depois, a implantação funil por funil. O agente passou a assumir a interação, com o freio decidindo quando escala.

**Resultado:** Mais de 90% das interações com clientes hoje passam por agentes. A transição custou cerca de um ano de crescimento parado, com KPIs de curto prazo e experiência do cliente caindo antes de subir (Carlos García Ottati, a16z Podcast, fev/2026).

**O que ensina:** Você não troca copiloto por agente com um prompt. Troca com governança. Ontologia, pipeline e freio vêm antes do rollout.

---

**Caso 2: Notion. De programador a gerente de agentes**

**Situação inicial:** O Notion passou por várias eras de código assistido: autocomplete, depois inserção e reescrita, depois agentes que implementam e verificam de ponta a ponta. Simon Last começou a usar o Claude Code por volta de abril do ano passado e considera isso o desbloqueio.

**O que mudou:** O output individual subiu muito. Mas o gap também. Simon diz que dá para ser um engenheiro cem vezes ou mil vezes mais produtivo usando as ferramentas direito, e que a diferença entre a mediana e o topo ficou muito maior. O output passou a depender da capacidade e da vontade de usar as ferramentas.

**O que permaneceu:** A revisão não sumiu. Todos os PRs continuam passando por review. Simon virou o verificador externo: desenha a tarefa de ponta a ponta, confere no final e vigia quando o agente sai dos trilhos. "Sou o gerente de agentes agora, não o programador" (Simon Last, No Priors, mar/2026).

**O que ensina:** A automação não elimina o julgamento. Ela muda onde ele entra. O humano sai do loop de escrever e entra no loop de verificar.

---

**Caso 3: Os dois casos lidos na Human Agency Scale**

A Kavak e o Notion chegaram ao mesmo lugar por caminhos diferentes, e a Human Agency Scale explica o porquê.

A Kavak começou no nível 1 do copiloto: a IA sugeria e o humano decidia, e o humano simplesmente não usava. Aí subiu a escala funil por funil, com freios no meio, até o agente assumir a interação com revisão humana nos casos críticos. Não foi um salto para o nível 5. Foi uma subida com guarda-corpo.

O Notion está num ponto parecido no código. O agente escreve e testa, mas o humano continua revisando todo PR. Simon nunca deixou de ser o verificador final.

Nos dois casos, a maturidade de governança subiu antes da autonomia. A escala de agência é consequência da confiança, não um atalho para ela.

---

### 5. Guia prático: 30/60/90 dias

**Implementação do OS Framework em 90 dias**

**Primeiros 30 dias (mês 1: fundação)**

- [ ] Mapeie todos os agentes de IA do seu time. Liste nome, função e nível atual de autonomia.
- [ ] Para cada agente, aplique a Human Agency Scale. Identifique qual nível é adequado.
- [ ] Monte um painel duplo: métrica de modelo de um lado, métrica de experiência e adoção do outro.
- [ ] Escolha um agente prioritário: o que mais impacta a experiência do usuário.
- [ ] Defina regras de escalação básicas: quando o agente decide sozinho, quando pede ajuda.
- [ ] Configure o daily do agente para revisar decisões anômalas.

**Próximos 30 dias (mês 2: ritualização)**

- [ ] Implemente o Schedule completo: daily, weekly review, análise mensal.
- [ ] Inicie a weekly review: analise os top erros da semana e documente padrões.
- [ ] Colete feedback explícito dos usuários: avaliação após cada interação com o agente.
- [ ] Ajuste a Human Agency Scale com base nos primeiros resultados.
- [ ] Treine o time: PM, engenheiros e designers precisam entender o OS.

**Próximos 30 dias (mês 3: iteração e escala)**

- [ ] Complete o primeiro ciclo de Iterate: coletar, analisar, priorizar, corrigir, validar.
- [ ] Repita o processo para todos os agentes do time.
- [ ] Faça o primeiro audit trimestral: revisão de casos-limite e alinhamento com estratégia.
- [ ] Documente lições aprendidas e compartilhe com o time.
- [ ] Ajuste as métricas de sucesso com base nos resultados reais.

**Ações concretas para líderes:**

- Não delegue governança de IA para o time técnico. É responsabilidade de quem responde pelo produto.
- Seu time está começando? Não introduza agente autônomo de uma vez. Comece no nível 1 ou 2 da Human Agency Scale e suba conforme a confiança.
- A métrica mais importante do seu agente não é accuracy. É "o usuário pediu para falar com humano?"

---

### 6. Métricas de sucesso

Duas referências reais dão a régua. A Kavak reporta mais de 90% das interações com clientes passando por agentes, depois de construir a fundação de governança (a16z, fev/2026). O Notion reescreve o harness a cada seis meses, com o tempo de reescrita caindo conforme o progresso acelera (Simon Last, No Priors, mar/2026).

A lição dos dois números é a mesma: a métrica de sucesso não é o desempenho do modelo. É a saúde do sistema em volta dele.

**Valor para o usuário**

- **Adoção:** As pessoas usam o agente ou pedem para sair dele? É a primeira pergunta, antes de qualquer métrica técnica.
- **Taxa de escalação para humano:** Quanto menor, melhor, mas não zero. Zero significa agente tomando decisão que não deveria.
- **Tempo de resolução:** Quanto o problema leva para ser resolvido, não para ser respondido.

**Valor para o negócio**

- **Custo por interação:** Custo da interação com agente contra custo da interação humana.
- **Retenção:** O cliente continua usando o produto depois de interagir com o agente.
- **Tempo de ciclo de feedback:** Quanto tempo entre um erro ser identificado e corrigido.

Se a métrica de modelo e a métrica de experiência divergirem, o Operating System precisa ser revisado. Foi exatamente a divergência que derrubou o copiloto da Kavak e que o Notion resolve com o loop de verificação.

---

### 7. Fechamento e gancho para o Capítulo 8

O Operating System não é um framework opcional. É a condição para a IA não destruir a experiência enquanto impressiona em métrica técnica.

A Kavak pagou o preço para descobrir: um ano de crescimento parado enquanto reconstruía a empresa em volta dos agentes, com os KPIs de curto prazo caindo antes de subir. O Notion aprendeu na prática que o agente só vale se o loop de verificação estiver certo. Se fizer bem, sai mais ambicioso e mais robusto. Se fizer mal, vira tudo slop.

Se você implementar os 5 rituais (Observe, Schedule, Escalate, Review, Iterate), seu time terá governança para escalar. Mas tem um problema: quando você tem 2, 5, 10 agentes rodando ao mesmo tempo, o OS precisa ser replicado sem perder qualidade. No próximo capítulo, veremos como escalar esse Operating System para múltiplos agentes sem perder o controle. Spoiler: não é duplicando reuniões.

# Capítulo 8: Cultura que adota e ética que protege

## Cena de abertura

Abra a sua rede social favorita e repare nos posts. Depois de um tempo, eles começam a parecer estranhamente parecidos entre si. Muitos comentários também são gerados por IA. Um número crescente de artigos acadêmicos, de colunas de opinião e até de contos premiados passa pelo mesmo filtro.

Ethan Mollick, professor da Wharton, descreveu esse fenômeno no ensaio "Choosing to Stay Human". Ele chama esses textos de "vampiros de atenção com formato de significado": parecem densos, exigem esforço mental para decodificar e devolvem quase nada de compreensão em troca.

O ponto dele não é demonizar a IA. É mais sutil, e mais duro. Ele escreve há décadas e construiu um estilo próprio com professores, reescritas e comentários maldosos na internet. Se a IA escreve "bom o suficiente", ele poderia pular tudo isso. Mas pular seria abrir mão de algo que se provou central para a carreira e para a felicidade dele.

O que ele condena não é usar IA. É usar IA no automático, como padrão, sem pensar. O mais importante, ele diz, é continuar perguntando o que entregar para a máquina e o que guardar para nós mesmos, e não esperar que ninguém, incluindo a IA, responda isso por nós (Ethan Mollick, professor da Wharton, One Useful Thing, fev/2026).

Essa frase vale para uma pessoa. E vale, com o dobro do peso, para uma empresa.

## Definição do problema

"Fernanda, como a gente constrói uma cultura de IA que não dependa de heróis individuais?"

Essa pergunta apareceu em todas as empresas que visitei nos últimos três anos. De fintechs a varejistas, de healthtechs a seguradoras. Todo mundo quer "cultura de IA". Mas ninguém quer o trabalho sujo de construir os sistemas que a sustentam.

Cultura de IA não é treinamento. Não é workshop. Não é palestra de executivo no kickoff dizendo "vamos ser guiados por dados". Cultura de IA é o conjunto de rituais, incentivos e normas que determinam como uma organização descobre, desenvolve e mantém produtos de IA.

Sem ética operacionalizada, cultura de IA é só branding. E branding não segura um modelo em produção.

O problema central é o mesmo que Mollick aponta no nível individual, só que no nível da organização. Ele nota que os padrões de uso da IA estão sendo definidos agora, sem muito planejamento: pelas empresas de IA que desenham o produto para uso sem atrito, pelos empregadores que decidem o que conta como "usar bem a IA" e pelos professores que definem a "alfabetização em IA". Uma vez que uma geração constrói hábitos em cima desses padrões, reverter fica difícil.

Empresas caem na mesma armadilha. Elas deixam que o comportamento correto dependa da vontade individual, em vez de desenharem sistemas que tornem o comportamento correto o caminho mais fácil. E vontade individual, sob pressão de entrega, perde.

**Três sintomas de uma cultura sem ética:**

1. **Modelos vão para produção sem documentação.** O cientista de dados sabe o que fez, mas ninguém mais sabe. Se ele sair da empresa, o modelo vira caixa-preta.

2. **Times de produto e dados não falam a mesma língua.** O PM pede "recomendação personalizada", o cientista entrega um modelo de regressão logística que ninguém entende, e o usuário final recebe sugestões irrelevantes.

3. **A empresa descobre o problema ético depois do lançamento.** Não porque ninguém viu. Porque quem viu não tinha para onde levar a preocupação.

A pesquisa mais recente da McKinsey sobre o tema indica que apenas 28% das organizações têm o CEO com responsabilidade direta pela governança de IA (McKinsey, State of AI, 2025). O padrão é claro: elas investem em treinamento, contratam cientistas de dados, compram ferramentas. Mas não criam os rituais que garantem que esses investimentos gerem produtos sustentáveis.

Cultura sem governança é anarquia. Governança sem cultura é burocracia.

A chave é um sistema que torne o comportamento ético mais fácil e mais recompensador que o comportamento antiético. Não é sobre moralismo. É sobre construir algo que dure.

## Framework Culture-Ethics

Vamos botar nome no troço. Chamo de **Culture-Ethics**, um framework de 8 componentes que conecta cultura de IA com ética operacionalizada.

Cada componente tem três partes: o que é, por que importa e como implementar.

### C, Checklists de Deploy

**O que é:** Uma lista de verificação que todo modelo precisa passar antes de ir para produção. Não é opcional. Não é "vamos ver se dá tempo".

**Por que importa:** Sem checklist, deploy vira decisão de pressa. O modelo entra em produção sem teste de viés porque ninguém exigiu, e a correção depois custa mais caro que a checagem antes.

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

**Por que importa:** Quem vê o problema de dentro nem sempre tem poder de parar o deploy. Sem um canal de escalação, a preocupação morre na mesa do chefe que quer lançar.

**Como implementar:** Comitê de ética em IA com membros de produto, dados, legal e um representante dos usuários. Canal anônimo para reportar preocupações. Garantia de que ninguém será punido por levantar uma bandeira vermelha.

### T, Time Rotation

**O que é:** Rotação periódica de responsabilidades dentro do time para evitar dependência de heróis.

**Por que importa:** O mesmo cientista de dados não pode ser a única pessoa que entende o modelo de crédito, o modelo de recomendação e o modelo de fraude. Se ela sair, a empresa quebra.

**Como implementar:** A cada trimestre, cada pessoa do time assume a responsabilidade primária por um modelo diferente. A pessoa anterior faz a transição, documenta o que sabe e vira suporte secundário.

O framework Culture-Ethics não é um conjunto de regras para engessar o time. É um conjunto de rituais para liberar o time de depender de heróis.

## Casos e exemplos

### Caso 1: Ethan Mollick e a escolha de permanecer humano

O argumento de Mollick não é contra a IA. Ele é explícito: "eu sou tranquilo com muita rendição cognitiva". Não decora mais números de telefone, não liga para os filhos não aprenderem letra cursiva, aceita a calculadora para o cálculo do dia a dia. Habilidades que perderam utilidade podem sumir sem drama.

IA é diferente porque é geral o suficiente para que praticamente qualquer tarefa cognitiva seja terceirizada até certo ponto. E aí mora o problema: a gente não quer entregar tudo, mas na maior parte das tarefas a gente ainda não sabe o que importa manter e o que não. Decidir isso, ele diz, vai ser um dos grandes desafios dos próximos anos.

A escolha, no fim, não é feita na hora do uso. Ela é feita antes, no desenho: nos padrões que as empresas de IA definem para uso sem atrito, nas regras que o empregador estabelece para o que conta como bom uso, no que a escola ensina como alfabetização. Esses padrões estão sendo definidos agora, quase sem planejamento, e reverter depois de uma geração de hábitos é difícil (Ethan Mollick, professor da Wharton, One Useful Thing, fev/2026).

**Lição:** O paralelo com a empresa é direto. O comportamento ético não se decide no momento da crise. Se decide no desenho do sistema, antes de o modelo entrar em produção. Checklist, métrica e canal de escalação são o jeito de a organização fazer a escolha de forma deliberada, em vez de reativa.

### Caso 2: Dianne Penn e a borda irregular

Dianne Penn foi a primeira gerente técnica de produto da Anthropic. Ela descreve o desenvolvimento de produto dirigido por evals: o time define testes objetivos antes de liberar o modelo, e o deploy é condicionado ao desempenho nesses testes.

O motivo vem do que ela chama de "jagged edge", a borda irregular da capacidade. O modelo é sobre-humano numa tarefa e, numa tarefa parecida logo ao lado, falha de forma ingênua. Isso torna impossível confiar na impressão geral de que "o modelo é bom". Você precisa medir tarefa por tarefa.

E é exatamente nessa borda que o julgamento humano continua insubstituível. O que a máquina faz bem ela faz em escala. O que a máquina faz mal, alguém precisa perceber cedo, antes de o erro virar produto (Dianne Penn, primeira PM técnica da Anthropic, Lenny's Podcast, jul/2026).

**Lição:** Os evals são a versão industrial dos componentes U, Unambiguous Metrics, e C, Checklists de Deploy. E a borda irregular é o argumento técnico para o R, Revisão de Viés, e o E, Ethical Escalation: quem enxerga a borda precisa ter para onde levar a observação.

### Caso 3: Kavak e a empresa reconstruída em torno de agentes

A Kavak, plataforma de compra e venda de carros usados da América Latina, passou de ferramentas copiloto que os funcionários não adotavam para agentes autônomos que hoje resolvem mais de 90% das interações com clientes. O fundador, Carlos García Ottati, contou essa história no podcast da a16z.

O que interessa aqui não é o resultado. É o método. Antes de liberar os agentes, a empresa construiu a fundação: ontologias, pipelines de dados e "freios de segurança" para o deploy. A transição exigiu aceitar cerca de um ano de crescimento estagnado enquanto os sistemas substituíam fluxos humanos. E o próprio fundador precisou "se recontratar", voltando a papéis operacionais e adotando deliberadamente uma nova persona de liderança (Carlos García Ottati, fundador da Kavak, The a16z Show, fev/2026).

**Lição:** Reconstruir a empresa em torno de agentes é, antes de tudo, um projeto de cultura. Os freios de segurança são o componente E, Ethical Escalation, embutido na engenharia. E a mudança de persona do líder mostra o custo real da transformação: ninguém delega cultura.

## Guia prático

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

**Dica:** Não tente implementar tudo de uma vez. Comece com o checklist de deploy e a rotação de responsabilidades. Esses dois componentes resolvem a maior parte dos problemas de dependência de heróis e de falta de governança.

## Métricas de sucesso

Como saber se o framework Culture-Ethics está funcionando? Acompanhe estas métricas, e acompanhe a direção em que elas se movem:

1. **Tempo médio de deploy de modelos:** Deve cair, conforme a padronização reduz o retrabalho.

2. **Taxa de modelos que chegam à produção:** Deve subir, conforme a colaboração entre produto e dados deixa de ser opcional.

3. **Tempo de recuperação de falhas:** Deve cair com a rotação de responsabilidades, porque o conhecimento deixa de depender de uma pessoa só.

4. **Rotatividade no time de dados:** Deve cair, conforme o trabalho fica mais produtivo e mais seguro.

5. **Número de vieses identificados e corrigidos:** Deve subir nos primeiros meses, conforme os testes começam a detectar problemas, e depois estabilizar.

6. **Satisfação dos usuários afetados pelo modelo:** Deve subir de forma contínua, conforme as decisões passam a poder ser contestadas.

**Como medir:** Crie um dashboard de governança com essas métricas. Atualize mensalmente. Compartilhe com o board.

## Fechamento e gancho

Mollick termina o ensaio com uma advertência simples: o mais importante que podemos fazer é continuar perguntando o que entregar para a máquina e o que guardar para nós, e não esperar que ninguém, incluindo a IA, responda isso por nós.

Para uma empresa, a mesma escolha se decide antes do uso, no desenho do sistema. A empresa que deixa a ética como decisão individual no calor da entrega está apostando contra si mesma. A que escreve a escolha em checklist, métrica e canal de escalação transforma o comportamento correto no caminho de menor resistência.

Cultura de IA não é sobre contratar as pessoas mais brilhantes. É sobre construir sistemas que tornem o comportamento correto mais fácil que o comportamento incorreto.

No próximo capítulo, a gente vai ver como escalar produtos de IA sem escalar os problemas. Como passar de 10 para 100 modelos sem perder o controle. Porque escalar sem governança não é escalar. É multiplicar o caos.

A cultura que adota é a que protege. O resto é só branding.

---

# EPÍLOGO: Seu Plano 30/60/90

Você terminou o livro. Feche os olhos por 30 segundos. Pense na sua organização. Em que parte ela está? Abra a ferramenta da parte onde você está. Preencha. Faça uma coisa esta semana. Não 10. Uma. Este livro não foi escrito para ser lido, foi escrito para ser usado.

---

*Fernanda Faria, 2026*
