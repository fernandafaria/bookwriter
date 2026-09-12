# Aparições públicas — Fernanda Faria (CPTO Zé Delivery / ex-Ambev)

Mapeamento de podcasts, palestras e entrevistas com áudio/vídeo, para alimentar o
corpus de voz (voice pipeline). Filtrado: homônimas removidas (SKY, Talent, Pande,
Aerah House, Verum ESG, e "Fernanda Souza Faria" PM Nubank — outra pessoa).

## Podcasts / vídeos (YouTube — têm legenda/áudio)

| # | Título | Programa | URL | ID | Status |
|---|--------|----------|-----|----|--------|
| 1 | O papel do Product Manager | Café com CPO (PM3) | https://www.youtube.com/watch?v=8qwXhNI-xYA | 8qwXhNI-xYA | transcript OK (4K, parcial) |
| 2 | Os desafios de escalar um time de Produto (Mesa de Produto #3) | Product Guru's | https://www.youtube.com/watch?v=d5G5hCF2yH4 | d5G5hCF2yH4 | transcript OK (245K) |
| 3 | Carreira de Produto e Scaling de Times | Papo na Arena (Product Arena) | https://www.youtube.com/watch?v=1GHit-pFR6Q | 1GHit-pFR6Q | transcript OK (137K) |
| 4 | Product Management e Liderança | Lenny & Friends Summit | https://www.youtube.com/watch?v=5z4cqkC9COA | 5z4cqkC9COA | transcript OK (157K) |
| 5 | Fernanda Faria — Diretora da AB InBev (maturidade de produto) | Product Guru's | https://www.youtube.com/watch?v=X9svqWFYZR8 | X9svqWFYZR8 | pendente |
| 6 | How to handle top-down directives (com Camila Lopes, Nubank) | Mesa de Produto | https://www.youtube.com/watch?v=K-CdG994DLo | K-CdG994DLo | pendente |
| 7 | O que é cultura de produto? (corte) | Mesa de Produto | https://www.youtube.com/watch?v=FvdHsEln3e0 | FvdHsEln3e0 | pendente |
| 8 | Meetup — IA para Líderes (AB-InBev) | Meetup | https://www.youtube.com/watch?v=65pfIFewvdU | 65pfIFewvdU | pendente |

## Palestras / eventos (sem vídeo direto, mas com resumo publicado)

| Ano | Evento | Tema | Referência |
|-----|--------|------|-----------|
| 2023 | Product Camp (Pcamp) | Como liderar times de produto no novo cenário de tecnologia | https://pm3.com.br/blog/como-liderar-times-de-produto-no-novo-cenario-de-tecnologia/ |
| 2026 | Papo na Arena — especial IA | Como a IA tá mudando a estrutura das organizações (mesa com Gabriel Hamu + Fainer Costa/Itaú) | instagram Papo na Arena (Dia 7) |

## Conteúdo escrito (voz, sem áudio)

- Substack — 13 artigos (já em SUBSTACK_ARTICLES no knowledge_base.py)
- LinkedIn — posts sobre product management / maturidade de produto

## Próximos passos

1. Baixar transcripts dos #5-8 (uvx yt-dlp, mesmo fluxo).
2. Rodar voice_ingest.py em cada um, aplicar deltas no FERNANDA_VOICE.
3. Extrair texto do resumo do Product Camp 2023 (pm3.com.br) → marcadores de palestra.
