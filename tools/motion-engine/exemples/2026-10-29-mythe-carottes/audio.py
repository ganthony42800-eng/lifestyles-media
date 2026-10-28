#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 7 : les carottes font mieux voir ? ». Synthèse procédurale, graine fixe.
Usage : python3 audio.py sortie.wav [rms_cible_dBFS]
Durée 25,25 s (le flux vidéo de 25,0 s fixe la fin). Temps calés sur index.html (script v2) :
 cuisine le soir (frigo 50 Hz, rumeur de ville derrière la vitre) + nappe Fa dièse mineur 11
 · 0,3-1,8 l'assiette frotte sur le bois (friction + modes céramiques) · 1,4 note basse « Pas toi »
 · 3,3 clic du variateur + bourdonnement qui descend, la nappe passe en passe-bas (« l'oreille passe en vision de nuit »)
 · 3,75 / 4,15 / 4,55 trois « plocs » de rondelles dans le jus, 4,0-5,2 débordement (glouglou + filet)
 · 5,6 vision de nuit (souffle étouffé) · 8,0-10,0 les aigus de la nappe s'éteignent un à un · SILENCE TOTAL 10,0-10,2
 · 10,2-10,35 vague de relais (« toc » feutrés panoramisés) · 10,35-10,9 « thunk » graves des traits du 190 M · 10,92 sub-boom
 · 11,75 pulsation corail (« cécité ») · 13,45 souffle de partage · 14,2-15,1 l'assiette est repoussée
 · 16,0-16,5 papier gommé lissé sur le verre (frottements secs) + vent froid · 17,2-18,5 bimoteur (dents de scie 85/87 Hz) G → D
 · 18,6 papier décollé + clic de la lampe, l'accord s'ouvre en Ré majeur 9 · 18,65 tampon MYTHE = croquement de carotte
 · 18,8-20,0 rallumage des fenêtres = tintements de verre du proche au lointain · 21,85 signature · 22,4 bouton
 · 24,4-24,9 la carotte se tranche : 6 tics de bois accordés · retour de l'ambiance du début (boucle)."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 25.25; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2910)
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


def tick(t0, f=2400, g=0.05, pan=0.0, dec=90):
    x = ax(0.06); put(np.sin(2 * np.pi * f * x) * np.exp(-x * dec) * np.clip(x / 0.0015, 0, 1), t0, g, pan)


def whoosh(t0, d, lo, hi, g, up=True, pan=0.0):
    x = ax(d); n = R.standard_normal(len(x)); env = (x / d) ** 2 if up else np.exp(-x / d * 4) * np.clip(x / 0.02, 0, 1)
    put(bp(n, lo, hi) * env, t0, g, pan)


# enveloppes de « mondes »
kit = win(-1, 10.0, 0.1, 0.02) + win(13.4, 16.0, 0.3, 0.3) + win(18.6, 26, 0.05, 0.1)       # cuisine
night = win(3.3, 18.62, 0.3, 0.03)                                                              # vision de nuit
w40 = win(16.0, 18.62, 0.3, 0.03)                                                               # 1940
# 1. Lit : frigo (50 Hz + harmoniques, très bas) + rumeur de ville filtrée derrière la vitre
fridge = sum(g * np.sin(2 * np.pi * f * T + R.random() * 6) for f, g in ((50, 1), (100, .5), (150, .25), (200, .12))) * 0.010
city = lp(R.standard_normal(N), 320) * 0.05 * (1 + 0.2 * np.sin(2 * np.pi * T * 0.13))
L += fridge * kit + city * (1 - 0.6 * w40); Rt += np.roll(fridge, 150) * kit + np.roll(city, 977) * (1 - 0.6 * w40)
# 2. Nappe Fa# m11 → Ré majeur 9 à 18,6 ; passe-bas pendant la nuit ; aigus qui s'éteignent un à un (8,0-10,0)
fsm = ((46.25, .45), (92.5, .35), (138.59, .26), (220.0, .2), (329.63, .14), (415.3, .10), (493.88, .08), (659.25, .05))
dmaj = ((36.71, .45), (73.42, .35), (110.0, .26), (185.0, .2), (277.18, .15), (329.63, .12), (440.0, .09), (659.25, .05))
padA = np.zeros(N); padD = np.zeros(N)
for i, (f, g) in enumerate(fsm):
    fade = 1.0 if f < 200 else np.clip(1 - sm((T - (8.0 + 0.4 * (i - 3))) / 0.4), 0, 1) + win(13.4, 18.6, 0.3, 0.05)
    padA += g * np.sin(2 * np.pi * f * T + R.random() * 6) * (0.8 + 0.2 * np.sin(2 * np.pi * T * (0.11 + f / 5000))) * np.clip(fade, 0, 1)
for f, g in dmaj:
    padD += g * np.sin(2 * np.pi * f * T + R.random() * 6) * (0.8 + 0.2 * np.sin(2 * np.pi * T * (0.15 + f / 5000)))
padA_lp = lp(padA, 380); padA_hi = lp(padA, 2600)
pad = (padA_hi * (1 - night) + padA_lp * night * 1.3) * (1 - win(18.6, 26, 0.35, 0.1)) + lp(padD, 3200) * win(18.6, 26, 0.35, 0.1)
pad *= 0.06 * (1 - 0.5 * w40)
L += pad; Rt += np.roll(pad, 330)
# 3. L'assiette frotte sur le bois (0,3-1,8) + modes céramiques ; même geste à 14,2-15,1 ; note basse « Pas toi »
for t0, d in ((0.3, 1.5), (14.2, 0.9)):
    x = ax(d); fr = bp(R.standard_normal(len(x)), 180, 1400) * (np.sin(np.pi * x / d) ** 2) * (0.7 + 0.3 * np.sin(2 * np.pi * x * 11))
    put(fr, t0, 0.10, -0.15)
    for f in (1870, 3130, 4710): put(tone(f, 0.9, 6), t0 + d * 0.15, 0.010, -0.15)
put(tone(46.25, 1.2, 3) + 0.4 * tone(92.5, 1.2, 4), 1.4, 0.22)
# 4. Variateur (3,3) : clic + bourdonnement qui descend
tick(3.3, 3600, 0.10, 0.25, 220); tick(3.315, 1400, 0.06, 0.25, 150)
x = ax(0.9); hum = np.sign(np.sin(2 * np.pi * np.cumsum(120 - 70 * (x / 0.9)) / SR)); put(lp(hum, 1500) * np.exp(-x * 3.5) * 0.4, 3.3, 0.05, 0.2)
# 5. Trois « plocs » dans le jus + débordement
for k, tb in enumerate((3.75 + 0.32, 4.15 + 0.32, 4.55 + 0.32)):
    x = ax(0.22); put(np.sin(2 * np.pi * np.cumsum(420 + 900 * np.exp(-x * 30)) / SR) * np.exp(-x * 22), tb, 0.16, 0.35)
    put(bp(R.standard_normal(len(x)), 800, 4000) * np.exp(-x * 40), tb, 0.05, 0.35)
for k in range(7):
    x = ax(0.12); put(np.sin(2 * np.pi * np.cumsum(260 + 300 * np.exp(-x * 25)) / SR) * np.exp(-x * 30), 4.1 + 0.11 * k + 0.03 * R.random(), 0.06, 0.3)
x = ax(1.2); put(bp(R.standard_normal(len(x)), 1500, 6000) * np.sin(np.pi * x / 1.2) ** 2, 4.3, 0.025, 0.3)
# 6. Vision de nuit (5,6) : souffle étouffé
whoosh(5.55, 0.6, 150, 900, 0.10)
# 7. Approche de la vitre (8,0-10,0) : souffle qui monte, puis SILENCE 10,0-10,2
whoosh(8.0, 2.0, 200, 2500, 0.07)
# 8. Vague de relais (10,2-10,35) : toc feutrés panoramisés
for k in range(26):
    t0 = 10.2 + 0.15 * R.random(); pan = R.uniform(-0.9, 0.9); f = 500 + 900 * R.random()
    x = ax(0.05); put(lp(np.sin(2 * np.pi * f * x) * np.exp(-x * 120), 2500), t0, 0.05, pan)
# 9. « 190 M » écrit trait par trait : thunk grave par glyphe + tics par fenêtre, sub-boom sous le chiffre
gl_t = [10.35, 10.35 + 0.55 * 10 / 58, 10.35 + 0.55 * 25 / 58, 10.35 + 0.55 * 41 / 58]
for i, tg in enumerate(gl_t):
    x = ax(0.35); put(np.sin(2 * np.pi * (55 + 40 * np.exp(-x * 30)) * x) * np.exp(-x * 9), tg, 0.30, -0.5 + i / 3)
for k in range(58): tick(10.35 + 0.55 * k / 58, 900 + 15 * k, 0.03, -0.6 + 1.2 * k / 58, 160)
x = ax(1.4); put(np.sin(2 * np.pi * (34 + 20 * np.exp(-x * 6)) * x) * np.exp(-x * 2.2), 10.92, 0.45)
put(tone(220, 1.0, 3) + 0.5 * tone(329.63, 1.0, 3.5), 10.94, 0.05)
# 10. Pulsation corail (« cécité »)
put(tone(110, 0.9, 3) * (0.6 + 0.4 * np.sin(2 * np.pi * 6 * ax(0.9))), 11.6, 0.10)
# 11. Partage (13,45)
whoosh(13.3, 0.45, 300, 4000, 0.12); put(tone(659.25, 0.5, 7) + 0.5 * tone(987.77, 0.5, 9), 13.5, 0.04)
# 12. 1940 : papier gommé lissé (4 frottements secs), vent froid, bimoteur
for k in range(8):
    x = ax(0.16); put(hp(R.standard_normal(len(x)), 1800) * np.sin(np.pi * x / 0.16) ** 3, 16.02 + 0.08 * (k // 2) + 0.05 * (k % 2), 0.06, -0.3 + 0.2 * (k % 4))
wind = bp(R.standard_normal(N), 300, 1800) * (0.6 + 0.4 * np.sin(2 * np.pi * T * 0.4)) * 0.03 * w40
L += wind; Rt += np.roll(wind, 1203)
pl = win(17.1, 18.6, 0.4, 0.4)
saw = ((T * 85.0) % 1.0 - 0.5) + ((T * 87.0) % 1.0 - 0.5)
eng = lp(saw, 600) * pl * 0.09
pan_t = np.clip((T - 17.2) / 1.3, 0, 1)
L += eng * (1 - pan_t * 0.8); Rt += eng * (0.2 + pan_t * 0.8)
# 13. Retour (18,6) : papier décollé, clic de lampe, tampon = croquement de carotte
x = ax(0.18); put(hp(R.standard_normal(len(x)), 1200) * np.exp(-x * 14), 18.58, 0.12, -0.2)
tick(18.64, 3400, 0.12, 0.2, 220); tick(18.655, 1500, 0.07, 0.2, 160)
crunch = np.zeros(int(0.45 * SR))
for k in range(55):
    c0 = int((0.004 + 0.30 * (k / 55) ** 1.6 + 0.01 * R.random()) * SR); ln = int(0.012 * SR)
    if c0 + ln < len(crunch): crunch[c0:c0 + ln] += R.standard_normal(ln) * np.exp(-np.arange(ln) / (0.002 * SR)) * (1 - k / 70)
crunch = bp(crunch, 1500, 6000)
crunch[:int(0.004 * SR)] += R.standard_normal(int(0.004 * SR)) * 1.5
put(crunch, 18.65, 0.30)
x = ax(0.5); put(np.sin(2 * np.pi * (60 + 40 * np.exp(-x * 30)) * x) * np.exp(-x * 9), 18.65, 0.25)
# 14. Rallumage des fenêtres : tintements de verre, du proche au lointain
for k in range(16):
    t0 = 18.8 + 1.2 * (k / 16) + 0.03 * R.random(); f = 1760 * 2 ** (R.integers(0, 7) * 2 / 12)
    put(tone(f, 0.8, 7) + 0.3 * tone(f * 2.76, 0.8, 12), t0, 0.03 * (1 - 0.6 * k / 16), R.uniform(-0.8, 0.8))
# 15. Signature (21,85) + bouton (22,4)
for kk in range(10): put(tone(1975.5 * 2 ** (kk / 12 * 1.2), 0.7, 5), 21.9 + kk * 0.05, 0.016, (kk / 5) - 1)
put(sum(g * tone(1174.66 * k, 2.0, 2.6 * (1 + 0.4 * i)) for i, (k, g) in enumerate(((1, 1), (2, .25), (3, .08)))), 22.3, 0.07)
put(tone(1568, 0.08, 60), 22.42, 0.06)
# 16. La carotte se tranche (24,4-24,9) : 6 tics de bois accordés
for k, tb in enumerate(np.linspace(24.45, 24.8, 6)):
    f = 740 * 2 ** ([0, 2, 4, 7, 9, 12][k] / 12)
    x = ax(0.08); put(lp(np.sin(2 * np.pi * f * x) * np.exp(-x * 70) + 0.3 * R.standard_normal(len(x)) * np.exp(-x * 200), 5000), tb, 0.08, -0.2 + 0.08 * k)
whoosh(24.35, 0.3, 300, 3000, 0.05)

# Mixage : réverbération courte (cuisine), SILENCE 10,0-10,2
mixL, mixR = L.copy(), Rt.copy()
for dl, g in ((0.023, .14), (0.037, .12), (0.061, .09), (0.097, .06), (0.151, .04), (0.22, .025)):
    k = int(dl * SR); mixL[k:] += mixR[:-k] * g; mixR[k:] += mixL[:-k] * g
gate = 1 - win(10.0, 10.2, 0.015, 0.005) * 0.995
out = np.stack([mixL * gate, mixR * gate], 1)
out *= np.clip(T / 0.01, 0, 1)[:, None] * np.clip((DUR - T) / 0.05, 0, 1)[:, None]


def limit(x, ceil):
    pkv = maximum_filter1d(np.max(np.abs(x), 1), int(0.006 * SR))
    gr = np.minimum(1.0, ceil / np.maximum(pkv, 1e-9))
    gr = np.minimum(gr, uniform_filter1d(gr, int(0.004 * SR)))
    gr = uniform_filter1d(gr, int(0.003 * SR))
    return x * gr[:, None]


target_rms = float(sys.argv[2]) if len(sys.argv) > 2 else -17.0
ceil = 10 ** (-3.5 / 20)
for _ in range(8):
    rms = np.sqrt(np.mean(out ** 2)); out *= 10 ** (target_rms / 20) / rms
    out = limit(out, ceil * 0.97)
out = np.clip(out, -ceil, ceil) * gate[:, None]
print(f"pic {20*np.log10(np.max(np.abs(out))):.2f} dBFS, RMS {20*np.log10(np.sqrt(np.mean(out**2))):.2f} dBFS")
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
