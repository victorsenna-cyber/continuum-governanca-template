# LANÇAMENTOS DA EMPRESA — {{EMPRESA}}

> **Tipo:** registro · **Aberto em:** `{{DATA_INSTANCIACAO}}` · **Escrito por:** rotina `financas-gmail` (`40-operacao-rotinas/FINANCAS-GMAIL.md`) e por sessões que conferem pagamento.
> **Fato de base:** `{{"sem CNPJ, a empresa recebe e paga pela conta pessoal do operador" | "conta PJ no banco X"}}`. Este arquivo separa o que é da empresa; o que é pessoal vai para `940-operador/FINANCAS.md` e **não entra aqui**.
> **Fonte:** e-mails de notificação do banco `{{BANCO}}` (ativados em `{{DATA}}`) e os extratos mensais em `extratos/`.
> 🔴 **Regra de pagamento de cliente:** combinado → *A receber*; recebido → *Receitas*; na confirmação, os dois movimentos no mesmo ato (risca a linha de *A receber* com `✅ recebido DD/MM`). O painel lê daqui.

## A receber

| Vencimento | Valor | Cliente | O quê | Certeza |
|---|---:|---|---|---|

## Receitas

| Data | Valor | Cliente | Referência | Gmail id |
|---|---:|---|---|---|

## Despesas

| Data | Valor | Fornecedor | Categoria | Gmail id |
|---|---:|---|---|---|
