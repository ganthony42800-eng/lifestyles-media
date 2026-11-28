#!/bin/sh
# réinjecte scene.part + texts.part dans index.html
python3 - <<'P'
h=open('index.html').read();s=open('scene.part').read();x=open('texts.part').read()
a=h.index('/* ép. 23');b=h.index('const TX=document')
open('index.html','w').write(h[:a]+s+'\n'+x+'\n'+h[b:])
P
