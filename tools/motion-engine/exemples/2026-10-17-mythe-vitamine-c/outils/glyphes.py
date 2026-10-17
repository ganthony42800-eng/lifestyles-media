# Extrait les contours de glyphes (Inter Display Black) en JSON pour THREE.ShapePath
import json, sys
from fontTools.ttLib import TTFont
from fontTools.pens.basePen import BasePen
FONT = "/home/claude/lifestyles-media/tools/motion-engine/fonts/InterDisplay-Black.otf"
f = TTFont(FONT); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f["head"].unitsPerEm
class P(BasePen):
    def __init__(s, g): super().__init__(g); s.c = []
    def _moveTo(s, p): s.c.append(["M", *p])
    def _lineTo(s, p): s.c.append(["L", *p])
    def _curveToOne(s, a, b, c): s.c.append(["C", *a, *b, *c])
    def _qCurveToOne(s, a, b): s.c.append(["Q", *a, *b])
    def _closePath(s): s.c.append(["Z"])
out = {"upm": upm, "glyphs": {}}
for ch in set("SCIENCE"):
    n = cmap[ord(ch)]; p = P(gs); gs[n].draw(p)
    out["glyphs"][ch] = {"adv": gs[n].width, "cmds": p.c}
json.dump(out, open(sys.argv[1], "w"))
print("ok", upm, {k: v["adv"] for k, v in out["glyphs"].items()})
