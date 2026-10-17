#!/usr/bin/env python3
"""Son original — Mythe ou science ? ép. 1 (vitamine C). Synthèse procédurale, seed fixe, 27,0 s.
Usage : python3 audio.py sortie.wav
Temps calés sur index.html : impact 0,1 · barre 0,4 · souffle 3,2 · tintement 4,08 · plops 5,55+0,085·rangée
· basse 7,3 · tics 9,2-14,6 · riser 13,6 · givre 14,6 · pop collectif 16,2 · silence piège 17,9 · eau 19,4
· ding 22,0 · pops 22,45/23,25 · crac 24,9 · ploc boucle 26,95."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt

SR = 44100; DUR = 27.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(17)
L = np.zeros(N); Rt = np.zeros(N)


def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def env_win(a, b, fa=0.2, fb=0.2): return np.clip((T - a) / fa, 0, 1) * np.clip((b - T) / fb, 0, 1)


def put(sig, t0, g=1.0, pan=0.0):
    i = int(t0 * SR)
    if i >= N: return
    s = sig[:N - i] * g
    L[i:i + len(s)] += s * (1 - max(pan, 0)); Rt[i:i + len(s)] += s * (1 + min(pan, 0))


def tone(f, d, dec, ph=0):
    x = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * f * x + ph) * np.exp(-x * dec)


def bubble(f0, d=0.06, g=1.0):  # plop de bulle : sinus à fréquence montante (Minnaert)
    x = np.arange(int(d * SR)) / SR
    f = f0 * (1 + 2.2 * x / d)
    return g * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x * (5 / d)) * np.clip(x / 0.002, 0, 1)


# 1. Pétillement (fil rouge) : milliers de micro-bulles + bruit filtré
fizz_env = (np.clip((T - 0.1) / 0.15, 0, 1) * (1 - 0.5 * np.clip((T - 3.4) / 1.0, 0, 1))
            * (1 - 0.75 * np.clip((T - 7.3) / 0.4, 0, 1) * (T < 9.2)) * (T < 17.9)
            + 0.55 * env_win(25.3, 27.0, 0.6, 0.02) + 0.35 * env_win(19.4, 22.0, 0.3, 0.3))
fz = hp(R.standard_normal(N), 3500) * 0.022
L += fz * fizz_env; Rt += np.roll(fz, 331) * fizz_env
ev = R.random(N) < (120 / SR)
for i in np.nonzero(ev)[0]:
    t0 = i / SR; g = np.interp(t0, T[::441], fizz_env[::441])
    if g < 0.02: continue
    put(bubble(R.uniform(1800, 6500), R.uniform(0.012, 0.03)), t0, 0.05 * g, R.uniform(-0.8, 0.8))

# 2. Nappe : accord grave mineur, filtre qui s'ouvre (démarre 1,6)
pad = np.zeros(N)
for f in (55, 82.41, 110, 130.81, 164.81):
    for det in (0.996, 1.004):
        pad += np.sign(np.sin(2 * np.pi * f * det * T)) * 0.5 + np.sin(2 * np.pi * f * det * T)
pad_open = lp(pad * 0.004, 900)
pad_env = (np.clip((T - 1.6) / 1.2, 0, 1) * (1 - 0.35 * ((T > 17.9) & (T < 19.4))) * np.clip((27.0 - T) / 0.4, 0, 1))
mixk = np.clip((T - 1.6) / 10, 0, 1)
padx = lp(pad * 0.004, 260) * (1 - mixk) + pad_open * mixk
L += padx * pad_env * 3.2; Rt += np.roll(padx, 600) * pad_env * 3.2

# 3. Impact « ploc » + sub (0,1) et boucle (26,95 coupé)
x = np.arange(int(0.35 * SR)) / SR
ploc = np.sin(2 * np.pi * (140 + 260 * np.exp(-x * 30)) * x) * np.exp(-x * 14)
sub = np.sin(2 * np.pi * 50 * x) * np.exp(-x * 9)
splash = bp(R.standard_normal(len(x)), 1200, 6000) * np.exp(-x * 18)
put(ploc * 0.5 + sub * 0.55 + splash * 0.25, 0.1)
put((ploc * 0.5 + splash * 0.2)[: int(0.05 * SR)], 26.95, 0.8)

# 4. « zip » de la barre (0,4)
x = np.arange(int(0.2 * SR)) / SR
zip_ = bp(R.standard_normal(len(x)), 2500, 9000) * np.sin(np.pi * x / 0.2) ** 2
put(zip_ * 0.35, 0.4, pan=-0.3); put(zip_ * 0.35, 0.45, pan=0.3)

# 5. Bulle solitaire (2,8)
put(bubble(900, 0.12), 2.8, 0.35, 0.6)

# 6. Souffle aspiré inversé (2,8 → 3,4) + tintement cristallin à la recomposition (4,08)
d = 0.6; x = np.arange(int(d * SR)) / SR
sw = bp(R.standard_normal(len(x)), 400, 5000) * (x / d) ** 2.5
put(sw * 0.55, 2.8)
for f, g in ((2093, 1), (3136, .5), (4186, .35), (5274, .2)):
    put(tone(f, 1.6, 3.2), 4.08, 0.11 * g, 0.2)
put(tone(1046.5, 1.2, 4), 4.08, 0.06)

# 7. Tics du compteur = bulles qui éclatent (4,0 → 4,85, de plus en plus serrés)
tt = 4.0
while tt < 4.85:
    put(bubble(R.uniform(1500, 3000), 0.02), tt, 0.16, R.uniform(-.5, .5))
    tt += 0.09 * (1 - (tt - 4.0) / 1.1) + 0.02

# 8. Grilles : 10 plops montants (rangées), le 10e étouffé (5,55 + 0,085 r)
for rw in range(10):
    f = 500 * 2 ** (rw / 12 * 1.6)
    s = bubble(f, 0.07)
    if rw == 9: s = lp(s, 700) * 0.6
    put(s, 5.55 + rw * 0.085 + 0.05, 0.42, 0.25)
for i in range(10):  # grille violette qui se range (5,2-5,7)
    put(bubble(R.uniform(350, 600), 0.05), 5.2 + i * 0.045, 0.12, -0.4)

# 9. Basse descendante (7,3 → 8,5)
x = np.arange(int(1.3 * SR)) / SR
f = 80 * (0.5 ** (x / 1.3))
put(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * x / 1.3) * 0.5, 7.3)
put(tone(1318, 0.5, 8), 7.72, 0.06)  # clignotement des anneaux

# 10. Tics d'horloge (bois) 2/s, 9,2 → 14,6 ; « glou » 10,05 et 11,9
def wood():
    x = np.arange(int(0.05 * SR)) / SR
    return bp(R.standard_normal(len(x)), 1500, 3200) * np.exp(-x * 120) + 0.4 * np.sin(2 * np.pi * 900 * x) * np.exp(-x * 90)
for k, tt in enumerate(np.arange(9.25, 14.55, 0.5)):
    put(wood(), tt, 0.28, -0.35 if k % 2 else 0.35)
for t0 in (10.05, 11.9):
    x = np.arange(int(0.5 * SR)) / SR
    put(lp(np.sin(2 * np.pi * (220 - 80 * x) * x) * np.exp(-x * 6), 600) * 0.25, t0)
put(bubble(700, 0.25), 11.25, 0.18)  # tube enfant qui se forme

# 11. Riser filtré (13,6 → 14,6) puis givre (14,6) : craquement + vent froid
d = 1.0; x = np.arange(int(d * SR)) / SR
rs = bp(R.standard_normal(len(x)), 300, 6000) * (x / d) ** 2
put(rs * 0.4, 13.6)
put(np.sin(2 * np.pi * np.cumsum(200 + 900 * (x / d) ** 2) / SR) * (x / d) ** 2 * 0.12, 13.6)
x = np.arange(int(0.9 * SR)) / SR
cr = np.zeros(len(x))
for _ in range(260):
    i = int(R.uniform(0, 0.8) * SR); cr[i:i + 40] += R.standard_normal(min(40, len(x) - i)) * np.exp(-i / SR * 3)
put(hp(cr, 3000) * 0.22, 14.6)
put(tone(4400, 1.2, 3), 14.62, 0.05)
put(hp(R.standard_normal(int(0.25 * SR)), 2000) * np.exp(-np.arange(int(0.25 * SR)) / SR * 14) * 0.35, 14.58)  # crève la surface
wind = bp(R.standard_normal(N), 250, 1400) * env_win(14.6, 17.9, 0.5, 0.4) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.35 * T))
L += wind * 0.05; Rt += np.roll(wind, 2000) * 0.05

# 12. Battements de cœur (2, puis accélérés) 14,9 → 16,1 ; pop collectif 16,2
def beat():
    x = np.arange(int(0.25 * SR)) / SR
    return np.sin(2 * np.pi * 55 * x) * np.exp(-x * 16)
for t0 in (14.95, 15.55, 15.85, 16.05):
    put(beat(), t0, 0.6); put(beat(), t0 + 0.13, 0.35)
x = np.arange(int(0.6 * SR)) / SR
put(np.sin(2 * np.pi * (60 * np.exp(-x * 1.5)) * x) * np.exp(-x * 5) * 0.7, 16.2)
for _ in range(100):
    put(bubble(R.uniform(900, 4000), 0.03), 16.2 + R.uniform(0, 0.12), 0.08, R.uniform(-1, 1))

# 13. Piège : silence relatif (pétillement coupé) ; eau qui coule 19,4 → 20,3 ; tic qui accélère ; ding 22,0
water = bp(R.standard_normal(N), 300, 4000) * env_win(19.4, 20.4, 0.08, 0.35) * (0.7 + 0.3 * np.sin(2 * np.pi * 7 * T))
L += water * 0.10; Rt += np.roll(water, 900) * 0.10
tt = 20.2
while tt < 21.95:
    p = (tt - 20.2) / 1.8
    put(wood(), tt, 0.2 + 0.1 * p, 0.2)
    tt += 0.28 * (1 - p) + 0.07
for f, g in ((1568, 1), (2349, .6), (3136, .4), (4699, .2)):
    put(tone(f, 1.8, 2.6), 22.0, 0.12 * g)

# 14. Pops doux des pulsations (22,45 / 23,25)
for t0 in (22.45, 23.25):
    put(bubble(420, 0.12), t0, 0.4); put(tone(110, 0.3, 12), t0, 0.3)

# 15. Carte qui se retourne (24,4 souffle) + « crac » sec (24,9)
x = np.arange(int(0.5 * SR)) / SR
put(bp(R.standard_normal(len(x)), 600, 4000) * np.sin(np.pi * x / 0.5) ** 2 * 0.2, 24.4)
crk = np.zeros(int(0.12 * SR))
for k, (o, g) in enumerate(((0, 1), (0.012, .7), (0.021, .5), (0.034, .3))):
    i = int(o * SR); n = int(0.008 * SR)
    crk[i:i + n] += R.standard_normal(n) * g * np.exp(-np.arange(n) / n * 4)
put(bp(crk, 800, 7000) * 0.9, 24.9)
put(tone(180, 0.15, 30), 24.9, 0.3)

# 16. Fin : balayage doré de la signature (25,5) — scintillement
for k in range(12):
    put(tone(2637 * 2 ** (k / 12), 0.6, 6), 25.5 + k * 0.04, 0.025, (k / 6) - 1)

# Mix : légère réverbération (échos décroissants), normalisation
mixL, mixR = L.copy(), Rt.copy()
for dl, g in ((0.031, .25), (0.047, .2), (0.073, .15), (0.11, .1), (0.17, .07)):
    k = int(dl * SR)
    mixL[k:] += Rt[:-k] * g; mixR[k:] += L[:-k] * g
out = np.stack([mixL, mixR], 1)
out *= np.clip(T / 0.01, 0, 1)[:, None]
from scipy.ndimage import maximum_filter1d, uniform_filter1d
def limit(x, ceil):  # limiteur à anticipation : enveloppe de crête lissée
    pkv = maximum_filter1d(np.max(np.abs(x), 1), int(0.006 * SR))
    gr = np.minimum(1.0, ceil / np.maximum(pkv, 1e-9))
    gr = np.minimum(gr, uniform_filter1d(gr, int(0.004 * SR)))
    gr = uniform_filter1d(gr, int(0.003 * SR))
    return x * gr[:, None]
target = 10 ** (-1.3 / 20)
for _ in range(6):
    rms = np.sqrt(np.mean(out ** 2)); out *= 10 ** (-17.0 / 20) / rms
    out = limit(out, target * 0.97)
out = np.clip(out, -target, target)
print(f"pic {20*np.log10(np.max(np.abs(out))):.2f} dBFS, RMS {20*np.log10(np.sqrt(np.mean(out**2))):.2f} dBFS")
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
