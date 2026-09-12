# Personas Sintéticas — Notas de literatura
Base Park + últimos 18 meses (fev/2025 → ago/2026)

Compilado: 2026-08-24 · Uso: material do Researcher/FactSheet do livro "Personas Sintéticas".
Aviso: muitos itens de 2026 são preprint arXiv (não peer-review). Peer-reviewed marcados explicitamente.
Valide cada citação antes de publicar — os arXiv IDs/DOIs/meses foram verificados via busca, não por leitura completa.

---

## 1. Base — Park (a linhagem fundadora)

1. Park, J.S., O'Brien, J.C., Cai, C.J., Morris, M.R., Liang, P., Bernstein, M.S. (2023).
   "Generative Agents: Interactive Simulacra of Human Behavior." UIST '23.
   arXiv:2304.03442 · DOI 10.1145/3586183.3606763
   → Marco fundador. 25 agentes com memória + reflexão + planejamento; comportamento emergente crível (Smallville).

2. Park, J.S., et al. (2024). "Generative Agent Simulations of 1,000 People"
   (título arXiv: "LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals").
   arXiv:2411.10109
   → O salto: agente ancorado em ENTREVISTA real de 2h, não prompt. ~85% de acerto no General Social Survey;
   previu a resposta do próprio humano 2 semanas depois; reduziu viés demográfico vs agente só-demográfico.

3. Park, J.S. (2025). Tese de doutorado "Generative Agent Simulations of Human Behavior."
   Stanford, jun/2025. Prêmio Arthur Samuel Best Thesis Award.
   → Consolida a linhagem. Park também fundou a Simile AI (Series A) pra levar a produto.

---

## 2. Últimos 18 meses (fev/2025 → ago/2026)

### A favor (sustentam a tese)

- Piao, J., et al. (2025). "AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents
  Advances Understanding of Human Behaviors and Society." Tsinghua. arXiv:2502.08691 (fev/2025).
  10 mil agentes, 5 milhões de interações — a prova de escala (e onde "sugere vs prevê" fica perigoso).

- "Can LLM Agents Simulate Multi-Turn Human Behavior? Evidence from Real Online Customer Behavior Data."
  arXiv:2503.20749 (mar/2025). Evidência com dado real de comportamento de cliente.

- "Can A Society of Generative Agents Simulate Human Behavior and Inform Public Health Policy?
  A Case Study on Vaccine Hesitancy." arXiv:2503.09639 (mar/2025). Simulação social → política pública.

- "Synthetic Founders: AI-Generated Social Simulations for Startup Validation."
  arXiv:2509.02605 (set/2025). Achado honesto: "semi-faithful simulation agents" (reproduzem heurísticas, geram lógica só-sintética).

- "Large Language Models as Virtual Survey Respondents: Evaluating Validity."
  arXiv:2509.06337 (set/2025). SSR ~90% da confiabilidade test-retest humana.

- "Simulating Human Opinions with Large Language Models." ACM. DOI 10.1145/3708319.3733685 (2025).
  Capacidades/limites de simular resposta de survey em pesquisa de mercado.

- "Large Language Models Can Predict the Results of Social Science Experiments."
  Nature, jul/2026. s41586-026-10742-x. ★ HEADLINE — LLM prevê resultado de experimento de ciência social.

- "The Silicon Society Cookbook: Design Space of LLM-based Social Simulations." arXiv:2605.00197 (mai/2026).
  O "cookbook" de design de simulação social — referência de "como se faz".

- "Evaluating LLMs as Human Surrogates in Controlled Experiments." arXiv:2604.15329 (abr/2026).

- "This Human Study Did Not Involve Human Subjects: Validating LLM Simulations as Behavioral Evidence."
  arXiv:2602.15785 (fev/2026). O título é o argumento do livro.

- "APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents."
  arXiv:2605.27419 (mai/2026). População em escala — direto no terreno das populações sintéticas.

- "Topology-Aware LLM-Driven Social Simulation: A Unified Framework." arXiv:2604.18011 (abr/2026).

- "Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions."
  AAMAS 2026. arXiv:2603.13890 (mar/2026).

### Limites / contra (matéria-prima do cap 5 "Sugere, Não Prevê" e cap 7 "Ética")

- Li, A., Chen, H., Namkoong, H., Peng, T. (2025). "LLM Generated Persona is a Promise with a Catch."
  arXiv:2503.16527 (mar/2025). O contra-canônico: em simulação de eleição 2024, previu varredura democrata em todos os estados.

- "Validation is the central challenge for generative social simulation: a critical review of LLMs in
  agent-based modeling." Artificial Intelligence Review (2025). DOI 10.1007/s10462-025-11412-6.
  Review crítica: validação é o gargalo central; LLM pode agravar, não aliviar.

- "The potential existential threat of large language models to online survey research."
  PNAS (2025). DOI 10.1073/pnas.2518075122. O lado sombrio que dá seriedade ao livro.

- "Whose Personae? Synthetic Persona Experiments in LLM Research and Pathways to Transparency."
  arXiv:2512.00461 (dez/2025). Transparência/ética de persona sintética.

- "When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses."
  arXiv:2607.26348 (jul/2026). Benchmark de onde o usuário sintético quebra.

- "Stop Drawing Scientific Claims from LLM Social Simulations Without Robustness Audits."
  arXiv:2605.18890 (mai/2026). Alerta metodológico.

- "Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents."
  WWW Companion '26 (abr/2026). DOI 10.1145/3774905.3795477 · arXiv:2602.18462.

- "Where Synthetic Respondents Fail: Diagnosing Local..." Leng (2026). SSRN 6835019.

- "Mechanism Plausibility in Generative Agent-Based Modeling." arXiv:2605.12824 (mai/2026).
  Escala de plausibilidade de mecanismo — perfeita pra operacionalizar "sugere vs prevê".

- "Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations."
  arXiv:2601.17087 (jan/2026).

### Tools / benchmarks

- "VISTA: A Versatile Interactive User Simulation Toolkit for Agent Evaluation." arXiv:2606.11079 (jun/2026).
- "MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Environment Simulation."
  ICML 2026. arXiv:2606.02470 (jun/2026).
- "Should LLM Agents Decide in Social Simulations? Comparing Finite-State and LLM-Based Decision Policies."
  arXiv:2606.12369 (jun/2026).
- "CityReal: Human-Aligned Urban Behavior and City Dynamics Simulation." arXiv:2608.16897 (jul/2026).
- "How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation."
  ACL 2026. arXiv:2603.13876 (mar/2026).

---

## 3. Fundação complementar (fora dos 18 meses, mas base conceitual)

- Argyle, L.P., Busby, E.C., Fulda, N., Gubler, J.R., Rytting, C., Wingate, D. (2023).
  "Out of One, Many: Using Language Models to Simulate Human Samples." Political Analysis 31(3):337–351.
  DOI 10.1017/pan.2023.2. → "silicon samples" + "algorithmic fidelity" (calibração demográfica importa).

- Horton, J.J., Filippas, A., Manning, B.S. (2023). "Large Language Models as Simulated Economic Agents:
  What Can We Learn from Homo Silicus?" NBER WP 31122. arXiv:2301.07543. → enquadramento teórico.

- Jiang, H., et al. (2024). "PersonaLLM: Investigating the Ability of LLMs to Express Personality Traits."
  Findings NAACL 2024. arXiv:2305.02547. → Big Five instilável; humanos percebem traços até 80%.

- Li, J., et al. (2024). "The Steerability of LLMs Toward Data-Driven Personas." NAACL 2024.
  Salminen, J., et al. (2024). "Deus ex machina and personas from LLMs." CHI '24. → composição de persona.

- Hermes, K., Poulsen, M. (2012). "A review of current methods to generate synthetic spatial microdata."
  Computers, Environment and Urban Systems. + Harland, K., et al. (2012). "Creating Realistic Synthetic
  Populations at Varying Spatial Scales." JASSS 15(1). → linhagem pré-LLM (IPF, microsimulação) = fundação da calibração.

---

## 4. Mapeamento para os capítulos do livro

- Cap 1 (Gente que não existe) → Park 2023 + Horton 2023
- Cap 2 (As Três Personas) → taxonomia própria (conselheiro/sujeito/executor)
- Cap 3 (Calibrar, Não Inventar) → Argyle 2023 + microsimulação + Park 2024
- Cap 4 (A Anatomia de uma Pessoa) → PersonaLLM + Li/Salminen 2024
- Cap 5 (Sugere, Não Prevê) → todo o bloco "contra": Promise with a Catch, Validation review, When Synthetic Users Fail, Stop Drawing Claims, Mechanism Plausibility
- Cap 6 (Decidir com Gente Sintética) → Nature 2026 + Park 2024 (1000 people) + VISTA/MCP-Persona
- Cap 7 (Limites e Ética) → PNAS 2025 + Whose Personae 2025

Tese do livro vira defensável com evidência 2026 dos dois lados: Nature prova que simula; "When Synthetic Users Fail"
prova que quebra. Os dois juntos = "sugere, não prevê" como estado da arte, não cautela.
