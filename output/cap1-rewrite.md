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
