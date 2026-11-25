#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 11 : un poisson rouge oublie tout en 3 secondes ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav
Temps calés sur index.html : 0-2,6 eau + tic-tac 3-2-1 · 2,6 tampon MYTHE · 4,45-8,4 nappe qui s'ouvre (semaines, mois, années)
8,6 palettes · 10,3 « ding » nourriture · 12,4-15 labyrinthe (pas arpégés) · 15,25 accord · 17,95 bocal étouffé · 19,4 bouton · 21,25 final."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1111)
L = np.zeros(N); Rt = np.zeros(N)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
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
def bubble(f0, d=0.12):
    x = ax(d); f = f0*(1+2.5*x/d); return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-x*30)*np.clip(x/0.002, 0, 1)
# eau : souffle grave filtré + bulles
water = lp(R.standard_normal(N), 380) * 0.5 * (1 - 0.6*sm((T-17.9)/0.4)*(1-sm((T-21.2)/0.4)))
L += water*0.05; Rt += np.roll(water, 900)*0.05
for k in range(70):
    put(bubble(R.uniform(500, 1400)), R.random()*24, 0.05, R.uniform(-0.7, 0.7))
# nappe (ré majeur) qui s'ouvre de 4,45 à 8,4
env = 0.35 + 0.65*sm((T-4.45)/3.5)*(1-sm((T-8.4)/0.8)) + 0.4*sm((T-15.2)/0.6)*(1-sm((T-17.9)/0.4)) + 0.5*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(73.42, 1.0), (146.83, 0.6), (185.0, 0.45), (220.0, 0.4), (293.66, 0.25), (369.99, 0.14)]:
    for det in (-0.6, 0.6): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 1100)*env*0.03
L += pad; Rt += np.roll(pad, 400)
# tic-tac 3-2-1
for t0 in (0.05, 0.9, 1.75):
    put(bell(1760.0, 0.25, 22), t0, 0.12); put(bell(880.0, 0.25, 18), t0+0.42, 0.06)
x = ax(1.0); put(hp(R.standard_normal(len(x)), 900)*sm(x/1.0)**2*0.5, 1.6, 0.05)
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.55); put(bell(1318.5, 0.8, 5.0), 3.05, 0.05)
# semaines, mois, années : trois notes qui s'élargissent
for t0, f in ((4.6, 587.33), (5.35, 739.99), (6.1, 880.0)):
    put(bell(f, 2.0, 1.8), t0, 0.07, -0.3); put(bell(f*1.5, 2.0, 2.2), t0+0.05, 0.03, 0.3)
# palettes : deux tons (rouge chaud / bleu froid) ; ding nourriture
put(bell(392.0, 1.0, 3), 8.6, 0.07, -0.5); put(bell(493.88, 1.0, 3), 8.75, 0.06, 0.5)
put(bell(1174.66, 1.2, 3), 10.3, 0.10, -0.3); put(bell(1567.98, 1.2, 3.5), 10.38, 0.06, -0.3)
for k in range(10): put(bubble(R.uniform(900, 1600)), 10.35+k*0.08, 0.07, -0.3)
# labyrinthe : pas arpégés
notes = [587.33, 659.25, 739.99, 880.0, 987.77, 880.0, 739.99, 880.0, 1174.66]
for k, f in enumerate(notes): put(bell(f, 0.6, 7), 12.6+k*0.27, 0.06, -0.6+k*0.15)
# des milliers d'études : accord + scintillement
for f in (293.66, 369.99, 440.0, 587.33): put(bell(f, 2.4, 1.3), 15.25, 0.05)
for k in range(16): put(bell(R.choice([1760.0, 2093.0, 2349.3, 2637.0]), 0.4, 11), 15.4+R.random()*2.2, 0.02, R.uniform(-0.8, 0.8))
# pourquoi : deux notes graves suspendues ; bouton
put(bell(220.0, 1.8, 2), 17.95, 0.07); put(bell(196.0, 1.8, 2), 18.6, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(700+500*y/0.12)*y)*np.exp(-y*30), 19.4, 0.10)
# fin
for f in (293.66, 440.0, 587.33, 880.0): put(bell(f, 2.6, 1.2), 21.25, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(900+600*y/0.12)*y)*np.exp(-y*30), 21.6, 0.12)
for k in range(10): put(bell(2637+220*k, 0.4, 10), 21.8+k*0.05, 0.02, -0.5+0.1*k)
mx = np.stack([L, Rt], 1); mx = mx/(np.max(np.abs(mx))+1e-9)*0.89
fade = np.ones(N); fade[:int(0.02*SR)] = np.linspace(0, 1, int(0.02*SR)); fade[-int(0.03*SR):] = np.linspace(1, 0, int(0.03*SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mx, -1, 1)*32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20*np.log10(np.sqrt(np.mean(mx**2))+1e-9), 1))
