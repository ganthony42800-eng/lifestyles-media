#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 17 : les chameaux stockent de l eau dans leur bosse ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1717)
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
# désert au crépuscule : grillons + vent
cr = np.zeros(N)
for f0, rate in [(4300, 14.0), (4700, 17.0)]:
    gate = (np.sin(2*np.pi*rate*T) > 0.3).astype(float) * (0.5 + 0.5*np.sin(2*np.pi*0.6*T + f0))
    cr += np.sin(2*np.pi*f0*T) * lp(gate, 200)
L += cr*0.006; Rt += np.roll(cr, 3000)*0.006
wind = lp(R.standard_normal(N), 400) * (0.6 + 0.3*np.sin(2*np.pi*0.09*T))
L += wind*0.05; Rt += np.roll(wind, 7000)*0.05
# nappe (fa mineur -> fa majeur au final)
env = 0.35 + 0.35*sm((T-4.45)/1.0) + 0.4*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(87.31, 1.0), (130.81, 0.55), (174.61, 0.45), (207.65, 0.3)]:
    for det in (-0.4, 0.4): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 900)*env*0.035
L += pad; Rt += np.roll(pad, 400)
# pas feutrés dans le sable + gargouillis de la bosse (eau) puis impact MYTHE
for t0 in (0.3, 1.5, 2.7): thud(t0, 0.10)
for k in range(8):
    x = ax(0.18); f = 300 + 500*R.random()
    put(np.sin(2*np.pi*(f+400*x)*x)*np.exp(-x*25), 0.4+k*0.27, 0.035, 0.2)
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
# graisse : nappe chaude
put(bell(523.25, 1.6, 2.2), 4.45, 0.06); put(bell(392.0, 1.8, 2.0), 5.8, 0.05)
# il boit : eau qui coule + gorgées
whoosh(8.6, 0.8, 0.05, 0.3)
x = ax(3.6); put(bp(R.standard_normal(len(x)), 800, 4000)*(0.5+0.5*np.sin(2*np.pi*3*x))*np.sin(np.pi*x/3.6), 9.4, 0.05, 0.3)
for k in range(7):
    x = ax(0.2); put(np.sin(2*np.pi*(180+260*x/0.2)*x)*np.exp(-x*18), 9.6+k*0.5, 0.09, 0.1)
# globules : battement grave
put(bell(349.23, 1.4, 2.4), 13.45, 0.05)
for k in range(5): thud(13.8+k*0.85, 0.08)
# nuance
put(bell(261.63, 1.8, 2), 17.95, 0.07); put(bell(392.0, 1.8, 2), 18.5, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(700+500*y/0.12)*y)*np.exp(-y*30), 19.4, 0.10)
# fin
for f in (349.23, 440.0, 523.25, 698.46): put(bell(f, 2.6, 1.2), 21.25, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(900+600*y/0.12)*y)*np.exp(-y*30), 21.6, 0.12)
mx = np.stack([L, Rt], 1); mx = mx/(np.max(np.abs(mx))+1e-9)*0.89
fade = np.ones(N); fade[:int(0.02*SR)] = np.linspace(0, 1, int(0.02*SR)); fade[-int(0.03*SR):] = np.linspace(1, 0, int(0.03*SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mx, -1, 1)*32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20*np.log10(np.sqrt(np.mean(mx**2))+1e-9), 1))
