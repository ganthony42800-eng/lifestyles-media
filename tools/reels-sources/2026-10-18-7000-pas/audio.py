import sys, numpy as np, wave
SR = 44100; DUR = 28.5; n = int(SR * DUR); t = np.arange(n) / SR
S = [0.0, 3.2, 6.6, 11.6, 15.2, 19.0, 22.0, 25.0, 28.5]   # identical to render.py
C3 = (S[2] + 0.25, 2.8); C5 = (S[4] + 0.25, 2.4)            # step counter timing (render.py)
rng = np.random.default_rng(3)
out = np.zeros((n, 2))
chords = [[110, 164.81, 261.63, 329.63], [87.31, 174.61, 261.63, 349.23], [130.81, 196, 261.63, 329.63],
          [98, 196, 246.94, 392], [110, 164.81, 261.63, 329.63], [87.31, 174.61, 261.63, 349.23],
          [130.81, 196, 261.63, 329.63], [130.81, 196, 261.63, 392]]
for i, ch in enumerate(chords):
    a, b = S[i], S[i + 1]
    env = np.clip((t - a + 0.4) / 0.6, 0, 1) * np.clip((b + 0.4 - t) / 0.6, 0, 1)
    for k, f in enumerate(ch):
        for det, side in ((0.997, 0), (1.003, 1)):
            out[:, side] += env * 0.05 * np.sin(2 * np.pi * f * det * t + k) * (0.8 + 0.2 * np.sin(2 * np.pi * 0.2 * t + k))
# soft arpeggio pluck every 0.4s
for j, tt in enumerate(np.arange(0.0, DUR - 0.5, 0.4)):
    i = max(x for x in range(8) if S[x] <= tt); f = chords[i][(j % 3) + 1] * 2
    m = (t >= tt) & (t < tt + 0.5); x = t[m] - tt
    s = 0.07 * np.sin(2 * np.pi * f * x) * np.exp(-x * 9)
    out[m, j % 2] += s; out[m, 1 - j % 2] += s * 0.6
# footstep-like sub pulse (walking tempo)
for tt in np.arange(0.0, DUR - 0.6, 0.8):
    for off, g in ((0, 1.0), (0.4, 0.55)):
        m = (t >= tt + off) & (t < tt + off + 0.3); x = t[m] - tt - off
        s = 0.2 * g * np.sin(2 * np.pi * 52 * x) * np.exp(-x * 14); out[m] += s[:, None]
# ticks synced with the step counter: one tick each time the display crosses a 250-step mark
def ease(x): x = np.clip(x, 0, 1); return 1 - (1 - x) ** 3
def steps(tt):
    if tt < S[3]: return 2000 + 5000 * ease((tt - C3[0]) / C3[1])
    return 7000 + 3000 * ease((tt - C5[0]) / C5[1])
def disp(v): return int(round(v / 50.0) * 50)
for a, b, pitch in ((S[2], S[3], 2400), (S[4], S[5], 2000)):
    prev = disp(steps(a)) // 250
    for fr in range(int(round(a * 30)), int(round(b * 30))):
        cur = disp(steps(fr / 30)) // 250
        if cur != prev:
            tt = fr / 30; m = (t >= tt) & (t < tt + 0.03); x = t[m] - tt
            out[m] += (0.32 * np.sin(2 * np.pi * pitch * x) * np.exp(-x * 180))[:, None]; prev = cur
# chime when -47 % lands
for tt, fs in ((C3[0] + C3[1] - 0.1, (880, 1318.5)),):
    m = (t >= tt) & (t < tt + 1.2); x = t[m] - tt
    s = sum(0.09 * np.sin(2 * np.pi * f * x) for f in fs) * np.exp(-x * 4); out[m] += s[:, None]
# whooshes at scene starts
for a in S[1:8]:
    tt = a - 0.25; m = (t >= tt) & (t < tt + 0.6); x = t[m] - tt
    nz = rng.standard_normal(m.sum()); nz = np.convolve(nz, np.ones(12) / 12, mode="same")
    e = np.sin(np.pi * x / 0.6) ** 2
    out[m, 0] += 0.25 * nz * e; out[m, 1] += 0.25 * nz[::-1] * e
out *= np.clip((DUR - t) / 0.8, 0, 1)[:, None]
out *= 0.89 / np.max(np.abs(out))
pcm = (out * 32767).astype(np.int16)
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print("ok")
