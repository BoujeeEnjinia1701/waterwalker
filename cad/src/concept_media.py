"""WaterWalker concept massing model and media (TRL 2).

Run from the repo root:  python cad/src/concept_media.py
Proportions and main parts only; not for fabrication.

Axes: X is the direction of travel (front is +X), Y is across the carrier, Z is up.
The user walks inside the open rear of the frame, between the rear wheels, and pushes
the hip bar. The cradle sits low between the axles, ahead of the user's feet.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / ".kit"))
from build123d import Box, Cylinder, Torus, Pos, Rot
from concept import Part, render_all

# Main dimensions (mm). Proposed values, awaiting Amish (see docs/02-concept.md).
WHEEL_R = 330.0          # 26 in wheel with 2.1 in tire, outside diameter about 660 mm
TIRE_R = 27.0            # tire section radius
TRACK = 800.0            # wheel centre to wheel centre across the carrier
WHEELBASE = 1520.0       # rear axle at X = 0, front axle at X = WHEELBASE
TRAIL = 60.0             # caster trail; swivel axis 60 mm ahead of the front axle
FRONT_X = 1200.0         # front risers, clear of the full caster sweep (radius about 390 mm)
ARM_Z = 815.0            # caster arms pass above the tires so the forks can swivel fully
RAIL_Y = 345.0           # side rail centre line; clear walking width about 660 mm
RAIL_Z = WHEEL_R         # side rails at axle height
TUBE = 30.0              # square steel tube section
HIP_X, HIP_Z = 50.0, 950.0   # hip bar position (height adjustable 850 to 1,050 mm)
CR_X0, CR_X1 = 390.0, 1170.0  # cradle, front of the user's feet to just behind the front axle
CR_HW = 215.0            # cradle half width
CR_Z = 150.0             # underside of cradle floor (ground clearance)
JC = (360.0, 175.0, 430.0)    # 20 L jerrycan, length x width x height


def along_x(x0, x1, y, z, s=TUBE):
    return Pos((x0 + x1) / 2, y, z) * Box(x1 - x0, s, s)


def along_y(y0, y1, x, z, s=TUBE):
    return Pos(x, (y0 + y1) / 2, z) * Box(s, y1 - y0, s)


def along_z(z0, z1, x, y, s=TUBE):
    return Pos(x, y, (z0 + z1) / 2) * Box(s, s, z1 - z0)


def wheel(x, y):
    """Tire, spokes and hub, axis along Y."""
    tire = Pos(x, y, WHEEL_R) * Rot(90, 0, 0) * Torus(WHEEL_R - TIRE_R, TIRE_R)
    hub = Pos(x, y, WHEEL_R) * Rot(90, 0, 0) * Cylinder(30, 90)
    spokes = None
    for a in range(0, 180, 30):
        s = Pos(x, y, WHEEL_R) * Rot(0, a, 0) * Box(2 * (WHEEL_R - TIRE_R), 6, 8)
        spokes = s if spokes is None else spokes + s
    return tire + hub + spokes


def front_wheel(x, y, trail=TRAIL):
    """Wheel on a full-swivel, lockable caster fork: head tube above the tire, fork legs either side."""
    head = Pos(x + trail, y, 760) * Cylinder(22, 140)
    crown = Pos(x + trail / 2, y, 690) * Box(70, 110, 25)
    legs = (Pos(x + trail / 2, y + 45, 510) * Box(18, 12, 360)
            + Pos(x + trail / 2, y - 45, 510) * Box(18, 12, 360))
    return wheel(x, y) + head + crown + legs


# 1 Frame: two side rails at axle height, open at the rear so the user steps in without a step-over,
# cradle cross members, front risers and upper cross member, caster arms, hip bar uprights, stub axles,
# and a small shelf for the optional battery pack.
frame = (along_x(-60, FRONT_X + 15, RAIL_Y, RAIL_Z) + along_x(-60, FRONT_X + 15, -RAIL_Y, RAIL_Z)
         + along_y(-RAIL_Y, RAIL_Y, CR_X0, RAIL_Z) + along_y(-RAIL_Y, RAIL_Y, CR_X1, RAIL_Z)
         + along_y(-RAIL_Y, RAIL_Y, FRONT_X, ARM_Z)
         + along_z(RAIL_Z, HIP_Z - 25, HIP_X, RAIL_Y) + along_z(RAIL_Z, HIP_Z - 25, HIP_X, -RAIL_Y)
         + Pos(FRONT_X + 75, 0, RAIL_Z + 5) * Box(120, 300, 10)
         + along_z(RAIL_Z + 10, ARM_Z, FRONT_X + 20, 120, 15) + along_z(RAIL_Z + 10, ARM_Z, FRONT_X + 20, -120, 15))
for sy in (1, -1):
    frame = frame + Pos(0, sy * (RAIL_Y + 40), RAIL_Z) * Rot(90, 0, 0) * Cylinder(10, 80)   # rear stub axle
    frame = frame + along_z(RAIL_Z, ARM_Z + 15, FRONT_X, sy * RAIL_Y)                       # front riser
    y0, y1 = sorted((sy * RAIL_Y, sy * (TRACK / 2 + 15)))
    frame = frame + along_y(y0, y1, FRONT_X, ARM_Z)                                        # arm stub
    frame = frame + along_x(FRONT_X, WHEELBASE + TRAIL, sy * TRACK / 2, ARM_Z)             # caster arm
    for x in (CR_X0 + 20, CR_X1 - 20):                                                      # cradle hangers
        frame = frame + along_z(CR_Z + 20, RAIL_Z, x, sy * (CR_HW - 20), 20)

# 2 and 3 Wheels
rear_l, rear_r = wheel(0, TRACK / 2), wheel(0, -TRACK / 2)
front_l, front_r = front_wheel(WHEELBASE, TRACK / 2), front_wheel(WHEELBASE, -TRACK / 2)

# 4 Hip bar with pad and rear-facing hand grips (rollator style)
hip_bar = (Pos(HIP_X, 0, HIP_Z) * Rot(90, 0, 0) * Cylinder(22, 2 * RAIL_Y + 40)
           + Pos(HIP_X, 0, HIP_Z) * Rot(90, 0, 0) * Cylinder(45, 480)
           + along_x(-230, HIP_X, RAIL_Y, HIP_Z, 34) + along_x(-230, HIP_X, -RAIL_Y, HIP_Z, 34))

# 5 Low padded cradle: floor, pad and low side walls; adjustable straps and dividers not modeled
cr_len = CR_X1 - CR_X0
cradle = Pos((CR_X0 + CR_X1) / 2, 0, CR_Z + 10) * Box(cr_len, 2 * CR_HW, 20)
cradle = cradle + Pos((CR_X0 + CR_X1) / 2, 0, CR_Z + 30) * Box(cr_len - 30, 2 * CR_HW - 30, 20)
wall_h = 160.0
for sy in (1, -1):
    cradle = cradle + Pos((CR_X0 + CR_X1) / 2, sy * (CR_HW - 8), CR_Z + 20 + wall_h / 2) * Box(cr_len, 16, wall_h)
for x in (CR_X0 + 8, CR_X1 - 8):
    cradle = cradle + Pos(x, 0, CR_Z + 20 + wall_h / 2) * Box(16, 2 * CR_HW, wall_h)

# 6 Four 20 L jerrycans standing 2 x 2 (user's own containers, shown for scale)
jz0 = CR_Z + 40
cans = []
for cx in (CR_X0 + 20 + JC[0] / 2, CR_X1 - 20 - JC[0] / 2):
    for cy in (JC[1] / 2 + 5, -JC[1] / 2 - 5):
        body = Pos(cx, cy, jz0 + JC[2] / 2) * Box(*JC)
        cap = Pos(cx + 110, cy, jz0 + JC[2] + 20) * Cylinder(22, 40)
        handle = Pos(cx - 40, cy, jz0 + JC[2] + 25) * Box(160, 30, 50)
        cans.append(body + cap + handle)

# 7 Brake: drum brakes on both rear hubs, lever with parking latch on a grip (lever not modeled)
drum_l = Pos(0, TRACK / 2 - 16, WHEEL_R) * Rot(90, 0, 0) * Cylinder(62, 20)
drum_r = Pos(0, -TRACK / 2 + 16, WHEEL_R) * Rot(90, 0, 0) * Cylinder(62, 20)

# 8 Skirt guards on the inner side of the rear wheels
guard_l = Pos(0, RAIL_Y + 22, 420) * Box(540, 4, 420)
guard_r = Pos(0, -RAIL_Y - 22, 420) * Box(540, 4, 420)

# 9 to 11 Optional assist: hub motor in the right rear wheel, SwapCell pack, push-force sensor and controller
motor = Pos(0, -TRACK / 2, WHEEL_R) * Rot(90, 0, 0) * Cylinder(90, 60)
pack = Pos(FRONT_X + 75, 0, RAIL_Z + 10 + 45) * Box(110, 280, 90)
sensor = Pos(HIP_X + 45, -RAIL_Y, HIP_Z - 90) * Box(50, 70, 90)

WHEEL, CAN = "#374151", "#E3B505"
parts = [
    Part("Steel tube frame", frame, "#0F766E", 1),
    Part("Rear wheel, 26 in (x2)", rear_r, WHEEL, 2, (-420, -250, 0)),
    Part("Rear wheel (left)", rear_l, WHEEL, None, (-420, 250, 0)),
    Part("Front wheel on swivel fork (x2)", front_r, WHEEL, 3, (500, -250, 0)),
    Part("Front wheel (left)", front_l, WHEEL, None, (500, 250, 0)),
    Part("Hip bar and hand grips", hip_bar, "#B45309", 4, (-150, 0, 380)),
    Part("Padded adjustable cradle", cradle, "#8B5E3C", 5, (0, 0, -300)),
    Part("20 L jerrycan (x4, user's own)", cans[0], CAN, 6, (0, 0, 650)),
    *[Part("20 L jerrycan", c, CAN, None, (0, 0, 650)) for c in cans[1:]],
    Part("Rear drum brake and parking latch", drum_r, "#6B7280", 7, (-420, -250, 430)),
    Part("Rear drum brake (left)", drum_l, "#6B7280", None, (-420, 250, 430)),
    Part("Skirt guard (x2)", guard_r, "#D1D5DB", 8, (-120, -40, 0)),
    Part("Skirt guard (left)", guard_l, "#D1D5DB", None, (-120, 40, 0)),
    Part("Optional hub motor, 250 W", motor, "#111827", 9, (-420, -520, 0)),
    Part("Optional SwapCell pack, 36 V", pack, "#C2410C", 10, (250, 0, 450)),
    Part("Optional push sensor and controller", sensor, "#2563EB", 11, (0, -380, 380)),
]

render_all(
    parts, project="WaterWalker", title="Walk-inside water carrier concept", dwg_no="WWK-DWG-010",
    key_figures=["80 L water per trip (4 x 20 L), about 4 times a head load",
                 "26 in wheels, 860 mm wide, 2.2 m long, 3.8 m turning circle",
                 "Push on firm ground about 25 to 55 N (estimate)",
                 "Push on loose sand about 225 to 340 N unassisted (estimate)",
                 "About $300 in parts without assist (indicative)"],
    cut=False,
    flow={"title": "water delivered per trip and per day (estimates)", "unit": "",
          "stages": [("Water point", "fill 4 x 20 L"),
                     ("Load cradle", "lift 20 kg to 0.35 m"),
                     ("Walk home", "80 L per trip vs 20 L"),
                     ("Household", "about 100 L per day"),
                     ("Trips per day", "2 vs 5 by head")]},
)
