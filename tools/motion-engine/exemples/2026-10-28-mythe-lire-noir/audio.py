#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 6 : lire dans le noir abîme les yeux ? ». Synthèse procédurale, graine fixe.
Usage : python3 audio.py sortie.wav [rms_cible_dBFS]
Durée 25,25 s (le flux vidéo de 25,0 s fixe la fin). Temps calés sur index.html :
 sous la couette (rumeur étouffée, souffle lent de période 25/6 s comme la couette) + nappe La majeur 9 chaude
 · 1,0 page tournée · 1,5 note basse « Pas vraiment » · 2,5-3,0 la lampe se tourne vers toi (souffle qui monte) · 3,0 éblouissement
 · 3,62 / 4,18 / 5,3 clignements (petits « tic » mouillés) · 4,35-4,8 roulement du compteur · 5,55-5,8 retour du faisceau
 · 6,35-8,15 la lampe grésille et vacille · SILENCE 8,25-8,45 · 8,45 la couette s'arrache (whoosh) + accord du jour + oiseaux
 · 10,6-11,2 montée vers la fenêtre · 11,55-12,85 : 395 tics à gauche · 13,95-14,95 : 304 tics à droite · cour d'école lointaine
 · 16,3-17,4 envol vers le globe · 17,55-18,5 : scintillement de 2 000 points · 19,2 tampon du verdict
 · 21,85 signature · 22,4 bouton · 23,4-24,3 la couette retombe · 23,95 clic de la lampe · retour de l'ambiance du début (boucle)."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 25.25; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2810)
L = np.zeros(N); Rt = np.zeros(N)


def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def sm(x): x = np.clip(x, 0, 1); return x * x * (3 - 2 * x)
def win(a, b, fa=0.2, fb=0.2): return sm((T - a) / fa) * sm((b - T) / fb)
def ax(d): return np.arange(int(d * SR)) / SR


def put(sig, t0, g=1.0, pan=0.0):
    i = int(round(t0 * SR))
    if i >= N or i + len(sig) <= 0: return
    s = sig * g
    if i < 0: s = s[-i:]; i = 0
    s = s[:N - i]
    L[i:i + len(s)] += s * (1 - max(pan, 0)); Rt[i:i + len(s)] += s * (1 + min(pan, 0))


def tone(f, d, dec, ph=0.0):
    x = ax(d); return np.sin(2 * np.pi * f * x + ph) * np.exp(-x * dec)


def tick(t0, f=2400, g=0.05, pan=0.0, dec=90):
    x = ax(0.06); put(np.sin(2 * np.pi * f * x) * np.exp(-x * dec) * np.clip(x / 0.0015, 0, 1), t0, g, pan)


def whoosh(t0, d, lo, hi, g, up=True, pan=0.0):
    x = ax(d); n = R.standard_normal(len(x)); env = (x / d) ** 2 if up else np.exp(-x / d * 4) * np.clip(x / 0.02, 0, 1)
    put(bp(n, lo, hi) * env, t0, g, pan)


night = win(-1, 8.25, 0.1, 0.02) + win(23.6, 26, 0.6, 0.1)
day = win(8.45, 23.6, 0.25, 0.5)
# 1. Sous la couette : rumeur étouffée + souffle lent (période 25/6 s)
room = lp(R.standard_normal(N), 220) * 0.07
breath = bp(R.standard_normal(N), 250, 1400) * 0.022 * (0.5 + 0.5 * np.sin(2 * np.pi * T / (25 / 6))) ** 2
L += (room + breath) * night; Rt += (np.roll(room, 431) + np.roll(breath, 211)) * night
# 2. Nappe La majeur 9 chaude (nuit) → accord clair Mi majeur add9 aigu (jour)
pad = np.zeros(N)
for f, g in ((55.0, .5), (110.0, .35), (164.81, .25), (220.0, .22), (277.18, .2), (415.3, .08), (493.88, .06)):
    pad += g * np.sin(2 * np.pi * f * T + R.random() * 6) * (0.8 + 0.2 * np.sin(2 * np.pi * T * (0.12 + f / 5000)))
pad = lp(pad, 1200) * 0.055
dpad = np.zeros(N)
for f, g in ((329.63, .3), (493.88, .25), (659.25, .22), (739.99, .16), (987.77, .1), (1318.5, .05)):
    dpad += g * np.sin(2 * np.pi * f * T + R.random() * 6) * (0.75 + 0.25 * np.sin(2 * np.pi * T * (0.2 + f / 6000)))
dpad = lp(dpad, 4000) * 0.03
glob = win(16.3, 19.2, 0.3, 0.05)
L += pad * (night + 0.35 * day * (1 - glob) + 0.9 * glob) + dpad * day * (1 - 0.7 * glob)
Rt += np.roll(pad, 300) * (night + 0.35 * day * (1 - glob) + 0.9 * glob) + np.roll(dpad, 520) * day * (1 - 0.7 * glob)
# 3. Page tournée (1,0) + note basse (1,5)
x = ax(0.45); put(hp(R.standard_normal(len(x)), 1500) * np.sin(np.pi * x / 0.45) ** 2, 0.95, 0.05, -0.2)
put(tone(55, 1.2, 3) + 0.4 * tone(110, 1.2, 4), 1.5, 0.22)
# 4. La lampe se tourne vers toi (2,5-3,0), éblouissement (3,0), retour (5,55-5,8)
whoosh(2.45, 0.55, 400, 5000, 0.16)
for kk in range(9): put(tone(1760 * 2 ** (kk * 2 / 12), 0.8, 5), 3.0 + kk * 0.03, 0.022, (kk / 4.5) - 1)
put(np.sin(2 * np.pi * 48 * ax(0.8)) * np.exp(-ax(0.8) * 5), 3.0, 0.25)
whoosh(5.5, 0.3, 400, 5000, 0.14); whoosh(5.8, 0.4, 300, 3000, 0.1, up=False)
# 5. Clignements : tic mouillé + sous-grave
for tb in (3.62, 4.18, 5.3):
    tick(tb - 0.02, 900, 0.10, 0.0, 120); tick(tb + 0.03, 650, 0.06, 0.0, 140)
    put(tone(70, 0.25, 18), tb, 0.12)
# 6. Roulement du compteur (4,35-4,8) : tics qui ralentissent
for k in range(14):
    tick(4.35 + 0.45 * (k / 14) ** 1.6, 2600 - 60 * k, 0.035, 0.1)
put(tone(880, 0.6, 7) + 0.5 * tone(1318.5, 0.6, 9), 4.8, 0.05)
# 7. Grésillement de la lampe (6,35-8,15)
for c, w in ((6.35, .05), (6.48, .07), (7.05, .06), (7.6, .08), (7.72, .05), (7.9, .06), (8.05, .05), (8.15, .04)):
    x = ax(w * 3); buzz = np.sign(np.sin(2 * np.pi * 100 * x)) * 0.5 + hp(R.standard_normal(len(x)), 3000)
    put(lp(buzz, 5000) * np.exp(-((x - w * 1.5) / w) ** 2), c - w * 1.5, 0.05, 0.3)
x = ax(1.9); put(lp(np.sign(np.sin(2 * np.pi * 50 * x)), 900) * 0.3 * (x / 1.9), 6.3, 0.03)
# 8. La couette s'arrache (8,45) + oiseaux du jour
x = ax(1.2); put(bp(R.standard_normal(len(x)), 200, 6000) * np.exp(-x * 2.5) * np.clip(x / 0.03, 0, 1), 8.45, 0.35)
x = ax(1.2); put(np.sin(2 * np.pi * (40 + 30 * np.exp(-x * 8)) * x) * np.exp(-x * 4), 8.45, 0.3)
for kk in range(12): put(tone(1318.5 * 2 ** (kk * 2 / 12 * 0.5), 1.2, 3), 8.48 + kk * 0.04, 0.016, (kk / 6) - 1)


def bird(t0, pan):
    for j in range(int(2 + R.integers(0, 4))):
        x = ax(0.07 + 0.05 * R.random()); f0 = 2600 + 1800 * R.random(); fr = f0 * (1 + 0.35 * np.sin(np.pi * x / x[-1]))
        put(np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.sin(np.pi * x / x[-1]) ** 2, t0 + j * 0.11, 0.025, pan)


for tb in list(8.9 + np.cumsum(R.uniform(0.4, 1.0, 4))) + list(19.4 + np.cumsum(R.uniform(0.5, 1.1, 5))):
    if tb < 11.0 or 19.2 < tb < 23.3: bird(tb, R.uniform(-0.8, 0.8))
whoosh(10.6, 0.62, 300, 7000, 0.18)
# 9. Cour d'école lointaine (11,2-16,3) + 395 tics à gauche, 304 à droite
yard = bp(R.standard_normal(N), 500, 2500) * (0.6 + 0.4 * np.abs(np.sin(2 * np.pi * T * 1.3))) * 0.012 * win(11.2, 16.4, 0.4, 0.3)
L += yard; Rt += np.roll(yard, 777)
for k in range(395): tick(11.55 + 1.3 * (k / 395) ** 0.75, 2000 + 900 * R.random(), 0.016, -0.55 + 0.3 * R.random())
for k in range(304): tick(13.95 + 1.0 * (k / 304) ** 0.75, 2000 + 900 * R.random(), 0.016, 0.55 - 0.3 * R.random())
for tl, pn in ((12.95, -0.4), (15.0, 0.4)): put(tone(1046.5, 0.5, 6) + 0.5 * tone(1568, 0.5, 8), tl, 0.05, pn)
# 10. Envol vers le globe (16,3-17,4) + 2 000 scintillements (17,55-18,5)
whoosh(16.25, 1.1, 300, 6000, 0.16)
x = ax(1.4); put(np.sin(2 * np.pi * np.cumsum(60 + 80 * (x / 1.4)) / SR) * np.sin(np.pi * x / 1.4), 16.3, 0.12)
for k in range(220): tick(17.55 + 0.95 * R.random(), 3000 + 2500 * R.random(), 0.010, R.uniform(-1, 1), 120)
whoosh(18.85, 0.35, 400, 6000, 0.14)
# 11. Tampon du verdict (19,2)
x = ax(0.6); put(np.sin(2 * np.pi * (48 + 50 * np.exp(-x * 35)) * x) * np.exp(-x * 8) + 0.5 * lp(R.standard_normal(len(x)), 1200) * np.exp(-x * 28), 19.2, 0.55)
# 12. Signature : scintillement doré (21,85) + bouton (22,4)
for kk in range(10): put(tone(1975.5 * 2 ** (kk / 12 * 1.2), 0.7, 5), 21.9 + kk * 0.05, 0.018, (kk / 5) - 1)
put(sum(g * tone(1318.5 * k, 2.0, 2.6 * (1 + 0.4 * i)) for i, (k, g) in enumerate(((1, 1), (2, .25), (3, .08)))), 22.3, 0.08)
put(tone(1568, 0.08, 60), 22.42, 0.06)
# 13. La couette retombe (23,4-24,3) + clic de la lampe (23,95)
x = ax(0.9); put(bp(R.standard_normal(len(x)), 150, 2500) * np.sin(np.pi * x / 0.9) ** 2, 23.4, 0.18)
put(np.sin(2 * np.pi * 45 * ax(0.4)) * np.exp(-ax(0.4) * 9), 24.25, 0.15)
tick(23.95, 3200, 0.09, 0.3, 200); tick(23.965, 1500, 0.05, 0.3, 160)

# Mixage : réverbération courte, SILENCE 8,25-8,45
mixL, mixR = L.copy(), Rt.copy()
for dl, g in ((0.029, .16), (0.043, .13), (0.067, .1), (0.101, .07), (0.157, .045), (0.23, .03)):
    k = int(dl * SR); mixL[k:] += mixR[:-k] * g; mixR[k:] += mixL[:-k] * g
gate = 1 - win(8.25, 8.45, 0.02, 0.005) * 0.985
out = np.stack([mixL * gate, mixR * gate], 1)
out *= np.clip(T / 0.01, 0, 1)[:, None] * np.clip((DUR - T) / 0.05, 0, 1)[:, None]


def limit(x, ceil):
    pkv = maximum_filter1d(np.max(np.abs(x), 1), int(0.006 * SR))
    gr = np.minimum(1.0, ceil / np.maximum(pkv, 1e-9))
    gr = np.minimum(gr, uniform_filter1d(gr, int(0.004 * SR)))
    gr = uniform_filter1d(gr, int(0.003 * SR))
    return x * gr[:, None]


target_rms = float(sys.argv[2]) if len(sys.argv) > 2 else -17.0
ceil = 10 ** (-3.5 / 20)
for _ in range(8):
    rms = np.sqrt(np.mean(out ** 2)); out *= 10 ** (target_rms / 20) / rms
    out = limit(out, ceil * 0.97)
out = np.clip(out, -ceil, ceil) * gate[:, None]
print(f"pic {20*np.log10(np.max(np.abs(out))):.2f} dBFS, RMS {20*np.log10(np.sqrt(np.mean(out**2))):.2f} dBFS")
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
