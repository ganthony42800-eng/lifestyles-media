#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 21 : une fourmi soulève 50 fois son poids ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2121)
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
# nuit en forêt : souffle grave + grillons
deep = lp(R.standard_normal(N), 260)*(0.7+0.3*np.sin(2*np.pi*0.07*T))
amb = deep*0.18
L += amb; Rt += np.roll(amb, 5000)
for t0 in np.arange(0.3, 23.5, 0.9):
    for k in range(3):
        x = ax(0.03); put(np.sin(2*np.pi*4700*x)*np.sin(np.pi*x/0.03)**2, t0+k*0.05, 0.010, -0.6 if int(t0) % 2 else 0.6)
# nappe (mi mineur → mi majeur au final)
env = 0.35 + 0.30*sm((T-4.4)/1.0) + 0.4*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(82.41, 1.0), (123.47, 0.55), (164.81, 0.45), (196.0, 0.3)]:
    for det in (-0.35, 0.35): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 800)*env*0.04
L += pad; Rt += np.roll(pad, 400)
# pas de fourmi (tic-tic légers)
def tick(t0, g=0.03, pan=0.0):
    x = ax(0.01); put(bp(R.standard_normal(len(x)), 2500, 7000)*np.exp(-x*600), t0, g, pan)
for t0 in np.arange(0.2, 4.3, 0.143): tick(t0, 0.035, 0.2)
for t0 in np.arange(18.0, 23.8, 0.13): tick(t0, 0.025, -0.2)
# tampon
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
for k, f in enumerate((659.25, 830.61, 987.77, 1318.5)): put(bell(f, 1.3, 2.8), 2.62+k*0.12, 0.04, -0.45+k*0.3)
# vitre (tintement) + cube posé
whoosh(4.35, 0.5, 0.07); put(bell(2093.0, 1.2, 3.5), 4.5, 0.035); put(bell(1567.98, 1.0, 4), 4.75, 0.03)
x = ax(0.3); put(np.sin(2*np.pi*110*x)*np.exp(-x*20), 5.0, 0.15)
# cou : tension qui monte puis rupture
whoosh(8.95, 0.6, 0.06)
x = ax(1.6); f = 120 + 260*(x/1.6)**2; put(np.sin(2*np.pi*np.cumsum(f)/SR)*sm(x/0.3)*0.8, 9.8, 0.07)
x = ax(0.8); f = 380 + 200*(x/0.8); put(np.sin(2*np.pi*np.cumsum(f)/SR)*(0.6+0.4*np.sin(2*np.pi*14*x)), 10.6, 0.06)
x = ax(1.0); crack = bp(R.standard_normal(len(x)), 1500, 9000)*np.exp(-x*9) + np.sin(2*np.pi*(70+60*np.exp(-x*20))*x)*np.exp(-x*5)
put(crack, 11.4, 0.35)
for k in range(12): put(bell(1200+R.random()*1800, 0.15, 25), 11.45+k*0.06, 0.015, R.random()*2-1)
# cubes : croissance + face + remplissage
whoosh(13.35, 0.5, 0.06)
x = ax(0.8); f = 220 + 220*(x/0.8); put(np.sin(2*np.pi*np.cumsum(f)/SR)*np.sin(np.pi*x/0.8), 14.0, 0.05)
put(bell(1318.5, 1.2, 3), 14.65, 0.04)
for k in range(8): put(bell(440*2**(k/12*1.5), 0.4, 8), 15.25+k*0.15, 0.025, -0.5+k*0.14)
# nuance + fin
whoosh(17.9, 0.6, 0.05)
put(bell(659.25, 1.8, 2), 18.0, 0.05); put(bell(830.61, 1.8, 2), 18.6, 0.045)
y = ax(0.12); put(np.sin(2*np.pi*(700+500*y/0.12)*y)*np.exp(-y*30), 19.4, 0.10)
for f in (329.63, 415.30, 493.88, 659.25): put(bell(f, 2.6, 1.2), 21.25, 0.06)
y = ax(0.12); put(np.sin(2*np.pi*(900+600*y/0.12)*y)*np.exp(-y*30), 21.6, 0.12)
mx = np.stack([L, Rt], 1); mx = mx/(np.max(np.abs(mx))+1e-9)*0.89
fade = np.ones(N); fade[:int(0.02*SR)] = np.linspace(0, 1, int(0.02*SR)); fade[-int(0.03*SR):] = np.linspace(1, 0, int(0.03*SR))
mx *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else 'audio.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mx, -1, 1)*32767).astype('<i2').tobytes())
print('ok', out, 'rms dBFS', round(20*np.log10(np.sqrt(np.mean(mx**2))+1e-9), 1))
