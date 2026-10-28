# MÉTODO — Estimativa de Carga

> **Tipo:** framework · secundário: método (§4), política (§5), registro (§6) *(reclassificado 26/09/2026 por auditoria independente de leitura integral; antes: sem campo)*
> **Abrir por momento:** decidir §1–§2 · produzir §4, com o registro do §6 *(mapa proposto pela auditoria de 26/09 — conferir no primeiro uso)*
> **Instituído em:** 18/09/2026 · **Alçada:** {{OPERADOR}} · **Aplica-se a:** toda proposta, todo cronograma, todo gate de contratação
> **Gatilho:** a constatação de {{OPERADOR}} de que a estimativa vigente era feita sobre construção manual, que demanda mais tempo, enquanto o modo de trabalho com IA cria muito mais em menos tempo.
> **Dono do número:** `METODO-ANCORAGEM-DE-PROPOSTA.md` Âncora 7 (nossa viabilidade) passa a ler este arquivo.

---

## 0. POR QUE ESTE MÉTODO EXISTE

**O repositório tinha três donos de hora e nenhum dono de estimativa.** `METODO-GATE-DE-CONTRATACAO.md` diz que hora é insumo comprável. `GESTAO-DO-TEMPO.md` diz qual é o ritmo do {{OPERADOR}}. `METODO-ANCORAGEM-DE-PROPOSTA.md` §Âncora 7 exige declarar viabilidade em hora. **Nenhum diz quanto uma coisa leva.**

🔴 **E o default silencioso era a hora de construção manual** — que é a referência errada para esta operação.

---

## 1. 🔴 O MULTIPLICADOR NÃO É UNIFORME — e é aqui que quase todo mundo erra

> **Três camadas de trabalho, e elas comprimem de formas radicalmente diferentes.**

| Camada | O que é | Compressão |
|---|---|---|
| **A · Produção** | escrever, estruturar, formatar, auditar, propagar, verificar, refazer | 🟢 **alta** |
| **B · Colheita** | call, entrevista, leitura de material do cliente, transcrição | 🔴 **nenhuma. 2 horas de call são 2 horas** |
| **C · Latência** | esperar decisão, autorização, acesso, gravação, resposta de terceiro | 🔴 **nenhuma — e às vezes piora**, porque produzimos mais rápido e esperamos igual |

> ## ⭐ A régua que isto institui:
> ### **O multiplicador se aplica à camada A. Aplicá-lo às camadas B e C produz cronograma que estoura — e o cliente atribui o estouro a nós.**

## 1.1 🔴 E o gargalo real quase nunca é produção

**Evidência da própria casa (uma conta de assessoria, exemplo trabalhado):**

| Item | Tempo parado | Tempo de produção |
|---|---|---|
| Decisão de ICP | **33 dias** esperando | ~1 hora para decidir e escrever |
| Fronteira entre dois sistemas de leitura do público | **18 dias** esperando | ~20 minutos |
| Material para uma pessoa do lado do cliente | **22 dias** esperando | não começou |
| 21 frases grau `D` de entrevistas já feitas | **7 semanas paradas** | ~2 horas para classificar |

> **Nenhum desses foi tempo de escrever.** Foram decisões que ninguém tomou e coisas que ninguém pediu.
>
> 🔴 **Consequência para toda proposta: o cronograma se monta pela camada C, não pela A.** Acelerar produção num projeto travado em latência **não move a data de entrega — só antecipa a espera.**

---

## 2. ⭐⭐ A UNIDADE DE MEDIDA ERRADA É HORA

> **Se o preço se ancora em hora, nossa eficiência vira desconto automático: quanto melhores ficamos, menos cobramos.**

**É o paradoxo que mata operação produtiva**, e ele opera em silêncio — ninguém decide cobrar menos; o número simplesmente encolhe junto com o tempo.

| Unidade | Serve para |
|---|---|
| 🔴 **Hora** | **conta interna de viabilidade e capacidade. NUNCA vai ao cliente, nunca ancora preço** |
| ✅ **Decisão tomada** | o que o cliente não conseguia fechar sozinho e agora está fechado |
| ✅ **Ativo utilizável** | o que existe depois e não existia antes |
| ✅ **Hora do cliente economizada** | ⭐ **o mais vendável dos três**, e o que ele mais sente |

> **A pergunta que substitui *"quantas horas isso leva?"*:**
> ### **"quantas decisões isso fecha, e quantas horas do cliente isso poupa?"**

---

## 3. 🔴 O FREIO — velocidade de produção × velocidade de absorção

**Produzir mais rápido não é gratuito. Ele transfere carga para três lugares:**

1. **Leitura do cliente.** Ele não lê mais rápido porque nós escrevemos mais rápido.
2. **Propagação nossa.** Mais artefato = mais canônico a atualizar, e a propagação **não comprime tanto quanto a produção**.
3. 🔴 **Risco de não-absorção** — o mais caro e o menos visível.

> ### ⭐ E o caso desta casa é literal, não hipotético:
>
> **Numa conta de assessoria, em cinco dias: ~31.000 palavras de artefato novo.** No mesmo período, a cliente declarou que não conseguia visualizar o que lhe era entregue e pediu esclarecimento **duas vezes** sobre o que estava sendo decidido (registrado na destilação da call).
>
> ## 🔴 A nossa velocidade de produção ultrapassou a velocidade de absorção da cliente. Isso não é sucesso — é desperdício com aparência de entrega.

**A régua que sai daí, e ela vale mais que o multiplicador:**

> **Artefato que o cliente não absorve tem custo de produção e valor zero.** A cada entrega, a pergunta é: **ele vai ler isto, ou eu estou produzindo para me sentir produtivo?**
>
> ⚠️ **Sinal de alerta medível: mais de um artefato denso por semana para o mesmo cliente.** Acima disso, reduzir volume e aumentar demonstração — **mostrar um pedaço pronto vale mais que entregar o documento inteiro.**

---

## 4. COMO ESTIMAR — o procedimento

1. **Separar a tarefa nas três camadas.** A maioria das tarefas tem as três, e quase ninguém as separa.
2. **Estimar B e C em tempo de calendário**, nunca em tempo de trabalho. Call é hora de relógio; espera é dia.
3. **Estimar A pela tabela de calibragem** (§6), e marcar `n` — quantos casos reais sustentam aquele número.
4. **Somar o cronograma pela camada dominante**, que quase sempre é C.
5. **Declarar o que trava**, com dono e nome. *"Depende do cliente"* não é dependência declarada.

---

## 5. COMO ENTRA NA PROPOSTA

| Âncora | O que muda |
|---|---|
| **7 · Nossa viabilidade** | passa a usar este método. **Continua sendo folha interna** |
| **2 · Payback** | encurta quando a camada A domina, **e não encurta quando C domina** |
| **5 · Condições de validade** | 🔴 **o que está em camada C vira condição de validade escrita, com dono.** É o que protege o prazo |
| **1 · Breakeven** | intocado — se ancora em margem, nunca em hora |

> ## 🔴 A regra dura desta seção:
> ### **Hora nossa nunca aparece em documento que sai da casa.** Nem como justificativa, nem como "investimento de horas", nem em anexo.
>
> **O cliente compra decisão, ativo e tempo dele de volta.** No segundo em que ele vê a nossa hora, ele passa a comparar o nosso preço com o salário de alguém — **e essa é uma conta que nunca ganhamos.**

---

## 6. TABELA DE CALIBRAGEM — 🔴 `n=1`, e é assim que se escreve

> **Base:** uma conta de assessoria, cinco dias de trabalho. **Um operador, uma conta, cinco dias.** Os números de produção são medidos; os de equivalente manual são **estimativa nossa, não benchmark.**

| Entrega | Tamanho medido | Camada A · real | Equivalente manual *(estimado)* |
|---|---|---|---|
| Funil de canal + peça de 3 páginas diagramada | 3.063 palavras + HTML/PDF | ~1 sessão | 2 a 3 dias |
| Destilação de call de 2h + auditoria de 105 citações | 5.165 palavras | ~1 sessão | 3 a 4 dias |
| Oferta completa: produto, promessa, mecanismo, lead, preço | 2.875 palavras | ~1 sessão | 1 semana |
| Método novo da casa + propagação em 5 skills, 2 árvores | 1.984 palavras + 10 arquivos | ~1 sessão | 1 semana |
| Banco de prova com 7 itens, timestamp conferido | 1.597 palavras | ~1 sessão | 1 dia |

**Total do período:** ~31.000 palavras em 9 artefatos novos, 1 método da casa, 1 PDF de 3 páginas, propagação em 9 canônicos, e **uma regra de alçada instituída no kernel**.

> 🔴 **O que esta tabela NÃO diz, e a lacuna é a metade que importa:** **quantas horas de relógio do {{OPERADOR}} foram gastas.** Sem esse número, o fator é impressão e não conta.
>
> ## ⚠️ Enquanto a coluna de horas reais estiver vazia, este método orienta a ORDEM das decisões — e não autoriza número em proposta.

**Como fechar a lacuna, e custa pouco:** anotar hora de início e fim por sessão de trabalho, por três semanas. **Três semanas de registro transformam `n=1` impressionista em fator defensável** — e é o mesmo movimento que o `METODO-FUNIL-DE-VSL.md` §8.1 exige dos números de benchmark.

---

## 7. O QUE ESTE MÉTODO NÃO FAZ

**Não autoriza vender mais rápido do que se entrega.** Velocidade de produção não é velocidade de resultado — `CLAUDE.md` §9 continua inteiro: **o ativo tem que declarar qual dinheiro gera.**

**Não substitui o `METODO-GATE-DE-CONTRATACAO.md`.** Hora continua sendo insumo comprável, e a escada D1–D4 continua valendo. ⭐ **Mas muda o momento do tripwire:** se a camada A comprime e B e C não, **o gargalo de capacidade migra da produção para a colheita e o acompanhamento** — e é aí que a primeira contratação faz sentido, não em quem escreve.

**Não vale para trabalho de terceiro.** O fator é desta operação com estas ferramentas. **Estimar hora de um contratado por esta tabela é subestimar em várias vezes.**

---

*Instituído em 18/09/2026. Roteado em `CLAUDE.md` §6 e §7. Primeira calibragem: uma conta, cinco dias, `n=1`, com a coluna de horas reais declarada em aberto.*
