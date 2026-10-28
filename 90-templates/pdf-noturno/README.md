# PDF NOTURNO — segundo gerador de PDF do repositório

> **Instituído em:** 18/09/2026 · **Alçada:** {{OPERADOR}}
> **Gatilho:** entregar o `.md` puro faz a formatação sair toda diferente quando aberto num bloco de notas. A visualização precisa ser preservada via PDF.
> **Convive com** `90-templates/pdf-continuum/` — não o substitui. Ver §3.
>
> 🔴 ⭐ **Ampliado em 19/09/2026, alçada {{OPERADOR}}** (o modelo de PDF virou canônico, sem eliminar o outro, com uma distinção entre eles). **O que virou canônico não é a folha de estilo — essa já era desde 18/09. É a ARQUITETURA DE CONTEÚDO do PDF de funil de 19/09 (exemplar da classe ESTRUTURA): mapa inteiro primeiro, cada seção detalhando uma caixa do mapa, diagrama abrindo cada seção.** Isso é uma **classe de documento**, e agora são três. **§3-bis é a parte nova deste arquivo.**

---

## 1. O QUE É

**Uma folha de estilo única, escura, que preserva no PDF a leitura que o `.md` tem renderizado.** Fundo `#1e1e20`, texto `#d8d6d3`, destaque `#e9a183`.

**Por que existe, e não é preferência estética:** o `.md` é o formato de trabalho e **só é legível dentro de um leitor que renderize**. Aberto em bloco de notas, vira texto com sinais de marcação — e quem recebe não vê nada do que foi construído. **O PDF é o que carrega a leitura para fora da casa.**

---

## 2. COMO SE USA

```
outputs/
  documento.html      ← conteúdo, com <link rel="stylesheet" href="noturno.css">
  noturno.css         ← cópia desta pasta
```

```bash
python3 -m weasyprint documento.html documento.pdf
```

**🔴 Não se escreve CSS novo por documento.** Classe nova que sirva a mais de um documento entra aqui; ajuste de um documento só não entra em lugar nenhum — **se precisou, quase sempre o conteúdo é que está errado.**

### As classes

| Classe | Para quê |
|---|---|
| `.capa` | primeira página, com `.kicker`, `h1`, `.lead`, `.rodape` |
| `.sub` | linha abaixo do título, cinza |
| `.ancora` | frase central grande, com `<span>` na cor de destaque |
| `.destaque` | bloco com barra lateral. `.lead` dentro dele é a frase-título |
| `.nota` | caixa discreta, para ressalva ou contexto |
| `.numeros` | três colunas com `.n` (número grande) e `.lbl` |
| `.fluxo` | SVG de diagrama, largura total · `.legenda-fluxo` abaixo |
| `.page-break` | quebra de página |
| `.copiar` + `.copiar-rotulo` *(12/10/2026)* | **bloco de texto que o leitor vai copiar**: roteiro, mensagem pronta, legenda. O rótulo acima diz onde o texto entra. Um bloco por coisa a copiar |

---

### Variante celular *(12/10/2026)*

`noturno-celular.css`, carregado **depois** do `noturno.css`. Troca a página A4 por **90 × 160 mm** e ajusta capa e corpo para leitura em tela de telefone. **Usar quando quem recebe só tem o celular**, que é o caso de boa parte das contas. Não muda cor, fonte nem classe.

**Primeira aplicação:** um PDF de roteiros de Reels de uma conta (classe ESTRUTURA, 17 páginas), com a fonte em HTML ao lado.

### ⭐ Variante elétrica: o MODELO PADRÃO de PDF da casa *(16/10/2026, alçada {{OPERADOR}})*

`eletrico.css`, carregado **depois** do `noturno.css` (e do `noturno-celular.css`, se for celular). Fundo `#05070F`, azul `#2F6BFF → #5B8CFF`, branco puro; títulos em **Anton** caixa alta, rótulos em **Montserrat** espaçada, corpo em **Inter** (as três por `<link>` do Google Fonts). Acrescenta `.fita` (faixa diagonal da capa), `.rotulo`, `.passo`, `.arquivos` e `.fluxo.alto` (diagrama limitado pela altura da página).

🔴 **Padrão desde 16/10/2026, para todo PDF que sai do gerador noturno** ({{OPERADOR}}, sobre o PDF-presente do perfil, que virou o novo modelo). ~~Só para material de marca; documento de conta e de método no noturno puro~~ *(vigente por algumas horas em 16/10, revogado pela mesma alçada)*. **O noturno puro continua disponível, mas só quando o {{OPERADOR}} pedir.** Carga padrão: `noturno.css` → (`noturno-celular.css`, se celular) → `eletrico.css`.

**Página de prompt** (`.prompt`, 16/10): texto para o leitor colar na IA dele, em fonte de 4,4 pt de propósito, para caber numa página e ser lido como prompt, não como texto. **Sempre acompanhado do mesmo texto em `.md`**, porque texto copiado de PDF leva as quebras de linha.

⚠️ **No Chrome, o `<style>` de um SVG vale para o documento inteiro.** Dois SVGs com a mesma classe (`.bx`, `.ts`) brigam, e o último vence. **Prefixar as classes de cada SVG** (`p-bx`, `q-ts`). O WeasyPrint isola; o Chrome não.

**Primeira aplicação:** o PDF do mapa do repositório, entregue como presente de perfil (classe ESTRUTURA, 17 páginas, celular).

### Gerar no Windows, sem WeasyPrint *(12/10/2026)*

Nesta máquina o WeasyPrint não está instalado. O Chrome sem interface gera o mesmo resultado, incluindo o fundo da página e o rodapé numerado:

```bash
chrome --headless=new --no-pdf-header-footer --print-to-pdf=saida.pdf arquivo.html
```

A fonte Lato entra por `<link>` do Google Fonts no `<head>`; os títulos caem para Georgia. ⚠️ **Texto copiado de PDF leva as quebras de linha da página.** Se o leitor vai colar o texto em outro aplicativo, mandar também o texto puro pela conversa.

## 3. 🔴 QUAL DOS DOIS USAR

| | `pdf-continuum/` | **`pdf-noturno/`** |
|---|---|---|
| **Fundo** | claro | **escuro** |
| **Entrada** | Markdown + capa JSON | **HTML** |
| **Serve a** | proposta, contrato, material formal | **documento de método, plano, estrutura, diagrama** |
| **Origem** | derivado de um PDF de destilação de call | esta folha |

> ⭐ **A régua: documento que se lê para ENTENDER vai no noturno. Documento que se lê para ASSINAR vai no continuum.**
>
> ⚠️ **O `pdf-continuum` está marcado para revisão** ({{OPERADOR}}, 18/09) — ele é derivado de um PDF de conta específica e nunca foi reescrito como template de casa.

---

## 3-bis. 🔴 ⭐ AS TRÊS CLASSES DE DOCUMENTO

> **Instituída em 19/09/2026.** A §3 escolhe o **gerador**. Esta escolhe **o que o documento faz** — e é a decisão que vem primeiro, porque duas das três classes rodam no mesmo gerador e saem completamente diferentes.

### A régua, em uma pergunta

> ## 🔴 Que pergunta do leitor este documento responde?

| Pergunta do leitor | Classe | Gerador | O eixo do documento |
|---|---|---|---|
| ***"como isso funciona?"*** | **ESTRUTURA** | noturno | **o mecanismo** — diagrama, peça por peça |
| ***"por que eu faria isso?"*** | **DECISÃO** | noturno | **a economia** — custo da inação, cenários, payback |
| ***"eu assino?"*** | **FORMAL** | continuum | **o compromisso** — escopo, preço, condições, prazo |

🔴 **As três são legítimas e nenhuma substitui outra.** O erro nunca é a classe existir; é **usar a classe errada para o momento errado do interlocutor.**

### ⭐ A ordem entre ESTRUTURA e DECISÃO, e ela não é intuitiva

> ## Quem ainda não VÊ o que está sendo proposto não tem como avaliar se vale a pena.
>
> **Economia apresentada a quem não visualiza o mecanismo não convence — convida a conferir a conta.** O leitor procura o ponto discutível do número porque é a única parte que ele consegue examinar, e **passa a discutir a projeção em vez de entender o método.**

**Com `n=0`, isso é pior ainda:** a projeção é, por construção, hipótese — e hipótese no eixo de um documento é o lugar mais frágil que ela podia ocupar.

| Estado do leitor | O que entregar |
|---|---|
| **não visualiza o que é** | **ESTRUTURA primeiro.** Decisão depois, e aí ela é curta |
| **já visualiza, falta razão para mover** | **DECISÃO direto** |
| **já decidiu, falta assinar** | **FORMAL** |

🔴 **Isso não autoriza entregar as três.** Três documentos sobre a mesma coisa é falha de absorção (`METODO-ESTIMATIVA-DE-CARGA.md` §3), não diligência. **Escolhe-se uma.**

### A arquitetura do documento de ESTRUTURA

**É o que ficou canônico em 19/09, e a sequência é a regra:**

| # | Página | O que faz |
|---|---|---|
| **1** | capa | título, uma linha do que o documento mostra |
| **2** | 🔴 **o mapa inteiro, como um diagrama só** | *"tudo que vem depois é o detalhe de uma destas caixas"* |
| **3+** | **uma seção por peça do mapa** | cada uma **abre com o próprio diagrama**, e detalha um nó |
| **n−1** | o que ainda precisa existir | **nosso × seu**, explícito |
| **n** | ⭐ **o que este documento NÃO faz** | o que só se sabe depois — **declarado, não omitido** |

> ⭐ **Por que o mapa na página 2 muda a leitura inteira:** ele dá ao leitor o modelo mental **antes** do primeiro parágrafo. Toda seção seguinte tem um lugar onde encaixar, e **o leitor nunca fica perdendo posição** — é a régua do §2 do `METODO-CAMADA-DE-VER.md` (*"o diagrama abre"*) aplicada ao documento inteiro, e não a uma seção.

> 🔴 ⭐ **E a última página é a que mais protege.** Declarar o que ainda não se sabe — CPA, conversão, taxa de upsell — **tira do documento a promessa que ele não pode sustentar, antes que o leitor a encontre sozinho.** Documento que só afirma parece forte e é frágil; documento que nomeia o próprio limite é o contrário.

### Modos de falha desta classe

| Falha | Como se reconhece |
|---|---|
| **vira DECISÃO disfarçada** | apareceu projeção, ROI ou "quanto isso gera" no meio do mecanismo |
| **mapa que não é mapa** | a página 2 tem uma caixa que nenhuma seção seguinte detalha, ou uma seção sem caixa |
| **diagrama decorativo por seção** | o diagrama repete o que o parágrafo abaixo já disse (modo de falha 1 do `METODO-CAMADA-DE-VER.md` §5) |
| **fecha vendendo** | a última página empolga em vez de declarar limite |
| 🔴 **síntese órfã** | o `.destaque` que fecha o raciocínio caiu sozinho na página seguinte, longe dos dados que ele resume — e frases como *"os blocos acima"* passam a apontar para o nada. **Correção: uma tabela por página, com a síntese na mesma página da última** *(encontrado na v2 de um funil, 19/09)* |

### ⭐ Quando o documento compara DUAS coisas

**É o caso mais frequente depois do mapa simples** — dois funis, antes × depois, nosso × seu. **A tentação é pôr as duas tabelas na mesma página para facilitar a comparação, e isso quase sempre estoura a página e órfã a síntese.**

> **O padrão que funciona: uma tabela por página, cada uma com os seus números grandes logo abaixo, e a síntese aritmética na mesma página da segunda.** O leitor compara pela memória dos números grandes, não pela adjacência física — e os números grandes existem justamente para serem lembrados.

---

## 4. RESTRIÇÕES

- 🔴 **Sem emoji.** As fontes do ambiente não têm os glifos, e eles saem como caixa vazia. **Em documento que sai da casa, emoji não entra de qualquer forma.**
- **Diagrama é SVG inline**, não Mermaid — o renderizador não executa JavaScript. **O Mermaid continua sendo a fonte no `.md`** (`METODO-CAMADA-DE-VER.md` §4); o SVG é a tradução para impressão.
- 🔴 **A folha de estilo do SVG vai DENTRO de cada `<svg>`, não no `<head>`.** O WeasyPrint renderiza SVG com um motor próprio que não enxerga o CSS do documento: `fill`, `stroke` e `text-anchor` declarados no `<head>` são descartados com o aviso `unknown property`, e o diagrama sai **com todas as caixas pretas e o texto desalinhado**. Um `<style>` como primeiro filho do `<svg>` resolve. **Repetir o bloco em cada `<svg>` do documento é o custo correto** — é a única exceção à regra de não escrever CSS por documento, porque não é CSS do documento, é do desenho. *(Descoberto na entrega de um funil, 19/09.)*
- **Fontes disponíveis:** `Lato` (corpo), `TeX Gyre Pagella` (títulos), `Poppins`, `Carlito`, `DejaVu`.
- **Margens e tipografia não se alteram por documento.** Se o conteúdo não cabe, corta-se o conteúdo.

---

## 5. APLICAÇÕES — e as duas primeiras são os dois exemplares das duas classes

| Data | Peça | Classe | Fonte |
|---|---|---|---|
| 18/09 | PDF de método de Direct Response entregue a uma conta (7p) | **DECISÃO** — exemplar | HTML do método, ao lado do PDF |
| **19/09** | **PDF de funil entregue a uma conta (8p)** | ⭐ **ESTRUTURA** — exemplar | HTML do funil, ao lado do PDF |
| 25/09 | PDF de encaixe entregue a uma conta (6p) | **ESTRUTURA** — variante *encaixe*: onde o que o cliente já está criando entra na estrutura. ⭐ **Página nova no padrão: "por que encaixar numa forma que já existe"** — o padrão repetido nas referências escaladas, **sem nome de concorrente**. Lição de montagem: seção curta que sobra sozinha na página sobe para a página do mapa (modo de falha "síntese órfã") | HTML do encaixe, ao lado do PDF |

| 16/10/2026 | PDF do mapa do repositório (18p, celular + elétrica) | ⭐ **ESTRUTURA — exemplar da linha elétrica.** O presente do story *"método"*. Mapa na p. 2, uma seção por caixa, página de prompt para a IA do leitor (fonte mínima), última página com o limite e a porta para o treinamento | `mapa-repositorio-continuum.html`, na mesma pasta |

> 🔴 ⭐ **A segunda NÃO substitui a primeira, e a correção é de 19/09** ({{OPERADOR}}: não eliminar o outro, mas fazer uma distinção). **São classes diferentes, não versões.** A de 18/09 abre pela projeção porque responde *"por que fazer isso"*; a de 19/09 abre pelo diagrama porque responde *"como isso funciona"*. **Cada uma é o exemplar de referência da sua classe** — quem for escrever uma das duas, copia a que corresponde.
>
> **O que a sequência das duas ensinou:** a de 18/09 não estava errada como documento de decisão. **Estava errada como primeira peça para uma leitora que tinha acabado de dizer que ainda não conseguia visualizar.** O defeito foi de ordem, não de conteúdo — e é isso que a §3-bis existe para não repetir.

### Modelo de partida

`90-templates/pdf-noturno/modelo-estrutura.html` — esqueleto comentado da classe ESTRUTURA, com os quatro padrões de SVG já montados. **Copiar e trocar o conteúdo; não recomeçar do zero.**

---

*Instituído em 18/09/2026. Classes de documento instituídas em 19/09/2026, alçada {{OPERADOR}}. Roteado em `CLAUDE.md` §7, com gate em `00-core/COMPLIANCE-DE-OUTPUT.md`.*
