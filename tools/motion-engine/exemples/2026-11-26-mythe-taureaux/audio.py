#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 15 : le rouge rend les taureaux furieux ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1515)
L = np.zeros(N); Rt = np.zeros(N)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def sm(x): x = np.clip(x, 0, 1); return x * x * (3 - 2 * x)
def ax(d): return np.arange(int(d * SR)) / SR
def put(sig, t0, g=1.0, pan=0.0):
    i = int(round(t0 * SR))
    if i >= N: return
    s = sig * g; s = s[:N - i]
    L[i:i + len(s)] += s * (1 - max(pan, 0)); Rt[i:i + len(s)] += s * (1 + min(pan, 0))
def bell(f, d=1.6, dec=3.0):
    x = ax(d)
    s = np.sin(2*np.pi*f*x) + 0.35*np.sin(2*np.pi*f*2.76*x)*np.exp(-x*4) + 0.15*np.sin(2*np.pi*f*5.4*x)*np.exp(-x*9)
    return s * np.exp(-x*dec) * np.clip(x/0.003, 0, 1)
def thunder(d=3.2, near=1.0):
    x = ax(d); n = R.standard_normal(len(x))
    crack = hp(n, 1500) * np.exp(-x*30) * near
    rumble = lp(n, 140 + 200*near) * (np.exp(-x*1.3) * (1 + 0.6*np.sin(2*np.pi*3.1*x + R.random()*6)))
    return crack*0.9 + rumble*2.2

# rumeur de l'arène (foule lointaine filtrée)
cenv = 0.6 + 0.2*np.sin(2*np.pi*0.07*T) + 0.6*sm((T-14.7)/0.3)*(1-sm((T-17.0)/0.6))
crowd = bp(R.standard_normal(N), 300, 1800) * cenv
L += crowd*0.022; Rt += np.roll(crowd, 5000)*0.022
# nappe (ré mineur -> ré majeur au final)
env = 0.35 + 0.35*sm((T-4.45)/1.0) + 0.4*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(73.42, 1.0), (110.0, 0.55), (146.83, 0.45), (174.61, 0.3)]:
    for det in (-0.4, 0.4): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 900)*env*0.035
L += pad; Rt += np.roll(pad, 400)
def hoof(g=0.16, pan=0.0, t0=0.0):
    x = ax(0.16); put(lp(R.standard_normal(len(x)), 320)*np.exp(-x*32)*1.2 + np.sin(2*np.pi*62*x)*np.exp(-x*24), t0, g, pan)
def whoosh(t0, d=0.5, g=0.06, pan=0.0):
    x = ax(d); put(bp(R.standard_normal(len(x)), 500, 3000)*np.sin(np.pi*x/d)**2, t0, g, pan)
# 0-4,4 : sabot qui gratte + souffle du taureau + muleta
for k in range(14):
    x = ax(0.22); put(bp(R.standard_normal(len(x)), 900, 4500)*np.exp(-x*14), 0.2+k/3.2, 0.05, -0.2)
for t0 in (0.6, 2.0, 3.5):
    x = ax(0.7); put(lp(R.standard_normal(len(x)), 700)*np.sin(np.pi*x/0.7)**2, t0, 0.10)
for t0 in (0.4, 1.3, 2.2, 3.1, 4.0): whoosh(t0, 0.45, 0.04, 0.4)
# 2,6 : tampon
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
# vue partagée : balayage + note
x = ax(0.9); put(np.sin(2*np.pi*(300+500*x/0.9)*x)*np.exp(-x*2.5), 5.0, 0.05)
put(bell(587.33, 1.6, 2.2), 4.45, 0.06); put(bell(440.0, 1.8, 2.0), 5.8, 0.05)
# capote : charge 9,0-10,6
for k in range(int(1.6*4.5)): hoof(0.17, 0.25*(-1)**k, 9.0+k/4.5)
whoosh(9.8, 0.8, 0.10, 0.3)
put(bell(349.23, 1.4, 2.4), 8.45, 0.05)
# drapeaux : immobiles (silence relatif) puis agités + charge 15,0-16,7
put(bell(293.66, 1.4, 2.4), 12.45, 0.05)
for k in range(6): whoosh(14.7+k*0.5, 0.45, 0.05, 0.3*(-1)**k)
for k in range(int(1.7*4.5)): hoof(0.18, 0.25*(-1)**k, 15.0+k/4.5)
for k in range(8): put(bell(293.66*2**(k/12), 0.25, 14), 15.0+k*0.15, 0.03)
# pourquoi rouge
put(bell(220.0, 1.8, 2), 17.95, 0.07); put(bell(329.63, 1.8, 2), 18.5, 0.06)
whoosh(18.2, 0.9, 0.05)
y = ax(0.12); put(np.sin(2*np.pi*(700+500*y/0.12)*y)*np.exp(-y*30), 19.4, 0.10)
# fin
for f in (293.66, 369.99, 440.0, 587.33): put(bell(f, 2.6, 1.2), 21.25, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(900+600*y/0.12)*y)*np.exp(-y*30), 21.6, 0.12)
mx = np.stack([L, Rt], 1); mx = mx/(np.max(np.abs(mx))+1e-9)*0.89
fade = np.ones(N); fade[:int(0.02*SR)] = np.linspace(0, 1, int(0.02*SR)); fade[-int(0.03*SR):] = np.linspace(1, 0, int(0.03*SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mx, -1, 1)*32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20*np.log10(np.sqrt(np.mean(mx**2))+1e-9), 1))
