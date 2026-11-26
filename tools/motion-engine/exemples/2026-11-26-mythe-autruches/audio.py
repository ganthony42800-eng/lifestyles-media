#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 14 : les autruches cachent leur tête dans le sable ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1414)
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

# vent du désert (souffle filtré, plus fort pendant le sprint)
wenv = 0.55 + 0.25*np.sin(2*np.pi*0.11*T) + 0.9*sm((T-12.45)/0.15)*(1-sm((T-15.15)/0.15))
wind = bp(R.standard_normal(N), 250, 2200) * wenv
L += wind*0.03; Rt += np.roll(wind, 3000)*0.03
# nappe chaude (la mineur -> la majeur au final)
env = 0.35 + 0.35*sm((T-4.45)/1.0) - 0.25*sm((T-12.45)/0.2)*(1-sm((T-15.25)/0.3)) + 0.4*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(110.0, 1.0), (164.81, 0.55), (220.0, 0.45), (261.63, 0.3)]:
    for det in (-0.4, 0.4): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 900)*env*0.03
L += pad; Rt += np.roll(pad, 400)
# 0-4,4 : grattement de sable (bec dans le sol)
for k in range(10):
    x = ax(0.18); put(bp(R.standard_normal(len(x)), 1200, 5000)*np.exp(-x*18), 0.3+k*0.4, 0.05, -0.2)
# 2,6 : tampon
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
# œufs retournés : petits clics de coquille
for k in range(8):
    x = ax(0.08); put(hp(R.standard_normal(len(x)), 2500)*np.exp(-x*70) + np.sin(2*np.pi*1800*x)*np.exp(-x*60)*0.4, 5.0+k*0.42, 0.06, 0.3*(-1)**k)
put(bell(523.25, 1.4, 2.6), 4.45, 0.06)
# couchée : glissando grave
x = ax(1.2); put(np.sin(2*np.pi*(220-120*x/1.2)*x)*np.exp(-x*2.2), 8.7, 0.06)
put(bell(329.63, 1.6, 2.2), 10.5, 0.05)
# sprint : foulées (≈ 4 par seconde, grave) + souffle
for k in range(int(2.7*4.1)):
    x = ax(0.16); put(lp(R.standard_normal(len(x)), 300)*np.exp(-x*30)*1.2 + np.sin(2*np.pi*70*x)*np.exp(-x*25), 12.5+k/4.1, 0.16, 0.25*(-1)**k)
for k in range(10): put(bell(440.0*2**(k/12), 0.25, 14), 12.85+k*0.135, 0.03)
# œil : scintillement
put(bell(783.99, 2.0, 1.8), 15.6, 0.06); put(bell(1046.5, 1.6, 2.2), 15.85, 0.04)
# Pline : deux notes « antiques »
put(bell(220.0, 1.8, 2), 17.95, 0.07); put(bell(329.63, 1.8, 2), 18.5, 0.06)
x = ax(0.6); put(bp(R.standard_normal(len(x)), 800, 4000)*np.exp(-x*6), 18.5, 0.05)  # froissement du buisson
y = ax(0.12); put(np.sin(2*np.pi*(700+500*y/0.12)*y)*np.exp(-y*30), 19.4, 0.10)
# fin
for f in (220.0, 277.18, 329.63, 440.0): put(bell(f, 2.6, 1.2), 21.25, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(900+600*y/0.12)*y)*np.exp(-y*30), 21.6, 0.12)
mx = np.stack([L, Rt], 1); mx = mx/(np.max(np.abs(mx))+1e-9)*0.89
fade = np.ones(N); fade[:int(0.02*SR)] = np.linspace(0, 1, int(0.02*SR)); fade[-int(0.03*SR):] = np.linspace(1, 0, int(0.03*SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mx, -1, 1)*32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20*np.log10(np.sqrt(np.mean(mx**2))+1e-9), 1))
