#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 3 : la chaleur par la tête ». Synthèse procédurale, seed fixe, 27 s.
Usage : python3 audio.py sortie.wav
Calé sur index.html : vent froid + givre qui craque 0,3-1,42 · 80 ms de silence · CRAC DE GLACE 1,5 (+ sub) · nappe froide
· whoosh 2,6 + tic-tac 2,6-17,6 (boucle ouverte « un cas ») · balayage 4,9-6,3 · froissement (emmitouflé) 6,9-8,1
· souffle chaud 8,0 · montées + dings 12,2 / 14,4 · glissando comique 15,7 · silence 17,6-17,85 puis clac du cadenas 17,9
· montée + ding aigu 19,3 · double tampon 20,05 / 20,45 · nappe chaude 21,3 · taps 23,75 / 24,25 · scintillement 24,85
· pop 25,7 · whip 26,3 · vent qui remonte, coupé net à 27,0 (boucle)."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 27.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2026)
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

# vent froid (lit continu, plus fort au début et à la fin)
wind = bp(R.standard_normal(N), 250, 2400, 2)
wenv = 0.05 + 0.04 * np.sin(2 * np.pi * 0.13 * T) ** 2
wenv *= 1 + 1.4 * win(0, 1.42, 0.05, 0.05) + 1.6 * win(26.4, 27.0, 0.4, 0.001)
wenv *= 1 - 0.7 * win(21.4, 26.3, 0.6, 0.3)
put(lp(wind, 1800) * wenv, 0.0, 0.9)

def ice_crack(g=1.0):
    x = ax(0.9); out = np.zeros(len(x))
    for dt, a in ((0, 1.0), (0.006, .8), (0.013, .6), (0.03, .45), (0.06, .3)):
        i = int(dt * SR); n = int(0.02 * SR)
        out[i:i + n] += R.standard_normal(n) * np.exp(-np.arange(n) / SR * 600) * a
    body = hp(out, 2500) * 1.2 + bp(out, 700, 3000) * 0.8
    for f, d in ((3100, 25), (4700, 30), (6200, 40), (2300, 18)): body += np.sin(2 * np.pi * f * x) * np.exp(-x * d) * 0.12
    body += np.sin(2 * np.pi * (48 + 40 * np.exp(-x * 25)) * x) * np.exp(-x * 7) * np.clip(x / 0.004, 0, 1) * 1.0
    return body * g
# givre qui grince avant le crac
x = ax(1.1); k = x / 1.1
creak = bp(R.standard_normal(len(x)), 1500, 6000) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * (18 + 40 * k) * x)))
put(creak * k ** 1.8 * 0.25, 0.32)
put(ice_crack(1.0), 1.5)
# nappes : froide puis chaude
pad_c = np.zeros(N); pad_w = np.zeros(N)
for f in (55.0, 82.41, 110.0, 146.83, 164.81):
    for det in (0.996, 1.004): pad_c += np.sin(2 * np.pi * f * det * T) + 0.25 * np.sign(np.sin(2 * np.pi * f * det * T))
for f in (65.41, 98.0, 130.81, 164.81, 196.0):
    for det in (0.996, 1.004): pad_w += np.sin(2 * np.pi * f * det * T) + 0.25 * np.sign(np.sin(2 * np.pi * f * det * T))
warm = np.clip(win(21.3, 27.0, 0.6, 0.6) + 0.6 * win(8.0, 11.2, 0.4, 0.4) + 0.5 * win(17.9, 21.2, 0.4, 0.4), 0, 1)
pad = lp(pad_c, 380) * (1 - warm) + lp(pad_w, 750) * warm
pad *= 0.011 * win(1.0, 27.0, 0.6, 0.01) * (1 + 0.15 * np.sin(2 * np.pi * 0.25 * T))
L += pad; Rt += np.roll(pad, 600)
# whoosh 2,6 + tic-tac
x = ax(0.55); put(bp(R.standard_normal(len(x)), 300, 5000) * np.sin(np.pi * x / 0.55) ** 2 * 0.35, 2.45)
def tick(f):
    x = ax(0.05); return bp(R.standard_normal(len(x)), f, f * 2.4) * np.exp(-x * 170) + 0.4 * np.sin(2 * np.pi * f * x) * np.exp(-x * 140)
kk = 0; tt = 2.7
while tt < 17.55:
    put(tick(2600 if kk % 2 == 0 else 1900), tt, 0.11, 0.3 if kk % 2 == 0 else -0.3); tt += 0.5; kk += 1
# balayage thermique 4,9-6,3
x = ax(1.4); put(np.sin(2 * np.pi * np.cumsum(4800 - 3200 * x / 1.4) / SR) * np.sin(np.pi * x / 1.4) ** 2 * 0.04, 4.9)
put(hp(R.standard_normal(len(x)), 3500) * np.sin(np.pi * x / 1.4) ** 2 * 0.05, 4.9, 1.0, 0.2)
# froissement de doudoune 6,9-8,1 (rafales de bruit filtré)
for i in range(9):
    x = ax(0.16); put(bp(R.standard_normal(len(x)), 900, 5000) * np.sin(np.pi * x / 0.16) * 0.16, 6.9 + i * 0.13 + 0.03 * R.random(), 1.0, R.uniform(-.5, .5))
# souffle chaud qui monte de la tête 8,0
x = ax(2.6); put(lp(R.standard_normal(len(x)), 900) * np.sin(np.pi * x / 2.6) ** 1.5 * 0.22, 8.0)
put(np.sin(2 * np.pi * np.cumsum(180 + 120 * x / 2.6) / SR) * np.sin(np.pi * x / 2.6) ** 2 * 0.05, 8.0)
# montées + dings (7 %, 10 %, 19 %)
for t0, t1, f0, f1, fd in ((11.45, 12.2, 220, 440, 1568.0), (13.65, 14.4, 247, 494, 1760.0), (18.65, 19.3, 262, 587, 2349.3)):
    d = t1 - t0; x = ax(d)
    put(np.sin(2 * np.pi * np.cumsum(f0 + (f1 - f0) * (x / d) ** 1.4) / SR) * (x / d) ** 1.2 * 0.07, t0)
    put(bp(R.standard_normal(len(x)), 500, 5000) * (x / d) ** 2 * 0.07, t0)
    for m, g in ((1, 1), (2.76, .35), (5.4, .15)): put(tone(fd * m, 1.6, 3.5), t1, 0.12 * g, 0.15)
# glissando comique « sans pantalon » 15,75
x = ax(0.55); put(np.sin(2 * np.pi * np.cumsum(900 * 0.35 ** (x / 0.55)) / SR) * np.exp(-x * 3) * 0.16, 15.75)
x = ax(0.18); put(np.sin(2 * np.pi * (300 + 500 * np.exp(-x * 30)) * x) * np.exp(-x * 20) * 0.25, 16.32)
# clac du cadenas 17,9
x = ax(0.15)
clac = bp(R.standard_normal(len(x)), 1200, 6000) * np.exp(-x * 90) + 0.6 * np.sin(2 * np.pi * 900 * x) * np.exp(-x * 70)
put(clac * 0.55, 17.9); put(tone(1300, 0.4, 12) * np.sin(2 * np.pi * 30 * ax(0.4)), 17.94, 0.06)
# double tampon
def stamp():
    x = ax(0.5)
    return (np.sin(2 * np.pi * (70 + 60 * np.exp(-x * 30)) * x) * np.exp(-x * 9) + bp(R.standard_normal(len(x)), 150, 2500) * np.exp(-x * 28) * 0.8)
put(stamp() * 0.85, 20.05, 1.0, -0.15); put(stamp() * 0.85, 20.45, 1.0, 0.15)
# « couvre tout » : fermeture éclair 21,35
x = ax(0.8); zz = np.sign(np.sin(2 * np.pi * np.cumsum(60 + 260 * x / 0.8) / SR)) * np.exp(-((x - 0.4) / 0.35) ** 2)
put(bp(zz + 0.3 * R.standard_normal(len(x)), 1500, 7000) * 0.16, 21.35)
# taps d'envoi
for t0 in (23.75, 24.25):
    x = ax(0.3); put(np.sin(2 * np.pi * (180 + 200 * np.exp(-x * 40)) * x) * np.exp(-x * 18) * 0.5 + tone(1760, 0.3, 14) * 0.15, t0)
# scintillement signature + pop abonnement
for m in range(8): put(tone(2093 * 2 ** (m / 12 * 1.5), 0.6, 6), 24.88 + m * 0.05, 0.025, m / 4 - 1)
x = ax(0.25); put(np.sin(2 * np.pi * np.cumsum(400 + 900 * x / 0.25) / SR) * np.exp(-x * 14) * 0.35, 25.62)
# whip 26,3
x = ax(0.3); put(bp(R.standard_normal(len(x)), 400, 6000) * np.sin(np.pi * x / 0.3) ** 2 * 0.3, 26.28)

gate = (1 - win(1.42, 1.5, 0.01, 0.002)) * (1 - win(17.6, 17.85, 0.03, 0.01))
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
for _ in range(6):
    rms = np.sqrt(np.mean(out ** 2)); out *= 10 ** (-17.0 / 20) / rms
    out = limit(out, target * 0.97)
out = np.clip(out, -target, target) * gate[:, None]
print(f"pic {20*np.log10(np.max(np.abs(out))):.2f} dBFS, RMS {20*np.log10(np.sqrt(np.mean(out**2))):.2f} dBFS")
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
