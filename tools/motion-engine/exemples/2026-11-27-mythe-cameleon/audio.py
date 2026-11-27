#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 19 : le caméléon change de couleur pour se cacher ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav"""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
SR = 44100; DUR = 24.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(1919)
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
lab = sm((T-13.2)/0.15)*(1-sm((T-18.0)/0.15))
# forêt de nuit : souffle feuillage + insectes (stridulations), coupés dans le plan microscope
leaves = bp(R.standard_normal(N), 250, 1800)*(0.6+0.3*np.sin(2*np.pi*0.11*T))
ins = np.sin(2*np.pi*4300*T)*(0.5+0.5*np.sign(np.sin(2*np.pi*31*T)))*(0.5+0.5*np.sin(2*np.pi*0.6*T))**4
amb = (leaves*0.05 + ins*0.012)*(1-lab)
L += amb; Rt += np.roll(amb, 7000)
# nappe (la mineur → la majeur au final)
env = 0.35 + 0.30*sm((T-4.4)/1.0) + 0.4*sm((T-21.25)/0.3)*(1-sm((T-23.6)/0.4))
env *= 1 - 0.7*sm((T-2.55)/0.08)*(1-sm((T-3.8)/0.8))
pad = np.zeros(N)
for f, a in [(110.0, 1.0), (164.81, 0.55), (220.0, 0.45), (261.63, 0.3)]:
    for det in (-0.4, 0.4): pad += a*np.sin(2*np.pi*(f+det)*T + R.random()*6.28)
pad = lp(pad, 900)*env*0.035
L += pad; Rt += np.roll(pad, 400)
# accroche : tampon + vague de couleur (arpège scintillant qui monte)
x = ax(1.4); hit = np.sin(2*np.pi*(55+90*np.exp(-x*18))*x)*np.exp(-x*4.5) + 0.6*lp(R.standard_normal(len(x)), 2500)*np.exp(-x*22)
put(hit, 2.6, 0.5)
for k, f in enumerate((440.0, 554.37, 659.25, 880.0, 1108.73, 1318.51)): put(bell(f, 1.2, 3.0), 2.62+k*0.14, 0.035, -0.6+k*0.24)
# duel : gonflements sifflés + cliquetis
for t0, pan in ((4.6, -0.5), (5.3, 0.5), (7.1, -0.4), (9.0, 0.4), (11.2, -0.3)):
    x = ax(0.45); put(bp(R.standard_normal(len(x)), 1800, 6000)*np.sin(np.pi*x/0.45)**3, t0, 0.04, pan)
put(bell(659.25, 1.6, 2.2), 4.4, 0.05); put(bell(587.33, 1.6, 2.2), 8.6, 0.05)
# microscope : réseau cristallin (pings) + glissando quand il s'écarte
whoosh(13.0, 0.5, 0.07)
for k, f in enumerate((1318.51, 1567.98, 1975.53, 2349.32)): put(bell(f, 1.1, 3.8), 13.4+k*0.22, 0.03, (k-1.5)*0.3)
x = ax(2.0); f = 520 + 260*sm(x/2.0); put(np.sin(2*np.pi*np.cumsum(f)/SR)*np.sin(np.pi*x/2.0)**2, 14.7, 0.035)
put(bell(783.99, 1.6, 2.5), 16.6, 0.04)
# nuance : retour au calme, bouton
whoosh(17.9, 0.6, 0.05)
put(bell(329.63, 1.8, 2), 18.0, 0.05); put(bell(440.0, 1.8, 2), 18.6, 0.045)
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
