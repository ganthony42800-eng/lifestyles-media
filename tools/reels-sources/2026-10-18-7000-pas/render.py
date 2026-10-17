import sys, math, subprocess, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
DUR = 28.5
N = int(DUR * FPS)
OUT = sys.argv[1]
SIG = sys.argv[2]
PREVIEW = len(sys.argv) > 3  # render only a few frames as stills

FD = "/usr/share/fonts/opentype/inter/"
def F(name, size): return ImageFont.truetype(FD + name, size)

CYAN = (94, 242, 224); VIOLET = (150, 130, 255); WHITE = (244, 244, 255)
GREY = (170, 172, 205); GOLD1 = (255, 214, 120); GOLD2 = (222, 150, 50)
ORANGE = (255, 150, 90); TEAL = (70, 220, 200)

# ---------- background ----------
rng = np.random.default_rng(7)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
bg = np.zeros((H, W, 3), np.float32)
top = np.array([14, 12, 40], np.float32); bot = np.array([4, 6, 14], np.float32)
t = (yy / H)[..., None]
bg += top * (1 - t) + bot * t
def blob(cx, cy, r, col, a):
    d = ((xx - cx) ** 2 + (yy - cy) ** 2) / (r * r)
    return np.exp(-d)[..., None] * np.array(col, np.float32) * a
bg += blob(540, 380, 520, (70, 50, 170), 0.55)
bg += blob(860, 1350, 480, (10, 110, 105), 0.45)
bg += blob(180, 1050, 380, (60, 40, 140), 0.30)
# stars
stars = []
for _ in range(260):
    x, y = rng.uniform(0, W), rng.uniform(0, H * 0.82)
    s = rng.choice([1, 1, 1, 2, 2, 3]); b = rng.uniform(0.3, 1.0)
    stars.append((x, y, s, b, rng.uniform(0, 6.28), rng.uniform(0.6, 2.0)))
bg_img = Image.fromarray(np.clip(bg, 0, 255).astype(np.uint8))
# perspective grid floor
g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
hz = 1500
for i in range(-14, 15):
    x0 = 540 + i * 40; x1 = 540 + i * 260
    gd.line([(x0, hz), (x1, H)], fill=(80, 200, 220, 38), width=2)
for k in range(1, 14):
    y = hz + (H - hz) * (k / 13) ** 1.8
    gd.line([(0, y), (W, y)], fill=(80, 200, 220, int(20 + 30 * k / 13)), width=2)
fade = Image.linear_gradient("L").resize((W, H - hz))
mask = Image.new("L", (W, H), 0); mask.paste(fade, (0, hz))
g.putalpha(Image.fromarray((np.array(g.split()[3], np.float32) * np.array(mask, np.float32) / 255).astype(np.uint8)))
bg_img = bg_img.convert("RGBA"); bg_img.alpha_composite(g)
# sparkle crosses
for (cx, cy) in [(860, 120), (90, 400), (980, 1180), (120, 1420)]:
    d = ImageDraw.Draw(bg_img)
    d.line([(cx - 16, cy), (cx + 16, cy)], fill=(220, 220, 255, 170), width=2)
    d.line([(cx, cy - 16), (cx, cy + 16)], fill=(220, 220, 255, 170), width=2)

# ---------- text helpers ----------
_cache = {}
def grad_fill(size, c1, c2):
    w, h = size
    a = np.linspace(0, 1, w, dtype=np.float32)[None, :, None]
    arr = np.array(c1, np.float32) * (1 - a) + np.array(c2, np.float32) * a
    arr = np.repeat(arr, h, axis=0)
    return Image.fromarray(arr.astype(np.uint8))

def text_layer(txt, font, color=WHITE, grad=None, glow=0, track=0, maxw=None):
    key = (txt, font.path, font.size, str(color), str(grad), glow, track)
    if key in _cache: return _cache[key]
    lines = txt.split("\n")
    asc, desc = font.getmetrics(); lh = int((asc + desc) * 1.08)
    def lw(s):
        if track == 0: return font.getlength(s)
        return sum(font.getlength(ch) + track for ch in s) - track
    w = int(max(lw(l) for l in lines)) + 2
    h = lh * len(lines)
    pad = glow * 3 + 10
    m = Image.new("L", (w + pad * 2, h + pad * 2), 0); d = ImageDraw.Draw(m)
    for i, l in enumerate(lines):
        x = pad + (w - lw(l)) / 2; y = pad + i * lh
        if track == 0: d.text((x, y), l, font=font, fill=255)
        else:
            for ch in l:
                d.text((x, y), ch, font=font, fill=255); x += font.getlength(ch) + track
    out = Image.new("RGBA", m.size, (0, 0, 0, 0))
    if grad: fill = grad_fill(m.size, *grad)
    else: fill = Image.new("RGB", m.size, color)
    if glow:
        gm = m.filter(ImageFilter.GaussianBlur(glow))
        gcol = grad_fill(m.size, *grad) if grad else Image.new("RGB", m.size, color)
        gl = gcol.convert("RGBA"); gl.putalpha(gm.point(lambda v: int(v * 0.85)))
        out.alpha_composite(gl)
    tl = fill.convert("RGBA"); tl.putalpha(m); out.alpha_composite(tl)
    _cache[key] = out
    return out

def place(canvas, layer, cx, y, alpha=1.0, dy=0, scale=1.0):
    if alpha <= 0.01: return
    L = layer
    if abs(scale - 1) > 0.003:
        L = L.resize((max(1, int(L.width * scale)), max(1, int(L.height * scale))), Image.BICUBIC)
    if alpha < 0.999:
        a = np.array(L.split()[3], np.float32) * alpha
        L = L.copy(); L.putalpha(Image.fromarray(a.astype(np.uint8)))
    canvas.alpha_composite(L, (int(cx - L.width / 2), int(y + dy - (L.height - layer.height) / 2)))

def ease(x): x = min(max(x, 0), 1); return 1 - (1 - x) ** 3
def env(t, t0, t1, fin=0.3, fout=0.25):
    """alpha + dy for element living from t0 to t1"""
    if t < t0 or t > t1: return 0, 0
    a_in = 0.3 + 0.7 * ease((t - t0) / fin); a_out = 1 - 0.7 * ease((t - (t1 - fout)) / fout) if t > t1 - fout else 1
    return a_in * a_out, (1 - a_in) * 40 - (1 - a_out) * 20

def rrect(size, radius, fill, outline=None, width=2):
    im = Image.new("RGBA", size, (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], radius, fill=fill, outline=outline, width=width)
    return im

# ---------- fonts ----------
fBlack = lambda s: F("InterDisplay-Black.otf", s)
fXB = lambda s: F("InterDisplay-ExtraBold.otf", s)
fSB = lambda s: F("InterDisplay-SemiBold.otf", s)
fMed = lambda s: F("Inter-Medium.otf", s)
fReg = lambda s: F("Inter-Regular.otf", s)

G_CV = (CYAN, VIOLET); G_GOLD = (GOLD1, GOLD2); G_WARN = (GOLD1, ORANGE)

sig_full = Image.open(SIG).convert("RGBA")
def sig(w):
    k = ("sig", w)
    if k not in _cache: _cache[k] = sig_full.resize((w, int(sig_full.height * w / sig_full.width)), Image.LANCZOS)
    return _cache[k]
PILL_TXT = "SPORT · SCIENCE"
_pt = text_layer(PILL_TXT, fMed(19), WHITE, track=2)
pill = rrect((300, 40), 20, (30, 30, 70, 200), (120, 120, 220, 160))
pill.alpha_composite(_pt, (int(150 - _pt.width / 2), -6))

# scene times
S = [0.0, 3.2, 6.6, 11.6, 15.2, 19.0, 22.0, 25.0, 28.5]
MINUS = "−"
G_ORA = (ORANGE, GOLD2)

# ---- step counter shared timing (audio.py uses the same) ----
C3 = (S[2] + 0.25, 2.8)   # start, duration 2000 -> 7000
C5 = (S[4] + 0.25, 2.4)   # 7000 -> 10000
def steps(t):
    if t < S[3]:
        return 2000 + 5000 * ease((t - C3[0]) / C3[1])
    return 7000 + 3000 * ease((t - C5[0]) / C5[1])
def fmt(n): return f"{int(n):,}".replace(",", " ")
def fmt_disp(n): return fmt(int(round(n / 50.0) * 50))

def benefit(s):
    u = (s - 2000) / 8000
    return 0.85 * (1 - math.exp(-(s - 2000) / 1800)) + 0.15 * u

CX0, CX1, CY0, CY1 = 170, 910, 660, 900  # chart box (layer coords): y0 top, y1 baseline
def sx(s): return CX0 + (CX1 - CX0) * (s - 2000) / 8000
def sy(b): return CY1 - (CY1 - CY0) * b

def counter_chart(L, d, t, a, dy, smax, s_from=2000):
    place(L, text_layer("PAS PAR JOUR", fMed(26), GREY, track=5), 540, 330, a, dy)
    place(L, text_layer(fmt_disp(smax), fBlack(170), grad=G_GOLD, glow=10), 540, 350, a, dy)
    if a <= 0: return
    A = int(255 * a)
    # axes
    d.line([(CX0, CY1 + dy), (CX1, CY1 + dy)], fill=(120, 120, 180, int(200 * a)), width=3)
    d.line([(CX0, CY0 - 10 + dy), (CX0, CY1 + dy)], fill=(120, 120, 180, int(140 * a)), width=2)
    # 7000 dashed marker
    x7 = sx(7000)
    for yy_ in range(CY0 - 10, CY1, 16):
        d.line([(x7, yy_ + dy), (x7, yy_ + 8 + dy)], fill=(150, 150, 210, int(120 * a)), width=2)
    for s_, lab in ((2000, "2 000"), (7000, "7 000"), (10000, "10 000")):
        tl = text_layer(lab.replace(" ", " "), fSB(28), GREY)
        place(L, tl, min(max(sx(s_), CX0 + 40), CX1 - 50), CY1 + 6, a, dy)
    place(L, text_layer("bénéfice", fMed(24), GREY, track=2), CX0 + 70, CY0 - 62, a, dy)
    # curve
    pts1, pts2 = [], []
    s = 2000.0
    while s <= smax + 1:
        p_ = (sx(s), sy(benefit(s)) + dy)
        (pts1 if s <= 7000 else pts2).append(p_)
        if s == 7000: pts2.append(p_)
        s += 50
    # fill under curve
    poly = pts1 + pts2[1:] if pts2 else pts1
    if len(poly) > 1:
        fl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); fd = ImageDraw.Draw(fl)
        fd.polygon(poly + [(poly[-1][0], CY1 + dy), (poly[0][0], CY1 + dy)], fill=CYAN + (int(38 * a),))
        L.alpha_composite(fl)
    gl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd_ = ImageDraw.Draw(gl)
    if len(pts1) > 1: gd_.line(pts1, fill=CYAN + (A,), width=14, joint="curve")
    if len(pts2) > 1: gd_.line(pts2, fill=VIOLET + (A,), width=14, joint="curve")
    L.alpha_composite(gl.filter(ImageFilter.GaussianBlur(9)))
    if len(pts1) > 1: d.line(pts1, fill=CYAN + (A,), width=7, joint="curve")
    if len(pts2) > 1: d.line(pts2, fill=VIOLET + (A,), width=7, joint="curve")
    px, py = poly[-1]
    d.ellipse([px - 12, py - 12, px + 12, py + 12], fill=WHITE + (A,))

def nuance(L, t, a):
    place(L, text_layer("Études d'observation : association, pas preuve de cause.", fReg(31), (210, 212, 238)), 540, 1330, a)

def frame(t):
    c = bg_img.copy()
    d = ImageDraw.Draw(c)
    for (x, y, s, b, ph, sp) in stars:
        v = b * (0.55 + 0.45 * math.sin(ph + t * sp))
        col = (int(200 * v + 40), int(205 * v + 40), int(255 * v))
        if s == 1: d.point((x, y), fill=col)
        else: d.ellipse([x - s / 2, y - s / 2, x + s / 2, y + s / 2], fill=col)
    ha = 1 - ease((t - S[7] + 0.1) / 0.3) if t > S[7] - 0.1 else 1
    if ha > 0:
        place(c, sig(360), 540, 70, ha)
        ln = Image.new("RGBA", (760, 2), (90, 220, 210, int(110 * ha))); c.alpha_composite(ln, (160, 205))
        place(c, pill, 540, 228, ha)

    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    # nuance line S3..S5 (continuous)
    if S[2] <= t < S[5]:
        na = ease((t - S[2]) / 0.3) * (1 - ease((t - (S[5] - 0.2)) / 0.2) if t > S[5] - 0.2 else 1)
        nuance(L, t, na)
    # ---- S1 hook ----
    if t < S[1]:
        a, dy = env(t, -1, S[1], fout=0.2); p = ease(t / 0.3)
        place(L, text_layer("Tu vises 10 000 pas ?".replace("10 000", "10 000"), fSB(62)), 540, 380, a, dy)
        # 10 000 struck -> 7 000
        old = text_layer("10 000", fBlack(100), (120, 122, 160))
        new = text_layer("7 000", fBlack(100), grad=G_GOLD, glow=10)
        arr = text_layer("→", fBlack(80), CYAN)
        ox, nx = 300, 745
        place(L, old, ox, 520, a, dy)
        ks = ease((t - 0.05) / 0.3)
        if ks > 0:
            y_ = 520 + old.height / 2 + 8 + dy
            x_a = ox - old.width / 2 + 18; x_b = ox + old.width / 2 - 18
            d.line([(x_a, y_), (x_a + (x_b - x_a) * ks, y_)], fill=ORANGE + (int(255 * a),), width=10)
        kn = ease((t - 0.2) / 0.3)
        place(L, arr, 532, 532, a * kn, dy)
        place(L, new, nx, 520 - new.height / 2 + old.height / 2, a * kn, dy + (1 - kn) * 30, 1.15 - 0.15 * kn)
        place(L, text_layer("7 000, c'est déjà\nbeaucoup.", fBlack(94), grad=G_CV, glow=14), 540, 760, a, dy, 1.03 - 0.03 * p)
    # ---- S2 study ----
    elif t < S[2]:
        t0, t1 = S[1], S[2]; a, dy = env(t, t0, t1, fout=0.2)
        card = _cache.get("card2")
        if card is None:
            card = rrect((780, 190), 28, (40, 40, 80, 175), (130, 130, 220, 130))
            l1 = text_layer("MÉTA-ANALYSE · 57 études", fXB(52), grad=G_CV, glow=6)
            l2 = text_layer("Ding et al., The Lancet Public Health, 2025", fSB(32), GREY)
            card.alpha_composite(l1, (int(390 - l1.width / 2), 0)); card.alpha_composite(l2, (int(390 - l2.width / 2), 100))
            _cache["card2"] = card
        place(L, card, 540, 380, a, dy)
        # 57 study tiles popping
        cols, tw, th, gx, gy = 10, 54, 68, 74, 92
        x0 = 540 - (cols - 1) * gx / 2; y0 = 680
        for i in range(57):
            ti = t0 + 0.15 + i * 0.03
            k = ease((t - ti) / 0.2)
            if k <= 0: continue
            r, cI = divmod(i, cols)
            if r == 5: cI += 1.5  # center last row of 7
            x = x0 + cI * gx; y = y0 + r * gy + dy + (1 - k) * 20
            al = int(255 * a * k)
            d.rounded_rectangle([x - tw / 2, y, x + tw / 2, y + th], 8, fill=(40, 40, 85, int(200 * a * k)), outline=CYAN + (al,), width=2)
            for j in range(3):
                d.line([(x - tw / 2 + 10, y + 16 + j * 14), (x + tw / 2 - 10 - (12 if j == 2 else 0), y + 16 + j * 14)], fill=(150, 150, 220, int(200 * a * k)), width=3)
    # ---- S3 counter + curve, -47 % ----
    elif t < S[3]:
        t0, t1 = S[2], S[3]; a, dy = env(t, t0, t1, fout=0.2)
        counter_chart(L, d, t, a, dy, steps(t))
        tr = C3[0] + C3[1]
        b = env(t, tr - 0.1, t1, fout=0.2)
        place(L, text_layer(MINUS + "47 %", fBlack(130), grad=G_CV, glow=14), 540, 960, b[0], b[1], 1.08 - 0.08 * ease((t - tr + 0.1) / 0.3))
        place(L, text_layer("de risque de décès", fBlack(64), grad=G_CV, glow=10), 540, 1140, b[0], b[1])
        c2 = env(t, tr + 0.4, t1, fout=0.2)
        place(L, text_layer("comparé à 2 000 pas par jour", fReg(36), GREY), 540, 1255, c2[0], c2[1])
    # ---- S4 other associations ----
    elif t < S[4]:
        t0, t1 = S[3], S[4]; a, dy = env(t, t0, t1, fout=0.2)
        place(L, text_layer("Aussi associé à :", fBlack(84), grad=G_CV, glow=12), 540, 340, a, dy)
        items = [("38", "démence"), ("25", "maladies cardiovasculaires"), ("22", "symptômes dépressifs")]
        for j, (n, lab) in enumerate(items):
            e = env(t, t0 + 0.25 + j * 0.35, t1, fout=0.2)
            key = ("s4", j)
            if key not in _cache:
                card = rrect((780, 170), 30, (35, 35, 75, 195), (120, 120, 210, 140))
                nl = text_layer(MINUS + n + " %", fBlack(76), grad=G_WARN, glow=6)
                card.alpha_composite(nl, (int(140 - nl.width / 2), int(85 - nl.height / 2)))
                ll = text_layer(lab, fSB(40))
                card.alpha_composite(ll, (270, int(85 - ll.height / 2)))
                _cache[key] = card
            place(L, _cache[key], 540, 520 + j * 200, e[0], e[1])
    # ---- S5 counter continues ----
    elif t < S[5]:
        t0, t1 = S[4], S[5]; a, dy = env(t, t0, t1, fout=0.2)
        counter_chart(L, d, t, a, dy, steps(t))
        b = env(t, t0 + 0.9, t1, fout=0.2)
        place(L, text_layer("Au-delà, le gain ralentit.", fBlack(66), grad=G_WARN, glow=10), 540, 990, b[0], b[1])
        c2 = env(t, t0 + 1.7, t1, fout=0.2)
        place(L, text_layer("10 000 reste un bon objectif si tu es déjà actif.", fReg(32), GREY), 540, 1125, c2[0], c2[1])
    # ---- S6 reveal ----
    elif t < S[6]:
        t0, t1 = S[5], S[6]; a, dy = env(t, t0, t1, fout=0.2)
        place(L, text_layer("Tu culpabilises sous les 10 000 ?", fSB(50)), 540, 540, a, dy)
        b = env(t, t0 + 0.35, t1, fout=0.2)
        place(L, text_layer("Tu es peut-être\ndéjà presque au max.", fBlack(72), grad=G_CV, glow=14), 540, 640, b[0], b[1], 1.05 - 0.05 * ease((t - t0 - 0.35) / 0.3))
        c2 = env(t, t0 + 1.0, t1, fout=0.2)
        place(L, text_layer("Et passer de 2 000 à 4 000 pas compte déjà.", fReg(34), GREY), 540, 900, c2[0], c2[1])
    # ---- S7 reflexes ----
    elif t < S[7]:
        t0, t1 = S[6], S[7]; a, dy = env(t, t0, t1, fout=0.2)
        place(L, text_layer("3 réflexes simples", fBlack(86), grad=G_CV, glow=12), 540, 340, a, dy)
        items = [("Appli Santé :", "regarde ta moyenne."), ("10 min de marche", "≈ 1 000 pas*"), ("Au téléphone ?", "Marche.")]
        for j, (l1, l2) in enumerate(items):
            e = env(t, t0 + 0.25 + j * 0.35, t1, fout=0.2)
            key = ("item", j)
            if key not in _cache:
                card = rrect((780, 150), 28, (35, 35, 75, 190), (120, 120, 210, 140))
                cd = ImageDraw.Draw(card); cd.ellipse([30, 43, 94, 107], outline=CYAN + (255,), width=3)
                n = text_layer(str(j + 1), fXB(36)); card.alpha_composite(n, (int(62 - n.width / 2), 75 - n.height // 2 - 2))
                a1 = text_layer(l1, fSB(40)); a2 = text_layer(l2, fSB(40), TEAL)
                card.alpha_composite(a1, (110, 14)); card.alpha_composite(a2, (110, 66))
                _cache[key] = card
            place(L, _cache[key], 540, 500 + j * 180, e[0], e[1])
        place(L, text_layer("*ordre de grandeur", fReg(30), GREY), 540, 1050, a * ease((t - t0 - 1.2) / 0.3), dy)
    # ---- S8 CTA ----
    else:
        t0 = S[7]; a, dy = env(t, t0, DUR + 1, fin=0.3)
        place(L, text_layer("Envoie ça à quelqu'un", fSB(66)), 540, 400, a, dy)
        place(L, text_layer("obsédé par\nsa montre.", fBlack(92), grad=G_CV, glow=12), 540, 490, a, dy)
        place(L, text_layer("Enregistre  ·  Abonne-toi pour la suite", fReg(34), GREY), 540, 790, a, dy)
        b = env(t, t0 + 0.3, DUR + 1)
        place(L, sig(760), 540, 870, b[0], b[1])
        place(L, text_layer("@lifestyles_hf", fSB(46), GOLD1), 540, 1140, b[0], b[1])
        place(L, text_layer("Source : Ding et al., Lancet Public Health, 2025", fReg(30), (210, 212, 238)), 540, 1230, b[0] * 0.9, b[1])
    c.alpha_composite(L, (0, 110))
    return c.convert("RGB")

if PREVIEW:
    times = [float(x) for x in sys.argv[4].split(",")] if len(sys.argv) > 4 else [0.0, 2.0, 5.5, 10.5, 14.0, 18.0, 21.0, 24.0, 27.0, 0.6]
    cols = 5; rows = (len(times) + cols - 1) // cols
    ims = [frame(x).resize((360, 640)) for x in times]
    sheet = Image.new("RGB", (360 * cols, 640 * rows))
    for i, im in enumerate(ims): sheet.paste(im, ((i % cols) * 360, (i // cols) * 640))
    sheet.save(OUT); frame(0.0).save(OUT.replace(".jpg", "_f0.jpg"), quality=92)
    sys.exit()

p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                      "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", OUT], stdin=subprocess.PIPE)
for i in range(N):
    p.stdin.write(frame(i / FPS).tobytes())
    if i % 150 == 0: print("frame", i, flush=True)
p.stdin.close(); p.wait()
print("done")
