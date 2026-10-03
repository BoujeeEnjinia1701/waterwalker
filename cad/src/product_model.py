"""WaterWalker product appearance model (build123d), TRL 3, constructable design.

Finished-product look for photoreal renders of the first prototype as it is built (WWK-DDR-003 and the
decisions of 2026-10-02): the components of model.build_components() (frame with its rear brackets and
cradle carrier, forks, headsets and lock collars, fork tabs, brake arms, skirt guards and clips, hip bar,
service brake lever, the hold-to-release bail, spring unit and cables, plywood cradle with hand holds,
rating plates, parking lock pin and the optional two-motor assist kit) with product materials, plus
wheels with treaded tires and laced spokes, jerrycans, straps, the hip pad, rubber grips, reflectors and
end caps drawn on model.py's dimensions. The optional assist kit appears in the exploded view only.
Context is the shared clay mannequin walking inside the frame with its hands on the grips.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION.

Axes as model.py: X is the direction of travel (front is +X), Y across the carrier (left is +Y),
Z up; the rear axle is at X = 0 and the ground at Z = 0. See docs/REVIEW.md.

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from math import cos, radians, sin
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / ".kit"))

from build123d import (Axis, Box, Compound, Cylinder, Plane, Pos, RegularPolygon, Rot, Solid, Sphere, Torus,
                       Vector, extrude, fillet)
from model import PARAMS, derived, frame_members, member_length

TITLE = "WaterWalker: walk-inside four-wheel water carrier"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "internal", "context"], "explode": False, "el": 24, "az": -38,
     "note": "Product render from the front right and above (about 24 deg elevation); the user walks inside "
             "the frame toward the viewer, pushing the padded hip bar, with four 20 L jerrycans strapped "
             "in the cradle between the axles"},
    {"name": "exploded", "groups": ["shell", "internal", "accessory"], "explode": True, "el": 28, "az": -55,
     "note": "Exploded view from the front right and above (about 28 deg elevation): frame, four wheels and "
             "forks, hip bar and grips with the brake lever, cradle and jerrycans, drum brakes, skirt guards, "
             "parking lock pin, hold-to-release brake and the optional two-motor assist kit (hub motors, SwapCell pack and receiver, push sensor)"},
    {"name": "detail", "groups": ["shell", "internal"], "explode": False, "el": 18, "az": -145,
     "note": "Detail from the rear right, slightly above (about 18 deg elevation), without the person: the open "
             "walk-in rear, padded hip bar, rear-facing grips with the brake lever and the hold-to-release bail, "
             "rear drum brakes, skirt guards and the parking lock pin"},
]

# Mannequin: height and the joint angles that put both hands on the rear-facing grips while the
# hips stand just behind the pad (solved against mannequin_landmarks; see docs/REVIEW.md).
PERSON_H = 1750.0
PERSON_JOINTS = dict(torso_lean=13.0, head_tilt=-4.0,
                     shoulder_flex_l=-20.0, shoulder_flex_r=-20.0,
                     shoulder_abd_l=22.47, shoulder_abd_r=22.47,
                     elbow_flex_l=94.96, elbow_flex_r=94.96)
HAND_X = -PARAMS["grip_back"] + PARAMS["grip_len"] / 2   # middle of the rubber grips (model.py)

# Colours (restrained product palette; kit accent for the frame)
C_FRAME = "#0F766E"
C_FORK = "#23272E"
C_BLACK = "#1C1F24"
C_DARK = "#2B2F36"
C_TIRE = "#26292E"
C_RIM = "#C3C8CE"
C_SPOKE = "#AEB4BB"
C_HUB = "#B8BEC6"
C_METAL = "#9CA3AF"
C_ZINC = "#C9CDD3"
C_BAR = "#3A3F47"
C_PAD = "#30353C"
C_SEAM = "#4B525B"
C_GRIP = "#1F2227"
C_PLY = "#C9A26B"
C_PLY_EDGE = "#B88D55"
C_RUBBER = "#2F3237"
C_CAN = "#E0A80E"
C_CAN_CAP = "#1E40AF"
C_STRAP = "#3F4650"
C_BUCKLE = "#1C1F24"
C_GUARD = "#DADDE1"
C_LABEL = "#F4F4F2"
C_PRINT = "#2B2F36"
C_RED = "#C0262D"
C_REFL_R = "#B91C1C"
C_REFL_W = "#E5E7EB"
C_MOTOR = "#1C1F24"
C_PACK = "#3A3F47"
C_LED = "#22C55E"
C_CLAY = "#9CA3AF"


def _fillet_try(shape, edges, radii):
    """Fillet `edges` with the first radius that gives a valid solid; else return the input."""
    edges = list(edges)
    if not edges:
        return shape
    for r in radii:
        try:
            out = fillet(edges, r)
            if out.is_valid and out.volume > 0:
                return out
        except Exception:
            pass
    return shape


def _box(cx, cy, cz, sx, sy, sz):
    return Pos(cx, cy, cz) * Box(sx, sy, sz)


def _ycyl(x, y, z, r, h):
    return Pos(x, y, z) * Rot(90, 0, 0) * Cylinder(r, h)


def _xcyl(x, y, z, r, h):
    return Pos(x, y, z) * Rot(0, 90, 0) * Cylinder(r, h)


def _zcyl(x, y, z, r, h):
    return Pos(x, y, z) * Cylinder(r, h)


def _rod(a, b, r):
    a, b = Vector(*a), Vector(*b)
    d = b - a
    return Solid.make_cylinder(r, d.length, Plane(origin=a, z_dir=d.normalized()))


def _pipe(points, r):
    """Round tube through `points` with spherical joints (clean bends)."""
    out = None
    for a, c in zip(points, points[1:]):
        seg = _rod(a, c, r)
        out = seg if out is None else out + seg
    for q in points[1:-1]:
        out += Pos(*q) * Sphere(r)
    return out


def _comp(shapes):
    shapes = [s for s in shapes if s is not None]
    return Compound(children=shapes)


def _edges_par(s, axis):
    return s.edges().filter_by(axis)


def _hex_y(x, y, z, af, length):
    """Hex prism along Y (across flats `af`)."""
    return Pos(x, y + length / 2, z) * extrude(Plane.XZ * RegularPolygon(af / 1.732, 6), amount=length)


def _tube(p, sec, a, b, r):
    """Frame member as model.py (same section and span) with rounded corners along its length."""
    h, w, _ = p[sec]
    L = member_length(a, b)
    c = tuple((a[i] + b[i]) / 2 for i in range(3))
    if a[0] != b[0]:
        size, ax = (L, w, h), Axis.X
    elif a[1] != b[1]:
        size, ax = (w, L, h), Axis.Y
    else:
        size, ax = (h, w, L), Axis.Z
    t = Pos(*c) * Box(*size)
    return _fillet_try(t, _edges_par(t, ax), [r, r * 0.6])


def _wheel(P, D, x, y, drum):
    """Wheel parts about the axle at (x, y, R): tire, tread, rim, spokes, hub, axle and nuts."""
    R, tw = D["wheel_r"], P["tire_w"]
    tire = Pos(x, y, R) * Rot(90, 0, 0) * Torus(R - tw / 2, tw / 2)
    knobs = []
    n = 56
    for i in range(n):
        th = 360.0 * i / n
        for dy in ((-11.0,) if i % 2 else (11.0,)):
            rr = R - 0.8
            kx, kz = x + rr * cos(radians(th)), R + rr * sin(radians(th))
            knobs.append(Pos(kx, y + dy, kz) * Rot(0, 90 - th, 0) * Box(12, 16, 3.2))
        rr = R - 5.5
        for sgn in (1, -1):
            kx, kz = x + rr * cos(radians(th + 3)), R + rr * sin(radians(th + 3))
            knobs.append(Pos(kx, y + sgn * 22.5, kz) * Rot(0, 90 - th - 3, 0) * Box(9, 7, 3.0))
    tread = _comp(knobs)
    ro, ri = R - tw + 4, R - tw - 10
    rim = _ycyl(x, y, R, ro, 20) - _ycyl(x, y, R, ri, 22)
    rim = _fillet_try(rim, rim.edges().filter_by_position(Axis.Y, y - 12, y + 12), [1.2, 0.8])
    rim -= _ycyl(x, y, R, ri + 3, 16) - _ycyl(x, y, R, ri - 1, 18)      # rim bed channel
    valve = _rod((x, y, R - ri - 2), (x, y, R - ri + 20), 3.0)
    # 36 spokes, tangential lacing between two hub flanges and the rim
    fl_r, fl_y = (34.0 if drum else 30.0), 33.0
    spokes = []
    for i in range(36):
        side = 1 if i % 2 == 0 else -1
        a0 = 360.0 * i / 36
        lead = 18.0 if (i // 2) % 2 == 0 else -18.0
        a1 = a0 + lead
        p0 = (x + fl_r * cos(radians(a0)), y + side * fl_y, R + fl_r * sin(radians(a0)))
        p1 = (x + (ri + 1) * cos(radians(a1)), y + side * 3.0, R + (ri + 1) * sin(radians(a1)))
        spokes.append(_rod(p0, p1, 1.0))
        spokes.append(Pos(*p1) * Sphere(1.9))
    spokes = _comp(spokes)
    barrel = _ycyl(x, y, R, 20.0, 2 * fl_y)
    barrel = _fillet_try(barrel, barrel.edges(), [3.0, 1.5])
    hub = barrel
    for s in (1, -1):
        f = _ycyl(x, y + s * fl_y, R, fl_r + 5, 3.0)
        f = _fillet_try(f, f.edges(), [1.0, 0.5])
        hub += f
    hub += _ycyl(x, y, R, 5.0, P["old"] + 2 * (P["dropout_t"] + P["axle_proud"]))
    if not drum:
        for s in (1, -1):
            hub += _ycyl(x, y + s * (fl_y + 9), R, 14.0, 12.0)
    nuts = None
    yn = P["old"] / 2 + P["dropout_t"] + P["axle_proud"] / 2
    for s in (1, -1):
        nt = _hex_y(x, y + s * yn, R, 15.0, P["axle_proud"])
        nuts = nt if nuts is None else nuts + nt
    return tire, tread, rim, spokes, hub, nuts, valve


def _fork(P, D, x_axle, y, steer_x):
    """Rigid bicycle fork, round blades from the dropouts to the crown, crown, steerer and dropouts."""
    R = D["wheel_r"]
    cz = P["crown_z"]
    by = P["old"] / 2 + P["dropout_t"] / 2
    parts = []
    for s in (1, -1):
        parts.append(_rod((x_axle, y + s * by, R), (steer_x, y + s * by, cz + 4), 10.5))
        parts.append(_rod((x_axle + (steer_x - x_axle) * 0.45, y + s * by, R + (cz - R) * 0.45),
                          (steer_x, y + s * by, cz + 4), 12.0))
        dp = _box(x_axle, y + s * by, R + 6, 30, P["dropout_t"], 42)
        dp = _fillet_try(dp, _edges_par(dp, Axis.Y), [8.0, 5.0])
        parts.append(dp)
    crown = _box(steer_x, y, cz + 12, 42, P["old"] + 34, 24)
    crown = _fillet_try(crown, crown.edges(), [8.0, 5.0, 3.0])
    parts.append(crown)
    parts.append(_zcyl(steer_x, y, cz + 24 + P["head_len"] / 2 + 8, 14, P["head_len"] + 16))
    out = parts[0]
    for q in parts[1:]:
        out += q
    return out


def product_parts(P=PARAMS):
    """Appearance parts. The frame, forks, headsets, lock collars and pins, brake arms, guards, hip bar,
    brake levers, the hold-to-release brake and its cables, the cradle, the rating plates and the assist
    kit are the constructable components of model.build_components(), so every dimension and position
    comes from model.py; wheels, jerrycans, straps, the pad, grips, reflectors and end caps are drawn
    here for realism on model.py's dimensions."""
    from context_parts import mannequin, mannequin_landmarks
    from model import build_components
    C = build_components(P)
    D = derived(P)
    R, t2, ry, rz = D["wheel_r"], D["t2"], D["rail_y"], D["rail_z"]
    fx, az = P["front_x"], P["arm_z"]
    hx, hz = P["hip_x"], P["hip_z"]
    out = []

    def add(name, shape, color, material, bom, group, explode):
        out.append({"name": name, "shape": shape, "color": color, "material": material,
                    "bom": bom, "group": group, "explode": tuple(float(v) for v in explode)})

    def comp(*keys):
        return _comp([C[k].shape for k in keys])

    # ------------------------------------------------------------ frame (BOM 1), as model.py
    add("Steel tube frame, rear brackets and cradle carrier (powder coated)",
        comp("frame", "rear_ht_l", "rear_ht_r", "carrier"), C_FRAME, "painted", 1, "shell", (0, 0, 0))
    add("Headset cups", comp("cups_front", "cups_rear"), C_ZINC, "metal", 16, "shell", (0, 0, 0))
    add("Lock collars, plates and top caps", comp("collars_front", "collars_rear"), C_DARK, "metal", 16, "shell", (0, 0, 0))
    add("Steering lock pins", comp("pins_front", "pins_rear"), C_RED, "painted", 16, "shell", (0, 0, 120))
    add("Rated load and slope plates", C["plates"].shape, C_LABEL, "paper", 12, "shell", (0, 0, 0))

    caps = []
    for sy in (1, -1):
        caps.append(_box(D["rail_x0"] - 2.5, sy * ry, rz, 5, P["main"][1] - 2, P["main"][0] - 2))
        caps.append(_box(hx, sy * ry, P["sleeve_top"] + 2.5, P["sleeve"][0] - 2, P["sleeve"][1] - 2, 5) -
                    _box(hx, sy * ry, P["sleeve_top"] + 2.5, P["post"][0] + 1, P["post"][1] + 1, 7))
    add("Tube end caps", _comp(caps), C_BLACK, "plastic", 12, "shell", (0, 0, 0))
    refl = [_box(hx - P["sleeve"][0] / 2 - 1.0, sy * ry, 560, 2.0, 22, 60) for sy in (1, -1)]
    add("Rear reflectors", _comp(refl), C_REFL_R, "plastic", 12, "shell", (-60, 0, 0))
    refl = [_box(fx + P["main"][0] / 2 + 1.0, sy * ry, 620, 2.0, 22, 60) for sy in (1, -1)]
    add("Front reflectors", _comp(refl), C_REFL_W, "plastic", 12, "shell", (60, 0, 0))

    # ------------------------------------------------------------ wheels and forks (BOM 2, 3, 14)
    for (x, sy, drum, bom, lab, ex, fk, s_) in [
            (0.0, -1, True, 2, "right rear", (-450, -260, 0), "rear_fork_r", "r"),
            (0.0, 1, True, 2, "left rear", (-250, 260, 0), "rear_fork_l", "l"),
            (P["wheelbase"], -1, False, 3, "right front", (500, -260, 0), "front_fork_r", "r"),
            (P["wheelbase"], 1, False, 3, "left front", (500, 260, 0), "front_fork_l", "l")]:
        y = sy * t2
        tire, tread, rim, spokes, hub, nuts, valve = _wheel(P, D, x, y, drum)
        add(f"Tire, {lab}", tire, C_TIRE, "rubber", 14, "shell", ex)
        add(f"Tire tread, {lab}", tread, C_TIRE, "rubber", 14, "shell", ex)
        add(f"Rim, {lab}", rim, C_RIM, "metal", bom, "shell", ex)
        add(f"Spokes, {lab}", spokes, C_SPOKE, "metal", bom, "shell", ex)
        add(f"Hub, {lab}", hub, C_HUB, "metal", bom, "shell", ex)
        add(f"Axle nuts and valve, {lab}", _comp([nuts, valve]), C_ZINC, "metal", bom, "shell", ex)
        fex = (ex[0], ex[1], ex[2] + 120)
        add(f"{'Rear' if drum else 'Swivel caster'} fork, {lab}", C[fk].shape, C_FORK, "painted", bom, "shell", fex)
        if drum:
            dr = _ycyl(0, sy * (t2 + P["old"] / 2 - 16), R, 50, 22)
            dr = _fillet_try(dr, dr.edges(), [4.0, 2.0])
            add(f"Drum brake plate, {lab}", dr, C_METAL, "metal", 2, "shell", ex)
            add(f"Brake reaction arm and clip, {lab}", C[f"brake_arm_{s_}"].shape, C_METAL, "metal", 2, "shell", ex)
    add("Fork tabs: lock pin tabs and torque-arm tabs", comp("pin_tabs", "torque_tab", "torque_tab_l"),
        C_FORK, "painted", 1, "shell", (-350, 0, 120))

    # ------------------------------------------------------------ hip bar, pad, grips (BOM 4)
    EH = (60, 0, 380)
    add("Hip bar, posts and grip tubes", C["hipbar"].shape, C_BAR, "painted", 4, "shell", EH)
    add("Height pins", C["hip_pins"].shape, C_BLACK, "metal", 4, "shell", (60, 0, 200))
    pad = _ycyl(hx, 0, hz, P["pad_d"] / 2, P["pad_len"])
    pad = _fillet_try(pad, pad.edges(), [16.0, 10.0, 6.0])
    pad -= _ycyl(hx, 0, hz, P["hip_bar_d"] / 2, P["pad_len"] + 2)
    add("Hip pad (foam, fabric cover)", pad, C_PAD, "fabric", 4, "shell", EH)
    seams = [_ycyl(hx, sy * (P["pad_len"] / 2 - 60), hz, P["pad_d"] / 2 + 0.6, 3.0) -
             _ycyl(hx, sy * (P["pad_len"] / 2 - 60), hz, P["pad_d"] / 2 - 2, 4.0) for sy in (1, -1)]
    add("Hip pad seams", _comp(seams), C_SEAM, "fabric", 4, "shell", EH)
    rub, plugs = [], []
    g0, g1 = -P["grip_back"], -P["grip_back"] + P["grip_len"]
    for sy in (1, -1):
        gr = _xcyl((g0 + g1) / 2, sy * ry, hz, 16.0, g1 - g0)
        gr = _fillet_try(gr, gr.edges(), [3.0, 1.5])
        for k in range(8):
            gr -= _xcyl(g0 + 15 + 14 * k, sy * ry, hz, 20, 3.0) - _xcyl(g0 + 15 + 14 * k, sy * ry, hz, 15.0, 4.0)
        gr -= _xcyl((g0 + g1) / 2, sy * ry, hz, P["grip_d"] / 2, g1 - g0 + 2)
        rub.append(gr)
        pl = _xcyl(g0 - 3, sy * ry, hz, 15.0, 6)
        plugs.append(_fillet_try(pl, pl.edges(), [2.5, 1.2]))
    add("Rubber hand grips", _comp(rub), C_GRIP, "rubber", 4, "shell", EH)
    add("Grip end plugs", _comp(plugs), C_BLACK, "plastic", 4, "shell", EH)

    # ------------------------------------------------------------ brakes (BOM 7, 17)
    add("Brake lever with parking latch (right grip)", C["lever"].shape, C_DARK, "metal", 7, "shell", EH)
    add("Hold-to-release bail lever (left grip)", C["bail"].shape, C_RED, "painted", 17, "shell", EH)
    add("Hold-to-release spring unit with cable yoke", C["dm_unit"].shape, C_DARK, "metal", 17, "shell", (0, 120, 0))
    add("Brake cables and housing", comp("serv_cable", "dm_cables"), C_BLACK, "rubber", 17, "shell", (0, 0, 0))

    # ------------------------------------------------------------ cradle (BOM 5), as model.py
    EC = (0, 0, -300)
    add("Cradle floor and walls with hand holds (exterior plywood)", C["cradle"].shape, C_PLY, "wood", 5, "shell", EC)
    add("Cradle rubber pad", C["cradle_pad"].shape, C_RUBBER, "rubber", 5, "shell", EC)
    add("Cradle angle brackets", C["cradle_brackets"].shape, C_ZINC, "metal", 5, "shell", EC)
    x0, x1, hw = P["cr_x0"], D["cr_x1"], P["cr_hw"]
    L, cx, wt = x1 - x0, (x0 + x1) / 2, P["wall_t"]
    div = _box(cx, 0, P["cr_z"] + P["floor_t"] + P["pad_t"] + 60, L - 2 * wt - 4, 4, 120)
    add("Removable divider", div, C_PLY, "wood", 5, "internal", EC)

    # ------------------------------------------------------------ jerrycans (BOM 6)
    jl, jw, jh = P["jc"]
    z0 = D["can_z0"]
    can_x = (x0 + wt + 2 + jl / 2, x1 - wt - 2 - jl / 2)
    EJ = (0, 0, 650)
    cans, caps_, ribs = [], [], []
    for cxx in can_x:
        for cy in (jw / 2 + 5, -jw / 2 - 5):
            b = _box(cxx, cy, z0 + jh / 2, jl, jw, jh)
            b = _fillet_try(b, _edges_par(b, Axis.Z), [22.0, 16.0, 10.0])
            b = _fillet_try(b, b.faces().sort_by(Axis.Z)[-1].edges(), [14.0, 10.0, 6.0])
            h = _box(cxx - 40, cy, z0 + jh + 25, 160, 30, 50)
            h = _fillet_try(h, _edges_par(h, Axis.Y), [12.0, 8.0])
            h -= _box(cxx - 40, cy, z0 + jh + 20, 118, 40, 26)
            neck = _zcyl(cxx + 110, cy, z0 + jh + 12, 18, 26)
            cans.append(b + h + neck)
            cap = _zcyl(cxx + 110, cy, z0 + jh + 28, 23, 16)
            caps_.append(_fillet_try(cap, cap.faces().sort_by(Axis.Z)[-1].edges(), [3.0, 1.5]))
            so = 1 if cy > 0 else -1
            for dz in (-120, -40, 40, 120):
                ribs.append(_box(cxx, cy + so * (jw / 2 + 0.8), z0 + jh / 2 + dz, jl - 90, 1.6, 10))
    add("20 L jerrycans (x4, user's own)", _comp(cans), C_CAN, "plastic", 6, "internal", EJ)
    add("Jerrycan caps", _comp(caps_), C_CAN_CAP, "plastic", 6, "internal", (0, 0, 700))
    add("Jerrycan side ribs", _comp(ribs), C_CAN, "plastic", 6, "internal", EJ)
    top, wall_top = z0 + jh, D["wall_top"]
    straps = []
    for cxx in can_x:
        sx_ = cxx + 64
        straps.append(_box(sx_, 0, top + 1.2, 30, 2 * (jw + 5) + 2, 2.4))
        for sy in (1, -1):
            straps.append(_box(sx_, sy * (jw + 5 + 1.2), (wall_top + top) / 2 + 1, 30, 2.4, top - wall_top + 2))
    add("Cradle straps (webbing)", _comp(straps), C_STRAP, "fabric", 5, "internal", (0, 0, 820))

    # ------------------------------------------------------------ skirt guards (BOM 8), as model.py
    for s_, lab, sy in (("r", "right", -1), ("l", "left", 1)):
        add(f"Skirt guard, {lab} (HDPE)", C[f"guard_{s_}"].shape, C_GUARD, "plastic", 8, "shell", (-120, sy * 60, 0))
        add(f"Guard clips and bolts, {lab}", comp(f"guard_clips_{s_}", f"guard_bolts_{s_}"), C_ZINC, "metal", 8, "shell",
            (-120, sy * 90, 0))

    # ------------------------------------------------------------ parking lock pin (BOM 15)
    EP = (-450, 520, 250)
    add("Parking lock pin", C["lock_pin"].shape, C_RED, "painted", 15, "shell", EP)

    # ------------------------------------------------------------ optional assist kit (accessory), as model.py
    add("Optional hub motors, 250 W, 48 V (2)", C["motor"].shape, C_MOTOR, "painted", 9, "accessory", (-650, 0, 0))
    add("Optional SwapCell pack", C["pack"].shape, C_PACK, "plastic", 10, "accessory", (250, 0, 420))
    add("Optional SwapCell receiver, V1", C["receiver"].shape, C_DARK, "metal", 13, "accessory", (250, 0, 250))
    add("Optional push sensor and controller", C["sensor"].shape, C_DARK, "plastic", 11, "accessory", (450, -650, -150))

    # ------------------------------------------------------------ context: the user, walking inside
    lm = mannequin_landmarks(PERSON_H, "push", **PERSON_JOINTS)
    hand_fwd = -lm["hands"][0][1]                   # hands ahead of the pelvis in the figure's frame
    px_ = HAND_X - hand_fwd                          # pelvis x on the carrier
    person = Pos(px_, 0, 0) * Rot(0, 0, 90) * mannequin(PERSON_H, "push", **PERSON_JOINTS)
    add("Person, 1.75 m, walking inside, hands on the grips", person, C_CLAY, "clay", None, "context",
        (0, 0, 0))
    return out


def person_landmarks():
    """Mannequin landmarks in carrier coordinates (for checks)."""
    from context_parts import mannequin_landmarks
    lm = mannequin_landmarks(PERSON_H, "push", **PERSON_JOINTS)
    px_ = HAND_X + lm["hands"][0][1]
    tr = lambda q: (round(px_ - q[1], 1), round(q[0], 1), q[2])
    return {k: [tr(q) for q in v] if isinstance(v, list) else tr(v)
            for k, v in lm.items() if k != "joints"}


if __name__ == "__main__":
    for p in product_parts():
        s = p["shape"]
        print(f"{p['name']:55s} {p['group']:9s} {p['material']:8s} valid={s.is_valid} vol={s.volume / 1000:9.2f} cm3")
