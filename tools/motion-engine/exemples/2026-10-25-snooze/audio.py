#!/usr/bin/env python3
"""Son original — « Le chiffre qui pique · ép. 3 : le snooze ». Synthèse procédurale, seed fixe, 21,4 s.
Usage : python3 audio.py sortie.wav [rms_cible_dBFS]
Temps calés sur index.html :
 sonnerie FM « verre » originale (mi6-si5-ré6-si5, 110 ms, cycle 0,91 s) 0-1,50 puis coupure nette ; reprise 20,86 (boucle)
 · 1,50 tok de vitre + onde · 1,62 bulle grave (le bloc traverse la vitre) · 1,95 tok sur tissu + 2,2 rebond
 · 2,9 clac doux du tiroir · 3,0 un oiseau lointain · 3,4 / 3,8 / 4,2 tapotements + règle-xylophone do-mi-sol (notes de pose 3,58 / 4,15 / 4,55)
 · 4,55 tic-tac d'attente → 5,6 · 5,6-6,6 montée filtrée · 6,6 « schhk » de lame + clic + note du 1er bloc étouffée, désaccordée (−40 cents)
 · 7,8 souffle de grue · 8,4 verre qui se fend · 8,8 ding cyan · 10,28 pli de verre · 10,5 swoosh de l'avion · 11,0 piqué
 · 11,5 / 11,85 / 12,2 tapotements nerveux + vibreur · SILENCE 12,6-12,9 · souffle grave de nuit + « pff » 14,3 / 14,75 / 15,2
 · 15,6 retour du matin · 16,35 pop du marque-page · 16,9-17,3 quatre « plongeons » dans l'écran · 17,6 clac du tiroir
 · 18,0-20,3 tic-tac du minuteur · 18,4 / 20,4 bascule de la pastille · 19,4 ding doux + scintillement doré de la signature.
Nappe la majeur 9 très basse, coupée pendant la nuit (12,6-15,6)."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 21.4; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(2510)
L = np.zeros(N); Rt = np.zeros(N)


def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def win(a, b, fa=0.2, fb=0.2): return np.clip((T - a) / fa, 0, 1) * np.clip((b - T) / fb, 0, 1)
def ax(d): return np.arange(int(d * SR)) / SR


def put(sig, t0, g=1.0, pan=0.0):
    i = int(round(t0 * SR))
    if i >= N: return
    s = sig[:N - i] * g
    L[i:i + len(s)] += s * (1 - max(pan, 0)); Rt[i:i + len(s)] += s * (1 + min(pan, 0))


def tone(f, d, dec, ph=0.0):
    x = ax(d); return np.sin(2 * np.pi * f * x + ph) * np.exp(-x * dec)


def bell(f, d, dec, parts=((1, 1), (2.76, .35), (5.4, .15), (8.93, .06))):
    return sum(g * tone(f * k, d, dec * (1 + 0.4 * i)) for i, (k, g) in enumerate(parts))


def glass(f, d=1.4, dec=3.5):  # verre frappé (partiels inharmoniques) pour la règle-xylophone
    x = ax(d); att = np.clip(x / 0.002, 0, 1)
    s = (np.sin(2 * np.pi * f * x) * np.exp(-x * dec) + 0.5 * np.sin(2 * np.pi * f * 2.32 * x) * np.exp(-x * dec * 1.8)
         + 0.25 * np.sin(2 * np.pi * f * 4.25 * x) * np.exp(-x * dec * 3) + 0.15 * np.sin(2 * np.pi * f * 6.63 * x) * np.exp(-x * dec * 5))
    return s * att


def fm(f, d, ratio=3.5, i0=4.0, i1=0.5, dec_i=0.12, cents=0.0):
    x = ax(d); f = f * 2 ** (cents / 1200)
    idx = i1 + (i0 - i1) * np.exp(-x / dec_i * 3)
    env = np.clip(x / 0.003, 0, 1) * np.clip((d - x) / 0.02, 0, 1) * np.exp(-x * 4)
    return np.sin(2 * np.pi * f * x + idx * np.sin(2 * np.pi * f * ratio * x)) * env


def thud(t0, g=1.0, f0=90):
    x = ax(0.35); put(np.sin(2 * np.pi * (f0 + 60 * np.exp(-x * 40)) * x) * np.exp(-x * 14) + 0.5 * lp(R.standard_normal(len(x)), 900) * np.exp(-x * 30), t0, g)


def tap(t0, g=0.25, pan=0.1):  # pulpe du doigt sur la vitre
    x = ax(0.06); put(bp(R.standard_normal(len(x)), 900, 4500) * np.exp(-x * 110) + 0.6 * np.sin(2 * np.pi * 320 * x) * np.exp(-x * 90), t0, g, pan)


def tick(t0, hi=True, g=0.18, pan=-0.3):
    x = ax(0.06)
    a = bp(R.standard_normal(len(x)), 1800 if hi else 1300, 5200 if hi else 4000) * np.exp(-x * 130)
    a += 0.4 * np.sin(2 * np.pi * (2100 if hi else 1650) * x) * np.exp(-x * 100)
    put(a, t0, g, pan)


def whoosh(t0, d, g, lo=300, hi=5000, pan=0.0):
    x = ax(d); put(bp(R.standard_normal(len(x)), lo, hi) * np.sin(np.pi * x / d) ** 2, t0, g, pan)


# 1. Ambiance de chambre au matin (souffle de couette, pièce) — audible tout du long sauf le silence 12,6-12,9
room = lp(R.standard_normal(N), 1100) * 0.010 + lp(R.standard_normal(N), 200) * 0.010
L += room; Rt += np.roll(room, 417)

# 2. Sonnerie originale (FM « verre », 2 voix désaccordées ±6 cents) : 0 → 1,50 (coupure nette) et 20,86 → fin
MOTIF = (1318.5, 987.77, 1174.66, 987.77)
def ring(t_start, t_stop):
    t = t_start
    while t < t_stop:
        for j, f in enumerate(MOTIF):
            tn = t + j * 0.18
            if tn >= t_stop: break
            d = min(0.11 + 0.25, t_stop - tn)
            for c, pan in ((-6, -0.35), (6, 0.35)):
                put(fm(f, d, cents=c), tn, 0.2, pan)
        t += 0.91
ring(0.0, 1.50); ring(20.86, DUR)

# 3. 1,50 : tok de vitre + onde (glissando descendant) ; 1,62 : bulle grave ; 1,95 : tok sur tissu ; 2,2 rebond
x = ax(0.12); put(bp(R.standard_normal(len(x)), 1500, 7000) * np.exp(-x * 90) * 0.6 + glass(2600, 0.5, 12)[:len(x)] * 0.6, 1.50, 0.55)
x = ax(0.5); put(np.sin(2 * np.pi * np.cumsum(900 - 600 * x / 0.5) / SR) * np.exp(-x * 7) * 0.25, 1.52, 1.0, 0.1)
x = ax(0.35); put(np.sin(2 * np.pi * np.cumsum(120 + 380 * (x / 0.35) ** 0.6) / SR) * np.sin(np.pi * x / 0.35) * 0.55, 1.60)
thud(1.95, 0.55, 75); thud(2.22, 0.25, 85)

# 4. 2,9 : clac doux du tiroir (glissement + butée) ; 3,0 : un oiseau lointain (une fois)
whoosh(2.86, 0.32, 0.12, 400, 3000, 0.4)
x = ax(0.08); put(bp(R.standard_normal(len(x)), 600, 3500) * np.exp(-x * 80) + 0.5 * np.sin(2 * np.pi * 180 * x) * np.exp(-x * 60), 3.25, 0.35, 0.4)
for kk, t0 in enumerate((3.05, 3.17, 3.26)):
    x = ax(0.09); f = 3600 + 1500 * np.sin(np.pi * x / 0.09) - 400 * kk
    put(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * x / 0.09) ** 2, t0, 0.03, -0.7)

# 5. Appuis 3,4 / 3,8 / 4,2 (tapotement + petite onde) ; règle-xylophone : do6 - mi6 - sol6 à la pose de chaque bloc
for t0 in (3.4, 3.8, 4.2):
    tap(t0, 0.32)
    x = ax(0.3); put(np.sin(2 * np.pi * np.cumsum(700 - 400 * x / 0.3) / SR) * np.exp(-x * 10) * 0.12, t0 + 0.02, 1.0, 0.0)
for t0, f in ((3.58, 1046.5), (4.15, 1318.5), (4.55, 1568.0)):
    put(glass(f), t0, 0.22, 0.35)
for i in range(5):  # graduation 30 qui s'allume : petit scintillement
    put(tone(3136 * 2 ** (i / 12 * 2), 0.5, 7), 4.6 + i * 0.04, 0.02, 0.5 - i * 0.2)

# 6. Tic-tac d'attente (la devinette) 4,55 → 5,6
for kk, t0 in enumerate(np.arange(4.6, 5.6, 0.25)):
    tick(t0, kk % 2 == 0, 0.16)

# 7. 5,6-6,6 : montée (nappe filtrée qui s'ouvre + rouleau du compteur) ; 6,6 : schhk + clic + note étouffée désaccordée
d = 1.0; x = ax(d); k = x / d
riser = np.zeros(len(x)); seg = int(0.02 * SR); src = R.standard_normal(len(x))
for i in range(0, len(x), seg):
    fc = 300 + 4200 * k[i] ** 2
    riser[i:i + seg] = bp(src[max(0, i - 3 * seg):i + seg], fc * 0.8, fc * 1.25)[-len(riser[i:i + seg]):]
riser += 0.3 * np.sin(2 * np.pi * np.cumsum(220 + 440 * k ** 2) / SR)
put(riser * k ** 1.5 * 0.35, 5.6, 1.0, 0.0)
for kk in range(6):  # crans du rouleau 0 → 6
    tick(5.6 + 1.0 * (1 - (1 - (kk + 1) / 6) ** (1 / 3)) - 0.03, True, 0.08, 0.2)
x = ax(0.22); put(hp(R.standard_normal(len(x)), 2500) * np.exp(-x * 18) * (x / 0.22 < 1), 6.55, 0.35, -0.2)
x = ax(0.04); put(bp(R.standard_normal(len(x)), 2000, 9000) * np.exp(-x * 200), 6.6, 0.5)
put(lp(glass(1046.5 * 2 ** (-40 / 1200), 1.2, 9), 1400), 6.62, 0.45, -0.3)
thud(6.6, 0.3, 60)

# 8. 7,8 : souffle de grue ; 8,4 : verre qui se fend (impact grave + craquelures) ; 8,8 : ding cyan
whoosh(7.75, 0.6, 0.16, 250, 3500, -0.2)
thud(8.4, 0.5, 55)
crk = np.zeros(int(0.35 * SR))
for i in range(30):
    j = int(R.uniform(0, len(crk) - 500)); crk[j:j + 400] += R.standard_normal(400) * np.exp(-np.arange(400) / 50) * R.uniform(0.3, 1)
put(hp(crk, 3000) * 0.3, 8.4, 1.0, -0.3)
for i in range(8):
    x = ax(0.05); put(glass(R.uniform(3000, 6000), 0.4, 20)[:len(x)] * np.exp(-x * 40), 8.55 + i * 0.06, 0.05, R.uniform(-0.6, 0.6))
put(bell(2093.0, 2.0, 2.4), 8.8, 0.16, 0.25); put(bell(3136.0, 1.5, 3.2), 8.805, 0.05, 0.3)

# 9. 10,28 : pli de verre (2 crans) ; 10,5 : swoosh de l'avion vers la droite ; 11,0 : piqué
for t0 in (10.3, 10.42):
    x = ax(0.05); put(bp(R.standard_normal(len(x)), 2500, 8000) * np.exp(-x * 120), t0, 0.22, 0.4)
d = 0.55; x = ax(d); sw = bp(R.standard_normal(len(x)), 600, 6000) * np.sin(np.pi * x / d) ** 2
put(sw * 0.3, 10.5, 1.0, 0.1); put(np.roll(sw, 2000) * 0.22, 10.55, 1.0, 0.8)
whoosh(10.98, 0.42, 0.28, 200, 4000, 0.0)

# 10. Tapotements nerveux + vibreur du bouton qui tremble (11,35 → 12,55)
for t0 in (11.5, 11.85, 12.2, 12.38):
    tap(t0, 0.3, -0.1)
d = 1.2; x = ax(d); vib = lp(np.sign(np.sin(2 * np.pi * 150 * x)) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 3.0 * x))), 500)
put(vib * 0.07 * np.clip(x / 0.1, 0, 1) * np.clip((d - x) / 0.1, 0, 1), 11.35)

# 11. Nuit : souffle grave (12,9 → 15,6) ; trois « pff » quand les blocs partent en fumée
x = ax(2.7); put(lp(R.standard_normal(len(x)), 220) * np.sin(np.pi * x / 2.7) ** 0.7 * 0.22 + np.sin(2 * np.pi * 48 * x) * 0.05 * np.sin(np.pi * x / 2.7), 12.9)
for t0 in (14.31, 14.76, 15.21):
    x = ax(0.45); put(bp(R.standard_normal(len(x)), 300, 2500) * np.exp(-x * 7) * np.clip(x / 0.02, 0, 1), t0, 0.32, R.uniform(-0.3, 0.3))
# batterie faible : deux bips graves discrets
for t0 in (13.1, 13.95):
    x = ax(0.12); put(np.sin(2 * np.pi * 440 * x) * np.clip(x / 0.005, 0, 1) * np.clip((0.12 - x) / 0.02, 0, 1), t0, 0.05, 0.0)

# 12. 15,6 : retour du matin (scintillement montant) ; 16,35 : pop du marque-page ; 16,9-17,3 : plongeons ; 17,6 : clac
for i in range(7):
    put(tone(1568 * 2 ** (i / 12 * 2), 0.6, 6), 15.62 + i * 0.05, 0.02, -0.6 + i * 0.2)
x = ax(0.15); put(np.sin(2 * np.pi * (300 + 500 * np.exp(-x * 60)) * x) * np.exp(-x * 30) * 0.5, 16.35, 1.0, 0.3)
for t0, f in ((17.0, 1568.0), (17.14, 1318.5), (17.28, 1174.7), (17.4, 1046.5)):
    x = ax(0.35); put(np.sin(2 * np.pi * np.cumsum(f * 0.5 * (1 - 0.5 * x / 0.35)) / SR) * np.exp(-x * 9) * 0.25 + glass(f, 0.6, 8)[:len(x)] * 0.1, t0, 1.0, 0.0)
x = ax(0.08); put(bp(R.standard_normal(len(x)), 600, 3500) * np.exp(-x * 80) + 0.5 * np.sin(2 * np.pi * 160 * x) * np.exp(-x * 60), 17.6, 0.35, 0.4)

# 13. Minuteur : tic-tac 18,0 → 20,3 ; bascules de pastille 18,4 / 20,4 ; ding doux 19,4 ; signature 19,8
for kk, t0 in enumerate(np.arange(18.05, 20.3, 0.25)):
    tick(t0, kk % 2 == 0, 0.14, 0.2)
for t0 in (18.4, 18.53, 20.4, 20.5):
    x = ax(0.04); put(bp(R.standard_normal(len(x)), 1200, 5000) * np.exp(-x * 150), t0, 0.28, 0.1)
put(bell(1760.0, 2.0, 2.8, ((1, 1), (2, .25), (3, .08))), 19.4, 0.13, 0.0)
for kk in range(10):
    put(tone(2093 * 2 ** (kk / 12 * 1.2), 0.7, 5), 19.8 + kk * 0.045, 0.02, (kk / 5) - 1)

# 14. Nappe claire (la majeur 9) très basse : entre à 1,9, éteinte pendant la nuit, revient à 15,7, s'efface avant la sonnerie
pad = np.zeros(N)
for f in (110.0, 138.59, 164.81, 207.65, 246.94):
    for det in (0.997, 1.003):
        pad += np.sin(2 * np.pi * f * det * T) + 0.25 * np.sin(4 * np.pi * f * det * T)
padx = lp(pad, 1200) * 0.012 * (win(1.9, 12.6, 0.8, 0.05) + win(15.7, 20.7, 0.8, 0.3))
L += padx; Rt += np.roll(padx, 700)

# Mix : silence 12,6-12,9 (gel) ; réverbération courte ; niveau ≈ −15 LUFS ; pic −1,5 dBFS
gate = 1 - win(12.6, 12.9, 0.004, 0.02) * 0.985
mixL, mixR = L.copy(), Rt.copy()
for dl, g in ((0.029, .20), (0.043, .16), (0.067, .12), (0.103, .08), (0.157, .05), (0.23, .03)):
    k = int(dl * SR); mixL[k:] += Rt[:-k] * g; mixR[k:] += L[:-k] * g
out = np.stack([mixL * gate, mixR * gate], 1)
out *= np.clip(T / 0.003, 0, 1)[:, None] * np.clip((DUR - T) / 0.003, 0, 1)[:, None]


def limit(x, ceil):
    pkv = maximum_filter1d(np.max(np.abs(x), 1), int(0.006 * SR))
    gr = np.minimum(1.0, ceil / np.maximum(pkv, 1e-9))
    gr = np.minimum(gr, uniform_filter1d(gr, int(0.004 * SR)))
    gr = uniform_filter1d(gr, int(0.003 * SR))
    return x * gr[:, None]


target_rms = float(sys.argv[2]) if len(sys.argv) > 2 else -17.4
ceil = 10 ** (-3.5 / 20)   # marge pour le dépassement de l’encodage AAC
for _ in range(8):
    rms = np.sqrt(np.mean(out ** 2)); out *= 10 ** (target_rms / 20) / rms
    out = limit(out, ceil * 0.97)
out = np.clip(out, -ceil, ceil) * gate[:, None]
print(f"pic {20*np.log10(np.max(np.abs(out))):.2f} dBFS, RMS {20*np.log10(np.sqrt(np.mean(out**2))):.2f} dBFS")
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
