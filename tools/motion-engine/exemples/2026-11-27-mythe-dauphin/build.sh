#!/bin/sh
# réinjecte scene.part dans index.html
python3 - <<'P'
h=open('index.html').read();s=open('scene.part').read()
a=h.index('/* ép. 20');b=h.index('/* ---------- textes ---------- */')
open('index.html','w').write(h[:a]+s+'\n'+h[b:])
P
