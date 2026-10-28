"""Dashboard fixo de resultado de tráfego em PDF (A4 deitado, uma página), no visual do painel de resultado.

Uso:  python3 gerar_dashboard.py <dados.json>
Gera <nome>.html e <nome>.pdf na pasta do JSON (ou em "saida", se o JSON disser). Molde dos dados: exemplo.json.
"""
import base64, json, pathlib, subprocess, sys

AQUI = pathlib.Path(__file__).resolve().parent
GOV = AQUI.parents[1]
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))), '40-operacao-rotinas', 'ferramentas'))
from navegador import chrome_path  # noqa: E402  Chrome em Windows, macOS e Linux (ou CHROME=<caminho>)
CHROME = chrome_path()
LOGO = GOV / "40-operacao-rotinas/ferramentas/painel-resultado/logo-continuum.png"


def brl(v, d=2):
    s = f"{v:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def topo_escala(v, passos=4):
    """Teto do eixo: múltiplo 'redondo' acima do maior valor."""
    import math
    bruto = v * 1.05 / passos
    mag = 10 ** math.floor(math.log10(bruto)) if bruto > 0 else 1
    for m in (1, 2, 2.5, 5, 10):
        if m * mag >= bruto:
            return m * mag * passos
    return 10 * mag * passos


W, H = 486, 222
PL, PR, PT, PB = 30, 6, 18, 26
pw, ph = W - PL - PR, H - PT - PB


def grid(maxv, passos, fmt):
    g = ""
    for i in range(passos + 1):
        v = maxv * i / passos
        y = PT + ph - ph * v / maxv
        g += f'<line x1="{PL}" x2="{W-PR}" y1="{y:.1f}" y2="{y:.1f}" class="gl"/>'
        g += f'<text x="{PL-8}" y="{y+4:.1f}" text-anchor="end">{fmt(v)}</text>'
    return g


def barras(serie):
    maxv = topo_escala(max(c for _, _, c in serie))
    s = grid(maxv, 4, lambda v: f"{v:.0f}")
    slot = pw / len(serie); bw = min(34, slot * .6)
    for i, (d, g, c) in enumerate(serie):
        x = PL + slot * i + (slot - bw) / 2
        h = ph * c / maxv; y = PT + ph - h; r = min(4, h / 2)
        s += (f'<path d="M{x:.1f},{PT+ph:.1f} V{y+r:.1f} Q{x:.1f},{y:.1f} {x+r:.1f},{y:.1f} '
              f'H{x+bw-r:.1f} Q{x+bw:.1f},{y:.1f} {x+bw:.1f},{y+r:.1f} V{PT+ph:.1f} Z" '
              f'class="bar{" fim" if i == len(serie)-1 else ""}"/>')
        s += f'<text x="{x+bw/2:.1f}" y="{y-6:.1f}" text-anchor="middle" class="val">{c}</text>'
        s += f'<text x="{x+bw/2:.1f}" y="{H-8}" text-anchor="middle">{d}</text>'
    return s


def linha(serie):
    vals = [g / c for _, g, c in serie]
    maxv = topo_escala(max(vals))
    s = grid(maxv, 4, lambda v: brl(v, 0) if v == int(v) else brl(v, 1))
    slot = pw / len(serie)
    pts = [(PL + slot * i + slot / 2, PT + ph - ph * v / maxv, v, d) for i, ((d, _, _), v) in enumerate(zip(serie, vals))]
    s += '<polyline class="ln" points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y, *_ in pts) + '"/>'
    for x, y, v, d in pts:
        s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" class="pt"/>'
        s += f'<text x="{x:.1f}" y="{y-11:.1f}" text-anchor="middle" class="val">{brl(v)}</text>'
        s += f'<text x="{x:.1f}" y="{H-8}" text-anchor="middle">{d}</text>'
    return s


def kpi(rot, val, sub="", dest=False):
    return (f'<div class="kpi{" dest" if dest else ""}"><div class="kr">{rot}</div>'
            f'<div class="kv">{val}</div><div class="ks">{sub}</div></div>')


def linha_tab(c, cls=""):
    seg = "—" if c.get("seguidores") is None else c["seguidores"]
    vis = "—" if c.get("visitas") is None else c["visitas"]
    return (f'<tr class="{cls}"><td class="nm">{c["nome"]}<span>{c.get("detalhe","")}</span></td>'
            f'<td>R$ {brl(c["gasto"])}</td><td class="hl">{c["conversas"]}</td>'
            f'<td class="hl">R$ {brl(c["gasto"]/c["conversas"])}</td>'
            f'<td>R$ {brl(c["gasto"]/c["impressoes"]*1000)}</td><td>{brl(c["impressoes"],0)}</td>'
            f'<td>{brl(c["alcance"],0)}</td><td>{brl(c["impressoes"]/c["alcance"])}</td>'
            f'<td>{vis}</td><td>{seg}</td><td>{brl(c["conversas"]/c["impressoes"]*1000, 1)}</td></tr>')


def gerar(dados_path):
    dp = pathlib.Path(dados_path).resolve()
    D = json.loads(dp.read_text(encoding="utf-8"))
    camps = D["campanhas"]
    soma = lambda k: sum(c.get(k) or 0 for c in camps)
    T = dict(nome="Total", detalhe=D["periodo"], gasto=soma("gasto"), conversas=soma("conversas"),
             impressoes=soma("impressoes"), alcance=soma("alcance"),
             visitas=soma("visitas"), seguidores=soma("seguidores"))
    serie = [(p["data"], p["gasto"], p["conversas"]) for p in D["serie"]]
    logo = base64.b64encode(LOGO.read_bytes()).decode()
    css = (AQUI / "estilo.css").read_text(encoding="utf-8")
    chips = "".join(f'<div class="chip">{c}</div>' for c in D["chips"])
    kpis = "".join([
        kpi("Investido", "R$ " + brl(T["gasto"]), f'de R$ {brl(D["verba"])} de verba' if D.get("verba") else ""),
        kpi("Conversas", T["conversas"], "iniciadas no WhatsApp", True),
        kpi("Custo por conversa", "R$ " + brl(T["gasto"] / T["conversas"]), "média do período", True),
        kpi("Impressões", brl(T["impressoes"], 0), "CPM R$ " + brl(T["gasto"] / T["impressoes"] * 1000)),
        kpi("Visitas ao perfil", T["visitas"], "R$ " + brl(T["gasto"] / T["visitas"]) + " por visita" if T["visitas"] else ""),
        kpi("Seguidores", "+" + str(T["seguidores"]), "Instagram"),
    ])
    linhas = "".join(linha_tab(c) for c in camps) + (linha_tab(T, "tot") if len(camps) > 1 else "")
    html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}</style></head><body><div class="pg">
<div class="top"><img src="data:image/png;base64,{logo}" alt="Continuum"><div class="meta">{chips}</div></div>
<div class="kpis">{kpis}</div>
<div class="row">
<div class="card"><div class="ct">Conversas acumuladas<span>por dia de leitura</span></div><svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{barras(serie)}</svg></div>
<div class="card"><div class="ct">Custo por conversa acumulado (R$)<span>por dia de leitura</span></div><svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{linha(serie)}</svg></div>
</div>
<div class="card" style="padding-bottom:4px"><div class="ct">Por campanha</div>
<table><thead><tr><th>Campanha</th><th>Investido</th><th>Conversas</th><th>Custo/conversa</th><th>CPM</th><th>Impressões</th><th>Alcance</th><th>Frequência</th><th>Visitas perfil</th><th>Seguidores</th><th>Conv./mil impr.</th></tr></thead>
<tbody>{linhas}</tbody></table>
<div class="nota">{D.get("nota","")}</div></div>
</div></body></html>"""
    saida = (dp.parent / D["saida"]) if D.get("saida") else dp.parent
    saida.mkdir(parents=True, exist_ok=True)
    hp = saida / f'{D["arquivo"]}.html'
    hp.write_text(html, encoding="utf-8")
    pdf = saida / f'{D["arquivo"]}.pdf'
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=8000", f"--print-to-pdf={pdf}", hp.as_uri()], check=True, capture_output=True)
    try:
        import fitz
        doc = fitz.open(pdf)
        prev = saida / f'{D["arquivo"]}.png'
        doc[0].get_pixmap(dpi=110).save(str(prev))
        print(f"{pdf}\n{len(doc)} página(s) · prévia: {prev}")
    except ImportError:
        print(pdf)


if __name__ == "__main__":
    gerar(sys.argv[1])
