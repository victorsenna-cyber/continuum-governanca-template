-- 25/10/2026 · apaga o esquema de abril do projeto continuum-finance (autorizado pelo {{OPERADOR}}: "pode apagar o esquema de abril").
-- O que havia, conferido antes de apagar: 153 linhas, todas de teste —
--   financial_categories 91 (o mesmo conjunto de 7 categorias repetido 13×) · financial_accounts 24 ("Conta Principal"/"Caixa" repetidas)
--   financial_transactions 21 ("Teste receita" R$ 1.000 / "Teste despesa" R$ 200, 12/04) · lancamentos 6 ("ARO Transportes" R$ 10.002, 11.111…,
--   "aluguel do prédio" R$ 6.000, 13–14/04) · audit_log 6 (logins de 27/05 a 02/06) · projetos 2 e pipeline 2 ("VS"/"CaSy") · fechamentos 1 (04/2026).
-- Fica: as tabelas financas_*, as funções financas_pode_ler e sincronizar_financas, e o usuário de Auth de abril (sem acesso ao painel).
drop trigger if exists on_auth_user_created on auth.users;
drop view if exists public.view_cash_balance, public.view_dre_month, public.view_payables_receivables cascade;
drop table if exists public.audit_log, public.conciliacao, public.configuracoes, public.contas_pagar, public.contas_receber,
  public.distribuicoes, public.fechamentos, public.financial_transactions, public.financial_accounts, public.financial_categories,
  public.financial_snapshots, public.lancamentos, public.movimentacoes_reservas, public.pipeline, public.projetos,
  public.reservas, public.usuarios cascade;
drop function if exists public.claim_owner(text), public.get_user_role(), public.handle_new_user() cascade;
