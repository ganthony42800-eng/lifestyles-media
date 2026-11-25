#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 13 : un éclair ne frappe jamais deux fois au même endroit ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav
Temps calés sur index.html : pluie continue · tonnerres aux frappes (1,0 · 2,55 · 23 frappes 4,6-8,2 en petits clics · 9,25 · 10,35 · 11,3 · 12,95 · 14,3 · 15,7 · 16,9 · 18,35 · 20,0)
2,6 tampon MYTHE · 13,3 alerte (zone de danger) · 15,5 intérieur (note chaude) · 19,4 bouton · 21,25 final."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1313)
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
# pluie (plus forte 15,2-18)
rainenv = 0.6 + 0.5*sm((T-15.2)/0.6)*(1-sm((T-17.6)/0.6))
rain = bp(R.standard_normal(N), 1500, 9000) * rainenv
L += rain*0.035; Rt += np.roll(rain, 2000)*0.035
# nappe grave (ré mineur → ré majeur au final)
env = 0.35 + 0.4*sm((T-4.45)/1.0)*(1-sm((T-8.3)/0.6)) + 0.5*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(73.42, 1.0), (146.83, 0.6), (174.61, 0.45), (220.0, 0.4), (293.66, 0.2)]:
    for det in (-0.4, 0.4): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 900)*env*0.03
L += pad; Rt += np.roll(pad, 400)
# tonnerres
for t0, near in [(1.0, 1.0), (2.55, 1.0), (9.25, 0.6), (10.35, 0.6), (11.3, 0.5), (12.95, 1.0), (14.3, 0.7), (15.7, 0.3), (16.9, 0.3), (18.35, 0.8), (20.0, 0.6)]:
    put(thunder(3.4, near), t0, 0.22*near + 0.06, R.uniform(-0.3, 0.3))
# compteur : 23 petits clics électriques montants
for k in range(23):
    t0 = 4.62 + 3.55*(k/22)**0.85; x = ax(0.09)
    put(hp(R.standard_normal(len(x)), 3000)*np.exp(-x*60)*0.6 + np.sin(2*np.pi*(600+40*k)*x)*np.exp(-x*40)*0.5, t0, 0.10, (-1)**k*0.3)
put(bell(587.33, 1.6, 2.5), 8.2, 0.07)
# 2,6 : tampon
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
# haut / pointu / isolé : trois notes
for k, f in enumerate([440.0, 554.37, 659.25]): put(bell(f, 1.2, 3), 9.0+k*0.5, 0.06, -0.4+0.4*k)
# zone de danger : double bip grave
for t0 in (13.3, 13.55): put(bell(196.0, 0.6, 6), t0, 0.08)
# intérieur : note chaude
put(bell(293.66, 2.4, 1.4), 15.5, 0.07); put(bell(369.99, 2.0, 1.6), 16.1, 0.05)
# question finale ; bouton
put(bell(293.66, 1.8, 2), 17.95, 0.07); put(bell(440.0, 1.8, 2), 18.5, 0.06)
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
