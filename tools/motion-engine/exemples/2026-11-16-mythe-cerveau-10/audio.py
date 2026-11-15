#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 9 : on n'utilise que 10 % de son cerveau ? ».
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

SR = 44100; DUR = 25.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(909)
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


# --- nappe (accord de ré mineur 9, très lent), suit la tension du récit
env = np.ones(N) * 0.5
env *= 1 - 0.55 * sm((T - 2.55) / 0.1) * (1 - sm((T - 3.6) / 1.0))       # trou après le tampon
env += 0.25 * sm((T - 12.0) / 1.5) * (1 - sm((T - 15.6) / 0.5))
env *= 1 - 0.5 * sm((T - 18.3) / 0.4) * (1 - sm((T - 21.8) / 0.4))
env += 0.3 * sm((T - 21.9) / 0.3) * (1 - sm((T - 24.2) / 0.6))
pad = np.zeros(N)
for f, a in [(73.42, 1.0), (110.0, 0.6), (146.83, 0.45), (174.61, 0.35), (220.0, 0.25), (329.63, 0.12)]:
    for det in (-0.6, 0.6):
        pad += a * np.sin(2 * np.pi * (f + det) * T + R.random() * 6.28)
pad = lp(pad, 900) * env * 0.035
L += pad; Rt += np.roll(pad, 300)

# --- grésillement électrique de la calotte (0-2,55 et retour 24,5-25)
cr = hp(R.standard_normal(N), 3000) * (R.random(N) > 0.996) * 0.9
crenv = (1 - sm((T - 2.5) / 0.1)) + sm((T - 24.5) / 0.4)
put(lp(cr * crenv, 9000), 0, 0.08, 0.2)

# --- montée vers le tampon puis impact
x = ax(1.2); put(hp(R.standard_normal(len(x)), 600) * sm(x / 1.2) ** 2 * 0.5, 1.4, 0.06)
x = ax(1.4); hit = np.sin(2 * np.pi * (55 + 90 * np.exp(-x * 18)) * x) * np.exp(-x * 4.5) + 0.6 * lp(R.standard_normal(len(x)), 2500) * np.exp(-x * 22)
put(hit, 2.6, 0.55)

# --- sept zones = sept notes montantes (pentatonique de ré)
notes = [587.3, 659.3, 880.0, 987.8, 1174.7, 1318.5, 1760.0]
for j, f in enumerate(notes):
    put(bell(f, 1.8, 2.6), 4.55 + j * 0.42, 0.075, -0.6 + 0.2 * j)

# --- lésion : bourdon désaccordé + crépitements
x = ax(3.3); buzz = (np.sign(np.sin(2 * np.pi * 61 * x)) * 0.5 + np.sin(2 * np.pi * 64.5 * x)) * sm(x / 0.25) * sm((3.3 - x) / 0.4)
put(lp(buzz, 700), 8.75, 0.07, 0.4)
for k in range(26):
    t0 = 8.8 + R.random() * 3.0; y = ax(0.03)
    put(hp(R.standard_normal(len(y)), 2000) * np.exp(-y * 120), t0, 0.12, R.uniform(-0.3, 0.9))

# --- flux d'énergie : souffle montant + pulsation cardiaque douce
x = ax(3.6); n = R.standard_normal(len(x)); sw = np.zeros(len(x))
for i0 in range(0, len(x), 2205):
    seg = n[i0:i0 + 2205]; fc = 300 + 2200 * (i0 / len(x)) ** 1.5
    sw[i0:i0 + len(seg)] = seg * 0 + seg
sw = bp(sw, 250, 2600) * sm(x / 1.0) * sm((3.6 - x) / 0.5)
put(sw, 12.0, 0.05)
for k in range(4):
    y = ax(0.35); put(np.sin(2 * np.pi * 52 * y) * np.exp(-y * 14), 12.3 + k * 0.85, 0.22)
y = ax(1.6); put(np.sin(2 * np.pi * 73.4 * y) * np.exp(-y * 2.2) + 0.4 * bell(880, 1.6, 2.0), 13.15, 0.18)

# --- neurones épars : pings brefs dans l'espace
for k in range(34):
    t0 = 15.75 + R.random() * 2.4; f = R.choice([1174.7, 1318.5, 1760.0, 1975.5, 2349.3])
    put(bell(f, 0.5, 9.0), t0, 0.035, R.uniform(-0.9, 0.9))

# --- 1936 : craquements de vieux disque + souffle
d = 3.45; y = ax(d)
vin = bp(R.standard_normal(len(y)), 900, 5000) * 0.25 + hp(R.standard_normal(len(y)), 1500) * (R.random(len(y)) > 0.9985) * 3
put(vin * sm(y / 0.15) * sm((d - y) / 0.25), 18.3, 0.06)
y = ax(0.12); put(np.sin(2 * np.pi * (700 + 500 * y / 0.12) * y) * np.exp(-y * 30), 20.0, 0.10)
put(bell(1318.5, 0.8, 5.0), 3.05, 0.05)
put(bell(1760.0, 0.8, 5.0), 6.55, 0.04)

# --- fin : accord, bouton, scintillement
for f in (293.7, 440.0, 587.3, 880.0):
    put(bell(f, 2.6, 1.2), 21.9, 0.06)
y = ax(0.12); put(np.sin(2 * np.pi * (900 + 600 * y / 0.12) * y) * np.exp(-y * 30), 22.25, 0.12)
for k in range(10):
    put(bell(2637 + 220 * k, 0.4, 10), 22.4 + k * 0.05, 0.02, -0.5 + 0.1 * k)

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
