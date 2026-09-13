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
