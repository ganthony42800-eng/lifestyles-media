#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 23 : les vaches se couchent quand il va pleuvoir ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2323)
L = np.zeros(N); Rt = np.zeros(N)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
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
def whoosh(t0, d=0.5, g=0.06, pan=0.0):
    x = ax(d); put(bp(R.standard_normal(len(x)), 500, 3000)*np.sin(np.pi*x/d)**2, t0, g, pan)
def moo(t0, d=1.3, f0=118, g=0.10, pan=0.0):
    x = ax(d); f = f0*(1+0.12*np.sin(np.pi*x/d)) - 18*(x/d)**2 + 1.5*np.sin(2*np.pi*5*x)
    ph = 2*np.pi*np.cumsum(f)/SR; saw = sum(np.sin(k*ph)/k for k in range(1, 14))
    v = bp(saw, 250, 900)*0.7 + lp(saw, 400)*0.5
    env = sm(x/0.15)*(1-sm((x-d+0.35)/0.35)); put(v*env, t0, g, pan)
# vent + pluie (plus dense pendant le plan Met Office)
wind = lp(R.standard_normal(N), 400)*(0.6+0.4*np.sin(2*np.pi*0.09*T))
rainE = 0.25 + 0.75*sm((T-4.6)/0.8)*(1-sm((T-8.9)/0.4)) + 0.35*sm((T-19.6)/0.8)
rain = bp(R.standard_normal(N), 1500, 7000)*rainE
L += wind*0.16 + rain*0.05; Rt += np.roll(wind, 7000)*0.16 + np.roll(rain, 3000)*0.05
# tonnerre lointain (accroche) + nappe
x = ax(3.0); thun = lp(R.standard_normal(len(x)), 140, 4)*np.exp(-x*1.2)*sm(x/0.4)
put(thun, 0.6, 1.4, -0.3)
env = 0.35 + 0.3*sm((T-4.4)/1.0) + 0.4*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(73.42, 1.0), (110.0, 0.55), (146.83, 0.45), (174.61, 0.3)]:
    for det in (-0.35, 0.35): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 800)*env*0.04
L += pad; Rt += np.roll(pad, 400)
moo(1.6, 1.4, 112, 0.09, 0.4)
# tampon
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
for k, f in enumerate((587.33, 698.46, 880.0, 1174.66)): put(bell(f, 1.3, 2.8), 2.62+k*0.12, 0.04, -0.45+k*0.3)
whoosh(4.35, 0.5, 0.07)
# horloge : tic-tac pendant le remplissage
whoosh(8.95, 0.6, 0.06)
for t0 in np.arange(9.5, 11.3, 0.15):
    y = ax(0.012); put(bp(R.standard_normal(len(y)), 2500, 6000)*np.exp(-y*500), t0, 0.06)
put(bell(1174.66, 1.4, 2.5), 11.25, 0.045)
# thermomètre qui monte, vache qui se lève
whoosh(13.35, 0.5, 0.06)
x = ax(1.6); f = 200 + 400*(x/1.6)**1.5; put(np.sin(2*np.pi*np.cumsum(f)/SR)*sm(x/0.2)*(1-sm((x-1.4)/0.2)), 13.8, 0.05)
put(bell(880.0, 1.2, 3), 15.4, 0.04)
moo(15.6, 1.1, 128, 0.07, -0.3)
x = ax(1.0); put(lp(R.standard_normal(len(x)), 300)*np.sin(np.pi*x)**2, 15.3, 0.25)
# nuance : troupeau qui se couche en cascade
whoosh(17.9, 0.6, 0.05)
for k, t0 in enumerate((18.4, 19.1, 19.6, 20.0)):
    x = ax(0.6); put(lp(R.standard_normal(len(x)), 200)*np.sin(np.pi*x/0.6)**2, t0+0.5, 0.3, -0.6+k*0.4)
    put(bell(440*2**(k*3/12), 0.8, 4), t0+0.6, 0.025, -0.6+k*0.4)
y = ax(0.12); put(np.sin(2*np.pi*(700+500*y/0.12)*y)*np.exp(-y*30), 19.4, 0.10)
for f in (293.66, 369.99, 440.0, 587.33): put(bell(f, 2.6, 1.2), 21.25, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(900+600*y/0.12)*y)*np.exp(-y*30), 21.6, 0.12)
mx = np.stack([L, Rt], 1); mx = mx/(np.max(np.abs(mx))+1e-9)*0.89
fade = np.ones(N); fade[:int(0.02*SR)] = np.linspace(0, 1, int(0.02*SR)); fade[-int(0.03*SR):] = np.linspace(1, 0, int(0.03*SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mx, -1, 1)*32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20*np.log10(np.sqrt(np.mean(mx**2))+1e-9), 1))
