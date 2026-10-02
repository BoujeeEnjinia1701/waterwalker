"""WaterWalker parametric model (build123d), TRL 3, constructable design (WWK-DDR-003).

Run from the repo root:
    python cad/src/model.py            exports STEP into cad/step and STL into cad/stl, then prints the checks
    python cad/src/model.py --check    prints the constructability checks only

Every component of the first prototype is modelled as it is made or bought, so that the build plan
(WWK-BLD-001, cad/src/build_plan_media.py) and the drawings come from one source:
build_components() returns each component by a short key. build_parts() groups them by BOM line for the
concept media and the general arrangement. Sections and positions are sized in WWK-CAL-001
(docs/04-calcs/01-sizing.md), which imports PARAMS, derived() and frame_members() from this file.

Axes: X is the direction of travel (front is +X), Y is across the carrier (+Y is the left side as the
user walks), Z is up. The rear axle is at X = 0 and the ground is at Z = 0. Dimensions in mm.
"""
import math
import sys
from dataclasses import dataclass
from pathlib import Path

# Top-level parameters (mm). Edit these, not the geometry below.
PARAMS = {
    # Wheels: 26 in (ETRTO 559) with 2.1 in (54 mm) tires; 2.4 in (61 mm) also fits
    "bead_d": 559.0, "tire_w": 54.0, "tire_w_max": 61.0,
    "old": 100.0,            # hub over-locknut width; front-type hub, all four wheels
    "dropout_t": 6.0, "axle_proud": 8.0,   # dropout plate and axle nut beyond it
    "blade": (22.0, 12.0),   # fork blade, fore-aft x across (massing of a round-bladed fork)
    "track": 770.0,          # wheel plane to wheel plane
    "wheelbase": 1530.0,     # rear axle to front axle
    "trail": 60.0,           # fork offset: caster trail at the front; rear head tube this far behind the rear axle
    "swivel_clear": 15.0,    # clearance from the swept tire to the front risers
    # Frame sections: height x width x wall (mm)
    "main": (40.0, 30.0, 1.2),   # side rails, front risers, caster arms, front cross members (RHS); WWK-DDR-002
    "cross": (25.0, 25.0, 1.5),  # rear cross member, rear head tube brackets, cradle bearers
    "sleeve": (30.0, 30.0, 1.5), # hip bar upright sleeves
    "post": (25.0, 25.0, 1.5),   # telescopic hip bar posts inside the sleeves
    "hanger": (20.0, 20.0, 1.5), # cradle hangers
    "front_x": 1150.0,       # front risers
    "arm_z": 815.0,          # caster arms, above the tires
    "crown_z": 700.0,        # underside of fork crowns
    "head_len": 140.0, "head_d": 44.0, "head_id": 34.0,   # head tubes: external-cup headsets (EC34)
    "cup_h": 6.0, "steerer_d": 28.6,
    "rear_bracket_z": (745.0, 805.0),   # the two rear head tube brackets (WWK-DDR-003)
    # Steering locks: a collar on each steerer carries a lock plate; a pin drops through it into a guide
    "collar": (40.0, 15.0), "lock_plate": (25.0, 3.0), "lock_r": 45.0, "guide_d": 14.0, "lock_pin_d": 8.0,
    # Hip bar and grips
    "hip_x": 60.0, "hip_z": 950.0, "hip_min": 850.0, "hip_max": 1050.0,
    "sleeve_top": 820.0, "grip_back": 230.0, "hip_bar_d": 32.0, "pad_d": 90.0, "pad_len": 480.0,
    "grip_d": 22.2, "grip_len": 130.0,  # 22.2 mm grip tubes take standard bicycle grips and brake levers
    "post_len": 364.0, "hip_pin_z": 775.0, "hip_pin_d": 6.0,
    # Cradle and its carrier
    "cr_x0": 350.0, "cr_hw": 215.0, "cr_z": 150.0,
    "floor_t": 6.0, "pad_t": 2.0, "wall_t": 4.0, "wall_h": 160.0,   # thinner cradle, WWK-DDR-002
    "rear_cross_x": 332.5,   # rear cross member, behind the cradle (WWK-DDR-003)
    "bearer_y": 150.0,       # cradle bearers, each side of the centre line
    "cradle_bolt_x": (400.0, 1080.0),
    # Containers (user's own)
    "jc": (360.0, 175.0, 430.0),
    # Skirt guards
    "guard_l": 540.0, "guard_h": 420.0, "guard_t": 3.0, "guard_z": 420.0, "guard_slot": 120.0,
    "guard_tab_x": (150.0, 240.0), "clip_z": (450.0, 600.0),
    # Positive parking lock pin through the left rear wheel (WWK-DDR-002), held at both ends (WWK-DDR-003)
    "pin_d": 10.0, "pin_x": -60.0, "pin_dz": 200.0,
    # Assist mounting points (SwapCell interface v0.3) and optional assist kit
    "pack": (90.0, 340.0, 80.0),        # SwapCell body, x (depth), y (length), z (width)
    "pack_handle": 35.0, "pack_plug": 18.0,
    "rx_plate": (140.0, 300.0, 3.0),    # receiver mounting plate on the upper cross member
    "motor_d": 180.0, "motor_w": 60.0,  # geared hub motor shell, right rear wheel
}
P = PARAMS


def derived(p=PARAMS):
    """Dimensions that follow from the parameters."""
    d = {}
    d["wheel_r"] = (p["bead_d"] + 2 * p["tire_w"]) / 2
    d["wheel_r_max"] = (p["bead_d"] + 2 * p["tire_w_max"]) / 2
    d["t2"] = p["track"] / 2
    d["rail_y"] = d["t2"] - p["old"] / 2 - p["main"][1] / 2
    d["rail_z"] = d["wheel_r"]
    d["pivot_x"] = p["wheelbase"] + p["trail"]
    d["rear_ht_x"] = -p["trail"]
    d["head_z"] = p["crown_z"] + 24 + p["cup_h"] + p["head_len"] / 2
    d["cr_x1"] = p["front_x"] - p["main"][0] / 2
    d["walk_width"] = 2 * (d["rail_y"] - p["main"][1] / 2)
    d["overall_width"] = 2 * (d["t2"] + p["old"] / 2 + p["dropout_t"] + p["axle_proud"])
    d["sweep_r"] = p["trail"] + d["wheel_r_max"]                    # caster sweep radius in plan
    d["riser_gap"] = d["pivot_x"] - (p["front_x"] + p["main"][0] / 2) - d["sweep_r"]
    d["wall_top"] = p["cr_z"] + p["floor_t"] + p["wall_h"]
    d["rail_top"] = d["rail_z"] + p["main"][0] / 2
    d["rail_bot"] = d["rail_z"] - p["main"][0] / 2
    d["rail_x0"] = p["hip_x"] - p["sleeve"][0] / 2                  # rails end flush with the sleeve's rear face
    d["rail_x1"] = p["front_x"] + p["main"][0] / 2
    d["can_z0"] = p["cr_z"] + p["floor_t"] + p["pad_t"]
    d["bearer_z"] = p["cr_z"] - p["cross"][0] / 2                   # bearer centre, top face under the floor
    d["arm_root_x"] = p["front_x"] + p["main"][1] / 2               # front face of the upper cross member
    d["clearance"] = d["bearer_z"] - p["cross"][0] / 2              # ground clearance under the bearers
    return d


def _arm_ends(p=PARAMS, sy=1):
    """Caster arm axis: from the front face of the upper cross member above the riser to the head tube."""
    d = derived(p)
    a = (d["arm_root_x"] - 5.0, sy * d["rail_y"], p["arm_z"])
    h = (d["pivot_x"], sy * d["t2"], p["arm_z"])
    L = math.hypot(h[0] - a[0], h[1] - a[1])
    u = ((h[0] - a[0]) / L, (h[1] - a[1]) / L)
    end = (h[0] - u[0] * (p["head_d"] / 2 - 1.0), h[1] - u[1] * (p["head_d"] / 2 - 1.0), p["arm_z"])
    return a, end, u


def frame_members(p=PARAMS):
    """Tube members of the welded frame and cradle carrier: (name, section, start, end), axis to axis
    along each member, ends where they butt on the next member. Used for the geometry and for the
    mass roll-up in WWK-CAL-001."""
    d = derived(p)
    ry, rz, fx, az = d["rail_y"], d["rail_z"], p["front_x"], p["arm_z"]
    h40 = p["main"][0] / 2
    c2 = p["cross"][0] / 2
    m = []
    for sy, side in ((1, "left"), (-1, "right")):
        m += [
            (f"side rail {side}", "main", (d["rail_x0"], sy * ry, rz), (d["rail_x1"], sy * ry, rz)),
            (f"front riser {side}", "main", (fx, sy * ry, d["rail_top"]), (fx, sy * ry, az - h40)),
            (f"caster arm {side}", "main", *_arm_ends(p, sy)[:2]),
            (f"hip upright sleeve {side}", "sleeve", (p["hip_x"], sy * ry, d["rail_top"]), (p["hip_x"], sy * ry, p["sleeve_top"])),
        ]
        for k, z in enumerate(p["rear_bracket_z"]):
            lvl = ("lower", "upper")[k]
            m += [
                (f"rear bracket arm {lvl} {side}", "cross", (d["rear_ht_x"] - c2, sy * ry, z),
                 (p["hip_x"] - p["sleeve"][0] / 2, sy * ry, z)),
                (f"rear bracket stub {lvl} {side}", "cross", (d["rear_ht_x"], sy * (ry + c2), z),
                 (d["rear_ht_x"], sy * (d["t2"] - p["head_d"] / 2), z)),
            ]
        by = sy * p["bearer_y"]
        m += [
            (f"cradle bearer {side}", "cross", (p["rear_cross_x"] - 10, by, d["bearer_z"]), (fx + 10, by, d["bearer_z"])),
            (f"cradle hanger rear {side}", "hanger", (p["rear_cross_x"], by, p["cr_z"]), (p["rear_cross_x"], by, rz - c2)),
            (f"cradle hanger front {side}", "hanger", (fx, by, p["cr_z"]), (fx, by, d["rail_bot"])),
        ]
    m += [
        ("rear cross member", "cross", (p["rear_cross_x"], -(ry - 15), rz), (p["rear_cross_x"], ry - 15, rz)),
        ("front lower cross member", "main", (fx, -(ry - 15), rz), (fx, ry - 15, rz)),
        ("upper cross member", "main", (fx, -(ry + 15), az), (fx, ry + 15, az)),
    ]
    return m


def member_length(a, b):
    return math.dist(a, b)


# ------------------------------------------------------------------ geometry helpers
def _b3d():
    import build123d as b
    return b


def bx(x0, x1, y0, y1, z0, z1):
    b = _b3d()
    return b.Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * b.Box(x1 - x0, y1 - y0, z1 - z0)


def ycyl(x, y0, y1, z, r):
    b = _b3d()
    return b.Pos(x, (y0 + y1) / 2, z) * b.Rot(90, 0, 0) * b.Cylinder(r, abs(y1 - y0))


def zcyl(x, y, z0, z1, r):
    b = _b3d()
    return b.Pos(x, y, (z0 + z1) / 2) * b.Cylinder(r, z1 - z0)


def xcyl(x0, x1, y, z, r):
    b = _b3d()
    return b.Pos((x0 + x1) / 2, y, z) * b.Rot(0, 90, 0) * b.Cylinder(r, abs(x1 - x0))


def fuse(shapes):
    out = None
    for s in shapes:
        if s is None:
            continue
        out = s if out is None else out + s
    return out


def oriented_box(a, c, sy, sz, up=(0.0, 0.0, 1.0), extend=0.0):
    """A box from point a to point c (its axis), sy wide and sz deep across it. up sets which way sz
    points (it is made square to the axis)."""
    b = _b3d()
    d = [c[i] - a[i] for i in range(3)]
    L = math.sqrt(sum(v * v for v in d))
    u = [v / L for v in d]
    dot = sum(up[i] * u[i] for i in range(3))
    z = [up[i] - dot * u[i] for i in range(3)]
    if math.sqrt(sum(v * v for v in z)) < 1e-6:
        z = [1.0, 0.0, 0.0]
    mid = [(a[i] + c[i]) / 2 for i in range(3)]
    pl = b.Plane(origin=tuple(mid), x_dir=tuple(u), z_dir=tuple(z))
    return pl.location * b.Box(L + 2 * extend, sy, sz)


def tube(p, sec, a, c, hollow=True):
    """Rectangular tube between two axis points. Horizontal members carry their height h vertically;
    uprights carry h along X."""
    h, w, t = p[sec]
    vertical = abs(a[0] - c[0]) < 1e-6 and abs(a[1] - c[1]) < 1e-6
    up = (1.0, 0.0, 0.0) if vertical else (0.0, 0.0, 1.0)
    outer = oriented_box(a, c, w, h, up)
    if not hollow:
        return outer
    return outer - oriented_box(a, c, w - 2 * t, h - 2 * t, up, extend=1.0)


@dataclass
class Comp:
    name: str
    shape: object
    bom: int | None
    kind: str            # made, bought, fixing, context
    group: str           # base, load, assist, context


# ------------------------------------------------------------------ components
def _fork(p, axle_x, y, steer_x):
    """Rigid 26 in bicycle fork, bought: dropouts with axle slots, blades raked from the dropouts to the
    crown, crown and 1 1/8 in steerer. The offset (axle to steering axis) is the trail."""
    d = derived(p)
    R = d["wheel_r"]
    bw, bt = p["blade"]
    parts = []
    for s in (1, -1):
        yi, yo = y + s * p["old"] / 2, y + s * (p["old"] / 2 + p["dropout_t"])
        drop = bx(axle_x - bw / 2, axle_x + bw / 2, min(yi, yo), max(yi, yo), R - 15, R + 40)
        drop -= bx(axle_x - 5, axle_x + 5, min(yi, yo) - 1, max(yi, yo) + 1, R - 16, R) + ycyl(axle_x, yi - s, yo + s, R, 5)
        yb0, yb1 = y + s * p["old"] / 2, y + s * (p["old"] / 2 + bt)
        blade = oriented_box((axle_x, (yb0 + yb1) / 2, R + 40), (steer_x, (yb0 + yb1) / 2, p["crown_z"] + 4),
                             bw, bt, up=(0, 1, 0))
        parts += [drop, blade]
    crown = bx(steer_x - 20, steer_x + 20, y - 65, y + 65, p["crown_z"], p["crown_z"] + 24)
    steer = zcyl(steer_x, y, p["crown_z"] + 24, d["head_z"] + p["head_len"] / 2 + p["cup_h"] + 2 + p["collar"][1] - 3,
                 p["steerer_d"] / 2)
    return fuse(parts + [crown, steer])


def blade_shape(p, axle_x, y, steer_x, s):
    """One fork blade (s = +1 on the +Y side of the wheel), as in _fork()."""
    d = derived(p)
    bw, bt = p["blade"]
    yb0, yb1 = y + s * p["old"] / 2, y + s * (p["old"] / 2 + bt)
    return oriented_box((axle_x, (yb0 + yb1) / 2, d["wheel_r"] + 40), (steer_x, (yb0 + yb1) / 2, p["crown_z"] + 4),
                        bw, bt, up=(0, 1, 0))


def blade_x(p, axle_x, steer_x, z):
    """Fore-aft position of a fork blade's centre line at height z."""
    d = derived(p)
    z0, z1 = d["wheel_r"] + 40, p["crown_z"] + 4
    return axle_x + (steer_x - axle_x) * (z - z0) / (z1 - z0)


def _wheel(p, x, y, hub_r, drum=False):
    b = _b3d()
    d = derived(p)
    R, tw = d["wheel_r"], p["tire_w"]
    tire = b.Pos(x, y, R) * b.Rot(90, 0, 0) * b.Torus(R - tw / 2, tw / 2)
    rim = ycyl(x, y - 9, y + 9, R, R - tw + 4) - ycyl(x, y - 10, y + 10, R, R - tw - 10)
    hub = ycyl(x, y - p["old"] / 2 + 8, y + p["old"] / 2 - 8, R, hub_r)          # hub barrel and flanges
    hub += ycyl(x, y - p["old"] / 2, y + p["old"] / 2, R, 12)                     # cones and locknuts
    axle = ycyl(x, y - p["old"] / 2 - p["dropout_t"] - p["axle_proud"], y + p["old"] / 2 + p["dropout_t"] + p["axle_proud"], R, 5)
    nuts = fuse([ycyl(x, y + s * (p["old"] / 2 + p["dropout_t"]), y + s * (p["old"] / 2 + p["dropout_t"] + p["axle_proud"]), R, 8)
                 for s in (1, -1)])
    spokes = fuse([b.Pos(x, y, R) * b.Rot(0, a, 0) * b.Box(2 * (R - tw), 4, 6) for a in range(0, 180, 30)])
    w = fuse([tire, rim, hub, axle, nuts, spokes])
    if drum:   # brake plate on the outboard side of the hub, inside the over-locknut width
        so = 1 if y > 0 else -1
        w += ycyl(x, y + so * (p["old"] / 2 - 27), y + so * (p["old"] / 2 - 5), R, 50)
    return w


def build_components(p=PARAMS):
    """Every component of the first prototype (and the optional assist kit), keyed by a short name."""
    b = _b3d()
    d = derived(p)
    R, t2, ry = d["wheel_r"], d["t2"], d["rail_y"]
    C = {}

    def add(key, name, shape, bom, kind="made", group="base"):
        C[key] = Comp(name, shape, bom, kind, group)

    hx, hz = d["rear_ht_x"], d["head_z"]
    ht0, ht1 = hz - p["head_len"] / 2, hz + p["head_len"] / 2
    c_top = ht1 + p["cup_h"] + 2          # collar sits 2 mm above the top cup
    plate_z = (c_top, c_top + p["lock_plate"][1])

    def head_tube(x, y):
        return zcyl(x, y, ht0, ht1, p["head_d"] / 2) - zcyl(x, y, ht0 - 1, ht1 + 1, p["head_id"] / 2)

    def guide(x, y, z0):
        g = zcyl(x, y, z0, c_top - 4, p["guide_d"] / 2) - zcyl(x, y, z0 - 1, c_top, p["lock_pin_d"] / 2 + 0.5)
        return g

    # ---- 1 Frame weldment (members, front head tubes, mounting plates, tabs, pin guides)
    fr = []
    for name, sec, a, c in frame_members(p):
        if name.startswith(("rear bracket", "cradle")) or name == "rear cross member":
            continue
        fr.append(tube(p, sec, a, c))
    for sy in (1, -1):
        fr.append(head_tube(d["pivot_x"], sy * t2))
        _, _, u = _arm_ends(p, sy)
        gx, gy = d["pivot_x"] - u[0] * p["lock_r"], sy * t2 - u[1] * p["lock_r"]
        fr.append(guide(gx, gy, p["arm_z"] + p["main"][0] / 2 - 0.5))
        for x in p["guard_tab_x"]:       # skirt guard tabs, 25 x 5 flat bar on the rail's outer face, tapped M6
            y0 = sy * (ry + p["main"][1] / 2)
            fr.append(bx(x - 12.5, x + 12.5, min(y0, y0 + sy * 5), max(y0, y0 + sy * 5), d["rail_bot"], d["rail_top"])
                      - ycyl(x, y0 - 6, y0 + 6, d["rail_z"], 2.5))
    rx = p["rx_plate"]
    fr.append(bx(p["front_x"], p["front_x"] + rx[0], -rx[1] / 2, rx[1] / 2, p["arm_z"] + 20, p["arm_z"] + 20 + rx[2]))
    # sensor tab: 4 mm plate standing forward from the right sleeve, above the hip bar pin
    sx0 = p["hip_x"] + p["sleeve"][0] / 2
    fr.append(bx(sx0, sx0 + 40, -ry - 2, -ry + 2, p["sleeve_top"] - 35, p["sleeve_top"] - 5)
              - ycyl(sx0 + 25, -ry - 3, -ry + 3, p["sleeve_top"] - 20, 3.25))
    frame = fuse(fr)
    for sy in (1, -1):
        _, _, u = _arm_ends(p, sy)
        gx, gy = d["pivot_x"] - u[0] * p["lock_r"], sy * t2 - u[1] * p["lock_r"]
        frame -= zcyl(gx, gy, p["arm_z"] + p["main"][0] / 2 - 10, p["arm_z"] + p["main"][0] / 2 + 1, p["lock_pin_d"] / 2 + 0.5)
        frame -= xcyl(p["hip_x"] - 20, p["hip_x"] + 20, sy * ry, p["hip_pin_z"], p["hip_pin_d"] / 2 + 0.25)
    add("frame", "Frame weldment", frame, 1)

    # rear head tubes on their two brackets, welded to the sleeves (part of the frame)
    for sy, side in ((1, "l"), (-1, "r")):
        pieces = [head_tube(hx, sy * t2)]
        for name, sec, a, c in frame_members(p):
            if name.startswith("rear bracket") and name.endswith("left" if sy > 0 else "right"):
                pieces.append(tube(p, sec, a, c))
        zt = p["rear_bracket_z"][1] + p["cross"][0] / 2
        pieces.append(guide(hx, sy * (t2 - p["lock_r"]), zt - 0.5))
        rh = fuse(pieces) - zcyl(hx, sy * (t2 - p["lock_r"]), zt - 10, zt + 1, p["lock_pin_d"] / 2 + 0.5)
        add(f"rear_ht_{side}", "Rear head tube and brackets" + (" (left)" if sy > 0 else " (right)"), rh, 1)

    # cradle carrier: two bearers and four hangers (part of the frame), drilled for the cradle bolts
    car = [tube(p, sec, a, c) for name, sec, a, c in frame_members(p) if name.startswith("cradle")]
    car.append(tube(p, "cross", *[m[2:] for m in frame_members(p) if m[0] == "rear cross member"][0]))
    carrier = fuse(car)
    for x in p["cradle_bolt_x"]:
        for sy in (1, -1):
            carrier -= zcyl(x, sy * p["bearer_y"], d["bearer_z"] - 20, p["cr_z"] + 1, 3.3)
    add("carrier", "Rear cross member and cradle carrier", carrier, 1)

    # ---- headsets (bought), lock collars with plates (made), steering lock pins (bought)
    cups, collars, pins = [], [], []
    for (x, y, tx, ty) in ([(d["pivot_x"], sy * t2) + (lambda u: (d["pivot_x"] - u[0] * p["lock_r"], sy * t2 - u[1] * p["lock_r"]))(_arm_ends(p, sy)[2])
                            for sy in (1, -1)] +
                           [(hx, sy * t2, hx, sy * (t2 - p["lock_r"])) for sy in (1, -1)]):
        for z0, z1 in ((ht0 - p["cup_h"], ht0), (ht1, ht1 + p["cup_h"])):
            cups.append(zcyl(x, y, z0, z1, p["head_d"] / 2) - zcyl(x, y, z0 - 1, z1 + 1, p["steerer_d"] / 2 + 0.3))
        col = zcyl(x, y, c_top, c_top + p["collar"][1], p["collar"][0] / 2) - zcyl(x, y, c_top - 1, c_top + p["collar"][1] + 1, p["steerer_d"] / 2)
        ang = math.atan2(ty - y, tx - x)
        L = p["lock_r"] + 14
        plate = b.Pos(x, y, (plate_z[0] + plate_z[1]) / 2) * b.Rot(0, 0, math.degrees(ang)) * b.Pos(L / 2, 0, 0) * b.Box(L, p["lock_plate"][0], p["lock_plate"][1])
        plate -= zcyl(tx, ty, plate_z[0] - 1, plate_z[1] + 1, p["lock_pin_d"] / 2 + 0.25)
        plate -= zcyl(x, y, plate_z[0] - 1, plate_z[1] + 1, p["steerer_d"] / 2)
        cap = zcyl(x, y, c_top + p["collar"][1], c_top + p["collar"][1] + 4, 18)
        collars.append(col + plate + cap)
        pin = zcyl(tx, ty, (p["arm_z"] + p["main"][0] / 2 if abs(x - hx) > 1 else p["rear_bracket_z"][1] + p["cross"][0] / 2) - 6,
                   plate_z[1] + 18, p["lock_pin_d"] / 2)
        pin += zcyl(tx, ty, plate_z[1] + 18, plate_z[1] + 24, 9)
        pins.append(pin)
    add("cups_front", "Headsets, front", fuse(cups[:4]), 16, "bought")
    add("cups_rear", "Headsets, rear", fuse(cups[4:]), 16, "bought")
    add("collars_front", "Lock collars, front (2)", fuse(collars[:2]), 16)
    add("collars_rear", "Lock collars, rear (2)", fuse(collars[2:]), 16)
    add("pins_front", "Swivel lock pins (2)", fuse(pins[:2]), 16, "bought")
    add("pins_rear", "Rear fork lock pins (2)", fuse(pins[2:]), 16, "bought")

    # ---- 2 rear wheels and forks; 3 front wheels and forks
    for sy, side in ((1, "l"), (-1, "r")):
        y = sy * t2
        add(f"rear_fork_{side}", "Rear fork" + (" (left)" if sy > 0 else " (right)"), _fork(p, 0.0, y, hx), 2, "bought")
        add(f"rear_wheel_{side}", "Rear wheel with drum hub" + (" (left)" if sy > 0 else " (right)"), _wheel(p, 0.0, y, 40, drum=True), 2, "bought")
        add(f"front_fork_{side}", "Front fork" + (" (left)" if sy > 0 else " (right)"), _fork(p, p["wheelbase"], y, d["pivot_x"]), 3, "bought")
        add(f"front_wheel_{side}", "Front wheel" + (" (left)" if sy > 0 else " (right)"), _wheel(p, p["wheelbase"], y, 35), 3, "bought")
        # drum brake reaction arm along the outer blade, held by a clip (bought with the hub)
        so = sy
        yo = y + so * p["old"] / 2
        z0, z1 = R + 30, R + 140
        xa, xb = blade_x(p, 0.0, hx, z0), blade_x(p, 0.0, hx, z1)
        arm = oriented_box((xa, yo - so * 2.5, z0), (xb, yo - so * 2.5, z1), 16, 5, up=(0, 1, 0))
        zc = R + 120
        xc = blade_x(p, 0.0, hx, zc)
        ring = oriented_box((xc, y + so * 56, zc - 10), (xc, y + so * 56, zc + 10), 30, 26, up=(0, 1, 0)) \
            - oriented_box((blade_x(p, 0.0, hx, zc - 12), y + so * 56, zc - 12), (blade_x(p, 0.0, hx, zc + 12), y + so * 56, zc + 12), 23, 13, up=(0, 1, 0)) \
            - oriented_box((blade_x(p, 0.0, hx, zc - 12), yo - so * 2.5, zc - 12), (blade_x(p, 0.0, hx, zc + 12), yo - so * 2.5, zc + 12), 17, 5.2, up=(0, 1, 0))
        add(f"brake_arm_{side}", "Brake reaction arm and clip" + (" (left)" if sy > 0 else " (right)"), arm + ring, 2, "bought")

    # fork tabs welded on by the frame builder: lock pin tabs on the left rear fork, torque-arm tab on the right
    pz = R + p["pin_dz"]
    xb_ = blade_x(p, 0.0, hx, pz)
    tabs = []
    for yc in (t2 - p["old"] / 2 - p["blade"][1] / 2, t2 + p["old"] / 2 + p["blade"][1] / 2):
        tab = bx(p["pin_x"] - 15, xb_, yc - 3, yc + 3, pz - 15, pz + 15)
        tab -= blade_shape(p, 0.0, t2, hx, 1 if yc > t2 else -1)
        tab -= ycyl(p["pin_x"], yc - 4, yc + 4, pz, p["pin_d"] / 2 + 0.25)
        tabs.append(tab)
    add("pin_tabs", "Lock pin tabs (left rear fork)", fuse(tabs), 15)
    tz = R + 60
    yct = -(t2 + p["old"] / 2 + p["blade"][1] / 2)
    tt = bx(-70, blade_x(p, 0.0, hx, tz), yct - 3, yct + 3, tz - 20, tz + 20)
    tt -= blade_shape(p, 0.0, -t2, hx, -1) + bx(-11, 11, yct - 4, yct + 4, R - 20, R + 41)
    tt -= ycyl(-50, yct - 4, yct + 4, tz, 5.5)
    add("torque_tab", "Torque-arm tab (right rear fork)", tt, 1)

    # ---- 8 skirt guards with a slot for the hub, two rail tabs and two clips on the inner blade
    for sy, side in ((1, "l"), (-1, "r")):
        y0 = sy * (ry + p["main"][1] / 2 + 5)
        y1 = y0 + sy * p["guard_t"]
        ya, yb_ = min(y0, y1), max(y0, y1)
        zg0, zg1 = p["guard_z"] - p["guard_h"] / 2, p["guard_z"] + p["guard_h"] / 2
        g = bx(-p["guard_l"] / 2, p["guard_l"] / 2, ya, yb_, zg0, zg1)
        sw = p["guard_slot"] / 2
        g -= bx(-sw, sw, ya - 1, yb_ + 1, zg0 - 1, R) + ycyl(0, ya - 1, yb_ + 1, R, sw)
        for x in p["guard_tab_x"]:
            g -= ycyl(x, ya - 1, yb_ + 1, d["rail_z"], 3.3)
        if sy > 0:
            g -= ycyl(p["pin_x"], ya - 1, yb_ + 1, pz, p["pin_d"] / 2 + 2)
        add(f"guard_{side}", "Skirt guard" + (" (left)" if sy > 0 else " (right)"), g, 8)
        # two clips on the inner blade: a rubber-lined band clip and a 5 mm spacer, one M6 bolt each
        clips = []
        for zc in p["clip_z"]:
            xc = blade_x(p, 0.0, hx, zc)
            yi = sy * (t2 - p["old"] / 2)
            clips.append(bx(xc - 15, xc + 15, min(yi, y0), max(yi, y0), zc - 10, zc + 10))
        add(f"guard_clips_{side}", "Guard clips" + (" (left)" if sy > 0 else " (right)"), fuse(clips), 8, "bought")
        bolts = []
        for x in p["guard_tab_x"]:
            yf = sy * (ry + p["main"][1] / 2)
            bolts.append(ycyl(x, yf, y1 + sy * 0.01, d["rail_z"], 3.0) + ycyl(x, y1, y1 + sy * 5, d["rail_z"], 6))
        add(f"guard_bolts_{side}", "Guard bolts" + (" (left)" if sy > 0 else " (right)"), fuse(bolts), 12, "fixing")

    # ---- 15 parking lock pin, through the inner tab, the guard, the spokes and the outer tab
    y_in = t2 - p["old"] / 2 - p["blade"][1] - 3
    y_out = t2 + p["old"] / 2 + p["blade"][1] + 2       # ends 2 mm past the outer tab, inside the axle nuts
    lp = ycyl(p["pin_x"], y_in - 10, y_out, pz, p["pin_d"] / 2)
    lp += ycyl(p["pin_x"], y_in - 18, y_in - 10, pz, 14) - ycyl(p["pin_x"], y_in - 19, y_in - 9, pz, 10)
    lp += ycyl(p["pin_x"], y_in - 12, y_in - 10, pz, 7)
    add("lock_pin", "Parking lock pin", lp, 15)

    # ---- 4 hip bar weldment, pad, grips, pin; 7 brake lever
    hb_z = p["hip_z"]
    r_bar = p["hip_bar_d"] / 2
    hb = ycyl(p["hip_x"], -(ry + 20), ry + 20, hb_z, r_bar) - ycyl(p["hip_x"], -(ry + 21), ry + 21, hb_z, r_bar - 1.5)
    post_top = hb_z - r_bar + 2
    for sy in (1, -1):
        pa = (p["hip_x"], sy * ry, post_top - p["post_len"])
        pc = (p["hip_x"], sy * ry, post_top)
        post = tube(p, "post", pa, pc)
        for k in range(9):   # height holes, 25 mm apart
            post -= xcyl(p["hip_x"] - 15, p["hip_x"] + 15, sy * ry, p["hip_pin_z"] + (hb_z - p["hip_min"]) - 25 * k, p["hip_pin_d"] / 2 + 0.25)
        hb += post
        gx0, gx1 = -p["grip_back"], p["hip_x"] - r_bar + 3
        gt = xcyl(gx0, gx1, sy * ry, hb_z, p["grip_d"] / 2) - xcyl(gx0 - 1, gx1 - 6, sy * ry, hb_z, p["grip_d"] / 2 - 1.6)
        hb += gt
    add("hipbar", "Hip bar weldment", hb, 4)
    pad = ycyl(p["hip_x"], -p["pad_len"] / 2, p["pad_len"] / 2, hb_z, p["pad_d"] / 2) - ycyl(p["hip_x"], -p["pad_len"] / 2 - 1, p["pad_len"] / 2 + 1, hb_z, r_bar)
    grips = fuse([xcyl(-p["grip_back"], -p["grip_back"] + p["grip_len"], sy * ry, hb_z, 16)
                  - xcyl(-p["grip_back"] - 1, -p["grip_back"] + p["grip_len"] + 1, sy * ry, hb_z, p["grip_d"] / 2) for sy in (1, -1)])
    add("pad_grips", "Hip pad and hand grips", pad + grips, 4, "bought")
    hpins = fuse([xcyl(p["hip_x"] - 22, p["hip_x"] + 22, sy * ry, p["hip_pin_z"], p["hip_pin_d"] / 2)
                  + xcyl(p["hip_x"] - 26, p["hip_x"] - p["sleeve"][0] / 2 - 1, sy * ry, p["hip_pin_z"], 6) for sy in (1, -1)])
    add("hip_pins", "Height pins (2)", hpins, 4, "bought")
    lx = -p["grip_back"] + p["grip_len"] + 4
    lever = xcyl(lx, lx + 16, -ry, hb_z, 16) - xcyl(lx - 1, lx + 17, -ry, hb_z, p["grip_d"] / 2)
    lever += oriented_box((lx + 8, -ry - 22, hb_z - 4), (lx - 105, -ry - 22, hb_z - 26), 10, 6, up=(0, 1, 0))
    lever += bx(lx + 2, lx + 14, -ry - 26, -ry - 14, hb_z - 12, hb_z + 4)
    add("lever", "Brake lever with parking latch", lever, 7, "bought")

    # ---- 5 cradle: plywood floor and walls, rubber pad, zinc angle brackets, four bolts to the bearers
    x0, x1, hw = p["cr_x0"], d["cr_x1"], p["cr_hw"]
    zf0, zf1 = p["cr_z"], p["cr_z"] + p["floor_t"]
    wt = p["wall_t"]
    fl = bx(x0, x1, -hw, hw, zf0, zf1)
    walls = [bx(x0, x1, hw - wt, hw, zf1, zf1 + p["wall_h"]), bx(x0, x1, -hw, -hw + wt, zf1, zf1 + p["wall_h"]),
             bx(x0, x0 + wt, -hw + wt, hw - wt, zf1, zf1 + p["wall_h"]), bx(x1 - wt, x1, -hw + wt, hw - wt, zf1, zf1 + p["wall_h"])]
    pad_ = bx(x0 + wt, x1 - wt, -hw + wt, hw - wt, zf1, zf1 + p["pad_t"])
    for x in p["cradle_bolt_x"]:
        for sy in (1, -1):
            fl -= zcyl(x, sy * p["bearer_y"], zf0 - 1, zf1 + 1, 3.3)
    add("cradle", "Cradle (floor and walls)", fuse([fl] + walls), 5)
    add("cradle_pad", "Cradle rubber pad", pad_, 5)
    br = []
    a, L, w_ = 1.5, 25.0, 20.0
    for x in (450.0, 740.0, 1030.0):          # bottom brackets on the side walls: leg up the wall, leg under the floor
        for sy in (1, -1):
            yo = sy * hw
            br.append(bx(x - w_ / 2, x + w_ / 2, min(yo, yo + sy * a), max(yo, yo + sy * a), zf0 - a, zf1 + 20))
            br.append(bx(x - w_ / 2, x + w_ / 2, min(yo + sy * a, yo - sy * L), max(yo + sy * a, yo - sy * L), zf0 - a, zf0))
    for xe, sx in ((x0, -1), (x1, 1)):          # bottom brackets on the end walls
        for y in (-75.0, 75.0):
            br.append(bx(min(xe, xe + sx * a), max(xe, xe + sx * a), y - w_ / 2, y + w_ / 2, zf0 - a, zf1 + 20))
            br.append(bx(min(xe + sx * a, xe - sx * L), max(xe + sx * a, xe - sx * L), y - w_ / 2, y + w_ / 2, zf0 - a, zf0))
    for xe, sx in ((x0, -1), (x1, 1)):          # corner brackets, outside
        for sy in (1, -1):
            zc0, zc1 = zf1 + 20, zf1 + 140
            br.append(bx(min(xe, xe + sx * a), max(xe, xe + sx * a), min(sy * hw, sy * (hw - L)), max(sy * hw, sy * (hw - L)), zc0, zc1))
            br.append(bx(min(xe + sx * a, xe - sx * (L - a)), max(xe + sx * a, xe - sx * (L - a)), min(sy * hw, sy * (hw + a)), max(sy * hw, sy * (hw + a)), zc0, zc1))
    add("cradle_brackets", "Cradle angle brackets (14)", fuse(br), 5, "bought")
    cb = []
    for x in p["cradle_bolt_x"]:
        for sy in (1, -1):
            cb.append(zcyl(x, sy * p["bearer_y"], d["bearer_z"] - p["cross"][0] / 2 - 7, zf1, 3.0)
                      + zcyl(x, sy * p["bearer_y"], d["bearer_z"] - p["cross"][0] / 2 - 7, d["bearer_z"] - p["cross"][0] / 2, 5.0))
    add("cradle_bolts", "Cradle bolts (4)", fuse(cb), 12, "fixing")

    # ---- 6 four 20 L jerrycans, 2 x 2 (user's own)
    jl, jw, jh = p["jc"]
    z0 = d["can_z0"]
    cans = []
    for cxx in (x0 + wt + 2 + jl / 2, x1 - wt - 2 - jl / 2):
        for cy in (jw / 2 + 5, -jw / 2 - 5):
            can = bx(cxx - jl / 2, cxx + jl / 2, cy - jw / 2, cy + jw / 2, z0, z0 + jh)
            can += zcyl(cxx + 110, cy, z0 + jh, z0 + jh + 40, 22)
            can += bx(cxx - 120, cxx + 40, cy - 15, cy + 15, z0 + jh, z0 + jh + 50)
            cans.append(can)
    add("cans", "20 L jerrycans (user's own)", fuse(cans), 6, "context", "load")

    # ---- optional assist kit (second prototype)
    motor = ycyl(0, -t2 - p["motor_w"] / 2, -t2 + p["motor_w"] / 2, R, p["motor_d"] / 2)
    add("motor", "Optional hub motor, 250 W, 48 V", motor, 9, "bought", "assist")
    pk = p["pack"]
    px0 = p["front_x"] + p["main"][1] / 2 + 25
    pz0 = p["arm_z"] + 20 + rx[2] + 8
    pack = bx(px0, px0 + pk[0], -pk[1] / 2, pk[1] / 2, pz0, pz0 + pk[2])
    pack += bx(px0 + pk[0] / 2 - 11, px0 + pk[0] / 2 + 11, pk[1] / 2, pk[1] / 2 + p["pack_handle"], pz0 + pk[2] / 2 - 30, pz0 + pk[2] / 2 + 30)
    add("pack", "Optional SwapCell pack", pack, 10, "bought", "assist")
    sensor = bx(sx0 + 5, sx0 + 45, -ry - 42, -ry - 2, p["sleeve_top"] - 40, p["sleeve_top"])
    add("sensor", "Optional push sensor and controller", sensor, 11, "bought", "assist")
    rcv = bx(px0 - 10, px0 + pk[0] + 10, -pk[1] / 2 - 10, pk[1] / 2 + 10, pz0 - 8, pz0)
    for s in (-1, 1):
        xg = px0 + pk[0] / 2 + s * (pk[0] / 2 + 7)
        rcv += bx(xg - 4, xg + 4, -pk[1] / 2, pk[1] / 2, pz0, pz0 + 50)
    rcv += bx(px0 - 10, px0 + pk[0] + 10, -(pk[1] / 2 + 24), -pk[1] / 2, pz0, pz0 + pk[2] + 10)
    add("receiver", "Optional SwapCell receiver, V1", rcv, 13, "made", "assist")
    return C


# BOM line -> (name, colour, explode offset) for the concept media and the general arrangement
BOM_VIEW = {
    1: ("Steel frame with cradle carrier and assist mounts", "#0F766E", (0, 0, 0)),
    2: ("Rear wheel in fixed fork, 26 in (x2)", "#374151", (-450, 0, 0)),
    3: ("Front wheel on swivel fork (x2)", "#374151", (500, 0, 0)),
    4: ("Hip bar and hand grips", "#B45309", (60, 0, 380)),
    5: ("Padded cradle", "#8B5E3C", (0, 0, -300)),
    6: ("20 L jerrycan (x4, user's own)", "#E3B505", (0, 0, 650)),
    7: ("Brake lever with parking latch", "#6B7280", (-300, -300, 350)),
    8: ("Skirt guard (x2)", "#D1D5DB", (-120, 0, 0)),
    9: ("Optional hub motor, 250 W, 48 V", "#111827", (-450, -620, 0)),
    10: ("Optional SwapCell pack", "#C2410C", (250, 0, 420)),
    11: ("Optional push sensor and controller", "#2563EB", (450, -650, -150)),
    12: ("Hardware", "#111827", (0, 0, 0)),
    13: ("Optional SwapCell receiver, V1", "#9A3412", (250, 0, 250)),
    15: ("Parking lock pin", "#DC2626", (-450, 520, 250)),
    16: ("Headsets and steering locks (4 sets)", "#1D4ED8", (0, 0, 200)),
}


def build_parts(p=PARAMS):
    """Return [(bom, name, shape, color, explode, group)] by BOM line for the concept media and the
    general arrangement. group is 'base' (first prototype), 'load' (the user's containers) or 'assist'."""
    C = build_components(p)
    lines = {}
    for c in C.values():
        if c.bom == 12:
            continue
        key = (c.bom, c.group)
        lines.setdefault(key, []).append(c.shape)
    out = []
    for (bom, group), shapes in sorted(lines.items(), key=lambda kv: kv[0][0]):
        name, color, ex = BOM_VIEW[bom]
        out.append((bom, name, fuse(shapes), color, ex, group))
    return out


def compound(parts, groups=("base", "load", "assist")):
    from build123d import Compound
    return Compound([s for _, _, s, _, _, g in parts if g in groups])


# ------------------------------------------------------------------ constructability checks
def _vol(a, b_):
    try:
        s = a & b_
        return s.volume if s is not None else 0.0
    except Exception:
        return float("nan")


def _gap(a, b_):
    return a.distance_to(b_)


def checks(p=PARAMS):
    """Pairs of components that must touch (contact, no overlap) or stay apart by a clearance (mm).
    Returns rows (description, overlap volume mm3, gap mm, expectation, ok)."""
    C = build_components(p)
    S = lambda k: C[k].shape  # noqa: E731
    d0 = derived(p)
    rows = []

    def chk(desc, a, b_, expect, vol_tol=1e-3):
        v = _vol(a, b_)
        gp = _gap(a, b_)
        ok = (v < vol_tol) and (gp < 0.05 if expect == "touch" else gp >= expect - 1e-6)
        rows.append((desc, v, gp, expect, ok))

    frame = S("frame")
    for s in ("l", "r"):
        side = "left" if s == "l" else "right"
        ff, rf = S(f"front_fork_{s}"), S(f"rear_fork_{s}")
        fw, rw = S(f"front_wheel_{s}"), S(f"rear_wheel_{s}")
        rh = S(f"rear_ht_{s}")
        chk(f"Rear head tube brackets ({side}) on the hip sleeve", rh, frame, "touch", vol_tol=50.0)
        chk(f"Rear wheel ({side}) in its fork dropouts", rw, rf, "touch")
        chk(f"Front wheel ({side}) in its fork dropouts", fw, ff, "touch")
        chk(f"Rear wheel ({side}) clear of the frame", rw, frame, 5.0)
        chk(f"Rear wheel ({side}) clear of the rear head tube brackets", rw, rh, 10.0)
        chk(f"Rear fork ({side}) clear of the frame", rf, frame, 5.0)
        chk(f"Rear fork crown ({side}) clear of the brackets", rf, rh, 0.0)
        chk(f"Front fork ({side}) clear of the frame below the head tube", ff, frame, 0.0)
        chk(f"Rear wheel ({side}) clear of the cradle carrier", rw, S("carrier"), 10.0)
        chk(f"Skirt guard ({side}) on its rail tabs", S(f"guard_{s}"), frame, "touch")
        chk(f"Skirt guard ({side}) clear of the wheel", S(f"guard_{s}"), rw, 3.0)
        chk(f"Skirt guard ({side}) clear of the fork", S(f"guard_{s}"), rf, 3.0)
        chk(f"Guard clips ({side}) on the inner blade", S(f"guard_clips_{s}"), rf, "touch")
        chk(f"Guard clips ({side}) on the guard", S(f"guard_clips_{s}"), S(f"guard_{s}"), "touch")
        chk(f"Guard bolts ({side}) clear of the wheel", S(f"guard_bolts_{s}"), rw, 10.0)
        chk(f"Brake arm ({side}) on the outer blade", S(f"brake_arm_{s}"), rf, "touch")
        chk(f"Brake arm ({side}) clear of the spokes and tire", S(f"brake_arm_{s}"), rw, 0.0)
    chk("Front headsets on the head tubes", S("cups_front"), frame, "touch")
    chk("Rear headsets on the head tubes", S("cups_rear"), S("rear_ht_l") + S("rear_ht_r"), "touch")
    chk("Front fork crowns on the lower headset cups", S("front_fork_l") + S("front_fork_r"), S("cups_front"), "touch")
    chk("Rear fork crowns on the lower headset cups", S("rear_fork_l") + S("rear_fork_r"), S("cups_rear"), "touch")
    chk("Front lock collars on the steerers", S("collars_front"), S("front_fork_l") + S("front_fork_r"), "touch")
    chk("Rear lock collars on the steerers", S("collars_rear"), S("rear_fork_l") + S("rear_fork_r"), "touch")
    chk("Front lock collars clear of the head tubes (2 mm above the cups)", S("collars_front"), S("cups_front"), 1.5)
    chk("Front lock plates clear of the pin guides", S("collars_front"), frame, 2.0)
    chk("Rear lock plates clear of the pin guides", S("collars_rear"), S("rear_ht_l") + S("rear_ht_r"), 2.0)
    chk("Swivel lock pins through the plates into the guides", S("pins_front"), frame, 0.2)
    chk("Swivel lock pins in the lock plate holes", S("pins_front"), S("collars_front"), 0.2)
    chk("Rear lock pins in their guides", S("pins_rear"), S("rear_ht_l") + S("rear_ht_r"), 0.2)
    chk("Carrier hangers under the cross members and on the frame", S("carrier"), frame, "touch")
    chk("Carrier clear of the rear wheels", S("carrier"), S("rear_wheel_l") + S("rear_wheel_r"), 10.0)
    chk("Cradle floor on the bearers", S("cradle"), S("carrier"), "touch")
    chk("Cradle clear of the frame", S("cradle"), frame, 4.0)
    chk("Cradle brackets on the cradle", S("cradle_brackets"), S("cradle"), "touch")
    chk("Cradle brackets clear of the carrier", S("cradle_brackets"), S("carrier"), 2.0)
    chk("Cradle bolts through the floor and bearers", S("cradle_bolts"), S("cradle") + S("carrier"), "touch", vol_tol=1.0)
    chk("Pad on the cradle floor", S("cradle_pad"), S("cradle"), "touch")
    chk("Jerrycans on the pad", S("cans"), S("cradle_pad"), "touch")
    chk("Jerrycans clear of the cradle walls", S("cans"), S("cradle"), 1.5)
    chk("Jerrycans clear of the frame", S("cans"), frame, 5.0)
    chk("Jerrycans clear of the rear cross member and carrier", S("cans"), S("carrier"), 5.0)
    chk("Hip posts inside the sleeves (sliding fit)", S("hipbar"), frame, 0.9)
    chk("Hip posts clear of the rear brackets (through the sleeve wall)", S("hipbar"), S("rear_ht_l") + S("rear_ht_r"), 2.0)
    chk("Height pins through the sleeve holes", S("hip_pins"), frame, 0.2)
    chk("Height pins through the post holes", S("hip_pins"), S("hipbar"), 0.2)
    chk("Pad and grips on the hip bar", S("pad_grips"), S("hipbar"), "touch")
    chk("Brake lever on the right grip tube", S("lever"), S("hipbar"), "touch")
    chk("Brake lever clear of the grip", S("lever"), S("pad_grips"), 1.0)
    chk("Lock pin through the inner and outer tabs", S("lock_pin"), S("pin_tabs"), 0.2)
    chk("Lock pin through the guard hole", S("lock_pin"), S("guard_l"), 1.5)
    chk("Lock pin clear of the spokes and rim", S("lock_pin"), S("rear_wheel_l"), 5.0)
    chk("Lock pin clear of the left rear fork", S("lock_pin"), S("rear_fork_l"), 5.0)
    yl = S("lock_pin").bounding_box().max.Y
    w_half = d0["t2"] + p["old"] / 2 + p["dropout_t"] + p["axle_proud"]
    rows.append(("Lock pin inside the axle nuts (width R6)", 0.0, w_half - yl, 0.0, yl <= w_half + 1e-6))
    chk("Lock pin tabs on the left rear fork blades", S("pin_tabs"), S("rear_fork_l"), "touch")
    chk("Lock pin tabs clear of the guard", S("pin_tabs"), S("guard_l"), 3.0)
    chk("Lock pin tabs clear of the left rear wheel", S("pin_tabs"), S("rear_wheel_l"), 10.0)
    chk("Torque-arm tab on the right rear fork blade", S("torque_tab"), S("rear_fork_r"), "touch")
    chk("Torque-arm tab clear of the right rear wheel and brake plate", S("torque_tab"), S("rear_wheel_r"), 5.0)
    chk("Torque-arm tab clear of the brake arm", S("torque_tab"), S("brake_arm_r"), 2.0)
    for s in ("l", "r"):
        side = "left" if s == "l" else "right"
        chk(f"Front fork and wheel ({side}) clear of the frame below the arm", S(f"front_wheel_{s}"), frame, 15.0)
    return rows


def caster_sweep_clearance(p=PARAMS):
    """Plan clearance from the swept front tire (any steer angle) to the frame members below the
    caster arms (risers, rails, lower cross member, hangers)."""
    d = derived(p)
    out = []
    for sy in (1, -1):
        px, py = d["pivot_x"], sy * d["t2"]
        # nearest point of the riser, rail end and lower cross member footprints to the pivot
        x_face = p["front_x"] + p["main"][0] / 2
        y_in, y_out = sorted((sy * (d["rail_y"] - p["main"][1] / 2), sy * (d["rail_y"] + p["main"][1] / 2)))
        ny = min(max(py, y_in), y_out)
        out.append(math.hypot(px - x_face, py - ny) - d["sweep_r"])
    return min(out)


def print_checks(p=PARAMS):
    rows = checks(p)
    bad = 0
    for desc, v, gp, exp, ok in rows:
        e = "touch" if exp == "touch" else f">= {exp:g} mm"
        print(f"  {'ok ' if ok else 'BAD'}  {desc:62s} overlap {v:9.3f} mm3  gap {gp:7.2f} mm  ({e})")
        bad += not ok
    sw = caster_sweep_clearance(p)
    print(f"  {'ok ' if sw >= p['swivel_clear'] else 'BAD'}  {'Caster sweep clear of the risers and rails (plan)':62s} clearance {sw:6.1f} mm  (>= {p['swivel_clear']:g} mm)")
    bad += sw < p["swivel_clear"]
    print(f"constructability checks: {len(rows) + 1 - bad} of {len(rows) + 1} pass")
    return bad


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(1 if print_checks() else 0)
    from build123d import Compound, export_step, export_stl
    root = Path(__file__).resolve().parents[1]
    (root / "step").mkdir(exist_ok=True)
    (root / "stl").mkdir(exist_ok=True)
    C = build_components()
    frame_keys = ("frame", "rear_ht_l", "rear_ht_r", "carrier")
    frame = Compound([C[k].shape for k in frame_keys])
    first = Compound([c.shape for c in C.values() if c.group in ("base", "load")])
    assist = Compound([c.shape for c in C.values() if c.group == "assist"])
    full = Compound([c.shape for c in C.values()])
    export_step(first, str(root / "step" / "waterwalker-first-prototype.step"))
    export_step(assist, str(root / "step" / "waterwalker-assist-kit.step"))
    export_step(full, str(root / "step" / "waterwalker-assembly.step"))
    export_step(frame, str(root / "step" / "waterwalker-frame.step"))
    export_stl(frame, str(root / "stl" / "waterwalker-frame.stl"), tolerance=0.5)
    export_stl(Compound([C["cradle"].shape, C["cradle_pad"].shape]), str(root / "stl" / "waterwalker-cradle.stl"), tolerance=0.5)
    export_stl(full, str(root / "stl" / "waterwalker-assembly.stl"), tolerance=1.0)
    bb = full.bounding_box()
    d = derived()
    print(f"assembly bounding box: {bb.size.X:.0f} x {bb.size.Y:.0f} x {bb.size.Z:.0f} mm")
    print(f"overall width (axle nuts) {d['overall_width']:.0f} mm; clear walking width {d['walk_width']:.0f} mm; "
          f"caster sweep clearance to risers {d['riser_gap']:.0f} mm; ground clearance under the bearers {d['clearance']:.0f} mm")
    print("wrote cad/step/waterwalker-{first-prototype,assist-kit,assembly,frame}.step and cad/stl/*.stl")
    print_checks()
