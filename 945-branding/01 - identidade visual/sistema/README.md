# sistema/ — o sistema de criativos da marca

O que o operador constrói quando a identidade (`../IDENTIDADE-VISUAL.md`) estiver decidida:

| Arquivo | O que é | Quem consome |
|---|---|---|
| `tokens.css` | cor, tipografia, espaçamento e raio como variáveis CSS, a partir das tabelas §2 e §3 | `render.py`, `90-templates/prancha-de-escolha/`, `90-templates/kit-de-marca/` |
| `componentes/` | um HTML por tipo de criativo (§4), parametrizado | `render.py` |
| `render.py` | gera PNG de cada peça a partir de um JSON (`pecas-demo.json` como exemplo) usando Chrome headless | a produção de peças e a prancha |
| `pecas-demo.json` | exemplo de peça por tipo, para testar o sistema | `render.py` |

Regra: a peça nunca é desenhada "no gosto". Entra pelo tipo de criativo, com a referência medida (`960-referências criativos/LEIA-ME-MODELAGEM.md`), e passa pelo gate visual (§7 da identidade).
