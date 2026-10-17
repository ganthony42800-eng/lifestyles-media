import sys, numpy as np, wave
SR = 44100; DUR = 25.0; n = int(SR * DUR); t = np.arange(n) / SR
S = [0.0, 3.4, 7.6, 11.2, 14.4, 17.8, 21.4, 25.0]
rng = np.random.default_rng(3)
out = np.zeros((n, 2))
# pad chords per scene
chords = [[110, 164.81, 261.63, 329.63], [87.31, 174.61, 261.63, 349.23], [130.81, 196, 261.63, 329.63],
          [98, 196, 246.94, 392], [110, 164.81, 261.63, 329.63], [87.31, 174.61, 261.63, 349.23], [130.81, 196, 261.63, 392]]
for i, ch in enumerate(chords):
    a, b = S[i], S[i + 1]
    env = np.clip((t - a + 0.4) / 0.6, 0, 1) * np.clip((b + 0.4 - t) / 0.6, 0, 1)
    for k, f in enumerate(ch):
        for det, side in ((0.997, 0), (1.003, 1)):
            out[:, side] += env * 0.05 * np.sin(2 * np.pi * f * det * t + k) * (0.8 + 0.2 * np.sin(2 * np.pi * 0.2 * t + k))
# soft arpeggio pluck every 0.4s
for j, tt in enumerate(np.arange(0.0, DUR - 0.5, 0.4)):
    i = max(x for x in range(7) if S[x] <= tt); f = chords[i][(j % 3) + 1] * 2
    m = (t >= tt) & (t < tt + 0.5); x = t[m] - tt
    s = 0.07 * np.sin(2 * np.pi * f * x) * np.exp(-x * 9)
    out[m, j % 2] += s; out[m, 1 - j % 2] += s * 0.6
# heartbeat sub pulse
for tt in np.arange(0.0, DUR - 0.6, 0.8):
    for off, g in ((0, 1.0), (0.18, 0.6)):
        m = (t >= tt + off) & (t < tt + off + 0.3); x = t[m] - tt - off
        s = 0.22 * g * np.sin(2 * np.pi * 52 * x) * np.exp(-x * 14); out[m] += s[:, None]
# clock ticks synced with hour counter (scene 2)
def ease(x): x = np.clip(x, 0, 1); return 1 - (1 - x) ** 3
prev = 0
for fr in range(int(S[1] * 30), int(S[2] * 30)):
    k = ease((fr / 30 - S[1] - 0.35) / 2.6); h = int(round(17 * k))
    if h != prev:
        tt = fr / 30; m = (t >= tt) & (t < tt + 0.03); x = t[m] - tt
        s = 0.35 * np.sin(2 * np.pi * 2400 * x) * np.exp(-x * 180); out[m] += s[:, None]; prev = h
# timeline ticks scene 5
for tt in np.linspace(S[4] + 0.5, S[4] + 2.1, 9):
    m = (t >= tt) & (t < tt + 0.03); x = t[m] - tt
    out[m] += (0.2 * np.sin(2 * np.pi * 1800 * x) * np.exp(-x * 200))[:, None]
# whooshes at scene starts
for a in S[1:7]:
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
