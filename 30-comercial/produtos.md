# produtos.md — Produtos e Plataforma da {{EMPRESA}}

> ⚠️ MODELO — preencher com a oferta da {{EMPRESA}}; o desenho é o método, os valores são seus.

> O que construímos como ativo de software — distinto de `servicos.md` (o que entregamos com mão de obra + IA).
> Princípio: **a operação financia o produto.** Cada módulo nasce de um processo já entregue a cliente real.

---

## 1. Continuum OS — *powered by Financial Core Runtime*

**Sistema operacional gerencial para PMEs / operações de serviço** — comercial, onboarding, financeiro, BI executivo e automação em um único shell.

- **Tese de arquitetura:** *"A casca é Continuum. O motor é Financial."* — Continuum (aditivo, módulos) encaixa sobre o Financial Core (confiável, transacional). Não funde código, acopla.
- **Forma:** SPA estático (HTML + JS vanilla, sem build) sobre **Supabase** (auth, banco, edge functions), **offline-first** (localStorage + syncQueue).
- **8 módulos:** comercial · onboarding · financeiro · analytics-onboarding · bi-executivo · integrations · configuracoes · sistema.

**Camada de decisão (diferencial):**
`Operação → Analytics → BI → Decision Engine → n8n → Execução (WhatsApp/ClickUp) → Feedback`.
O **Decision Engine** transforma alertas de BI em decisões executáveis (ação, SLA, responsável, escala, canal).

**Financial Core Runtime (`window.FinancialCore`):** DRE, fechamento de competência, distribuição societária, reservas, fluxo de caixa, contas a pagar/receber, conciliação — + camada de segurança (AuthService, RBAC, RLS, AuditService, CryptoService, CSP+SRI, 8 Edge Functions).

**Estado atual:** `<fase em que está o seu produto; o que está em produção e o que não está>`. Regime: nada avança sem comando de tarefa explícito; zero regressão.

> Roadmap de productização (Fase 02): **Follow-up AI · Cobrança e Reativação · Onboarding Orquestrado · BI Executivo · Decision Engine** — cada um vira módulo vendável a partir do processo validado em serviço.

---

## 2. Sistema Multiagente na VPS (*Continuum OS — fábrica de crescimento*)

**Fábrica autônoma de crescimento e entrega, governada pelo {{OPERADOR}}.** Recebe comando em linguagem natural (cockpit web ou Telegram), interpreta intenção, compõe skills + agentes e opera prospecção, venda, criação de ativos, entrega, medição e aprendizado — sob gates humanos.

- **3 primitivas:** **Skill** (capacidade reutilizável: SDR, Closer, CEO, CFO…) · **Agente** (composição de skills com papel) · **Projeto** (trava o "como"/processo).
- **Componentes:** **Hermes** (runtime de composição + auto-construção) · **Orquestrador FastAPI** (cérebro único) · **OpenClaw** (borda de canais).
- **Malha de agentes:** BDR/Research · Scoring · SDR · Follow-up · Closer · Handoff · Production Planner · Web Design · QA · BI · Learning.
- **Stack:** Python/FastAPI + Redis + worker async · Docker Swarm (`cos_`) · Supabase multi-tenant (RLS, eventos/aprovações append-only, pgvector) · **Qwen local (Ollama) default, Gemini exceção** · Telegram + WhatsApp (Evolution, governado) · cockpit em **app.{{DOMINIO}}**.
- **Estado:** `<o que está deployado, quantos testes, quais gates; o que está pendente>`.
- **Regime de construção:** o Claude planeja e executa sob task (`40-operacao-rotinas/tarefas/README.md`), com a regra de supply-chain de 7 dias para dependências novas.

---

## 3. CRM próprio — Twenty (alternativa open-source ao Salesforce)

- **Produto:** **Twenty** (React front + NestJS server, PostgreSQL + Redis, multi-workspace, GraphQL/REST + webhooks, SDK/CLI, Zapier). Licença **AGPL-3.0**.
- **Uso atual:** **interno da {{EMPRESA}}** (sem revenda SaaS por ora, para evitar obrigação AGPL). Roda em stack Docker isolada na VPS com Postgres próprio + botão no cockpit.
- **Integração prevista:** funil ↔ CRM via API/webhooks (task futura).
- **Evolução:** SaaS multi-workspace (1 workspace por cliente) como produto futuro.

---

## 4. Automações n8n

Orquestração de toda a prospecção/SDR (self-hosted na VPS). No Continuum OS o n8n é **borda de execução** — orquestra, nunca decide. 4 workflows de prospecção: orquestrador Telegram, prospecção sob comando, recepção de respostas (webhook), follow-up automático (cron 6h).

---

## 5. Sistema Financeiro (planilhas — motor de regra)

Modelos `.xlsx` que codificam a lógica financeira real (antes/ao lado do OS): abas INPUTS → RECEITA → CUSTOS → IMPOSTOS → DRE → FLUXO DE CAIXA → DISTRIBUIÇÃO → INDICADORES → PROJEÇÃO, com SUMIFS/COUNTIFS dinâmicos. 🔴 **Sócio único, {{OPERADOR}} 100%:** a aba DISTRIBUIÇÃO tem uma linha só. O modelo com mais de um sócio permanece útil como **template vendável a cliente com sociedade** — não descreve a nossa estrutura, é produto. Detalhe em `50-integracoes-dados/` e `45-financeiro/`.

---

## 6. Relação produto × serviço

| Camada | Hoje (serviço) | Amanhã (produto) |
|---|---|---|
| Prospecção/SDR | Operado por nós (n8n + Claude/Chrome) | Módulo SDR no OS / fábrica VPS |
| Follow-up | Cadência manual/assistida | Follow-up AI (módulo) |
| Cobrança | Processo do cliente | Cobrança e Reativação (módulo) |
| Onboarding | Sprints + acompanhamento | Onboarding Orquestrado (módulo) |
| Decisão | Rituais + dashboards | Decision Engine (módulo) |
| CRM | Twenty interno | Twenty SaaS multi-workspace |

---

## 7. Handoffs

← `oferta.md` (como o produto é vendido) · → `servicos.md` (o que opera em volta do produto) · ← `c-level/CTO.skill.md` (arquitetura/roadmap técnico) · ← `heads/head-ti-cybersec.skill.md` (infra/VPS/segurança) · → `50-integracoes-dados/` (conectores e fontes).

---
*Base: o repositório do Continuum OS (contexto do projeto e estratégia de unificação), o repositório do sistema multiagente (README, AGENTS.md, checkpoints, auditoria do CRM Twenty), as automações de prospecção ativa e as planilhas financeiras. Provenância, não leitura obrigatória.*
