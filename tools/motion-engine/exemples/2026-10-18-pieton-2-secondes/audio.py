#!/usr/bin/env python3
"""Son original — « Piéton : 2 secondes ». Synthèse procédurale, seed fixe, 24,5 s.
Usage : python3 audio.py sortie.wav
Temps calés sur index.html : tics clignotant 0/1/2 et 21,5/22,5/23,5 (boucle) · essuie-glace 22,15 · aspiration → coup sourd 2,5
(pluie coupée, temps figé) · balayage HUD 2,7 · traversée du pare-brise 5,0 · riser 5,0-7,5 · dings 5,8 / 6,6 · grue 7,5
· crissement 8,3-9,0 · tics de marge 9,0-10,2 · impact « trop tard » 10,2 · compteur 11,0-11,4 + impact 11,4 · rembobinage 11,3-12,3
· pluie + clacs des lampadaires 14,0-15,4 · silence 15,7-16,0 · basse 16,0 · scans 16,0/16,5/17,0 · scratch 17,5
· carillon 18,4 (+18,62 / 18,9) · souffle du recul 19,2-20,8 · avion 21,0-22,2 · signature 23,4."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 24.5; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1810)
L = np.zeros(N); Rt = np.zeros(N)


def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def win(a, b, fa=0.2, fb=0.2): return np.clip((T - a) / fa, 0, 1) * np.clip((b - T) / fb, 0, 1)


def put(sig, t0, g=1.0, pan=0.0):
    i = int(t0 * SR)
    if i >= N: return
    s = sig[:N - i] * g
    L[i:i + len(s)] += s * (1 - max(pan, 0)); Rt[i:i + len(s)] += s * (1 + min(pan, 0))


def tone(f, d, dec):
    x = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * f * x) * np.exp(-x * dec)


def noise(d): return R.standard_normal(int(d * SR))


# 1. Pluie (toit + pare-brise) : 0-2,5 coupée net (passe-bas 0,1 s), revient 14,0 ; ambiance plus lointaine hors POV
rain_env = (np.clip((2.5 - T) / 0.1, 0, 1) * (T < 2.6)
            + np.clip((T - 14.0) / 1.0, 0, 1) * (T < 15.7) * 0.75
            + np.clip((T - 16.0) / 0.15, 0, 1) * (T >= 16.0) * np.where(T < 21.9, 0.6, 1.0))
rn = bp(R.standard_normal(N), 900, 9000) * 0.05
drops = np.zeros(N); ev = np.nonzero(R.random(N) < 260 / SR)[0]
for i in ev:
    n = min(300, N - i); drops[i:i + n] += R.standard_normal(n) * np.exp(-np.arange(n) / 40) * R.uniform(0.1, 0.5)
drops = hp(drops, 1500) * 0.10
L += (rn + drops) * rain_env; Rt += (np.roll(rn, 557) + np.roll(drops, 211)) * rain_env

# 2. Moteur au ralenti (POV : 0-2,5 et 21,9-24,5) + reprise pendant la simulation de freinage (7,8-9,0)
eng_env = (T < 2.5) * 1.0 + np.clip((T - 21.9) / 0.4, 0, 1) + win(7.8, 9.0, 0.1, 0.05) * 0.6
f_eng = 38 + 4 * np.sin(2 * np.pi * 0.3 * T)
ph = 2 * np.pi * np.cumsum(f_eng) / SR
eng = lp(np.sin(ph) + 0.5 * np.sin(2 * ph) + 0.3 * np.sign(np.sin(3 * ph)) * 0.3 + 0.2 * R.standard_normal(N), 220) * 0.09
L += eng * eng_env; Rt += eng * eng_env

# 3. Tic de clignotant (fil rouge + boucle)
def tic(g=1.0):
    x = np.arange(int(0.06 * SR)) / SR
    a = bp(R.standard_normal(len(x)), 1800, 5200) * np.exp(-x * 140) + 0.5 * np.sin(2 * np.pi * 1250 * x) * np.exp(-x * 110)
    b = 0.6 * bp(R.standard_normal(len(x)), 900, 3000) * np.exp(-x * 160)
    out = np.zeros(int(0.32 * SR)); out[:len(x)] += a; out[int(0.24 * SR):int(0.24 * SR) + len(x)] += b * 0.7
    return out * g
for t0 in (0.0, 1.0, 2.0, 21.5, 22.5, 23.5):
    put(tic(), t0 + 0.005, 0.32, -0.25)

# 4. Essuie-glace 1,3 : « fwoump » aller-retour + petit grincement
for t0, d in ((22.15, 0.25), (22.4, 0.25)):
    x = np.arange(int(d * SR)) / SR
    sw = bp(R.standard_normal(len(x)), 300, 2500) * np.sin(np.pi * x / d) ** 2
    sq = np.sin(2 * np.pi * np.cumsum(1900 + 500 * np.sin(np.pi * x / d)) / SR) * np.sin(np.pi * x / d) ** 6 * 0.15
    put(sw * 0.35 + sq, t0, 1.0, 0.3 if t0 < 22.3 else -0.3)

# 5. Aspiration (whoosh inversé) qui culmine à 2,5 + coup sourd sub 45 Hz + nappe tenue du temps figé
d = 0.8; x = np.arange(int(d * SR)) / SR
asp = bp(R.standard_normal(len(x)), 300, 6000) * (x / d) ** 3
put(asp * 0.6, 2.5 - d)
x = np.arange(int(0.9 * SR)) / SR
thud = np.sin(2 * np.pi * (45 + 40 * np.exp(-x * 25)) * x) * np.exp(-x * 4.5) + 0.3 * lp(R.standard_normal(len(x)), 300) * np.exp(-x * 20)
put(thud * 0.95, 2.5)
pad = np.zeros(N)
for f in (55, 65.41, 82.41, 98.0, 110.0):
    for det in (0.997, 1.003):
        pad += np.sin(2 * np.pi * f * det * T) + 0.35 * np.sign(np.sin(2 * np.pi * f * det * T))
pad_dark = lp(pad, 240) * 0.012; pad_open = lp(pad, 1400) * 0.010
pad_env = win(2.5, 15.7, 0.3, 0.3) + win(16.0, 24.5, 0.2, 0.3) * 0.8
openk = np.clip((T - 18.4) / 0.4, 0, 1) * (T < 21.0)
padx = pad_dark * (1 - openk) + pad_open * openk
L += padx * pad_env; Rt += np.roll(padx, 700) * pad_env

# 6. Balayage HUD 2,7-3,2 : scintillement montant
x = np.arange(int(0.55 * SR)) / SR
put(np.sin(2 * np.pi * np.cumsum(2000 + 4000 * x / 0.55) / SR) * np.sin(np.pi * x / 0.55) ** 2 * 0.05, 2.7, 1.0, -0.4)
put(hp(R.standard_normal(len(x)), 5000) * np.sin(np.pi * x / 0.55) ** 2 * 0.08, 2.7, 1.0, 0.4)

# 7. Traversée du pare-brise 5,0 (souffle + « tink ») ; riser 5,0 → 7,5 ; dings 5,8 et 6,6
x = np.arange(int(0.45 * SR)) / SR
put(bp(R.standard_normal(len(x)), 500, 5000) * np.sin(np.pi * x / 0.45) ** 2 * 0.35, 4.95)
put(tone(3300, 0.6, 9), 5.15, 0.05)
d = 2.5; x = np.arange(int(d * SR)) / SR
riser = bp(R.standard_normal(len(x)), 200, 4000) * (x / d) ** 2 * 0.22
riser += np.sin(2 * np.pi * np.cumsum(110 + 330 * (x / d) ** 2) / SR) * (x / d) ** 2 * 0.06
riser *= np.clip((d - x) / 0.08, 0, 1)
put(riser, 5.0)
for t0, f in ((5.8, 1760), (6.6, 2637)):
    for k, g in ((1, 1), (2.76, .35), (5.4, .15)):
        put(tone(f * k, 1.4, 4.5), t0, 0.10 * g, 0.2)

# 8. Grue vers la vue de dessus 7,5-8,1 : souffle large
x = np.arange(int(0.7 * SR)) / SR
put(bp(R.standard_normal(len(x)), 250, 3000) * np.sin(np.pi * x / 0.7) ** 2 * 0.3, 7.45, 1.0, -0.2)

# 9. Freinage simulé : crissement 8,3 → 9,0 qui s'arrête net, impact sourd à 9,0
d = 0.7; x = np.arange(int(d * SR)) / SR
f = 2300 - 500 * x / d + 60 * np.sin(2 * np.pi * 23 * x)
scr = (np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.5 * np.sin(2 * np.pi * np.cumsum(f * 1.5) / SR)) * 0.5
scr = scr * (0.6 + 0.4 * bp(R.standard_normal(len(x)), 10, 60) * 3) + bp(R.standard_normal(len(x)), 1500, 6000) * 0.6
scr *= np.clip(x / 0.05, 0, 1) * np.clip((d - x) / 0.015, 0, 1)
put(scr * 0.16, 8.3, 1.0, 0.1)
x = np.arange(int(0.5 * SR)) / SR
put(np.sin(2 * np.pi * (60 + 30 * np.exp(-x * 30)) * x) * np.exp(-x * 7) * 0.6, 9.0)
for k in range(3):  # tics de la marge qui clignote
    put(tic(0.8), 9.05 + k * 0.4, 0.28, 0.2)

# 10. « Trop tard » 10,2 : impact grave + éclat filtré
x = np.arange(int(1.2 * SR)) / SR
hit = np.sin(2 * np.pi * (42 + 70 * np.exp(-x * 18)) * x) * np.exp(-x * 3.2) + 0.5 * bp(R.standard_normal(len(x)), 200, 3000) * np.exp(-x * 9)
put(hit * 0.9, 10.2)

# 11. Bascule vers l'horloge 11,0 ; rembobinage 11,3-12,3 ; impact 12,3 ; tics du compteur
x = np.arange(int(0.6 * SR)) / SR
put(bp(R.standard_normal(len(x)), 300, 3500) * np.sin(np.pi * x / 0.6) ** 2 * 0.25, 10.95, 1.0, 0.3)
d = 1.0; x = np.arange(int(d * SR)) / SR
fr = 900 * (1 - 0.7 * x / d) + 150 * np.sin(2 * np.pi * 9 * x)
rew = np.sin(2 * np.pi * np.cumsum(fr) / SR) * 0.4 + bp(R.standard_normal(len(x)), 800, 5000) * 0.5
rew *= (x / d) ** 0.5 * np.clip((d - x) / 0.05, 0, 1) * (0.7 + 0.3 * np.sin(2 * np.pi * 14 * x))
put(rew * 0.22, 11.3, 1.0, -0.2)
x = np.arange(int(0.9 * SR)) / SR
put((np.sin(2 * np.pi * (50 + 60 * np.exp(-x * 20)) * x) * np.exp(-x * 4) + 0.3 * bp(R.standard_normal(len(x)), 100, 2000) * np.exp(-x * 12)) * 0.8, 11.4)
def click():
    x = np.arange(int(0.025 * SR)) / SR
    return bp(R.standard_normal(len(x)), 2500, 7000) * np.exp(-x * 260) + 0.4 * np.sin(2 * np.pi * 2100 * x) * np.exp(-x * 200)
tt = 11.0
while tt < 11.4:
    put(click(), tt, 0.22, 0.15)
    p = (tt - 11.0) / 0.4
    tt += 0.03 + 0.07 * p ** 2

# 12. Changement d'heure 14,0 : nappe descendante, clacs des lampadaires en cascade
x = np.arange(int(1.6 * SR)) / SR
put(np.sin(2 * np.pi * np.cumsum(330 * 0.5 ** (x / 1.6)) / SR) * np.sin(np.pi * x / 1.6) * 0.07, 14.0)
for k in range(9):
    t0 = 14.42 + k * 0.11 + 0.02 * np.sin(k * 3.1)
    x = np.arange(int(0.12 * SR)) / SR
    cl = bp(R.standard_normal(len(x)), 300, 2500) * np.exp(-x * 60) + 0.5 * np.sin(2 * np.pi * 120 * x) * np.exp(-x * 40)
    hum = np.sin(2 * np.pi * 100 * np.arange(int(0.4 * SR)) / SR) * np.exp(-np.arange(int(0.4 * SR)) / SR * 6) * 0.15
    put(cl * 0.4 * (1 - k * 0.06), t0, 1.0, 0.6 - k * 0.13); put(hum, t0, 0.5 * (1 - k * 0.08))

# 13. Silence 15,7-16,0 (géré au mixage) puis basse 16,0 ; scans de tenue 16,0 / 16,5 / 17,0
x = np.arange(int(1.2 * SR)) / SR
put(np.sin(2 * np.pi * 50 * x) * np.exp(-x * 2.5) * np.clip(x / 0.01, 0, 1) * 0.75, 16.0)
for t0 in (16.0, 16.5, 17.0):
    x = np.arange(int(0.2 * SR)) / SR
    put(np.sin(2 * np.pi * np.cumsum(3000 - 2000 * x / 0.2) / SR) * np.sin(np.pi * x / 0.2) ** 2 * 0.06, t0 + 0.02, 1.0, 0.2)

# 14. Scratch (velcro) 17,5 ; phares qui approchent 17,9-18,4 ; carillon 18,4 (+ 18,62 / 18,9)
d = 0.28; x = np.arange(int(d * SR)) / SR
vel = bp(R.standard_normal(len(x)), 1500, 8000) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 70 * x))) * np.sin(np.pi * x / d) ** 0.5
put(vel * 0.35, 17.5, 1.0, 0.25)
x = np.arange(int(0.5 * SR)) / SR
put(bp(R.standard_normal(len(x)), 200, 1500) * (x / 0.5) ** 2 * 0.25, 17.9)
for t0, base, g in ((18.4, 1568, 1.0), (18.62, 1975.5, 0.55), (18.9, 2349.3, 0.5)):
    for k, gg in ((1, 1), (2, .4), (3, .2), (4.2, .1)):
        put(tone(base * k, 2.2, 2.4), t0, 0.11 * g * gg, (t0 - 18.6) * 1.5)

# 15. Recul 150 m 19,2-20,8 : souffle de vitesse ; avion 21,0-22,2 (panoramique droite → gauche) ; vitre 21,9
d = 1.6; x = np.arange(int(d * SR)) / SR
put(bp(R.standard_normal(len(x)), 300, 5000) * np.sin(np.pi * x / d) ** 1.5 * 0.3, 19.2)
d = 1.2; x = np.arange(int(d * SR)) / SR
fl = bp(R.standard_normal(len(x)), 700, 6000) * np.sin(np.pi * x / d) ** 2 * 0.35
i0 = int(21.0 * SR)
pan = np.linspace(0.9, -0.9, len(x))
L[i0:i0 + len(x)] += fl * (1 - np.maximum(pan, 0)); Rt[i0:i0 + len(x)] += fl * (1 + np.minimum(pan, 0))
put(tone(3000, 0.5, 10), 21.9, 0.04)

# 16. Signature 23,4 : scintillement doré
for k in range(10):
    put(tone(2093 * 2 ** (k / 12 * 1.2), 0.7, 5), 23.4 + k * 0.045, 0.03, (k / 5) - 1)

# Mix : silence total 15,7-16,0 ; réverbération courte ; normalisation (WAV : pic -2 dB, RMS ≈ -17,5 dB)
gate = 1 - win(15.72, 15.98, 0.03, 0.02)
mixL, mixR = L.copy(), Rt.copy()
for dl, g in ((0.029, .22), (0.043, .18), (0.067, .13), (0.101, .09), (0.157, .06)):
    k = int(dl * SR); mixL[k:] += Rt[:-k] * g; mixR[k:] += L[:-k] * g
out = np.stack([mixL * gate, mixR * gate], 1)
out *= np.clip(T / 0.004, 0, 1)[:, None]
def limit(x, ceil):
    pkv = maximum_filter1d(np.max(np.abs(x), 1), int(0.006 * SR))
    gr = np.minimum(1.0, ceil / np.maximum(pkv, 1e-9))
    gr = np.minimum(gr, uniform_filter1d(gr, int(0.004 * SR)))
    gr = uniform_filter1d(gr, int(0.003 * SR))
    return x * gr[:, None]
target = 10 ** (-2.0 / 20)
for _ in range(6):
    rms = np.sqrt(np.mean(out ** 2)); out *= 10 ** (-17.5 / 20) / rms
    out = limit(out, target * 0.97)
out = np.clip(out, -target, target) * gate[:, None]
print(f"pic {20*np.log10(np.max(np.abs(out))):.2f} dBFS, RMS {20*np.log10(np.sqrt(np.mean(out**2))):.2f} dBFS")
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
