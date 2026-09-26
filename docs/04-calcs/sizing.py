"""WaterWalker sizing calculations, WWK-CAL-001 v0.2 (TRL 3).

Run from the repo root:  python docs/04-calcs/sizing.py
Prints every number quoted in docs/04-calcs/01-sizing.md and writes
docs/04-calcs/results.csv. Geometry comes from cad/src/model.py (PARAMS,
derived() and frame_members()), and prices from bom/bom.csv, so the note,
the model and the BOM share one source. All values are first-principles
estimates for a paper design; nothing here is measured.
"""
import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "cad" / "src"))
from model import PARAMS as P, derived, frame_members, member_length  # noqa: E402

D = derived()
g = 9.81
RHO_STEEL = 7850.0          # kg/m3
E_STEEL, G_STEEL = 205e3, 79e3   # MPa
FY = 235.0                  # MPa, mild steel yield (S235 class; ERW tube is often higher)
DYN = 2.5                   # dynamic load factor for rough paths, ruts and kerbs
OUT = []                    # (key, value, unit) rows for results.csv


def out(key, value, unit="", fmt="{:.2f}"):
    OUT.append((key, fmt.format(value) if isinstance(value, float) else value, unit))
    return value


def section(title):
    print(f"\n== {title}")


# ---------------------------------------------------------------- 1. Geometry
section("1. Geometry from cad/src/model.py")
R = D["wheel_r"] / 1000
print(f"wheel radius {D['wheel_r']:.1f} mm (2.1 in tire), {D['wheel_r_max']:.1f} mm (2.4 in)")
print(f"track {P['track']:.0f} mm, wheelbase {P['wheelbase']:.0f} mm, caster trail {P['trail']:.0f} mm, pivot x {D['pivot_x']:.0f} mm")
print(f"overall width over axle nuts {D['overall_width']:.0f} mm; clear walking width {D['walk_width']:.0f} mm")
print(f"caster sweep radius {D['sweep_r']:.1f} mm; clearance to front risers {D['riser_gap']:.1f} mm")
out("overall_width", D["overall_width"], "mm", "{:.0f}")
out("walk_width", D["walk_width"], "mm", "{:.0f}")
out("riser_gap", D["riser_gap"], "mm", "{:.1f}")
overall_len = P["wheelbase"] + 2 * D["wheel_r"]
print(f"overall length, rear tire to front tire (casters trailing): {overall_len:.0f} mm "
      f"({P['wheelbase'] + 2 * D['wheel_r_max']:.0f} mm with 2.4 in tires)")
out("overall_length", overall_len, "mm", "{:.0f}")
cradle_len = D["cr_x1"] - P["cr_x0"]
can_row = 2 * P["jc"][0] + 2 * P["wall_t"] + 4
print(f"cradle inside length {cradle_len - 2 * P['wall_t']:.0f} mm for two jerrycans in line ({2 * P['jc'][0]:.0f} mm): spare {cradle_len - can_row:.0f} mm")
pot_d = 380.0
pot_spare = cradle_len - 2 * P["wall_t"] - 2 * pot_d
print(f"clay pots, {pot_d:.0f} mm diameter: {int((cradle_len - 2 * P['wall_t']) // pot_d)} in line, "
      f"{int((2 * P['cr_hw'] - 2 * P['wall_t']) // pot_d)} across; spare length for two in line {pot_spare:.0f} mm")
out("jerrycan_spare", cradle_len - can_row, "mm", "{:.0f}")
out("pot_spare", pot_spare, "mm", "{:.0f}")
lift = D["rail_top"] + 10
print(f"container lift height over the side rail: {lift:.0f} mm (cradle wall top {D['wall_top']:.0f} mm)")
out("lift_height", lift, "mm", "{:.0f}")

# ---------------------------------------------------------------- 2. Mass
section("2. Mass roll-up")


def rhs_area(h, w, t):
    return 2 * t * (h + w) - 4 * t * t        # mm2


tube_len, tube_mass = {}, {}
for _, sec, a, b in frame_members():
    L = member_length(a, b) / 1000
    tube_len[sec] = tube_len.get(sec, 0) + L
for sec, L in tube_len.items():
    kgm = rhs_area(*P[sec]) * 1e-6 * RHO_STEEL
    tube_mass[sec] = L * kgm
    print(f"  {sec:7s} {P[sec][0]:.0f} x {P[sec][1]:.0f} x {P[sec][2]:.1f} mm: {L:.2f} m at {kgm:.3f} kg/m = {tube_mass[sec]:.2f} kg")
tubes = sum(tube_mass.values())
rx = P["rx_plate"]
frame_extras = {
    "head tubes (4), 0.25 kg each": 1.00,
    "dropout tabs (2)": 0.12,
    "receiver plate 140 x 300 x 3 mm": rx[0] * rx[1] * rx[2] * 1e-9 * RHO_STEEL,
    "torque-arm tab and sensor boss": 0.15,
    "welds and paint, 4 % of tube": 0.04 * tubes,
}
frame = tubes + sum(frame_extras.values())
print(f"tube length {sum(tube_len.values()):.2f} m, tube mass {tubes:.2f} kg; frame with extras {frame:.2f} kg")
out("frame_tube_length", sum(tube_len.values()), "m")
wheel = {"rim": 0.55, "spokes": 0.30, "tire": 0.85, "tube": 0.45, "liner": 0.20}
rear_wheel = sum(wheel.values()) + 0.75      # 70 mm drum hub
front_wheel = sum(wheel.values()) + 0.35     # plain hub
fork = 1.10
cradle = {"floor": (cradle_len * 2 * P["cr_hw"] * P["floor_t"]) * 1e-9 * 600,
          "pad": ((cradle_len - 2 * P["wall_t"]) * (2 * P["cr_hw"] - 2 * P["wall_t"]) * P["pad_t"]) * 1e-9 * 1150,
          "walls": (2 * (cradle_len + 2 * P["cr_hw"]) * P["wall_h"] * P["wall_t"]) * 1e-9 * 600,
          "straps and dividers": 0.40}
masses = {
    "frame": frame,
    "rear wheels with drum hubs (2)": 2 * rear_wheel,
    "front wheels (2)": 2 * front_wheel,
    "forks (4)": 4 * fork,
    "headsets, clamps and swivel locks": 2 * 0.15 + 2 * 0.10 + 2 * 0.05,
    "hip bar, posts, pad and grips": 2.20,
    "cradle": sum(cradle.values()),
    "brake lever, latch and cables": 0.45,
    "skirt guards (2)": 2 * P["guard_l"] * P["guard_h"] * P["guard_t"] * 1e-9 * 950,
    "hardware and reflectors": 0.60,
    "parking lock pin, tab and lanyard": 0.10,
}
for k, v in masses.items():
    print(f"  {k:36s} {v:6.2f} kg")
m_empty = out("mass_empty", sum(masses.values()), "kg")
assist = {"motor delta (2.60 kg motor less 0.75 kg drum hub)": 2.60 - 0.75, "disc brake for motor wheel": 0.35,
          "controller and wiring": 0.65, "push sensor and controller": 0.20, "SwapCell receiver, class V1": 0.60,
          "SwapCell pack": 2.85}
m_assist_kit = sum(assist.values())
m_empty_a = out("mass_empty_assist", m_empty + m_assist_kit, "kg")
print(f"empty mass {m_empty:.2f} kg ({m_empty * 2.2046:.1f} lb); with assist kit {m_empty_a:.2f} kg (kit {m_assist_kit:.2f} kg)")
print(f"cradle {sum(cradle.values()):.2f} kg (floor {cradle['floor']:.2f}, pad {cradle['pad']:.2f}, walls {cradle['walls']:.2f})")
water, can = 80.0, 1.1
payload = water + 4 * can
m_load = out("mass_loaded", m_empty + payload, "kg")
m_load_a = out("mass_loaded_assist", m_empty_a + payload, "kg")
print(f"payload {payload:.1f} kg; loaded {m_load:.1f} kg; loaded with assist {m_load_a:.1f} kg")
pots_payload = 2 * 20 + 2 * 8.0
print(f"two clay pots, 8 kg each empty, full: payload {pots_payload:.0f} kg")

# Mass changes applied by WWK-DDR-002 (against the v0.1 model: 1.5 mm main wall; cradle floor 9 mm,
# walls 6 mm, pad 4 mm) and the options left open (puncture protection kept by the same decision)
h_, w_, t_ = P["main"]
applied = {
    "main RHS wall 1.5 to 1.2 mm": tube_len["main"] * (rhs_area(h_, w_, 1.5) - rhs_area(h_, w_, t_)) * 1e-6 * RHO_STEEL * 1.04,
    "cradle floor 9 to 6 mm, walls 6 to 4 mm, pad 4 to 2 mm":
        (cradle_len * 2 * P["cr_hw"] * 9.0) * 1e-9 * 600 + ((cradle_len - 12) * (2 * P["cr_hw"] - 12) * 4.0) * 1e-9 * 1150
        + (2 * (cradle_len + 2 * P["cr_hw"]) * P["wall_h"] * 6.0) * 1e-9 * 600 + 0.40 - sum(cradle.values()),
    "parking lock pin added": -0.10,
}
for k, v in applied.items():
    print(f"  applied: {k:52s} {-v:+.2f} kg")
m_empty_v01 = m_empty + sum(applied.values())
print(f"  empty mass before DDR-002 changes (v0.1) {m_empty_v01:.2f} kg; now {m_empty:.2f} kg")
out("mass_empty_v01", m_empty_v01, "kg")
opt = {
    "tires without puncture belt (0.65 kg)": 4 * (0.85 - 0.65),
    "no tire liners (keep thorn-resistant tubes)": 4 * 0.20,
}
opt_total = sum(opt.values())
for k, v in opt.items():
    print(f"  open option (not applied): {k:44s} -{v:.2f} kg")
print(f"  with both open options: -{opt_total:.2f} kg, empty {m_empty - opt_total:.2f} kg")
out("mass_options_total", opt_total, "kg")
out("mass_empty_with_options", m_empty - opt_total, "kg")

# Centre of mass (x, z) of the loaded carrier from component positions
fill_h = 20000 / (P["jc"][0] / 10 * P["jc"][1] / 10) * 10     # mm of water in a 360 x 175 mm footprint
x_c = (P["cr_x0"] + D["cr_x1"]) / 2
items = [  # (mass, x, z)
    (water, x_c, D["can_z0"] + fill_h / 2), (4 * can, x_c, D["can_z0"] + P["jc"][2] / 2),
    (sum(cradle.values()), x_c, P["cr_z"] + 40), (frame, 700.0, 520.0),
    (2 * rear_wheel + 2 * fork + 0.2, 0.0, D["wheel_r"] + 60), (2 * front_wheel + 2 * fork + 0.4, P["wheelbase"], D["wheel_r"] + 60),
    (2.20, P["hip_x"] - 40, P["hip_z"]), (0.45 + 1.3 + 0.6, 400.0, 400.0)]
M = sum(i[0] for i in items)
x_cg = sum(i[0] * i[1] for i in items) / M / 1000
z_cg = sum(i[0] * i[2] for i in items) / M / 1000
Lb = P["wheelbase"] / 1000
front_share = x_cg / Lb
print(f"loaded centre of mass x = {x_cg * 1000:.0f} mm, z = {z_cg * 1000:.0f} mm; front axle share {front_share * 100:.1f} %")
out("x_cg", x_cg * 1000, "mm", "{:.0f}")
out("z_cg", z_cg * 1000, "mm", "{:.0f}")
Wl = m_load * g
Nf_wheel, Nr_wheel = Wl * front_share / 2, Wl * (1 - front_share) / 2
print(f"static wheel loads: front {Nf_wheel:.0f} N, rear {Nr_wheel:.0f} N each")

# ---------------------------------------------------------------- 3. Rolling resistance and push force
section("3. Rolling resistance and push force")
crr_firm = (0.02, 0.05)


def crr_sinkage(z_mm, D_mm):
    """Rigid-wheel rolling resistance from sinkage: resultant soil force through the axle at half the entry angle."""
    theta = math.acos(1 - 2 * z_mm / D_mm)
    return math.tan(theta / 2)


Dw = 2 * D["wheel_r"]
sink = (25.0, 55.0)
crr_sand = tuple(crr_sinkage(z, Dw) for z in sink)
print(f"sand: sinkage {sink[0]:.0f} to {sink[1]:.0f} mm on a {Dw:.0f} mm wheel gives Crr {crr_sand[0]:.3f} to {crr_sand[1]:.3f}")
out("crr_sand_lo", crr_sand[0], "", "{:.3f}")
out("crr_sand_hi", crr_sand[1], "", "{:.3f}")
n_b = 1.1                              # Bekker sinkage exponent typical of dry sand
kz = 2 / (2 * n_b + 1)                 # z ~ (W / (b sqrt D))^kz for a soil where k_phi dominates
print("tire width and diameter sensitivity (Bekker scaling, Crr ~ sqrt(z/D)):")
for label, b, dia in (("26 x 2.1 in", 54, 667), ("26 x 2.4 in", 61, 681), ("26 x 3.0 in", 76, 711), ("26 x 4.0 in", 102, 763), ("28 x 2.0 in", 50, 722)):
    zf = (54 / b * math.sqrt(667 / dia)) ** kz
    f = math.sqrt(zf * 667 / dia)
    print(f"  {label}: Crr x {f:.2f}, sand push {f * crr_sand[0] * Wl:.0f} to {f * crr_sand[1] * Wl:.0f} N")
    if label == "26 x 4.0 in":
        out("fat_tire_factor", f, "", "{:.2f}")


def push(m, crr, grade=0.0):
    a = math.atan(grade)
    return m * g * (crr * math.cos(a) + math.sin(a))


F_firm = [push(m_load, c) for c in crr_firm]
F_sand = [push(m_load, c) for c in crr_sand]
F_climb = [push(m_load, c, 0.10) for c in crr_firm]
F_desc = [m_load * g * (math.sin(math.atan(0.1)) - c * math.cos(math.atan(0.1))) for c in crr_firm]
print(f"firm level: {F_firm[0]:.1f} to {F_firm[1]:.1f} N; human power at 1.0 m/s {F_firm[0]:.0f} to {F_firm[1]:.0f} W")
print(f"loose sand, unassisted: {F_sand[0]:.0f} to {F_sand[1]:.0f} N")
print(f"10 % climb, firm, unassisted: {F_climb[0]:.1f} to {F_climb[1]:.1f} N")
print(f"10 % descent hold-back: {F_desc[1]:.0f} to {F_desc[0]:.0f} N")
out("F_firm_hi", F_firm[1], "N", "{:.1f}")
out("F_sand_lo", F_sand[0], "N", "{:.0f}")
out("F_sand_hi", F_sand[1], "N", "{:.0f}")
out("F_climb_hi", F_climb[1], "N", "{:.1f}")
out("F_desc_hi", F_desc[0], "N", "{:.0f}")
m_opt = m_empty - opt_total + payload
print(f"with both open mass options ({m_opt:.1f} kg loaded): firm {push(m_opt, crr_firm[1]):.1f} N, 10 % climb {push(m_opt, crr_firm[1], 0.10):.1f} N")
out("F_firm_hi_options", push(m_opt, crr_firm[1]), "N", "{:.1f}")
out("F_climb_hi_options", push(m_opt, crr_firm[1], 0.10), "N", "{:.1f}")
half = m_empty + payload / 2
print(f"sand with two jerrycans only ({half:.1f} kg): {push(half, crr_sand[0]):.0f} to {push(half, crr_sand[1]):.0f} N")
out("F_sand_half_hi", push(half, crr_sand[1]), "N", "{:.0f}")

# ---------------------------------------------------------------- 4. Assist (later prototype)
section("4. Assist kit (later prototype, SwapCell interface v0.3)")
T_motor = 40.0                          # N m, geared 250 W hub motor, assumed peak at low speed
thrust1 = T_motor / R
F_sand_a = [push(m_load_a, c) for c in crr_sand]
F_climb_a = [push(m_load_a, c, 0.10) for c in crr_firm]
print(f"one motor: thrust {thrust1:.0f} N; sand push {F_sand_a[0] - thrust1:.0f} to {F_sand_a[1] - thrust1:.0f} N; "
      f"10 % climb {max(0, F_climb_a[0] - thrust1):.0f} to {F_climb_a[1] - thrust1:.0f} N")
out("F_sand_assist1_hi", F_sand_a[1] - thrust1, "N", "{:.0f}")
need = F_sand_a[1] - 150
print(f"thrust needed to meet R3 on the loosest sand: {need:.0f} N, {need * R:.0f} N m at the wheels "
      f"({need * R / 2:.0f} N m per motor with two motors)")
out("thrust_needed_R3", need, "N", "{:.0f}")
thrust2 = 2 * thrust1
print(f"two motors: thrust {thrust2:.0f} N; sand push {max(0, F_sand_a[0] - thrust2):.0f} to {F_sand_a[1] - thrust2:.0f} N")
out("F_sand_assist2_hi", F_sand_a[1] - thrust2, "N", "{:.0f}")
for v in (0.6, 1.0):
    print(f"  wheel speed at {v} m/s: {v / (2 * math.pi * R) * 60:.1f} rpm")
eta = 0.40                               # motor, gearbox and controller at 17 to 29 rpm (assumed)
for label, F, v in (("one motor, sand", thrust1, 0.6), ("two motors, sand", need, 0.6)):
    p_mech = F * v
    p_el = p_mech / eta
    print(f"  {label}: {p_mech:.0f} W at the wheel, {p_el:.0f} W electric, {p_el - p_mech:.0f} W heat, "
          f"{p_el / 46.8:.1f} A from 46.8 V, {F * 1000 / eta / 3600:.0f} Wh per km")
    if label.startswith("one"):
        out("assist_Wh_per_km_1", F * 1000 / eta / 3600, "Wh/km", "{:.0f}")
    else:
        out("assist_Wh_per_km_2", F * 1000 / eta / 3600, "Wh/km", "{:.0f}")
        out("assist_current_2", p_el / 46.8, "A", "{:.1f}")
E_pack = 452.0                            # Wh, SwapCell at minimum cell capacity (SWC-CAL-001)
print(f"SwapCell {E_pack:.0f} Wh: {E_pack / (thrust1 * 1000 / eta / 3600):.1f} km of one-motor assist; "
      f"{E_pack / (need * 1000 / eta / 3600):.1f} km of two-motor assist on loose sand")
out("assist_range_1", E_pack / (thrust1 * 1000 / eta / 3600), "km", "{:.1f}")
yaw = thrust1 * P["track"] / 2000
Nf = m_load_a * g * front_share
print(f"single motor yaw moment {yaw:.0f} N m; locked casters need {yaw / Lb:.0f} N lateral at the front axle "
      f"({yaw / Lb / Nf * 100:.0f} % of front load); free casters need {yaw / (2 * D['rail_y'] / 1000):.0f} N differential at the grips")
out("yaw_moment", yaw, "N m", "{:.0f}")

# ---------------------------------------------------------------- 5. Brakes and parking (R10)
section("5. Brakes and parking")
r_drum, C_star, cam_ratio, lever_ratio, cable_eff = 0.035, 0.8, 5.0, 4.0, 0.8


def hand_force(F_tires):
    """Hand force for a total tire braking force shared by both rear drums through one lever and a splitter."""
    T_hub = F_tires / 2 * R
    F_act = T_hub / (C_star * r_drum)           # shoe actuation force per hub
    cable = F_act / cam_ratio
    return T_hub, cable, 2 * cable / (lever_ratio * cable_eff)


for label, m in (("unassisted", m_load), ("with assist", m_load_a)):
    a = math.atan(0.20)
    F_park = m * g * math.sin(a)
    T, cab, hand = hand_force(F_park)
    print(f"park on 20 % grade, {label}: {F_park:.0f} N at the tires, {T:.1f} N m per hub, cable {cab:.0f} N, hand {hand:.0f} N")
    if label == "with assist":
        out("F_park_20", F_park, "N", "{:.0f}")
        out("hand_park_20", hand, "N", "{:.0f}")
    for facing, sgn in (("facing downhill", -1), ("facing uphill", 1)):
        Nr = m * g * (math.cos(a) * (1 - front_share) + sgn * math.sin(a) * z_cg / Lb)
        mu_req = F_park / Nr
        print(f"  {facing}: rear axle load {Nr:.0f} N, friction needed {mu_req:.2f}")
        if label == "with assist" and facing == "facing downhill":
            out("mu_req_park", mu_req, "", "{:.2f}")
a10 = math.atan(0.10)
F_stop = m_load_a * g * (math.sin(a10) - crr_firm[0] * math.cos(a10)) + m_load_a * 0.5
T, cab, hand = hand_force(F_stop)
print(f"stop from 1.0 m/s in 1.0 m on a 10 % descent (0.5 m/s2), with assist mass: {F_stop:.0f} N, {T:.1f} N m per hub, hand {hand:.0f} N")
out("hand_stop_10", hand, "N", "{:.0f}")
T, cab, hand = hand_force(F_desc[0])
print(f"hold on a 10 % descent, unassisted: hand {hand:.0f} N")
out("hand_hold_10", hand, "N", "{:.0f}")

# ---------------------------------------------------------------- 6. Frame and axles
section("6. Frame, axles and hip bar")


def I_rhs(h, w, t):
    return (w * h ** 3 - (w - 2 * t) * (h - 2 * t) ** 3) / 12


h, w, t = P["main"]
Z_main = I_rhs(h, w, t) / (h / 2)
print(f"main RHS {h:.0f} x {w:.0f} x {t:.1f}: I = {I_rhs(h, w, t):.0f} mm4, Z = {Z_main:.0f} mm3")
# One side rail as a beam on the rear axle (x = 0) and the front contact (x = wheelbase)
Pc = (payload + sum(cradle.values())) * g / 4            # per hanger
xs = (P["cr_x0"], D["cr_x1"] - 10)
Lmm = P["wheelbase"]
self_w = (frame + 2.2) * g / 2                           # frame and hip bar per side, lumped at x = 600 mm
loads = [(Pc, xs[0]), (Pc, xs[1]), (self_w, 600.0)]
Rf = sum(F * x for F, x in loads) / Lmm
Rr = sum(F for F, _ in loads) - Rf
M390 = Rr * xs[0] - self_w * max(0, xs[0] - 600) / 1000
M_riser = Rf * (Lmm - P["front_x"])
M_arm = Rf * (D["pivot_x"] - P["front_x"] - w / 2)
print(f"per side: hanger load {Pc:.0f} N each, reactions rear {Rr:.0f} N, front {Rf:.0f} N (static)")
for label, Mst in (("rail at rear hanger", M390 / 1000), ("rail at front riser", M_riser / 1000), ("caster arm root", M_arm / 1000)):
    s = Mst * 1000 * DYN / Z_main
    print(f"  {label}: {Mst:.0f} N m static, {Mst * DYN:.0f} N m at {DYN} g, stress {s:.0f} MPa, factor on yield {FY / s:.2f}")
    if label == "caster arm root":
        out("arm_stress", s, "MPa", "{:.0f}")
        out("arm_fos", FY / s, "", "{:.2f}")
    if label == "rail at rear hanger":
        out("rail_stress", s, "MPa", "{:.0f}")
Z_15 = I_rhs(h, w, 1.5) / (h / 2)
print(f"  caster arm with the v0.1 1.5 mm wall (Z {Z_15:.0f} mm3): {M_arm * DYN / Z_15:.0f} MPa, factor {FY / (M_arm * DYN / Z_15):.2f}")
out("arm_fos_15", FY / (M_arm * DYN / Z_15), "", "{:.2f}")
Z_30 = I_rhs(30, 30, 1.5) / 15
s30 = M_arm * DYN / Z_30
print(f"  same caster arm in the TRL 2 section 30 x 30 x 1.5 (Z {Z_30:.0f} mm3): {s30:.0f} MPa, factor {FY / s30:.2f}")
out("arm_stress_30sq", s30, "MPa", "{:.0f}")
rng = M390 * 1.5 / Z_main
print(f"weld fatigue: stress range for +/-0.75 g about 1 g at the rear hanger {rng:.0f} MPa against detail category 71 MPa at 2 million cycles")
out("fatigue_range", rng, "MPa", "{:.0f}")
# Torsion: one front wheel unloaded in a rut
Am = (h - t) * (w - t)
T_tw = Nf_wheel * P["track"] / 1000
tau = T_tw * 1000 / (2 * Am * t)
J = 4 * Am ** 2 * t / (2 * ((h - t) + (w - t)))
GJ = G_STEEL * J / 1e6                                    # N m2
twist = T_tw * (P["front_x"] / 1000) / (2 * GJ)
print(f"torsion with one front wheel unloaded: {T_tw:.0f} N m; shear if one rail carries it {tau:.0f} MPa; "
      f"twist with both rails {math.degrees(twist):.2f} deg, accommodating a rut of {twist * P['track']:.0f} mm")
out("frame_twist", math.degrees(twist), "deg")
out("rut_accommodated", twist * P["track"], "mm", "{:.0f}")
# Rear axle: TRL 2 cantilever stub axle versus the double-supported fork
Fw = Nr_wheel * DYN
d_root = 8.9
for label, arm in (("cantilever stub, 40 mm to the wheel plane", 40.0), ("fork, 100 mm dropouts, flange 15 mm in", 15.0)):
    Mx = Fw * arm if label.startswith("cant") else Fw / 2 * arm
    s = 32 * Mx / (math.pi * d_root ** 3)
    print(f"  M10 x 1 axle, {label}: {Mx / 1000:.1f} N m, {s:.0f} MPa")
    out("axle_stress_" + label.split()[0].replace(",", ""), s, "MPa", "{:.0f}")
# Hip bar uprights
F_hb = max(F_sand[1], 400.0)
Mup = F_hb / 2 * (P["hip_z"] - D["rail_z"]) / 1000
Zs = I_rhs(*P["sleeve"]) / (P["sleeve"][0] / 2)
print(f"hip bar uprights, {F_hb:.0f} N push shared by two: {Mup:.0f} N m each, {Mup * 1000 / Zs:.0f} MPa, factor {FY / (Mup * 1000 / Zs):.1f}")

# ---------------------------------------------------------------- 7. Turning, stability
section("7. Turning and stability")
t2 = P["track"] / 2
wr, tw = D["wheel_r_max"], P["tire_w_max"] / 2


def reach(cx, cy):
    """Largest distance from a turn centre to the carrier, with the casters trailing tangentially."""
    rs = []
    for sy in (1, -1):
        px, py = D["pivot_x"], sy * t2
        rc = math.hypot(math.hypot(px - cx, py - cy), P["trail"])
        rs.append(math.hypot(rc, wr) + tw)                    # front wheel
        rs.append(math.hypot(math.hypot(px - cx, py - cy), P["head_d"] / 2 + 15))  # head tube
        rs.append(math.hypot(math.hypot(-cx, py - cy), wr) + tw)                   # rear wheel
        rs.append(math.hypot(-P["grip_back"] - cx, sy * D["rail_y"] - cy))          # grip ends
    return max(rs)


D_inner = 2 * reach(0.0, -t2)
D_spin = 2 * reach(0.0, 0.0)
print(f"turn about the inner rear wheel: swept circle {D_inner / 1000:.2f} m; spin about the rear axle centre {D_spin / 1000:.2f} m")
out("turn_circle_inner", D_inner / 1000, "m")
out("turn_circle_spin", D_spin / 1000, "m")
tip_side = math.degrees(math.atan(t2 / 1000 / z_cg))
print(f"static side tip angle, loaded: {tip_side:.0f} deg (half track {t2:.0f} mm, centre of mass {z_cg * 1000:.0f} mm)")
out("tip_side", tip_side, "deg", "{:.0f}")
tip_fwd = math.degrees(math.atan((Lb - x_cg) / z_cg))
tip_back = math.degrees(math.atan(x_cg / z_cg))
print(f"static tip angle forward over the front axle {tip_fwd:.0f} deg, backward over the rear axle {tip_back:.0f} deg")

# ---------------------------------------------------------------- 8. Water delivered
section("8. Water delivered")
day, route, v_walk = 100.0, 3.0, 4.0
trips_head = math.ceil(day / 20)
trips_ww = math.ceil(day / 80)
print(f"trips for {day:.0f} L: head {trips_head}, WaterWalker {trips_ww} ({day / 80:.2f} rounded up); "
      f"walking time on a {route:.0f} km round trip at {v_walk:.0f} km/h: {trips_head * route / v_walk:.2f} h vs {trips_ww * route / v_walk:.2f} h")

# ---------------------------------------------------------------- 9. Cost
section("9. Cost from bom/bom.csv")
rows = list(csv.DictReader((ROOT / "bom" / "bom.csv").open()))
base = assist_cost = 0.0
for r in rows:
    c = float(r["qty"]) * float(r["unit_cost_usd"])
    if "Optional" in r["item"]:
        assist_cost += c
    else:
        base += c
budget = 450.0
print(f"first prototype (no assist, with mounting points): ${base:.2f} against ${budget:.0f}, margin ${budget - base:.2f}")
print(f"assist kit (motor, sensor, receiver; SwapCell pack priced in the SwapCell BOM): ${assist_cost:.2f}; "
      f"carrier with assist ${base + assist_cost:.2f}")
out("cost_base", base, "USD")
out("cost_assist_kit", assist_cost, "USD")

# ---------------------------------------------------------------- 10. Requirement table
section("10. Requirements")


def status(value, target, lower_is_better=True):
    r = value / target if lower_is_better else target / value
    return "met" if r <= 0.95 else ("at risk" if r <= 1.0 else "not met")


REQ = [
    ("R1", "80 L in four jerrycans or 40 L in two clay pots; payload 90 kg or less",
     f"{payload:.1f} kg (jerrycans), {pots_payload:.0f} kg (pots); spare length {cradle_len - can_row:.0f} mm (cans), {pot_spare:.0f} mm (pots)",
     "met" if pot_spare >= 0.05 * 2 * pot_d else ("at risk" if pot_spare >= 0 else "not met")),
    ("R2", "60 N or less, firm level path", f"{F_firm[0]:.0f} to {F_firm[1]:.1f} N", status(F_firm[1], 60)),
    ("R3", "150 N or less, loose sand", f"{F_sand[0]:.0f} to {F_sand[1]:.0f} N unassisted; {F_sand_a[1] - thrust1:.0f} N worst with one motor", status(F_sand[1], 150)),
    ("R4", "180 N or less, 10 % climb; controlled descent", f"{F_climb[1]:.1f} N climb; hold-back hand force {hand_force(F_desc[0])[2]:.0f} N", status(F_climb[1], 180)),
    ("R5", "4.0 m turning circle or less", f"{D_inner / 1000:.2f} m (inner rear wheel pivot), {D_spin / 1000:.2f} m (spin)", status(D_inner / 1000, 4.0)),
    ("R6", "900 mm wide or less", f"{D['overall_width']:.0f} mm over axle nuts", status(D["overall_width"], 900)),
    ("R7", "Step-over 50 mm or less; walking width 600 mm or more; hip bar 850 to 1,050 mm; skirt guards",
     f"0 mm; {D['walk_width']:.0f} mm; {P['hip_min']:.0f} to {P['hip_max']:.0f} mm; both rear wheels", status(D["walk_width"], 600, False)),
    ("R8", "Lift 450 mm or less, either side", f"{lift:.0f} mm", status(lift, 450)),
    ("R9", "Empty 35 kg or less (42 kg with assist)", f"{m_empty:.1f} kg ({m_empty_a:.1f} kg)",
     "not met" if (m_empty > 35 or m_empty_a > 42) else status(max(m_empty / 35, m_empty_a / 42), 1.0)),
    ("R10", "Service brake while walking; park rated gross mass on 20 %", f"lock pin for parking; hand {hand_force(m_load_a * g * math.sin(math.atan(0.2)))[2]:.0f} N at the latch; friction needed up to {OUT[[k for k, *_ in OUT].index('mu_req_park')][1]}", "at risk"),
    ("R11", "First prototype, no assist, with mounting points, $450 or less", f"${base:.0f}", status(base, 450)),
    ("R12", "Wear parts are standard 26 in bicycle parts", "100 mm drum hubs, 26 in rims, tires, tubes, cables, headsets", "at risk"),
    ("R13", "Assist-ready to SwapCell interface v0.3", "mounting plate, torque-arm tab, sensor boss in the model; class V1 retention by test only", "not verifiable at TRL 3"),
]
for rid, target, value, st in REQ:
    print(f"  {rid:4s} {st:24s} {value}   [target: {target}]")
    OUT.append((f"req_{rid}", st, value))

with (ROOT / "docs" / "04-calcs" / "results.csv").open("w", newline="") as f:
    wr_ = csv.writer(f)
    wr_.writerow(["key", "value", "unit_or_note"])
    wr_.writerows(OUT)
print("\nwrote docs/04-calcs/results.csv")
