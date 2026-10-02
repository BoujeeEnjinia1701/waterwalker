"""WaterWalker prototype build plan pictures (WWK-BLD-001, STANDARDS section 18).

Run from the repo root:  python cad/src/build_plan_media.py [overview|sheets|joints|steps ...]
With no argument it draws everything; a name with a number (sheets:103, joints:4, steps:7) draws only that
picture, which keeps memory low. Every picture is drawn from cad/src/model.py (build_components), so the
pictures and the model never disagree:
    docs/05-build-plan/overview.png        every component pulled apart, numbered in build order
    cad/drawings/WWK-DWG-101 to 108        making sketches for the made components
    docs/05-build-plan/joint-NN.png        close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png         one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from model import PARAMS as P, build_components, derived, frame_members, tube, bx, fuse  # noqa: E402

OUT = ROOT / "docs" / "05-build-plan"
DWG = ROOT / "cad" / "drawings"
DATE = "2026-10-02"
D = derived(P)
_C = None


def C():
    global _C
    if _C is None:
        _C = build_components(P)
    return _C


def S(*ks):
    return fuse([C()[k].shape for k in ks])


COL = {"frame": "#0F766E", "rear_ht": "#14B8A6", "carrier": "#0E7490", "cups": "#1D4ED8", "fork": "#374151",
       "tabs": "#DC2626", "collar": "#7C3AED", "pin": "#B45309", "guard": "#CBD5E1", "clip": "#475569",
       "wheel": "#4B5563", "hipbar": "#B45309", "pad": "#1F2937", "lever": "#6B7280", "cradle": "#A16207",
       "padr": "#57534E", "brackets": "#94A3B8", "bolt": "#111827", "lockpin": "#DC2626", "cans": "#E3B505",
       "arm": "#9CA3AF"}


def part(name, shape, color, explode=(0, 0, 0), alpha=1.0):
    return Part(name, shape, color, None, tuple(explode), alpha)


def win(shape, x0, x1, y0, y1, z0, z1):
    return shape & bx(x0, x1, y0, y1, z0, z1)


def solid_members(prefixes, exclude=()):
    """The welded members as solid bars, for clean views on the making sketches."""
    out = []
    for name, sec, a, c in frame_members(P):
        if name.startswith(prefixes) and not name.startswith(exclude):
            out.append(tube(P, sec, a, c, hollow=False))
    return fuse(out)


# ----------------------------------------------------------------- named parts, in build order
def made():
    return [
        ("frame", part("Frame weldment", S("frame"), COL["frame"])),
        ("rear_ht", part("Rear head tubes and brackets (2)", S("rear_ht_l", "rear_ht_r"), COL["rear_ht"])),
        ("carrier", part("Rear cross member and cradle carrier", S("carrier"), COL["carrier"])),
        ("locks", part("Headsets, lock collars and lock pins (4 sets)", S("cups_front", "cups_rear", "collars_front", "collars_rear",
                                                                        "pins_front", "pins_rear"), COL["collar"])),
        ("rforks", part("Rear forks with welded tabs (2)", S("rear_fork_l", "rear_fork_r", "pin_tabs", "torque_tab"), COL["fork"])),
        ("fforks", part("Front forks (2)", S("front_fork_l", "front_fork_r"), "#1F2937")),
        ("guard_l", part("Skirt guard, left, with clips and bolts", S("guard_l", "guard_clips_l"), COL["guard"])),
        ("guard_r", part("Skirt guard, right, with clips and bolts", S("guard_r", "guard_clips_r"), COL["guard"])),
        ("rwheels", part("Rear wheels with drum hubs (2)", S("rear_wheel_l", "rear_wheel_r", "brake_arm_l", "brake_arm_r"), COL["wheel"])),
        ("fwheels", part("Front wheels (2)", S("front_wheel_l", "front_wheel_r"), "#6B7280")),
        ("hipbar", part("Hip bar with pad, grips and height pins", S("hipbar", "pad_grips", "hip_pins"), COL["hipbar"])),
        ("lever", part("Brake lever with parking latch", S("lever"), "#DC2626")),
        ("cradle", part("Cradle with pad, brackets and bolts", S("cradle", "cradle_pad", "cradle_brackets"), COL["cradle"])),
        ("lockpin", part("Parking lock pin", S("lock_pin"), COL["lockpin"])),
    ]


# ----------------------------------------------------------------- overview
def overview():
    M = made()
    off = {"frame": (0, 0, 0), "rear_ht": (-170, 0, 140), "carrier": (0, 0, -230), "locks": (0, 0, 230),
           "rforks": (-260, 0, -60), "fforks": (260, 0, -60), "guard_l": (-100, 560, -120), "guard_r": (-60, -680, 60),
           "rwheels": (-700, 0, -100), "fwheels": (700, 0, -100), "hipbar": (-140, 0, 330), "lever": (-420, -330, 420),
           "cradle": (0, -330, -520), "lockpin": (-100, 820, 120)}
    parts = []
    for k, p in M:
        p.explode = off[k]
        parts.append(p)
    return bv.overview(parts, OUT / "overview.png", "WaterWalker prototype: every component, pulled apart",
                       subtitle="Numbered in build order; seen from behind on the left, above. The 20 L jerrycans are the user's own",
                       elev=26, azim=140, size=(12, 8.5), dpi=150, key=True)


# ----------------------------------------------------------------- making sketches
def sheets(only=None):
    import build123d as b
    base = dict(project="WaterWalker", date=DATE)
    out = []
    grey = lambda k, n: part(n, S(*k) if isinstance(k, tuple) else S(k), "#D1D5DB")  # noqa: E731

    def want(n):
        return only is None or only == n

    if want(101):
        import model
        fr = solid_members(("side rail", "front riser", "caster arm", "hip upright", "front lower", "upper cross"))
        hz = D["head_z"]
        for sy in (1, -1):
            fr += model.zcyl(D["pivot_x"], sy * D["t2"], hz - P["head_len"] / 2, hz + P["head_len"] / 2, P["head_d"] / 2)
        rx = P["rx_plate"]
        fr += bx(P["front_x"], P["front_x"] + rx[0], -rx[1] / 2, rx[1] / 2, P["arm_z"] + 20, P["arm_z"] + 20 + rx[2])
        out.append(bv.component_sheet(
            Part("Frame weldment", S("frame"), COL["frame"]), [grey(("rear_ht_l", "rear_ht_r"), "rear"), grey("carrier", "carrier"),
                                                            grey(("front_fork_l", "front_fork_r"), "forks")],
            dwg_no="WWK-DWG-101", title="WaterWalker frame weldment: making sketch",
            material="Mild steel RHS 40 x 30 x 1.2 mm; square 30 x 30 x 1.5 mm sleeves; tube 44 mm OD head tubes",
            view_shape=fr, inset_view=(24, 50),
            notes=["Cut list (centre to centre lengths are in the build plan, Table 2):",
                   "  side rails 2 x 1,125; front risers 2 x 442; caster arms 2 x 408,",
                   "  angled 8.6 degrees outward; lower cross member 610 and upper",
                   "  cross member 670 (40 x 30 x 1.2); hip sleeves 2 x 467 (30 x 30).",
                   "Build it upside down on a flat floor: rail centres 640 apart,",
                   "  square to the lower cross member; check the diagonals agree.",
                   "Risers stand on the rails at their front ends; the upper cross",
                   "  member sits on the riser tops; caster arms butt on its front",
                   "  face over each riser and are coped to the head tubes.",
                   "Head tubes upright, 770 apart, 1,590 ahead of the rear axle line.",
                   "Sleeves stand on the rail ends, rear faces flush with the rail ends.",
                   "Weld the receiver plate on the upper cross member, the pin guides",
                   "  on the caster arms, the guard tabs on the rails, the sensor tab.",
                   "Check: posts slide in the sleeves; head tubes parallel."],
            **base))
    if want(102):
        lk = [m for m in frame_members(P) if m[0].startswith("rear bracket") and m[0].endswith("left")]
        rh = fuse([tube(P, sec, a, c, hollow=False) for _, sec, a, c in lk])
        import model
        ht = model.zcyl(D["rear_ht_x"], D["t2"], D["head_z"] - P["head_len"] / 2, D["head_z"] + P["head_len"] / 2, P["head_d"] / 2) \
            - model.zcyl(D["rear_ht_x"], D["t2"], D["head_z"] - P["head_len"] / 2 - 1, D["head_z"] + P["head_len"] / 2 + 1, P["head_id"] / 2)
        out.append(bv.component_sheet(
            Part("Rear head tube and brackets", S("rear_ht_l"), COL["rear_ht"]),
            [grey("frame", "frame"), grey("rear_fork_l", "fork"), grey("rear_wheel_l", "wheel")],
            dwg_no="WWK-DWG-102", title="WaterWalker rear head tube and brackets (make 2, mirror): making sketch",
            material="Square tube 25 x 25 x 1.5 mm; head tube 44 mm OD, 34 mm bore, 140 long",
            view_shape=b.Pos(-D["rear_ht_x"], -D["rail_y"], -700) * (rh + ht), inset_view=(25, 135),
            notes=["Two brackets, one above the other, each an arm and a stub:",
                   "  arm 117.5 long along the rail line, stub 30.5 long out to the",
                   "  head tube; lower bracket centred 745 up, upper 805 up.",
                   "Weld each stub square to the end of its arm (an L), then cope",
                   "  the stub's free end to the 44 mm head tube.",
                   "Jig the head tube upright 385 out from the centre line and 60",
                   "  behind the rear axle line, its bottom 730 above the ground.",
                   "Weld both stubs to the head tube, then both arm ends to the",
                   "  rear face of the hip sleeve (left and right are mirror images).",
                   "Pin guide: 14 mm tube 57 long welded upright on the upper stub,",
                   "  45 in from the head tube axis; drill the stub top 9 mm under it.",
                   "Face both head tube ends square and ream the bore to the headset",
                   "  maker's size (34 mm for external cups).",
                   "Check: head tube upright both ways within 0.5 degree."],
            **base))
    if want(103):
        car = solid_members(("cradle", "rear cross member"))
        out.append(bv.component_sheet(
            Part("Cradle carrier", S("carrier"), COL["carrier"]), [grey("frame", "frame"), grey("cradle", "cradle")],
            dwg_no="WWK-DWG-103", title="WaterWalker rear cross member and cradle carrier: making sketch",
            material="Square tube 25 x 25 x 1.5 mm (cross member, bearers); 20 x 20 x 1.5 mm (hangers)",
            view_shape=car, inset_view=(22, 50),
            notes=["Rear cross member 610 long between the rails, 332.5 ahead of the",
                   "  rear axle line, centre at axle height (333.5 up).",
                   "Bearers 2 x 837.5 long, 300 apart centre to centre, top faces 150",
                   "  above the ground (125 mm ground clearance underneath).",
                   "Hangers: rear 2 x 171 under the rear cross member, front",
                   "  2 x 164 under the front lower cross member, all 150 out from",
                   "  the centre line, standing on the bearer ends.",
                   "Weld the hangers to the bearers first (a ladder upside down),",
                   "  then offer it up under the cross members and weld the tops.",
                   "Drill four 6.6 mm holes through the bearers for the cradle bolts:",
                   "  400 and 1,080 ahead of the rear axle line.",
                   "Check: bearer tops level within 2 mm and 300 apart; cradle",
                   "  drops in with 5 mm to spare in front of the hangers."],
            **base))
    if want(104):
        import model
        x, y = D["pivot_x"], D["t2"]
        col = S("collars_front") & bx(x - 70, x + 70, y - 70, y + 70, 0, 2000)
        out.append(bv.component_sheet(
            Part("Lock collar", col, COL["collar"]), [grey("frame", "frame"), grey("front_fork_l", "fork"), grey("cups_front", "cups")],
            dwg_no="WWK-DWG-104", title="WaterWalker lock collar with lock plate (make 4): making sketch",
            material="Bought 40 mm clamp collar for 28.6 mm; steel plate 3 mm",
            view_shape=b.Pos(-x, -y, -900) * col, inset_view=(30, 40),
            notes=["Plate 59 x 25 x 3 mm, one end rounded to the collar's outside.",
                   "Drill 8.5 mm, 45 from the collar centre on the plate centre line.",
                   "Weld the plate flat to the underside of the collar, pointing",
                   "  away from the clamp bolt; keep the bore free of spatter.",
                   "Fit: the collar sits on the top headset cup with a 2 mm spacer,",
                   "  its bolt clamps the steerer; the top cap and its bolt above",
                   "  set the headset preload before the collar is tightened.",
                   "Front: turn the collar so the hole lines up over the pin guide",
                   "  with the wheel trailing straight back; the pin drops in to lock.",
                   "Rear: same, wheel straight ahead; the pin stays in, R-clipped.",
                   "Check: with the pin out the fork turns freely and does not knock."],
            **base))
    if want(105):
        tabs = S("pin_tabs")
        out.append(bv.component_sheet(
            Part("Lock pin tabs", tabs, COL["tabs"]), [grey("rear_fork_l", "fork"), grey("rear_wheel_l", "wheel"), grey("lock_pin", "pin")],
            dwg_no="WWK-DWG-105", title="WaterWalker fork tabs: lock pin tabs (left rear) and torque-arm tab (right rear)",
            material="Steel flat bar 30 x 6 mm",
            view_shape=b.Pos(60, -385, -533.5) * tabs, inset_view=(20, 125),
            notes=["Lock pin tabs, make 2: 30 x 6 bar, about 40 long, one end shaped",
                   "  to sit on the back of the fork blade. Drill 10.5 mm, 20 from",
                   "  that end. Weld one to the inner and one to the outer blade of",
                   "  the left rear fork, 200 above and 60 behind the axle.",
                   "Jig both tabs with a 10 mm bar through both holes so they line up.",
                   "Torque-arm tab, make 1: 30 x 6 bar 60 long (40 high), 11 mm hole",
                   "  50 behind the axle; weld to the back of the outer blade of the",
                   "  right rear fork, centred 60 above the axle.",
                   "Steel forks only. Clean off paint, short welds, no undercut on",
                   "  the blade; let them cool in air. Paint after.",
                   "Check: the 10 mm pin slides through both tabs with the wheel out."],
            **base))
    if want(106):
        g = S("guard_l")
        out.append(bv.component_sheet(
            Part("Skirt guard", g, COL["guard"]), [grey("frame", "frame"), grey("rear_fork_l", "fork"), grey("rear_wheel_l", "wheel")],
            dwg_no="WWK-DWG-106", title="WaterWalker skirt guard (make 2, mirror): making sketch",
            material="HDPE sheet 3 mm",
            view_shape=b.Pos(0, -D["rail_y"] - 20, -420) * g, inset_view=(15, 120),
            notes=["Cut 540 x 420; round the corners to about 20 mm.",
                   "Slot for the hub: 120 wide from the bottom edge up to the axle",
                   "  centre (123.5 up from the bottom edge), ending in a 60 radius.",
                   "Two 6.6 mm holes for the rail tabs, 123.5 up from the bottom",
                   "  edge, 150 and 240 ahead of the axle line.",
                   "Left guard only: a 14 mm hole for the lock pin, 60 behind the",
                   "  axle line, 323.5 up from the bottom edge.",
                   "Make the right guard as a mirror image without the pin hole.",
                   "Fit: flat against the guard tabs on the rail, 5 mm outside the",
                   "  rail; two clips on the inner blade, 450 and 600 above ground.",
                   "Fit it before the wheel: the hub goes up into the slot.",
                   "Check: 15 mm or more from the spokes all round."],
            **base))
    if want(107):
        hb = S("hipbar")
        out.append(bv.component_sheet(
            Part("Hip bar weldment", hb, COL["hipbar"]), [grey("frame", "frame"), grey("pad_grips", "pad")],
            dwg_no="WWK-DWG-107", title="WaterWalker hip bar weldment: making sketch",
            material="Steel tube 32 x 1.5 mm; square tube 25 x 25 x 1.5 mm; tube 22.2 x 1.6 mm",
            view_shape=b.Pos(0, 0, -800) * hb, inset_view=(25, 140),
            notes=["Bar: 32 mm tube 680 long. Posts: 25 x 25 tube, 2 x 364 long,",
                   "  640 apart centre to centre, saddle-coped to the bar.",
                   "Grip tubes: 22.2 mm tube, 2 x 277 long, along the posts' line,",
                   "  coped to the back of the bar, pointing back toward the user.",
                   "Weld on a flat table with the posts square to the bar.",
                   "Height holes: nine 6.5 mm holes through each post, front to",
                   "  back, 25 apart; the top one 75 below the bar centre.",
                   "Fit: the posts slide into the hip sleeves (1 mm clearance each",
                   "  side); a 6 mm pin through sleeve and post holds the height,",
                   "  bar centre 850 to 1,050 above the ground.",
                   "Check: both posts enter and slide together without binding."],
            **base))
    if want(108):
        cr = S("cradle")
        out.append(bv.component_sheet(
            Part("Cradle", cr, COL["cradle"]), [grey("carrier", "carrier"), grey("frame", "frame")],
            dwg_no="WWK-DWG-108", title="WaterWalker cradle (floor and walls): making sketch",
            material="Exterior plywood 6 mm (floor) and 4 mm (walls); zinc angle brackets",
            view_shape=b.Pos(-740, 0, -230) * cr, inset_view=(30, 50),
            notes=["Floor 780 x 430, 6 mm. Side walls 2 x 780 x 160, end walls",
                   "  2 x 422 x 160, 4 mm. Walls stand on the floor at its edges;",
                   "  the end walls fit between the side walls.",
                   "Brackets outside: 10 along the bottom joints (3 per side, 2",
                   "  per end), 4 up the corners; M4 bolts, washers both sides.",
                   "Seal all edges with exterior paint or varnish before assembly.",
                   "Four 6.6 mm holes in the floor for the bolts to the bearers,",
                   "  150 each side of the centre line, 50 and 730 from the rear edge;",
                   "  countersink them from the inside so the pad lies flat.",
                   "Pad: 2 mm rubber, 772 x 422, laid loose on the floor.",
                   "Strap anchors: one M6 bolt with a large washer through each side",
                   "  wall, 20 up, at 186 and 594 from the rear edge.",
                   "Check: four jerrycans drop in 2 x 2 with 2 mm to the walls."],
            **base))
    return out


# ----------------------------------------------------------------- joints
def joints(only=None):
    out = []
    W = lambda k, *box_: win(S(*k) if isinstance(k, tuple) else S(k), *box_)  # noqa: E731

    def want(n):
        return only is None or only == n
    hx, t2, ry = D["rear_ht_x"], D["t2"], D["rail_y"]
    if want(1):
        b_ = (-110, 95, 290, 420, 722, 905)
        out.append(bv.joint([
            part("Hip sleeve", W("frame", *b_), "#64748B"),
            part("Rear head tube, two brackets, pin guide", W("rear_ht_l", *b_), COL["rear_ht"]),
            part("Headset cups", W("cups_rear", *b_), COL["cups"]),
            part("Fork steerer and crown", W("rear_fork_l", *b_), COL["fork"]),
            part("Lock collar and plate", W("collars_rear", *b_), COL["collar"]),
            part("Lock pin, always in", W("pins_rear", *b_), COL["pin"])],
            OUT / "joint-01.png", "Joint 1: rear head tube on its two brackets (left side)",
            subtitle="Seen from the left, a little ahead. Two brackets 60 mm apart carry the fork's twisting load into the hip sleeve",
            elev=30, azim=75, size=(8, 6)))
    if want(2):
        x0 = D["pivot_x"]
        b_ = (x0 - 130, x0 + 45, t2 - 70, t2, 690, 935)
        out.append(bv.joint([
            part("Head tube and caster arm (cut)", W("frame", *b_), COL["frame"]),
            part("Headset cups (cut)", W("cups_front", *b_), COL["cups"]),
            part("Fork steerer and crown (cut)", W("front_fork_l", *b_), "#CBD5E1"),
            part("Lock collar, plate and top cap (cut)", W("collars_front", *b_), COL["collar"]),
            part("Pin guide on the arm, swivel lock pin", W("pins_front", x0 - 130, x0 + 45, t2 - 70, t2 + 40, 690, 935), COL["pin"])],
            OUT / "joint-02.png", "Joint 2: front head tube, headset and swivel lock, cut through the middle (left side)",
            subtitle="Seen from the left. The pin drops through the plate into the guide when the wheel trails straight back",
            elev=12, azim=95, size=(8, 6)))
    if want(3):
        b_ = (295, 440, P["bearer_y"], 260, 100, 365)
        out.append(bv.joint([
            part("Rear cross member", W("carrier", 295, 440, P["bearer_y"], 260, 321, 365), "#64748B"),
            part("Hanger and bearer (cut)", W("carrier", 295, 440, P["bearer_y"], 260, 100, 321), COL["carrier"]),
            part("Cradle floor and rear wall (cut)", W("cradle", *b_), COL["cradle"]),
            part("Rubber pad", W("cradle_pad", *b_), COL["padr"]),
            part("M6 bolt, nyloc under the bearer (cut)", W("cradle_bolts", *b_), COL["bolt"])],
            OUT / "joint-03.png", "Joint 3: rear hanger, bearer and cradle bolt, cut along the bearer (left side)",
            subtitle="Seen from the centre line. The hanger stands on the bearer end, welded under the rear cross member; the floor rests on the bearer",
            elev=10, azim=-75, size=(8, 6)))
    def mem(name):
        for n, sec, a, c in frame_members(P):
            if n == name:
                return tube(P, sec, a, c)
        raise KeyError(name)
    if want(4):
        x0 = P["front_x"]
        b_ = (x0 - 40, x0 + 260, -ry - 90, -ry + 90, 700, 880)
        out.append(bv.joint([
            part("Front riser", win(mem("front riser right"), *b_), "#64748B"),
            part("Upper cross member, on the riser top", win(mem("upper cross member"), *b_), COL["frame"]),
            part("Caster arm, butted on the cross member face", win(mem("caster arm right"), *b_), "#B45309"),
            part("Receiver plate (assist mount)", win(S("frame"), x0 + 15, x0 + 260, -ry - 90, -ry + 90, 836, 845), COL["carrier"])],
            OUT / "joint-04.png", "Joint 4: top of the front riser (right side)",
            subtitle="Seen from the front right and above. The caster arm leaves directly over the riser, angled 8.6 degrees outward",
            elev=28, azim=-40, size=(8, 6)))
    if want(10):
        x0 = P["front_x"]
        b_ = (x0 - 80, x0 + 60, -ry - 40, -100, 110, 420)
        out.append(bv.joint([
            part("Side rail", win(mem("side rail right"), *b_), "#64748B"),
            part("Front riser, standing on the rail", win(mem("front riser right"), *b_), COL["frame"]),
            part("Front lower cross member, between the rails", win(mem("front lower cross member"), *b_), "#B45309"),
            part("Front hanger and bearer", win(S("carrier"), *b_), COL["carrier"])],
            OUT / "joint-10.png", "Joint 10: foot of the front riser (right side)",
            subtitle="Seen from behind, inside the carrier. The hanger is welded under the lower cross member and stands on the bearer end",
            elev=20, azim=-150, size=(8, 6)))
    if want(5):
        b_ = (20, 110, ry, ry + 40, 720, 975)
        out.append(bv.joint([
            part("Hip sleeve (cut open)", W("frame", *b_), "#64748B"),
            part("Rear brackets", W("rear_ht_l", *b_), COL["rear_ht"]),
            part("Hip post (cut open) and bar", W("hipbar", *b_), COL["hipbar"]),
            part("Height pin, front to back", W("hip_pins", *b_), "#DC2626")],
            OUT / "joint-05.png", "Joint 5: hip post in its sleeve, cut through the middle (left side)",
            subtitle="Seen from the walking space, ahead. 1 mm clearance each side; the pin goes between the two rear brackets",
            elev=22, azim=-50, size=(8, 6)))
    if want(6):
        b_ = (-300, 300, ry + 10, ry + 30, 200, 640)
        out.append(bv.joint([
            part("Rail outer wall (rail cut away) and guard tabs", W("frame", -300, 300, ry + 10, ry + 30, 290, 640), "#64748B"),
            part("Inner fork blade (cut)", W("rear_fork_l", *b_), COL["fork"]),
            part("Rubber-lined clip with 5 mm spacer", W("guard_clips_l", *b_), "#DC2626"),
            part("Skirt guard", W("guard_l", *b_), COL["guard"]),
            part("M6 bolts into the tapped tabs", W("guard_bolts_l", *b_), COL["bolt"])],
            OUT / "joint-06.png", "Joint 6: skirt guard fixings, seen from the walking space (left side)",
            subtitle="The rail and fork are cut away to show the fixings: two bolts into the rail tabs, two clips on the inner fork blade",
            elev=10, azim=-80, size=(8, 6)))
    if want(7):
        pz = D["wheel_r"] + P["pin_dz"]
        b_ = (-110, 30, 270, 470, pz - 30, pz + 30)
        out.append(bv.joint([
            part("Left rear fork blades", W("rear_fork_l", *b_), COL["fork"]),
            part("Lock pin tabs, inner and outer", W("pin_tabs", *b_), "#F59E0B"),
            part("Skirt guard", W("guard_l", *b_), COL["guard"]),
            part("Spokes (the pin passes between them)", W("rear_wheel_l", *b_), COL["wheel"]),
            part("Parking lock pin", W("lock_pin", *b_), COL["lockpin"])],
            OUT / "joint-07.png", "Joint 7: parking lock pin, seen from above (left rear wheel)",
            subtitle="The pin goes from the walking space through the inner tab, the guard, between the spokes and into the outer tab",
            elev=62, azim=-130, size=(8, 6)))
    if want(8):
        R = D["wheel_r"]
        b_ = (-95, 40, -470, -400, R - 40, R + 170)
        out.append(bv.joint([
            part("Right rear fork, outer blade", W("rear_fork_r", *b_), "#64748B"),
            part("Drum brake plate (hub cut away)", W("rear_wheel_r", -95, 40, -432, -408, R - 60, R + 170), COL["wheel"]),
            part("Brake reaction arm and clip", W("brake_arm_r", *b_), "#F59E0B"),
            part("Torque-arm tab (for the later motor)", W("torque_tab", *b_), "#DC2626")],
            OUT / "joint-08.png", "Joint 8: drum brake reaction arm and torque-arm tab (right rear)",
            subtitle="Seen from inside the wheel, ahead. The arm lies along the inside of the outer blade and is clipped to it; the tab is behind the blade",
            elev=15, azim=60, size=(8, 6)))
    if want(9):
        b_ = (325, 500, 40, 245, 115, 330)
        out.append(bv.joint([
            part("Cradle floor and walls", W("cradle", *b_), COL["cradle"]),
            part("Angle brackets, outside the walls", W("cradle_brackets", *b_), "#94A3B8"),
            part("Bearer under the floor", W("carrier", 325, 500, 40, 245, 115, 151), COL["carrier"])],
            OUT / "joint-09.png", "Joint 9: cradle rear left corner, seen from behind on the left",
            subtitle="Walls stand on the floor; brackets go outside so nothing catches a jerrycan; the floor rests on the bearer",
            elev=28, azim=150, size=(8, 6)))
    return out


# ----------------------------------------------------------------- assembly steps
def steps(only=None):
    out = []
    W = lambda k, *box_: win(S(*k) if isinstance(k, tuple) else S(k), *box_)  # noqa: E731

    def want(n):
        return only is None or only == n

    def st(n, done, new, title, sub, **kw):
        if want(n):
            out.append(bv.step(done, new, OUT / f"step-{n:02d}.png", f"Step {n}: {title}", subtitle=sub, **kw))
    t2 = D["t2"]
    fx = D["pivot_x"]
    hx = D["rear_ht_x"]
    FB = (fx - 260, fx + 120, t2 - 120, t2 + 120, 280, 1000)       # left front corner
    RB = (hx - 180, 330, t2 - 150, t2 + 120, 280, 1010)           # left rear corner
    if want(1):
        st(1, [part("Front head tube and caster arm", W("frame", *FB), COL["frame"])],
           [part("Lower cup", W("cups_front", *FB[:4], 600, 760), COL["cups"], (0, 0, -90)),
            part("Upper cup", W("cups_front", *FB[:4], 800, 900), COL["cups"], (0, 0, 90))],
           "headset cups into the four head tubes",
           "Left front shown; the same at all four. Press the cups square with a headset press or a threaded bar",
           elev=18, azim=45)
    if want(2):
        st(2, [part("Frame", W("frame", *RB), COL["frame"]), part("Rear head tube", W("rear_ht_l", *RB), COL["rear_ht"]),
               part("Cups", W("cups_rear", *RB), COL["cups"])],
           [part("Rear fork with tabs", W(("rear_fork_l", "pin_tabs"), *RB[:4], 0, 1010), COL["fork"], (0, 0, -260)),
            part("Lock collar", W("collars_rear", *RB), COL["collar"], (0, 0, 90)),
            part("Lock pin and R-clip", W("pins_rear", *RB), COL["pin"], (0, 0, 160))],
           "rear forks up into the rear head tubes",
           "Left shown. Steerer up through the head tube; collar and top cap; set the preload; pin in, R-clip on",
           elev=16, azim=130, label_done=False)
    if want(3):
        st(3, [part("Frame", W("frame", *FB), COL["frame"]), part("Cups", W("cups_front", *FB), COL["cups"])],
           [part("Front fork, trailing", W("front_fork_l", *FB[:4], 0, 1010), COL["fork"], (0, 0, -260)),
            part("Lock collar", W("collars_front", *FB), COL["collar"], (0, 0, 90)),
            part("Swivel lock pin", W("pins_front", *FB), COL["pin"], (0, 0, 160))],
           "front forks up into the front head tubes",
           "Left shown. Dropouts behind the steering axis (trailing); collar hole over the guide with the fork straight",
           elev=16, azim=40, label_done=False)
    REAR = (-420, 420, -470, 470, 0, 1010)
    rear_done = [part("Frame", W("frame", *REAR), COL["frame"]), part("Rear head tubes", W(("rear_ht_l", "rear_ht_r"), *REAR), COL["rear_ht"]),
                 part("Rear forks", W(("rear_fork_l", "rear_fork_r", "pin_tabs", "torque_tab", "cups_rear", "collars_rear", "pins_rear"), *REAR), COL["fork"])]
    if want(4):
        st(4, rear_done,
           [part("Left skirt guard and clips", S("guard_l", "guard_clips_l", "guard_bolts_l"), "#0EA5E9", (0, 260, 0)),
            part("Right skirt guard and clips", S("guard_r", "guard_clips_r", "guard_bolts_r"), "#0EA5E9", (0, -260, 0))],
           "skirt guards, before the wheels",
           "Two M6 bolts into the rail tabs; two rubber-lined clips with 5 mm spacers on the inner blade",
           elev=18, azim=150, label_done=False)
    guards = part("Skirt guards", S("guard_l", "guard_r", "guard_clips_l", "guard_clips_r", "guard_bolts_l", "guard_bolts_r"), COL["guard"])
    if want(5):
        st(5, rear_done + [guards],
           [part("Rear wheels with drum hubs", S("rear_wheel_l", "rear_wheel_r"), COL["wheel"], (0, 0, -300)),
            part("Reaction arms and clips", S("brake_arm_l", "brake_arm_r"), COL["arm"], (0, 0, -300))],
           "rear wheels into the rear forks",
           "Drum on the outside; hub up through the guard slot; axle nuts to the hub maker's torque; clip the reaction arm",
           elev=14, azim=150, label_done=False)
    FRONT = (1080, 1700, -470, 470, 0, 1010)
    front_done = [part("Frame", W("frame", *FRONT), COL["frame"]),
                  part("Front forks", W(("front_fork_l", "front_fork_r", "cups_front", "collars_front", "pins_front"), *FRONT), COL["fork"])]
    if want(6):
        st(6, front_done, [part("Front wheels", S("front_wheel_l", "front_wheel_r"), COL["wheel"], (0, 0, -300))],
           "front wheels into the front forks",
           "Axle nuts to the hub maker's torque; spin each wheel and swivel each fork through a full turn",
           elev=14, azim=35, label_done=False)
    allframe = ("frame", "rear_ht_l", "rear_ht_r", "carrier")
    wheels = ("rear_fork_l", "rear_fork_r", "front_fork_l", "front_fork_r", "pin_tabs", "torque_tab", "cups_front", "cups_rear",
              "collars_front", "collars_rear", "pins_front", "pins_rear", "rear_wheel_l", "rear_wheel_r", "front_wheel_l",
              "front_wheel_r", "brake_arm_l", "brake_arm_r", "guard_l", "guard_r", "guard_clips_l", "guard_clips_r")
    rolling = [part("Frame", S(*allframe), COL["frame"]), part("Wheels, forks and guards", S(*wheels), COL["wheel"])]
    if want(7):
        st(7, [part("Frame", W(allframe, -420, 420, -470, 470, 250, 1100), COL["frame"])],
           [part("Hip bar weldment with pad", S("hipbar", "pad_grips"), COL["hipbar"], (0, 0, 320)),
            part("Height pins, front to back", S("hip_pins"), "#DC2626", (-150, 0, 0))],
           "hip bar into the sleeves",
           "Pad and grips on first. Both posts into the sleeves together; height pin through sleeve and post, front to back",
           elev=20, azim=-130, label_done=False)
    if want(8):
        GB = (-260, 100, -380, -260, 880, 1010)
        st(8, [part("Right grip tube and hip bar", W("hipbar", *GB), COL["hipbar"])],
           [part("Brake lever with parking latch", S("lever"), COL["lever"], (-200, 0, 0)),
            part("Hand grip", W("pad_grips", -260, -60, -380, -260, 880, 1010), COL["pad"], (-320, 0, 0))],
           "brake lever and grip onto the right grip tube",
           "Lever first, blade under the grip; then the grip. Cable to a splitter, then one cable to each rear drum",
           elev=22, azim=-120, label_done=True)
    if want(9):
        st(9, rolling + [part("Hip bar", S("hipbar", "pad_grips", "hip_pins", "lever"), COL["hipbar"])],
           [part("Cradle", S("cradle", "cradle_pad", "cradle_brackets"), COL["cradle"], (0, 0, 380)),
            part("Four M6 bolts", S("cradle_bolts"), COL["bolt"], (0, 0, -120))],
           "cradle onto the bearers",
           "Lower it between the cross members; four M6 bolts down through the floor and bearers, nylocs underneath",
           elev=28, azim=-55, label_done=False)
    if want(10):
        pz = D["wheel_r"] + P["pin_dz"]
        LB = (-260, 300, 180, 480, 150, 900)
        st(10, [part("Frame", W(allframe, *LB), COL["frame"]), part("Left rear wheel, fork and guard",
                W(("rear_wheel_l", "rear_fork_l", "pin_tabs", "guard_l", "guard_clips_l", "brake_arm_l"), *LB), COL["wheel"])],
           [part("Parking lock pin", S("lock_pin"), COL["lockpin"], (0, -170, 0))],
           "parking lock pin",
           "From the walking space: through the inner tab, the guard and the spokes into the outer tab. Lanyard to the frame",
           elev=15, azim=-115, label_done=False)
    if want(11):
        st(11, rolling + [part("Hip bar and cradle", S("hipbar", "pad_grips", "lever", "cradle", "cradle_pad", "cradle_brackets"), COL["hipbar"]),
                          part("Lock pin", S("lock_pin"), COL["lockpin"])],
           [part("Four 20 L jerrycans (user's own)", S("cans"), COL["cans"], (0, 0, 420))],
           "first load: jerrycans and straps",
           "Lift each can in from the side over the rail, 2 x 2; strap each row down. Load only after the stops in section 6",
           elev=24, azim=-55, label_done=False)
    return out


if __name__ == "__main__":
    args = sys.argv[1:] or ["overview", "sheets", "joints", "steps"]
    fns = {"overview": overview, "sheets": sheets, "joints": joints, "steps": steps}
    OUT.mkdir(parents=True, exist_ok=True)
    for a in args:
        name, _, num = a.partition(":")
        r = fns[name]() if name == "overview" else fns[name](int(num) if num else None)
        print(a, "->", r)
