# servicos.md — Serviços da {{EMPRESA}}

> ⚠️ MODELO — preencher com a oferta da {{EMPRESA}}; o desenho é o método, os valores são seus.

> O que entregamos com método + mão de obra + IA. Cada serviço resolve uma dor estrutural e alimenta o roadmap de produto (`produtos.md`).
> Princípio: **não vendemos execução isolada.** Todo serviço existe dentro de uma lógica de receita/operação.

---

## 0. Mapa da Ordem *(porta de entrada paga · ICP A — já fatura)*

**O que é:** mapeamento das dimensões de uma operação que já vende, entregue como documento único, com o que está de pé, o que está travado, quanto isso custa, **em que ordem resolver e o que fazer em cada frente**.

**Duas versões. A distinção é amplitude diagnosticada, não profundidade — e nenhuma delas é "básica":**

| | **Núcleo** | **Operação** |
|---|---|---|
| Amplitude | **5 dimensões**: ICP, promessa, oferta, narrativa e **Pivô de Conversão** | **10 dimensões**: as 5 do Núcleo + página, funil, conteúdo, **tráfego pago e dados/tracking** |
| Responde | *o que eu vendo, para quem, com qual história, e onde isso vira venda* | *tudo isso, e mais: por onde a pessoa chega, quanto custa trazê-la, e se dá para medir* |
| Produção | ~8h | ~20h |
| Prazo / devolutiva | 7 dias · 45 min | 14 dias · 90 min |
| Preço | **{{TICKET_MAPA_NUCLEO}}** | **a partir de {{TICKET_MAPA_OPERACAO}}** |

**Nas duas o cliente sai com o mapa E as sugestões de execução** — o que fazer por dimensão, a primeira alavanca já paga com a conta, e a ordem com a razão da ordem.

**Abatimento:** integral no setup da Assessoria se fechada em até 15 dias da devolutiva. O Núcleo abate no Operação dentro de 60 dias.

> **A fronteira, dita na devolutiva:** o Mapa entrega **o que fazer e em que ordem**. A Assessoria é **quem faz junto, toda semana.** Sugestão de execução não é execução.

**Por que existe:** a fase de descoberta é a que mais consome hora e era a que sempre foi dada de graça. Em um contrato anterior, ele **só coube porque a descoberta já tinha sido paga** — do zero, a resposta correta seria recusar. Cobrar a descoberta é a correção estrutural mais cara que estava em aberto.

**Regra de entrega:** o documento **não é enviado antes da devolutiva**. Documento lido sozinho vira julgamento; lido junto vira conversa.

⛔ **Não vender ao ICP B (quem ainda não fatura), nem com desconto.** A maior parte das dimensões depende de evidência que ele não tem. O produto daquele ICP é o **Alicerce** (§0-bis).

**Método:** `100-métodos/METODO-DIAGNOSTICO-DE-OPERACAO.md` · **Template:** `90-templates/diagnostico-operacao/` · **Pivô de Conversão:** `100-métodos/METODO-PIVO-DE-CONVERSAO.md` · **Rubrica de conteúdo:** `100-métodos/MATRIZ-LEITURA-CONTEUDO.md`

---

## 0-bis. Assessoria Estratégica · Alicerce *(ICP B — constrói do zero)*

**O que é:** construção dos **4 pilares** para quem quer começar ou recomeçar — ICP, promessa, oferta e narrativa, montados junto e **testados em conversa real**.

**Escopo fechado nos 4 pilares.** Página, funil e campanha ficam fora, nomeados com o preço do degrau.

**Preço:** a partir de **{{TICKET_ALICERCE}}** ({{HORAS_ALICERCE}}h ao piso de {{VALOR_HORA_PISO}}/h).

**Gate de saída:** a oferta foi levada a **pelo menos 10 conversas reais** com o ICP definido, e as respostas estão registradas. **Não é "vendeu" — é "foi testada".** Obrigação de meio, verificável pelas duas partes.

**A diferença de método, e ela não é de preço:** o Mapa da Ordem **lê evidência**; o Alicerce **cria e testa hipótese**. Quem não vende não tem evidência para ler.

⚠️ **Teto de capacidade: 1 cliente de Alicerce por vez**, até haver um caso completo. É construção pura — a fase de ~40h/mês da curva de carga (`POLITICAS` §4-ter).

**Método:** `100-métodos/METODO-ALICERCE.md`

---

## 1. Prospecção Ativa / SDR AI no WhatsApp *(serviço-âncora)*

**O que é:** agente de IA que prospecta listas frias, abre conversa, diagnostica gargalo, qualifica (BANT) e conduz ao **agendamento da reunião certa**. *"Você não fecha contratos — você agenda a conversa certa com a pessoa certa."*

**Como entregamos (dois modos):**

- **Assistido:** Claude in Chrome / Cowork operando WhatsApp Web, com **aprovação humana antes de enviar** (gerar lista → aguardar "ok" → executar). Cadência 10–20 leads/dia.
- **Automatizado (n8n):** orquestrador Telegram · prospecção sob comando · recepção de respostas (webhook) · follow-up (cron 6h). Anti-ban: espera 45–75s, ~10 msg/dia em horário comercial. Score BANT 0–12, classificação de intenção, anti-injection.

**Stack:** n8n · Gemini 2.0/2.5 Flash · Evolution API / Z-API / WhatsApp Cloud API · Supabase (`prospeccao_leads`, `prospeccao_conversas`) · Telegram · Apify (Google Maps scraper).

**Entregáveis:** lista qualificada · conversas registradas · leads scorados (quente/morno/frio) · reuniões agendadas.

---

## 2. Estruturação Comercial (Sistema Comercial Mínimo Viável)

**O que é:** montar pipeline, scripts de abordagem/follow-up, papéis (SDR/closer) e critérios de avanço por etapa. *"O problema não é falta de oportunidade — é falta de estrutura para aproveitá-la."* Estruturar o que já existe, não reinventar.

**Como entregamos:** ~4 semanas — Diagnóstico → estrutura inicial → operação real → calibração. Proposta HTML premium por cliente.

**Entregáveis:** pipeline definido · scripts · critérios de qualificação · rituais de pipeline · forecast inicial.

---

## 3. Assessoria de Marketing e Crescimento

**O que é:** estruturação de esteira de vendas (low/mid/high ticket) — funil, tráfego pago (Meta Ads), criativos, páginas, copy, conteúdo, produto e tracking. **Obrigação de meio**, não de resultado.

**Contrato de referência:** {{PRECO_ASSESSORIA_TOTAL}} / 6 meses ({{TICKET_ASSESSORIA}}/mês). Escopo (Anexo): funil completo · páginas (captura/quiz/venda/checkout) · Meta Ads · até 8 criativos/mês · até 3h de cortes/mês · conteúdo IG/TikTok/YT · robustecimento de eBook + arquitetura de workshop · tracking (Pixel, GTM, GA, API Conversões, PagTrust, UTMs) · alinhamentos quinzenais. Pode incluir **garantia de performance** (meta de referência 1,5× investimento).

**Entregáveis por sprint (modelo validado):**
- Sprint 1: sistema de ICP/prontidão · arquitetura da oferta · funil de consciência · protocolo de qualificação · sistema de conteúdo · cockpit operacional.
- Sprint 2: identidade operacional · anti-posicionamento · jornada do cliente · onboarding orquestrado (bônus).

---

## 4. Tráfego Pago

Aquisição qualificada (Google / Meta) **acoplada ao funil** — *"tráfego acelera o que já tem direção."* Não se vende solto: entra quando há estrutura comercial que sustente a demanda.

---

## 5. Conteúdo / Marketing de Autoridade

Linha editorial de 4 camadas — **Notícias · Dados · Autoridade/método · Clareza do que fazemos**. Carrosséis Instagram (1080×1350) com design system próprio. Disciplina de dados (fonte + data + unidade). Entrega via Cowork (copy) + Design (arte).

---

## 6. Dashboards de Leads (HTML interativo)

Transforma `.md` de leads em **dashboard dark editorial**: cards, busca em tempo real, filtros (estado/decisores), paginação, botões copiar e-mail/WhatsApp/Instagram, detalhes (dores, desejos, script de conexão). Gerado via Python (regex → JSON → HTML standalone). Entregável rápido de valor que abre conversa para CORE.

---

## 7. Sites de Conversão / Web Design

Para nichos premium (serviço local de ticket alto, onde a página é o ativo de conversão). Sites focados em conversão, acoplados à frente de prospecção.

---

## 8. Matriz serviço → dor → oferta

| Serviço | Dor que resolve | Entra em |
|---|---|---|
| **Mapa da Ordem** | "quero alavancar e não sei por onde começar" — falta visão de fora da própria operação | **porta de entrada paga → Assessoria** |
| **Alicerce** | "quero começar e não sei montar nada disso" — não existe estrutura para diagnosticar | **ICP B, escopo fechado** |
| SDR AI WhatsApp | Pipeline vazio / sem prospecção | CORE Essencial+ |
| Estruturação Comercial | Vende sem método, forecast na cabeça | CORE Avançado / avulso |
| Assessoria Marketing | Sem funil / sem esteira de produto | Pacote dedicado por conta |
| Tráfego Pago | Falta demanda qualificada | Complemento ao funil |
| Conteúdo/Autoridade | Sem posicionamento / sem inbound | Complemento recorrente |
| Dashboard de Leads | Sem visão de pipeline | Porta de entrada / CORE |
| Sites de Conversão | Sem ativo de conversão | Nichos premium |

---

## 9. Regras de entrega

- Todo serviço passa por **Onboarding Orquestrado** após o "sim" (`onboarding.md`).
- Nenhum serviço sem **responsável dos dois lados** e **first value definido (TTFV)**.
- Não escalar serviço sem operação estável; não prometer o que não há capacidade de entregar.

---

## 10. Handoffs

← `oferta.md` / `ICP.md` (a quem e como vender) · → `onboarding.md` (ativação) · → `produtos.md` (productização) · ← `heads/{head-trafego,head-conteudo,head-onboarding-orquestrado,head-customer-success}.skill.md` · ← `c-level/COO.skill.md` (capacidade/SLA).

---
*Base: automações de prospecção ativa, materiais comerciais (Claude Cowork, documentos e blueprints, propostas HTML), marketing, onboarding de contas anteriores (contrato, sprints, framework de ICP) e a arquitetura do sistema de prospecção. Provenância, não leitura obrigatória.*
