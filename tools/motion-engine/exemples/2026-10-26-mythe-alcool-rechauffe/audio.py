#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 4 : l'alcool réchauffe ? ». Synthèse procédurale, graine fixe.
Usage : python3 audio.py sortie.wav [rms_cible_dBFS]
Durée 25,25 s (le flux vidéo de 25,0 s fixe la fin : évite la perte d'images avec -shortest).
Temps calés sur index.html :
 ronronnement du câble (modulé par le balancement 0,36 Hz) + vent d'altitude, tout du long
 · woosh des chaises descendantes à 2,0 + 2,5 k (croisement à gauche, effet Doppler)
 · pylônes 0,8 et 10,6 : clac-clac-clac des galets + petite secousse grave
 · 3,5 clic du bouchon · 4,0-4,4 souffle de vent quand la tête bascule (aucun bruit de gorgée)
 · 5,0 « flush » : nappe chaude grave (attaque lente) + battement de cœur 66 bpm → 56 bpm après 9,25 → arrêt 16,8
 · 7,95-8,55 fermeture éclair · 8,5 crépitement doux de la braise
 · SILENCE 9,0-9,25 · 9,25 rafale + cristallisation (crépitements aigus)
 · 11,0-12,0 froissement de poche + « pouf » · 12,8-17,2 la nappe se désaccorde, vent plus fort
 · 15,2-17,2 givre qui crépite · 16,2 alarme douce coupée net · 17,2 tampon sourd + givre · 17,2-19,4 tempête
 · 19,4 vapeur + accord qui se résout · 22,3 scintillement de la signature · 24,4 retour de l'ambiance du début.
Interdits respectés : ni déglutition, ni glouglou, ni glaçons, ni trinquage, ni musique de bar."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 25.25; LOOP = 25.0; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2610)
L = np.zeros(N); Rt = np.zeros(N)


def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def sm(x): x = np.clip(x, 0, 1); return x * x * (3 - 2 * x)
def win(a, b, fa=0.2, fb=0.2): return sm((T - a) / fa) * sm((b - T) / fb)
def ax(d): return np.arange(int(d * SR)) / SR


def put(sig, t0, g=1.0, pan=0.0):
    i = int(round(t0 * SR))
    if i >= N or i + len(sig) <= 0: return
    s = sig * g
    if i < 0: s = s[-i:]; i = 0
    s = s[:N - i]
    L[i:i + len(s)] += s * (1 - max(pan, 0)); Rt[i:i + len(s)] += s * (1 + min(pan, 0))


def tone(f, d, dec, ph=0.0):
    x = ax(d); return np.sin(2 * np.pi * f * x + ph) * np.exp(-x * dec)


# 1. Fil rouge : le câble (bruit grave filtré, modulé par le balancement de la chaise, périodique sur 25 s)
sway = 0.5 + 0.5 * np.sin(2 * np.pi * (9 / LOOP) * T)
hum = bp(R.standard_normal(N), 55, 130) * (0.6 + 0.4 * sway)
hum += 0.25 * np.sin(2 * np.pi * 73.0 * T) * (0.7 + 0.3 * sway) + 0.12 * np.sin(2 * np.pi * 146.3 * T)
hum *= 0.05
# 2. Vent d'altitude : rafales lentes, plus fort la nuit et dans la tempête
wind_src = lp(R.standard_normal(N), 420) + 0.35 * bp(R.standard_normal(N), 600, 2200)
gusts = 0.55 + 0.25 * np.sin(2 * np.pi * T * 0.21 + 1.0) + 0.2 * np.sin(2 * np.pi * T * 0.53)
storm = 1 + 0.7 * win(12.8, 19.6, 1.5, 1.0) + 1.3 * win(17.0, 19.8, 0.4, 1.2) + 1.6 * win(9.25, 10.6, 0.05, 0.8)
wind = wind_src * gusts * storm * 0.032
L += hum + wind; Rt += np.roll(hum, 331) + np.roll(wind, 911)

# 3. Chaises descendantes : woosh toutes les 2,5 s (croisement à gauche, fréquence qui descend)
for k in range(-1, 11):
    tc = 2.0 + 2.5 * k
    d = 0.9; x = ax(d); u = x / d
    src = R.standard_normal(len(x)); out = np.zeros(len(x)); seg = int(0.02 * SR)
    for i in range(0, len(x), seg):
        fc = 1800 - 1300 * u[i]
        out[i:i + seg] = bp(src[max(0, i - 3 * seg):i + seg], fc * 0.7, fc * 1.4)[-len(out[i:i + seg]):]
    put(out * np.sin(np.pi * u) ** 3 * 0.10, tc - 0.45, 1.0, -0.6)

# 4. Pylônes : clac-clac-clac des galets + choc grave
def clack(t0, g=1.0):
    for j in range(3):
        x = ax(0.12)
        s = bp(R.standard_normal(len(x)), 700, 5000) * np.exp(-x * 90)
        for f, a in ((900, 0.6), (1400, 0.4), (2300, 0.25)):
            s += a * np.sin(2 * np.pi * f * x) * np.exp(-x * 45)
        put(s, t0 - 0.1 + j * 0.09, 0.32 * g, 0.15)
    x = ax(0.5); put(np.sin(2 * np.pi * (60 + 40 * np.exp(-x * 30)) * x) * np.exp(-x * 9), t0, 0.35 * g)
    x = ax(0.6); put(lp(R.standard_normal(len(x)), 300) * np.exp(-x * 6), t0, 0.12 * g)
clack(0.8); clack(10.6)

# 5. Gestes
x = ax(0.05); put(bp(R.standard_normal(len(x)), 2500, 9000) * np.exp(-x * 160), 3.50, 0.25, 0.3)       # bouchon
x = ax(0.04); put(bp(R.standard_normal(len(x)), 2000, 7000) * np.exp(-x * 200), 3.58, 0.18, 0.3)
x = ax(0.6); put(bp(R.standard_normal(len(x)), 300, 2500) * np.sin(np.pi * x / 0.6) ** 2, 3.95, 0.10, 0.0)  # souffle de la tête qui bascule
# fermeture éclair : dents qui cliquettent, montée du filtre
d = 0.6; x = ax(d); z = np.zeros(len(x))
for i, tz in enumerate(np.cumsum(np.full(40, d / 41))):
    j = int(tz * SR); z[j:j + 300] += np.exp(-np.arange(min(300, len(z) - j)) / 40) * (0.6 + 0.4 * R.random())
put(hp(z * R.standard_normal(len(z)), 1500) * 0.5 + bp(R.standard_normal(len(x)), 1500, 5000) * 0.08, 7.95, 0.5, 0.1)
# poche : froissement + « pouf » ironique
x = ax(1.0); put(bp(R.standard_normal(len(x)), 800, 6000) * (0.4 + 0.6 * np.abs(np.sin(x * 17))) * np.sin(np.pi * x) ** 2, 11.0, 0.07, 0.6)
x = ax(0.25); put(np.sin(2 * np.pi * (220 - 120 * x / 0.25) * x) * np.exp(-x * 14), 12.0, 0.18, 0.4)

# 6. Chaleur : nappe grave (ré majeur) qui gonfle à 5,0 ; se désaccorde la nuit ; se résout à 19,4
pad = np.zeros(N)
det = 1 + 0.018 * win(12.8, 19.4, 2.0, 0.6)
for f, a in ((73.42, 1.0), (110.0, 0.7), (146.83, 0.55), (185.0, 0.4)):
    for dd in (0.997, 1.003):
        ph = 2 * np.pi * np.cumsum(f * dd * (det if f in (110.0, 185.0) else 1.0)) / SR
        pad += a * (np.sin(ph) + 0.2 * np.sin(2 * ph))
pad = lp(pad, 900) * 0.022 * (win(5.0, 9.0, 0.8, 0.02) + 0.55 * win(9.25, 17.5, 0.5, 1.5))
res = np.zeros(N)
for f in (146.83, 220.0, 293.66, 369.99):
    res += np.sin(2 * np.pi * f * T) + 0.15 * np.sin(4 * np.pi * f * T)
res = lp(res, 1600) * 0.012 * win(19.4, 24.6, 0.9, 0.8)
L += pad + res; Rt += np.roll(pad, 600) + np.roll(res, 900)
# battement de cœur : 66 bpm (5,0 → 9,0), 56 bpm (9,6 → 16,8)
def beat(t0, g):
    for dt, a in ((0, 1.0), (0.17, 0.6)):
        x = ax(0.25); put(np.sin(2 * np.pi * (55 + 25 * np.exp(-x * 40)) * x) * np.exp(-x * 18) * a, t0 + dt, g)
tb = 5.05
while tb < 9.0: beat(tb, 0.45 * min(1, (tb - 4.9) / 0.8)); tb += 60 / 66
tb = 9.6
while tb < 16.8: beat(tb, 0.38 * (1 - (tb - 9.6) / 9)); tb += 60 / 56
# braise : crépitement doux 8,5-9,0
for i in range(26):
    x = ax(0.03); put(bp(R.standard_normal(len(x)), 800, 3000) * np.exp(-x * 150), 8.45 + R.random() * 0.55, 0.06 + 0.06 * R.random(), R.uniform(-0.3, 0.3))

# 7. Froid : rafale + cristallisation (9,25) ; givre 15,2-17,2 ; tampon 17,2
x = ax(1.3); put(bp(R.standard_normal(len(x)), 200, 5000) * np.exp(-x * 1.8) * np.clip(x / 0.03, 0, 1), 9.25, 0.35, -0.2)
def crackle(t0, t1, n, g):
    for i in range(n):
        tc = t0 + (t1 - t0) * (i / n) ** 0.7 + R.random() * 0.03
        x = ax(0.02); put(bp(R.standard_normal(len(x)), 6000, 9500) * np.exp(-x * 300), tc, g * (0.5 + 0.5 * R.random()), R.uniform(-0.7, 0.7))
        if R.random() < 0.3: put(tone(R.uniform(3500, 6500), 0.25, 18), tc, g * 0.15, R.uniform(-0.5, 0.5))
crackle(9.3, 10.4, 70, 0.10); crackle(15.2, 17.2, 90, 0.08); crackle(17.2, 18.0, 40, 0.09)
# « Alarme coupée » : deux tons doux d'alarme interne, coupés net à 16,2
for k, t0 in enumerate(np.arange(15.45, 16.2, 0.25)):
    f = 880 if k % 2 == 0 else 698.5
    d = min(0.2, 16.2 - t0); x = ax(d)
    put(np.sin(2 * np.pi * f * x) * np.clip(x / 0.01, 0, 1) * np.clip((d - x) / 0.005, 0, 1), t0, 0.035, 0.0)
x = ax(0.3); put(lp(R.standard_normal(len(x)), 500) * np.exp(-x * 25), 16.2, 0.15)
# tampon du verdict
x = ax(0.6); put(np.sin(2 * np.pi * (48 + 50 * np.exp(-x * 35)) * x) * np.exp(-x * 8) + 0.5 * lp(R.standard_normal(len(x)), 1200) * np.exp(-x * 28), 17.2, 0.55)
# 8. Vapeur du thermos (19,5 → 21,8)
x = ax(2.3); put(bp(R.standard_normal(len(x)), 2500, 8000) * np.sin(np.pi * x / 2.3) ** 2 * (0.7 + 0.3 * np.sin(x * 5)), 19.5, 0.025, 0.0)
# 9. Signature : scintillement doré
for kk in range(10):
    put(tone(1975.5 * 2 ** (kk / 12 * 1.2), 0.7, 5), 22.3 + kk * 0.05, 0.018, (kk / 5) - 1)
put(sum(g * tone(1318.5 * k, 2.0, 2.6 * (1 + 0.4 * i)) for i, (k, g) in enumerate(((1, 1), (2, .25), (3, .08)))), 22.6, 0.09, 0.0)

# Mixage : silence 9,0-9,25 ; réverbération courte ; fondus d'extrémité très courts (raccord de boucle)
gate = 1 - win(9.0, 9.25, 0.03, 0.005) * 0.985
mixL, mixR = L.copy(), Rt.copy()
for dl, g in ((0.031, .18), (0.047, .14), (0.071, .11), (0.109, .07), (0.163, .045), (0.24, .03)):
    k = int(dl * SR); mixL[k:] += Rt[:-k] * g; mixR[k:] += L[:-k] * g
out = np.stack([mixL * gate, mixR * gate], 1)
out *= np.clip(T / 0.01, 0, 1)[:, None] * np.clip((DUR - T) / 0.05, 0, 1)[:, None]


def limit(x, ceil):
    pkv = maximum_filter1d(np.max(np.abs(x), 1), int(0.006 * SR))
    gr = np.minimum(1.0, ceil / np.maximum(pkv, 1e-9))
    gr = np.minimum(gr, uniform_filter1d(gr, int(0.004 * SR)))
    gr = uniform_filter1d(gr, int(0.003 * SR))
    return x * gr[:, None]


target_rms = float(sys.argv[2]) if len(sys.argv) > 2 else -17.0
ceil = 10 ** (-3.5 / 20)   # marge pour le dépassement de l'encodage AAC
for _ in range(8):
    rms = np.sqrt(np.mean(out ** 2)); out *= 10 ** (target_rms / 20) / rms
    out = limit(out, ceil * 0.97)
out = np.clip(out, -ceil, ceil) * gate[:, None]
print(f"pic {20*np.log10(np.max(np.abs(out))):.2f} dBFS, RMS {20*np.log10(np.sqrt(np.mean(out**2))):.2f} dBFS")
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
