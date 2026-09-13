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
