"""WaterWalker product appearance model (build123d), TRL 3.

Finished-product look for photoreal renders of the first prototype: a powder-coated steel tube frame
with rounded tube corners, end caps, headset cups, dropout tabs, reflectors and a rating plate;
four 26 in wheels with treaded tires, alloy rims, laced spokes, hubs and axle nuts; rigid rear forks
and swivel caster forks with drop-pin locks; the hip bar with a stitched foam pad, telescopic posts,
clamp collars, rubber grips and the brake lever with its cables to both rear drum brakes; the
plywood cradle with its rubber pad, divider, corner brackets and two webbing straps over four 20 L
jerrycans; HDPE skirt guards; and the red-ringed parking lock pin. The optional assist kit (hub
motor, SwapCell pack, push sensor and receiver) appears in the exploded view only, as in the concept
media. Context is the shared clay mannequin walking inside the frame and pushing the hip bar.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION.

Every main dimension and interface comes from PARAMS, derived() and frame_members() in model.py.
Axes as model.py: X is the direction of travel (front is +X), Y across the carrier (left is +Y),
Z up; the rear axle is at X = 0 and the ground at Z = 0. See docs/REVIEW.md, session 2026-09-26.

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
             "parking lock pin and the optional assist kit (hub motor, SwapCell pack and receiver, push sensor)"},
    {"name": "detail", "groups": ["shell", "internal"], "explode": False, "el": 18, "az": -145,
     "note": "Detail from the rear right, slightly above (about 18 deg elevation), without the person: the open "
             "walk-in rear, padded hip bar, rear-facing grips with the brake lever, rear drum brakes, skirt "
             "guards and the parking lock pin"},
]

# Mannequin: height and the joint angles that put both hands on the rear-facing grips while the
# hips stand just behind the pad (solved against mannequin_landmarks; see docs/REVIEW.md).
PERSON_H = 1750.0
PERSON_JOINTS = dict(torso_lean=13.0, head_tilt=-4.0,
                     shoulder_flex_l=-20.0, shoulder_flex_r=-20.0,
                     shoulder_abd_l=22.47, shoulder_abd_r=22.47,
                     elbow_flex_l=94.96, elbow_flex_r=94.96)
HAND_X = 0.0                   # grip point along the grips (x), just behind the hip bar posts

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
    from context_parts import mannequin, mannequin_landmarks
    D = derived(P)
    R, t2, ry, rz = D["wheel_r"], D["t2"], D["rail_y"], D["rail_z"]
    fx, az, pvx = P["front_x"], P["arm_z"], D["pivot_x"]
    hx, hz = P["hip_x"], P["hip_z"]
    head_z = P["crown_z"] + 24 + P["head_len"] / 2 + 6
    out = []

    def add(name, shape, color, material, bom, group, explode):
        out.append({"name": name, "shape": shape, "color": color, "material": material,
                    "bom": bom, "group": group, "explode": tuple(float(v) for v in explode)})

    # ------------------------------------------------------------ frame (BOM 1)
    radii = {"main": 4.0, "cross": 3.0, "sleeve": 3.5, "hanger": 2.5}
    tubes = [_tube(P, sec, a, b, radii[sec]) for _, sec, a, b in frame_members(P)]
    heads, cups = [], []
    for sy in (1, -1):
        for x in (pvx, 0.0):
            h = _zcyl(x, sy * t2, head_z, P["head_d"] / 2, P["head_len"])
            heads.append(_fillet_try(h, h.edges(), [2.0, 1.0]))
            for dz in (-1, 1):
                c = _zcyl(x, sy * t2, head_z + dz * (P["head_len"] / 2 + 4), P["head_d"] / 2 + 2.5, 8)
                cups.append(_fillet_try(c, c.edges(), [1.5, 0.8]))
            cups.append(_zcyl(x, sy * t2, head_z + P["head_len"] / 2 + 13, 16, 10))     # top cap and nut
        tab = _box(0, sy * (ry + P["main"][1] / 2 - 4), R, 60, 8, 70)
        tubes.append(_fillet_try(tab, _edges_par(tab, Axis.Y), [10.0, 6.0]))
    tubes += heads
    # assist mounting points, as model.py: torque-arm tab (right rear) and sensor boss (right sleeve)
    ta = _box(-40, -(t2 + P["old"] / 2 + P["dropout_t"] / 2), R + 60, 60, 6, 40)
    tubes.append(_fillet_try(ta, _edges_par(ta, Axis.Y), [8.0, 5.0]))
    boss = _box(hx + 30, -ry, P["sleeve_top"] - 40, 30, 30, 60)
    tubes.append(_fillet_try(boss, _edges_par(boss, Axis.Z), [3.0, 2.0]))
    add("Steel tube frame (powder coated)", _comp(tubes), C_FRAME, "painted", 1, "shell", (0, 0, 0))
    add("Headset cups and top caps", _comp(cups), C_ZINC, "metal", 3, "shell", (0, 0, 0))

    rx = P["rx_plate"]
    rpx = fx + P["main"][1] / 2 - 5 + rx[0] / 2
    rpz = az + P["main"][0] / 2 + rx[2] / 2
    plate = _box(rpx, 0, rpz, *rx)
    plate = _fillet_try(plate, _edges_par(plate, Axis.Z), [10.0, 6.0])
    for sx in (-1, 1):
        for sy in (-1, 1):
            plate -= _zcyl(rpx + sx * 45, sy * 120, rpz, 4.5, 10)
    add("Receiver mounting plate (galvanized)", plate, C_ZINC, "metal", 1, "shell", (0, 0, 0))

    caps = []
    for sy in (1, -1):
        c = _box(-17.0, sy * ry, rz, 5, P["main"][1] - 2, P["main"][0] - 2)
        caps.append(_fillet_try(c, c.faces().sort_by(Axis.X)[0].edges(), [2.0, 1.0]))
        c = _box(fx, sy * (t2 + 17.0), az, P["main"][0] - 2, 5, P["main"][1] - 2)
        caps.append(c)
    add("Tube end caps", _comp(caps), C_BLACK, "plastic", 12, "shell", (0, 0, 0))

    refl = []
    for sy in (1, -1):
        r_ = _box(hx - 15 - 1.0, sy * ry, 560, 2.0, 22, 60)
        refl.append(_fillet_try(r_, _edges_par(r_, Axis.X), [4.0, 2.0]))
    add("Rear reflectors", _comp(refl), C_REFL_R, "plastic", 12, "shell", (-60, 0, 0))
    refl = []
    for sy in (1, -1):
        r_ = _box(fx + 20 + 1.0, sy * ry, 620, 2.0, 22, 60)
        refl.append(_fillet_try(r_, _edges_par(r_, Axis.X), [4.0, 2.0]))
    add("Front reflectors", _comp(refl), C_REFL_W, "plastic", 12, "shell", (60, 0, 0))

    # rating plate and wordmark on the right side rail (thin raised parts)
    ly = -ry - P["main"][1] / 2 - 0.2
    add("Rated load and slope plate", _box(640, ly, rz, 150, 0.4, 30), C_LABEL, "paper", 12, "shell", (0, -60, 0))
    ink = [_box(640 - 50, ly - 0.3, rz + 6, 36, 0.3, 9), _box(640 + 18, ly - 0.3, rz + 7, 80, 0.3, 3),
           _box(640 + 18, ly - 0.3, rz + 1, 80, 0.3, 3), _box(640, ly - 0.3, rz - 8, 130, 0.3, 3)]
    add("Rating plate print", _comp(ink), C_PRINT, "paper", 12, "shell", (0, -60, 0))
    add("WaterWalker wordmark", _box(900, ly, rz + 2, 140, 0.4, 12), C_LABEL, "paper", 12, "shell", (0, -60, 0))

    # ------------------------------------------------------------ wheels and forks (BOM 2, 3, 14)
    for (x, sy, drum, bom, lab, ex) in [
            (0.0, -1, True, 2, "right rear", (-450, -260, 0)), (0.0, 1, True, 2, "left rear", (-250, 260, 0)),
            (P["wheelbase"], -1, False, 3, "right front", (500, -260, 0)),
            (P["wheelbase"], 1, False, 3, "left front", (500, 260, 0))]:
        y = sy * t2
        tire, tread, rim, spokes, hub, nuts, valve = _wheel(P, D, x, y, drum)
        add(f"Tire, {lab}", tire, C_TIRE, "rubber", 14, "shell", ex)
        add(f"Tire tread, {lab}", tread, C_TIRE, "rubber", 14, "shell", ex)
        add(f"Rim, {lab}", rim, C_RIM, "metal", bom, "shell", ex)
        add(f"Spokes, {lab}", spokes, C_SPOKE, "metal", bom, "shell", ex)
        add(f"Hub, {lab}", hub, C_HUB, "metal", bom, "shell", ex)
        add(f"Axle nuts and valve, {lab}", _comp([nuts, valve]), C_ZINC, "metal", bom, "shell", ex)
        steer = 0.0 if drum else pvx
        fk = _fork(P, D, x, y, steer)
        fex = (ex[0], ex[1], ex[2] + 120)
        add(f"{'Fixed' if drum else 'Swivel caster'} fork, {lab}", fk, C_FORK, "painted", bom, "shell", fex)
        if not drum:
            pin = _zcyl(pvx - 30, y, head_z + P["head_len"] / 2 - 10, 4, 50)
            knob = Pos(pvx - 30, y, head_z + P["head_len"] / 2 + 20) * Sphere(9.0)
            add(f"Swivel lock drop pin, {lab}", _comp([pin, knob]), C_RED, "painted", 3, "shell",
                (ex[0], ex[1], 200))

    # ------------------------------------------------------------ drum brakes (BOM 7)
    for sy, lab in ((-1, "right"), (1, "left")):
        y = sy * (t2 + P["old"] / 2 - 16)
        dr = _ycyl(0, y, R, 50, 22)
        dr = _fillet_try(dr, dr.edges(), [4.0, 2.0])
        for k in range(4):
            dr += _ycyl(0, y, R, 52, 1.6) if k == 0 else _ycyl(0, y - sy * (6 - 4 * k), R, 51.5, 1.6)
        arm = _box(60, y + sy * 6, R - 10, 120, 8, 16)
        arm = _fillet_try(arm, _edges_par(arm, Axis.Y), [6.0, 3.0])
        dr += arm
        add(f"Drum brake plate, {lab} rear", dr, C_METAL, "metal", 7, "shell",
            (-450 if sy < 0 else -250, sy * 420, 0))

    # ------------------------------------------------------------ hip bar, posts and grips (BOM 4)
    EH = (60, 0, 380)
    bar = _ycyl(hx, 0, hz, P["hip_bar_d"] / 2, 2 * ry + 40)
    bar = _fillet_try(bar, bar.edges(), [4.0, 2.0])
    grips_tube = []
    for sy in (1, -1):
        g = _xcyl((hx - P["grip_back"]) / 2, sy * ry, hz, 14.0, hx + P["grip_back"])
        grips_tube.append(g)
    add("Hip bar and grip tubes", _comp([bar] + grips_tube), C_BAR, "painted", 4, "shell", EH)
    pad = _ycyl(hx, 0, hz, P["pad_d"] / 2, P["pad_len"])
    pad = _fillet_try(pad, pad.edges(), [16.0, 10.0, 6.0])
    add("Hip pad (foam, fabric cover)", pad, C_PAD, "fabric", 4, "shell", EH)
    seams = [_ycyl(hx, sy * (P["pad_len"] / 2 - 60), hz, P["pad_d"] / 2 + 0.6, 3.0) -
             _ycyl(hx, sy * (P["pad_len"] / 2 - 60), hz, P["pad_d"] / 2 - 2, 4.0) for sy in (1, -1)]
    seams.append(_box(hx - P["pad_d"] / 2 - 0.2, 0, hz, 1.6, P["pad_len"] - 60, 3.0) &
                 _ycyl(hx, 0, hz, P["pad_d"] / 2 + 0.6, P["pad_len"]))
    add("Hip pad seams", _comp(seams), C_SEAM, "fabric", 4, "shell", EH)

    posts, dots, collars = [], [], []
    pz0 = P["sleeve_top"] - 150
    for sy in (1, -1):
        pt = _box(hx, sy * ry, (pz0 + hz) / 2, 25, 25, hz - pz0)
        posts.append(_fillet_try(pt, _edges_par(pt, Axis.Z), [2.5, 1.5]))
        for z in (855, 885, 915):
            dots.append(_ycyl(hx, sy * (ry + 12.5 + 0.2), z, 3.5, 0.4))
        col = _box(hx, sy * ry, P["sleeve_top"] + 6, 38, 38, 14)
        col = _fillet_try(col, _edges_par(col, Axis.Z), [5.0, 3.0])
        col -= _box(hx, sy * ry, P["sleeve_top"] + 6, 25.5, 25.5, 20)
        lever = _box(hx - 26, sy * (ry + 12), P["sleeve_top"] + 6, 26, 8, 10)
        lever = _fillet_try(lever, lever.edges(), [3.0, 1.5])
        knob = _ycyl(hx, sy * (ry + 23), P["sleeve_top"] + 34, 7.0, 8.0)
        knob = _fillet_try(knob, knob.edges(), [2.0, 1.0])
        collars += [col, lever, knob]
    add("Telescopic hip bar posts", _comp(posts), C_ZINC, "metal", 4, "shell", EH)
    add("Post height holes", _comp(dots), C_BLACK, "plastic", 4, "shell", EH)
    add("Clamp collars and height pins", _comp(collars), C_BLACK, "plastic", 4, "shell", (60, 0, 200))

    rub, plugs = [], []
    g0, g1 = -110.0, 40.0
    for sy in (1, -1):
        gr = _xcyl((g0 + g1) / 2, sy * ry, hz, 17.5, g1 - g0)
        gr = _fillet_try(gr, gr.edges(), [3.0, 1.5])
        for k in range(9):
            gr -= _xcyl(g0 + 22 + 13 * k, sy * ry, hz, 20, 3.0) - _xcyl(g0 + 22 + 13 * k, sy * ry, hz, 16.6, 4.0)
        rub.append(gr)
        pl = _xcyl(-P["grip_back"] - 2, sy * ry, hz, 15.0, 6)
        plugs.append(_fillet_try(pl, pl.edges(), [2.5, 1.2]))
    add("Rubber hand grips", _comp(rub), C_GRIP, "rubber", 4, "shell", EH)
    add("Grip end plugs", _comp(plugs), C_BLACK, "plastic", 4, "shell", EH)

    # ------------------------------------------------------------ brake lever and cables (BOM 7)
    lx = g0 - 14
    clamp = _xcyl(lx, -ry, hz, 19, 16)
    clamp = _fillet_try(clamp, clamp.edges(), [2.5, 1.2])
    clamp += _box(lx, -ry, hz - 24, 22, 20, 18)
    blade = _box(lx + 70, -ry, hz - 30, 150, 10, 7)
    blade = _fillet_try(blade, _edges_par(blade, Axis.X), [3.0, 1.5])
    latch = _box(lx + 8, -ry - 18, hz - 12, 14, 10, 10)
    add("Brake lever with parking latch", _comp([clamp, blade, latch]), C_DARK, "metal", 7, "shell", EH)
    cy_r, cy_l = -ry - 26, ry + 26
    cables = [
        _pipe([(lx, -ry - 8, hz - 30), (lx - 20, cy_r, hz - 90), (-30, cy_r, 860), (-30, cy_r, 800),
               (-30, -(t2 + 74), 700), (-30, -(t2 + 74), 430), (125, -(t2 + 46), R - 8)], 2.6),
        _pipe([(lx, -ry + 8, hz - 30), (hx - 30, -ry + 30, hz - 20), (hx - 30, ry - 30, hz - 20),
               (hx - 30, ry + 26, hz - 60), (-30, cy_l, 860), (-30, cy_l, 800),
               (-30, t2 + 74, 700), (-30, t2 + 74, 430), (125, t2 + 46, R - 8)], 2.6),
    ]
    add("Brake cables and housing", _comp(cables), C_BLACK, "rubber", 7, "shell", (0, 0, 0))

    # ------------------------------------------------------------ cradle (BOM 5)
    x0, x1, hw = P["cr_x0"], D["cr_x1"], P["cr_hw"]
    L, cx = x1 - x0, (x0 + x1) / 2
    wt, wh, ft = P["wall_t"], P["wall_h"], P["floor_t"]
    EC = (0, 0, -300)
    floor = _box(cx, 0, P["cr_z"] + ft / 2, L, 2 * hw, ft)
    floor = _fillet_try(floor, _edges_par(floor, Axis.Z), [8.0, 5.0])
    wz = P["cr_z"] + ft + wh / 2
    walls = []
    for sy in (1, -1):
        w = _box(cx, sy * (hw - wt / 2), wz, L, wt, wh)
        w = _fillet_try(w, w.faces().sort_by(Axis.Z)[-1].edges().filter_by(Axis.X), [1.8, 1.0])
        w -= _box(cx - L / 4, sy * (hw - wt / 2), wz + wh / 2 - 30, 90, 10, 26)      # hand holds
        w -= _box(cx + L / 4, sy * (hw - wt / 2), wz + wh / 2 - 30, 90, 10, 26)
        walls.append(w)
    for x in (x0 + wt / 2, x1 - wt / 2):
        w = _box(x, 0, wz, wt, 2 * hw - 2 * wt, wh)
        walls.append(_fillet_try(w, w.faces().sort_by(Axis.Z)[-1].edges().filter_by(Axis.Y), [1.8, 1.0]))
    add("Cradle floor (exterior plywood)", floor, C_PLY_EDGE, "wood", 5, "shell", EC)
    add("Cradle walls (plywood)", _comp(walls), C_PLY, "wood", 5, "shell", EC)
    pad_c = _box(cx, 0, P["cr_z"] + ft + P["pad_t"] / 2, L - 2 * wt, 2 * hw - 2 * wt, P["pad_t"])
    add("Cradle rubber pad", pad_c, C_RUBBER, "rubber", 5, "shell", EC)
    brk = []
    for x, sx in ((x0, 1), (x1, -1)):
        for sy in (1, -1):
            b_ = _box(x + sx * 20, sy * (hw + 1.0), wz + 20, 40, 2.0, 40) + \
                 _box(x - sx * 1.0, sy * (hw - 20), wz + 20, 2.0, 40, 40)
            brk.append(b_)
    add("Cradle corner brackets", _comp(brk), C_ZINC, "metal", 12, "shell", EC)
    div = _box(cx, 0, P["cr_z"] + ft + P["pad_t"] + 60, L - 2 * wt - 4, 4, 120)
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
            b = _fillet_try(b, b.faces().sort_by(Axis.Z)[0].edges(), [6.0, 4.0])
            h = _box(cxx - 40, cy, z0 + jh + 25, 160, 30, 50)
            h = _fillet_try(h, _edges_par(h, Axis.Y), [12.0, 8.0])
            h -= _box(cxx - 40, cy, z0 + jh + 20, 118, 40, 26)
            h = _fillet_try(h, h.edges().filter_by(Axis.X), [4.0, 2.0])
            neck = _zcyl(cxx + 110, cy, z0 + jh + 12, 18, 26)
            b = b + h + neck
            cans.append(b)
            cap = _zcyl(cxx + 110, cy, z0 + jh + 28, 23, 16)
            cap = _fillet_try(cap, cap.faces().sort_by(Axis.Z)[-1].edges(), [3.0, 1.5])
            for k in range(18):
                a = 360.0 * k / 18
                cap -= _zcyl(cxx + 110 + 23.5 * cos(radians(a)), cy + 23.5 * sin(radians(a)), z0 + jh + 26, 2.0, 12)
            caps_.append(cap)
            so = 1 if cy > 0 else -1
            for dz in (-120, -40, 40, 120):
                r_ = _box(cxx, cy + so * (jw / 2 + 0.8), z0 + jh / 2 + dz, jl - 90, 1.6, 10)
                ribs.append(_fillet_try(r_, _edges_par(r_, Axis.Y), [4.0, 2.0]))
    add("20 L jerrycans (x4, user's own)", _comp(cans), C_CAN, "plastic", 6, "internal", EJ)
    add("Jerrycan caps", _comp(caps_), C_CAN_CAP, "plastic", 6, "internal", (0, 0, 700))
    add("Jerrycan side ribs", _comp(ribs), C_CAN, "plastic", 6, "internal", EJ)

    # webbing straps over the cans with cam buckles (BOM 5)
    top = z0 + jh
    wall_top = D["wall_top"]
    straps, buckles = [], []
    for cxx in can_x:
        sx_ = cxx + 64
        straps.append(_box(sx_, 0, top + 1.2, 30, 2 * (jw + 5) + 2, 2.4))
        for sy in (1, -1):
            yo = sy * (jw + 5 + 1.2)
            straps.append(_box(sx_, yo, (wall_top + top) / 2 + 1, 30, 2.4, top - wall_top + 2))
            straps.append(_box(sx_, sy * (jw + 5 + hw) / 2 + sy * 0.5, wall_top + 1.2, 30, hw - jw - 5 + 4, 2.4))
            straps.append(_box(sx_, sy * (hw + 1.2), wall_top - 40, 30, 2.4, 82))
        bk = _box(sx_, -70, top + 5, 40, 34, 8)
        bk = _fillet_try(bk, _edges_par(bk, Axis.Z), [4.0, 2.0])
        bk = _fillet_try(bk, bk.faces().sort_by(Axis.Z)[-1].edges(), [2.0, 1.0])
        buckles.append(bk)
    add("Cradle straps (webbing)", _comp(straps), C_STRAP, "fabric", 5, "internal", (0, 0, 820))
    add("Strap cam buckles", _comp(buckles), C_BUCKLE, "plastic", 5, "internal", (0, 0, 830))

    # ------------------------------------------------------------ skirt guards (BOM 8)
    for sy, lab in ((-1, "right"), (1, "left")):
        y = sy * (t2 - P["old"] / 2 + 5 + P["guard_t"] / 2)
        g = _box(0, y, P["guard_z"], P["guard_l"], P["guard_t"], P["guard_h"])
        g = _fillet_try(g, _edges_par(g, Axis.Y), [40.0, 25.0, 12.0])
        g -= _ycyl(0, y, R, 60, 10)
        if sy > 0:
            g -= _ycyl(P["pin_x"], y, R + P["pin_dz"], P["pin_d"] / 2 + 2, 10)
        add(f"Skirt guard, {lab} (HDPE)", g, C_GUARD, "plastic", 8, "shell", (-120, sy * 60, 0))
        bolts = []
        for bx, bz in ((-230, 600), (230, 600), (-230, 250), (230, 250)):
            b_ = _ycyl(bx, y - sy * 2.6, bz, 7.0, 2.4)
            bolts.append(_fillet_try(b_, b_.edges(), [0.8, 0.4]))
        add(f"Skirt guard bolts, {lab}", _comp(bolts), C_ZINC, "metal", 12, "shell", (-120, sy * 90, 0))

    # ------------------------------------------------------------ parking lock pin (BOM 15)
    y_in = t2 - P["old"] / 2 - P["dropout_t"] / 2
    pz = R + P["pin_dz"]
    EP = (-450, 520, 250)
    pin = _ycyl(P["pin_x"], t2 - 25, pz, P["pin_d"] / 2, 110)
    pin = _fillet_try(pin, pin.edges(), [2.0, 1.0])
    tab = _box(P["pin_x"] / 2, y_in, pz, abs(P["pin_x"]) + 30, 6, 30)
    tab = _fillet_try(tab, _edges_par(tab, Axis.Y), [6.0, 3.0])
    add("Parking lock pin and tab", _comp([pin, tab]), C_ZINC, "metal", 15, "shell", EP)
    ring = Pos(P["pin_x"], t2 - 84, pz) * Rot(90, 0, 0) * Torus(14, 3.2)
    ring += _ycyl(P["pin_x"], t2 - 80, pz, 6.5, 8)
    add("Lock pin pull ring", ring, C_RED, "painted", 15, "shell", EP)
    lan = _pipe([(P["pin_x"], t2 - 84, pz - 14), (P["pin_x"] + 20, t2 - 88, pz - 90),
                 (P["pin_x"] + 60, ry - 20, rz + 60), (P["pin_x"] + 90, ry - 16, rz + 22)], 1.6)
    add("Lock pin lanyard", lan, C_DARK, "fabric", 15, "shell", EP)

    # ------------------------------------------------------------ optional assist kit (accessory)
    EM = (-650, -720, 0)
    mo = _ycyl(0, -t2, R, P["motor_d"] / 2, P["motor_w"])
    mo = _fillet_try(mo, mo.edges(), [8.0, 5.0])
    for s in (1, -1):
        mo -= _ycyl(0, -t2 + s * P["motor_w"] / 2, R, P["motor_d"] / 2 - 18, 3.0) - \
              _ycyl(0, -t2 + s * P["motor_w"] / 2, R, P["motor_d"] / 2 - 21, 4.0)
    add("Optional hub motor, 250 W, 48 V", mo, C_MOTOR, "painted", 9, "accessory", EM)
    fl = []
    for s in (1, -1):
        fl.append(_ycyl(0, -t2 + s * (P["motor_w"] / 2 - 4), R, P["motor_d"] / 2 + 6, 3.0) -
                  _ycyl(0, -t2 + s * (P["motor_w"] / 2 - 4), R, P["motor_d"] / 2 - 4, 4.0))
        for k in range(8):
            a = radians(22.5 + 45 * k)
            fl.append(_ycyl(52 * cos(a), -t2 + s * (P["motor_w"] / 2 + 0.6), R + 52 * sin(a), 3.5, 2.0))
    fl.append(_ycyl(0, -t2, R, 5.0, P["old"] + 28))
    fl.append(_pipe([(0, -t2 - 36, R - 14), (-30, -t2 - 44, R - 60), (-40, -t2 - 44, R - 120)], 3.5))
    add("Hub motor flanges, axle and cable", _comp(fl), C_METAL, "metal", 9, "accessory", EM)

    pk = P["pack"]
    px0 = fx + P["main"][1] / 2 + 25
    pz0 = az + P["main"][0] / 2 + rx[2] + 8
    pcx = px0 + pk[0] / 2
    EK = (250, 0, 420)
    pack = _box(pcx, 0, pz0 + pk[2] / 2, *pk)
    pack = _fillet_try(pack, _edges_par(pack, Axis.Y), [12.0, 8.0])
    pack = _fillet_try(pack, pack.faces().sort_by(Axis.Y)[0].edges(), [4.0, 2.0])
    add("Optional SwapCell pack", pack, C_PACK, "plastic", 10, "accessory", EK)
    hnd = _box(pcx, pk[1] / 2 + P["pack_handle"] / 2, pz0 + pk[2] / 2, 22, P["pack_handle"], 60)
    hnd = _fillet_try(hnd, _edges_par(hnd, Axis.X), [8.0, 5.0])
    hnd -= _box(pcx, pk[1] / 2 + 14, pz0 + pk[2] / 2, 30, 14, 40)
    band = _box(pcx, 0, pz0 + pk[2] + 0.2, pk[0] - 24, pk[1] - 60, 0.4)
    add("SwapCell handle and accent band", _comp([hnd, band]), C_FRAME, "painted", 10, "accessory", EK)
    leds = [_zcyl(pcx + 22, -110 + 14 * k, pz0 + pk[2] + 0.6, 3.0, 1.2) for k in range(3)]
    add("SwapCell charge lights (lit)", _comp(leds), C_LED, "emissive", 10, "accessory", EK)

    rcx = pcx
    ER = (250, 0, 250)
    rcv = [_box(rcx, 0, pz0 - 4, pk[0] + 20, pk[1] + 20, 8)]
    for s in (1, -1):
        gd = _box(rcx + s * (pk[0] / 2 + 7), 0, pz0 + 25, 8, pk[1], 50)
        rcv.append(_fillet_try(gd, _edges_par(gd, Axis.Y), [3.0, 1.5]))
    rc = _box(rcx, -(pk[1] / 2 + 12), pz0 + pk[2] / 2, pk[0] + 20, 24, pk[2] + 10)
    rcv.append(_fillet_try(rc, _edges_par(rc, Axis.Y), [5.0, 3.0]))
    add("Optional SwapCell receiver, V1", _comp(rcv), C_DARK, "metal", 13, "accessory", ER)
    lev = _box(rcx + pk[0] / 2 + 16, 60, pz0 + 40, 6, 120, 14)
    lev = _fillet_try(lev, lev.edges(), [2.5, 1.2])
    add("Receiver preload lever", lev, C_FRAME, "painted", 13, "accessory", ER)

    ES = (450, -650, -150)
    sen = _box(hx + 30, -ry, P["sleeve_top"] + 20, 40, 40, 40)
    sen = _fillet_try(sen, sen.edges(), [5.0, 3.0])
    add("Optional push sensor and controller", sen, C_DARK, "plastic", 11, "accessory", ES)
    sled = _ycyl(hx + 30, -ry - 20.4, P["sleeve_top"] + 30, 3.0, 1.2)
    add("Push sensor status light (lit)", sled, C_LED, "emissive", 11, "accessory", ES)

    # ------------------------------------------------------------ context: the user, walking inside
    lm = mannequin_landmarks(PERSON_H, "push", **PERSON_JOINTS)
    hand_fwd = -lm["hands"][0][1]                   # hands ahead of the pelvis in the figure's frame
    px_ = HAND_X - hand_fwd                          # pelvis x on the carrier
    person = Pos(px_, 0, 0) * Rot(0, 0, 90) * mannequin(PERSON_H, "push", **PERSON_JOINTS)
    add("Person, 1.75 m, walking inside and pushing the hip bar", person, C_CLAY, "clay", None, "context",
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
