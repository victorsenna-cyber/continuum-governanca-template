# Termos de busca — Places API (modelo: ICP de terapias holísticas / espiritualidade)

> ⚠️ **MODELO — a lista abaixo é o exemplo de um nicho. Substitua pelos termos do SEU ICP (`30-comercial/ICP.md`), mantendo a estrutura: tiers, exclusões e notas de operação.**
> **Tipo:** ativo operacional de prospecção · Consumidor: sistema de scraping do Continuum OS → CRM
> Padrão de query (Text Search): `"<termo> em <cidade>"` ou `"<termo> <bairro> <cidade>"` para adensar. Rodar por cidade-alvo, deduplicar por place_id/telefone antes de sincronizar.
> **Filtro de qualificação primário: ausência de `websiteUri`** (lead com ficha no mapa e sem site = dor exata do produto). `businessStatus = OPERATIONAL` obrigatório.

## Campos a capturar → slots do script (`scripts-whatsapp.md`)

| Campo Places | Slot / uso |
|---|---|
| displayName | nome (regra do "você": se for nome de pessoa, falamos com ela; nome fantasia só se real) |
| termo que encontrou | `[modalidade]` |
| cidade/bairro (formattedAddress) | `[cidade]` |
| websiteUri ausente / só ficha | `[estado digital]` (é o fato que a copy afirma) |
| rating + userRatingCount | contexto de qualificação (muitas avaliações + sem site = lead quente) |
| telefone | canal WhatsApp (validar formato) |

## Tier 1 — núcleo do ICP (rodar primeiro)

terapeuta holística · terapias holísticas · espaço holístico · espaço terapêutico · centro de terapias holísticas
taróloga · tarot · tarot terapêutico · leitura de tarot · baralho cigano · cartomante
reiki · terapeuta reiki · mestre de reiki
terapias integrativas · terapeuta integrativa · práticas integrativas
constelação familiar · consteladora familiar
thetahealing · barras de access · access consciousness
terapeuta quântica · mesa radiônica · radiestesia · apometria
florais de bach · terapeuta floral
aromaterapia · aromaterapeuta · cromoterapia · cristaloterapia
astróloga · astrologia · mapa astral · numerologia · numeróloga
xamanismo · vivência xamânica · terapeuta xamânica
canalização · terapeuta transpessoal · hipnoterapia

## Tier 2 — adjacente corpo-energia (rodar após saturar Tier 1)

massagem ayurvédica · ayurveda · terapeuta ayurvédica
reflexologia podal · massoterapia · spa holístico
yoga · estúdio de yoga · meditação · mindfulness
acupuntura · auriculoterapia *(mais clínico: qualificar com mais cuidado, linguagem menos mística)*

## Tier 3 — espaços e lojas do meio (produto site também serve)

loja esotérica · loja de cristais · espaço esotérico · casa de terapias

## Exclusões (anti-ICP — não sincronizar)

Igrejas, terreiros, centros espíritas e instituições religiosas (não vendem serviço nesse modelo) · clínicas médicas/estéticas grandes (outro ICP) · registro duplicado do mesmo profissional em dois endereços.

## Notas de operação

1. **Quem não aparece no Places:** mentoras e terapeutas 100% online (sem endereço). Esse recorte vem por Instagram, não por Places — canal separado, `a calibrar`.
2. Cidades-alvo iniciais: `<cidade-alvo>` e a região metropolitana dela; expandir por capitais com densidade do nicho. Registrar no OS quais cidades/termos já rodaram.
3. Termo novo descoberto em campo (lead usa palavra que não está aqui) → adicionar aqui via atualização registrada, não só no scraper. Este arquivo é a fonte; o scraper é o consumidor.

---
*Fonte do ICP: `30-comercial/ICP.md` + `PROJECT.md` (pertencimento). Handoff: `50-integracoes-dados/OS-STATUS.md` (execuções reportadas lá).*
