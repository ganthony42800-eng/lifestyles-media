import sys
from story import *

TOTAL = 35.0
SMALL = (270, 480)
yy, xx = np.mgrid[0:SMALL[1], 0:SMALL[0]].astype(np.float32)
VIG = vignette(SMALL[1], SMALL[0])

def studio(t):
    cx, cy = 135 + 20 * math.sin(t * .3), 300
    d = np.hypot((xx - cx) / 160, (yy - cy) / 220)
    spot = np.clip(1 - d, 0, 1) ** 1.6
    g = (yy / SMALL[1])[..., None]
    base = np.array([3, 7, 7], np.float32) * (1 - g) + np.array([6, 16, 14], np.float32) * g
    col = base + spot[..., None] * np.array([16, 70, 52], np.float32)
    # grille fine en perspective (sol)
    floor = yy > 360
    gl = np.abs(np.sin(900 / (yy - 330 + 1e-3))) > .97
    col = np.where((floor & gl)[..., None], col + np.array([10, 60, 44], np.float32) * ((yy - 360) / 120)[..., None], col)
    col *= VIG
    return Image.fromarray(np.clip(col, 0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)

POSES = [  # décalage horizontal le long de la colonne (0 = bas, 1 = haut)
    lambda s: 0 * s,                                   # droit
    lambda s: 120 * np.sin(np.pi * s * .9) * s,        # avachi (C)
    lambda s: -55 * np.sin(2 * np.pi * s) + 30 * s,    # cambré
    lambda s: 60 * np.sin(np.pi * s) - 20 * s,         # penché
]
def spine(fr, t, alpha):
    n = 17
    seg = t / 2.6
    i0 = int(seg) % len(POSES); i1 = (i0 + 1) % len(POSES)
    m = ease_io(seg - int(seg))
    s = np.linspace(0, 1, n)
    off = POSES[i0](s) * (1 - m) + POSES[i1](s) * m
    base_x, y_bot, y_top = 540, 1440, 860
    rot = t * .9
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    pts = []
    for i in range(n):
        x = base_x + off[i]
        y = y_bot - (y_bot - y_top) * s[i]
        pts.append((x, y))
    # moelle / disques lumineux
    d.line(pts, fill=EMER + (int(120 * alpha),), width=10, joint="curve")
    for i, (x, y) in enumerate(pts):
        sz = 1.0 - .45 * s[i]
        w = 92 * sz * (.78 + .22 * abs(math.cos(rot + i * .12)))
        h = 22 * sz
        sp = math.sin(rot + i * .12) * 30 * sz
        d.ellipse((x - w, y - h, x + w, y + h), fill=(30, 26, 18, int(235 * alpha)),
                  outline=GOLD + (int(255 * alpha),), width=3)
        d.ellipse((x - w * .6, y - h * .55 - 4, x + w * .6, y + h * .2 - 4), fill=GOLD + (int(70 * alpha),))
        d.polygon([(x + sp - 8, y), (x + sp + 8, y), (x + sp * 1.6, y + h + 10)], fill=GOLD_HI + (int(150 * alpha),))
        if i < n - 1:
            d.ellipse((x - w * .7, y - h - 9, x + w * .7, y - h + 1), fill=EMER + (int(160 * alpha),))
    glow = lay.filter(ImageFilter.GaussianBlur(16))
    fr.alpha_composite(glow)
    fr.alpha_composite(lay)

SC = [
 (0.0, 4.8, [
   ("chip", 0, "CORPS · TRAVAIL SUR ÉCRAN"),
   ("h", .15, "Tu te tiens bien droit devant ton écran ?", 88, 290),
   ("h", 1.7, "Ton dos n'est *pas convaincu.*", 88, 570),
 ]),
 (4.8, 11.2, [
   ("chip", 0, "CE QUE DIT LA SCIENCE"),
   ("big", .1, "41", 220, 250, GOLD_HI),
   ("p", .6, "revues de la littérature passées au crible en 2020", 42, 490, WHITE),
   ("card", 1.6, (M, 640, W - M, 830), EMER),
   ("p", 1.8, "Verdict : *aucun consensus* pour dire qu'une posture _cause_ le mal de dos.", 40, 668, WHITE),
   ("src", 2.4, "Swain et al., Journal of Biomechanics, 2020", 846),
 ]),
 (11.2, 17.8, [
   ("chip", 0, "ET LE « TEXT NECK » ?"),
   ("big", .1, "582", 200, 250, GOLD_HI),
   ("p", .6, "adultes photographiés en train d'écrire sur leur smartphone", 42, 470, WHITE),
   ("card", 1.6, (M, 620, W - M, 740), EMER),
   ("p", 1.8, "L'angle du cou n'était *pas lié* aux douleurs.", 40, 648, WHITE),
   ("src", 2.4, "Correia et al., Spine, 2021", 758),
 ]),
 (17.8, 24.4, [
   ("chip", 0, "CE QUI AIDE"),
   ("h", .1, "La meilleure posture, c'est *la suivante.*", 86, 290),
   ("card", 1.2, (M, 530, W - M, 880)),
   ("step", 1.4, 1, "Change de position *souvent*", 560),
   ("step", 2.2, 2, "Lève-toi, marche, étire-toi", 660),
   ("step", 3.0, 3, "Reste *actif* dans la semaine", 760),
 ]),
 (24.4, 29.6, [
   ("chip", 0, "NUANCE", 190, GOLD),
   ("p", .1, "Ces études montrent des *associations*, pas des preuves de cause.", 48, 290, WHITE),
   ("card", 1.2, (M, 470, W - M, 690), GOLD),
   ("p", 1.4, "Douleur qui dure, descend dans la jambe ou te réveille la nuit : *consulte.*", 40, 500, WHITE),
 ]),
 (29.6, 35.0, [
   ("h", 0, "Envoie ça au collègue *raide comme un piquet.*", 84, 300),
   ("line", .8, 600, 260),
   ("p", 1.0, "Et toi, tu es dans quelle position *là, maintenant ?*", 46, 650, WHITE),
 ]),
]

def frame(t):
    fr = studio(t).convert("RGBA")
    a = 1.0 if t < 4.8 or t > 29.6 else .5
    spine(fr, t, a)
    for s, e, items in SC:
        run_scene(fr, t, s, e, items)
    progress(fr, t, TOTAL)
    signature(fr, ease(t / .6))
    return fr

if __name__ == "__main__":
    if sys.argv[1] == "still":
        for tt in map(float, sys.argv[2:]):
            frame(tt).convert("RGB").save(f"/home/claude/reels/out/post_{tt:.1f}.jpg", quality=90)
    else:
        cuts = [s for s, _, _ in SC[1:]]
        ambient("/home/claude/reels/out/post.wav", TOTAL, cuts, base=123, seed=9)
        render("/home/claude/reels/out/posture.mp4", TOTAL, frame, "/home/claude/reels/out/post.wav")
