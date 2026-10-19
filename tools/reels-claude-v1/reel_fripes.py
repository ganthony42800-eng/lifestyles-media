import sys
from story import *

TOTAL = 35.0
SMALL = (270, 480)
yy, xx = np.mgrid[0:SMALL[1], 0:SMALL[0]].astype(np.float32)
VIG = vignette(SMALL[1], SMALL[0])

def water(t):
    x, y = xx / 40, yy / 40
    v = (np.sin(x * 1.7 + t * .9) + np.sin(y * 1.3 - t * 1.1 + x * .4)
         + np.sin((x + y) * 1.1 + t * .6) + np.sin(np.hypot(x - 3.4, y - 7) * 2.2 - t * 1.6))
    c = np.clip(1 - np.abs(v) / 2.2, 0, 1) ** 6
    grad = (yy / SMALL[1])[..., None]
    base = np.array([2, 9, 11], np.float32) * (1 - grad) + np.array([4, 34, 32], np.float32) * grad
    col = base + c[..., None] * np.array([30, 150, 120], np.float32) * (.35 + .65 * grad)
    col = col * VIG
    return Image.fromarray(np.clip(col, 0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)

FP_BOX = (90, 760, 990, 1500)  # zone de l'empreinte
def fingerprint(fr, t, amp, alpha):
    w, h = FP_BOX[2] - FP_BOX[0], FP_BOX[3] - FP_BOX[1]
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    cx, cy = w / 2, h / 2 + 20
    th = np.linspace(0, 2 * np.pi, 260)
    for i in range(15):
        a = 34 + i * 22
        b = a * 1.32
        r = 1 + (amp * np.sin(th * (5 + i % 4) + i * .9 + t * 1.4) * (0.5 + i / 30)) / a
        px = cx + a * r * np.cos(th) + 8 * np.sin(i * .5 + t * .3)
        py = cy + b * r * np.sin(th)
        gap = int(18 + (i * 37) % 60)
        pts = list(zip(px[gap:], py[gap:]))
        k = 1 - i / 17
        col = GOLD if i % 3 else EMER
        d.line(pts, fill=col + (int(220 * k * alpha),), width=4 if i < 6 else 3, joint="curve")
    glow = lay.filter(ImageFilter.GaussianBlur(12))
    fr.alpha_composite(glow, FP_BOX[:2])
    fr.alpha_composite(glow, FP_BOX[:2])
    fr.alpha_composite(lay, FP_BOX[:2])

SC = [
 (0.0, 4.6, [
   ("chip", .0, "CORPS · SYSTÈME NERVEUX"),
   ("h", .15, "Tes doigts fripent dans l'eau ?", 92, 290),
   ("h", 1.5, "Ce n'est pas l'eau.", 92, 520),
   ("h", 2.6, "C'est ton *système nerveux.*", 92, 625),
 ]),
 (4.6, 10.6, [
   ("chip", 0, "LA PREUVE"),
   ("h", .1, "Un doigt dont le nerf est abîmé…", 80, 290),
   ("big", .9, "reste _lisse._", 120, 480, WHITE),
   ("card", 1.8, (M, 700, W - M, 850)),
   ("p", 2.0, "Observé dès les années 1930 chez des patients touchés au *nerf médian* (Lewis & Pickering).", 38, 735, WHITE),
 ]),
 (10.6, 17.4, [
   ("chip", 0, "LE MÉCANISME"),
   ("card", .1, (M, 280, W - M, 860)),
   ("step", .3, 1, "Quelques minutes dans l'eau chaude", 320),
   ("step", 1.3, 2, "Ton système nerveux *resserre les vaisseaux* du bout des doigts", 480),
   ("step", 2.5, 3, "La pulpe dégonfle légèrement : la peau *se plisse*", 680),
 ]),
 (17.4, 23.0, [
   ("chip", 0, "À L'HÔPITAL"),
   ("h", .1, "Les médecins s'en servent comme *test.*", 84, 290),
   ("card", 1.0, (M, 560, W - M, 860), EMER),
   ("p", 1.2, "Doigts dans l'eau à ~40 °C. Pas de rides ? On vérifie le nerf.", 42, 595, WHITE),
   ("src", 1.6, "Test des rides : O'Riain, 1973", 790),
 ]),
 (23.0, 29.6, [
   ("chip", 0, "MAIS À QUOI ÇA SERT ?"),
   ("h", .1, "Des « pneus pluie » pour tes doigts ?", 78, 290),
   ("card", .9, (M, 520, W - M, 640)),
   ("p", 1.0, "*2013* · objets mouillés saisis _12 % plus vite_", 40, 548, WHITE),
   ("card", 1.9, (M, 665, W - M, 785)),
   ("p", 2.0, "*2014* · 40 personnes : _aucun gain_ mesuré", 40, 693, WHITE),
   ("p", 3.2, "Mécanisme : *prouvé*. Utilité : *débattue*.", 46, 840, WHITE),
 ]),
 (29.6, 35.0, [
   ("h", 0, "Envoie ça à quelqu'un qui croit que la peau *« boit »* l'eau.", 78, 300),
   ("line", .8, 640, 260),
   ("p", 1.0, "Abonne-toi : la science de ton corps, *chaque jour.*", 46, 690, WHITE),
 ]),
]

def frame(t):
    fr = water(t * .8)
    z = 1 + .04 * t / TOTAL
    if z > 1.001:
        fr = fr.resize((int(W * z), int(H * z)), Image.BILINEAR).crop(
            (int((W * z - W) / 2), int((H * z - H) / 2), int((W * z - W) / 2) + W, int((H * z - H) / 2) + H))
    fr = fr.convert("RGBA")
    amp = 2 + 12 * ease_io(t / 14)
    vis = 1.0 if (t < 4.6 or 10.6 > t) else .45
    vis = .9 if t < 4.6 else (.55 if t < 29.6 else .8)
    fingerprint(fr, t, amp, vis)
    for s, e, items in SC:
        run_scene(fr, t, s, e, items)
    progress(fr, t, TOTAL)
    signature(fr, ease(t / .6))
    return fr

if __name__ == "__main__":
    if sys.argv[1] == "still":
        for tt in map(float, sys.argv[2:]):
            frame(tt).convert("RGB").save(f"/home/claude/reels/out/fripes_{tt:.1f}.jpg", quality=90)
    else:
        cuts = [s for s, _, _ in SC[1:]]
        ambient("/home/claude/reels/out/fripes.wav", TOTAL, cuts, base=110, seed=3)
        render("/home/claude/reels/out/fripes.mp4", TOTAL, frame, "/home/claude/reels/out/fripes.wav")
