#!/usr/bin/env python3
"""Moteur de rendu Lifestyles : scène HTML/three.js capturée image par image.

Usage :
  python3 capture.py <dossier_scene> <sortie.mp4> --duree 27 [--fps 30] [--audio audio.wav] [--apercu 0,3.5,9]

La scène (index.html dans <dossier_scene>) doit exposer :
  window.sceneReady : Promise résolue quand tout est chargé
  window.renderAt(t) : dessine l'état exact au temps t (secondes) — déterministe
Les fichiers du moteur (vendor/three, lib/) sont servis sous /engine/.
"""
import argparse, functools, http.server, os, subprocess, sys, threading
from playwright.sync_api import sync_playwright

ENGINE = "/home/claude/lifestyles-media/tools/motion-engine"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, scene_dir=None, **k):
        self.scene_dir = scene_dir
        super().__init__(*a, directory=scene_dir, **k)

    def translate_path(self, path):
        p = path.split("?")[0]
        if p.startswith("/engine/"):
            return os.path.join(ENGINE, p[len("/engine/"):])
        return super().translate_path(path)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *a):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scene"); ap.add_argument("out")
    ap.add_argument("--duree", type=float, required=True)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--audio")
    ap.add_argument("--apercu", help="liste de temps : produit des PNG au lieu d'une vidéo")
    a = ap.parse_args()
    scene_dir = os.path.abspath(a.scene)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Handler, scene_dir=scene_dir))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{srv.server_address[1]}/index.html"
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-gl=angle", "--use-angle=swiftshader", "--enable-webgl", "--ignore-gpu-blocklist",
                                    "--enable-unsafe-swiftshader", "--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.on("console", lambda m: print("[scene]", m.text) if m.type in ("error", "warning") else None)
        pg.on("pageerror", lambda e: print("[scene ERREUR]", e))
        pg.goto(url); pg.evaluate("window.sceneReady")
        if a.apercu:
            os.makedirs(a.out, exist_ok=True)
            for t in [float(x) for x in a.apercu.split(",")]:
                pg.evaluate(f"window.renderAt({t})")
                pg.screenshot(path=os.path.join(a.out, f"t{t:05.2f}.png"))
            print("aperçus :", a.out); b.close(); return
        n = int(round(a.duree * a.fps))
        tmp = a.out + ".video.mp4"
        ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(a.fps), "-c:v", "mjpeg", "-i", "-",
                               "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
        for i in range(n):
            pg.evaluate(f"window.renderAt({i / a.fps})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=95))
            if i % 90 == 0: print(f"image {i}/{n}", flush=True)
        ff.stdin.close(); ff.wait(); b.close()
    if a.audio:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-i", a.audio, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                        "-shortest", "-movflags", "+faststart", a.out], check=True)
        os.remove(tmp)
    else:
        os.replace(tmp, a.out)
    print("terminé :", a.out)


if __name__ == "__main__":
    main()
