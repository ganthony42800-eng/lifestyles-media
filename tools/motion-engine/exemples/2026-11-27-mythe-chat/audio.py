#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 18 : le chat retombe toujours sur ses pattes ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1818)
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
# ville de nuit : rumeur grave + vent en hauteur
city = lp(R.standard_normal(N), 180) * (0.7 + 0.2*np.sin(2*np.pi*0.07*T))
L += city*0.06; Rt += np.roll(city, 5000)*0.06
# nappe (ré mineur -> ré majeur au final)
env = 0.35 + 0.35*sm((T-4.45)/1.0) + 0.4*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(73.42, 1.0), (110.0, 0.55), (146.83, 0.45), (174.61, 0.3)]:
    for det in (-0.4, 0.4): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 900)*env*0.035
L += pad; Rt += np.roll(pad, 400)
# chute : souffle d'air qui monte, deux « swish » du retournement
x = ax(4.4); put(bp(R.standard_normal(len(x)), 300, 2500)*(0.3+0.7*x/4.4)*np.sin(np.pi*np.clip(x/4.4,0,1))**0.5, 0.0, 0.07)
whoosh(1.2, 0.6, 0.07, -0.4); whoosh(1.65, 0.6, 0.07, 0.4)
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
# ralenti : deux rotations opposées
put(bell(587.33, 1.6, 2.2), 4.45, 0.05)
whoosh(5.0, 1.4, 0.06, -0.5); whoosh(5.8, 1.4, 0.06, 0.5)
# oreille interne : pings cristallins
for k, f in enumerate((1174.66, 1396.91, 1760.0)): put(bell(f, 1.2, 3.5), 9.4+k*0.35, 0.035, (k-1)*0.4)
put(bell(880.0, 1.6, 2.5), 11.6, 0.03)
# table : glissade, chute courte, bruit sourd feutré, se relève
x = ax(0.8); put(bp(R.standard_normal(len(x)), 1500, 5000)*np.sin(np.pi*x/0.8)**2, 13.6, 0.03)
whoosh(14.4, 0.9, 0.05)
thud(15.35, 0.22)
put(bell(440.0, 1.4, 2.5), 16.8, 0.04)
# fenêtre : nappe, vitre qui coulisse + clic
put(bell(293.66, 1.8, 2), 17.95, 0.06); put(bell(440.0, 1.8, 2), 18.5, 0.05)
x = ax(0.9); put(bp(R.standard_normal(len(x)), 600, 2400)*np.sin(np.pi*x/0.9)**2, 19.9, 0.05)
y = ax(0.05); put(np.sin(2*np.pi*2400*y)*np.exp(-y*90), 20.8, 0.10)
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
