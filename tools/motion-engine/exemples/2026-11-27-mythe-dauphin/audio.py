#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 20 : le dauphin dort avec un œil ouvert ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2020)
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
# eau profonde : grondement filtré + houle lente
deep = lp(R.standard_normal(N), 220)*(0.7+0.3*np.sin(2*np.pi*0.08*T))
amb = deep*0.22
L += amb; Rt += np.roll(amb, 5000)
# nappe (ré mineur → ré majeur au final)
env = 0.35 + 0.30*sm((T-4.4)/1.0) + 0.4*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(73.42, 1.0), (110.0, 0.55), (146.83, 0.45), (174.61, 0.3)]:
    for det in (-0.35, 0.35): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 800)*env*0.04
L += pad; Rt += np.roll(pad, 400)
# clics d'écholocation + sifflements de dauphin
def click(t0, g=0.05, pan=0.0):
    x = ax(0.012); put(bp(R.standard_normal(len(x)), 3000, 9000)*np.exp(-x*500), t0, g, pan)
for t0 in np.arange(0.2, 2.4, 0.11): click(t0, 0.06, 0.3)
def whistle(t0, d, f0, f1, g=0.03, pan=0.0):
    x = ax(d); f = f0 + (f1-f0)*np.sin(np.pi*x/d*0.9)**2; put(np.sin(2*np.pi*np.cumsum(f)/SR)*np.sin(np.pi*x/d)**2, t0, g, pan)
whistle(0.9, 0.8, 5200, 9000, 0.025, -0.3); whistle(13.6, 0.9, 6000, 10500, 0.02, 0.4); whistle(18.3, 0.7, 7000, 11500, 0.02, -0.2)
# accroche : tampon VRAI + accord lumineux
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
for k, f in enumerate((587.33, 739.99, 880.0, 1174.66)): put(bell(f, 1.3, 2.8), 2.62+k*0.12, 0.04, -0.45+k*0.3)
# cerveau : pulsations rapides (côté éveillé) / onde lente (côté endormi)
for t0 in np.arange(5.0, 13.2, 0.25): put(bell(1760.0, 0.25, 18), t0, 0.012, 0.4 if t0 < 10.2 else -0.4)
x = ax(8.0); put(np.sin(2*np.pi*90*x)*(0.5+0.5*np.sin(2*np.pi*0.8*x))*np.sin(np.pi*x/8.0), 5.0, 0.05)
whoosh(4.35, 0.5, 0.07); whoosh(9.6, 0.7, 0.06)
put(bell(880.0, 1.6, 2.2), 4.5, 0.05); put(bell(783.99, 1.6, 2.2), 10.3, 0.05)
# groupe : respiration à la surface (souffle) + bulles
whoosh(13.3, 0.5, 0.06)
x = ax(0.6); put(bp(R.standard_normal(len(x)), 300, 2500)*np.sin(np.pi*x/0.6)**2, 15.6, 0.12)
for k in range(14): put(bell(900+R.random()*900, 0.12, 30), 15.8+k*0.07, 0.02, R.random()*2-1)
# nuance
whoosh(17.9, 0.6, 0.05)
put(bell(587.33, 1.8, 2), 18.0, 0.05); put(bell(739.99, 1.8, 2), 18.6, 0.045)
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
