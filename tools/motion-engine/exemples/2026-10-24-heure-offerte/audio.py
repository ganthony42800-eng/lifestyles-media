#!/usr/bin/env python3
"""Son original — « Le chiffre qui pique · ép. 2 : l'heure offerte ». Synthèse procédurale, seed fixe, 26,0 s.
Usage : python3 audio.py sortie.wav
Temps calés sur index.html : tic-tac d'une pendule lointaine 0-2,6 et 25,2-26 (raccord de boucle) · respiration du dormeur
(0,23 Hz, comme la caméra) · déclic 1,40 · rembobinage + craquement numérique 1,50-1,75 · nappe 2,6 · cristal du trait 60 à 3,1
· souffle du filé 4,55 / 7,5 · bips capteur 4,85 / 5,6 / 6,35 / 7,1 + scintillement 5,6 · remplissage dont la hauteur monte 8,0-9,8
· ding de verre 9,8 · impact 10,2 + trois tics du fantôme · filé 12,6 + notification 12,7 + souffle de la carte 13,0 + 2 pulsations
d'envoi · SILENCE TOTAL 15,0-15,3 (clignement) · sonnerie 2 notes + vibration 15,3 · glouglou 15,6-17,4 · aube : nappe qui s'éclaire
+ un oiseau 18,6 + 7 gouttes régulières 18,45-19,05 · tracé + pop du marque-page 20,8 / 21,33 · sonnerie courte 23,0 · pulsations
SNOOZE · bascule de la pastille 23,6 · scintillement doré signature 23,9 · retour du tic-tac 25,25."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 26.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2410)
L = np.zeros(N); Rt = np.zeros(N)


def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def win(a, b, fa=0.2, fb=0.2): return np.clip((T - a) / fa, 0, 1) * np.clip((b - T) / fb, 0, 1)
def ax(d): return np.arange(int(d * SR)) / SR
def noise(d): return R.standard_normal(int(d * SR))


def put(sig, t0, g=1.0, pan=0.0):
    i = int(round(t0 * SR))
    if i >= N: return
    s = sig[:N - i] * g
    L[i:i + len(s)] += s * (1 - max(pan, 0)); Rt[i:i + len(s)] += s * (1 + min(pan, 0))


def tone(f, d, dec, ph=0.0):
    x = ax(d); return np.sin(2 * np.pi * f * x + ph) * np.exp(-x * dec)


def bell(f, d, dec, parts=((1, 1), (2.76, .35), (5.4, .15), (8.93, .06))):
    return sum(g * tone(f * k, d, dec * (1 + 0.4 * i)) for i, (k, g) in enumerate(parts))


# 1. Ambiance de chambre : bruit de pièce très bas + respiration lente (0,23 Hz = 6 cycles / 26 s)
room = lp(R.standard_normal(N), 900) * 0.010 + lp(R.standard_normal(N), 180) * 0.012
br_ph = np.sin(2 * np.pi * 6 * T / DUR)
breath_env = np.clip(br_ph, 0, 1) ** 1.5 * 0.9 + np.clip(-br_ph, 0, 1) ** 2 * 0.5
breath = bp(R.standard_normal(N), 300, 1800) * breath_env * 0.020
amb = room + breath
L += amb; Rt += np.roll(amb, 331)

# 2. Tic-tac d'une pendule d'une autre pièce (fil rouge, et raccord de boucle : 25,25 / 25,5 / 25,75 → 26,0 = 0,0)
def tick(hi=True):
    x = ax(0.07)
    a = bp(R.standard_normal(len(x)), 1500 if hi else 1100, 4800 if hi else 3600) * np.exp(-x * 120)
    a += 0.45 * np.sin(2 * np.pi * (1900 if hi else 1500) * x) * np.exp(-x * 90)
    return lp(a, 5000)
for k, t0 in enumerate((0.0, 0.5, 1.0, 1.85, 2.35, 25.25, 25.5, 25.75)):
    put(tick(k % 2 == 0), t0 + 0.004, 0.26 if t0 < 3 or t0 > 25 else 0.2, -0.35)

# 3. 1,40 : déclic sec (03:00) ; 1,50-1,75 : bande rembobinée + craquement numérique ; 1,75 : tout se pose
x = ax(0.05); put(bp(R.standard_normal(len(x)), 2000, 8000) * np.exp(-x * 200) + 0.6 * np.sin(2 * np.pi * 900 * x) * np.exp(-x * 120), 1.40, 0.6)
d = 0.27; x = ax(d)
fr = 1400 * (1 - 0.75 * x / d) + 220 * np.sin(2 * np.pi * 16 * x)
rew = np.sin(2 * np.pi * np.cumsum(fr) / SR) * 0.5 + bp(R.standard_normal(len(x)), 700, 6000) * 0.6
rew *= np.clip(x / 0.01, 0, 1) * np.clip((d - x) / 0.03, 0, 1) * (0.6 + 0.4 * np.sign(np.sin(2 * np.pi * 34 * x)))
put(rew * 0.38, 1.50, 1.0, -0.15)
crk = np.zeros(int(0.25 * SR))
for i in range(40):
    j = int(R.uniform(0, len(crk) - 400)); crk[j:j + 300] += R.standard_normal(300) * np.exp(-np.arange(300) / 40) * R.uniform(0.3, 1)
put(hp(crk, 2500) * 0.22, 1.50, 1.0, 0.25)
x = ax(0.6); put(np.sin(2 * np.pi * (55 + 50 * np.exp(-x * 25)) * x) * np.exp(-x * 6) * 0.55, 1.75)

# 4. Nappe grave (accord tenu, ouvert à 2,6, s'éclaire à l'aube 18,2-23, redescend vers la nuit 24,4-25,2)
pad = np.zeros(N)
for f in (55.0, 82.41, 110.0, 130.81, 164.81):
    for det in (0.996, 1.004):
        pad += np.sin(2 * np.pi * f * det * T) + 0.3 * np.sin(4 * np.pi * f * det * T)
dark = lp(pad, 260) * 0.016; bright = lp(pad, 1600) * 0.010
dawn = np.clip((T - 18.2) / 1.2, 0, 1) * (1 - np.clip((T - 24.4) / 0.8, 0, 1))
pad_env = win(2.6, 25.25, 0.6, 0.4) * (1 + 0.25 * dawn)
padx = (dark * (1 - dawn) + bright * dawn) * pad_env
L += padx; Rt += np.roll(padx, 900)

# 5. 3,1 : trait 60 qui s'allume (cristal qui fait le tour du verre, de gauche à droite)
for k in range(8):
    put(bell(2637 * 2 ** (k / 24), 1.2, 6), 3.10 + k * 0.034, 0.025, -0.7 + k * 0.2)

# 6. Souffles des panoramiques filés (4,55 / 7,5 / 12,6) et recul punch (10,2)
for t0, dd, g in ((4.55, 0.45, 0.32), (7.5, 0.5, 0.28), (12.58, 0.35, 0.4)):
    x = ax(dd); put(bp(R.standard_normal(len(x)), 300, 5000) * np.sin(np.pi * x / dd) ** 2 * g, t0, 1.0, 0.3)

# 7. Capteur : bips 2 kHz 60 ms à chaque pulsation LED ; 5,6 : scintillement des 7 211 points
for t0 in (4.85, 5.6, 6.35, 7.1):
    x = ax(0.07); put(np.sin(2 * np.pi * 2000 * x) * np.clip(x / 0.004, 0, 1) * np.clip((0.07 - x) / 0.01, 0, 1), t0, 0.075, 0.2)
x = ax(0.9); sh = hp(R.standard_normal(len(x)), 6000) * np.exp(-x * 3.5) * (0.5 + 0.5 * np.sin(2 * np.pi * 37 * x))
put(sh * 0.10, 5.6, 1.0, -0.3); put(np.roll(sh, 999) * 0.10, 5.62, 1.0, 0.3)
for k in range(12):
    put(tone(3500 + 220 * k, 0.25, 18), 5.6 + k * 0.05, 0.012, R.uniform(-0.8, 0.8))
x = ax(0.06); put(bp(R.standard_normal(len(x)), 1000, 4000) * np.exp(-x * 90), 6.4, 0.18)   # « 43-78 ans »

# 8. 8,0-9,8 : remplissage dont la hauteur monte (résonance d'un verre qu'on remplit) + bulles ; 9,8 : ding de verre
d = 1.8; x = ax(d); k = x / d
fc = 380 + 1700 * (1 - (1 - k) ** 2)
pour = bp(R.standard_normal(len(x)), 200, 6000) * 0.25
res = np.zeros(len(x))
seg = int(0.02 * SR)
for i in range(0, len(x), seg):
    f0 = fc[i]; xx = x[i:i + seg]
    res[i:i + seg] = bp(pour[max(0, i - 2 * seg):i + seg], f0 * 0.9, f0 * 1.1)[-len(xx):]
fill = (res * 3.0 + pour * 0.25) * np.clip(x / 0.15, 0, 1) * np.clip((d - x) / 0.03, 0, 1)
put(fill * 0.6, 8.0, 1.0, 0.15)
for i in range(26):
    t0 = 8.05 + R.uniform(0, 1.7); x = ax(0.05); f = R.uniform(700, 1500) * (1 + (t0 - 8.0) / 1.8)
    put(np.sin(2 * np.pi * np.cumsum(f * (1 + 2 * x)) / SR) * np.exp(-x * 80), t0, 0.04, R.uniform(-0.4, 0.6))
put(bell(1975.5, 2.6, 2.2), 9.80, 0.17, 0.15); put(bell(2959.9, 2.0, 3.0), 9.805, 0.06, 0.2)

# 9. 10,2 : impact grave sub 45 Hz ; trois tics électriques sur les clignotements du fantôme ; 10,8 « Pas 60. »
x = ax(1.1); put(np.sin(2 * np.pi * (45 + 60 * np.exp(-x * 18)) * x) * np.exp(-x * 3.2) + 0.4 * bp(R.standard_normal(len(x)), 150, 2500) * np.exp(-x * 10), 10.2, 0.9)
for t0 in (10.2, 10.6, 11.0):
    x = ax(0.06); put(bp(R.standard_normal(len(x)), 3000, 9000) * np.exp(-x * 120) + 0.3 * np.sign(np.sin(2 * np.pi * 120 * x)) * np.exp(-x * 80), t0 + 0.01, 0.2, -0.2)
x = ax(0.5); put(np.sin(2 * np.pi * (70 + 40 * np.exp(-x * 30)) * x) * np.exp(-x * 9) * 0.45, 10.8)

# 10. 12,7 : notification (synthé maison, deux notes douces) ; 13,0 : souffle de la carte qui sort ; 13,75 / 14,25 : envoi
put(bell(1318.5, 0.8, 7, ((1, 1), (2, .3))), 12.70, 0.09, -0.2); put(bell(1760, 0.9, 6, ((1, 1), (2, .3))), 12.80, 0.08, -0.2)
d = 0.5; x = ax(d); put(bp(R.standard_normal(len(x)), 800, 7000) * (x / d) ** 2 * np.clip((d - x) / 0.05, 0, 1) * 0.25, 12.95)
for t0 in (13.75, 14.25):
    x = ax(0.18); put(np.sin(2 * np.pi * np.cumsum(600 + 1400 * x / 0.18) / SR) * np.sin(np.pi * x / 0.18) ** 2, t0 - 0.05, 0.07, 0.4)

# 11. 15,3 : sonnerie (2 notes, mélodie originale) + vibration du téléphone ; 15,6-17,4 : glouglou d'écoulement
def ring(t0, reps):
    for r in range(reps):
        for j, f in enumerate((1046.5, 1318.5)):
            put(bell(f, 0.5, 9, ((1, 1), (3, .25), (5, .08))), t0 + r * 0.46 + j * 0.16, 0.10 * (1 - r * 0.12), 0.0)
ring(15.32, 5)
d = 2.2; x = ax(d); vib = np.sign(np.sin(2 * np.pi * 150 * x)) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 2.2 * x)))
put(lp(vib, 600) * 0.06 * np.clip((d - x) / 0.3, 0, 1), 15.32)
for i in range(30):
    t0 = 15.6 + 1.8 * (i / 30) + R.uniform(-0.03, 0.03); x = ax(0.09); f0 = 900 - 450 * (i / 30) + R.uniform(-80, 80)
    put(np.sin(2 * np.pi * np.cumsum(f0 * (1 - 1.2 * x)) / SR) * np.exp(-x * 45) * np.clip(x / 0.004, 0, 1), t0, 0.07, R.uniform(-0.3, 0.3))
x = ax(1.8); put(lp(R.standard_normal(len(x)), 500) * np.sin(np.pi * x / 1.8) * 0.05, 15.6)

# 12. Aube : un oiseau lointain (18,6) ; 7 gouttes à intervalles réguliers (18,45 → 19,05) ; retombée 20,45
for k, t0 in enumerate((18.6, 18.72)):
    x = ax(0.12); f = 3800 + 1200 * np.sin(np.pi * x / 0.12) - 600 * k
    put(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * x / 0.12) ** 2, t0, 0.035, 0.6)
for i in range(7):
    put(bell(1567.98 * 2 ** (i / 12 * 2), 0.6, 9), 18.45 + i * 0.1, 0.05, -0.6 + i * 0.2)
for i in range(7):
    x = ax(0.05); put(np.sin(2 * np.pi * np.cumsum(1200 - 6000 * x) / SR) * np.exp(-x * 70), 20.62 + i * 0.03, 0.04, 0.1)

# 13. Marque-page : tracé lumineux (20,78-21,15) puis pop feutré au clip (21,33)
d = 0.37; x = ax(d); put(np.sin(2 * np.pi * np.cumsum(900 + 1800 * x / d) / SR) * np.sin(np.pi * x / d) * 0.04 + hp(R.standard_normal(len(x)), 4000) * np.sin(np.pi * x / d) * 0.03, 20.78)
x = ax(0.15); put(np.sin(2 * np.pi * (300 + 500 * np.exp(-x * 60)) * x) * np.exp(-x * 30) * 0.4, 21.33, 1.0, 0.25)

# 14. 23,0 : sonnerie courte (mêmes 2 notes, une fois) ; pulsations SNOOZE ; 23,6 : bascule de la pastille ; 23,9 : signature
ring(23.0, 1)
for t0 in (23.25, 23.85, 24.45):
    x = ax(0.2); put(np.sin(2 * np.pi * 90 * x) * np.exp(-x * 18), t0, 0.25)
for t0 in (23.6, 23.73):
    x = ax(0.04); put(bp(R.standard_normal(len(x)), 1200, 5000) * np.exp(-x * 150), t0, 0.3, 0.1)
for k in range(10):
    put(tone(2093 * 2 ** (k / 12 * 1.2), 0.7, 5), 23.9 + k * 0.045, 0.022, (k / 5) - 1)

# Mix : silence total 15,0-15,3 ; réverbération courte ; normalisation ≈ -15 LUFS (RMS -17,4 dBFS), pic -1,5 dBFS
gate = 1 - win(15.0, 15.3, 0.015, 0.01)
mixL, mixR = L.copy(), Rt.copy()
for dl, g in ((0.031, .20), (0.047, .16), (0.071, .12), (0.109, .08), (0.163, .05), (0.24, .03)):
    k = int(dl * SR); mixL[k:] += Rt[:-k] * g; mixR[k:] += L[:-k] * g
out = np.stack([mixL * gate, mixR * gate], 1)
out *= np.clip(T / 0.003, 0, 1)[:, None] * np.clip((DUR - T) / 0.003, 0, 1)[:, None]


def limit(x, ceil):
    pkv = maximum_filter1d(np.max(np.abs(x), 1), int(0.006 * SR))
    gr = np.minimum(1.0, ceil / np.maximum(pkv, 1e-9))
    gr = np.minimum(gr, uniform_filter1d(gr, int(0.004 * SR)))
    gr = uniform_filter1d(gr, int(0.003 * SR))
    return x * gr[:, None]


target_rms = float(sys.argv[2]) if len(sys.argv) > 2 else -17.4
ceil = 10 ** (-1.5 / 20)
for _ in range(8):
    rms = np.sqrt(np.mean(out ** 2)); out *= 10 ** (target_rms / 20) / rms
    out = limit(out, ceil * 0.97)
out = np.clip(out, -ceil, ceil) * gate[:, None]
print(f"pic {20*np.log10(np.max(np.abs(out))):.2f} dBFS, RMS {20*np.log10(np.sqrt(np.mean(out**2))):.2f} dBFS")
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
