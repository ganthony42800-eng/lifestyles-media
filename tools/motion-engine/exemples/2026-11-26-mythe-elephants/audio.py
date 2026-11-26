#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 16 : les éléphants ont peur des souris ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1616)
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
# savane au crépuscule : grillons + vent doux
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
env *= 1 - 0.6*sm((T-9.75)/0.05)*(1-sm((T-11.0)/0.8))
pad = np.zeros(N)
for f, a in [(87.31, 1.0), (130.81, 0.55), (174.61, 0.45), (207.65, 0.3)]:
    for det in (-0.4, 0.4): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 900)*env*0.035
L += pad; Rt += np.roll(pad, 400)
# pas lourds de l'éléphant + souris
for t0 in (0.3, 1.8, 3.3): thud(t0, 0.18)
for t0 in (0.9, 1.4, 3.8): squeak(t0, 0.03, 0.35)
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
# test 2006 : calme, bâillement grave
put(bell(523.25, 1.6, 2.2), 4.45, 0.06); put(bell(392.0, 1.8, 2.0), 5.8, 0.05)
x = ax(1.2); put(lp(R.standard_normal(len(x)), 300)*np.sin(np.pi*x/1.2)**2, 6.6, 0.12)
# souris qui file + sursaut (barrissement synthétique bref)
for k in range(10): put(lp(R.standard_normal(int(0.03*SR)), 3000)*0.5, 9.3+k*0.07, 0.05, 0.6-0.12*k)
whoosh(9.3, 0.7, 0.07, 0.5)
x = ax(0.9); f = 520 + 260*np.sin(np.pi*x/0.9)
tr = np.sin(2*np.pi*np.cumsum(f)/SR) + 0.5*np.sin(2*np.pi*np.cumsum(f*2.01)/SR) + 0.3*np.sin(2*np.pi*np.cumsum(f*3.02)/SR)
tr = bp(tr*(1+0.3*R.standard_normal(len(x))), 300, 3500) * np.sin(np.pi*x/0.9)**0.6
put(tr, 9.8, 0.10)
thud(10.15, 0.22)
# trompe : souffle + souris qui roule
put(bell(349.23, 1.4, 2.4), 13.45, 0.05)
x = ax(1.3); put(bp(R.standard_normal(len(x)), 200, 2500)*np.sin(np.pi*x/1.3)**1.5, 15.0, 0.16, 0.2)
for k in range(4): squeak(15.2+k*0.22, 0.025, 0.4)
for k in range(5): put(lp(R.standard_normal(int(0.04*SR)), 1500), 15.9+k*0.09, 0.03, 0.4)
# nuance
put(bell(261.63, 1.8, 2), 17.95, 0.07); put(bell(392.0, 1.8, 2), 18.5, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(700+500*y/0.12)*y)*np.exp(-y*30), 19.4, 0.10)
# fin
for f in (349.23, 440.0, 523.25, 698.46): put(bell(f, 2.6, 1.2), 21.25, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(900+600*y/0.12)*y)*np.exp(-y*30), 21.6, 0.12)
squeak(22.4, 0.02, 0.3)
mx = np.stack([L, Rt], 1); mx = mx/(np.max(np.abs(mx))+1e-9)*0.89
fade = np.ones(N); fade[:int(0.02*SR)] = np.linspace(0, 1, int(0.02*SR)); fade[-int(0.03*SR):] = np.linspace(1, 0, int(0.03*SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mx, -1, 1)*32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20*np.log10(np.sqrt(np.mean(mx**2))+1e-9), 1))
