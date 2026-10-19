"""Petit langage de scènes : chaque scène = (début, fin, éléments)."""
from engine import *

M = 70           # marge gauche
TW = W - 2 * M - 40  # largeur texte

def run_scene(fr, t, s, e, items):
    if t < s - .01 or t > e + .01:
        return
    out = 1 - ease((t - (e - .32)) / .32) if t > e - .32 else 1
    lift = (1 - out) * -40
    lt = t - s
    for it in items:
        kind, st = it[0], it[1]
        p, dy = anim(lt, st)
        a = p * out
        if a <= .01:
            continue
        dy += lift
        if kind == "chip":
            chip(fr, M, it[3] + dy if len(it) > 3 else 190 + dy, it[2], a,
                 col=it[4] if len(it) > 4 else EMER)
        elif kind == "h":       # titre : texte, taille, y, [align]
            _, _, txt, size, y, *rest = it
            align = rest[0] if rest else "left"
            img = text_block(txt, "InterDisplay-ExtraBold.otf", size, TW, align=align, lh=1.06)
            put(fr, img, M, y, a, dy)
        elif kind == "p":       # paragraphe : texte, taille, y, [couleur], [align]
            _, _, txt, size, y, *rest = it
            col = rest[0] if rest else MUTED
            align = rest[1] if len(rest) > 1 else "left"
            img = text_block(txt, "Inter-Medium.otf", size, TW, color=col, align=align, lh=1.3)
            put(fr, img, M, y, a, dy)
        elif kind == "src":     # source en petit
            _, _, txt, y = it
            img = text_block(txt, "Inter-Medium.otf", 27, TW, color=(150, 160, 152), lh=1.3, shadow=False)
            put(fr, img, M, y, a, dy)
        elif kind == "card":    # boîte verre : (x0,y0,x1,y1), [bordure]
            _, _, box, *rest = it
            b = (box[0] - 34, box[1] + dy, box[2] + 34, box[3] + dy)
            glass(fr, b, a, border=rest[0] if rest else GOLD)
        elif kind == "big":     # chiffre géant : texte, taille, y, couleur, [align]
            _, _, txt, size, y, col, *rest = it
            align = rest[0] if rest else "left"
            sc = .85 + .15 * p
            img = text_block(txt, "InterDisplay-Black.otf", size, TW, color=col, align=align, lh=1.0)
            if sc < .999:
                img = img.resize((int(img.width * sc), int(img.height * sc)), Image.LANCZOS)
                off = (TW + 40) * (1 - sc) / 2 if align == "center" else 0
                put(fr, img, M + off, y + (1 - sc) * size / 2, a, dy)
            else:
                put(fr, img, M, y, a, dy)
        elif kind == "step":    # étape numérotée : n, texte, y
            _, _, n, txt, y = it
            d = ImageDraw.Draw(fr)
            cx, cy = M + 34, y + dy + 30
            ov = Image.new("RGBA", (72, 72), (0, 0, 0, 0))
            od = ImageDraw.Draw(ov)
            od.ellipse((2, 2, 69, 69), fill=(6, 40, 30, 230), outline=GOLD + (255,), width=3)
            f = font("InterDisplay-Bold.otf", 34)
            od.text((36 - f.getlength(str(n)) / 2, 14), str(n), font=f, fill=GOLD_HI + (255,))
            fr.alpha_composite(with_alpha(ov, a), (int(cx - 36), int(cy - 36)))
            img = text_block(txt, "Inter-SemiBold.otf", 40, TW - 110, color=WHITE, lh=1.25)
            put(fr, img, M + 100, y + 4, a, dy)
        elif kind == "line":    # filet or : y, largeur
            _, _, y, wd = it
            d = ImageDraw.Draw(fr)
            d.rounded_rectangle((M, y + dy, M + wd * p, y + dy + 4), 2, fill=GOLD + (int(255 * a),))
