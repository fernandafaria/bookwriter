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
