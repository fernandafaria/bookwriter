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
