# Governança {{EMPRESA}}

Centro de comando da {{EMPRESA}}. Esta pasta governa cultura, estratégia, tática e operação como um sistema único.
**Comece sempre pelo `CLAUDE.md`** — ele define que você opera como CEO da {{EMPRESA}}.
**Primeira vez aqui?** `LEIA-ME-TEMPLATE.md` (e apague-o quando terminar).

---

## Como usar

1. Abrir `CLAUDE.md` → assume o papel de CEO e as regras permanentes.
2. Rotear o pedido para uma das sete árvores (`CLAUDE.md` §6 → `00-core/roteador/`).
3. Carregar na ordem do processo: `framework → trilho → método → blueprint → política → gate`.
4. Consultar o estado (`STATUS.md`) e o contexto da conta (`clientes/<cliente>/`).
5. Entregar decisão + direção + ação + impacto; registrar (`CLAUDE.md` §11); fechar com `verificar-propagacao.py` e `sincronizar.py`.

---

## Mapa de pastas

| Pasta | O que contém |
|---|---|
| `00-core/` | DNA da empresa: princípio, cultura, manifesto, políticas de decisão (os números), modos de resposta, critérios, compliance de output, KPIs, protocolo multi-modelo, taxonomia de artefatos e `roteador/` (as 7 árvores). |
| `10-skills/` | Skills portáteis (copy, página, ui-ux), personas (C-level, heads), jurídico, métodos não portados e a voz do operador. |
| `100-métodos/` | Os artefatos de conhecimento, tipados: frameworks, trilhos, métodos, políticas, gates. |
| `20-projeto-escopo/` | Detalhamento por dimensão (fonte: `PROJECT.md`/`SCOPE.md`). |
| `30-comercial/` | Só processo comercial da casa: ICP, oferta, produtos, serviços, onboarding, prospecção, swipe file, benchmark. Nada de cliente aqui. |
| `40-operacao-rotinas/` | Rituais, gestão do tempo, operação por tasks, medição de tokens, rito de integração da antessala e as `ferramentas/`. |
| `45-financeiro/` | Lançamentos da empresa e extratos classificados (fonte do painel *Caixa*). |
| `50-integracoes-dados/` | Estado dos sistemas (CRM, automações), escrito pelo sistema. |
| `60-planos/` | Plano de 90 dias e metas vigentes. |
| `70-metodologias-chave/` | Biblioteca de referência (PDFs, fora do git). |
| `80-juridico/` | Políticas jurídicas, templates de contrato, registros de caso, societário, dados do contratado. |
| `90-templates/` | Blueprints: repo de cliente, conta nova, léxico de ICP, benchmark de VSL, diagnóstico, PDFs, prancha, kit de marca, tráfego. |
| `900-oficina/` | Oficina das skills e agentes (edita-se aqui, publica-se em `10-skills/` e `.claude/agents/`). |
| `940-operador/` | O que é pessoal do operador e precisa estar no sistema (finanças pessoais). |
| `945-branding/` · `950-marketing/` · `960-referências criativos/` · `980-web-design/` | Marca, peças de marketing, referências de criativo, páginas e painéis nossos. |
| `clientes/` · `parceiros/` | Uma pasta por cliente e por parceiro; o molde em `clientes/README.md`. |
| `execução Codex/` | A antessala de um executor externo; nada aqui é canônico antes do rito. |
| `Padrão Linguístico - Operador/` | Fonte da voz do operador (corpus falado). |

---

## Documentos raiz

- `CLAUDE.md` — comportamento e papel de CEO (autoritativo).
- `STATUS.md` — estado vivo, fonte única de fato atual.
- `PROJECT.md` — tudo sobre a {{EMPRESA}} · `SCOPE.md` — escopo de atuação.
- `MAPA-DO-REPO.md` — o grafo de funcionamento (o README diz o que existe; o mapa, o que acontece depois).
- `AGENTS.md` — ponteiro para o kernel, regenerado por `sincronizar.py`.
- `METODO-*.md` — ponteiros para a fonte em `100-métodos/`.

---

## Estado

| Item | Status |
|---|---|
| Arquitetura e métodos | ✅ instanciados do template Continuum |
| Placeholders `{{…}}` | 🟡 a preencher (`LEIA-ME-TEMPLATE.md` §2) |
| Políticas e ICP | 🟡 a calibrar com evidência |
| Primeiro pedido real roteado | ⏳ pendente |
