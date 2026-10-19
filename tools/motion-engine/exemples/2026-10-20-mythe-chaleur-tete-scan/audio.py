#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 3 : la chaleur par la tête ». Synthèse procédurale, seed fixe, 25,4 s.
Usage : python3 audio.py sortie.wav [rms_dbfs]
Calé sur index.html : vent d'hiver + pas lointains dans la neige · clic d'étalonnage 0,9 (+ sifflement électronique)
· bip de palette 3,0 + nappe qui gonfle · silence 5,95-6,2 · bip 6,2 + swoosh de scan 6,2-7,35 + sub 7,35
· clics de zoom 8,4 / 9,6 · 4 tics 8,6-9,2 · 2 notes 11,0 / 11,3 · tampon 12,4 · silence 13,4-13,7 + battement grave
· souffles · silence 17,1-17,4, bonnet 17,4 (laine + choc mat + filtre descendant) · tic étiré 19,0-19,6 · laine 20,0
· swoosh 20,4 · tap 21,6 · scintillement signature 23,1 + pop 23,3 · bonnet qui s'envole 23,4 · ré-armement 25,15 (boucle)."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 25.4; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2010)
L = np.zeros(N); Rt = np.zeros(N)


def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def win(a, b, fa=0.2, fb=0.2): return np.clip((T - a) / fa, 0, 1) * np.clip((b - T) / fb, 0, 1)
def ax(d): return np.arange(int(d * SR)) / SR


def put(sig, t0, g=1.0, pan=0.0):
    i = int(t0 * SR)
    if i >= N: return
    s = sig[:N - i] * g
    L[i:i + len(s)] += s * (1 - max(pan, 0)); Rt[i:i + len(s)] += s * (1 + min(pan, 0))


def tone(f, d, dec):
    x = ax(d); return np.sin(2 * np.pi * f * x) * np.exp(-x * dec)


def noise(d): return R.standard_normal(int(d * SR))


# 1. Vent d'hiver : bruit filtré, rafales lentes (périodiques sur 25,4 s pour la boucle)
w = 2 * np.pi / DUR
gust = 0.55 + 0.25 * np.sin(w * 3 * T + 0.4) + 0.2 * np.sin(w * 7 * T + 1.3)
windL = lp(bp(R.standard_normal(N), 120, 900), 700) * gust
windR = lp(bp(R.standard_normal(N), 120, 900), 700) * gust[::-1]
whistle = bp(R.standard_normal(N), 1400, 1700, 2) * (0.3 + 0.7 * np.clip(np.sin(w * 5 * T), 0, 1)) * 0.25
amb = 0.10 * (1 - 0.6 * win(8.2, 13.4, 0.5, 0.5))  # le vent s'efface sous les chiffres
L += (windL + whistle) * amb; Rt += (windR + whistle) * amb


# 2. Pas lointains dans la neige (craquement doux)
def crunch():
    x = ax(0.16); e = np.exp(-x * 30) * np.clip(x / 0.01, 0, 1)
    return bp(R.standard_normal(len(x)), 900, 4500) * e * (0.6 + 0.4 * np.sin(2 * np.pi * 37 * x))
for i, t0 in enumerate(np.arange(0.2, 25.0, 0.62)):
    if 5.9 < t0 < 6.3 or 17.0 < t0 < 17.5 or 13.35 < t0 < 13.75: continue
    put(crunch(), t0, 0.035 * (0.7 + 0.3 * (i % 2)), 0.55 if i % 2 else 0.35)


# 3. Clic d'étalonnage (obturateur NUC) : double claquement + sifflement électronique
def nuc(g=1.0):
    x = ax(0.6); out = np.zeros(len(x))
    for dt, a in ((0.0, 1.0), (0.034, 0.75)):
        i = int(dt * SR); n = int(0.02 * SR)
        e = R.standard_normal(n) * np.exp(-np.arange(n) / SR * 500) * a
        out[i:i + n] += e
    body = bp(out, 1500, 7000) * 1.4 + lp(out, 900) * 0.6
    body += np.sin(2 * np.pi * 2300 * x) * np.exp(-x * 120) * 0.25
    body += np.sin(2 * np.pi * (7200 + 600 * x) * x) * np.clip((x - 0.06) / 0.05, 0, 1) * np.exp(-x * 6) * 0.03
    return body * g
put(nuc(1.0), 0.9)
for t0 in (8.4, 9.6): put(nuc(0.45), t0, 1.0, 0.2)


# 4. Nappe grave froide → s'ouvre au verdict → se referme au bonnet
pad_c = np.zeros(N); pad_w = np.zeros(N)
for f in (55.0, 82.41, 110.0, 130.81, 164.81):
    for det in (0.997, 1.003): pad_c += np.sin(2 * np.pi * f * det * T) + 0.25 * np.sign(np.sin(2 * np.pi * f * det * T))
for f in (65.41, 98.0, 130.81, 164.81, 246.94):
    for det in (0.997, 1.003): pad_w += np.sin(2 * np.pi * f * det * T) + 0.25 * np.sign(np.sin(2 * np.pi * f * det * T))
warm = win(12.4, 17.4, 0.3, 0.6)
# filtre descendant au bonnet (17,4) : coupe 1400 → 250 Hz, réalisé par fondu entre deux versions
pad = (lp(pad_c, 420) * (1 - warm) + lp(pad_w, 1100) * warm)
dark = lp(pad_c, 160)
dk = np.clip((T - 17.4) / 1.0, 0, 1) * (1 - np.clip((T - 18.4) / 0.8, 0, 1))
pad = pad * (1 - dk) + dark * dk * 1.4
pad_env = 0.5 + 0.5 * win(3.0, 6.0, 1.2, 0.1) + 0.35 * win(12.4, 15.6, 0.2, 0.6)
pad *= 0.010 * pad_env * (1 + 0.12 * np.sin(w * 6 * T))
L += pad; Rt += np.roll(pad, 700)


# 5. Bips de palette 3,0 (vers « white hot ») et 6,2 (retour fer)
def beep(f, d=0.09):
    x = ax(d); return (np.sin(2 * np.pi * f * x) + 0.3 * np.sin(2 * np.pi * 2 * f * x)) * np.clip(x / 0.004, 0, 1) * np.clip((d - x) / 0.01, 0, 1)
put(beep(1760), 3.0, 0.16); put(beep(2093, 0.06), 3.1, 0.12)
put(beep(2349, 0.07), 6.2, 0.15)

# 6. Swoosh ascendant du scan 6,2 → 7,35 + sub à l'arrivée ; même chose à l'envers 13,6 → 14,8
d = 1.15; x = ax(d); k = x / d
f = 300 * (5000 / 300) ** k
sw = np.zeros(len(x)); nz = R.standard_normal(len(x))
for i0 in range(0, len(x), 2048):
    seg = slice(i0, min(len(x), i0 + 2048)); fc = f[i0]
    sw[seg] = bp(nz[max(0, i0 - 2048):seg.stop], fc * 0.7, min(fc * 1.4, 18000))[-(seg.stop - i0):]
sw *= np.sin(np.pi * k) ** 0.7 * 0.5
tonal = np.sin(2 * np.pi * np.cumsum(220 * 4 ** k) / SR) * np.sin(np.pi * k) * 0.06
put(sw + tonal, 6.2, 1.0, -0.2)
xs = ax(1.2); sub = np.sin(2 * np.pi * (50 + 25 * np.exp(-xs * 12)) * xs) * np.exp(-xs * 3) * np.clip(xs / 0.01, 0, 1)
put(sub * 0.75, 7.35)
put((sw + tonal)[::-1] * 0.6, 13.6, 1.0, 0.2)

# 7. Tics secs de la barre de surface 8,6 / 8,8 / 9,0 / 9,2
def tick(f):
    x = ax(0.06); return bp(R.standard_normal(len(x)), f, f * 2.2) * np.exp(-x * 150) + 0.5 * np.sin(2 * np.pi * f * x) * np.exp(-x * 120)
for i, t0 in enumerate((8.6, 8.8, 9.0, 9.2)): put(tick(2400 - 200 * i), t0, 0.28, 0.3)

# 8. Deux notes montantes (colonne « pertes ») 11,0 / 11,3
for t0, fq in ((11.0, 659.25), (11.3, 880.0)):
    put(tone(fq, 1.2, 4) + 0.3 * tone(fq * 2, 1.2, 6) + 0.12 * tone(fq * 3, 1.2, 8), t0, 0.13, 0.15)

# 9. Tampon sourd du verdict 12,4
x = ax(0.6)
stamp = np.sin(2 * np.pi * (65 + 70 * np.exp(-x * 28)) * x) * np.exp(-x * 8) + bp(R.standard_normal(len(x)), 150, 2200) * np.exp(-x * 30) * 0.8
put(stamp * 0.95, 12.4)

# 10. « Mais… » : battement grave 13,75 / 14,55 / 15,35
def thump():
    x = ax(0.5); return np.sin(2 * np.pi * (48 + 30 * np.exp(-x * 20)) * x) * np.exp(-x * 10) * np.clip(x / 0.004, 0, 1)
for t0 in (13.75, 14.55, 15.35):
    put(thump() * 0.7, t0); put(thump() * 0.45, t0 + 0.2)

# 11. Souffles (synchronisés aux nuages tièdes)
for t0 in (0.4, 3.6, 6.9, 10.1, 13.3, 16.2, 17.75, 21.3, 23.45):
    if 5.9 < t0 < 6.3: continue
    xx = ax(1.0); env = np.sin(np.pi * np.clip(xx / 1.0, 0, 1)) ** 2 * np.exp(-xx * 1.5)
    put(bp(R.standard_normal(len(xx)), 400, 2600) * env, t0 - 0.1, 0.05)

# 12. Bonnet 17,4 : frottement de laine (17,25-17,4) + choc mat
def wool(d, g):
    x = ax(d); e = np.sin(np.pi * x / d) ** 1.5
    return bp(R.standard_normal(len(x)), 500, 3500) * e * (0.6 + 0.4 * np.abs(np.sin(2 * np.pi * 17 * x))) * g
put(wool(0.35, 0.35), 17.4)
x = ax(0.4); thud = np.sin(2 * np.pi * (90 + 60 * np.exp(-x * 40)) * x) * np.exp(-x * 14) + lp(R.standard_normal(len(x)), 500) * np.exp(-x * 35) * 0.6
put(thud * 0.75, 17.4)
xd = ax(1.2); put(lp(R.standard_normal(len(xd)), 600) * np.exp(-xd * 2.0) * np.sin(2 * np.pi * np.cumsum(180 * 0.4 ** (xd / 1.2)) / SR) * 0.25, 17.42)
put(wool(0.3, 0.25), 17.95)  # le bonnet s'envole (morphing bébé)

# 13. Tic étiré (segment tête 7 → 19 %) 19,0-19,6 ; laine douce 20,0 (mini-bonnet)
x = ax(0.6); put(np.sin(2 * np.pi * np.cumsum(900 + 1200 * x / 0.6) / SR) * np.sin(np.pi * x / 0.6) * 0.09, 19.0)
put(tick(2600), 19.6, 0.25)
put(wool(0.3, 0.25), 19.85); put(thud * 0.35, 20.0)

# 14. Swoosh 20,4 (retour adulte) ; tap 21,6 sur l'icône d'envoi
x = ax(0.6); put(bp(R.standard_normal(len(x)), 500, 6000) * np.sin(np.pi * x / 0.6) ** 2 * 0.3, 20.35, 1.0, -0.3)
x = ax(0.3); put(np.sin(2 * np.pi * (200 + 220 * np.exp(-x * 40)) * x) * np.exp(-x * 18) * 0.5 + tone(1760, 0.3, 14) * 0.15, 21.6)

# 15. Fin : scintillement doré 23,1, pop d'abonnement 23,3, bonnet qui s'envole 23,4, chaleur qui revient
for kk in range(8): put(tone(2093 * 2 ** (kk / 12 * 1.5), 0.6, 6), 23.05 + kk * 0.05, 0.03, kk / 4 - 1)
x = ax(0.25); put(np.sin(2 * np.pi * np.cumsum(400 + 900 * x / 0.25) / SR) * np.exp(-x * 14) * 0.35, 23.3)
put(wool(0.4, 0.3), 23.4, 1.0, 0.1)
x = ax(0.5); put(bp(R.standard_normal(len(x)), 300, 4000) * np.sin(np.pi * x / 0.5) ** 2 * 0.22, 24.75)
# ré-armement de l'obturateur (servo) 25,15 → coupé net : la boucle enchaîne sur le clic de 0,9 s
x = ax(0.25); put(np.sin(2 * np.pi * np.cumsum(600 + 500 * x / 0.25) / SR) * (x / 0.25) * 0.05 + bp(R.standard_normal(len(x)), 3000, 6000) * (x / 0.25) * 0.04, 25.15)

# Mix : silences (vide avant le clic, 5,95-6,2, 13,4-13,7, 17,1-17,4)
gate = (1 - win(0.75, 0.9, 0.02, 0.002)) * (1 - win(5.95, 6.2, 0.04, 0.003)) * (1 - win(13.4, 13.7, 0.04, 0.01)) * (1 - win(17.1, 17.4, 0.04, 0.003))
mixL, mixR = L.copy(), Rt.copy()
for dl, g in ((0.029, .18), (0.043, .15), (0.067, .11), (0.101, .08), (0.157, .05), (0.233, .03)):
    k = int(dl * SR); mixL[k:] += Rt[:-k] * g; mixR[k:] += L[:-k] * g
out = np.stack([mixL * gate, mixR * gate], 1)
out *= np.clip(T / 0.004, 0, 1)[:, None] * np.clip((DUR - T) / 0.004, 0, 1)[:, None]


def limit(x, ceil):
    pkv = maximum_filter1d(np.max(np.abs(x), 1), int(0.006 * SR))
    gr = np.minimum(1.0, ceil / np.maximum(pkv, 1e-9))
    gr = np.minimum(gr, uniform_filter1d(gr, int(0.004 * SR)))
    gr = uniform_filter1d(gr, int(0.003 * SR))
    return x * gr[:, None]


target = 10 ** (-1.5 / 20)
rms_t = float(sys.argv[2]) if len(sys.argv) > 2 else -17.0
for _ in range(6):
    rms = np.sqrt(np.mean(out ** 2)); out *= 10 ** (rms_t / 20) / rms
    out = limit(out, target * 0.97)
out = np.clip(out, -target, target) * gate[:, None]
print(f"pic {20*np.log10(np.max(np.abs(out))):.2f} dBFS, RMS {20*np.log10(np.sqrt(np.mean(out**2))):.2f} dBFS")
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as wv:
    wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes(pcm.tobytes())
