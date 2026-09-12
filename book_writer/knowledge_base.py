"""Knowledge Base — Fatos, frameworks e fontes compartilhadas entre agentes.

Mantém a fonte única de verdade para dados, definições e referências.
Cada agente consulta esta base antes de escrever ou verificar.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Framework:
    """Framework autoral do livro."""
    name: str
    acronym: str
    chapter: int
    components: list[str]
    definition: str
    examples: list[str]


@dataclass
class DataPoint:
    """Dado quantitativo com fonte verificável."""
    value: str
    source: str
    year: int
    context: str
    verified: bool = False


@dataclass
class CaseStudy:
    """Case study de empresa real."""
    company: str
    chapter: int
    sector: str
    problem: str
    solution: str
    results: dict[str, str]
    verified: bool = False


# ── FRAMEWORKS AUTORAIS ──

FRAMEWORKS = {
    "escape": Framework(
        name="ESCAPE",
        acronym="ESCAPE",
        chapter=1,
        components=[
            "Empathy First — Comece com necessidades dos usuários, não capacidades da tecnologia",
            "Simple Metrics — Métricas que conectam com valor para usuário e negócio",
            "Context Awareness — Considere contexto real de uso, não cenários ideais",
            "Augmentation over Automation — IA para augmentar humanos, não substituí-los",
            "Progressive Enhancement — Implemente IA gradualmente, validando valor em cada etapa",
            "Ethical Considerations — Implicações éticas e sociais desde o início",
        ],
        definition="Framework para evitar a AI Trap: organizações obcecadas por implementar IA ao invés de criar valor real.",
        examples=[
            "Banco Digital: chatbot com 92% accuracy e NPS 1.8 → redesign → NPS 4.2",
            "E-commerce: recomendações com CTR 2.3% → contextualização → CTR 12.7%",
            "Startup Mobilidade: algoritmo com 96% accuracy e 12% adoção → redesign → 78% adoção",
        ],
    ),
    "ai_trap": Framework(
        name="AI Trap",
        acronym="AI Trap",
        chapter=1,
        components=[
            "Obsessão por métricas técnicas",
            "Soluções em busca de problemas",
            "Ignorar limitações e contexto",
            "Falta de human-centered design",
            "Ausência de feedback loops",
        ],
        definition="Quando organizações ficam obcecadas por implementar IA ao invés de criar valor real para usuários.",
        examples=[
            "Fintech: modelo com 94% accuracy rejeitava 60% dos clientes bons",
            "Varejo: sistema de recomendações de R$ 2.3M aumentou conversão em 0.3%",
            "Hospital: sistema de diagnóstico com 89% accuracy abandonado por falta de explicabilidade",
        ],
    ),
    "7_sinais": Framework(
        name="7 Sinais do Momento de Inflexão",
        acronym="7 Sinais",
        chapter=2,
        components=[
            "Mudança no Comportamento do Consumidor",
            "Investimento Corporativo Massivo",
            "Transformação do Mercado de Trabalho",
            "Mudança Regulatória Global",
            "Emergência de Novos Modelos de Negócio",
            "Mudança na Educação e Formação",
            "Impacto Geopolítico",
        ],
        definition="Sinais que confirmam que estamos em um momento de inflexão irreversível para IA.",
        examples=[
            "ChatGPT: 100M usuários em 2 meses — mais rápido que qualquer tecnologia na história",
            "89% das Fortune 500 têm projetos ativos de IA",
            "Vagas para AI PM cresceram 1200% em 2023",
        ],
    ),
    "10_competencias": Framework(
        name="10 Competências do AI PM",
        acronym="10 Competências",
        chapter=3,
        components=[
            "Technical Fluency",
            "Data Literacy",
            "Experimentation Mindset",
            "Ethical AI Understanding",
            "Cross-Functional Leadership",
            "AI-Specific Metrics",
            "User Research for AI",
            "AI Strategy & Roadmapping",
            "Regulatory & Compliance Awareness",
            "Change Management",
        ],
        definition="As 10 competências essenciais que diferenciam um AI Product Manager de um PM tradicional.",
        examples=[
            "Technical Fluency: saber perguntar 'Qual é o precision e recall? Testamos em produção?'",
            "Data Literacy: descobrir que 78% dos dados de treino são de homens 25-35 anos",
            "Experimentação: lançar chatbot para 5% dos usuários com múltiplas variações",
        ],
    ),
}


# ── DATAPOINTS (a atualizar com dados 2025-2026 via Researcher) ──

DATAPOINTS = [
    DataPoint(
        value="100 milhões de usuários em 2 meses",
        source="Reuters, fevereiro 2023",
        year=2023,
        context="Velocidade de adoção do ChatGPT comparada a outras tecnologias",
    ),
    DataPoint(
        value="67% dos profissionais de tecnologia usam IA regularmente",
        source="Stack Overflow Survey 2023",
        year=2023,
        context="Adoção de IA entre desenvolvedores",
    ),
    DataPoint(
        value="89% das empresas Fortune 500 têm projetos ativos de IA",
        source="McKinsey Global AI Survey 2023",
        year=2023,
        context="Adoção corporativa de IA",
    ),
    DataPoint(
        value="$93.5 bilhões em 2023",
        source="IDC Worldwide AI Spending Guide",
        year=2023,
        context="Investimento global em IA",
    ),
    DataPoint(
        value="Vagas para AI PM cresceram 1200% em 2023",
        source="LinkedIn Workforce Report 2023",
        year=2023,
        context="Demanda por AI Product Managers",
    ),
    DataPoint(
        value="78% dos consumidores brasileiros usaram IA nos últimos 6 meses",
        source="Pesquisa Datafolha/Bain 2023",
        year=2023,
        context="Adoção de IA no Brasil",
    ),
    DataPoint(
        value="Mercado global de IA: $207.9 bilhões (2023), projeção $1.8 trilhões (2030)",
        source="Grand View Research, 2023",
        year=2023,
        context="Tamanho e crescimento do mercado de IA",
    ),
    DataPoint(
        value="CAGR 38.1% (vs internet 28%, mobile 31%)",
        source="Análise comparativa da autora, 2023",
        year=2023,
        context="Comparação de velocidade de adoção entre revoluções tecnológicas",
    ),
]


# ── CASE STUDIES ──

CASE_STUDIES = [
    CaseStudy(
        company="Banco Digital (Brasil)",
        chapter=1,
        sector="Financeiro",
        problem="Chatbot com 92% accuracy técnica e NPS 1.8. 89% dos usuários pediam humano.",
        solution="Redesenharam experiência com foco no usuário, implementaram escalação inteligente, explicações simples, feedback loops.",
        results={
            "NPS": "1.8 → 4.2",
            "Adoção": "67% preferem chatbot para tarefas simples",
            "ROI": "Positivo em 8 meses",
            "Custo": "Redução de 34% em custos de atendimento",
        },
    ),
    CaseStudy(
        company="E-commerce (Brasil)",
        chapter=1,
        sector="Varejo",
        problem="Sistema de recomendações com métricas técnicas excelentes (precision 0.89) mas CTR de 2.3%.",
        solution="Mudaram métricas para revenue, implementaram contextualização, adicionaram explicações, A/B tests focados em outcomes.",
        results={
            "CTR": "2.3% → 12.7%",
            "Conversão": "0.8% → 8.4%",
            "Ticket médio": "+23%",
            "Revenue": "34% do revenue total via recomendações",
        },
    ),
    CaseStudy(
        company="Startup de Mobilidade (Brasil)",
        chapter=1,
        sector="Transporte",
        problem="Algoritmo de otimização de rotas com 96% accuracy mas 12% adoção dos motoristas.",
        solution="Incluíram motoristas no design, simplificaram interface, adicionaram explicações, implementaram override manual.",
        results={
            "Adoção": "12% → 78%",
            "Satisfação": "4.1/5",
            "Tempo": "Redução real de 22%",
            "Combustível": "-15% em custos",
        },
    ),
]


# ── BOOK OUTLINE ──

BOOK_OUTLINE = {
    "title": "Liderando na Era dos Agentes",
    "subtitle": "O manual de liderança de produto para a era da IA — por quem opera a transformação",
    "author": "Fernanda Faria",
    "parts": {
        1: {
            "title": "Diagnóstico: Onde você está?",
            "epigraph": "Antes de decidir o que fazer com IA, você precisa saber onde sua organização está. Sem diagnóstico, qualquer solução é tiro no escuro.",
            "chapters": {
                1: "A Armadilha de IA — e como explicar pro board que 'IA em tudo' é um erro",
                2: "O Mapa de Maturidade: os 5 níveis que toda área atravessa",
            },
            "tool": "Maturity Scan Canvas + AI Trap Detector",
        },
        2: {
            "title": "Decisão: O que fazer?",
            "epigraph": "Com o diagnóstico em mãos, a pergunta vira: construir, comprar, usar API ou open-source? E quanto isso custa de verdade?",
            "chapters": {
                3: "Build, Buy ou Partner? A decisão que define tudo",
                4: "O Custo Oculto: métricas e ROI que ninguém te conta",
            },
            "tool": "Build vs Buy Matrix + Custo Real Calculator",
        },
        3: {
            "title": "Time: Quem faz?",
            "epigraph": "Com a decisão tomada, é hora de olhar pro time. Quem fica, quem sai, quem se transforma — e o que o PM vira nesse mundo novo.",
            "chapters": {
                5: "Quem Fica, Quem Sai, Quem se Transforma",
                6: "O PM na Era dos Agentes: o que muda, o que some, o que nasce",
            },
            "tool": "Team Design Canvas + PM Brain OS",
        },
        4: {
            "title": "Operação: Como fazer rodar?",
            "epigraph": "Time redesenhado, decisão tomada. Agora é sobre rituais, governança, cultura e ética — o que faz a transformação durar.",
            "chapters": {
                7: "O Operating System: rituais, decisões e governança",
                8: "Cultura que Adota e Ética que Protege",
            },
            "tool": "Operating Model Canvas + Culture Scorecard + Ethics Checklist",
        },
    },
}


CHAPTER_DETAILS = {
    8: {
        "chapter_title": "Building AI Teams — Humanos e Agentes, Orquestrando o Time Híbrido",
        "premise": "Em 2026, o PM não gerencia só humanos. Gerencia um sistema híbrido onde agentes de IA são teammates com responsabilidades, autonomia e supervisão definidas.",
        "sections": [
            {
                "name": "Cena de abertura",
                "focus": "Uma reunião de planning onde um dos participantes é um agente de IA. Alguém na sala pergunta: 'Espera, quem escreveu esse PRD?' E a resposta incomoda.",
            },
            {
                "name": "O Time Híbrido: Humanos + Agentes",
                "focus": "Definir o conceito de time híbrido. Agentes de IA como teammates, não ferramentas. O PM como orquestrador de um sistema sócio-técnico.",
                "subsections": [
                    "O que agentes de IA fazem em um time de produto (exemplos concretos 2025-2026)",
                    "Níveis de autonomia: assistente → colaborador → delegado → autônomo",
                    "Quando um agente substitui um humano vs quando complementa",
                ],
            },
            {
                "name": "AI Agents como Teammates — O Novo Paradigma",
                "focus": "Seção central. Como agentes de IA atuam como membros da equipe: code review automatizado, PRDs gerados por agentes, análise de dados em linguagem natural, prototipação com Lovable/Cursor/Claude Code.",
                "subsections": [
                    "Tipos de agentes no time de produto: Researcher Agent, Analytics Agent, Prototyping Agent, Code Review Agent, Documentation Agent",
                    "O PM Brain OS: Claude/DeepSeek como segundo cérebro do PM (seguindo Product Compass Learning Roadmap)",
                    "Delegar para agentes: como definir tarefas, critérios de aceite, e revisão",
                    "Riscos: dependência excessiva, perda de pensamento crítico, viés de automação",
                ],
                "product_compass_refs": [
                    "PM Brain OS (Learning Roadmap #3)",
                    "Agentic Workflow Thinking (7-Layer Framework #3)",
                    "Claude Design como ferramenta de prototipação PM",
                ],
            },
            {
                "name": "Estrutura do Time Híbrido",
                "focus": "Como montar a org chart. Papéis humanos (PM, Designer, Engineer, Data Scientist) + papéis de agente. Reporting lines, rituais, comunicação.",
                "subsections": [
                    "O PM como Product Architect (não apenas manager)",
                    "Rituais do time híbrido: daily com agentes, planning com output de agente, retro do sistema",
                    "Métricas de eficácia do time híbrido: throughput, qualidade, autonomia",
                ],
            },
            {
                "name": "Casos Reais",
                "focus": "3 cases de empresas que já operam com times híbridos em 2025-2026: startups usando Cursor + Claude Code, enterprises com agentes internos, times de produto com AI prototyping stack.",
            },
            {
                "name": "Guia Prático",
                "focus": "30/60/90 dias para começar a integrar agentes no time: semana 1 (experimente um agente de pesquisa), mês 1 (integre ao workflow), trimestre 1 (time híbrido operacional).",
            },
            {
                "name": "Fechamento com Gancho",
                "focus": "Conectar com Cap 9 (AI Product Strategy): 'Montar o time é o primeiro passo. A pergunta seguinte é: com esse time, qual estratégia de produto de IA cria vantagem competitiva que não pode ser copiada?'",
            },
        ],
        "curiosity_gaps": {
            "to_plant": [
                "Com agentes no time, o que acontece com a cultura de produto?",
                "Se um agente pode escrever PRDs melhores que um PM junior, qual o novo papel do PM junior?",
            ],
            "to_resolve": [
                "Como montar um time de IA que não depende de heróis? (plantado no Cap 7)",
            ],
        },
    },
}


# ── SUBSTACK ARTICLES (Frameworks, Cases & Voice Reference) ──

SUBSTACK_ARTICLES = {
    "product_maturity": {
        "title": "Maturidade de Produto: Como anda a sua por aí?",
        "date": "2025-02-13",
        "frameworks": {
            "Product Excellence Maturity Model": {
                "levels": {
                    1: {"name": "Intuitivo", "motto": "Decide no Feeling", "traits": ["Decisões do chefe sem validação", "Discovery desconhecida", "Roadmap é 'vamos vendo'"]},
                    2: {"name": "Introdução a Processos", "motto": "Parece estruturado mas não tá", "traits": ["Conversam com clientes mas não registram", "Priorização por quem grita mais alto", "Roadmap existe mas ninguém confia"]},
                    3: {"name": "Estruturado", "motto": "Agora sim, data-driven!", "traits": ["Múltiplas fontes mas priorização frágil", "A/B tests tímidos", "Stakeholders tentam alterar roadmap"]},
                    4: {"name": "Alinhado ao Usuário", "motto": "Estratégia é coisa séria", "traits": ["Product Trio em fluxo contínuo", "Experimentação diária", "Dados usados com inteligência"]},
                    5: {"name": "Cultura de Produto de Alto Nível", "motto": "Produto é o próprio negócio", "traits": ["Empresa inteira entende estratégia", "Consumidores co-criam", "IA aliada estratégica"]},
                },
                "pillars": [
                    "Clareza de Estratégia — Se não sabe para onde está indo, qualquer bug serve",
                    "Entendimento Profundo do Usuário — Se não conhece quem usa, qualquer funcionalidade parece boa ideia",
                    "Roadmap Inspirador — Se não tem plano, qualquer deadline vira caos",
                ],
            },
        },
        "voice_samples": [
            "A gente confia no instinto e bora lançar esse troço",
            "Agora a gente faz reuniões de discovery! (mas ninguém anota nada…)",
            "Se não sabe para onde está indo, qualquer bug serve",
        ],
    },
    "high_performance_teams": {
        "title": "Do Caos à Excelência: Como Transformar seu Time de Produto",
        "date": "2025-02-17",
        "phases": {
            1: {"name": "Diagnóstico", "focus": "Encare a realidade. Decisões são data-driven ou 'achei legal'? Product Trio trabalha junto? Stakeholders confiam?", "quote": "Se as respostas te derem um leve desespero, você não está sozinho."},
            2: {"name": "Arrumando a Casa", "focus": "Crie processos que funcionam. Defina estratégia clara. Pare de tentar ensinar stakeholders sobre produto.", "quote": "Não entre naquela de 'as pessoas precisam aprender sobre como produto é feito', pois elas não deveriam precisar."},
            3: {"name": "Cultura de Experimentação", "focus": "Aprendizado contínuo intencional. Errar e aprender > entregar qualquer coisa. Novas contratações elevam a barra.", "quote": "Pensa como um custo: se você valida pouco, provável que vai gastar mais para arrumar depois."},
        },
        "key_quotes": [
            "Crie a visão de onde quer chegar e separe em pequenas entregas e aprendizados",
            "Product Trio (PM, Design, Tech) precisa estar junto da definição do problema à entrega",
            "Roadmap baseado em impacto, não no que o CEO pediu",
        ],
    },
    "product_vision": {
        "title": "Como Criar uma Visão de Produto que Todo Mundo Quer Seguir",
        "date": "2025-02-19",
        "inspiration": "Ebi Atawodi (ex-YouTube, Netflix, Uber) — talk no Lenny & Friends Summit 2024",
        "checklist": [
            "Sua visão é fácil de lembrar?",
            "Ela inspira e tem propósito claro?",
            "O time vê relação direta entre o que faz e essa visão?",
            "Você reforça e comunica essa visão o tempo todo?",
        ],
        "key_quotes": [
            "Se sua visão não der aquele arrepio ou empolgação na equipe, você ainda não chegou lá",
            "Lembre-se que as pessoas às vezes ficarão meio 'sem jeito' de te dizer a verdade",
            "Uma criança precisa ouvir uma palavra nova de 15 a 20 vezes para aprendê-la — considere essa métrica para repetir sua visão",
            "Sua visão tem que ser clara, mas adaptável. Tenha um norte, mas esteja pronto para recalcular a rota",
        ],
    },
    "future_teams": {
        "title": "O Futuro dos Times de Produto e Design: Novas Habilidades Essenciais",
        "date": "2025-03-10",
        "core_thesis": "Product Management está morto. Ou quase. O segredo é aprender a jogar junto com a IA, não contra ela.",
        "new_skills": [
            "Pensamento Sistêmico e Visão Estratégica — Mapear impactos no longo prazo, entender ecossistema maior",
            "Cultura de Experimentação e Uso de Dados — Testes A/B, análise profunda, usuários sintéticos para acelerar descoberta",
            "IA como Copiloto — Automação do trabalho tradicional do PM, generalistas híbridos, fronteiras PM/Design/Eng diluídas",
            "Liderança Adaptativa — Gerenciar agentes (IA) além de pessoas, inspirar times, fazer perguntas certas",
        ],
        "key_quotes": [
            "PM do futuro não é o que tem todas as respostas, mas o que sabe fazer as perguntas certas",
            "Se a IA pode testar hipóteses instantaneamente, por que você ainda toma decisões no feeling?",
            "Quem ainda espera 'receber briefing' para começar a trabalhar está errado",
        ],
    },
    "technical_to_leadership": {
        "title": "Minha Jornada: Do Técnico à Alta Liderança",
        "date": "2025-05-07",
        "key_insights": {
            "delegation": "Aprender a delegar vai de confiar. As pessoas farão da forma delas e provavelmente será diferente da sua. O que importa é o resultado.",
            "vulnerability": "Na liderança é bom ser vulnerável. Na alta liderança isso pode virar contra você. Você se sentiria seguro se o piloto do avião falasse 'tô bem não, minha atenção está baixa hoje'?",
            "purpose": "Entendi que ser mulher, LGBTQIA+ como líder, pode inspirar mais pessoas.",
            "transformation": "O técnico se importa mais com execução do produto. A liderança se importa mais com pessoas e desenvolvimento delas.",
            "advice": "Use o conhecimento técnico como fortaleza. Mas gaste a mesma energia em estudar liderança. Liderança é competência técnica também.",
        },
        "key_quotes": [
            "A pergunta deixou de ser 'como fazemos este produto crescer?' e passou a ser 'como fazemos estas pessoas crescerem?'",
            "Você abdica muito do tempo em família, tempo com amigos, às vezes a saúde mental dá uma sacudida também",
            "Como legado, quero que as pessoas vejam que diferentes perfis podem chegar na liderança",
        ],
    },
    "stop_categorizing": {
        "title": "Por que Líderes Precisam Parar de Categorizar Pessoas",
        "date": "2025-05",
        "key_concepts": {
            "complexity": "Nenhuma pessoa é binária. Carregamos virtudes e defeitos, mudando conforme contexto e momento.",
            "expectations": "Líderes criam expectativas próprias — a decepção surge da visão limitada, não da falha do outro.",
            "long_term_bet": "Aposto nas pessoas no longo prazo. Conviver mais tempo aumenta intimidade, confiança e conhecimento genuíno.",
            "self_work": "Se você virou líder, faça terapia. Líderes carregam inseguranças, medos e impaciências, e isso afeta todo o time.",
        },
        "references": ["Brené Brown (Daring Greatly, Dare to Lead)", "Patrick Lencioni (5 Desafios das Equipes)", "Han Byung-Chul (Sociedade da Transparência, Sociedade do Cansaço)"],
        "key_quotes": [
            "Clear is kind. Unclear is unkind. — Brené Brown",
            "A pressa é inimiga da reflexão. — Han Byung-Chul",
            "Você não pode dar aquilo que não tem. Você não pode ensinar aquilo que não sabe. — Brené Brown",
        ],
    },
    "user_agency": {
        "title": "Futuro da Experiência: Da Personalização à Agência do Usuário",
        "date": "2025-07-07",
        "core_thesis": "A experiência digital do futuro não está em prever com mais precisão o que o usuário gosta, mas em devolver a ele a capacidade de agir, explorar e cocriar.",
        "formula": "Intenção do Usuário + Ferramenta Poderosa = Experiência Cocriada",
        "concept": "Agência do usuário = poder de agir, sair do banco do passageiro e assumir o volante.",
        "examples": {
            "ecommerce_today": "Você comprou cerveja X, talvez goste de Y.",
            "ecommerce_tomorrow": "Fe, tô com seis amigos em casa pra um churrasco, tá um calor do cão. Preciso de um mix de cervejas leves, inclui uma opção de trigo pra variar, e uma sem álcool. Traz gelo e uma cachaça diferente. Entrega em 40 minutos.",
            "travel_today": "Vimos que você busca voos pro Rio. Veja estas ofertas.",
            "travel_tomorrow": "Tô com 4 dias de férias em setembro e R$3.000. Quero Nordeste, fugindo do óbvio, praias vazias com barracas. Me mostre 3 destinos com roteiro.",
        },
        "key_quotes": [
            "Os algoritmos são tão bons em nos dar o que a gente gosta que nos prendem numa bolha, numa espécie de 'Dia da Marmota' cultural",
            "Menos sobre dar o peixe e mais sobre entregar a melhor e mais inteligente vara de pescar do mundo",
            "Me recuso a ser só uma passageira da minha própria experiência",
        ],
    },
    "feminine_leadership_manifesto": {
        "title": "Manifesto da Liderança Feminina: Uma Liderança com Propósito e Presença",
        "date": "2025-07-20",
        "three_layers": {
            "visão": "Canalizar o que ainda não foi dito mas já pulsa no coletivo",
            "presença": "Sustentar o fogo do time, especialmente nos dias comuns e sem glamour",
            "integração": "Transformar o invisível em escolhas concretas, produtos e caminhos",
        },
        "key_quotes": [
            "Eu lidero com sabedoria antiga e visão além do tempo. O que chega a mim já pulsa no invisível",
            "Não vim agradar, vim abrir caminho",
            "Inovação sem presença é só ansiedade com branding",
            "Nem todo backlog merece sua energia. Nem toda métrica é bússola",
        ],
        "references": ["Aspásia de Mileto", "Hipátia de Alexandria", "Reshma Saujani", "Julie Zhuo"],
    },
    "stanford_framework": {
        "title": "O Framework de Stanford que Transforma AI no Superpoder do PM",
        "date": "2025-08-28",
        "frameworks": {
            "Human Agency Scale (HAS)": {
                "description": "5 níveis de automação, análogos aos níveis de carros autônomos. A maioria dos trabalhadores se sente confortável em H3-H5.",
                "levels": {
                    "H1": "Automação total — sem envolvimento humano",
                    "H2": "Alta automação — supervisão humana mínima",
                    "H3": "Parceiro igual — envolvimento humano e AI equivalentes",
                    "H4": "Automação parcial — AI é ferramenta, requer direção humana",
                    "H5": "Envolvimento humano essencial — AI não funciona sem input contínuo",
                },
            },
            "Automation Matrix": {
                "description": "2×2: Capacidade de Automação (X) × Desejo de Automação (Y)",
                "zones": {
                    "green": "Alto desejo + Alta capacidade → IMPLEMENTAR JÁ",
                    "red": "Baixo desejo + Alta capacidade → EVITAR, mesmo que tecnicamente possível",
                    "yellow": "Alto desejo + Baixa capacidade → Investir em R&D",
                    "white": "Baixo desejo + Baixa capacidade → Ignorar por enquanto",
                },
            },
            "Supernovas vs Shooting Stars": {
                "supernovas": "$0→$40M ARR ano 1, margens baixas (25% ou negativas). Ex: Perplexity, Cursor, Abridge",
                "shooting_stars": "~$3M ARR ano 1, margem bruta 60%, padrão Q2T3. Vantagem competitiva sustentável",
            },
        },
        "cases": {
            "perplexity": "H2 com supervisão estratégica. $125M+ ARR em 2 anos. Controle humano em curadoria de fontes e parâmetros de qualidade.",
            "cursor": "H3 parceria. AI sugere código, dev mantém controle total. Automatiza boilerplate, preserva controle de arquitetura.",
            "intercom": "$100M+ com controle humano no loop. Respostas nível 1 automatizadas (H2), casos complexos mantidos com humanos (H4).",
        },
        "key_quotes": [
            "O desejo do trabalhador pela automação é mais determinante do que a viabilidade técnica para o sucesso da adoção de AI",
            "AI estratégica não é substituir processos humanos, mas amplificar onde faz sentido e manter controle onde é crítico",
        ],
    },
    "judgment_taste": {
        "title": "A Ascensão do Julgamento: Por que 'Taste' Importa Mais que Frameworks na Era da AI",
        "date": "2026-02-20",
        "core_thesis": "Com AI tornando execução trivial, o único moat restante é taste/julgamento. Construir ficou fácil. O diferenciador é decidir o que construir.",
        "paradigm_shift": "Era 50/50 (craft + taste). Agora é 90/10. A construção fica mais fácil. O verdadeiro diferenciador é judgment. — Ravi Mehta (ex-Facebook, Tinder, TripAdvisor)",
        "seven_shifts_2025": [
            "Ownership end-to-end está encolhendo — PMs desenvolvem julgamento mais rápido com menos ciclos completos",
            "Discovery permanece raro — muitos PMs perdem sinais iniciais e pagam o preço na escala",
            "AI virou table stakes — diferenciação migrou pra credibilidade e julgamento",
            "Roadmaps viraram hipóteses — estratégia, experimentação rápida e tradeoffs de launch importam mais",
            "Outcomes batem outputs — 'No metric, no merit'",
            "Product leaders puxados pra GTM, pricing, revenue — GTM vira traço inato",
            "PM hiring mudou drasticamente — pouco espaço pra PMs puramente gerenciais; entrevistas favorecem execution, AI fluency e tradeoff scars",
        ],
        "top_skills_2026": [
            "Taste and Judgment",
            "AI Fluency",
            "Execution & Technical Depth",
            "Strategic Thinking",
            "Customer Insight",
        ],
        "defining_taste": [
            "Saber quais problemas valem a pena resolver",
            "Identificar features para matar antes de desperdiçar meses",
            "Sentir quando algo está certo ou errado antes dos dados confirmarem",
            "Criar produtos com alma — algo que scripts não replicam",
        ],
        "key_quotes": [
            "As the barrier to 'developer' hits zero, taste is the only moat left. If it doesn't have a soul, it's just noise. — Chase Hostler, loric.ai",
            "AI can generate strategy documents, but it can't feel the market shift under your feet. It can't see the pattern that isn't in the training data yet. — Ravi Mehta",
            "The hard part isn't building — it's deciding what not to build and being confident in that call. — Abhishek Gupta",
        ],
    },
    "product_principles": {
        "title": "Princípios de Produto: Uma Ferramenta Poderosa para Tomar Decisões",
        "date": "2025-09-04",
        "core_argument": "A diferença entre times que executam e times paralisados não é mais dados — são princípios de produto bem definidos.",
        "framework": {
            "name": "Product Principles Canvas",
            "components": {
                "core_values": "Inegociáveis. Slack: simplicidade sobre funcionalidade. Airbnb: conexão humana sobre eficiência. Amazon: cliente acima de tudo.",
                "decision_filters": "Transformar valores em perguntas. Slack: 'Isso vai fazer o usuário pensar mais ou menos?' Airbnb: 'Isso vai fazer as pessoas se sentirem mais conectadas?'",
                "tradeoff_guidelines": "Hierarquia. Simplicidade vs funcionalidade → simplicidade. Velocidade vs qualidade → qualidade. Usuário vs negócio → usuário.",
                "behavioral_anchors": "Histórias reais documentadas. 2-3 parágrafos de como princípios foram aplicados.",
                "evolution_triggers": "Quando revisar. NPS cair abaixo de X por 2 trimestres. Mudança regulatória. Disrupção de mercado.",
            },
        },
        "cases": {
            "slack": "Dilema: mais customização ou simplificar? Princípio 'Don't make me think' → removeu 30% das configs. Resultado: onboarding ↓40%, satisfação ↑25%.",
            "airbnb": "Dilema na pandemia: business travel ou long stays? Princípio 'Belong Anywhere' → long stays. Resultado: estadias 28+ dias cresceram 400%.",
            "amazon": "Dilema: remover conteúdo polêmico ou dar controle? Princípio 'Customer Obsession' → controle parental robusto. Resultado: satisfação ↑15%, churn ↓8%.",
        },
        "key_quotes": [
            "Empresas que decidem rápido têm 2× mais probabilidade de superar concorrentes financeiramente (McKinsey)",
            "Princípios não limitam criatividade — dão foco e direção para inovação mais efetiva",
            "O ideal é 1 princípio cristalino, ou no máximo 3-5. Mais que isso ninguém lembra",
        ],
    },
    "feminine_leadership_paradox": {
        "title": "O Paradoxo da Liderança Feminina em Tech: Vulnerabilidade",
        "date": "2025-09-03",
        "framework": {
            "name": "L.I.D.E.R.A.",
            "components": {
                "L": "Legitimidade através da competência — Provar competência de forma mais contundente, mas transformar isso em vantagem",
                "I": "Inteligência emocional como diferencial — Emoção no lugar certo, com o tempo se aprende",
                "D": "Diversidade como estratégia — Empresas com diversidade de gênero têm tendência financeira 25% melhor (McKinsey)",
                "E": "Empatia que transforma — A perspectiva diversa não é bônus de inclusão, é necessidade estratégica",
                "R": "Resiliência autêntica — A vulnerabilidade estratégica de admitir que o ambiente tech tem problemas estruturais",
                "A": "Ação multiplicadora — Nenhuma mulher sobe sozinha; criar caminhos para outras",
            },
        },
        "stats": [
            "30% dos cargos de alta gerência em tecnologia no Brasil são ocupados por mulheres",
            "Mulheres aplicam quando atendem 100% dos requisitos; homens com 60%",
            "Empresas com diversidade de gênero: tendência financeira 25% melhor e cultura de inovação 600% maior",
        ],
        "references": ["Nikila Srinivasan (VP Produto Meta)", "Ebi Atawodi (YouTube Studio)", "Adriana Aroulho (Presidente SAP América Latina)", "Daniela Binatti (CTO Pismo)", "Claudia Muchaluat (Presidente Intel Brasil)"],
        "key_quotes": [
            "Pensamos que devemos ocupar a liderança quando estamos 100% preparadas. Mas a verdade é que nunca estamos totalmente prontas",
            "Em vez de tentar se adaptar a uma cultura tóxica, podemos decidir criar uma nova cultura",
            "Nenhuma mulher sobe sozinha",
        ],
    },
}

# ── VOICE STYLE REFERENCE (extraído de todos os artigos + vídeos) ──

FERNANDA_VOICE = {
    "signature_openings": [
        "Era uma terça-feira de março quando...",
        "Quantas vezes você já se sentiu preparada apenas 60%?",
        "Se você acha que seu trabalho está seguro, sinto informar...",
        "Lembro de uma reunião onde...",
        "O mais difícil para mim é quem não é da área de produto",
        "Eu gosto de pensar: cara, divide o racional",
        "A cultura de produto tem muito a ver com você começar do valor gerado",
        "A maior barreira é as pessoas saírem do escopo atual delas",
        "Tem um paradoxo bizarro no meio dessa transformação digital",
        "Toda semana cai na minha caixa um fornecedor prometendo um agente de IA autônomo",
        "Antes de entrar no tema técnico de hoje, queria puxar um fio",
        "Nesses últimos 15 dias eu fui a um campeonato de Lorcana",
        "Se 2025 foi o ano em que todo mundo virou especialista em IA no LinkedIn",
    ],
    "tone_markers": [
        "Direta, sem pedir licença — 'Não vim agradar, vim abrir caminho'",
        "Antipática com hype — 'Inovação sem presença é só ansiedade com branding'",
        "Prática e acionável — Todo artigo termina com checklist, guia ou próximos passos",
        "Autobiográfica mas não autoindulgente — Usa a própria história como gancho, não como tema",
        "Humor seco — 'Você tem mais foco que eu em uma reunião de orçamento às 17h de uma sexta-feira 😉'",
        "Nomeia conceitos — Cria acrônimos e frameworks (ESCAPE, L.I.D.E.R.A., CLEAR, INTELIGENTE, Product Excellence Maturity Model)",
    ],
    "structural_pattern": [
        "1. Gancho pessoal/emocional (cena real)",
        "2. Problema/provocação (a pergunta que incomoda)",
        "3. Framework autoral (batizado, com componentes nomeados)",
        "4. Cases/evidências (preferência por cases brasileiros)",
        "5. Guia prático (30/60/90 dias ou checklist)",
        "6. Gancho pro próximo (deixa pergunta no ar)",
    ],
    "vocabulary": {
        "uses": ["bora", "tá", "sim", "rs", "D", "a gente", "troço", "zzzz...", "cara", "né", "Putz", "pô", "caramba", "rolê", "tipo", "maluquice", "fogo de palha", "barato saiu caro", "ralo de dinheiro", "puxar pra frente", "destrinchar", "real talk"],
        "avoids": ["sinergia", "solução robusta", "maximizar", "alavancar", "disruptivo", "storytelling", "terceiriza a responsabilidade", "falta maturidade como desculpa", "contratar senior como solução mágica", "discurso de autonomia total", "métrica de vaidade", "hype"],
    },
}

# ── PODCASTS & VIDEOS (metadados) ──

PODCASTS = [
    {"title": "Café com CPO: O papel do Product Manager", "platform": "PM3", "topic": "Liderança de produto, CPO", "url": "https://www.youtube.com/watch?v=8qwXhNI-xYA"},
    {"title": "Fe Faria: Liderança Tech, Zé Delivery e Carreira", "platform": "Product Guru's", "topic": "Carreira, liderança feminina", "url": "https://www.youtube.com/watch?v=d5G5hCF2yH4"},
    {"title": "Carreira de Produto e Scaling de Times", "platform": "Papo na Arena", "topic": "Scaling, times de produto", "url": "https://www.youtube.com/watch?v=1GHit-pFR6Q"},
    {"title": "Product Management e Liderança", "platform": "Lenny & Friends Summit", "topic": "Liderança, estratégia", "url": "https://www.youtube.com/watch?v=5z4cqkC9COA"},
    {"title": "Fernanda Faria — Diretora da AB InBev (maturidade de produto)", "platform": "Product Guru's", "topic": "Maturidade de produto", "url": "https://www.youtube.com/watch?v=X9svqWFYZR8"},
    {"title": "How to handle top-down directives (com Camila Lopes)", "platform": "Mesa de Produto", "topic": "Liderança, diretivas top-down", "url": "https://www.youtube.com/watch?v=K-CdG994DLo"},
    {"title": "O que é cultura de produto? (corte)", "platform": "Mesa de Produto", "topic": "Cultura de produto", "url": "https://www.youtube.com/watch?v=FvdHsEln3e0"},
    {"title": "Meetup — IA para Líderes", "platform": "Meetup AB-InBev", "topic": "IA, liderança", "url": "https://www.youtube.com/watch?v=65pfIFewvdU"},
]


def get_chapter_info(chapter_num: int) -> dict:
    """Retorna informações do capítulo: parte, título, epígrafe e detalhes."""
    result = {}
    for part_num, part_data in BOOK_OUTLINE["parts"].items():
        if chapter_num in part_data["chapters"]:
            result = {
                "chapter": chapter_num,
                "part": part_num,
                "part_title": part_data["title"],
                "part_epigraph": part_data["epigraph"],
                "chapter_title": part_data["chapters"][chapter_num],
            }
            break
    # Merge com CHAPTER_DETAILS se existir
    if chapter_num in CHAPTER_DETAILS:
        result["details"] = CHAPTER_DETAILS[chapter_num]
    return result


def get_style_guide_prompt() -> str:
    """Retorna o style guide como prompt para o Writer."""
    from book_writer.style_guide import STYLE_GUIDE
    return STYLE_GUIDE


def knowledge_summary() -> str:
    """Resumo para logging."""
    return (
        f"Knowledge Base: {len(FRAMEWORKS)} frameworks | "
        f"{len(DATAPOINTS)} datapoints | "
        f"{len(CASE_STUDIES)} case studies | "
        f"{len(SUBSTACK_ARTICLES)} Substack articles | "
        f"{len(PODCASTS)} podcasts"
    )
