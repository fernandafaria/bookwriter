"""Article Topics — Definicoes de temas para geracao de artigos.

Cada topico define: titulo, tese, fontes, contexto, e parametros de geracao.
Usado pelo run_article.py para injetar contexto no Researcher.
"""

from typing import Optional

# ── TOPIC DEFINITIONS ──

ARTICLE_TOPICS = {
    "julgamento-vs-dados": {
        "id": "julgamento-vs-dados",
        "title": "A Ascensao do Julgamento: Por que 'Taste' Importa Mais que Dados na Era da IA",
        "subtitle": "Com IA tornando execucao trivial, o unico moat restante e julgamento. Construir ficou facil. O diferenciador e decidir o que construir.",
        "format": "artigo",
        "target_words": 1800,
        "core_thesis": (
            "O split historico de Product Management era 50% craft (construcao, execucao) "
            "e 50% taste (julgamento, decisao). Com AI generativa, a construcao colapsou "
            "pra 10% do trabalho. O verdadeiro diferenciador e julgamento: saber quais "
            "problemas valem a pena resolver, identificar features pra matar antes de "
            "desperdicar meses, sentir quando algo esta certo antes dos dados confirmarem."
        ),
        "paradigm_shift": (
            "Ravi Mehta (ex-Facebook, Tinder, TripAdvisor) cunhou: 'O split era 50/50. "
            "Agora e 90/10. A construcao fica mais facil a cada dia. O verdadeiro "
            "diferenciador e judgment.' Chase Hostler (loric.ai) complementa: 'As the "
            "barrier to developer hits zero, taste is the only moat left. If it doesn't "
            "have a soul, it's just noise.'"
        ),
        "seven_shifts": [
            "Ownership end-to-end esta encolhendo: PMs desenvolvem julgamento mais rapido com menos ciclos completos",
            "Discovery permanece raro: muitos PMs perdem sinais iniciais e pagam o preco na escala",
            "AI virou table stakes: diferenciacao migrou pra credibilidade e julgamento",
            "Roadmaps viram hipoteses: estrategia, experimentacao rapida e tradeoffs de launch importam mais",
            "Outcomes batem outputs: 'No metric, no merit'",
            "Product leaders puxados pra GTM, pricing, revenue: GTM vira traco inato",
            "PM hiring mudou drasticamente: pouco espaco pra PMs puramente gerenciais",
        ],
        "defining_taste": [
            "Saber quais problemas valem a pena resolver",
            "Identificar features para matar antes de desperdicar meses",
            "Sentir quando algo esta certo ou errado antes dos dados confirmarem",
            "Criar produtos com alma: algo que scripts nao replicam",
        ],
        "top_skills_2026": [
            "Taste and Judgment",
            "AI Fluency",
            "Execution & Technical Depth",
            "Strategic Thinking",
            "Customer Insight",
        ],
        "key_quotes": [
            "AI can generate strategy documents, but it can't feel the market shift under your feet. It can't see the pattern that isn't in the training data yet. — Ravi Mehta",
            "As the barrier to 'developer' hits zero, taste is the only moat left. If it doesn't have a soul, it's just noise. — Chase Hostler, loric.ai",
        ],
        "context_from_fernanda_articles": """
A Fernanda escreveu sobre este tema no Substack em 2026 ("A Ascensao do Julgamento").
O artigo original descreveu 7 shifts no mercado de PM: ownership encolhendo, AI virando
table stakes, roadmaps virando hipoteses, outcomes batendo outputs, e hiring migrando
pra execution + AI fluency + tradeoff scars.

Ela tambem cita o framework de Stanford (Human Agency Scale) que mostra que o desejo
do trabalhador pela automacao e mais determinante do que a viabilidade tecnica.

O tom do artigo original e direto: "Nao vim agradar, vim abrir caminho."
""",
        "research_queries": [
            "Ravi Mehta product management judgment taste 2025 2026",
            "AI replacing product managers 2025 2026 statistics",
            "product manager skills 2026 most valuable",
            "Chase Hostler loric.ai taste moat product",
            "Claire Vo AI in EPD operating model judgment",
            "Pawel Huryn Product Compass PM Brain OS judgment data 2026",
            "PM hiring trends 2025 2026 execution judgment",
            "produto digital Brasil IA julgamento 2025 2026",
        ],
    },
    
    "lideranca-feminina": {
        "id": "lideranca-feminina",
        "title": "Lideranca Feminina em Tech: O Paradoxo de 2026",
        "subtitle": "Quanto mais IA entra, mais habilidades humanas importam. E as mulheres ja chegam treinadas nisso.",
        "format": "artigo",
        "target_words": 1800,
        "core_thesis": (
            "Com IA automatizando tarefas tecnicas, as habilidades mais valorizadas "
            "passam a ser aquelas historicamente associadas a lideranca feminina: "
            "comunicacao, empatia estrategica, gestao de stakeholders, e capacidade "
            "de construir confianca em ambientes ambiguos."
        ),
        "research_queries": [
            "lideranca feminina tecnologia Brasil 2025 2026",
            "mulheres em produto digital estatisticas 2025",
            "female product leaders AI era 2026",
            "Yue Zhao executive presence framework",
        ],
    },
    
    "maturidade-produto": {
        "id": "maturidade-produto",
        "title": "Maturidade de Produto: O Diagnostico que Precede a Estrategia de IA",
        "subtitle": "Antes de decidir onde aplicar IA, voce precisa saber em que estagio sua organizacao esta.",
        "format": "artigo",
        "target_words": 1800,
        "core_thesis": (
            "O Product Excellence Maturity Model com 5 niveis e 3 pilares permite "
            "diagnosticar onde a organizacao esta antes de decidir onde investir em IA. "
            "A maioria das empresas brasileiras esta entre os niveis 2 e 3."
        ),
        "research_queries": [
            "product maturity model 2025 2026",
            "product excellence framework assessment",
            "maturidade produto digital Brasil 2025",
            "Claire Vo AI operating model maturity",
        ],
    },

    "agentes-como-teammates": {
        "id": "agentes-como-teammates",
        "title": "Agentes de IA como Teammates: O Novo Modelo Mental do PM",
        "subtitle": "Seu time nao e mais so humano. Como liderar quando metade do trabalho e feito por agentes.",
        "format": "artigo",
        "target_words": 2000,
        "core_thesis": (
            "O PM de 2026 gerencia um time hibrido: humanos + agentes de IA. "
            "Isso requer um novo modelo mental: Agentic Workflow Thinking, "
            "delegacao com niveis de autonomia, e PM Brain OS como segundo cerebro."
        ),
        "research_queries": [
            "AI agents product management 2025 2026",
            "agentic workflow thinking product manager",
            "Pawel Huryn PM Brain OS architecture",
            "multi-agent systems product development 2026",
            "AI teammates delegation patterns",
        ],
    },
    
    "operating-model": {
        "id": "operating-model",
        "title": "O Novo Modelo Operacional: Como a IA Muda o Jeito que Seu Time Trabalha",
        "subtitle": "As empresas que estao tendo ganhos de 2x, 5x, 10x nao estao usando ferramentas melhores. Estao operando com um modelo diferente.",
        "format": "artigo",
        "target_words": 2000,
        "core_thesis": (
            "Claire Vo (CEO ChatPRD) diz: 'The companies seeing 2x, 5x, 10x gains "
            "aren't running better AI tools than you — they're running a different "
            "operating model.' O novo modelo operacional redefine como o trabalho e "
            "escopado, delegado e revisado."
        ),
        "research_queries": [
            "Claire Vo AI operating model EPD 2026",
            "AI-native product organization operating model",
            "how AI changes product development workflow 2025 2026",
            "product operating model AI transformation",
        ],
    },
}


def get_topic(topic_id: str) -> Optional[dict]:
    """Retorna definicao do topico ou None se nao existir."""
    return ARTICLE_TOPICS.get(topic_id)


def list_topics() -> list[dict]:
    """Lista todos os topicos disponiveis."""
    return [
        {"id": tid, "title": t["title"], "format": t.get("format", "artigo")}
        for tid, t in ARTICLE_TOPICS.items()
    ]


def get_research_context(topic_id: str) -> str:
    """Monta contexto de pesquisa para o Researcher baseado no topico."""
    topic = get_topic(topic_id)
    if not topic:
        return ""

    lines = [
        f"TOPICO: {topic['title']}",
        f"TESE CENTRAL: {topic['core_thesis']}",
        f"FORMATO: {topic['format']} ({topic['target_words']} palavras)",
        "",
        "── PESQUISE OS SEGUINTES TEMAS ──",
    ]
    for q in topic.get("research_queries", []):
        lines.append(f"  - {q}")
    
    if topic.get("paradigm_shift"):
        lines.append(f"\nCONTEXTO ADICIONAL:\n{topic['paradigm_shift']}")
    
    if topic.get("context_from_fernanda_articles"):
        lines.append(f"\nCONTEXTO DOS ARTIGOS DA AUTORA:\n{topic['context_from_fernanda_articles']}")

    return "\n".join(lines)


def get_writer_context(topic_id: str) -> str:
    """Monta contexto para o Writer baseado no topico."""
    topic = get_topic(topic_id)
    if not topic:
        return ""

    parts = [
        f"TITULO: {topic['title']}",
        f"SUBTITULO: {topic.get('subtitle', '')}",
        f"TESE CENTRAL: {topic['core_thesis']}",
        f"EXTENSAO ALVO: {topic['target_words']} palavras",
    ]

    if topic.get("seven_shifts"):
        parts.append("\n7 SHIFTS DO MERCADO (para desenvolver):")
        for s in topic["seven_shifts"]:
            parts.append(f"  - {s}")
    
    if topic.get("defining_taste"):
        parts.append("\nDEFININDO JULGAMENTO/TASTE:")
        for d in topic["defining_taste"]:
            parts.append(f"  - {d}")
    
    if topic.get("key_quotes"):
        parts.append("\nCITACOES PARA USAR:")
        for q in topic["key_quotes"]:
            parts.append(f"  > {q}")

    return "\n".join(parts)
