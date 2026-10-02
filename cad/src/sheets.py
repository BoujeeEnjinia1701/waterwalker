"""WaterWalker general arrangement drawing WWK-DWG-001 (Rev P3).

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
          rev="P3", author="Amish Chadha", date="2026-10-02", concept=True,
          material="Mild steel tube frame; 26 in bicycle wheels and forks; plywood cradle. See bom/bom.csv",
          revisions=[("P1", "Preliminary GA from the parametric model (WWK-CAL-001)", "2026-09-25", "AC"),
                     ("P2", "1.2 mm main wall, thinner cradle, parking lock pin (WWK-DDR-002)", "2026-09-25", "AC"),
                     ("P3", "Design for construction: carrier, brackets, headsets, fixings (WWK-DDR-003)", "2026-10-02", "AC")])
s.add_ortho(views, ["front", "top", "right"])
s.add_svg(views["iso"], 276, 38, 140, 76, label="Isometric view", sublabel="Not to scale; assist kit shown fitted")
s.add_notes("Key dimensions (mm) and notes", [
    f"Track {P['track']:.0f}; wheelbase {P['wheelbase']:.0f}; caster trail {P['trail']:.0f}",
    f"Overall width {D['overall_width']:.0f} over axle nuts (R6 900 max)",
    f"Clear walking width {D['walk_width']:.0f} between rails (R7 600 min)",
    f"Wheels 26 in, ETRTO 559, 2.1 to 2.4 in tires, 100 mm hubs",
    "Headsets on all forks; rear pinned, front swivel",
    f"Caster sweep R{D['sweep_r']:.0f}; {D['riser_gap']:.0f} clear of front risers",
    f"Hip bar {P['hip_min']:.0f} to {P['hip_max']:.0f} above ground; open rear entry",
    f"Cradle {D['cr_x1'] - P['cr_x0']:.0f} x {2 * P['cr_hw']:.0f}, floor {P['cr_z']:.0f} up, on two bearers",
    f"Ground clearance under the bearers {D['clearance']:.0f}",
    f"Lift over side rail {D['rail_top'] + 10:.0f} (R8 450 max)",
    "Main tube RHS 40 x 30 x 1.2; cross 25 x 25 x 1.5",
    "Making sketches WWK-DWG-101 to 108 (build plan WWK-BLD-001)",
    "Parking lock pin, 10 mm, through left rear spokes",
    "Optional later assist kit: SwapCell v0.3, class V1",
    "Empty 39.6 kg; loaded 124 kg (WWK-CAL-001 v0.3)",
    "PRELIMINARY, NOT FOR FABRICATION",
], x=276, y=128, width=140)
s.save(ROOT / "cad/drawings/WWK-DWG-001")
shutil.rmtree(work, ignore_errors=True)
print("wrote cad/drawings/WWK-DWG-001.svg, .pdf, .png")
