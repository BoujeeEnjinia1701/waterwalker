"""WaterWalker general arrangement drawing WWK-DWG-001 (Rev P1).

Run from the repo root:  python cad/src/sheets.py
Builds cad/drawings/WWK-DWG-001.svg, .pdf and .png from the parametric model.
The concept blueprint sheet keeps its own number, WWK-DWG-010.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".kit"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from drawing import Sheet, project_views  # noqa: E402
from model import PARAMS as P, build_parts, compound, derived  # noqa: E402

D = derived()
parts = build_parts()
asm = compound(parts, ("base", "load", "assist"))
work = ROOT / "cad/drawings/_views"
views = project_views(asm, work)

s = Sheet(project="WaterWalker", title="General arrangement, walk-inside water carrier", dwg_no="WWK-DWG-001",
          rev="P1", author="Amish Chadha", date="2026-09-25", concept=True,
          material="Mild steel tube frame; 26 in bicycle wheels and forks; plywood cradle. See bom/bom.csv",
          revisions=[("P1", "Preliminary GA from the parametric model (WWK-CAL-001)", "2026-09-25", "AC")])
s.add_ortho(views, ["front", "top", "right"])
s.add_svg(views["iso"], 276, 30, 140, 84, label="Isometric view", sublabel="Not to scale; assist kit shown fitted")
s.add_notes("Key dimensions (mm) and notes", [
    f"Track {P['track']:.0f}; wheelbase {P['wheelbase']:.0f}; caster trail {P['trail']:.0f}",
    f"Overall width {D['overall_width']:.0f} over axle nuts (R6 900 max)",
    f"Clear walking width {D['walk_width']:.0f} between rails (R7 600 min)",
    f"Wheels 26 in, ETRTO 559, 2.1 to 2.4 in tires, 100 mm hubs",
    f"Rear wheels in fixed forks; front forks swivel, lock pin",
    f"Caster sweep R{D['sweep_r']:.0f}; {D['riser_gap']:.0f} clear of front risers",
    f"Hip bar {P['hip_min']:.0f} to {P['hip_max']:.0f} above ground; open rear entry",
    f"Cradle {D['cr_x1'] - P['cr_x0']:.0f} x {2 * P['cr_hw']:.0f}, floor {P['cr_z']:.0f} above ground",
    f"Lift over side rail {D['rail_top'] + 10:.0f} (R8 450 max)",
    "Main tube RHS 40 x 30 x 1.5; cross 25 x 25 x 1.5",
    "Assist kit (items 9 to 11, 13) is optional, later:",
    "  SwapCell interface v0.3, class V1 receiver",
    "Empty 40.8 kg; loaded 125 kg (WWK-CAL-001)",
    "PRELIMINARY, NOT FOR FABRICATION",
], x=276, y=128, width=140)
s.save(ROOT / "cad/drawings/WWK-DWG-001")
shutil.rmtree(work, ignore_errors=True)
print("wrote cad/drawings/WWK-DWG-001.svg, .pdf, .png")
