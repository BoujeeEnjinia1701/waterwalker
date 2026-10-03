"""WaterWalker concept media from the parametric model (TRL 3).

Run from the repo root:  python cad/src/concept_media.py
Geometry comes from cad/src/model.py; numbers in the key figures come from
WWK-CAL-001 (docs/04-calcs/sizing.py). Not for fabrication.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / ".kit"))
sys.path.insert(0, str(HERE))
from concept import ROOT, Part, _render, render_all  # noqa: E402
from model import build_parts, patch_svg_export  # noqa: E402

patch_svg_export()

raw = build_parts()
# Hero, blueprint and 3D viewer show the approved first prototype: no assist, with mounting points.
parts = [Part(name, shape, color, bom, explode) for bom, name, shape, color, explode, grp in raw if grp != "assist"]
# The exploded view also shows the optional assist kit (items 9 to 11 and 13) so its callouts match the BOM.
parts_all = [Part(name, shape, color, bom, explode) for bom, name, shape, color, explode, _ in raw]

render_all(
    parts, project="WaterWalker", title="Walk-inside water carrier concept", dwg_no="WWK-DWG-010",
    date="2026-10-02", rev="P3", cut=False,
    key_figures=["80 L per trip (4 x 20 L jerrycans) or 40 L (2 clay pots)",
                 "26 in wheels, 898 mm wide, 2.2 m long, 3.7 m turning circle",
                 "Push, firm path 24 to 61 N; loose sand 241 to 367 N (calc.)",
                 "Empty 40.3 kg; parts $492 (no assist); hold-to-release brake",
                 "Assist-ready (not fitted): two-motor tabs, SwapCell v0.3"],
    flow={"title": "water delivered per trip and per day (estimates, WWK-CAL-001)", "unit": "",
          "stages": [("Water point", "fill 4 x 20 L"),
                     ("Load cradle", "lift 20 kg to 0.36 m"),
                     ("Walk home", "80 L per trip vs 20 L"),
                     ("Household", "about 100 L per day"),
                     ("Trips per day", "2 vs 5 by head")]},
)
_render(parts_all, ROOT / "media" / "exploded.png", offsets=True, labels=True,
        title="WaterWalker: exploded view (optional assist kit shown)")
print("wrote media/ (hero, blueprint, exploded, flow, model.glb, viewer.html)")
