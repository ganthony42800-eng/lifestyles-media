import sys, math, subprocess, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
DUR = 25.0
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
    a_in = ease((t - t0) / fin); a_out = 1 - ease((t - (t1 - fout)) / fout) if t > t1 - fout else 1
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
pill = rrect((300, 40), 20, (30, 30, 70, 200), (120, 120, 220, 160))
pill.alpha_composite(text_layer("SOMMEIL · SCIENCE", fMed(19), WHITE, track=2), (int(150 - text_layer("SOMMEIL · SCIENCE", fMed(19), WHITE, track=2).width / 2), -6))

# scene times
S = [0.0, 3.4, 7.6, 11.2, 14.4, 17.8, 21.4, 25.0]

def frame(t):
    c = bg_img.copy()
    d = ImageDraw.Draw(c)
    for (x, y, s, b, ph, sp) in stars:
        v = b * (0.55 + 0.45 * math.sin(ph + t * sp))
        col = (int(200 * v + 40), int(205 * v + 40), int(255 * v))
        if s == 1: d.point((x, y), fill=col)
        else: d.ellipse([x - s / 2, y - s / 2, x + s / 2, y + s / 2], fill=col)
    # header: signature + line + pill (scenes 1-6)
    ha = 1 - ease((t - S[6] + 0.1) / 0.3) if t > S[6] - 0.1 else 1
    if ha > 0:
        place(c, sig(360), 540, 70, ha)
        ln = Image.new("RGBA", (760, 2), (90, 220, 210, int(110 * ha))); c.alpha_composite(ln, (160, 205))
        place(c, pill, 540, 228, ha)

    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    # ---- S1 hook (visible from frame 0) ----
    if t < S[1]:
        a, dy = env(t, -1, S[1]); p = ease(t / 0.45)
        place(L, text_layer("Debout depuis 17 h ?", fSB(66)), 540, 560, a, dy)
        place(L, text_layer("Ton cerveau roule\nà 0,5 g/L.", fBlack(108), grad=G_CV, glow=14), 540, 650, a, dy, 1.06 - 0.06 * p)
        place(L, text_layer("(sans une goutte d'alcool)", fReg(38), GREY), 540, 1000, a * ease((t - 0.5) / 0.4), dy)
    # ---- S2 study + counters ----
    elif t < S[2]:
        t0, t1 = S[1], S[2]; a, dy = env(t, t0, t1)
        card = _cache.get("card2")
        if card is None:
            card = rrect((760, 150), 26, (40, 40, 80, 170), (130, 130, 220, 120))
            l1 = text_layer("ÉTUDE EN LABORATOIRE", fMed(22), TEAL, track=3)
            l2 = text_layer("39 adultes  ·  jusqu'à 28 h sans dormir", fSB(38))
            card.alpha_composite(l1, (int(380 - l1.width / 2), 12)); card.alpha_composite(l2, (int(380 - l2.width / 2), 52))
            _cache["card2"] = card
        place(L, card, 540, 340, a, dy)
        k = ease((t - t0 - 0.35) / 2.6); hrs = int(round(17 * k))
        place(L, text_layer("HEURES ÉVEILLÉ", fMed(26), GREY, track=5), 540, 560, a, dy)
        place(L, text_layer(f"{hrs} h", fBlack(210), grad=G_GOLD, glow=10), 540, 590, a, dy)
        # 24 dots
        for i in range(24):
            on = i < hrs; x = 540 - 23 * 17 + i * 34; y = 880 + dy
            col = (CYAN if on else (70, 70, 110)) + (int(255 * a),)
            d.ellipse([x - 8, y - 8, x + 8, y + 8], fill=col if on else None, outline=col, width=2)
        # alcohol gauge
        ga = a * ease((t - t0 - 0.5) / 0.4)
        place(L, text_layer("ALCOOLÉMIE ÉQUIVALENTE*", fMed(26), GREY, track=5), 540, 980, ga, dy)
        bx, by, bw, bh = 160, 1050 + dy, 760, 34
        if ga > 0:
            d.rounded_rectangle([bx, by, bx + bw, by + bh], 17, outline=(130, 130, 220, int(200 * ga)), width=2)
            fw = int(bw / 2 * k)
            if fw > 20:
                gimg = grad_fill((fw, bh - 8), CYAN, ORANGE if k > 0.98 else VIOLET).convert("RGBA")
                m = Image.new("L", gimg.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, fw - 1, bh - 9], 13, fill=int(255 * ga))
                gimg.putalpha(m); L.alpha_composite(gimg, (int(bx + 4), int(by + 4)))
            val = f"{0.5 * k:.1f}".replace(".", ",") + " g/L"
            place(L, text_layer(val, fXB(64), grad=G_CV, glow=8), 540, 1110, ga, dy)
        place(L, text_layer("*sur certains tests de réaction", fReg(26), GREY), 540, 1205, ga, dy)
    # ---- S3 reflexes ----
    elif t < S[3]:
        t0, t1 = S[2], S[3]; a, dy = env(t, t0, t1)
        place(L, text_layer("Après 17 à 19 h sans dormir :", fSB(50)), 540, 340, a, dy)
        b = env(t, t0 + 0.25, t1)
        place(L, text_layer("TES RÉFLEXES", fBlack(118), grad=G_CV, glow=14), 540, 440, b[0], b[1])
        place(L, text_layer("jusqu'à 50 % plus lents", fXB(76), grad=G_WARN, glow=10), 540, 600, b[0], b[1])
        ca = a * ease((t - t0 - 0.7) / 0.3)
        if ca > 0:
            place(L, text_layer("Temps de réaction", fMed(28), GREY, track=2), 540, 790, ca, dy)
            for j, (lab, col, full) in enumerate([("Reposé", CYAN, 420), ("17 h éveillé", ORANGE, 630)]):
                y = 870 + j * 110 + dy
                lab_l = text_layer(lab, fSB(34)); L.alpha_composite(lab_l, (130, int(y - 18))) if ca > .5 else None
                g2 = ease((t - t0 - 0.8 - j * 0.35) / 0.8)
                bw = int(full * g2)
                if bw > 8:
                    d.rounded_rectangle([130, y + 40, 130 + bw, y + 70], 15, fill=col + (int(255 * ca),))
        place(L, text_layer("Résultats de laboratoire, sur certains tests.", fReg(28), GREY), 540, 1130, ca, dy)
    # ---- S4 legal limit ----
    elif t < S[4]:
        t0, t1 = S[3], S[4]; a, dy = env(t, t0, t1)
        place(L, text_layer("Et 0,5 g/L, c'est…", fSB(62)), 540, 540, a, dy)
        b = env(t, t0 + 0.45, t1)
        place(L, text_layer("la limite légale\nau volant en France.", fBlack(96), grad=G_GOLD, glow=14), 540, 650, b[0], b[1], 1.05 - 0.05 * ease((t - t0 - 0.45) / 0.4))
        place(L, text_layer("(0,2 g/L en permis probatoire)", fReg(34), GREY), 540, 970, b[0] * ease((t - t0 - 1.0) / 0.4), b[1])
    # ---- S5 the trap ----
    elif t < S[5]:
        t0, t1 = S[4], S[5]; a, dy = env(t, t0, t1)
        place(L, text_layer("Le piège ?", fBlack(100), grad=G_CV, glow=12), 540, 340, a, dy)
        place(L, text_layer("Réveil à 7 h…", fSB(58)), 540, 530, a, dy)
        k = ease((t - t0 - 0.5) / 1.6)
        x0, x1, y = 160, 920, 700 + dy
        if a > 0:
            d.line([(x0, y), (x1, y)], fill=(90, 90, 140, int(255 * a)), width=6)
            d.line([(x0, y), (x0 + (x1 - x0) * k, y)], fill=CYAN + (int(255 * a),), width=6)
            for x in (x0, x1): d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=(150, 150, 210, int(255 * a)))
            px = x0 + (x1 - x0) * k
            gl = Image.new("RGBA", (80, 80), (0, 0, 0, 0)); ImageDraw.Draw(gl).ellipse([20, 20, 60, 60], fill=CYAN + (220,))
            gl = gl.filter(ImageFilter.GaussianBlur(8)); L.alpha_composite(gl, (int(px - 40), int(y - 40)))
            d.ellipse([px - 13, y - 13, px + 13, y + 13], fill=WHITE + (int(255 * a),))
            place(L, text_layer("7 h", fSB(38), GREY), x0, y + 30 - dy, a, dy)
            place(L, text_layer("minuit", fSB(38), GREY), x1, y + 30 - dy, a, dy)
            hr = (7 + int(17 * k)) % 24
            place(L, text_layer(f"{hr:02d}:00", fXB(54), WHITE), px, y - 105 - dy, a, dy)
        b = a * ease((t - t0 - 2.1) / 0.35)
        place(L, text_layer("17 h éveillé", fXB(60), grad=G_WARN, glow=8), 540, 830, b, dy)
        place(L, text_layer("À minuit, tu y es déjà.", fBlack(78), grad=G_CV, glow=12), 540, 930, b, dy)
    # ---- S6 3 reflexes ----
    elif t < S[6]:
        t0, t1 = S[5], S[6]; a, dy = env(t, t0, t1)
        place(L, text_layer("3 réflexes simples", fBlack(88), grad=G_CV, glow=12), 540, 330, a, dy)
        items = [("Somnolent ?", "Pas de volant."), ("Route de nuit :", "une pause toutes les 2 h."), ("Coup de barre :", "sieste de 15 à 20 min.")]
        for j, (l1, l2) in enumerate(items):
            e = env(t, t0 + 0.3 + j * 0.45, t1)
            key = ("item", j)
            if key not in _cache:
                card = rrect((860, 150), 28, (35, 35, 75, 190), (120, 120, 210, 140))
                cd = ImageDraw.Draw(card); cd.ellipse([30, 43, 94, 107], outline=CYAN + (255,), width=3)
                n = text_layer(str(j + 1), fXB(36)); card.alpha_composite(n, (int(62 - n.width / 2), 75 - n.height // 2 - 2))
                a1 = text_layer(l1, fSB(40)); a2 = text_layer(l2, fSB(40), TEAL)
                card.alpha_composite(a1, (110, 14)); card.alpha_composite(a2, (110, 66))
                _cache[key] = card
            place(L, _cache[key], 540, 480 + j * 180, e[0], e[1])
        place(L, text_layer("Le café ne remplace pas le sommeil.", fReg(32), GREY), 540, 1030, a * ease((t - t0 - 1.8) / 0.4), dy)
    # ---- S7 CTA ----
    else:
        t0 = S[6]; a, dy = env(t, t0, DUR + 1, fin=0.35)
        place(L, text_layer("Envoie ça à quelqu'un", fSB(66)), 540, 430, a, dy)
        place(L, text_layer("qui rentre tard\nen voiture.", fBlack(92), grad=G_CV, glow=12), 540, 520, a, dy)
        place(L, text_layer("Enregistre  ·  Abonne-toi pour la suite", fReg(34), GREY), 540, 830, a, dy)
        b = env(t, t0 + 0.4, DUR + 1)
        place(L, sig(820), 540, 910, b[0], b[1])
        place(L, text_layer("@lifestyles_hf", fSB(46), GOLD1), 540, 1200, b[0], b[1])
        place(L, text_layer("Source : Williamson & Feyer, Occup. Environ. Med., 2000", fReg(24), GREY), 540, 1300, b[0] * 0.9, b[1])
    c.alpha_composite(L, (0, 110))
    return c.convert("RGB")

if PREVIEW:
    times = [0.0, 2.0, 6.5, 10.0, 13.0, 17.0, 20.5, 24.0]
    ims = [frame(x).resize((270, 480)) for x in times]
    sheet = Image.new("RGB", (270 * 4, 480 * 2))
    for i, im in enumerate(ims): sheet.paste(im, ((i % 4) * 270, (i // 4) * 480))
    sheet.save(OUT); frame(0.0).save(OUT.replace(".jpg", "_f0.jpg"), quality=92)
    sys.exit()

p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                      "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", OUT], stdin=subprocess.PIPE)
for i in range(N):
    p.stdin.write(frame(i / FPS).tobytes())
    if i % 150 == 0: print("frame", i, flush=True)
p.stdin.close(); p.wait()
print("done")
