#!/usr/bin/env python3
"""Son original — « Teste ton cerveau : ce point va disparaître (angle mort) ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 22.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2711)
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
def squeak(t0, g=0.03, pan=0.3):
    x = ax(0.09); f = 3200 + 900*np.sin(np.pi*x/0.09)
    put(np.sin(2*np.pi*np.cumsum(f)/SR)*np.sin(np.pi*x/0.09)**2, t0, g, pan)
def whoosh(t0, d=0.5, g=0.06, pan=0.0):
    x = ax(d); put(bp(R.standard_normal(len(x)), 500, 3000)*np.sin(np.pi*x/d)**2, t0, g, pan)
def thud(t0, g=0.25):
    x = ax(0.5); put(np.sin(2*np.pi*(48+30*np.exp(-x*12))*x)*np.exp(-x*7) + 0.4*lp(R.standard_normal(len(x)), 200)*np.exp(-x*10), t0, g)
# nappe spatiale (ré mineur -> ré majeur au final), retenue pendant le test
env = 0.45 + 0.4*sm((T-10.3)/0.8) + 0.4*sm((T-19.2)/0.3)*(1-sm((T-21.4)/0.5))
env *= 1 - 0.55*sm((T-2.7)/0.3)*(1-sm((T-10.0)/0.3))
pad = np.zeros(N)
for f, a in [(73.42, 1.0), (110.0, 0.55), (146.83, 0.45), (174.61, 0.3)]:
    for det in (-0.35, 0.35): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 1000)*env*0.04
L += pad; Rt += np.roll(pad, 500)
air = lp(R.standard_normal(N), 900)*0.012; L += air; Rt += np.roll(air, 5000)
# accroche : souffle + impact grave + scintillement de l'iris qui glisse vers le point
whoosh(0.0, 0.6, 0.07)
x = ax(1.4); hit = np.sin(2*np.pi*(50+80*np.exp(-x*16))*x)*np.exp(-x*4.0) + 0.5*lp(R.standard_normal(len(x)), 2200)*np.exp(-x*20)
put(hit, 0.05, 0.45)
for k in range(6): put(bell(1318.5+k*90, 0.5, 9), 0.7+k*0.12, 0.02, 0.4)
# test : tic doux régulier, puis « pop » à la question
y = ax(0.06)
for k in range(14): put(np.sin(2*np.pi*2000*y)*np.exp(-y*90), 3.0+k*0.5, 0.025, -0.2 if k%2 else 0.2)
y = ax(0.15); put(np.sin(2*np.pi*(500+900*y/0.15)*y)*np.exp(-y*25), 7.7, 0.12)
# coupe de l'œil : souffle, rayons (scintillement), le disque s'allume
whoosh(10.2, 0.7, 0.07)
x = ax(4.5); put(bp(R.standard_normal(len(x)), 3000, 9000)*np.sin(np.pi*x/4.5)**2, 10.9, 0.025)
put(bell(587.33, 1.8, 2.0), 10.4, 0.06); put(bell(880.0, 1.8, 2.0), 12.6, 0.07); put(bell(659.25, 1.6, 2.2), 13.1, 0.05)
# le cerveau bouche le trou : montée douce
x = ax(1.8); f = 300 + 500*sm(x/1.8); put(np.sin(2*np.pi*np.cumsum(f)/SR)*np.sin(np.pi*x/1.8)**2, 16.5, 0.05)
put(bell(587.33, 1.8, 2), 15.65, 0.06)
# fin
for f in (293.66, 369.99, 440.0, 587.33): put(bell(f, 2.6, 1.2), 19.2, 0.06)
for t0 in (19.9, 20.4):
    y = ax(0.12); put(np.sin(2*np.pi*(900+600*y/0.12)*y)*np.exp(-y*30), t0, 0.11)
mx = np.stack([L, Rt], 1); mx = mx/(np.max(np.abs(mx))+1e-9)*0.89
fade = np.ones(N); fade[:int(0.02*SR)] = np.linspace(0, 1, int(0.02*SR)); fade[-int(0.03*SR):] = np.linspace(1, 0, int(0.03*SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mx, -1, 1)*32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20*np.log10(np.sqrt(np.mean(mx**2))+1e-9), 1))
