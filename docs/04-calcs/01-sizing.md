---
doc_id: WWK-CAL-001
title: WaterWalker sizing calculations
project: WaterWalker
doc_type: Calculation note
version: "0.2"
status: Draft
date: '2026-09-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-25'
  author: Amish Chadha
  change: First TRL 3 sizing note (geometry, mass, push force on firm ground, slopes and sand, assist, brakes, frame, axles, turning, cost, requirement table)
- version: "0.2"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); 1.2 mm main-tube wall, thinner cradle and parking lock pin applied; all results recalculated
---

# WaterWalker sizing calculations

On paper, the first prototype (no assist, with mounting points) carries 80 L, turns in 3.7 m, lifts containers only 364 mm and costs about $426. Version 0.2 applies Amish's 2026-09-25 decisions (WWK-DDR-002): a 1.2 mm wall on the main tube, a thinner cradle and a positive parking lock pin. The carrier now weighs 37.4 kg empty (40.8 kg in v0.1, 31 kg estimated at TRL 2). **Two requirements are not met:** R3 (loose sand, 236 to 358 N against 150 N) and R9 (37.4 kg against 35 kg). Seven are at risk: R1, R2 (59.7 N against 60 N), R4 (178.3 N against 180 N), R6, R7, R10 and R12. The lighter main tube raises the weld stress range at the cradle hangers to 75 MPa, above the 71 MPa of a typical fillet-welded detail, which is new and flagged for Amish. The calculations also found two layout faults in the TRL 2 concept that are fixed in the model: the cantilevered rear stub axles were overstressed, and the swivelling front tires would hit the front risers.

Every number in this note is printed by `docs/04-calcs/sizing.py` (run from the repo root: `python docs/04-calcs/sizing.py`), which also writes `docs/04-calcs/results.csv`. The script reads the geometry from `cad/src/model.py` and the prices from `bom/bom.csv`, so the note, the model, drawing WWK-DWG-001 and the BOM share one source. All values are first-principles estimates; nothing here is measured.

## 1. Assumptions

*Table 1. Inputs. All are assumptions for a paper design.*

| Input | Value | Basis |
| --- | --- | --- |
| Load | Four 20 L jerrycans, 80 kg of water plus 4 x 1.1 kg; or two 20 L clay pots of 8 kg each | WWK-REQ-001 R1 |
| Wheels | 26 in, ETRTO 559 rim, 2.1 in (54 mm) tires, radius 333.5 mm; 2.4 in (61 mm) also fits, radius 340.5 mm | Decided, WWK-DDR-001 item 1 |
| Hubs | Front-type 100 mm over-locknut hubs on all four wheels; 70 mm drums on the rear pair | Decided, WWK-DDR-001 item 9 (WWK-DDR-002) |
| Rolling resistance, firm dirt path | Crr 0.02 to 0.05 | Typical for wide bicycle tires on packed to rough dirt |
| Rolling resistance, loose sand | Sinkage 25 to 55 mm, giving Crr 0.197 to 0.300 (section 4) | To be measured in the field |
| Grade | 10 % climb and descent (R4); 20 % parking (R10) | WWK-REQ-001 |
| Steel | Mild steel, yield 235 MPa, 7,850 kg/m³, G = 79 GPa | S235 class; ERW tube is often stronger |
| Dynamic factor | 2.5 g on static loads | Ruts, stones and kerbs at walking speed |
| Target factor on yield | 1.5 or more at 2.5 g | Paper design margin |
| Component masses | Rim 0.55 kg, spokes 0.30, puncture-resistant tire 0.85, thorn-resistant tube 0.45, liner 0.20, drum hub 0.75, plain hub 0.35, rigid fork 1.10 each | Typical catalogue values for utility parts |
| Drum brake | 70 mm drum, brake factor C* = 0.8, cam ratio 5, lever ratio 4, cable efficiency 0.8, one lever to both drums | Typical cable-operated drums |
| Assist motor (later) | 250 W, 48 V geared hub motor, 40 N·m at low speed; 40 % efficient at 17 to 29 rpm | Assumed; geared hub motors are rated at much higher speeds |
| SwapCell pack | 46.8 V nominal, 452 Wh at minimum cell capacity, 2.85 kg, 20 A continuous, 15 A in legacy mode | SwapCell interface v0.3 and SWC-CAL-001 |
| Household use | 100 L per day, 3 km round trip at 4 km/h | WWK-PRB-001 |

## 2. Geometry and layout

The layout is set by three limits that squeeze each other: overall width (R6, 900 mm), clear walking width (R7, 600 mm) and 100 mm bicycle hubs held on both sides. With a 770 mm track the carrier is 898 mm wide over the axle nuts and 610 mm clear between the side rails, so both R6 and R7 hold, each by less than 2 %. The overall length is 2,197 mm (2,211 mm with 2.4 in tires).

Two TRL 2 layout faults were found and fixed in the model:

- **Rear axles.** The TRL 2 concept hung each rear wheel on a stub axle outboard of the side rail. A standard M10 bicycle axle cantilevered 40 mm carries about 32.7 N·m at 2.5 g, which is about 472 MPa, beyond what a bicycle axle survives in fatigue. Holding each rear wheel in a fixed rigid bicycle fork with 100 mm dropouts cuts this to about 89 MPa and uses the same fork as the front casters (decided, WWK-DDR-001 item 9, WWK-DDR-002).
- **Caster sweep.** A swivelling front wheel sweeps a circle of 400.5 mm radius about its swivel axis (60 mm trail plus the 2.4 in tire radius). The TRL 2 risers sat inside that circle, so the tire would hit them after only a few degrees of steer. The risers now stand at x = 1,150 mm and the wheelbase is 1,530 mm, which leaves 19.5 mm of clearance (decided, WWK-DDR-001 item 10, WWK-DDR-002).

The cradle is 780 x 430 mm outside and, with the 4 mm walls of v0.2, 772 mm long inside. Two jerrycans in line (720 mm) leave 48 mm; two 380 mm clay pots leave only 12 mm, so the pot case (R1) is at risk until real pot sizes are known. The heaviest lift is over the side rail at 364 mm (R8).

## 3. Mass

*Table 2. Mass roll-up, first prototype.*

| Part | Mass (kg) | Basis |
| --- | --- | --- |
| Frame | 12.83 | 8.27 m of tube from `frame_members()` in the model: 5.69 m of 40 x 30 x 1.2 mm (7.25 kg), 0.97 m of 30 x 30 x 1.5 mm (1.31 kg), 0.89 m of 25 x 25 x 1.5 mm (0.99 kg), 0.71 m of 20 x 20 x 1.5 mm (0.62 kg); head tubes, tabs, receiver plate, welds and paint |
| Rear wheels with drum hubs (2) | 6.20 | Table 1 |
| Front wheels (2) | 5.40 | Table 1 |
| Forks (4) | 4.40 | Table 1 |
| Headsets, clamps and swivel locks | 0.60 | Estimate |
| Hip bar, posts, pad and grips | 2.20 | Estimate |
| Cradle | 3.29 | 6 mm plywood floor 1.21, 2 mm rubber pad 0.75, 4 mm walls 0.93, straps 0.40 |
| Brake lever, latch and cables | 0.45 | Estimate |
| Skirt guards (2) | 1.29 | 3 mm HDPE |
| Hardware and reflectors | 0.60 | Estimate |
| Parking lock pin, tab and lanyard | 0.10 | Estimate (WWK-DDR-002) |
| **Total, empty** | **37.35 (82.4 lb)** | R9 limit 35 kg |

The assist kit adds 6.50 kg (motor wheel less the drum hub, disc brake, controller, sensor, class V1 receiver and the 2.85 kg SwapCell pack), for 43.85 kg against the 42 kg limit. Loaded with four jerrycans, the carrier weighs 121.8 kg, or 128.3 kg with the assist kit. The loaded centre of mass is 716 mm ahead of the rear axle and 360 mm above the ground, so the front wheels carry 46.8 % of the load: about 279 N per front wheel and 318 N per rear wheel.

R9 is **not met**, by 2.4 kg. The TRL 2 figure of 31 kg left out the tires, tubes and liners (1.5 kg per wheel), the fourth pair of forks, and the heavier frame section that the strength check calls for. Amish decided on 2026-09-25 (WWK-DDR-001 item 12, WWK-DDR-002) to apply two of the four v0.1 mass options, the 1.2 mm wall on the main tube (1.80 kg saved) and the thinner cradle (floor 9 to 6 mm, walls 6 to 4 mm, pad 4 to 2 mm; 1.80 kg saved), to keep the puncture protection, and to revisit R9 with users in co-design. With the 0.10 kg lock pin the empty mass falls from 40.85 kg to 37.35 kg. The two options left open, tires without a puncture belt and no tire liners, would save 1.60 kg more (35.75 kg, still over 35 kg) at the cost of punctures on thorny paths.

## 4. Push force

Push force is F = m g (Crr cos α + sin α) for a grade angle α.

On a firm, level dirt path the loaded carrier needs 23.9 to 59.7 N, which is 24 to 60 W of human power at 1.0 m/s. R2 is **at risk**, with 0.3 N of margin at the rough end (61.4 N and not met in v0.1). Climbing a 10 % grade on firm ground takes 142.6 to 178.3 N; R4 is **at risk**, with 1.7 N of margin (183.4 N and not met in v0.1). Both follow from the mass: with the two open mass options as well the figures would be 58.9 N and 175.9 N.

**Loose sand.** A rigid wheel that sinks z into soil meets it at an entry angle θ, where cos θ = 1 - 2z/D, and the soil reaction passes through the axle, so the rolling resistance coefficient is tan(θ/2). For a 667 mm wheel, a sinkage of 25 to 55 mm gives Crr 0.197 to 0.300, which matches the 0.2 to 0.3 used at TRL 2. The loaded carrier then needs **236 to 358 N**, which is 1.6 to 2.4 times the 150 N target. R3 is **not met**, and the first prototype has no assist.

*Table 3. Effect of tire size on the sand push force (loaded, unassisted).*

| Tire | Crr factor | Sand push force (N) |
| --- | --- | --- |
| 26 x 2.1 in | 1.00 | 236 to 358 |
| 26 x 2.4 in | 0.95 | 224 to 340 |
| 26 x 3.0 in | 0.86 | 203 to 309 |
| 26 x 4.0 in (fat bike) | 0.75 | 177 to 269 |
| 28 x 2.0 in | 0.97 | 229 to 348 |

The factors scale sinkage with Bekker's pressure-sinkage relation for a soil whose frictional modulus dominates, with a sinkage exponent n of 1.1, typical of dry sand, so sinkage varies as (W / (b √D))^(2/(2n+1)), and Crr as √(z/D). They are relative only. Even fat-bike tires leave the push force well above 150 N, so the TRL 2 question of whether wider tires could avoid assist is answered: they cannot. Carrying only two jerrycans on a sandy stretch (79.6 kg) still takes 154 to 234 N.

On a 10 % descent the carrier pulls downhill with 59 to 95 N more than rolling resistance absorbs.

## 5. Assist kit (later prototype)

The assist is not in the first prototype (WWK-DDR-001 item 2); this section checks that the mounting points suit a later kit built to SwapCell interface v0.3.

One 250 W geared hub motor at 40 N·m gives 120 N of thrust at the 333.5 mm wheel radius. On loose sand the user would still push 128 to 257 N, so one motor does not meet R3. Meeting R3 on the loosest sand with the assisted mass takes 227 N of thrust, 76 N·m at the wheels: about 38 N·m from each of two motors, one in each rear wheel. With two motors the user pushes 8 to 137 N. Two motors also cancel the yaw from one-sided drive: one motor makes a 46 N·m yaw moment, which locked casters resist with 30 N of side force (5 % of the front load) but free casters leave to the user as a 72 N difference between the hands.

At walking pace the wheel turns at only 17.2 rpm (0.6 m/s) to 28.6 rpm (1.0 m/s), far below where hub motors are efficient. At an assumed 40 % efficiency, one motor on sand uses 180 W and turns 108 W into heat; two motors at the R3 thrust use 341 W (7.3 A from the 46.8 V pack) and make 204 W of heat, so motor temperature is at risk and needs a thermal check before any assist build. Energy use is about 83 Wh/km with one motor and 158 Wh/km with two on loose sand, so a SwapCell pack (452 Wh) gives about 5.4 km or 2.9 km of assisted sand. The current is well inside the pack's 15 A legacy-mode limit, so a simple controller without CAN can use the pack through the INTERLOCK coding resistor alone (interface v0.3 item W).

## 6. Brakes and parking (R10)

Parking the assisted carrier (128.3 kg) on a 20 % grade needs 247 N at the tires, or 41.1 N·m in each rear drum. With the assumed drum and cable ratios that needs about 184 N at the lever when the latch is set (174 N unassisted), which is a hard squeeze for many users. Amish decided on 2026-09-25 to add a positive lock pin and keep the latch for short stops (WWK-DDR-001 item 13, WWK-DDR-002). The 10 mm pin is pushed from the walking space through the left skirt guard and the left rear spokes, 200 mm above and 60 mm behind the axle, so parking no longer depends on hand force. Pinning one wheel puts the whole 247 N parking force through that wheel's spokes and fork; the pin then pushes sideways on the spokes it meets with about the tire force times the wheel radius over the pin radius (247 N x 333.5 / 200), about 410 N. That load bends the spokes rather than pulling them, so the pin fit, a guard sleeve on the pin and spoke damage need a test. Traction is the second limit and the pin does not change it: parked facing downhill, the rear wheels carry only 598 N, so the tires need a friction coefficient of 0.41 (0.35 facing uphill); with only the pinned wheel locked, that wheel alone must supply the force. That holds on firm dirt but not reliably on loose gravel or sand. R10 therefore stays **at risk**.

Holding speed on a 10 % descent takes about 71 N at the lever, and stopping from 1.0 m/s within 1.0 m (0.5 m/s²) with the assisted mass takes about 122 N. The service brake meets R4's descent clause on paper, but sustained 71 N on long descents is tiring.

## 7. Frame, axles and hip bar

One side rail is treated as a beam on the rear axle and the front tire contact, loaded through two cradle hangers (219 N each, static) and its share of frame mass. Table 4 gives the peak bending stresses at 2.5 g for the 40 x 30 x 1.2 mm rectangular section (Z = 1,887 mm³).

*Table 4. Frame stresses at 2.5 g.*

| Location | Moment, static (N·m) | Moment at 2.5 g (N·m) | Stress (MPa) | Factor on yield |
| --- | --- | --- | --- | --- |
| Side rail at the rear hanger | 94 | 235 | 124 | 1.89 |
| Side rail at the front riser | 89 | 224 | 119 | 1.98 |
| Caster arm root | 100 | 250 | 133 | 1.77 |

The TRL 2 section (30 x 30 x 1.5 mm square) would reach 162 MPa at the caster arm root, a factor of only 1.45, so the main members are 40 x 30 mm (decided, WWK-DDR-001 item 11). The v0.1 wall of 1.5 mm would give 109 MPa (factor 2.16); the decided 1.2 mm wall (item 12) still gives a factor of 1.77, above the 1.5 target. Weld fatigue is **at risk and now past the reference value**: a ±0.75 g swing about 1 g gives a 75 MPa stress range at the rear hanger (63 MPa in v0.1), above the 71 MPa of a typical fillet-welded detail at 2 million cycles. Gussets at the hanger and caster arm joints, or a local 1.5 mm wall there, are options for Amish (`docs/REVIEW.md`); either way it cannot be verified without testing.

With one front wheel unloaded in a rut, the frame carries 215 N·m of torsion. If one rail took it all the shear stress would be 80 MPa; shared by both rails the frame twists about 2.02 degrees, so a front wheel stays on the ground over a rut about 27 mm deep before the carrier rests on three wheels.

The hip bar uprights (30 x 30 x 1.5 mm) carry a 400 N push shared between them at 616 mm above the rails: 123 N·m and 80 MPa each, a factor of 2.9.

## 8. Turning and stability

With the casters trailing tangentially and the 2.4 in tires, a turn about the inner rear wheel sweeps a circle of 3.66 m, and a spin about the rear axle centre (one rear wheel rolling backward) sweeps 3.41 m. R5 is met.

The static side tip angle, loaded, is 47 degrees (half track 385 mm, centre of mass 360 mm). The static tip angles over the front and rear axles are 66 and 63 degrees. These are static angles; a wheel dropping into a rut on a cross-slope still needs a dynamic check in the field.

## 9. Water delivered and cost

A household using 100 L per day needs 5 head-carried trips or 2 WaterWalker trips (1.25 rounded up). On a 3 km round trip at 4 km/h that is 3.75 h against 1.50 h of walking, if walking speed is similar; sandy routes are slower.

The priced BOM gives **$426.00** for the first prototype (no assist, with mounting points) against the $450 budget, a margin of $24.00 (5.3 %), so R11 is met. The thinner main tube and cradle save $9 and the lock pin adds $5. The assist kit (hub motor, sensor and class V1 receiver) adds $260.00; the SwapCell pack is priced once in the SwapCell BOM and excluded here.

## 10. Results against every requirement

Status rule: **met** means the value is within 95 % of the limit; **at risk** means within the limit but with less than 5 % margin, or dependent on an unverified assumption; **not met** means past the limit.

*Table 5. Requirement results (WWK-REQ-001 v0.4).*

| ID | Target | Value | Status |
| --- | --- | --- | --- |
| R1 | 80 L in four jerrycans or 40 L in two clay pots; payload 90 kg or less | 84.4 kg with jerrycans, 56 kg with pots; spare length 48 mm (jerrycans), 12 mm (pots) | At risk (pot size) |
| R2 | 60 N or less, firm level path | 23.9 to 59.7 N | At risk |
| R3 | 150 N or less, loose sand (with assist if fitted) | 236 to 358 N unassisted; 128 to 257 N with one motor; 8 to 137 N with two | **Not met** (first prototype has no assist) |
| R4 | 180 N or less on a 10 % climb; controlled descent | 142.6 to 178.3 N climb; 71 N at the lever to hold on the descent | At risk (climb) |
| R5 | 4.0 m turning circle or less | 3.66 m about the inner rear wheel; 3.41 m spin | Met |
| R6 | 900 mm wide or less | 898 mm over the axle nuts | At risk |
| R7 | No step-over; walking width 600 mm or more; hip bar 850 to 1,050 mm; skirt guards | 0 mm; 610 mm; 850 to 1,050 mm; guards on both rear wheels | At risk (walking width margin 10 mm) |
| R8 | Lift 450 mm or less, from either side | 364 mm | Met |
| R9 | Empty 35 kg or less (42 kg with assist) | 37.4 kg (43.9 kg) | **Not met** |
| R10 | Service brake while walking; park rated gross mass on 20 % | Lever on the grip; positive lock pin for parking (latch 184 N for short stops); tire friction 0.41 needed | At risk |
| R11 | First prototype (no assist, with mounting points) $450 or less | $426 | Met |
| R12 | Wear parts are standard 26 in bicycle parts | 26 in rims, tires, tubes, spokes, cables, headsets; 100 mm drum hubs are less common than rim-brake hubs in rural markets | At risk |
| R13 | Assist-ready to SwapCell interface v0.3 | Receiver plate, torque-arm tab and sensor boss in the model; 7.3 A peak against the 15 A legacy limit; latch class V1 retention needs a test | Not verifiable at TRL 3 |

Summary: 3 met, 7 at risk, 2 not met (R3, R9), 1 not verifiable at TRL 3. In v0.1: 2 met, 6 at risk, 4 not met (R2, R3, R4, R9).

## 11. Corrections to TRL 2 figures

The TRL 2 figures in WWK-PRC-001 v0.2 were checked against this script and corrected in v0.3: empty mass 31 kg to 40.8 kg (47.3 kg with assist); loaded mass 115 kg to 125.2 kg; firm push force 25 to 55 N to 24.6 to 61.4 N; sand push force 225 to 340 N to 242 to 368 N; 10 % climb 135 to 170 N to 146.7 to 183.4 N; hold-back on the descent 55 to 90 N to 61 to 98 N; parking force 250 N to 253 N; turning circle 3.8 m to 3.66 m; width 860 mm to 898 mm; walking width 660 mm to 610 mm; lift height 350 mm to 364 mm; side tip angle 45 degrees to 47 degrees; parts cost about $300 to $430; assist energy 70 Wh/km to 83 Wh/km; and the assist pack is 46.8 V (SwapCell 13S), not 36 V.

Version 0.2 (WWK-DDR-002) then changed: empty mass 40.8 kg to 37.4 kg; loaded mass 125.2 kg to 121.8 kg; firm push force 61.4 N to 59.7 N; 10 % climb 183.4 N to 178.3 N; sand 242 to 368 N to 236 to 358 N; caster arm stress 112 MPa to 133 MPa; weld stress range 63 MPa to 75 MPa; parts cost $430 to $426.

> **Safety:** These are paper calculations. The brake, parking and frame figures depend on assumed drum ratios, tire friction and a 2.5 g dynamic factor, none of which has been measured. Nothing in this note makes the carrier safe to build or load. TRL 4 testing is on hold by Amish's instruction.
