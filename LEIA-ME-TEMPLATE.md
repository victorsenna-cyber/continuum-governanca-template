# LEIA-ME — como instanciar este template

> Este repositório é o **template do repositório de governança Continuum**: a arquitetura completa (kernel, três camadas, sete árvores, taxonomia, métodos tipados, skills, blueprints, gates mecanizados, operação por tasks, rastro e sincronia git) de uma operação real, **sem dado pessoal, sem cliente e sem regra que só valia para a casa de origem**. O que ficou é o que decide.
> **Apague este arquivo quando a instanciação terminar.** Ele não faz parte da carga (`CLAUDE.md` §3).

---

## 1. O que é o quê

| Camada | O que você recebe | O que você faz |
|---|---|---|
| **Kernel** (`CLAUDE.md`) | papel, carga, roteador, regras permanentes, validação financeira, rastro | troca os placeholders; não apaga regra sem registrar a decisão |
| **Identidade** (`00-core/`) | princípio, cultura, manifesto, modos, compliance, taxonomia, protocolo multi-modelo, as 7 árvores | `CULTURA.md` §0 e §9 e `PROJECT.md` recebem a sua operação |
| **Política** (`00-core/POLITICAS-DE-DECISAO.md`, `30-comercial/`) | as réguas com o porquê; os números como `{{…}}` | calibra os números no dia 1; o que não sabe fica `a calibrar` |
| **Estado** (`STATUS.md`, `60-planos/`, `40-operacao-rotinas/`) | esqueletos com a forma certa | preenche e **mantém**: estado velho com cara de fonte é pior que não ter |
| **Métodos** (`100-métodos/`) | 37 artefatos tipados, anonimizados, íntegros | lê pela árvore, nunca "de cabeça"; método novo segue a REGRA Nº 1 |
| **Skills** (`10-skills/`, `.claude/agents/`) | portáteis, personas, jurídico, agentes de VSL | `voz-operador.skill.md` é esqueleto: a sua voz entra pela extração de linguagem |
| **Ferramentas** (`40-operacao-rotinas/ferramentas/`) | verificador de propagação, sincronia git, medição de tokens, despachante, transcrição, captura, painéis | liga só o que vai usar; cada uma tem README |

## 2. Placeholders

Rode `python3 40-operacao-rotinas/ferramentas/instanciar-template.py --listar` para ver todos os `{{…}}` com arquivo e linha, e `--definir CHAVE=valor` para substituir em todo o repositório. Os principais:

| Placeholder | O que é | Onde pesa |
|---|---|---|
| `{{EMPRESA}}` | nome da sua empresa | kernel, personas, contratos |
| `{{OPERADOR}}` | quem detém a alçada (nome) | kernel, políticas, alçadas, registros |
| `{{DOMINIO}}` · `{{EMAIL}}` | domínio e e-mail da operação | painéis, workflows, contratos |
| `{{BANCO}}` · `{{BANCO_DOMINIO}}` | o banco das notificações | rotina `financas-gmail` |
| `{{META_MRR}}` · `{{MRR_ESTAGIO_B}}` · `{{MRR_ESTAGIO_C}}` · `{{DATA_HORIZONTE}}` | norte e gates de estágio | `POLITICAS` §2, personas, gate de contratação |
| `{{MOTOR_DE_CAIXA}}` | o produto de ciclo curto que paga o mês | `POLITICAS` §2, `STATUS` |
| `{{VALOR_HORA_PISO}}` · `{{MARGEM_MINIMA}}` · `{{TETO_DESPESA}}` · `{{TETO_HORAS_MES}}` · `{{HORAS_ENTREGA_SEMANA}}` | pisos e tetos | `POLITICAS` §1, §4, §5 e todo método que ancora proposta |
| `{{TICKET_MAPA_NUCLEO}}` · `{{TICKET_MAPA_OPERACAO}}` · `{{TICKET_ALICERCE}}` · `{{TICKET_SITE}}` · `{{TICKET_ASSESSORIA}}` · `{{TICKET_ASSESSORIA_COMPLETA}}` · `{{TICKET_ASSESSORIA_LOCAL}}` · `{{SETUP_CORE_ESSENCIAL}}` · `{{MENSAL_CORE_ESSENCIAL}}` · `{{MONTAGEM_RETORNO}}` · `{{MENSAL_RETORNO}}` · `{{MONTAGEM_RETORNO_SDR}}` · `{{MENSAL_RETORNO_SDR}}` | a escada de ofertas | `POLITICAS` §5, `oferta.md`, `ICP.md` §4-bis, métodos de diagnóstico e prospecção |
| `{{VERBA_POR_TENTATIVA}}` | capital de teste de mídia por tentativa | `POLITICAS` §5, funil de VSL |
| `{{SUPABASE_URL}}` · `{{SUPABASE_ANON_KEY}}` · `{{HOSTINGER_CONTA}}` | integrações opcionais dos painéis | `980-web-design/painel-*/config.js`, `.github/workflows/` |
| `{{DATA_INSTANCIACAO}}` · `{{DATA}}` · `{{MES_ANO}}` | datas | `STATUS`, rodapés |

**Regra:** placeholder que você não sabe preencher vira `a calibrar`, nunca palpite. Campo inventado contamina toda peça produzida depois.

## 2-bis. Qual kernel a sua ferramenta lê

| Ferramenta | Lê | O que fazer |
|---|---|---|
| Claude Code | `CLAUDE.md` | nada; `AGENTS.md` é réplica mantida pelo `sincronizar.py` |
| Codex, GPT e outras que leem `AGENTS.md` | `AGENTS.md` | nada; é o mesmo kernel com outro nome — o Codex opera como agente principal (CEO) |
| Dois agentes (um principal, um executor na antessala) | principal: `CLAUDE.md` ou `AGENTS.md` · executor: `AGENTS-EXEC.md` | renomear `AGENTS-EXEC.md` para o nome que o executor lê, se for o caso |

O roteiro de entrevista para popular o repositório com o contexto da empresa está no `README.md`.

**macOS ou Linux:** comece por `40-operacao-rotinas/ferramentas/macos/README.md` e rode `./40-operacao-rotinas/ferramentas/macos/instalar-mac.sh`. Toda a documentação usa `python3`; o que era só Windows (agendador, `.bat`, atalho, caminho do Chrome) tem equivalente lá.

## 3. O dia 1, em ordem

1. **`CLAUDE.md` §1** — confirme a realidade operacional (uma pessoa, 100%). Se tiver sócio ou equipe, corrija aqui, em `STATUS.md` §4 e em `POLITICAS` §1 **no mesmo ato** — e nada vale sem instrumento escrito (`80-juridico/POLITICAS-JURIDICAS.md` §1).
2. **`PROJECT.md` e `SCOPE.md`** — identidade, dimensões, o vocabulário de trabalho do operador (`CLAUDE.md` §5.1 lê daqui).
3. **`00-core/POLITICAS-DE-DECISAO.md`** — todos os `{{…}}`. Os números são seus; as réguas não.
4. **`30-comercial/ICP.md`, `oferta.md`, `servicos.md`, `produtos.md`, `onboarding.md`** — o desenho é o método; preencha com a sua oferta. O que não tem dado fica `n=0`, escrito assim.
5. **`STATUS.md`** — §1 a §6. A tabela §7 (registro de métodos) já vem preenchida: ela é o que o verificador confere.
6. **`80-juridico/DADOS-DO-CONTRATADO.md`** — sua qualificação; os contratos puxam daqui.
7. **`10-skills/voz-operador.skill.md`** — fica esqueleto até a primeira call destilada (eixo 13 de `METODO-DESTILACAO-DE-CALLS.md`). Não invente a própria voz.
8. **`945-branding/01 - identidade visual/IDENTIDADE-VISUAL.md`** — quando houver marca decidida; antes disso, `ARQUETIPOS-DE-MARCA.md` + `METODO-KIT-DE-MARCA.md`.
9. **Git:** `git init`, remoto privado, e `.claude/settings.json` já chama `sincronizar.py` ao abrir e ao fechar a sessão (`CLAUDE.md` §11.6). Sem remoto, rode `sincronizar.py --sem-push`.
10. **Feche:** `python3 40-operacao-rotinas/ferramentas/verificar-propagacao.py` em ✅. Depois, **o primeiro pedido real pelo roteador** — e registre no `STATUS.md` o que o repositório não soube responder. É assim que ele passa a ser seu.

## 4. O que ficou de fora, de propósito

- Toda conta de cliente (`clientes/` vem só com o molde), prospects, parceiros, registros jurídicos e societários, finanças reais, extratos, áudios, transcrições, peças publicadas, site, referências de página e de criativo (imagens), livros de terceiros.
- A skill de voz do operador de origem (85 KB de uma pessoa) e os padrões linguísticos dela.
- A "tela" de apresentação da prospecção presencial e o treino (carregam a marca de origem): o método descreve as telas; você constrói as suas.
- Os registros de auditoria e verificação que instituíram regras (a lição de cada um está no método que ela mudou).
- O histórico de regras (`_legado/`): as pastas existem vazias, porque o procedimento de substituição (`CLAUDE.md` §7.1, item 3) precisa delas.

## 5. O que nunca mudar sem registrar

As REGRAS Nº 0, 1 e 2 (`CLAUDE.md` §8), a régua-mãe do §9, a saída mínima do §10 e o rastro do §11. Elas não são preferência da casa de origem: são o que fez o repositório funcionar como memória e como mecanismo de carga. Mudar é legítimo; **mudar sem registrar, no `STATUS.md` e no rodapé do arquivo, não.**

## 6. Os casos anonimizados

Vários métodos trazem "o caso que instituiu a regra" como narrativa genérica ("uma conta de assessoria em que…"). Onde um mesmo caso é citado várias vezes num arquivo, ele aparece como rótulo estável (`Conta A`, `Conta B`…). **São casos reais, anonimizados, não exemplos inventados** — a régua que nasceu deles é verificável pelo porquê que acompanha cada uma. Quando a sua operação produzir o próprio caso, substitua.
