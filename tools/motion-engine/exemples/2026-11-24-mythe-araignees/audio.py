#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 10 : on avale des araignées en dormant ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav
Temps calés sur index.html :
 0-2,55 nappe sombre + grésillement de la calotte « 10 % » · 2,6 tampon MYTHE (impact + flash)
 4,55-7,1 sept zones s'allument = sept notes cristallines montantes · 8,75-12 lésion : bourdon désaccordé, crépitements
 12-15,6 flux d'énergie : souffle montant + pulsation · 13,15 « ≈ 20 % » accent grave
 15,7-18,2 neurones épars = petits pings aléatoires dans l'espace stéréo · 18,3-21,75 craquements de vieux disque (1936) · 20,0 bouton « Envoie »
 21,9 accord final · 22,25 bouton · 22,4 scintillement de la signature · 24,4-25 retour de la nappe (raccord avec 0 s)."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt

SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1010)
L = np.zeros(N); Rt = np.zeros(N)


def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def sm(x): x = np.clip(x, 0, 1); return x * x * (3 - 2 * x)
def ax(d): return np.arange(int(d * SR)) / SR


def put(sig, t0, g=1.0, pan=0.0):
    i = int(round(t0 * SR))
    if i >= N: return
    s = sig * g
    if i < 0: s = s[-i:]; i = 0
    s = s[:N - i]
    L[i:i + len(s)] += s * (1 - max(pan, 0)); Rt[i:i + len(s)] += s * (1 + min(pan, 0))


def bell(f, d=1.6, dec=3.0):
    x = ax(d)
    s = np.sin(2 * np.pi * f * x) + 0.35 * np.sin(2 * np.pi * f * 2.76 * x) * np.exp(-x * 4) + 0.15 * np.sin(2 * np.pi * f * 5.4 * x) * np.exp(-x * 9)
    return s * np.exp(-x * dec) * np.clip(x / 0.003, 0, 1)


# --- nappe sombre (la mineur), trou après le tampon, tension pendant les vibrations
env = np.ones(N) * 0.5
env *= 1 - 0.55 * sm((T - 2.55) / 0.1) * (1 - sm((T - 3.6) / 1.0))
env += 0.25 * sm((T - 8.5) / 1.0) * (1 - sm((T - 12.2) / 0.4))
env *= 1 - 0.4 * sm((T - 17.9) / 0.3) * (1 - sm((T - 21.2) / 0.4))
env += 0.3 * sm((T - 21.25) / 0.3) * (1 - sm((T - 23.6) / 0.4))
pad = np.zeros(N)
for f, a in [(55.0, 1.0), (110.0, 0.6), (130.81, 0.45), (164.81, 0.35), (220.0, 0.22), (246.94, 0.12)]:
    for det in (-0.5, 0.5):
        pad += a * np.sin(2 * np.pi * (f + det) * T + R.random() * 6.28)
pad = lp(pad, 850) * env * 0.035
L += pad; Rt += np.roll(pad, 300)

# --- frémissement de soie (cordes pincées très aiguës, aléatoires) 0-2,5 et 4,5-8,4
for k in range(40):
    t0 = R.random() * 8.4
    if 2.5 < t0 < 4.5: continue
    put(bell(R.choice([1760.0, 2093.0, 2349.3, 2637.0]), 0.5, 11), t0, 0.022, R.uniform(-0.8, 0.8))
# glissement de la descente (début) + retour de boucle
x = ax(2.2); put(bp(R.standard_normal(len(x)), 2500, 7000) * sm(x / 0.5) * sm((2.2 - x) / 0.8), 0.0, 0.035, 0.3)

# --- montée puis tampon MYTHE
x = ax(1.2); put(hp(R.standard_normal(len(x)), 600) * sm(x / 1.2) ** 2 * 0.5, 1.4, 0.06)
x = ax(1.4); hit = np.sin(2 * np.pi * (55 + 90 * np.exp(-x * 18)) * x) * np.exp(-x * 4.5) + 0.6 * lp(R.standard_normal(len(x)), 2500) * np.exp(-x * 22)
put(hit, 2.6, 0.55)
put(bell(1318.5, 0.8, 5.0), 3.05, 0.05)

# --- « le monde = vibrations » : ondes douces (sinus graves modulés)
x = ax(3.8); put(np.sin(2 * np.pi * 98 * x) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.38 * x)) * sm(x / 0.6) * sm((3.8 - x) / 0.5), 4.6, 0.06)

# --- dormeur : cœur (8,7), souffle (9,4), ronflement (10,1), sursaut (10,75), fuite
for k in range(int((14.9 - 8.7) / 1.05) + 1):
    t0 = 8.7 + k * 1.05; g = 0.25 * min(1, (t0 - 8.6) / 0.5)
    for dt, gg in ((0, 1.0), (0.22, 0.7)):
        y = ax(0.3); put(lp(np.sin(2 * np.pi * 48 * y) * np.exp(-y * 16), 300), t0 + dt, g * gg)
for k in range(3):
    x = ax(2.4); br = bp(R.standard_normal(len(x)), 300, 1600) * np.sin(np.pi * x / 2.4) ** 2
    put(br, 9.4 + k * 2.6, 0.05, -0.2)
x = ax(1.6)
sn = bp(R.standard_normal(len(x)), 80, 600) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 38 * x))) * np.sin(np.pi * x / 1.6) ** 1.5
put(lp(sn, 700), 10.1, 0.10, 0.2)
x = ax(0.5); put(np.sin(2 * np.pi * (1200 - 900 * x / 0.5) * x) * np.exp(-x * 9) + 0.5 * hp(R.standard_normal(len(x)), 3000) * np.exp(-x * 25), 10.75, 0.14)
x = ax(1.3); put(bp(R.standard_normal(len(x)), 1500, 6000) * sm(x / 0.2) * np.exp(-x * 2.2) * (0.5 + 0.5 * np.sin(2 * np.pi * (6 + 20 * x) * x)), 10.9, 0.07, -0.3)

# --- rocher : coup sourd ; « aucune proie » ping
y = ax(1.6); put(np.sin(2 * np.pi * 41.2 * y) * np.exp(-y * 3) + 0.3 * lp(R.standard_normal(len(y)), 400) * np.exp(-y * 8), 12.45, 0.22)
put(bell(880.0, 1.0, 4.0), 14.25, 0.05, 0.3)
# --- hasard : deux notes suspendues
put(bell(659.3, 1.4, 3.0), 15.25, 0.05, -0.4); put(bell(987.8, 1.4, 3.0), 15.75, 0.05, 0.4)
put(bell(440.0, 1.6, 2.5), 16.25, 0.05)

# --- 1993 : grésillement de modem / numérique + glitchs
d = 3.2; y = ax(d)
dig = np.sign(np.sin(2 * np.pi * (1100 + 700 * np.sign(np.sin(2 * np.pi * 9 * y))) * y)) * 0.15 + bp(R.standard_normal(len(y)), 1200, 5000) * 0.25
put(lp(dig, 6000) * sm(y / 0.1) * sm((d - y) / 0.3) * (R.random(len(y)) > 0.0), 17.95, 0.035)
for k in range(8):
    t0 = 17.95 + k * 0.07; z = ax(0.04); put(hp(R.standard_normal(len(z)), 2500) * np.exp(-z * 60), t0, 0.12, R.uniform(-0.6, 0.6))
y = ax(0.12); put(np.sin(2 * np.pi * (700 + 500 * y / 0.12) * y) * np.exp(-y * 30), 19.4, 0.10)

# --- fin : accord, bouton, scintillement
for f in (220.0, 329.63, 440.0, 659.3):
    put(bell(f, 2.6, 1.2), 21.25, 0.06)
y = ax(0.12); put(np.sin(2 * np.pi * (900 + 600 * y / 0.12) * y) * np.exp(-y * 30), 21.6, 0.12)
for k in range(10):
    put(bell(2637 + 220 * k, 0.4, 10), 21.8 + k * 0.05, 0.02, -0.5 + 0.1 * k)
# --- master
mx = np.stack([L, Rt], 1)
mx = mx / (np.max(np.abs(mx)) + 1e-9) * 0.89           # pic ≈ −3,1 dBFS
fade = np.ones(N); fade[:int(0.02 * SR)] = np.linspace(0, 1, int(0.02 * SR)); fade[-int(0.03 * SR):] = np.linspace(1, 0, int(0.03 * SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mx, -1, 1) * 32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20 * np.log10(np.sqrt(np.mean(mx ** 2)) + 1e-9), 1))
