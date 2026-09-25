"""WaterWalker parametric model (build123d), TRL 3.

Run from the repo root:  python cad/src/model.py
Exports STEP into cad/step and STL into cad/stl.

Massing-plus detail: correct interfaces and main dimensions of the first
prototype (no assist, with assist mounting points) and of the optional assist
kit; not fabrication detail. Sections and positions are sized in WWK-CAL-001
(docs/04-calcs/01-sizing.md), which imports PARAMS and frame_members() from
this file so the calculation and the geometry share one source.

Axes: X is the direction of travel (front is +X), Y is across the carrier,
Z is up. The rear axle is at X = 0 and the ground is at Z = 0. Dimensions in mm.
"""
from pathlib import Path

# Top-level parameters (mm). Edit these, not the geometry below.
PARAMS = {
    # Wheels: 26 in (ETRTO 559) with 2.1 in (54 mm) tires; 2.4 in (61 mm) also fits
    "bead_d": 559.0, "tire_w": 54.0, "tire_w_max": 61.0,
    "old": 100.0,            # hub over-locknut width; front-type hub, all four wheels
    "dropout_t": 6.0, "axle_proud": 8.0,   # dropout plate and axle nut beyond it
    "track": 770.0,          # wheel plane to wheel plane
    "wheelbase": 1530.0,     # rear axle to front axle
    "trail": 60.0,           # front caster: swivel axis ahead of the front axle
    "swivel_clear": 15.0,    # clearance from the swept tire to the front risers
    # Frame sections: height x width x wall (mm)
    "main": (40.0, 30.0, 1.5),   # side rails, front risers, caster arms and stubs (RHS)
    "cross": (25.0, 25.0, 1.5),  # cross members and rear fork brackets
    "sleeve": (30.0, 30.0, 1.5), # hip bar upright sleeves
    "post": (25.0, 25.0, 1.5),   # telescopic hip bar posts inside the sleeves
    "hanger": (20.0, 20.0, 1.5), # cradle hangers
    "front_x": 1150.0,       # front risers
    "arm_z": 815.0,          # caster arms, above the tires
    "crown_z": 700.0,        # underside of fork crowns
    "head_len": 140.0, "head_d": 44.0,
    "rear_bracket_z": 790.0, # rear fork head tube bracket
    # Hip bar and grips
    "hip_x": 60.0, "hip_z": 950.0, "hip_min": 850.0, "hip_max": 1050.0,
    "sleeve_top": 820.0, "grip_back": 230.0, "hip_bar_d": 32.0, "pad_d": 90.0, "pad_len": 480.0,
    # Cradle
    "cr_x0": 350.0, "cr_hw": 215.0, "cr_z": 150.0,
    "floor_t": 9.0, "pad_t": 4.0, "wall_t": 6.0, "wall_h": 160.0,
    # Containers (user's own)
    "jc": (360.0, 175.0, 430.0),
    # Skirt guards
    "guard_l": 540.0, "guard_h": 420.0, "guard_t": 3.0, "guard_z": 420.0,
    # Assist mounting points (SwapCell interface v0.3) and optional assist kit
    "pack": (90.0, 340.0, 80.0),        # SwapCell body, x (depth), y (length), z (width)
    "pack_handle": 35.0, "pack_plug": 18.0,
    "rx_plate": (140.0, 300.0, 3.0),    # receiver mounting plate ahead of the upper cross member
    "motor_d": 180.0, "motor_w": 60.0,  # geared hub motor shell, right rear wheel
}
P = PARAMS


def derived(p=PARAMS):
    """Dimensions that follow from the parameters."""
    d = {}
    d["wheel_r"] = (p["bead_d"] + 2 * p["tire_w"]) / 2
    d["wheel_r_max"] = (p["bead_d"] + 2 * p["tire_w_max"]) / 2
    d["t2"] = p["track"] / 2
    d["rail_y"] = d["t2"] - p["old"] / 2 - p["main"][1] / 2        # rail outer face on the inner dropout
    d["rail_z"] = d["wheel_r"]
    d["pivot_x"] = p["wheelbase"] + p["trail"]
    d["cr_x1"] = p["front_x"] - p["main"][0] / 2
    d["walk_width"] = 2 * (d["rail_y"] - p["main"][1] / 2)
    d["overall_width"] = 2 * (d["t2"] + p["old"] / 2 + p["dropout_t"] + p["axle_proud"])
    d["sweep_r"] = p["trail"] + d["wheel_r_max"]                    # caster sweep radius in plan
    d["riser_gap"] = d["pivot_x"] - (p["front_x"] + p["main"][0] / 2) - d["sweep_r"]
    d["wall_top"] = p["cr_z"] + p["floor_t"] + p["wall_h"]
    d["rail_top"] = d["rail_z"] + p["main"][0] / 2
    d["can_z0"] = p["cr_z"] + p["floor_t"] + p["pad_t"]
    return d


def frame_members(p=PARAMS):
    """Axis-aligned tube members of the frame: (name, section, start, end).
    Used for the geometry and for the mass roll-up in WWK-CAL-001."""
    d = derived(p)
    ry, rz, t2, fx, az = d["rail_y"], d["rail_z"], d["t2"], p["front_x"], p["arm_z"]
    h40 = p["main"][0] / 2
    m = []
    for sy, side in ((1, "left"), (-1, "right")):
        m += [
            (f"side rail {side}", "main", (-15.0, sy * ry, rz), (fx + h40, sy * ry, rz)),
            (f"front riser {side}", "main", (fx, sy * ry, rz), (fx, sy * ry, az + h40)),
            (f"caster arm stub {side}", "main", (fx, sy * ry, az), (fx, sy * (t2 + 15), az)),
            (f"caster arm {side}", "main", (fx, sy * t2, az), (d["pivot_x"], sy * t2, az)),
            (f"hip upright sleeve {side}", "sleeve", (p["hip_x"], sy * ry, rz), (p["hip_x"], sy * ry, p["sleeve_top"])),
            (f"rear bracket x {side}", "cross", (0.0, sy * ry, p["rear_bracket_z"]), (p["hip_x"], sy * ry, p["rear_bracket_z"])),
            (f"rear bracket y {side}", "cross", (0.0, sy * ry, p["rear_bracket_z"]), (0.0, sy * t2, p["rear_bracket_z"])),
        ]
        for x in (p["cr_x0"], d["cr_x1"] - 10):
            m.append((f"cradle hanger {side} x{x:.0f}", "hanger",
                      (x, sy * (p["cr_hw"] - 20), p["cr_z"] + p["floor_t"]), (x, sy * (p["cr_hw"] - 20), rz)))
    m += [
        ("rear cross member", "cross", (p["cr_x0"], -ry, rz), (p["cr_x0"], ry, rz)),
        ("front lower cross member", "main", (fx, -ry, rz), (fx, ry, rz)),
        ("upper cross member", "main", (fx, -ry, az), (fx, ry, az)),
    ]
    return m


def member_length(a, b):
    return sum(abs(b[i] - a[i]) for i in range(3))


def build_parts(p=PARAMS):
    """Return [(bom, name, shape, color, explode, group)] for the concept media and exports.
    group is 'base' (first prototype) or 'assist' (optional kit, later)."""
    from build123d import Box, Cylinder, Torus, Pos, Rot
    d = derived(p)
    R, tw, t2 = d["wheel_r"], p["tire_w"], d["t2"]

    def tube(sec, a, b):
        h, w, _ = p[sec]
        L = member_length(a, b)
        c = tuple((a[i] + b[i]) / 2 for i in range(3))
        if a[0] != b[0]:
            size = (L, w, h)          # along X: height h vertical
        elif a[1] != b[1]:
            size = (w, L, h)          # along Y: height h vertical
        else:
            size = (h, w, L)          # uprights: bending depth h along X
        return Pos(*c) * Box(*size)

    def wheel(x, y, hub_r=35.0):
        tire = Pos(x, y, R) * Rot(90, 0, 0) * Torus(R - tw / 2, tw / 2)
        rim = Pos(x, y, R) * Rot(90, 0, 0) * Cylinder(R - tw + 4, 18) - Pos(x, y, R) * Rot(90, 0, 0) * Cylinder(R - tw - 10, 20)
        hub = Pos(x, y, R) * Rot(90, 0, 0) * Cylinder(hub_r, p["old"])
        axle = Pos(x, y, R) * Rot(90, 0, 0) * Cylinder(5, p["old"] + 2 * (p["dropout_t"] + p["axle_proud"]))
        spokes = None
        for a in range(0, 180, 30):
            s = Pos(x, y, R) * Rot(0, a, 0) * Box(2 * (R - tw), 4, 6)
            spokes = s if spokes is None else spokes + s
        return tire + rim + hub + axle + spokes

    def fork(x_axle, y, steer_x):
        """Rigid bicycle fork: blades either side of the wheel from the axle to the crown, crown, steerer."""
        blade_y = p["old"] / 2 + p["dropout_t"] / 2
        crown_z = p["crown_z"]
        bl = None
        for s in (1, -1):
            b = Pos((x_axle + steer_x) / 2, y + s * blade_y, (R + crown_z) / 2) * Box(abs(steer_x - x_axle) + 22, 12, crown_z - R + 20)
            bl = b if bl is None else bl + b
        crown = Pos(steer_x, y, crown_z + 12) * Box(40, p["old"] + 30, 24)
        steerer = Pos(steer_x, y, crown_z + 24 + p["head_len"] / 2 + 8) * Cylinder(14, p["head_len"] + 16)
        return bl + crown + steerer

    parts = []
    # 1 Frame: members, head tubes, dropout tabs and assist mounting points
    frame = None
    for _, sec, a, b in frame_members(p):
        t = tube(sec, a, b)
        frame = t if frame is None else frame + t
    head_z = p["crown_z"] + 24 + p["head_len"] / 2 + 6
    for sy in (1, -1):
        frame += Pos(d["pivot_x"], sy * t2, head_z) * Cylinder(p["head_d"] / 2, p["head_len"])      # front swivel head tube
        frame += Pos(0, sy * t2, head_z) * Cylinder(p["head_d"] / 2, p["head_len"])                  # rear fixed head tube
        frame += Pos(0, sy * (d["rail_y"] + p["main"][1] / 2 - 4), R) * Box(60, 8, 70)              # inner dropout tab on the rail
    rx = p["rx_plate"]
    frame += Pos(p["front_x"] + p["main"][1] / 2 - 5 + rx[0] / 2, 0, p["arm_z"] + p["main"][0] / 2 + rx[2] / 2) * Box(*rx)
    frame += Pos(-40, -(t2 + p["old"] / 2 + p["dropout_t"] / 2), R + 60) * Box(60, 6, 40)             # torque-arm tab, right rear
    frame += Pos(p["hip_x"] + 30, -d["rail_y"], p["sleeve_top"] - 40) * Box(30, 30, 60)             # sensor mounting boss
    parts.append((1, "Steel frame with assist mounts", frame, "#0F766E", (0, 0, 0), "base"))

    # 2 Rear wheels in fixed forks (front-type 100 mm drum hubs)
    for sy, nm, bom in ((-1, "Rear wheel and fixed fork, 26 in (x2)", 2), (1, "Rear wheel and fixed fork (left)", None)):
        w = wheel(0, sy * t2, 40) + fork(0, sy * t2, 0)
        parts.append((bom, nm, w, "#374151", (-450 if sy < 0 else -250, sy * 260, 0), "base"))
    # 3 Front wheels on full-swivel caster forks with drop-pin lock
    for sy, nm, bom in ((-1, "Front wheel on swivel fork (x2)", 3), (1, "Front wheel on swivel fork (left)", None)):
        w = wheel(p["wheelbase"], sy * t2) + fork(p["wheelbase"], sy * t2, d["pivot_x"])
        w += Pos(d["pivot_x"] - 30, sy * t2, head_z + p["head_len"] / 2 - 10) * Cylinder(4, 50)
        parts.append((bom, nm, w, "#374151", (500, sy * 260, 0), "base"))

    # 4 Hip bar on telescopic posts, pad and rear-facing grips
    ry = d["rail_y"]
    hb = Pos(p["hip_x"], 0, p["hip_z"]) * Rot(90, 0, 0) * Cylinder(p["hip_bar_d"] / 2, 2 * ry + 40)
    hb += Pos(p["hip_x"], 0, p["hip_z"]) * Rot(90, 0, 0) * Cylinder(p["pad_d"] / 2, p["pad_len"])
    for sy in (1, -1):
        hb += Pos(p["hip_x"], sy * ry, (p["sleeve_top"] - 150 + p["hip_z"]) / 2) * Box(25, 25, p["hip_z"] - p["sleeve_top"] + 150)
        hb += Pos((p["hip_x"] - p["grip_back"]) / 2, sy * ry, p["hip_z"]) * Rot(0, 90, 0) * Cylinder(16, p["hip_x"] + p["grip_back"])
    parts.append((4, "Hip bar and hand grips", hb, "#B45309", (60, 0, 380), "base"))

    # 5 Cradle: plywood floor, rubber pad, low walls
    x0, x1, hw = p["cr_x0"], d["cr_x1"], p["cr_hw"]
    L, cx = x1 - x0, (x0 + x1) / 2
    cr = Pos(cx, 0, p["cr_z"] + p["floor_t"] / 2) * Box(L, 2 * hw, p["floor_t"])
    cr += Pos(cx, 0, p["cr_z"] + p["floor_t"] + p["pad_t"] / 2) * Box(L - 2 * p["wall_t"], 2 * hw - 2 * p["wall_t"], p["pad_t"])
    wz = p["cr_z"] + p["floor_t"] + p["wall_h"] / 2
    for sy in (1, -1):
        cr += Pos(cx, sy * (hw - p["wall_t"] / 2), wz) * Box(L, p["wall_t"], p["wall_h"])
    for x in (x0 + p["wall_t"] / 2, x1 - p["wall_t"] / 2):
        cr += Pos(x, 0, wz) * Box(p["wall_t"], 2 * hw, p["wall_h"])
    parts.append((5, "Padded cradle", cr, "#8B5E3C", (0, 0, -300), "base"))

    # 6 Four 20 L jerrycans, 2 x 2 (user's own)
    jl, jw, jh = p["jc"]
    z0 = d["can_z0"]
    first = True
    for cxx in (x0 + p["wall_t"] + 2 + jl / 2, x1 - p["wall_t"] - 2 - jl / 2):
        for cy in (jw / 2 + 5, -jw / 2 - 5):
            can = Pos(cxx, cy, z0 + jh / 2) * Box(jl, jw, jh)
            can += Pos(cxx + 110, cy, z0 + jh + 20) * Cylinder(22, 40)
            can += Pos(cxx - 40, cy, z0 + jh + 25) * Box(160, 30, 50)
            parts.append((6 if first else None, "20 L jerrycan (x4, user's own)" if first else "20 L jerrycan",
                          can, "#E3B505", (0, 0, 650), "load"))
            first = False

    # 7 Drum brakes on the outboard side of both rear hubs, reaction arms to the outer fork blades
    for sy, nm, bom in ((-1, "Rear drum brake and parking latch", 7), (1, "Rear drum brake (left)", None)):
        y = sy * (t2 + p["old"] / 2 - 16)
        dr = Pos(0, y, R) * Rot(90, 0, 0) * Cylinder(50, 22) + Pos(60, y, R - 10) * Box(120, 8, 16)
        parts.append((bom, nm, dr, "#6B7280", (-450, sy * 420, 380), "base"))

    # 8 Skirt guards between the inner fork blade and the spokes, with a hub cut-out
    for sy, nm, bom in ((-1, "Skirt guard (x2)", 8), (1, "Skirt guard (left)", None)):
        y = sy * (t2 - p["old"] / 2 + 5 + p["guard_t"] / 2)
        g = Pos(0, y, p["guard_z"]) * Box(p["guard_l"], p["guard_t"], p["guard_h"])
        g -= Pos(0, y, R) * Rot(90, 0, 0) * Cylinder(60, 10)
        parts.append((bom, nm, g, "#D1D5DB", (-120, sy * 60, 0), "base"))

    # 9 to 11 and 13 Optional assist kit (second prototype)
    motor = Pos(0, -t2, R) * Rot(90, 0, 0) * Cylinder(p["motor_d"] / 2, p["motor_w"])
    parts.append((9, "Optional hub motor, 250 W, 48 V", motor, "#111827", (-450, -620, 0), "assist"))
    pk, px0 = p["pack"], p["front_x"] + p["main"][1] / 2 + 25
    pz0 = p["arm_z"] + p["main"][0] / 2 + rx[2] + 8
    pack = Pos(px0 + pk[0] / 2, 0, pz0 + pk[2] / 2) * Box(*pk)
    pack += Pos(px0 + pk[0] / 2, pk[1] / 2 + p["pack_handle"] / 2, pz0 + pk[2] / 2) * Box(22, p["pack_handle"], 60)
    parts.append((10, "Optional SwapCell pack", pack, "#C2410C", (250, 0, 420), "assist"))
    sensor = Pos(p["hip_x"] + 30, -ry, p["sleeve_top"] + 20) * Box(40, 40, 40)
    parts.append((11, "Optional push sensor and controller", sensor, "#2563EB", (450, -650, -150), "assist"))
    rcv = Pos(px0 + pk[0] / 2, 0, pz0 - 4) * Box(pk[0] + 20, pk[1] + 20, 8)
    for s in (1, -1):
        rcv += Pos(px0 + pk[0] / 2 + s * (pk[0] / 2 + 7), 0, pz0 + 25) * Box(8, pk[1], 50)
    rcv += Pos(px0 + pk[0] / 2, -(pk[1] / 2 + 12), pz0 + pk[2] / 2) * Box(pk[0] + 20, 24, pk[2] + 10)
    parts.append((13, "Optional SwapCell receiver, V1", rcv, "#9A3412", (250, 0, 250), "assist"))
    return parts


def compound(parts, groups=("base", "load", "assist")):
    from build123d import Compound
    return Compound([s for _, _, s, _, _, g in parts if g in groups])


if __name__ == "__main__":
    from build123d import Compound, export_step, export_stl
    root = Path(__file__).resolve().parents[1]
    (root / "step").mkdir(exist_ok=True)
    (root / "stl").mkdir(exist_ok=True)
    parts = build_parts()
    frame = parts[0][2]
    cradle = [s for b, _, s, *_ in parts if b == 5][0]
    first = compound(parts, ("base", "load"))
    assist = compound(parts, ("assist",))
    full = compound(parts)
    export_step(first, str(root / "step" / "waterwalker-first-prototype.step"))
    export_step(assist, str(root / "step" / "waterwalker-assist-kit.step"))
    export_step(full, str(root / "step" / "waterwalker-assembly.step"))
    export_step(Compound([frame]), str(root / "step" / "waterwalker-frame.step"))
    export_stl(frame, str(root / "stl" / "waterwalker-frame.stl"))
    export_stl(cradle, str(root / "stl" / "waterwalker-cradle.stl"))
    export_stl(full, str(root / "stl" / "waterwalker-assembly.stl"))
    bb = full.bounding_box()
    d = derived()
    print(f"assembly bounding box: {bb.size.X:.0f} x {bb.size.Y:.0f} x {bb.size.Z:.0f} mm")
    print(f"overall width (axle nuts) {d['overall_width']:.0f} mm; clear walking width {d['walk_width']:.0f} mm; "
          f"caster sweep clearance to risers {d['riser_gap']:.0f} mm")
    print("wrote cad/step/waterwalker-{first-prototype,assist-kit,assembly,frame}.step and cad/stl/*.stl")
