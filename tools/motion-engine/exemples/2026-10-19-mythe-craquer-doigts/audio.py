#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 2 : craquer ses doigts ». Synthèse procédurale, seed fixe, 25,5 s.
Usage : python3 audio.py sortie.wav
Calé sur index.html : tension 0,85-1,48 · 80 ms de silence · CRAC 1,5 (+ sub 55 Hz) · nappe violette dès 1,0
· whoosh 2,6 + tic-tac 2,6-15,4 · ticks cristallins 4,42-4,9 (215 radios) + balayage 5,0-5,95 · montée + ding 8,0
· montée + ding aigu 10,0 · silence 11,25-11,45 puis pop grave 11,45 (cavité) · silence 13,2-13,5, clac du cadenas 13,62
· compression grave 15,3 (le tic-tac s'arrête) · double tampon 17,86 / 18,0 · nappe 18,8 · CRAC rappel 20,8 + swoosh
· taps 21,64 / 22,2 · souffle froid 22,9 + pop 23,99 · whip 24,65 · tension 25,0-25,5 coupée net, SANS crac (boucle)."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 25.5; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1910)
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


# --- le crac de doigt : 3 micro-claquements serrés + résonance osseuse + sub
def crack(g=1.0, sub=True):
    x = ax(0.5); out = np.zeros(len(x))
    for k, (dt, a) in enumerate(((0.0, 1.0), (0.0042, 0.7), (0.0105, 0.45))):
        i = int(dt * SR); n = int(0.012 * SR)
        e = R.standard_normal(n) * np.exp(-np.arange(n) / SR * 900) * a
        out[i:i + n] += e
    body = bp(out, 900, 4200, 2) * 1.6 + hp(out, 3500) * 0.7
    body += np.sin(2 * np.pi * 1450 * x) * np.exp(-x * 160) * 0.35 + np.sin(2 * np.pi * 620 * x) * np.exp(-x * 90) * 0.25
    if sub: body += np.sin(2 * np.pi * (55 + 30 * np.exp(-x * 30)) * x) * np.exp(-x * 9) * np.clip(x / 0.004, 0, 1) * 0.9
    return body * g


# --- tension : grincement tendu qui monte (filtre qui s'ouvre)
def tension(d, g=1.0):
    x = ax(d); k = x / d
    f = 140 + 260 * k ** 1.5
    creak = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * (0.5 + 0.5 * np.sin(2 * np.pi * 23 * x))
    out = np.zeros(len(x)); lo = lp(creak, 900)
    nz = R.standard_normal(len(x)); out += lo * 0.25 + (bp(nz, 300, 900) * (1 - k) + bp(nz, 1500, 4500) * k) * 0.5
    return out * k ** 1.6 * g


# 1. Tension 0,25 → 0,88 puis 80 ms de silence total, CRAC 0,9
put(tension(0.6, 0.35), 0.82)
put(crack(1.0), 1.5)
# 2. Nappe grave froide (violette), bascule chaude pendant la nuance (15,2-19,2)
pad_c = np.zeros(N); pad_w = np.zeros(N)
for f in (55.0, 82.41, 98.0, 123.47, 164.81):
    for det in (0.996, 1.004): pad_c += np.sin(2 * np.pi * f * det * T) + 0.3 * np.sign(np.sin(2 * np.pi * f * det * T))
for f in (65.41, 98.0, 130.81, 164.81, 196.0):
    for det in (0.996, 1.004): pad_w += np.sin(2 * np.pi * f * det * T) + 0.3 * np.sign(np.sin(2 * np.pi * f * det * T))
warm = win(15.25, 18.8, 0.4, 0.5)
pad = lp(pad_c, 380) * (1 - warm) + lp(pad_w, 700) * warm
pad_env = win(1.0, 25.5, 0.6, 0.01) * (0.55 + 0.45 * win(18.8, 20.8, 0.4, 0.3) + 0.2 * win(6.4, 10.8, 0.5, 0.3))
pad *= 0.010 * pad_env * (1 + 0.15 * np.sin(2 * np.pi * 0.25 * T))
L += pad; Rt += np.roll(pad, 600)
# 3. Whoosh 2,6 + tic-tac 2,6 → 15,4 (horloge de la poigne)
x = ax(0.55); put(bp(R.standard_normal(len(x)), 300, 5000) * np.sin(np.pi * x / 0.55) ** 2 * 0.35, 2.45)
def tick(f):
    x = ax(0.05); return bp(R.standard_normal(len(x)), f, f * 2.4) * np.exp(-x * 170) + 0.4 * np.sin(2 * np.pi * f * x) * np.exp(-x * 140)
k = 0; tt = 2.7
while tt < 15.4:
    if not (4.4 <= tt < 6.4) and not (13.2 <= tt < 13.5) and not (11.2 <= tt < 11.5):
        put(tick(2600 if k % 2 == 0 else 1900), tt, 0.16, 0.3 if k % 2 == 0 else -0.3)
    tt += 0.5; k += 1
# 4. 215 radios : ticks cristallins en cascade (arrivées) + balayage du scanner
Rr = np.random.default_rng(215)
for i in range(60):
    t0 = 4.42 + 0.45 * (i / 60) ** 0.8 + 0.02 * Rr.random()
    put(tone(3000 + 2200 * Rr.random(), 0.25, 30), t0, 0.035, Rr.uniform(-0.7, 0.7))
x = ax(0.95); put(np.sin(2 * np.pi * np.cumsum(5200 - 3000 * x / 0.95) / SR) * np.sin(np.pi * x / 0.95) ** 2 * 0.035, 5.0)
put(hp(R.standard_normal(len(x)), 4000) * np.sin(np.pi * x / 0.95) ** 2 * 0.06, 5.0, 1.0, 0.2)
# 5. Montées des jauges + dings (8,0 et 10,0, plus aigu)
for t0, t1, f0, f1, fd in ((7.0, 8.0, 220, 440, 1568.0), (9.0, 10.0, 247, 523, 2093.0)):
    d = t1 - t0; x = ax(d)
    put(np.sin(2 * np.pi * np.cumsum(f0 + (f1 - f0) * (x / d) ** 1.4) / SR) * (x / d) ** 1.2 * 0.07, t0)
    put(bp(R.standard_normal(len(x)), 500, 5000) * (x / d) ** 2 * 0.08, t0)
    for kk, g in ((1, 1), (2.76, .35), (5.4, .15)): put(tone(fd * kk, 1.6, 3.5), t1, 0.12 * g, 0.15)
# 6. Plongée 10,8 (souffle) · silence 11,25-11,45 · pop grave 11,45 (la cavité s'ouvre)
x = ax(0.5); put(bp(R.standard_normal(len(x)), 200, 2500) * np.sin(np.pi * x / 0.5) ** 2 * 0.3, 10.75)
x = ax(0.8)
pop = np.sin(2 * np.pi * (48 + 90 * np.exp(-x * 22)) * x) * np.exp(-x * 6) * np.clip(x / 0.003, 0, 1)
pop += lp(R.standard_normal(len(x)), 600) * np.exp(-x * 40) * 0.4
put(pop * 0.95, 11.45); put(crack(0.35, sub=False), 11.45)
# 7. Silence 13,2-13,5 puis clac du cadenas 13,62 (+ ressort)
x = ax(0.15)
clac = bp(R.standard_normal(len(x)), 1200, 6000) * np.exp(-x * 90) + 0.6 * np.sin(2 * np.pi * 900 * x) * np.exp(-x * 70)
put(clac * 0.55, 13.62); put(tone(1300, 0.4, 12) * np.sin(2 * np.pi * 30 * ax(0.4)), 13.66, 0.06)
# 8. Compression grave 15,3 (la poigne baisse) ; craquement mat 16,5
x = ax(1.6)
comp = np.sin(2 * np.pi * np.cumsum(90 * 0.5 ** (x / 1.6)) / SR) * np.sin(np.pi * x / 1.6) ** 0.6 * 0.4
comp += lp(R.standard_normal(len(x)), 200) * np.sin(np.pi * x / 1.6) * 0.3
put(comp, 15.3)
put(lp(crack(0.6, sub=False), 1400), 16.5)
# 9. Double tampon 17,95 / 18,45
def stamp():
    x = ax(0.5)
    return (np.sin(2 * np.pi * (70 + 60 * np.exp(-x * 30)) * x) * np.exp(-x * 9) + bp(R.standard_normal(len(x)), 150, 2500) * np.exp(-x * 28) * 0.8)
put(stamp() * 0.85, 17.86, 1.0, -0.15); put(stamp() * 0.85, 18.0, 1.0, 0.15)
# 10. CRAC rappel 21,2 (précédé de 100 ms de silence) + swoosh ; taps 22,04 / 22,6
put(crack(0.95), 20.8)
x = ax(0.7); put(bp(R.standard_normal(len(x)), 500, 6000) * np.sin(np.pi * x / 0.7) ** 2 * 0.3, 20.9, 1.0, -0.3)
for t0 in (21.64, 22.2):
    x = ax(0.3)
    put(np.sin(2 * np.pi * (180 + 200 * np.exp(-x * 40)) * x) * np.exp(-x * 18) * 0.5 + tone(1760, 0.3, 14) * 0.15, t0)
# 11. Souffle froid 23,3 (vent filtré) + pop d'abonnement 24,15 ; scintillement doré de la signature 23,3
x = ax(1.8); put(bp(R.standard_normal(len(x)), 1500, 7000) * np.sin(np.pi * x / 1.8) ** 1.2 * 0.18, 22.92, 1.0, 0.3)
x = ax(0.25); put(np.sin(2 * np.pi * np.cumsum(400 + 900 * x / 0.25) / SR) * np.exp(-x * 14) * 0.35, 23.99)
for kk in range(8): put(tone(2093 * 2 ** (kk / 12 * 1.5), 0.6, 6), 22.88 + kk * 0.05, 0.025, kk / 4 - 1)
# 12. Whip 24,7 puis tension 25,0 → 25,5 coupée net, sans crac (raccord avec la tension de l'image 0)
x = ax(0.3); put(bp(R.standard_normal(len(x)), 400, 6000) * np.sin(np.pi * x / 0.3) ** 2 * 0.3, 24.65)
put(tension(0.5, 0.35)[:int(0.5 * SR)], 25.0)

# Mix : silences (80 ms avant le crac, 11,25-11,45, 13,2-13,5, 100 ms avant le rappel)
gate = (1 - win(1.42, 1.5, 0.01, 0.002)) * (1 - win(11.25, 11.45, 0.03, 0.005)) * (1 - win(13.2, 13.5, 0.03, 0.01)) * (1 - win(20.7, 20.8, 0.01, 0.002))
mixL, mixR = L.copy(), Rt.copy()
for dl, g in ((0.031, .2), (0.047, .16), (0.071, .12), (0.109, .08), (0.163, .05)):
    k = int(dl * SR); mixL[k:] += Rt[:-k] * g; mixR[k:] += L[:-k] * g
out = np.stack([mixL * gate, mixR * gate], 1)
out *= np.clip(T / 0.004, 0, 1)[:, None]
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
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
