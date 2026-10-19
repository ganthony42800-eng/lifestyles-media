import sys
from story import *

TOTAL = 35.0
SMALL = (270, 480)
yy, xx = np.mgrid[0:SMALL[1], 0:SMALL[0]].astype(np.float32)
VIG = vignette(SMALL[1], SMALL[0])
GROUND = 1440
rng = np.random.default_rng(7)

# gouttes : 3 profondeurs
DROPS = []
for depth, n in ((0, 90), (1, 60), (2, 28)):
    DROPS.append(dict(x=rng.uniform(0, W, n), y0=rng.uniform(0, H, n),
                      v=rng.uniform(1500, 2100, n) * (0.55 + .3 * depth), depth=depth))
SPL = dict(x=rng.uniform(60, W - 60, 40), ph=rng.uniform(0, 1, 40), per=rng.uniform(.9, 1.6, 40))
AER = dict(x=rng.uniform(40, W - 40, 120), ph=rng.uniform(0, 1, 120), per=rng.uniform(3, 6, 120),
           dr=rng.uniform(-20, 20, 120), s=rng.uniform(2, 5, 120))

def sky(t):
    x, y = xx / 60, yy / 60
    n = (np.sin(x * 1.3 + t * .15) * np.sin(y * .9 - t * .1) + .5 * np.sin(x * 2.7 - y * 1.9 + t * .2))
    cloud = np.clip(.5 + .5 * n, 0, 1) * np.clip(1 - yy / 320, 0, 1)
    g = (yy / SMALL[1])[..., None]
    base = np.array([4, 10, 10], np.float32) * (1 - g) + np.array([8, 30, 24], np.float32) * g
    col = base + cloud[..., None] * np.array([18, 34, 30], np.float32)
    gy = GROUND / H * SMALL[1]
    soil = (yy > gy)[..., None]
    soilcol = np.array([14, 16, 12], np.float32) + np.sin(xx * .9 + yy * 1.7)[..., None] * 3
    col = np.where(soil, soilcol, col)
    glow = np.exp(-((yy - gy) / 6) ** 2)[..., None] * np.array([20, 90, 64], np.float32)
    col = (col + glow) * VIG
    return Image.fromarray(np.clip(col, 0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)

def rain(fr, t, k):
    far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); near = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    df, dn = ImageDraw.Draw(far), ImageDraw.Draw(near)
    for L in DROPS:
        d = df if L["depth"] < 2 else dn
        ln = 26 + 30 * L["depth"]
        y = (L["y0"] + L["v"] * t) % (GROUND + 80) - 80
        a = int((60 + 70 * L["depth"]) * k)
        col = (180, 230, 210, a) if L["depth"] < 2 else (230, 214, 170, a)
        for x, yy_ in zip(L["x"], y):
            x2 = x - .18 * ln
            d.line((x, yy_, x2, yy_ + ln), fill=col, width=1 + L["depth"])
    # impacts + bulles
    for x, ph, per in zip(SPL["x"], SPL["ph"], SPL["per"]):
        p = ((t / per) + ph) % 1
        r = 8 + 70 * p
        a = int(200 * (1 - p) * k)
        dn.ellipse((x - r, GROUND - r * .22, x + r, GROUND + r * .22), outline=(120, 240, 190, a), width=2)
        if p < .5:  # gouttelettes éjectées
            for j in range(4):
                bx = x + (j - 1.5) * 14 * (1 + p * 3)
                by = GROUND - 140 * p * (1 - p) * (1.4 + j % 2)
                dn.ellipse((bx - 3, by - 3, bx + 3, by + 3), fill=(220, 255, 235, a))
    for x, ph, per, dr, s in zip(AER["x"], AER["ph"], AER["per"], AER["dr"], AER["s"]):
        p = ((t / per) + ph) % 1
        yb = GROUND - 30 - 520 * p
        xb = x + dr * math.sin(p * 6 + ph * 9)
        a = int(170 * math.sin(math.pi * p) * k)
        dn.ellipse((xb - s, yb - s, xb + s, yb + s), fill=GOLD_HI + (a,))
    far = far.filter(ImageFilter.GaussianBlur(2.2))
    fr.alpha_composite(far)
    g = near.filter(ImageFilter.GaussianBlur(7))
    fr.alpha_composite(g)
    fr.alpha_composite(near)

SC = [
 (0.0, 4.8, [
   ("chip", 0, "NATURE · ODORAT"),
   ("h", .15, "L'odeur après la pluie ?", 96, 290),
   ("h", 1.6, "Ton nez la détecte à *dose infime.*", 96, 520),
 ]),
 (4.8, 11.0, [
   ("chip", 0, "L'ÉQUIVALENT DE"),
   ("big", .1, "1 grain de riz", 118, 290, GOLD_HI),
   ("h", .9, "dissous dans une _piscine olympique._", 80, 450),
   ("card", 1.9, (M, 700, W - M, 900)),
   ("p", 2.1, "Seuil de détection de la *géosmine* : 5 à 15 milliardièmes de gramme par litre d'eau, selon les personnes.", 36, 728, WHITE),
 ]),
 (11.0, 16.6, [
   ("chip", 0, "SON NOM"),
   ("big", .1, "pétrichor", 150, 300, GOLD_HI),
   ("p", 1.0, "Nommé en *1964* par deux chercheurs australiens, Isabel Bear et Richard Thomas, dans la revue _Nature_.", 42, 500, WHITE),
 ]),
 (16.6, 23.4, [
   ("chip", 0, "D'OÙ ELLE VIENT"),
   ("card", .1, (M, 280, W - M, 880)),
   ("step", .3, 1, "Des bactéries du sol (*Streptomyces*) fabriquent la *géosmine*", 320),
   ("step", 1.4, 2, "Chaque goutte piège de minuscules *bulles d'air*", 500),
   ("step", 2.5, 3, "Elles éclatent et projettent des particules qui portent l'odeur", 670),
   ("src", 3.0, "MIT, 2015 · ~600 expériences filmées en haute vitesse", 820),
 ]),
 (23.4, 29.6, [
   ("chip", 0, "LE DÉTAIL QUI SURPREND"),
   ("h", .1, "Une *petite pluie* sur sol sec sent plus fort qu'une averse.", 80, 290),
   ("card", 1.4, (M, 620, W - M, 780), EMER),
   ("p", 1.6, "Pluie légère à modérée = _plus de particules_ libérées. Pluie forte = beaucoup moins.", 38, 648, WHITE),
 ]),
 (29.6, 35.0, [
   ("h", 0, "Envoie ça à quelqu'un qui *adore* l'odeur de la pluie.", 80, 300),
   ("line", .8, 600, 260),
   ("p", 1.0, "Et toi, team pétrichor ou pas ? *Dis-le en commentaire.*", 46, 650, WHITE),
 ]),
]

def frame(t):
    fr = sky(t).convert("RGBA")
    k = .55 if 4.8 < t < 29.6 else 1.0
    rain(fr, t, k)
    for s, e, items in SC:
        run_scene(fr, t, s, e, items)
    progress(fr, t, TOTAL)
    signature(fr, ease(t / .6))
    return fr

if __name__ == "__main__":
    if sys.argv[1] == "still":
        for tt in map(float, sys.argv[2:]):
            frame(tt).convert("RGB").save(f"/home/claude/reels/out/petri_{tt:.1f}.jpg", quality=90)
    else:
        cuts = [s for s, _, _ in SC[1:]]
        ambient("/home/claude/reels/out/petri.wav", TOTAL, cuts, base=98, seed=5)
        render("/home/claude/reels/out/petrichor.mp4", TOTAL, frame, "/home/claude/reels/out/petri.wav")
