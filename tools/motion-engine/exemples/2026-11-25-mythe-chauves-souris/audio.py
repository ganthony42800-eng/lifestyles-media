#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 12 : les chauves-souris sont aveugles ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav
Temps calés sur index.html : 0-2,6 grotte + cris du sonar et échos · 2,6 tampon MYTHE + yeux qui s'ouvrent · 4,45 nappe (gros plan)
8,45 roussettes (notes chaudes) · 12,45-13,9 balayage ultraviolet · 15,35-17,9 sonar · 17,95 question · 19,4 bouton · 21,25 final."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1212)
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
def chirp(f0=4200, f1=1900, d=0.06):
    x = ax(d); f = f0 + (f1 - f0) * x / d
    return np.sin(2*np.pi*np.cumsum(f)/SR) * np.sin(np.pi*x/d)**2
# grotte : souffle grave + gouttes
cave = lp(R.standard_normal(N), 260) * 0.6
L += cave*0.05; Rt += np.roll(cave, 1200)*0.05
for k in range(26):
    put(bell(R.uniform(1300, 2300), 0.5, 9), R.random()*24, 0.025, R.uniform(-0.8, 0.8))
# battements d'ailes : bouffées de bruit au rythme du vol
rate = np.where((T > 4.2) & (T < 8.3), 0.55, 1.55)
ph = np.cumsum(rate) / SR
flapenv = np.clip(np.sin(2*np.pi*ph), 0, 1)**6
flaps = bp(R.standard_normal(N), 120, 900) * flapenv * 0.9
L += flaps*0.05; Rt += flaps*0.05
# sonar : cris + échos (aux mêmes instants que les ondes)
pulses = list(np.arange(0.15, 2.6, 0.5)) + list(np.arange(15.35, 17.9, 0.42))
for t0 in pulses:
    put(chirp(), t0, 0.10)
    for k, (dt, g) in enumerate([(0.18, 0.04), (0.31, 0.03), (0.47, 0.02)]):
        put(chirp(3900, 1800, 0.05), t0 + dt, g, (-1)**k*0.6)
# nappe (mi mineur → mi majeur au final)
env = 0.3 + 0.5*sm((T-4.45)/1.2)*(1-sm((T-8.3)/0.8)) + 0.35*sm((T-8.45)/0.5)*(1-sm((T-15.2)/0.5)) + 0.5*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(82.41, 1.0), (164.81, 0.6), (196.0, 0.45), (246.94, 0.4), (329.63, 0.22), (392.0, 0.12)]:
    for det in (-0.5, 0.5): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 1000)*env*0.03
L += pad; Rt += np.roll(pad, 400)
# 2,6 : tampon + yeux qui s'ouvrent (scintillement montant)
x = ax(1.0); put(hp(R.standard_normal(len(x)), 900)*sm(x/1.0)**2*0.5, 1.6, 0.05)
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.55)
for k, f in enumerate([987.77, 1318.5, 1661.2, 1975.5]): put(bell(f, 1.4, 3.5), 2.70+k*0.06, 0.05, -0.3+0.2*k)
# gros plan sur les yeux : deux notes
put(bell(659.25, 2.2, 1.6), 4.6, 0.07, -0.3); put(bell(987.77, 2.2, 1.8), 5.3, 0.05, 0.3)
# roussettes : notes chaudes, odeur (souffle doux)
for t0, f in ((8.6, 392.0), (8.85, 493.88), (9.1, 587.33)): put(bell(f, 1.4, 2.6), t0, 0.06, -0.4 + 0.4*(f > 450))
x = ax(2.4); put(bp(R.standard_normal(len(x)), 2000, 5000)*np.sin(np.pi*x/2.4)**2*0.25, 9.6, 0.25)
# ultraviolet : balayage montant + scintillement
x = ax(1.0); f = 600 + 1800*x
put(np.sin(2*np.pi*np.cumsum(f)/SR)*np.sin(np.pi*x)**2, 13.0, 0.05)
for k in range(14): put(bell(R.choice([1567.98, 1975.5, 2349.3, 2637.0]), 0.5, 9), 13.2+R.random()*1.6, 0.02, R.uniform(-0.8, 0.8))
put(bell(220.0, 1.2, 3), 14.1, 0.06)  # « Toi, non. »
# question finale ; bouton
put(bell(246.94, 1.8, 2), 17.95, 0.07); put(bell(329.63, 1.8, 2), 18.5, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(700+500*y/0.12)*y)*np.exp(-y*30), 19.4, 0.10)
# fin
for f in (329.63, 415.3, 493.88, 659.25): put(bell(f, 2.6, 1.2), 21.25, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(900+600*y/0.12)*y)*np.exp(-y*30), 21.6, 0.12)
for k in range(10): put(bell(2637+220*k, 0.4, 10), 21.8+k*0.05, 0.02, -0.5+0.1*k)
mx = np.stack([L, Rt], 1); mx = mx/(np.max(np.abs(mx))+1e-9)*0.89
fade = np.ones(N); fade[:int(0.02*SR)] = np.linspace(0, 1, int(0.02*SR)); fade[-int(0.03*SR):] = np.linspace(1, 0, int(0.03*SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mx, -1, 1)*32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20*np.log10(np.sqrt(np.mean(mx**2))+1e-9), 1))
