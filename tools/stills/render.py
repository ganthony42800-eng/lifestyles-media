#!/usr/bin/env python3
"""Visuels fixes Lifestyles (stories motivation 9:16 et publications feed 4:5) rendus en HTML/CSS par Chromium.

Usage : python3 tools/stills/render.py <spec.json> <dossier_sortie>
spec.json = liste d'objets {"type": "story" | "post", "file": "story-01.png", ...champs du gabarit}

Gabarit « story » (motivation / conditionnement) :
  theme   : sport | travail | assiduite | exigence | einstein | mental
  kicker  : petite étiquette en haut (ex. « ASSIDUITÉ »)
  quote   : texte principal (HTML simple autorisé : <b>, <em>, <br>)
  author  : signature de la citation (vide pour une maxime Lifestyles)
  source  : source exacte en petit (obligatoire pour une citation ou un chiffre)
  cta     : petite ligne d'action (ex. « Envoie-la à quelqu'un qui reprend lundi »)
Gabarit « post » (style feed ChatGPT : noir profond, titre capitales or, sous-titre, signature) :
  title, subtitle, foot (petite ligne de source), theme
La signature officielle brand/signature-officielle.png est collée telle quelle (jamais redessinée).
"""
import json, os, sys, html, http.server, functools, threading
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FONTS = os.path.join(ROOT, "tools", "motion-engine", "fonts")

THEMES = {  # fond, halo 1, halo 2, accent, accent clair
    "sport":     ("#03110D", "#0E8F6A", "#14C8A0", "#3EF0C0", "#C9FFF0"),
    "travail":   ("#05061A", "#3B3FD8", "#8C6CFF", "#9C8CFF", "#E4DEFF"),
    "assiduite": ("#0C0904", "#B8862B", "#F2C46B", "#F7D58A", "#FFF3D6"),
    "exigence":  ("#120405", "#B2262B", "#FF7A3A", "#FF8A5B", "#FFE2D2"),
    "einstein":  ("#07051A", "#5B3BD8", "#F2C46B", "#F2C46B", "#F4EEFF"),
    "mental":    ("#030B14", "#1667C8", "#3FD3F5", "#6FE3FF", "#DDF7FF"),
}

CSS = """
@font-face{font-family:IDBk;src:url(/fonts/InterDisplay-Black.otf)}
@font-face{font-family:IDXb;src:url(/fonts/InterDisplay-ExtraBold.otf)}
@font-face{font-family:IDSb;src:url(/fonts/InterDisplay-SemiBold.otf)}
@font-face{font-family:IDMd;src:url(/fonts/InterDisplay-Medium.otf)}
@font-face{font-family:IDLi;src:url(/fonts/InterDisplay-LightItalic.otf)}
*{box-sizing:border-box}html,body{margin:0;overflow:hidden;background:var(--bg)}
.stage{position:relative;width:var(--w);height:var(--h);overflow:hidden;background:var(--bg)}
.halo{position:absolute;border-radius:50%;filter:blur(90px);opacity:.55}
.floor{position:absolute;left:-40%;width:180%;height:900px;bottom:-260px;transform:perspective(700px) rotateX(72deg);
  background-image:linear-gradient(var(--a1) 1.5px,transparent 1.5px),linear-gradient(90deg,var(--a1) 1.5px,transparent 1.5px);
  background-size:90px 90px;opacity:.16;-webkit-mask:linear-gradient(to top,#000 10%,transparent 85%);mask:linear-gradient(to top,#000 10%,transparent 85%)}
.ring{position:absolute;border-radius:50%;border:2px solid var(--a1);opacity:.22}
.dot{position:absolute;border-radius:50%;background:var(--a2);box-shadow:0 0 12px var(--a1)}
.grain{position:absolute;inset:0;opacity:.13;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 45%,rgba(0,0,0,.72) 100%)}
.sig{position:absolute;left:50%;transform:translateX(-50%);opacity:.95}
.hdl{position:absolute;left:0;right:0;text-align:center;font-family:IDMd;color:rgba(255,255,255,.75);letter-spacing:.05em}
.pill{position:absolute;left:50%;transform:translateX(-50%);padding:0 34px;border-radius:999px;font-family:IDSb;letter-spacing:.22em;white-space:nowrap;
  color:var(--a2);border:2px solid var(--a1);background:color-mix(in srgb,var(--a1) 14%,transparent);box-shadow:0 0 22px color-mix(in srgb,var(--a1) 45%,transparent)}
.q{position:absolute;left:90px;right:90px;color:#fff;text-shadow:0 6px 40px rgba(0,0,0,.6)}
.q b{font-family:IDBk;background:linear-gradient(180deg,var(--a4) 0%,var(--a2) 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 0 18px color-mix(in srgb,var(--a1) 55%,transparent))}
.mark{position:absolute;font-family:Georgia,'DejaVu Serif',serif;font-weight:700;line-height:1;color:var(--a1);opacity:.9;filter:drop-shadow(0 0 20px var(--a1))}
.bar{position:absolute;height:6px;border-radius:3px;background:linear-gradient(90deg,var(--a1),transparent)}
.au{position:absolute;left:90px;right:90px;font-family:IDXb;color:var(--a2);letter-spacing:.06em}
.src{position:absolute;left:90px;right:90px;font-family:IDMd;color:rgba(255,255,255,.62)}
.cta{position:absolute;left:90px;right:90px;font-family:IDSb;color:#fff;opacity:.92}
.cta i{font-style:normal;color:var(--a2)}
.ptitle{position:absolute;left:84px;right:84px;font-family:IDBk;text-transform:uppercase;line-height:1.04;letter-spacing:-.01em;
  background:linear-gradient(180deg,#FFF3D6 0%,#F2C46B 45%,#B8862B 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 4px 30px rgba(242,196,107,.25))}
.psub{position:absolute;left:84px;right:84px;font-family:IDMd;color:rgba(255,255,255,.86);line-height:1.32}
.psub b{font-family:IDBk;color:#3EF0C0}
.pline{position:absolute;left:84px;width:140px;height:5px;border-radius:3px;background:linear-gradient(90deg,#F2C46B,#3EF0C0)}
.wm{position:absolute;font-family:IDBk;white-space:nowrap;line-height:.9;color:transparent;-webkit-text-stroke:2px var(--a1);opacity:.34;letter-spacing:-.02em}
.pfoot{position:absolute;left:84px;right:84px;font-family:IDMd;color:rgba(255,255,255,.55)}
"""


def deco(seed, w, h, a1, a2):
    import random
    R = random.Random(seed)
    out = [f'<div class="halo" style="left:{-200+R.randint(0,200)}px;top:{int(h*0.12)}px;width:{int(w*0.9)}px;height:{int(w*0.9)}px;background:{a1}"></div>',
           f'<div class="halo" style="right:{-300+R.randint(0,150)}px;top:{int(h*0.5)}px;width:{int(w*0.8)}px;height:{int(w*0.8)}px;background:{a2};opacity:.3"></div>',
           '<div class="floor"></div>']
    cx, cy = w * 0.5, h * 0.47
    for r in (420, 560, 720):
        out.append(f'<div class="ring" style="left:{cx-r}px;top:{cy-r}px;width:{2*r}px;height:{2*r}px;opacity:{0.08+0.14*R.random():.2f}"></div>')
    for _ in range(70):
        s = R.choice([2, 2, 3, 3, 4, 6])
        out.append(f'<div class="dot" style="left:{R.randint(0,w)}px;top:{R.randint(0,h)}px;width:{s}px;height:{s}px;opacity:{0.15+0.7*R.random():.2f}"></div>')
    return "\n".join(out)


def story_html(it, i):
    bg, a1, a2, a3, a4 = THEMES[it.get("theme", "mental")]
    W, H = 1080, 1920
    q = it["quote"]
    n = len(html.unescape(q.replace("<b>", "").replace("</b>", "").replace("<br>", " ")))
    fs = 104 if n < 40 else 92 if n < 60 else 80 if n < 85 else 70 if n < 120 else 62
    body = f"""
<div class="stage" style="--w:{W}px;--h:{H}px;--bg:{bg};--a1:{a1};--a2:{a3};--a4:{a4}">
{deco(1000+i, W, H, a1, a2)}
<div class="wm" style="left:-30px;top:1250px;font-size:{int(it.get('wmsize',230))}px;transform:rotate(-6deg)">{html.escape(it.get('wm',''))}</div>
<div class="vig"></div><div class="grain"></div>
<img class="sig" src="/brand/signature-officielle.png" style="top:150px;width:300px">
<div class="hdl" style="top:252px;font-size:26px">@lifestyles_hf</div>
<div class="pill" style="top:330px;height:64px;line-height:62px;font-size:28px">{html.escape(it['kicker'])}</div>
{'<div class="mark" id="mk" style="left:78px;font-size:200px">“</div>' if it.get('author') else ''}
<div class="q" style="top:0px;font-family:IDXb;font-size:{fs}px;line-height:1.1">{q}</div>
<div class="bar" id="bar" style="left:90px;width:180px"></div>
<div class="au" id="au" style="font-size:38px">{html.escape(it.get('author',''))}</div>
<div class="src" id="src" style="font-size:27px;line-height:1.35">{html.escape(it.get('source',''))}</div>
<div class="cta" style="top:1500px;font-size:36px;line-height:1.3">{it.get('cta','')}</div>
</div>
<script>
const q=document.querySelector('.q');const qh=q.getBoundingClientRect().height;const qt=Math.max(560,Math.round(930-qh/2));q.style.top=qt+'px';const mk=document.getElementById('mk');if(mk)mk.style.top=(qt-150)+'px';const b=q.getBoundingClientRect();let y=b.bottom+46;
const bar=document.getElementById('bar');bar.style.top=y+'px';y+=34;
const au=document.getElementById('au');if(au.textContent.trim()){{au.style.top=y+'px';y+=au.getBoundingClientRect().height+12;}}
const s=document.getElementById('src');s.style.top=y+'px';
window.__overflow=(s.getBoundingClientRect().bottom>1470);
</script>"""
    return W, H, body


def post_html(it, i):
    bg, a1, a2, a3, a4 = THEMES[it.get("theme", "sport")]
    W, H = 1080, 1350
    body = f"""
<div class="stage" style="--w:{W}px;--h:{H}px;--bg:#040807;--a1:{a1};--a2:{a3};--a4:{a4}">
{deco(2000+i, W, H, '#0E8F6A', '#B8862B')}
<div class="vig"></div><div class="grain"></div>
<img class="sig" src="/brand/signature-officielle.png" style="top:56px;width:270px">
<div class="ptitle" id="t" style="top:300px;font-size:{it.get('size',104)}px">{it['title']}</div>
<div class="pline" id="l"></div>
<div class="psub" id="s" style="font-size:44px">{it['subtitle']}</div>
<div class="wm" style="right:-20px;bottom:40px;font-size:{it.get('wmsize',420)}px;-webkit-text-stroke:3px #F2C46B;opacity:.16">{html.escape(it.get('wm',''))}</div>
<div class="pfoot" style="bottom:70px;font-size:26px">{html.escape(it.get('foot',''))}</div>
</div>
<script>
const t=document.getElementById('t').getBoundingClientRect();const l=document.getElementById('l');l.style.top=(t.bottom+44)+'px';
const s=document.getElementById('s');s.style.top=(t.bottom+90)+'px';
window.__overflow=(s.getBoundingClientRect().bottom>1240);
</script>"""
    return W, H, body


class H(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        p = path.split("?")[0]
        if p.startswith("/fonts/"): return os.path.join(FONTS, p[7:])
        if p.startswith("/brand/"): return os.path.join(ROOT, "brand", p[7:])
        return os.path.join(self.server.tmpdir, p.lstrip("/"))
    def log_message(self, *a): pass


def main():
    spec = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
    import tempfile
    tmp = tempfile.mkdtemp()
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H); srv.tmpdir = tmp
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"])
        for i, it in enumerate(spec):
            W, Hh, body = (story_html if it["type"] == "story" else post_html)(it, i)
            open(os.path.join(tmp, f"p{i}.html"), "w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
            pg = b.new_page(viewport={"width": W, "height": Hh})
            pg.goto(f"http://127.0.0.1:{srv.server_address[1]}/p{i}.html")
            pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            pg.evaluate("Promise.all(Array.from(document.images).map(i=>i.decode().catch(()=>{})))")
            pg.evaluate("(()=>{const s=document.querySelectorAll('script');eval(s[s.length-1].textContent)})()")
            if pg.evaluate("window.__overflow"): print("⚠️ DÉBORDEMENT :", it["file"])
            pg.screenshot(path=os.path.join(out, it["file"]))
            pg.close(); print("ok", it["file"])
        b.close()


if __name__ == "__main__":
    main()
