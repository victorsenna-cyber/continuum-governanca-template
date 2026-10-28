#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sincronizar.py — CLAUDE.md §11.6, mecanizado.

Uma operação, igual no local (Windows) e na nuvem (sessão web, branch claude/...):
  1. commita tudo o que mudou na pasta (git add -A)
  2. traz a main do GitHub e mescla no ponto atual (merge, nunca rebase)
  3. regenera o AGENTS.md (cabeçalho do atual + corpo do CLAUDE.md vigente): réplica do kernel para quem lê AGENTS.md
  4. publica: HEAD → main  (e HEAD → a própria branch, se não for a main)

Conflitos:
  AGENTS.md           → resolvido sozinho (é gerado: regenera do CLAUDE.md mesclado)
  qualquer outro      → a mescla é desfeita, nada se perde, e o conflito é reportado

Rodado pelos hooks do .claude/settings.json (SessionStart e Stop) e à mão:
  python 40-operacao-rotinas/ferramentas/sincronizar.py [-m "mensagem"]
  --hook   modo hook: lê o JSON do Claude Code no stdin; em conflito no Stop,
           sai com código 2 para o Claude resolver (uma vez — sem laço)
  --sem-push   commita e mescla, mas não publica
"""
import io, json, os, subprocess, sys, time, socket

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AUTO = {"AGENTS.md"}


def git(*args, ok=False):
    r = subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0 and not ok:
        raise RuntimeError(f"git {' '.join(args)}: {(r.stderr or r.stdout).strip()[-800:]}")
    return r


def regenerar_agents():
    pa, pc = os.path.join(RAIZ, "AGENTS.md"), os.path.join(RAIZ, "CLAUDE.md")
    if not (os.path.exists(pa) and os.path.exists(pc)):
        return False
    a = io.open(pa, encoding="utf-8").read()
    c = io.open(pc, encoding="utf-8").read()
    if "<<<<<<<" in a:   # conflito: o cabeçalho (§0) vem da nossa versão
        a = git("show", "HEAD:AGENTS.md").stdout
    i, j = a.find("## 1. PAPEL"), c.find("## 1. PAPEL")
    if i < 0 or j < 0:
        return False
    novo = a[:i] + c[j:].replace("este `CLAUDE.md`", "este `AGENTS.md`")  # AGENTS.md é réplica do kernel; só a autorreferência muda
    if novo != io.open(pa, encoding="utf-8").read():
        io.open(pa, "w", encoding="utf-8", newline="").write(novo)
        return True
    return False


def commitar(msg):
    git("add", "-A")
    if git("diff", "--cached", "--quiet", ok=True).returncode != 0:
        git("commit", "-q", "-m", msg)
        return True
    return False


def mesclar_main():
    """Mescla origin/main no HEAD. Devolve lista de conflitos não resolvíveis (vazia = ok)."""
    git("fetch", "-q", "origin", "main")
    if git("merge-base", "--is-ancestor", "origin/main", "HEAD", ok=True).returncode == 0:
        return []
    r = git("merge", "--no-edit", "-q", "origin/main", ok=True)
    if r.returncode == 0:
        return []
    conflitos = [l for l in git("-c", "core.quotepath=false", "diff", "--name-only", "--diff-filter=U").stdout.splitlines() if l]
    duros = [f for f in conflitos if f not in AUTO]
    if duros:
        git("merge", "--abort", ok=True)
        return duros
    regenerar_agents()
    git("add", "-A")
    git("commit", "-q", "--no-edit")
    return []


def main():
    hook = "--hook" in sys.argv
    sem_push = "--sem-push" in sys.argv
    msg = None
    if "-m" in sys.argv:
        msg = sys.argv[sys.argv.index("-m") + 1]
    evento, repetido = {}, False
    if hook:
        try:
            evento = json.load(sys.stdin)
        except Exception:
            evento = {}
        repetido = bool(evento.get("stop_hook_active"))

    if os.name == "nt":
        git("config", "core.fileMode", "false", ok=True)

    ramo = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    onde = "nuvem" if ramo.startswith("claude/") else socket.gethostname()
    carimbo = time.strftime("%d/%m/%Y %H:%M")
    try:
        if git("rev-parse", "-q", "--verify", "MERGE_HEAD", ok=True).returncode == 0:
            raise RuntimeError("há uma mescla em andamento — resolva os conflitos e rode de novo")
        commitar(msg or f"sync ({onde}): {carimbo}")
        duros = mesclar_main()
        if duros:
            txt = ("🔴 sincronizar: conflito com a main em " + ", ".join(duros) +
                   ". A mescla foi desfeita e nada se perdeu. Resolver: `git merge origin/main`, "
                   "editar os arquivos (manter as duas versões quando ambas forem válidas), "
                   "`git add -A`, `git commit`, e rodar o sincronizar.py de novo.")
            print(txt, file=sys.stderr)
            if hook and evento.get("hook_event_name") == "Stop" and not repetido:
                sys.exit(2)
            sys.exit(0 if hook else 1)
        if regenerar_agents():
            commitar(f"AGENTS.md regenerado ({onde}): {carimbo}")
        if not sem_push:
            for tentativa in range(3):
                r = git("push", "-q", "origin", "HEAD:main", ok=True)
                if r.returncode == 0:
                    break
                if mesclar_main():
                    raise RuntimeError("main mudou durante o push e gerou conflito")
            else:
                raise RuntimeError("push para a main recusado: " + r.stderr.strip()[-300:])
            if ramo not in ("main", "HEAD"):
                git("push", "-q", "-u", "origin", f"HEAD:{ramo}", ok=True)
        print(f"✅ sincronizado ({onde}, {ramo} → main) {carimbo}")
    except RuntimeError as e:
        print(f"🔴 sincronizar: {e}", file=sys.stderr)
        sys.exit(0 if hook else 1)


if __name__ == "__main__":
    main()
