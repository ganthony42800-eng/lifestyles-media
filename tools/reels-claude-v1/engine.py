"""Moteur de rendu Reels Lifestyles (1080x1920, 30 fps) — PIL + numpy + ffmpeg."""
import math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
F = "/usr/share/fonts/opentype/inter/"
GOLD = (226, 190, 120)
GOLD_HI = (255, 226, 160)
EMER = (40, 214, 150)
EMER_DEEP = (8, 70, 52)
WHITE = (246, 244, 238)
MUTED = (196, 200, 194)

_fc = {}
def font(name, size):
    k = (name, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(F + name, size)
    return _fc[k]

def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))

def ease(x):
    x = clamp(x)
    return 1 - (1 - x) ** 3

def ease_io(x):
    x = clamp(x)
    return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2

# ---------- texte riche : *or*  _émeraude_ ----------
def _words(text):
    """Renvoie une liste de mots ; chaque mot = liste de segments (texte, mode)."""
    text = (text.replace(" ?", " ?").replace(" !", " !").replace(" :", " :")
                .replace("« ", "« ").replace(" »", " »").replace(" %", " %"))
    words, cur, seg, mode = [], [], "", None
    for c in text:
        if c in "*_":
            if seg:
                cur.append((seg, mode)); seg = ""
            m = "gold" if c == "*" else "emer"
            mode = None if mode == m else m
        elif c == " ":
            if seg:
                cur.append((seg, mode)); seg = ""
            if cur:
                words.append(cur); cur = []
        else:
            seg += c
    if seg:
        cur.append((seg, mode))
    if cur:
        words.append(cur)
    return words

_tc = {}
def text_block(text, fname, size, maxw, color=WHITE, align="left", lh=1.12, shadow=True):
    k = (text, fname, size, maxw, color, align, lh, shadow)
    if k in _tc:
        return _tc[k]
    f = font(fname, size)
    sp = f.getlength(" ")
    lines, line, lw = [], [], 0
    for segs in _words(text):
        ww = sum(f.getlength(s) for s, _ in segs)
        add = ww + (sp if line else 0)
        if line and lw + add > maxw:
            lines.append(line); line, lw = [], 0; add = ww
        line.append((segs, ww)); lw += add
    if line:
        lines.append(line)
    asc, desc = f.getmetrics()
    lhpx = int(size * lh)
    hgt = lhpx * len(lines) + desc + 10
    img = Image.new("RGBA", (int(maxw) + 40, hgt + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cols = {None: color, "gold": GOLD_HI, "emer": EMER}
    y = 10
    for ln in lines:
        tw = sum(x[1] for x in ln) + sp * (len(ln) - 1)
        x = 20 + (0 if align == "left" else (maxw - tw) / 2 if align == "center" else maxw - tw)
        for segs, ww in ln:
            for s, m in segs:
                d.text((x, y), s, font=f, fill=cols[m] + (255,))
                x += f.getlength(s)
            x += sp
        y += lhpx
    if shadow:
        sh = img.split()[3].filter(ImageFilter.GaussianBlur(8)).point(lambda v: int(v * .55))
        base = Image.new("RGBA", img.size, (0, 0, 0, 0))
        base.putalpha(sh)
        base.alpha_composite(img)
        img = base
    _tc[k] = img
    return img

def with_alpha(img, a):
    if a >= .999:
        return img
    im = img.copy()
    al = np.asarray(im.split()[3], dtype=np.float32) * clamp(a)
    im.putalpha(Image.fromarray(al.astype(np.uint8)))
    return im

def put(frame, img, x, y, a=1.0, dy=0):
    if a <= 0.01:
        return
    frame.alpha_composite(with_alpha(img, a), (int(x) - 20, int(y + dy) - 10))

def anim(t, start, dur=.55, rise=36):
    p = ease((t - start) / dur)
    return p, (1 - p) * rise

# ---------- éléments graphiques ----------
def rounded_mask(w, h, r):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=255)
    return m

_mc = {}
def glass(frame, box, a=1.0, tint=(10, 18, 16), border=GOLD, r=34, strength=.62):
    if a <= .01:
        return
    x0, y0, x1, y1 = [int(v) for v in box]
    w, h = x1 - x0, y1 - y0
    region = frame.crop((x0, y0, x1, y1)).convert("RGB").filter(ImageFilter.GaussianBlur(22))
    arr = np.asarray(region, dtype=np.float32)
    arr = arr * (1 - strength) + np.array(tint, dtype=np.float32) * strength
    # reflet diagonal
    gy = np.linspace(0, 1, h)[:, None]
    gx = np.linspace(0, 1, w)[None, :]
    sheen = np.clip(1 - np.abs((gx + gy * .6) - .35) * 3, 0, 1) ** 2 * 18
    arr += sheen[..., None]
    card = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
    key = (w, h, r)
    if key not in _mc:
        _mc[key] = rounded_mask(w, h, r)
    m = _mc[key]
    card.putalpha(m.point(lambda v: int(v * a)))
    # ombre portée
    sh = Image.new("RGBA", (w + 80, h + 80), (0, 0, 0, 0))
    sm = Image.new("L", (w + 80, h + 80), 0)
    ImageDraw.Draw(sm).rounded_rectangle((40, 52, w + 40, h + 52), r, fill=int(150 * a))
    sh.putalpha(sm.filter(ImageFilter.GaussianBlur(26)))
    frame.alpha_composite(sh, (x0 - 40, y0 - 40))
    frame.alpha_composite(card, (x0, y0))
    bd = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dd = ImageDraw.Draw(bd)
    dd.rounded_rectangle((0, 0, w - 1, h - 1), r, outline=border + (int(150 * a),), width=2)
    dd.line((r, 1, w * .55, 1), fill=GOLD_HI + (int(210 * a),), width=2)
    frame.alpha_composite(bd, (x0, y0))

def chip(frame, x, y, text, a=1.0, col=EMER):
    if a <= .01:
        return
    f = font("Inter-Bold.otf", 30)
    tw = f.getlength(text)
    w, h = int(tw + 56), 58
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), 29, fill=(6, 30, 24, 220), outline=col + (255,), width=2)
    d.ellipse((20, 24, 30, 34), fill=col + (255,))
    d.text((40, 12), text, font=f, fill=WHITE + (255,))
    frame.alpha_composite(with_alpha(im, a), (int(x), int(y)))
    return w

def progress(frame, t, total):
    d = ImageDraw.Draw(frame)
    d.rounded_rectangle((60, 120, W - 60, 128), 4, fill=(255, 255, 255, 50))
    x = 60 + (W - 120) * clamp(t / total)
    d.rounded_rectangle((60, 120, max(68, x), 128), 4, fill=GOLD + (255,))

def vignette(h=H, w=W):
    y = np.linspace(-1, 1, h)[:, None]
    x = np.linspace(-1, 1, w)[None, :]
    v = 1 - np.clip((x ** 2 * .55 + y ** 2 * .45) - .25, 0, 1) * .75
    return v[..., None].astype(np.float32)

# ---------- signature officielle ----------
SIG_PATH = os.environ.get("LS_SIGNATURE", "/home/claude/reels/assets/signature.png")
_sig = None
def signature(frame, a=1.0, cx=W // 2, cy=1555, width=540):
    global _sig
    if _sig is None:
        if os.path.exists(SIG_PATH):
            s = Image.open(SIG_PATH).convert("RGBA")
            bb = s.getbbox()
            if bb:
                s = s.crop(bb)
            s = s.resize((width, int(s.height * width / s.width)), Image.LANCZOS)
            pad = 70
            halo = Image.new("L", (s.width + 2 * pad, s.height + 2 * pad), 0)
            ImageDraw.Draw(halo).ellipse((pad // 2, pad // 2, s.width + pad * 1.5, s.height + pad * 1.5), fill=170)
            halo = halo.filter(ImageFilter.GaussianBlur(30))
            full = Image.new("RGBA", halo.size, (2, 8, 7, 0))
            full.putalpha(halo)
            full.alpha_composite(s, (pad, pad))
            _sig = full
        else:
            s = Image.new("RGBA", (width, 130), (0, 0, 0, 0))
            d = ImageDraw.Draw(s)
            d.rounded_rectangle((0, 0, width - 1, 129), 18, outline=GOLD + (200,), width=2)
            f = font("Inter-SemiBold.otf", 26)
            t = "SIGNATURE OFFICIELLE (à insérer)"
            d.text(((width - f.getlength(t)) / 2, 50), t, font=f, fill=GOLD + (230,))
            _sig = s
    frame.alpha_composite(with_alpha(_sig, a), (int(cx - _sig.width / 2), int(cy - _sig.height / 2)))

# ---------- encodage ----------
def render(path, total, draw_fn, audio=None):
    n = int(total * FPS)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"]
    if audio:
        cmd += ["-i", audio, "-c:a", "aac", "-b:a", "192k", "-shortest"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
            "-profile:v", "high", "-movflags", "+faststart", path]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        fr = draw_fn(i / FPS)
        p.stdin.write(fr.convert("RGB").tobytes())
        if i % 150 == 0:
            print(f"  {path}: {i}/{n}", flush=True)
    p.stdin.close()
    p.wait()

# ---------- audio : nappe ambiante + souffles aux transitions ----------
def ambient(path, total, cuts, base=110.0, seed=1):
    sr = 44100
    n = int(total * sr)
    t = np.arange(n) / sr
    rng = np.random.default_rng(seed)
    chord = [1, 1.5, 2, 2.4, 3, 4.5]  # quinte / neuvième, sonorité ouverte
    sig = np.zeros(n)
    for i, r in enumerate(chord):
        f = base * r
        lfo = .5 + .5 * np.sin(2 * np.pi * (0.05 + .02 * i) * t + i)
        sig += np.sin(2 * np.pi * f * t + .3 * np.sin(2 * np.pi * .2 * t)) * lfo / (1 + i * .6)
    # pulsation douce
    beat = 60 / 84
    env = np.exp(-((t % beat) / .09))
    sig += np.sin(2 * np.pi * 55 * t) * env * .9
    hat = rng.standard_normal(n) * np.exp(-(((t + beat / 2) % beat) / .012)) * .08
    sig += hat
    for c in cuts:
        i0 = int(max(0, c - .45) * sr)
        L = int(.9 * sr)
        nz = rng.standard_normal(L)
        nz = np.convolve(nz, np.ones(40) / 40, mode="same")
        e = np.sin(np.linspace(0, np.pi, L)) ** 2
        sig[i0:i0 + L] += (nz * e * 1.6)[:max(0, min(L, n - i0))]
    fade = np.clip(t / 1.2, 0, 1) * np.clip((total - t) / 1.5, 0, 1)
    sig = sig * fade
    sig = sig / np.max(np.abs(sig)) * .5
    st = np.stack([sig, np.roll(sig, 300)], 1)
    import wave
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((st * 32767).astype(np.int16).tobytes())
