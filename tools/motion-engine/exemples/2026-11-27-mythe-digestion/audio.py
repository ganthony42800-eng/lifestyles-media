#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 22 : digérer brûle des calories… donc manger fait maigrir ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2222)
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
# ambiance cuisine de nuit : souffle grave chaud + crépitement de flamme
deep = lp(R.standard_normal(N), 220)*(0.7+0.3*np.sin(2*np.pi*0.05*T))
amb = deep*0.16
L += amb; Rt += np.roll(amb, 4000)
def crackle(t0, t1, rate, g, pan=0.0):
    for tt in np.sort(R.uniform(t0, t1, int((t1-t0)*rate))):
        x = ax(0.012); put(bp(R.standard_normal(len(x)), 1800, 8000)*np.exp(-x*500), tt, g*(0.4+0.6*R.random()), pan+0.3*(R.random()*2-1))
crackle(0.2, 2.6, 14, 0.035); crackle(3.2, 4.4, 6, 0.02)
crackle(5.9, 8.3, 16, 0.03); crackle(13.5, 16.7, 20, 0.035); crackle(18.9, 21.2, 14, 0.03)
# nappe (ré mineur → ré majeur au final)
env = 0.35 + 0.25*sm((T-4.4)/1.0) + 0.4*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(73.42, 1.0), (110.0, 0.55), (146.83, 0.45), (174.61, 0.3)]:
    for det in (-0.3, 0.3): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 750)*env*0.04
L += pad; Rt += np.roll(pad, 400)
# tampon FAUX… MAIS
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
for k, f in enumerate((587.33, 698.46, 880.0)): put(bell(f, 1.3, 2.8), 2.62+k*0.12, 0.04, -0.4+k*0.4)
# grille : apparition puis unités qui partent (petits « pops » montants)
whoosh(4.35, 0.5, 0.07)
for k in range(10): put(bell(880*2**(k/24), 0.25, 14), 4.5+k*0.07, 0.012, -0.5+k*0.1)
def pop(t0, f0, g=0.05, pan=0.0):
    y = ax(0.14); put(np.sin(2*np.pi*np.cumsum(f0+900*y/0.14)/SR)*np.exp(-y*28), t0, g, pan)
for k in range(10): pop(5.75+k*0.13, 500+k*30, 0.05, R.random()*1.2-0.6)
# jauges qui se remplissent
whoosh(8.35, 0.6, 0.06)
for k, (f, t0) in enumerate([(196.0, 8.9), (246.94, 9.25), (293.66, 9.6)]):
    x = ax(1.2); ff = f*(1+0.5*(x/1.2)); put(np.sin(2*np.pi*np.cumsum(ff)/SR)*np.sin(np.pi*x/1.2), t0, 0.05, -0.5+k*0.5)
    put(bell(f*4, 1.0, 3.5), t0+1.2, 0.03, -0.5+k*0.5)
# 100 kcal de protéines : 20 unités partent
whoosh(12.55, 0.5, 0.06)
for k in range(20): pop(13.3+k*0.08, 450+k*25, 0.04, R.random()*1.2-0.6)
x = ax(1.6); put(lp(R.standard_normal(len(x)), 1200)*np.sin(np.pi*x/1.6), 14.9, 0.05)
# céleri : croquement
whoosh(16.75, 0.5, 0.06)
for k in range(5):
    x = ax(0.06); put(bp(R.standard_normal(len(x)), 900, 6000)*np.exp(-x*70), 17.2+k*0.045, 0.16, 0.1)
put(bell(523.25, 1.2, 3), 17.6, 0.035)
# geste + partage + fin
whoosh(18.85, 0.6, 0.05)
put(bell(587.33, 1.8, 2), 18.95, 0.05); put(bell(739.99, 1.8, 2), 19.5, 0.045)
y = ax(0.12); put(np.sin(2*np.pi*(700+500*y/0.12)*y)*np.exp(-y*30), 19.6, 0.10)
for f in (293.66, 369.99, 440.0, 587.33): put(bell(f, 2.6, 1.2), 21.25, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(900+600*y/0.12)*y)*np.exp(-y*30), 21.6, 0.12)
mx = np.stack([L, Rt], 1); mx = mx/(np.max(np.abs(mx))+1e-9)*0.89
fade = np.ones(N); fade[:int(0.02*SR)] = np.linspace(0, 1, int(0.02*SR)); fade[-int(0.03*SR):] = np.linspace(1, 0, int(0.03*SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mx, -1, 1)*32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20*np.log10(np.sqrt(np.mean(mx**2))+1e-9), 1))
