---
doc_id: WWK-CAL-001
title: WaterWalker sizing calculations
project: WaterWalker
doc_type: Calculation note
version: "0.4"
status: Draft
date: '2026-10-02'
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
- version: "0.3"
  date: '2026-10-02'
  author: Amish Chadha
  change: Constructable design (WWK-DDR-003); mass, frame load path, rear head tube brackets, cradle bearers and lock pin checked; budget treated as a value-engineering target; all results recalculated
- version: "0.4"
  date: '2026-10-02'
  author: Amish Chadha
  change: Decisions of 2026-10-02 carried into the design; hold-to-release brake (mass, spring, bail forces, descent and parking), two-motor assist kit and its value-engineering target, second torque-arm tab, rating plates; all results recalculated
---

# WaterWalker sizing calculations

On paper, the first prototype (no assist, with mounting points) carries 80 L, turns in 3.7 m, lifts containers only 364 mm and has parts estimated at USD 492, USD 42 over the USD 450 value-engineering target. Version 0.4 follows the constructable design of WWK-DDR-003 (accepted by Amish on 2026-10-02) with the decisions of the same day carried in: a hold-to-release brake (a bail under the left grip, a spring unit on the left hip sleeve and a cable yoke to both rear drums), a torque-arm tab on each rear fork for the two-motor assist kit, rated load and slope plates and hand holds in the cradle walls. The carrier now weighs 40.3 kg empty (39.6 kg in v0.3). **Four requirements are not met:** R2 (firm path, 61.2 N against 60 N), R3 (loose sand, 241 to 367 N against 150 N), R4 (10 % climb, 182.6 N against 180 N) and R9 (40.3 kg against 35 kg); no status changed from v0.3. Five are at risk: R1, R6, R7, R10 and R12. The spring of the hold-to-release brake alone holds the loaded carrier with the assist kit on grades up to 12 %. The weld stress range in the rail stays at 61 MPa, below the 71 MPa reference, and the rear brackets, cradle bearers and two-tab lock pin keep a factor of 1.9 or more on yield.

Every number in this note is printed by `docs/04-calcs/sizing.py` (run from the repo root: `python docs/04-calcs/sizing.py`), which also writes `docs/04-calcs/results.csv`. The script reads the geometry from `cad/src/model.py` and the prices from `bom/bom.csv`, so the note, the model, drawing WWK-DWG-001 and the BOM share one source. All values are first-principles estimates; nothing here is measured.

## 1. Assumptions

*Table 1. Inputs. All are assumptions for a paper design.*

| Input | Value | Basis |
| --- | --- | --- |
| Load | Four 20 L jerrycans, 80 kg of water plus 4 x 1.1 kg; or two 20 L clay pots of 8 kg each | WWK-REQ-001 R1 |
| Wheels | 26 in, ETRTO 559 rim, 2.1 in (54 mm) tires, radius 333.5 mm; 2.4 in (61 mm) also fits, radius 340.5 mm | Decided, WWK-DDR-001 item 1 |
| Hubs | Front-type 100 mm over-locknut hubs on all four wheels; 70 mm drums on the rear pair | Decided, WWK-DDR-001 item 9 (WWK-DDR-002) |
| Forks | Four identical rigid 26 in forks, 60 mm offset: the caster trail at the front; the rear head tubes stand 60 mm behind the rear axle | WWK-DDR-003, P3; offset to confirm when bought |
| Rolling resistance, firm dirt path | Crr 0.02 to 0.05 | Typical for wide bicycle tires on packed to rough dirt |
| Rolling resistance, loose sand | Sinkage 25 to 55 mm, giving Crr 0.197 to 0.300 (section 4) | To be measured in the field |
| Grade | 10 % climb and descent (R4); 20 % parking (R10) | WWK-REQ-001 |
| Steel | Mild steel, yield 235 MPa, 7,850 kg/m³, G = 79 GPa | S235 class; ERW tube is often stronger |
| Dynamic factor | 2.5 g on static loads | Ruts, stones and kerbs at walking speed |
| Target factor on yield | 1.5 or more at 2.5 g | Paper design margin |
| Component masses | Rim 0.55 kg, spokes 0.30, puncture-resistant tire 0.85, thorn-resistant tube 0.45, liner 0.20, drum hub 0.75, plain hub 0.35, rigid fork 1.10, headset 0.12, lock collar and plate 0.06, lock pin 0.03 each | Typical catalogue values for utility parts |
| Drum brake | 70 mm drum, brake factor C* = 0.8, cam ratio 5, lever ratio 4, cable efficiency 0.8, one lever to both drums through the cable yoke | Typical cable-operated drums |
| Hold-to-release brake | Spring sized to hold the loaded carrier with the assist kit on 10 % with a margin of 1.25; spring rate 10 N/mm, 8 mm of release travel; bail ratio 6; a toggle in the unit carries the spring once the bail is home, so holding takes 0.25 of the squeeze | Decided 2026-10-02 (WWK-DEC-001); the toggle factor is an estimate |
| Assist motor (later) | Two 250 W, 48 V geared hub motors, one in each rear wheel, 40 N·m each at low speed; 40 % efficient at 17 to 29 rpm | Two-motor kit decided 2026-10-02; geared hub motors are rated at much higher speeds |
| SwapCell pack | 46.8 V nominal, 452 Wh at minimum cell capacity, 2.85 kg, 20 A continuous, 15 A in legacy mode | SwapCell interface v0.3 and SWC-CAL-001 |
| Household use | 100 L per day, 3 km round trip at 4 km/h | WWK-PRB-001 |

## 2. Geometry and layout

The layout is set by three limits that squeeze each other: overall width (R6, 900 mm), clear walking width (R7, 600 mm) and 100 mm bicycle hubs held on both sides. With a 770 mm track the carrier is 898 mm wide over the axle nuts and 610 mm clear between the side rails, so both R6 and R7 hold, each by less than 2 %. The overall length is 2,197 mm (2,211 mm with 2.4 in tires).

Two TRL 2 layout faults were found and fixed in the model:

- **Rear axles.** The TRL 2 concept hung each rear wheel on a stub axle outboard of the side rail. A standard M10 bicycle axle cantilevered 40 mm carries about 32.7 N·m at 2.5 g, which is about 472 MPa, beyond what a bicycle axle survives in fatigue. Holding each rear wheel in a fixed rigid bicycle fork with 100 mm dropouts cuts this to about 89 MPa and uses the same fork as the front casters (decided, WWK-DDR-001 item 9, WWK-DDR-002).
- **Caster sweep.** A swivelling front wheel sweeps a circle of 400.5 mm radius about its swivel axis (60 mm trail plus the 2.4 in tire radius). The TRL 2 risers sat inside that circle, so the tire would hit them after only a few degrees of steer. The risers now stand at x = 1,150 mm and the wheelbase is 1,530 mm, which leaves 19.5 mm of clearance (decided, WWK-DDR-001 item 10, WWK-DDR-002).

The cradle is 780 x 430 mm outside and, with the 4 mm walls of v0.2, 772 mm long inside. It rests on two bearers 150 mm above the ground, so the ground clearance under the carrier is 125 mm (WWK-DDR-003, P4). Two jerrycans in line (720 mm) leave 48 mm; two 380 mm clay pots leave only 12 mm, so the pot case (R1) is at risk until real pot sizes are known. The heaviest lift is over the side rail at 364 mm (R8).

## 3. Mass

*Table 2. Mass roll-up, first prototype.*

| Part | Mass (kg) | Basis |
| --- | --- | --- |
| Frame, rear brackets and cradle carrier | 14.51 | 9.72 m of tube from `frame_members()` in the model: 5.24 m of 40 x 30 x 1.2 mm (6.67 kg), 0.93 m of 30 x 30 x 1.5 mm (1.25 kg), 2.88 m of 25 x 25 x 1.5 mm (3.18 kg), 0.67 m of 20 x 20 x 1.5 mm (0.58 kg); head tubes, receiver plate, tabs (two torque-arm tabs and the spring unit tab), pin guides, welds and paint |
| Rear wheels with drum hubs (2) | 6.20 | Table 1 |
| Front wheels (2) | 5.40 | Table 1 |
| Forks (4) | 4.40 | Table 1 |
| Headsets, lock collars and lock pins (4 sets) | 0.84 | Table 1 (WWK-DDR-003) |
| Hip bar, posts, pad and grips | 2.20 | Estimate |
| Cradle | 3.29 | 6 mm plywood floor 1.21, 2 mm rubber pad 0.75, 4 mm walls 0.93, straps 0.40 |
| Brake lever, latch and service cable | 0.45 | Estimate |
| Hold-to-release brake: bail, spring unit, yoke and cables | 0.60 | Estimate (decided 2026-10-02) |
| Skirt guards (2) | 1.29 | 3 mm HDPE |
| Hardware, reflectors and two rating plates | 0.64 | Estimate |
| Cradle brackets and bolts; guard clips and bolts | 0.33 | Estimate (WWK-DDR-003) |
| Parking lock pin, two tabs and lanyard | 0.13 | Estimate (WWK-DDR-002, WWK-DDR-003) |
| **Total, empty** | **40.28 (88.8 lb)** | R9 limit 35 kg |

The two-motor assist kit adds 9.35 kg (two motor wheels less the drum hubs, two disc brakes, two controllers and wiring, the push sensor, the class V1 receiver and the 2.85 kg SwapCell pack), for 49.63 kg against the 42 kg limit. Loaded with four jerrycans, the carrier weighs 124.7 kg, or 134.0 kg with the assist kit. The loaded centre of mass is 712 mm ahead of the rear axle and 365 mm above the ground, so the front wheels carry 46.5 % of the load: about 285 N per front wheel and 327 N per rear wheel.

R9 is **not met**, by 5.3 kg. In v0.3 the carrier was 39.57 kg (37.35 kg in v0.2, 40.85 kg in v0.1). The decisions of 2026-10-02 added 0.71 kg: the hold-to-release brake (0.60 kg), the second torque-arm tab and the spring unit tab, and two rating plates. Making the design constructable (WWK-DDR-003) had added 2.24 kg: the cradle carrier and second rear brackets, headsets and lock collars, cradle brackets, guard fixings and the second lock pin tab. The two mass options left open in WWK-DDR-002, tires without a puncture belt and no tire liners, would save 1.60 kg (38.68 kg); Amish kept the puncture protection on 2026-10-02 (WWK-DEC-001).

## 4. Push force

Push force is F = m g (Crr cos α + sin α) for a grade angle α.

On a firm, level dirt path the loaded carrier needs 24.5 to 61.2 N, which is 24 to 61 W of human power at 1.0 m/s. R2 is **not met**, by 1.2 N at the rough end (60.8 N in v0.3). Climbing a 10 % grade on firm ground takes 146.0 to 182.6 N; R4 is **not met**, by 2.6 N (181.5 N in v0.3). Both follow from the mass, and the hold-to-release brake moved both a little further from their limits; Amish accepted R2 and R4 as not met on paper on 2026-10-02, with the push limits to be confirmed with users. With the two mass options as well the figures would be 60.4 N and 180.2 N.

**Loose sand.** A rigid wheel that sinks z into soil meets it at an entry angle θ, where cos θ = 1 - 2z/D, and the soil reaction passes through the axle, so the rolling resistance coefficient is tan(θ/2). For a 667 mm wheel, a sinkage of 25 to 55 mm gives Crr 0.197 to 0.300, which matches the 0.2 to 0.3 used at TRL 2. The loaded carrier then needs **241 to 367 N**, which is 1.6 to 2.4 times the 150 N target. R3 is **not met**, and the first prototype has no assist.

*Table 3. Effect of tire size on the sand push force (loaded, unassisted).*

| Tire | Crr factor | Sand push force (N) |
| --- | --- | --- |
| 26 x 2.1 in | 1.00 | 241 to 367 |
| 26 x 2.4 in | 0.95 | 229 to 348 |
| 26 x 3.0 in | 0.86 | 208 to 316 |
| 26 x 4.0 in (fat bike) | 0.75 | 181 to 275 |
| 28 x 2.0 in | 0.97 | 235 to 357 |

The factors scale sinkage with Bekker's pressure-sinkage relation for a soil whose frictional modulus dominates, with a sinkage exponent n of 1.1, typical of dry sand, so sinkage varies as (W / (b √D))^(2/(2n+1)), and Crr as √(z/D). They are relative only. Even fat-bike tires leave the push force well above 150 N, so the TRL 2 question of whether wider tires could avoid assist is answered: they cannot. Carrying only two jerrycans on a sandy stretch (82.5 kg) still takes 160 to 243 N.

On a 10 % descent the carrier pulls downhill with 61 to 97 N more than rolling resistance absorbs.

## 5. Assist kit (later prototype)

The assist is not in the first prototype (WWK-DDR-001 item 2); this section checks that the mounting points suit a later kit built to SwapCell interface v0.3. Amish decided on 2026-10-02 that the assist prototype is a two-motor kit, one geared hub motor in each rear wheel, each held by a torque arm bolted to a tab on its rear fork; both rear forks now carry the tab.

Value-engineering target for the assist prototype: USD 450 (two motors with their controllers, the push sensor and the class V1 receiver; the shared SwapCell pack is counted separately). Estimated cost of the two-motor kit: USD 450 (on the target). The USD 260 one-motor kit is used only if sand trials show one motor meets R3.

One 250 W geared hub motor at 40 N·m gives 120 N of thrust at the 333.5 mm wheel radius. On loose sand the user would still push 140 to 274 N with one motor, so one motor does not meet R3. Meeting R3 on the loosest sand with the assisted mass (134.0 kg with two motors) takes 244 N of thrust, 81 N·m at the wheels: about 41 N·m from each motor, slightly above the 40 N·m assumed. With two motors the user pushes 20 to 154 N, so on the loosest sand the two-motor kit is now 4 N short of R3 (144 N in v0.3, when the second motor's mass was not counted); a motor of about 41 N·m, or less mass, closes the gap. Two motors also cancel the yaw from one-sided drive: one motor makes a 46 N·m yaw moment, which locked casters resist with 30 N of side force (5 % of the front load) but free casters leave to the user as a 72 N difference between the hands.

At walking pace the wheel turns at only 17.2 rpm (0.6 m/s) to 28.6 rpm (1.0 m/s), far below where hub motors are efficient. At an assumed 40 % efficiency, one motor on sand uses 180 W and turns 108 W into heat; two motors at the R3 thrust use 366 W (7.8 A from the 46.8 V pack) and make 220 W of heat, so motor temperature is at risk and needs a thermal check before any assist build. Energy use is about 83 Wh/km with one motor and 170 Wh/km with two on loose sand, so a SwapCell pack (452 Wh) gives about 5.4 km or 2.7 km of assisted sand. The current is well inside the pack's 15 A legacy-mode limit, so a simple controller without CAN can use the pack through the INTERLOCK coding resistor alone (interface v0.3 item W).

## 6. Brakes and parking (R10)

Parking the assisted carrier (134.0 kg) on a 20 % grade needs 258 N at the tires, or 43.0 N·m in each rear drum. With the assumed drum and cable ratios that needs about 192 N at the lever when the latch is set (179 N unassisted), which is a hard squeeze for many users. Amish decided on 2026-09-25 to add a positive lock pin and keep the latch for short stops (WWK-DDR-001 item 13, WWK-DDR-002). The 10 mm pin is pushed from the walking space through a tab on the inner fork blade, the left skirt guard, the left rear spokes and a tab on the outer blade, 200 mm above and 60 mm behind the axle, so parking no longer depends on hand force. Pinning one wheel puts the whole parking force through that wheel's spokes and fork; the spokes push sideways on the pin with about the tire force times the wheel radius over the pin radius (258 N x 333.5 / 200), about 430 N. Held by the inner tab alone, as in the concept, the pin would bend as a cantilever at 219 MPa, a factor of only 1.1; held by both tabs (WWK-DDR-003) it sees 123 MPa, a factor of 1.9. The spokes still take that load in bending, so the pin fit and spoke damage need a test. Traction is the second limit and the pin does not change it: parked facing downhill, the rear wheels carry only 628 N, so the tires need a friction coefficient of 0.41 (0.34 facing uphill); with only the pinned wheel locked, that wheel alone must supply the force. That holds on firm dirt but not reliably on loose gravel or sand. R10 therefore stays **at risk**.

Holding speed on a 10 % descent takes about 72 N at the lever, and stopping from 1.0 m/s within 1.0 m (0.5 m/s²) with the assisted mass takes about 128 N. The service brake meets R4's descent clause on paper, but sustained 72 N on long descents is tiring.

**Hold-to-release brake (decided 2026-10-02).** A spring in the unit on the left hip sleeve pulls both rear drum cables through the cable yoke unless the user holds the bail under the left grip; the service lever pulls the same yoke, so either one brakes both drums. If the user lets go on a 10 % descent, the loaded carrier with the assist kit pulls downhill with 105 N more than rolling resistance absorbs at the low end (Crr 0.02). Holding that takes 312 N of spring force at the yoke; with a margin of 1.25 the spring is set to about **390 N**. On its own the spring then gives 131 N at the rear tires, which holds the loaded carrier with the assist kit on grades up to **12 %**, and if the user lets go at 1.0 m/s on a 10 % descent the carrier slows at 0.20 m/s² and stops in about **2.6 m**. Squeezing the bail home against the spring, with a bail ratio of 6 and 8 mm of release travel, takes about **98 N**, about the same as a firm stop on the service lever; a toggle in the unit then carries most of the spring load, so holding the bail while walking takes about **24 N** (an estimate that depends on the toggle). The spring alone does not park on 20 %: the latch and the lock pin stay the parking brakes. With the assist kit fitted the yoke cables go to the motor wheels' disc brakes, and the bail also works the controllers' brake cut-off, so letting go stops the motors as well.

## 7. Frame, axles and hip bar

In the constructable design (WWK-DDR-003) the side rail no longer reaches the rear axle: the rear wheel load comes up the fork into the rear head tube, through its two brackets and down the hip sleeve onto the rail. One side rail is therefore treated as a beam on the hip sleeve (60 mm ahead of the rear axle) and the front tire contact. The cradle hangs from the rear and front lower cross members, which load each rail with 215 N (static) at 332.5 mm and 1,150 mm, plus the rail's share of frame mass. Table 4 gives the peak bending stresses at 2.5 g for the 40 x 30 x 1.2 mm rectangular section (Z = 1,887 mm³).

*Table 4. Frame stresses at 2.5 g.*

| Location | Moment, static (N·m) | Moment at 2.5 g (N·m) | Stress (MPa) | Factor on yield |
| --- | --- | --- | --- | --- |
| Side rail at the rear cross member | 77 | 193 | 102 | 2.30 |
| Side rail at the front riser | 87 | 218 | 116 | 2.03 |
| Caster arm root | 98 | 244 | 129 | 1.82 |

The TRL 2 section (30 x 30 x 1.5 mm square) would reach 158 MPa at the caster arm root, a factor of only 1.49, so the main members are 40 x 30 mm (decided, WWK-DDR-001 item 11); the decided 1.2 mm wall (item 12) gives a factor of 1.82, above the 1.5 target. Each caster arm now leaves the upper cross member directly over its riser (WWK-DDR-003, P6), so its root moment goes straight down the riser rather than twisting the cross member. Weld fatigue is **at risk**: a ±0.75 g swing about 1 g gives a 61 MPa stress range in the rail at the rear cross member, below the 71 MPa of a typical fillet-welded detail at 2 million cycles (75 MPa at the old hanger position in v0.2). Only a test can confirm the life; until the TRL 4 fatigue test, Amish decided on 2026-10-02 that the rear cross member and caster arm welds are inspected at every service (build plan, first checks and service).

**Rear head tube brackets.** Each rear head tube sits 60 mm behind the axle, on two 25 x 25 x 1.5 mm brackets 60 mm apart that weld to the hip sleeve. The worst case is parking on 20 % with the lock pin through one wheel: 258 N at that tire, about 200 N·m about the bracket level, or 3,331 N of push and pull in the two brackets. The short stubs then bend at 97 MPa (factor 2.4) and the arms carry 24 MPa in tension or compression. Under the rear wheel load at 2.5 g (817 N, shared by the two brackets) the arms see 41 MPa of bending and 16 MPa of twist, 50 MPa combined (factor 4.7). Below the brackets the hip sleeve carries the parking moment at 129 MPa (factor 1.8, static).

**Cradle bearers.** Each 25 x 25 x 1.5 mm bearer spans 818 mm between its hangers and carries half the loaded cradle: 1,075 N at 2.5 g, 110 N·m, 105 MPa (factor 2.2).

With one front wheel unloaded in a rut, the frame carries 219 N·m of torsion. If one rail took it all the shear stress would be 82 MPa; shared by both rails the frame twists about 2.06 degrees, so a front wheel stays on the ground over a rut about 28 mm deep before the carrier rests on three wheels.

Each rear wheel sits in a fork with 100 mm dropouts, so its M10 axle carries about 89 MPa at 2.5 g; a cantilevered stub axle, as at TRL 2, would reach 472 MPa. The hip bar uprights (30 x 30 x 1.5 mm sleeves) carry a 400 N push shared between them at 616 mm above the rails: 123 N·m and 80 MPa each, a factor of 2.9.

## 8. Turning and stability

With the casters trailing tangentially and the 2.4 in tires, a turn about the inner rear wheel sweeps a circle of 3.66 m, and a spin about the rear axle centre (one rear wheel rolling backward) sweeps 3.41 m. R5 is met. The swept front tire clears the risers and rails by 19.5 mm at any steer angle (`cad/src/model.py --check`).

The static side tip angle, loaded, is 47 degrees (half track 385 mm, centre of mass 365 mm). The static tip angles over the front and rear axles are 66 and 63 degrees. These are static angles; a wheel dropping into a rut on a cross-slope still needs a dynamic check in the field.

## 9. Water delivered and cost

A household using 100 L per day needs 5 head-carried trips or 2 WaterWalker trips (1.25 rounded up). On a 3 km round trip at 4 km/h that is 3.75 h against 1.50 h of walking, if walking speed is similar; sandy routes are slower.

Value-engineering target: USD 450. Estimated cost of the constructable design: USD 492 (USD 42 over the target). This is the first prototype without assist and with mounting points (`budget_usd`, a hypothetical control target, not a limit). Making the design constructable added USD 36: four headset and steering lock sets (BOM line 16), the cradle carrier and second rear brackets, cradle brackets, guard clips and fixings. The decisions of 2026-10-02 added USD 30: the hold-to-release brake (BOM line 17, USD 30) less the splitter it replaces (line 7, USD 4), the second torque-arm tab and the spring unit tab (line 1, USD 1) and two rating plates (line 12, USD 3). The assist prototype has its own value-engineering target of USD 450; its two-motor kit (two hub motors, the push sensor and the class V1 receiver) is estimated at USD 450.00, on the target. The SwapCell pack is priced once in the SwapCell BOM and excluded here. Cost drivers and savings worth trying are in WWK-DEC-001.

## 10. Results against every requirement

Status rule: **met** means the value is within 95 % of the limit; **at risk** means within the limit but with less than 5 % margin, or dependent on an unverified assumption; **not met** means past the limit. R11 is reported against the value-engineering target.

*Table 5. Requirement results (WWK-REQ-001 v0.7).*

| ID | Target | Value | Status |
| --- | --- | --- | --- |
| R1 | 80 L in four jerrycans or 40 L in two clay pots; payload 90 kg or less | 84.4 kg with jerrycans, 56 kg with pots; spare length 48 mm (jerrycans), 12 mm (pots) | At risk (pot size) |
| R2 | 60 N or less, firm level path | 24.5 to 61.2 N | **Not met** (by 1.2 N; accepted on paper 2026-10-02) |
| R3 | 150 N or less, loose sand (with assist if fitted) | 241 to 367 N unassisted; 140 to 274 N with one motor; 20 to 154 N with the two-motor kit | **Not met** (first prototype has no assist; two-motor kit 4 N short on the loosest sand) |
| R4 | 180 N or less on a 10 % climb; controlled descent | 146.0 to 182.6 N climb; 72 N at the lever to hold on the descent; the hold-to-release brake alone holds up to 12 % if the user lets go | **Not met** (climb, by 2.6 N; accepted on paper 2026-10-02) |
| R5 | 4.0 m turning circle or less | 3.66 m about the inner rear wheel; 3.41 m spin | Met |
| R6 | 900 mm wide or less | 898 mm over the axle nuts; the lock pin ends inside them | At risk |
| R7 | No step-over; walking width 600 mm or more; hip bar 850 to 1,050 mm; skirt guards | 0 mm; 610 mm; 850 to 1,050 mm with 150 mm of post in the sleeve at full height; guards on both rear wheels | At risk (walking width margin 10 mm) |
| R8 | Lift 450 mm or less, from either side | 364 mm | Met |
| R9 | Empty 35 kg or less (42 kg with assist) | 40.3 kg (49.6 kg with the two-motor kit) | **Not met** |
| R10 | Service brake while walking; park rated gross mass on 20 % | Lever on the grip and a hold-to-release brake (squeeze 98 N, hold 24 N); positive lock pin held at both ends for parking (latch 192 N for short stops); tire friction 0.41 needed | At risk |
| R11 | First prototype (no assist, with mounting points): value-engineering target USD 450 | USD 492 | Over the target by USD 42 |
| R12 | Wear parts are standard 26 in bicycle parts | 26 in rims, tires, tubes, spokes, cables, 1 1/8 in headsets; 100 mm drum hubs are less common than rim-brake hubs in rural markets | At risk |
| R13 | Assist-ready to SwapCell interface v0.3 | Receiver plate, torque-arm tabs on both rear forks and sensor tab in the model; 7.8 A peak against the 15 A legacy limit; latch class V1 retention needs a test | Not verifiable at TRL 3 |

Summary: 2 met, 5 at risk, 4 not met (R2, R3, R4, R9), R11 over the value-engineering target, 1 not verifiable at TRL 3. No status changed from v0.3. In v0.2: 3 met, 7 at risk, 2 not met (R3, R9).

## 11. Corrections to earlier figures

The TRL 2 figures in WWK-PRC-001 v0.2 were checked against this script and corrected in v0.3 of the precis: empty mass 31 kg to 40.8 kg (47.3 kg with assist); loaded mass 115 kg to 125.2 kg; firm push force 25 to 55 N to 24.6 to 61.4 N; sand push force 225 to 340 N to 242 to 368 N; 10 % climb 135 to 170 N to 146.7 to 183.4 N; hold-back on the descent 55 to 90 N to 61 to 98 N; parking force 250 N to 253 N; turning circle 3.8 m to 3.66 m; width 860 mm to 898 mm; walking width 660 mm to 610 mm; lift height 350 mm to 364 mm; side tip angle 45 degrees to 47 degrees; parts cost about USD 300 to USD 430; assist energy 70 Wh/km to 83 Wh/km; and the assist pack is 46.8 V (SwapCell 13S), not 36 V.

Version 0.2 (WWK-DDR-002) then changed: empty mass 40.8 kg to 37.4 kg; loaded mass 125.2 kg to 121.8 kg; firm push force 61.4 N to 59.7 N; 10 % climb 183.4 N to 178.3 N; sand 242 to 368 N to 236 to 358 N; caster arm stress 112 MPa to 133 MPa; weld stress range 63 MPa to 75 MPa; parts cost USD 430 to USD 426.

Version 0.3 (WWK-DDR-003, constructable design) changed: empty mass 37.4 kg to 39.6 kg; loaded mass 121.8 kg to 124.0 kg; firm push force 59.7 N to 60.8 N; 10 % climb 178.3 N to 181.5 N; sand 236 to 358 N to 240 to 365 N; the rail is carried on the hip sleeve and the cradle hangs from the cross members, so the caster arm stress is 129 MPa and the weld stress range 61 MPa; parts cost USD 426 to USD 462.

Version 0.4 (decisions of 2026-10-02) changed: empty mass 39.6 kg to 40.3 kg; loaded mass 124.0 kg to 124.7 kg; firm push force 60.8 N to 61.2 N; 10 % climb 181.5 N to 182.6 N; sand 240 to 365 N to 241 to 367 N; the assist kit is two motors (9.35 kg, USD 450) instead of one (6.50 kg, USD 260), so the assisted mass is 49.6 kg empty and 134.0 kg loaded and the two-motor sand push 154 N, not 144 N; lock pin factor 2.0 to 1.9; hip sleeve factor 1.9 to 1.8; parts cost USD 462 to USD 492.

> **Safety:** These are paper calculations. The brake, parking and frame figures depend on assumed drum ratios, tire friction and a 2.5 g dynamic factor, none of which has been measured. Nothing in this note makes the carrier safe to build or load. TRL 4 testing is on hold by Amish's instruction.
