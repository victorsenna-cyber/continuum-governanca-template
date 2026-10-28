# Laya x árvore do roteador

O que é: teste de bancada para ver se o Laya 0.4.12 (checkpoint `multilingual`, CPU) decide a ÁRVORE
de um pedido (NEGOCIO, CONTA, LEITURA, ESCRITA, OPERACAO, CASA, JURIDICO), primeira decisão do `CLAUDE.md` §6.
Não está roteado nem em produção: é medição. Nada aqui altera o roteador.

Como rodar (python do venv; offline, usa o cache do modelo numa pasta `laya-teste` fora da Governança):
`<pasta laya-teste>\.venv\Scripts\python.exe -I avaliar.py` (zero-shot, ~2 min)
`... avaliar.py --treinar --epocas 2` (fine-tune em CPU, limite de 25 min de relógio, ~20 min)

O que mede: gera `dados/` (frases-sinal das 7 `ARVORE-*.md` + coluna "O pedido é sobre" do §6; 80/20 estratificado,
semente 42), acurácia zero-shot com as 7 descrições como opções, matriz 7x7, latência, estabilidade (ordem invertida),
e o mesmo depois do treino. Saída completa em `dados/resultado.json`; tabelas em `RESULTADO-<data>.md`.

Resultado de referência (n=86 na prova): zero-shot 23,3% (acaso 14,3%; classe majoritária 23,3%); 34/86 respostas mudam
ao inverter as opções. Treinado 2 épocas (19 min): 39,5%, ainda 33/86 instáveis. Não serve para rotear.
O modelo treinado (1,36 GB, >500 MB) fica fora do repositório, na pasta `laya-teste`.
