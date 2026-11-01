#!/usr/bin/env python3
"""Son original — « Mythe ou science ? ép. 8 : un chewing-gum avalé reste 7 ans dans le ventre ? ».
Synthèse procédurale, graine fixe, sans voix ni musique sous droits. Usage : python3 audio.py sortie.wav [rms_cible_dBFS]
Temps calés sur index.html (script v3) :
 lit = classe vide à 16 h 20 (radiateur, horloge à 1 Hz, rumeur de cour sans voix)
 0,15 / 0,9 mastication humide · froissements du papier argenté · 1,8 « Non. » = coup de craie
 3,45-4,9 arômes = scintillements menthe · souffle descendant (le gum devient gris)
 4,6-5,8 gonflement caoutchouteux, l'horloge accélère 1 → 4 tics/s · 5,8-6,0 SILENCE TOTAL
 6,0 POP étiré et grave (ralenti) → 6,3 claque au temps réel · 6,3-7,0 nuée de 2 555 feuilles G → D
 7 tocs de craie (les années) · 7,1 trois notes de marimba (cases roses) · 9,2 tampon de prof
 10,6-11,8 plongée sous la table, tout passe en passe-bas jusqu'à 18,0 · boules qui pulsent (squelchs doux)
 13,3-14,9 les boules tombent (plocs collants), fusion visqueuse · 15,0-16,8 4 pièces roulent et sont avalées (tintement étouffé)
 18,0 remontée (le filtre s'ouvre) · 18,3-19,0 quatre plis du papier · 19,42 pichenette · 20,45 corbeille
 21,6 sonnerie de fin de cours · 21,7-22,4 le tableau s'efface · 22,2 bouton · 22,4 signature
 24,4-25,0 nouveau papier qui se déplie + feuille « 7 ANS » qui se rabat, raccord avec 0 s."""
import sys, wave
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.ndimage import maximum_filter1d, uniform_filter1d

SR = 44100; DUR = 25.25; N = int(SR * DUR); T = np.arange(N) / SR
R = np.random.default_rng(802)
L = np.zeros(N); Rt = np.zeros(N)          # monde « au-dessus de la table »
UL = np.zeros(N); UR = np.zeros(N)         # monde « sous la table » (passe-bas ensuite)


def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def sm(x): x = np.clip(x, 0, 1); return x * x * (3 - 2 * x)
def win(a, b, fa=0.2, fb=0.2): return sm((T - a) / fa) * sm((b - T) / fb)
def ax(d): return np.arange(int(d * SR)) / SR


def put(sig, t0, g=1.0, pan=0.0, under=False):
    i = int(round(t0 * SR))
    if i >= N or i + len(sig) <= 0: return
    s = sig * g
    if i < 0: s = s[-i:]; i = 0
    s = s[:N - i]
    A, B = (UL, UR) if under else (L, Rt)
    A[i:i + len(s)] += s * (1 - max(pan, 0)); B[i:i + len(s)] += s * (1 + min(pan, 0))


def tone(f, d, dec, ph=0.0):
    x = ax(d); return np.sin(2 * np.pi * f * x + ph) * np.exp(-x * dec)


def noise(d): return R.standard_normal(int(d * SR))


def squelch(t0, g=0.12, pan=0.0, under=False, f1=420, f2=950):
    x = ax(0.22); n = noise(0.22)
    env = np.clip(x / 0.012, 0, 1) * np.exp(-x * 16)
    body = bp(n, f1 * 0.7, f1 * 1.4) + 0.6 * bp(n, f2 * 0.8, f2 * 1.25)
    body += 0.5 * np.sin(2 * np.pi * (f1 * 0.5 + 300 * x) * x) * np.exp(-x * 25)
    put(body * env, t0, g, pan, under)


def crinkle(t0, d, g=0.06, pan=0.0, dens=180):
    s = np.zeros(int(d * SR))
    for _ in range(int(dens * d)):
        c = int(R.random() * (len(s) - 300)); ln = int((0.0015 + 0.004 * R.random()) * SR)
        s[c:c + ln] += R.standard_normal(ln) * np.exp(-np.arange(ln) / (0.0008 * SR)) * R.uniform(0.3, 1)
    s = bp(s, 2800, 9500) * np.sin(np.pi * np.arange(len(s)) / len(s)) ** 0.5
    put(s, t0, g, pan)


def tick(t0, g=0.05, pan=0.25, under=False):
    x = ax(0.05); s = (np.sin(2 * np.pi * 2900 * x) * np.exp(-x * 160) + 0.5 * R.standard_normal(len(x)) * np.exp(-x * 400))
    put(hp(s, 1200), t0, g, pan, under)


def marimba(f, t0, g=0.08, pan=0.0):
    x = ax(1.2); s = np.sin(2 * np.pi * f * x) * np.exp(-x * 5) + 0.25 * np.sin(2 * np.pi * f * 3.93 * x) * np.exp(-x * 18) \
        + 0.08 * np.sin(2 * np.pi * f * 9.2 * x) * np.exp(-x * 40)
    put(s * np.clip(x / 0.002, 0, 1), t0, g, pan)


def whoosh(t0, d, lo, hi, g, up=True, pan=0.0, under=False):
    x = ax(d); n = noise(d); env = np.sin(np.pi * x / d) ** 2 if up else np.exp(-x / d * 4) * np.clip(x / 0.02, 0, 1)
    put(bp(n, lo, hi) * env, t0, g, pan, under)


# ---------- 1. Lit : radiateur, rumeur de cour, horloge ----------
room = win(-1, 10.9, 0.1, 0.6) + win(17.9, 27, 0.5, 0.1)
underK = win(10.6, 18.3, 0.8, 0.4)
rad = lp(R.standard_normal(N), 180) * 0.05 + 0.006 * np.sin(2 * np.pi * 50 * T) + 0.004 * np.sin(2 * np.pi * 100 * T)
yard = bp(R.standard_normal(N), 350, 1400) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.13 * T) ** 2) * 0.012
bed = rad + yard
L += bed * room; Rt += np.roll(bed, 701) * room
UL += bed * underK * 1.2; UR += np.roll(bed, 701) * underK * 1.2
# horloge : 1 Hz, accélère pendant la bulle (4,6 → 5,8), muette pendant le silence et sous la table
tt = 0.5
while tt < 25.2:
    if 5.8 <= tt < 6.6: tt = 6.6; continue
    under = 10.9 <= tt < 18.2
    tick(tt, 0.035 if not under else 0.03, 0.3, under)
    rate = 1.0 + 3.0 * float(sm((tt - 4.6) / 1.2)) if 4.6 <= tt < 5.8 else 1.0
    tt += 1.0 / rate
# ---------- 2. Image 0 : mastication + papier argenté ----------
squelch(0.12, 0.14, -0.15); squelch(0.85, 0.12, -0.2, f1=380, f2=880)
crinkle(0.0, 1.5, 0.035, -0.2, 90)
marimba(622.25, 0.30, 0.05, -0.2); marimba(783.99, 0.55, 0.045, 0.0); marimba(932.33, 0.80, 0.04, 0.2); marimba(1046.5, 1.05, 0.04, 0.1)
# 1,8 « Non. » : coup de craie
x = ax(0.25); chalk = hp(R.standard_normal(len(x)), 2500) * np.exp(-x * 30) * (1 + 0.5 * np.sin(2 * np.pi * 70 * x)) + np.sin(2 * np.pi * 260 * x) * np.exp(-x * 60)
put(chalk, 1.8, 0.22, 0.05)
marimba(311.13, 2.05, 0.06)
# ---------- 3. Arômes : scintillements menthe + souffle descendant ----------
for k in range(42):
    t0 = 3.45 + 1.35 * R.random(); f = R.uniform(4000, 7200)
    put(tone(f, 0.12, 40) * np.clip(ax(0.12) / 0.003, 0, 1), t0, 0.022, R.uniform(-0.8, 0.8))
x = ax(1.3); put(bp(noise(1.3), 300, 2500) * np.sin(np.pi * x / 1.3) ** 2 * np.exp(-x * 0.8), 3.75, 0.05, 0.0)
x = ax(1.3); put(np.sin(2 * np.pi * (520 - 300 * x / 1.3) * x) * np.sin(np.pi * x / 1.3) ** 2, 3.75, 0.012)
# ---------- 4. Gonflement (4,6-5,8) : étirement caoutchouteux ----------
d = 1.2; x = ax(d); ph = 2 * np.pi * np.cumsum(70 + 40 * x / d + 6 * np.sin(2 * np.pi * 9 * x)) / SR
creak = np.sign(np.sin(ph)) * 0.3 + np.sin(ph)
stretch = lp(creak, 900) * (x / d) ** 1.5 * 0.5 + (bp(noise(d), 600, 1800) * (1 - x / d) + bp(noise(d), 1500, 4200) * (x / d)) * (x / d) ** 2 * 0.6
put(stretch, 4.6, 0.10)
# ---------- 5. 6,0 POP étiré (ralenti) puis claque à 6,3 ----------
x = ax(0.32); slow = np.sin(2 * np.pi * np.cumsum(90 - 30 * x / 0.32) / SR) * np.clip(x / 0.03, 0, 1) * (0.4 + 0.6 * x / 0.32)
slow += lp(R.standard_normal(len(x)), 400) * 0.6 * (x / 0.32)
put(slow, 6.0, 0.16)
x = ax(0.5); snap = R.standard_normal(len(x)) * np.exp(-x * 900) * 2.0 + np.sin(2 * np.pi * 180 * x) * np.exp(-x * 22) + 0.6 * np.sin(2 * np.pi * 95 * x) * np.exp(-x * 12)
put(snap, 6.30, 0.42)
# nuée de papier, panoramique G → D
d = 0.85; s = np.zeros(int(d * SR))
for _ in range(900):
    c = int(R.random() ** 0.8 * (len(s) - 2000)); ln = int((0.004 + 0.02 * R.random()) * SR)
    s[c:c + ln] += R.standard_normal(ln) * np.hanning(ln) * R.uniform(0.2, 1)
s = bp(s, 1200, 7000) * np.exp(-np.arange(len(s)) / SR * 2.0)
pan_t = np.linspace(-0.9, 0.9, len(s))
i0 = int(6.32 * SR); L[i0:i0 + len(s)] += s * 0.10 * (1 - np.clip(pan_t, 0, 1)); Rt[i0:i0 + len(s)] += s * 0.10 * (1 + np.clip(pan_t, -1, 0))
# 7 tocs de craie (les 7 ans)
for k in range(7):
    x = ax(0.12); put(lp(R.standard_normal(len(x)) * np.exp(-x * 120) + np.sin(2 * np.pi * 900 * x) * np.exp(-x * 80), 5000), 6.98 + k * 0.05, 0.10, -0.6 + 0.2 * k)
for k, f in enumerate((1244.5, 1568.0, 1864.7)): marimba(f, 7.12 + k * 0.11, 0.06, -0.5 + 0.15 * k)
# 9,2 tampon de prof
x = ax(0.4); stamp = np.sin(2 * np.pi * 75 * x) * np.exp(-x * 18) + lp(R.standard_normal(len(x)), 1200) * np.exp(-x * 50) * 0.8
put(stamp, 9.2, 0.38)
# ---------- 6. Plongée sous la table ----------
whoosh(10.55, 1.25, 150, 1600, 0.10, True, 0.0)
for k in range(int((13.2 - 11.8) * 0.85) + 2):
    t0 = 11.8 + k / 0.85
    if t0 < 13.25: squelch(t0, 0.05, 0.0, True, 300, 650)
# chutes (plocs collants) puis fusion visqueuse
for k in range(16):
    t0 = 13.62 + 1.3 * (k / 15) ** 0.9 + 0.03 * R.random(); squelch(t0, 0.07, R.uniform(-0.5, 0.5), True, 260, 600)
d = 1.6; x = ax(d); visc = lp(np.sign(np.sin(2 * np.pi * np.cumsum(40 + 25 * np.sin(2 * np.pi * 0.7 * x)) / SR)), 400) * np.sin(np.pi * x / d)
put(visc, 13.9, 0.05, 0.0, True)
x = ax(0.6); put(np.sin(2 * np.pi * (55 + 30 * np.exp(-x * 10)) * x) * np.exp(-x * 7), 15.4, 0.30, 0.0, True)
# 4 pièces : roulement métallique puis tintement étouffé, avalées
for i in range(4):
    ta = 15.62 + 0.40 * i; t0 = ta - 0.62
    put(tone(3200, 0.25, 30) + 0.5 * tone(5400, 0.25, 45), t0, 0.05, 0.35, True)
    d = 0.6; x = ax(d); roll = bp(noise(d), 2500, 6000) * (0.5 + 0.5 * np.sin(2 * np.pi * (14 + 10 * x) * x)) * 0.5
    put(roll, t0 + 0.02, 0.05, 0.3 - 0.15 * (x[0]), True)
    x = ax(0.35); clink = (np.sin(2 * np.pi * 2650 * x) + 0.6 * np.sin(2 * np.pi * 4410 * x)) * np.exp(-x * 14) * np.where(x < 0.07, 1.0, np.exp(-(x - 0.07) * 90))
    put(clink, ta, 0.10, 0.1, True); squelch(ta + 0.05, 0.08, 0.0, True, 220, 520)
# ---------- 7. Remontée, papier qui se replie, pichenette, corbeille ----------
whoosh(17.95, 0.8, 200, 2400, 0.08)
for i in range(4): crinkle(18.30 + i * 0.22, 0.24, 0.07, -0.25 + 0.1 * i, 400)
x = ax(0.3); put(np.sin(2 * np.pi * (240 + 180 * np.exp(-x * 9)) * x) * np.exp(-x * 14), 19.30, 0.07)
whoosh(19.40, 0.5, 900, 5000, 0.10, False, -0.1)
d = 1.0; x = ax(d); put(bp(noise(d), 500, 3000) * np.sin(np.pi * x / d) ** 2, 19.45, 0.03, 0.2)
x = ax(0.6); thunk = np.sin(2 * np.pi * 180 * x) * np.exp(-x * 14) + 0.5 * np.sin(2 * np.pi * 523 * x) * np.exp(-x * 9) + 0.3 * np.sin(2 * np.pi * 1210 * x) * np.exp(-x * 11) \
    + R.standard_normal(len(x)) * np.exp(-x * 120) * 0.5
put(thunk, 20.45, 0.22, 0.35)
# ---------- 8. Sonnerie de fin de cours (cloche électrique) ----------
d = 1.25; x = ax(d); hammer = (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 21 * x))) * 0.7 + 0.3
bell = sum(a * np.sin(2 * np.pi * 1180 * k * x) for k, a in ((1, 1.0), (2.76, 0.45), (5.4, 0.2), (8.9, 0.08)))
bell = lp(bell * hammer, 6000) * np.clip(x / 0.01, 0, 1) * np.clip((d - x) / 0.25, 0, 1)
put(bell, 21.60, 0.11, 0.3); put(np.roll(bell, 900), 21.60, 0.05, -0.4)
# le tableau s'efface
# (le tableau est effacé hors champ pendant la séquence sous la table)
put(tone(783.99, 0.1, 50), 22.2, 0.05)
for kk in range(10): put(tone(1567.98 * 2 ** (kk / 12 * 1.2), 0.7, 5), 22.42 + kk * 0.05, 0.016, (kk / 5) - 1)
marimba(622.25, 22.45, 0.05); marimba(932.33, 22.62, 0.045); marimba(1244.5, 22.80, 0.04)
# ---------- 9. Boucle : le papier argenté se déplie, la feuille se rabat ----------
squelch(24.42, 0.05, -0.1)
crinkle(24.55, 0.42, 0.05, -0.2, 300)
x = ax(0.18); put(bp(R.standard_normal(len(x)), 600, 3500) * np.sin(np.pi * x / 0.18) ** 2, 24.62, 0.06, 0.3)

# ---------- Mixage ----------
# sous la table : passe-bas
cut = lp(lp(UL, 700), 900), lp(lp(UR, 700), 900)
mixL = L + cut[0] * 1.6; mixR = Rt + cut[1] * 1.6
for dl, g in ((0.019, .12), (0.031, .10), (0.053, .08), (0.087, .06), (0.13, .045), (0.19, .03), (0.27, .02)):
    k = int(dl * SR); mixL[k:] += mixR[:-k] * g; mixR[k:] += mixL[:-k] * g
gate = 1 - win(5.8, 6.0, 0.012, 0.004) * 0.998
out = np.stack([mixL * gate, mixR * gate], 1)
out *= np.clip(T / 0.01, 0, 1)[:, None] * np.clip((DUR - T) / 0.05, 0, 1)[:, None]


def limit(x, ceil):
    pkv = maximum_filter1d(np.max(np.abs(x), 1), int(0.006 * SR))
    gr = np.minimum(1.0, ceil / np.maximum(pkv, 1e-9))
    gr = np.minimum(gr, uniform_filter1d(gr, int(0.004 * SR)))
    gr = uniform_filter1d(gr, int(0.003 * SR))
    return x * gr[:, None]


target_rms = float(sys.argv[2]) if len(sys.argv) > 2 else -18.0
ceil = 10 ** (-5.0 / 20)
for _ in range(8):
    rms = np.sqrt(np.mean(out ** 2)); out *= 10 ** (target_rms / 20) / rms
    out = limit(out, ceil * 0.97)
out = np.clip(out, -ceil, ceil) * gate[:, None]
print(f"pic {20*np.log10(np.max(np.abs(out))):.2f} dBFS, RMS {20*np.log10(np.sqrt(np.mean(out**2))):.2f} dBFS")
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
