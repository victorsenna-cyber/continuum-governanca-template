# ÁRVORE — OPERAÇÃO

> **Tipo:** trilho · **Instituído:** 26/09/2026 (onda 5 da auditoria de roteamento de 26/09/2026) · **Alçada:** {{OPERADOR}}
> **Carrega-se quando:** o pedido é **executar e entregar** — tráfego, PDF, diagrama, prazo, rotina, financeiro, retenção, onboarding operacional, infraestrutura, tecnologia.
> **Réguas transversais** (§8 REGRAS Nº 0, 1, 2 · procedência · ordem) **valem aqui e não se repetem.**

---

## 1. Pré-condição

Nenhuma de entrada. ⚠️ **PDF de proposta** carrega a proposta pronta (ESCRITA) — a classe do PDF decide onde a economia aparece, **nunca se ela existe.**

## 2. O processo desta árvore

| Tipo | O que se carrega |
|---|---|
| **framework** | `100-métodos/METODO-CAMADA-DE-VER.md` · `100-métodos/METODO-ESTIMATIVA-DE-CARGA.md` |
| **trilho** | as fases do `100-métodos/METODO-TRAFEGO-PAGO.md` (gate → projeto → objetivo → página → criativo → campanha → tracking → gestão → relatório) |
| **método** | `100-métodos/METODO-TRAFEGO-PAGO.md` · `100-métodos/METODO-ITERACAO-DE-CPA.md` 🟡 · `100-métodos/METODO-EDICAO-DE-VIDEO-CURTO.md` 🟡 |
| **blueprint** | `90-templates/pdf-noturno/` · `90-templates/pdf-continuum/` · `90-templates/trafego-cliente/` (tráfego pago do cliente: nasce em `clientes/<Cliente>/NN - tráfego pago/`) · `90-templates/pdf-dashboard-trafego/` 🟡 (resultado fechado de campanha em PDF, uma página, visual do painel) |
| **política** | as três classes de PDF (`90-templates/pdf-noturno/README.md` §3-bis) · pisos e tetos de mídia do tráfego §2.2 |
| **gate** | `00-core/COMPLIANCE-DE-OUTPUT.md` (camada de ver) · gate do método em uso |

## 3. Linhas — sinal → carga → veto

| Sinais | Carga, na ordem do processo | 🔴 Veto |
|---|---|---|
| gestão de tráfego de cliente: plano de mídia, campanha, criativo de anúncio (lado mídia), otimização, escala, relatório, diagnóstico de CPA | `100-métodos/METODO-TRAFEGO-PAGO.md` *(método — abrir por momento)* + `10-skills/gestao-trafego.skill.md` + `clientes/<Cliente>/NN - tráfego pago/` | criativo **sem hipótese escrita** · linha de matriz sem os campos obrigatórios · *(27/10)* campanha para WhatsApp **fora de Engajamento** sem motivo no log, ou otimizada por clique (§5.2) |
| **iterar CPA, custo por conversa, custo por mensagem, taxa de conversão do WhatsApp, "o anúncio traz conversa e não vende", entrega da Assessoria de Marketing Local, ciclo mensal de otimização** | `100-métodos/METODO-ITERACAO-DE-CPA.md` *(método, 🟡 provisório desde 19/10)* → `METODO-TRAFEGO-PAGO.md` §7 + `METODO-LATERALIZACAO-DE-CRIATIVOS.md` → `clientes/<Cliente>/NN - tráfego pago/LOG-DECISOES.md` · **leitura dos números e projeção: `40-operacao-rotinas/ferramentas/painel-resultado/`** *(painel, 20/10: custo por conversa, taxa com faixa de confiança, custo por venda, projeção por verba e prazo com teto de entrega)* | 🔴 **CPA prometido ao cliente** · 🔴 **verba escalada sobre a taxa medida com menos de 5 vendas** (decide-se pelo piso da faixa) · campanha sem etiqueta de venda · mudança que melhorou a alavanca e piorou o CPA · duas mudanças na mesma alavanca no mesmo ciclo |
| "o hook rate está alto e não vende", queda de conversão, fadiga de criativo | `100-métodos/METODO-TRAFEGO-PAGO.md` §7.4 e §4.4 — **diagnóstico de mídia primeiro** | **presumir que a causa é o gancho** · classificar base como vencedora sem o critério da conta |
| **PDF com o resultado da campanha, "dashboard em PDF", fechamento de teste ou de ciclo para o cliente, "resultados fixos"** | os números do Gerenciador na data de fechamento + o `painel.json` do cliente (série diária) → `90-templates/pdf-dashboard-trafego/` *(blueprint, 🟡 provisório desde 27/10)* → JSON e PDF em `clientes/<Cliente>/NN - tráfego pago/relatorios/` | número sem fonte na nota · **venda ou faturamento sem confirmação** · headline no lugar de dado · eixo duplo · CSS próprio por cliente |
| tráfego nosso, canais, geração de demanda | `10-skills/heads/head-trafego.skill.md` | — |
| gerar PDF de qualquer artefato, "manda em PDF", material diagramado para fora | 🔴 **CLASSE antes do gerador** (`90-templates/pdf-noturno/README.md` §3-bis): *"como funciona?"* → ESTRUTURA · *"por que eu faria?"* → DECISÃO · *"eu assino?"* → FORMAL — **escolhida pelo ESTADO DO LEITOR** → **classe ESTRUTURA: + `100-métodos/METODO-CAMADA-DE-VER.md`** (o diagrama é o eixo e abre o documento) **+ o exemplar da mesma classe, se existir, antes de gerar do zero** *(replay de verificação, 26/09: sem isto o roteador novo carregava menos que o antigo)* → gerador: entender = `pdf-noturno/` (HTML) **com `eletrico.css`, o modelo padrão desde 16/10** (noturno puro só se o {{OPERADOR}} pedir) · assinar = `pdf-continuum/` (Markdown, ⚠️ marcado para revisão) | emoji em PDF · diagrama que não seja SVG inline · CSS novo por documento · **PDF do noturno sem `eletrico.css` sem pedido do {{OPERADOR}}** · página de prompt sem o `.md` ao lado · **PDF de material que não sai da casa** · classe usada para tirar as âncoras da proposta |
| "não estou conseguindo ver", fluxograma, diagrama, BPMN, mapa de processo, cliente que não visualiza, proposta que não entra | `100-métodos/METODO-CAMADA-DE-VER.md` *(framework)* + gate em `00-core/COMPLIANCE-DE-OUTPUT.md` | artefato de decisão **sem diagrama que abre o documento** · matriz no lugar de grafo · sem losango ou sem loop · falha no teste dos 5 segundos |
| "quanto tempo isso leva?", estimar prazo, cronograma, "cabe na semana?", dimensionar entrega | `100-métodos/METODO-ESTIMATIVA-DE-CARGA.md` *(framework — camadas A/B/C)* | **hora nossa em documento que sai da casa** · multiplicador de produção aplicado a colheita ou latência · número em proposta com calibragem `n=1` |
| editar vídeo gravado, edição de vídeo, cortar o bruto, legenda animada, motion no vídeo, tratar áudio do vídeo, "edita esse vídeo" | `100-métodos/METODO-EDICAO-DE-VIDEO-CURTO.md` *(método — 🟡 provisório até o 1º vídeo real)* + `40-operacao-rotinas/ferramentas/edicao-video/README.md` + `950-marketing/conteudo-perfil/` | render final **sem roteiro de corte aprovado** · legenda sem conferência de nome próprio · fonte do WhatsApp como original · áudio fora de −14 LUFS ±1 · trecho que fere a régua de tom |
| 🔴 **imagens ilustrativas de VSL, edição de VSL, b-roll, motion graphic, texto ou diagrama animado, explainer animado, vídeo de lançamento, anúncio em vídeo animado, vinheta** — para nós ou para cliente | **aviso: `40-operacao-rotinas/ferramentas/video-por-codigo/README.md`** *(ponteiro de recurso, 20/10)* → motor: skill `hyperframes:hyperframes` → repertório de forma: biblioteca de prompts de vídeo mantida fora da Governança (o README da ferramenta diz onde) · VSL: + o roteiro aprovado e a `COMPOSICAO-VSL.md` da conta · fala gravada: + a linha acima | **prompt da biblioteca como estrutura de venda** (REGRA Nº 2) · **imagem que cria fato, número ou depoimento que a fala não diz** · edição de VSL sem roteiro aprovado e sem laudo do A7 · render final sem roteiro visual aprovado · texto, logo ou arte de terceiro copiados |
| arquitetura, automação, IA, dados, segurança | `10-skills/c-level/CTO.skill.md` | — |
| processo, entrega, SLA | `10-skills/c-level/COO.skill.md` · **"capacidade estourada" → NEGÓCIO (contratação)** | — |
| cobrança, conciliação, rotina financeira | `10-skills/heads/head-financeiro.skill.md` | — |
| **cliente pagou**, "caiu", "recebi", PIX ou cartão confirmado, comprovante de cliente *(25/10/2026)* | `45-financeiro/LANCAMENTOS-EMPRESA.md` (cabeçalho: regra de pagamento de cliente) → linha em *Receitas* **e** a de *A receber* riscada com `✅ recebido`, no mesmo ato · depois o `STATUS.md` da conta | 🔴 **pagamento confirmado só no `STATUS.md` da conta** — o painel segue mostrando *atrasado* · dinheiro de cliente lançado como dinheiro pessoal |
| **compromisso novo**, dívida nova, parcela, acordo de pagamento, **crédito a receber combinado** — vindo de conversa de WhatsApp, call ou e-mail *(25/10/2026)* | a pagar da empresa e a receber de cliente → `45-financeiro/LANCAMENTOS-EMPRESA.md` (*A pagar* / *A receber*; multa e juros no mesmo lançamento) — **no formato do cabeçalho de `40-operacao-rotinas/ferramentas/financas-painel.py`**, conferido com `--json` → `sincronizar.py` (o push atualiza o painel sozinho, pelo Action `financas-painel`) | 🔴 **compromisso registrado só no registro da conversa** (`MSG-*.md`, `STATUS.md` da conta): o painel e a rotina `financas-gmail` não o enxergam |
| painel financeiro, DRE, fluxo de caixa, a pagar, a receber, *"o painel não atualizou"* | `980-web-design/painel-financeiro/README.md` → `40-operacao-rotinas/ferramentas/financas-painel.py` | 🔴 dado se corrige no `.md`, **nunca no Supabase** (é cópia reescrita a cada push) |
| **painel de projetos**, andamento das contas, "onde está cada cliente", o que falta entregar, prazos das contas, "o que preciso decidir", conta sem toque, *"puxar cliente por cliente"* *(28/10/2026)* | `980-web-design/painel-projetos/README.md` → `40-operacao-rotinas/ferramentas/painel-projetos.py` (`--json` dá o estado de todas as contas numa chamada N0; `--verificar` é o gate) → a camada de máquina é o frontmatter de `clientes/<Conta>/PAINEL.md` (regra de manutenção na `ARVORE-CONTA.md`) · site em `financeiro.{{DOMINIO}}/projetos/` | 🔴 **estado da conta lido do painel e não do `STATUS.md` para decidir** (o painel é leitor, o STATUS é a fonte) · dado corrigido no Supabase ou no site · saúde escrita na mão · varredura "cliente por cliente" lendo os STATUS inteiros quando o `--json` responde |
| retenção, adoção, churn, health score | `10-skills/heads/head-customer-success.skill.md` | — |
| ativação, kickoff, TTFV, onboarding | `10-skills/heads/head-onboarding-orquestrado.skill.md` | — |
| infraestrutura, VPS, n8n, cybersec | `10-skills/heads/head-ti-cybersec.skill.md` | — |

## 4. Desempate interno

- 🔴 **Onde mora a peça de cliente (25/10/2026, alçada {{OPERADOR}}):** campanha, plano de mídia, briefing, estrutura, matriz de criativos, log, relatório, script de criação de campanha e `painel.json` → `clientes/<Cliente>/NN - tráfego pago/` (molde em `90-templates/trafego-cliente/`) · página e site do cliente, com a configuração de publicação → `clientes/<Cliente>/NN - web design/`. **`30-comercial/` é só processo comercial da casa — nada de cliente mora lá.** Pasta que não existe no cliente é criada na mesma tarefa, com o próximo número livre da sequência dele.
- **Anúncio:** mídia (campanha, verba, CPA) → aqui · texto do anúncio → ESCRITA.
- **Vídeo:** o que dizer e o gancho de fala → ESCRITA (módulo 06) · editar o que já foi gravado → aqui · o que aparece na tela além da fala (imagem ilustrativa, motion) → aqui, pelo aviso `video-por-codigo/`.
- **Diagrama de proposta:** a proposta é ESCRITA; o diagrama que a abre é daqui — carregar os dois, **ESCRITA primeiro.**

---
*Linhas migradas do roteador v1 (R12–R14, R18, R27, R29–R32, R43, R46, R47)..*
