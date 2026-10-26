#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 5 : cheveux mouillés dehors = rhume ? ». Synthèse procédurale, graine fixe.
Usage : python3 audio.py sortie.wav [rms_cible_dBFS]
Durée 25,25 s (le flux vidéo de 25,0 s fixe la fin). Temps calés sur index.html :
 rue de nuit (rumeur de ville, vent froid, voiture lointaine) + nappe Ré mineur 9 qui respire
 · gouttes « plic » au bout des mèches (0,6 · 1,5 détachement) · 2,55-3,0 plongée (souffle qui monte) · 3,0 plouf étouffé
 · 3,0-8,0 dans la goutte : son « sous l'eau » (passe-bas) · 3,35 le virus apparaît (scintillement) · 5,5 givre qui crépite
 · 6,9 et 7,5 deux pulsations identiques (même son dans les 2 gouttes) · 8,0 sortie
 · 8,0-9,6 condensation : 180 micro-gouttes · SILENCE 10,25-10,45 avant « Mais… »
 · 11,05-12,2 : 13 tics graves (coral) · 13,35-14,0 : 5 tics · 15,4 givre · 16,2 le virus se réveille (montée)
 · 17,85 tampon du verdict · 21,5 scintillement de la signature · 24,4 retour de l'ambiance du début."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 25.25; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2710)
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


def plic(t0, f=1400, g=0.12, pan=0.0):
    x = ax(0.18); fr = f * (1 + 1.6 * np.exp(-x * 60))
    put(np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-x * 30) * np.clip(x / 0.002, 0, 1), t0, g, pan)


street = win(-1, 3.0, 0.1, 0.05) + win(8.0, 15.4, 0.05, 0.05) * 0.55 + win(17.8, 26, 0.05, 0.1)
inside = win(3.0, 8.0, 0.05, 0.05) + win(15.4, 17.8, 0.05, 0.05)
# 1. Rumeur de ville + vent froid
city = lp(R.standard_normal(N), 180) * 0.6 + bp(R.standard_normal(N), 300, 1200) * 0.25
city *= (0.75 + 0.25 * np.sin(2 * np.pi * T * 0.13)) * 0.05
wind = bp(R.standard_normal(N), 500, 3000) * (0.5 + 0.5 * np.sin(2 * np.pi * T * 0.21 + 1)) * 0.018
L += (city + wind) * street; Rt += (np.roll(city, 557) + np.roll(wind, 991)) * street
# voiture lointaine qui passe (8,6 → 11)
car = lp(R.standard_normal(N), 400) * win(8.4, 11.2, 1.2, 1.2) * 0.04
L += car * np.clip(1 - (T - 8.4) / 2.8, 0, 1); Rt += car * np.clip((T - 8.4) / 2.8, 0, 1)
# 2. Nappe Ré mineur 9 (D, F, A, E) : chaude dans la rue, étouffée dans la goutte
pad = np.zeros(N)
for f, g in ((73.42, .5), (146.83, .35), (174.61, .25), (220.0, .25), (329.63, .14), (440.0, .06)):
    pad += g * np.sin(2 * np.pi * f * T + R.random() * 6) * (0.8 + 0.2 * np.sin(2 * np.pi * T * (0.11 + f / 4000)))
pad = lp(pad, 1500) * 0.06 * (0.8 + 0.4 * win(17.8, 24.4, 0.5, 0.3))
L += pad; Rt += np.roll(pad, 300)
# 3. Dans la goutte : grondement sous-marin + bulles
under = lp(R.standard_normal(N), 140) * 0.09 * inside
L += under; Rt += np.roll(under, 211)
for k in range(26):
    tb = 3.2 + R.random() * 4.6 if k < 18 else 15.5 + R.random() * 2.2
    plic(tb, 500 + R.random() * 700, 0.025, R.random() * 2 - 1)
# 4. Gouttes au bout des mèches
plic(0.62, 1700, 0.05, 0.4); plic(1.5, 1250, 0.14, 0.45); plic(19.9, 1300, 0.10, 0.45); plic(24.75, 1700, 0.04, 0.4)
# 5. Plongée (2,55 → 3,0) : souffle qui monte, plouf étouffé à 3,0
x = ax(0.5); put(bp(R.standard_normal(len(x)), 300, 4000) * (x / 0.5) ** 2, 2.5, 0.22)
x = ax(0.9); put(np.sin(2 * np.pi * (55 + 90 * np.exp(-x * 9)) * x) * np.exp(-x * 5) + 0.6 * lp(R.standard_normal(len(x)), 600) * np.exp(-x * 9), 3.0, 0.45)
# 6. Apparition du virus (3,35) : scintillement corail
for kk in range(8):
    put(tone(1046.5 * 2 ** (kk * 2 / 12), 0.6, 6), 3.35 + kk * 0.035, 0.03, (kk / 4) - 1)
# givre qui crépite (5,5 → 6,4) et (15,4 → 16,2)
for (a, b) in ((5.5, 6.4), (15.4, 16.2)):
    for k in range(40):
        t0 = a + R.random() * (b - a); x = ax(0.02)
        put(hp(R.standard_normal(len(x)), 4000) * np.exp(-x * 300), t0, 0.06 * R.random(), R.random() * 2 - 1)
# arrivée de la 2e goutte (5,4 → 6,2) : glissé
x = ax(0.8); put(bp(R.standard_normal(len(x)), 800, 3000) * np.sin(np.pi * x / 0.8), 5.4, 0.05, 0.6)
# 2 pulsations identiques (6,9 et 7,5), mêmes à gauche et à droite
for tp in (6.9, 7.5):
    put(tone(98, 0.5, 9) + 0.5 * tone(196, 0.5, 12), tp - 0.04, 0.35, -0.5)
    put(tone(98, 0.5, 9) + 0.5 * tone(196, 0.5, 12), tp - 0.04, 0.35, 0.5)
# 7. Sorties (8,0 et 15,4 et 17,8) : souffle inverse
for tt in (8.0, 15.4, 17.8):
    x = ax(0.35); put(bp(R.standard_normal(len(x)), 400, 5000) * np.exp(-x * 10), tt, 0.12)
# 8. Condensation des 180 gouttes (8,0 → 9,8)
for k in range(60):
    plic(8.05 + 1.6 * R.random(), 2000 + R.random() * 1600, 0.012, R.random() * 2 - 1)
# 9. Tics : 13 (gauche) puis 5 (droite)
for k in range(13):
    put(tone(392 if k % 2 == 0 else 349.2, 0.25, 18) + 0.4 * tone(784, 0.25, 25), 11.05 + k * 0.095, 0.13, -0.45)
for k in range(5):
    put(tone(392, 0.3, 14) + 0.4 * tone(784, 0.3, 22), 13.35 + k * 0.16, 0.13, 0.45)
# 10. Le virus se réveille (16,0 → 16,4) : montée + impact doux
x = ax(0.45); put(np.sin(2 * np.pi * np.cumsum(120 + 500 * (x / 0.45) ** 2) / SR) * (x / 0.45), 15.9, 0.06)
x = ax(0.8); put(np.sin(2 * np.pi * (65 + 40 * np.exp(-x * 20)) * x) * np.exp(-x * 6), 16.3, 0.35)
# 11. Tampon du verdict
x = ax(0.6); put(np.sin(2 * np.pi * (48 + 50 * np.exp(-x * 35)) * x) * np.exp(-x * 8) + 0.5 * lp(R.standard_normal(len(x)), 1200) * np.exp(-x * 28), 17.85, 0.55)
# 12. Signature : scintillement doré
for kk in range(10):
    put(tone(1975.5 * 2 ** (kk / 12 * 1.2), 0.7, 5), 21.5 + kk * 0.05, 0.018, (kk / 5) - 1)
put(sum(g * tone(1318.5 * k, 2.0, 2.6 * (1 + 0.4 * i)) for i, (k, g) in enumerate(((1, 1), (2, .25), (3, .08)))), 21.8, 0.09, 0.0)
# bouton « Abonne-toi » (21,8) : petit clic
put(tone(1568, 0.08, 60), 21.82, 0.06)

# Mixage : passe-bas « sous l'eau » dans la goutte, silence avant « Mais… », réverbération courte
mixL, mixR = L.copy(), Rt.copy()
lpL, lpR = lp(mixL, 700), lp(mixR, 700)
mixL = mixL * (1 - 0.8 * inside) + lpL * 0.8 * inside; mixR = mixR * (1 - 0.8 * inside) + lpR * 0.8 * inside
for dl, g in ((0.031, .18), (0.047, .14), (0.071, .11), (0.109, .07), (0.163, .045), (0.24, .03)):
    k = int(dl * SR); mixL[k:] += mixR[:-k] * g; mixR[k:] += mixL[:-k] * g
gate = 1 - win(10.25, 10.45, 0.03, 0.005) * 0.985
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
