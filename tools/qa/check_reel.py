#!/usr/bin/env python3
"""Contrôle qualité automatique d'un Reel Lifestyles.

Usage : python3 tools/qa/check_reel.py reels/<fichier>.mp4 [--json rapport.json]

Mesures : format, durée, audio, images vides, plans figés, luminosité,
contenu hors zone sûre, contraste de l'accroche, mouvement par seconde.
Sortie : tableau OK / ALERTE / ÉCHEC + score /100. Code retour 1 si un ÉCHEC.
"""
import json, subprocess, sys
import numpy as np

W, H = 1080, 1920
SAFE = dict(top=220, bottom=1500, left=90, right=W - 150)


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "stream=codec_type,codec_name,width,height,r_frame_rate:format=duration",
                          "-of", "json", path], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def frames(path, fps=4, scale=4):
    w, h = W // scale, H // scale
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={fps},scale={w}:{h}",
                        "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True, check=True).stdout
    arr = np.frombuffer(p, np.uint8)
    return arr.reshape(-1, h, w).astype(np.float32), fps, scale


def audio_peak_mean(path):
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", path, "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    peak = mean = None
    for line in r.splitlines():
        if "max_volume" in line: peak = float(line.split(":")[1].split()[0])
        if "mean_volume" in line: mean = float(line.split(":")[1].split()[0])
    return peak, mean


def main():
    path = sys.argv[1]
    res = []
    def add(name, status, detail): res.append({"controle": name, "statut": status, "detail": detail})

    info = probe(path)
    v = [s for s in info["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in info["streams"] if s["codec_type"] == "audio"]
    dur = float(info["format"]["duration"])
    add("Format 1080x1920", "OK" if (v["width"], v["height"]) == (W, H) else "ÉCHEC", f'{v["width"]}x{v["height"]}')
    add("Codec H.264", "OK" if v["codec_name"] == "h264" else "ÉCHEC", v["codec_name"])
    add("Durée 18-30 s", "OK" if 18 <= dur <= 30 else ("ALERTE" if dur <= 40 else "ÉCHEC"), f"{dur:.1f} s")
    if not a:
        add("Audio présent", "ÉCHEC", "aucune piste audio")
    else:
        peak, mean = audio_peak_mean(path)
        ok = peak is not None and peak <= -0.5 and mean is not None and -24 <= mean <= -12
        add("Niveau audio", "OK" if ok else "ALERTE", f"pic {peak} dB, moyenne {mean} dB")

    F, fps, sc = frames(path)
    # images vides
    means = F.mean(axis=(1, 2)); stds = F.std(axis=(1, 2))
    empty = [i / fps for i in range(len(F)) if stds[i] < 6]
    add("Aucune image vide", "OK" if not empty else "ÉCHEC", f"{len(empty)} image(s) vide(s) {empty[:5]}")
    # plans figés > 2,5 s
    diffs = np.abs(np.diff(F, axis=0)).mean(axis=(1, 2))
    still, run, worst = [], 0, 0
    for i, d in enumerate(diffs):
        run = run + 1 if d < 0.35 else 0
        worst = max(worst, run)
    worst_s = worst / fps
    add("Pas de plan figé > 2,5 s", "OK" if worst_s <= 2.5 else ("ALERTE" if worst_s <= 4 else "ÉCHEC"), f"plus long figé : {worst_s:.2f} s")
    # rythme : changements forts
    changes = int((diffs > 4).sum())
    per = dur / max(changes, 1)
    add("Rythme (changement fort ≤ 3 s)", "OK" if per <= 3 else "ALERTE", f"{changes} changements forts, 1 toutes les {per:.1f} s")
    # luminosité
    add("Luminosité moyenne", "OK" if 15 <= means.mean() <= 140 else "ALERTE", f"{means.mean():.0f}/255")
    # hors zone sûre (contenu lumineux net hors marges, hors haut réservé à la signature)
    t, b, l, r = (SAFE["top"] // sc, SAFE["bottom"] // sc, SAFE["left"] // sc, SAFE["right"] // sc)
    bright = []
    for i, f in enumerate(F):
        base = np.median(f)
        m = f > base + 90
        m[:t, :] = False  # zone signature autorisée
        outside = m.copy(); outside[t:b, l:r] = False
        if outside.sum() > 120:  # ignore étoiles et petits décors
            bright.append(i / fps)
    add("Contenu dans la zone sûre", "OK" if not bright else "ALERTE", f"{len(bright)} image(s) avec du contenu hors zone {bright[:5]}")
    # accroche image 0 : contraste
    f0 = F[0][t:b, l:r]
    contrast = float(np.percentile(f0, 99.5) - np.median(f0))
    add("Accroche image 0 contrastée", "OK" if contrast >= 120 else ("ALERTE" if contrast >= 80 else "ÉCHEC"), f"écart {contrast:.0f}")
    add("Accroche présente image 0", "OK" if stds[0] >= 12 else "ÉCHEC", f"détail {stds[0]:.1f}")

    weights = {"OK": 1, "ALERTE": 0.5, "ÉCHEC": 0}
    score = round(100 * sum(weights[x["statut"]] for x in res) / len(res))
    fail = any(x["statut"] == "ÉCHEC" for x in res)
    print(f"Contrôle : {path}\n")
    for x in res: print(f'{x["statut"]:7} | {x["controle"]:34} | {x["detail"]}')
    print(f"\nScore : {score}/100 — {'NO-GO' if fail else ('GO' if score >= 85 else 'À AMÉLIORER')}")
    if "--json" in sys.argv:
        json.dump({"fichier": path, "score": score, "resultats": res}, open(sys.argv[sys.argv.index("--json") + 1], "w"), ensure_ascii=False, indent=1)
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
