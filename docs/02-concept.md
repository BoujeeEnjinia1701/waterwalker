---
doc_id: WWK-PRC-001
title: WaterWalker design precis
project: WaterWalker
doc_type: Design precis
version: "0.7"
status: Draft
date: '2026-10-02'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-24'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-09-24'
  author: Amish Chadha
  change: Populate to TRL 2 (architecture, first-order numbers, design choices, safety, media)
- version: "0.3"
  date: '2026-09-25'
  author: Amish Chadha
  change: TRL 3. Record Amish's decisions (WWK-DDR-001); numbers replaced with checked values from WWK-CAL-001; rear wheels in fixed forks, risers moved clear of the caster sweep, main tube upsized; assist mounting points to SwapCell interface v0.3; general arrangement WWK-DWG-001
- version: "0.4"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); 1.2 mm main-tube wall, thinner cradle and parking lock pin; numbers from WWK-CAL-001 v0.2; WWK-DWG-001 Rev P2
- version: "0.5"
  date: '2026-10-02'
  author: Amish Chadha
  change: Design made constructable (WWK-DDR-003); build plan WWK-BLD-001 and design decisions register WWK-DEC-001; numbers from WWK-CAL-001 v0.3; WWK-DWG-001 Rev P3; budget as a value-engineering target
- version: "0.6"
  date: '2026-10-02'
  author: Amish Chadha
  change: Dead-man brake, assist target and partner from Amish's decisions of 2026-10-02 (WWK-DEC-001)
- version: "0.7"
  date: '2026-10-02'
  author: Amish Chadha
  change: Decisions of 2026-10-02 carried into the design; hold-to-release brake (item 17) and two-motor assist mounting described; numbers from WWK-CAL-001 v0.4; WWK-DWG-001 Rev P4
---

# WaterWalker design precis

WaterWalker is a four-wheel water carrier that the user walks inside and pushes, like a rollator. Four 20 L jerrycans, or two 20 L clay pots, ride low in a padded cradle between the axles, so one trip carries up to 80 L, four times a head load, with no weight on the head or spine. The TRL 3 calculations (WWK-CAL-001 v0.4) show that the carrier turns in 3.7 m and needs about 24 to 61 N on firm ground, but it is heavier than estimated at TRL 2 (40.3 kg empty against a 35 kg target) and loose sand takes about 241 to 367 N, far above the 150 N target. Amish decided on 2026-09-25 to build the first prototype without assist but with mounting points for it, and later that day accepted the remaining recommendations (WWK-DDR-002): a lighter main tube and cradle and a positive parking lock pin. On 2026-10-02 the design was made constructable (WWK-DDR-003, accepted by Amish the same day), adding a cradle carrier, two-level rear head tube brackets, headsets and steering locks and the fixings the concept lacked; Amish's decisions of that day added a hold-to-release brake, a torque-arm tab on each rear fork for a two-motor assist kit, rating plates and cradle hand holds. The build plan (WWK-BLD-001) shows how to make it. Value-engineering target: USD 450. Estimated cost of the constructable design: USD 492 (USD 42 over the target). All numbers are paper estimates that co-design with the intended users must test (WWK-PRB-001).

![Hero render](../media/hero.png)

*Figure 1. First prototype with four jerrycans, no assist fitted, beside a 1.75 m person.*

## How it works

1. **Walk in.** The frame is open at the rear. The user steps in between the rear wheels with no step-over and stands behind a padded hip bar, with a hand grip on each side, as in a rollator. Skirt guards sit between the user and the spokes of both rear wheels.
2. **Load.** Four 20 L jerrycans (or two clay pots) are lifted from the side, over a side rail at 364 mm, into a low padded cradle between the rear and front wheels.
3. **Push.** The user walks normally and pushes through the hip bar and grips. There is no pedalling, balancing or treadmill, so it works on slopes, in long skirts and for any walking user.
4. **Steer.** The rear wheels are fixed in rigid bicycle forks. The front wheels are on full-swivel caster forks, so the carrier follows the hip bar and turns about the user. The casters can be pinned straight for sand, cross-slopes and descents.
5. **Brake and park.** Drum brakes in both rear hubs are worked from a lever on the right grip, which has a latch for short stops. To park, the user pushes a lock pin from the walking space through tabs on both blades of the left rear fork and between the spokes, so the wheel cannot turn.
6. **Assist (later, optional).** The first prototype has mounting points but no assist. A later kit adds hub motors in the rear wheels (two are needed to meet R3 on the loosest sand; the kit's value-engineering target is set for two), powered by a removable SwapCell pack built to SwapCell interface v0.3, and gives thrust only while a sensor in the hip bar mount feels the user pushing, so the carrier never moves on its own.

![Water delivered per trip and per day](../media/flow.png)

*Figure 2. Water delivered per trip and per day (estimates, WWK-CAL-001).*

## Main components

Item numbers match `bom/bom.csv`, the exploded view (Figure 3) and drawing WWK-DWG-001.

*Table 1. Main components.*

| # | Component | Choice | Notes |
| --- | --- | --- | --- |
| 1 | Frame | Mild steel: 40 x 30 x 1.2 mm rectangular tube for the side rails, front risers, caster arms and front cross members (wall decided 2026-09-25, WWK-DDR-002); 25 x 25 x 1.5 mm for the rear cross member, the two-level rear head tube brackets and the cradle bearers; 20 x 20 x 1.5 mm cradle hangers (WWK-DDR-003); 30 x 30 x 1.5 mm hip bar sleeves; welded | Open rear for walk-in entry; repairable by a local welder. Carries the assist mounting points: a receiver plate on the upper cross member, a torque-arm tab on each rear fork and a sensor tab on the right hip bar sleeve; a tab on the left hip bar sleeve carries the hold-to-release spring unit |
| 2 | Rear wheels (2) | 26 x 2.1 to 2.4 in wheels with 100 mm front-type drum-brake hubs, in rigid bicycle forks on headsets, pinned straight (item 16) | Wheel size decided 2026-09-25. Forks replace the TRL 2 stub axles (decided, WWK-DDR-001 item 9, WWK-DDR-002) |
| 3 | Front wheels (2) | 26 in wheels in rigid bicycle forks turned into caster forks, 60 mm trail, on headsets with a drop-pin swivel lock (item 16) | Full swivel, decided 2026-09-25 |
| 4 | Hip bar and hand grips | Padded steel bar on telescopic posts, 850 to 1,050 mm, rear-facing grips | Push through the hips as well as the hands; grip position and spacing are asked of users at the first co-design session |
| 5 | Cradle | Tray 780 x 430 mm: 6 mm plywood floor, 4 mm plywood walls 160 mm high, 2 mm rubber pad from used tires, straps and removable dividers, two 90 x 26 mm hand holds in each side wall | Four jerrycans 2 x 2, or two clay pots in line (decided 2026-09-25); thinner cradle decided 2026-09-25 (WWK-DDR-002) |
| 6 | Containers | The user's own 20 L jerrycans (four) | Shown for scale; not purchased |
| 7 | Brakes | Drum brakes in both rear hubs, one lever with a parking latch on the right grip; its cable runs along the front of the hip bar to the cable yoke in item 17 | Decided 2026-09-25; cable route 2026-10-02 |
| 8 | Skirt guards (2) | 3 mm HDPE panels between the inner fork blade and the spokes | Keep skirts, wraps and hands out of the spokes |
| 9 | Hub motors (optional, later, 2) | Two 250 W, 48 V geared front-type hub motors (100 mm) in 26 in rims, one in each rear wheel, each with a controller, torque arm and disc brake | Not in the first prototype; two-motor kit decided 2026-10-02 |
| 10 | Battery (optional, later) | SwapCell pack, interface v0.3 (13S2P, 46.8 V, about 450 Wh, 2.85 kg) | Priced once in the SwapCell BOM, excluded here |
| 11 | Push sensor and controller (optional, later) | 50 kg load cell in the hip bar mount, amplifier, microcontroller, brake cut-off | Motor runs only while the user pushes |
| 12 | Hardware and consumables | Bolts, axle nuts, paint, reflectors; two rated load and slope plates, on the outside of the right rail and the inside of the left rail | Plates modelled (decided 2026-10-02); fixings not modelled |
| 13 | SwapCell receiver (optional, later) | Vehicle receiver to latch class V1 with a 10 kΩ INTERLOCK coding resistor | Bolts to the item 1 receiver plate |
| 14 | Tires, tubes and liners (4 sets) | 26 x 2.1 to 2.4 in puncture-resistant tires, thorn-resistant tubes, liners | Not modelled separately; puncture protection kept (WWK-DDR-002) |
| 15 | Parking lock pin | 10 mm ball-lock pin with pull ring and lanyard, through tabs welded to the inner and outer blades of the left rear fork; passes through a hole in the left skirt guard and through the spokes | Decided 2026-09-25 (WWK-DDR-002); held at both ends (WWK-DDR-003); nothing projects beyond the axle nuts |
| 16 | Headset and steering lock sets (4) | 1 1/8 in external-cup headsets; a clamp collar with a lock plate on each steerer; an 8 mm pin into a guide on the frame | Added for construction (WWK-DDR-003) |
| 17 | Hold-to-release brake | A bail under the left grip; a spring unit (a 26 mm tube with a 390 N spring, a toggle and a cable yoke) on the left hip bar sleeve; cables to both rear drums | Decided 2026-10-02 (WWK-DEC-001); let go of the bail and the spring applies both rear brakes |

![Exploded view](../media/exploded.png)

*Figure 3. Exploded view with BOM callouts; the optional assist kit (items 9 to 11 and 13) is shown for its mounting points.*

The general arrangement is drawing WWK-DWG-001 Rev P4 (`cad/drawings/WWK-DWG-001.pdf`), generated from the parametric model `cad/src/model.py`. STEP files of the first prototype, the frame, the assist kit and the full assembly are in `cad/step/`.

## Assist mounting points and SwapCell interface v0.3

The first prototype carries mounting points so that a later assist kit bolts on without re-welding the frame (R13):

- **Pack receiver.** A 140 x 300 x 3 mm plate on the upper front cross member, about 835 mm above the ground and clear of the caster sweep, takes a SwapCell vehicle receiver built to latch class V1 (interface v0.3 item V: no release and no contact interruption under the UN 38.3 T3 vibration profile, 330 N preload through an over-centre lever). The pack lies across the carrier with its back and lid faces open to air, as the interface asks for vehicle mounts.
- **Wake without CAN.** The receiver fits the 10 kΩ INTERLOCK coding resistor (item W), which wakes the pack with no supply from the host. A simple assist controller without CAN then gets the pack's legacy discharge-only output (15 A limit); the two-motor assist needs at most about 7.8 A. A CAN controller may send the host heartbeat instead.
- **No charging on the carrier.** WaterWalker does not use the charge-while-discharging mode (item C); the pack is charged in a SwapCell dock.
- **Motors and sensor.** Both rear forks' 100 mm dropouts accept a front-type geared hub motor, and each rear fork carries a torque-arm tab welded behind its outer blade, 60 mm above the axle, so the two-motor kit bolts on (decided 2026-10-02). The motor wheels replace the drum-hub wheels, so the hold-to-release brake's yoke cables go to the motors' disc brakes, and the bail also works the controllers' brake cut-off. A tab on the right hip bar sleeve takes the push sensor. Value-engineering target for the assist prototype: USD 450. Estimated cost of the two-motor kit: USD 450 (on the target), pack excluded.

## Checked numbers

All values are from WWK-CAL-001 v0.4 and were checked against `docs/04-calcs/sizing.py`.

Assumptions: four 20 L jerrycans (84.4 kg with the cans); empty mass 40.3 kg from the mass roll-up of the model; loaded mass 124.7 kg (134.0 kg with the two-motor assist kit); g = 9.81 m/s²; rolling resistance coefficient 0.02 to 0.05 on firm dirt, and 0.197 to 0.300 on loose sand from a sinkage of 25 to 55 mm; one 250 W geared hub motor gives 40 N·m (120 N of thrust); walking at 1.0 m/s on firm ground and 0.6 m/s on sand.

*Table 2. Checked numbers against the requirements.*

| Quantity | Value | Requirement and status |
| --- | --- | --- |
| Water per trip | 80 L (four jerrycans) or 40 L (two clay pots, 12 mm spare length) | R1 at risk (pot size) |
| Push force, firm level path | 24.5 to 61.2 N | R2 (60 N) **not met** (by 1.2 N; accepted on paper) |
| Push force, loose sand, unassisted | 241 to 367 N | R3 (150 N) **not met** |
| Push force, loose sand, one or two motors (later) | 140 to 274 N (one); 20 to 154 N (two) | R3 needs two motors of about 41 N·m each |
| Push force, 10 % climb, firm | 146.0 to 182.6 N | R4 (180 N) **not met** (by 2.6 N; accepted on paper) |
| Hold-back force, 10 % descent | 61 to 97 N; about 72 N at the brake lever | R4 descent met on paper |
| Hold-to-release brake | 390 N spring; holds the loaded carrier with assist on up to 12 % if let go, stopping in about 2.6 m from 1.0 m/s on 10 %; squeeze 98 N, hold 24 N (estimate) | R10 at risk |
| Parking on 20 % | 258 N at the tires; lock pin (no hand force), or 192 N at the lever latch; tire friction 0.41 needed | R10 at risk |
| Turning circle | 3.66 m about the inner rear wheel | R5 met |
| Overall size | 898 mm wide, 2.2 m long | R6 at risk (2 mm margin) |
| Walk-in fit | 0 mm step-over; 610 mm clear walking width; hip bar 850 to 1,050 mm | R7 at risk (10 mm margin) |
| Container lift height | 364 mm over the side rail | R8 met |
| Side tip angle, loaded | 47 degrees | Static only |
| Empty mass | 40.3 kg (49.6 kg with the two-motor assist kit) | R9 **not met** (5.3 kg over) |
| Frame stress at 2.5 g | 129 MPa at the caster arm root; factor 1.82 on yield; rear brackets factor 2.4 when parked | Weld stress range 61 MPa, below the 71 MPa reference |
| Assist energy (later) | 170 Wh/km (two motors) on loose sand; 2.7 km per SwapCell pack | R13 not verifiable at TRL 3 |
| Parts cost | USD 492 first prototype; two-motor assist kit USD 450 more, pack excluded | R11 over the USD 450 value-engineering target by USD 42; assist kit on its USD 450 target |

### Comparison with head carrying

For a household of five using about 100 L per day, on a 3 km round trip (estimates):

*Table 3. Head carrying and WaterWalker.*

| | Head carrying | WaterWalker |
| --- | --- | --- |
| Water per trip | 20 L | 80 L |
| Trips per day for 100 L | 5 | 2 (1.25 rounded up) |
| Trips saved per day | | 3 |
| Walking time per day at 4 km/h | about 3.75 h | about 1.5 h, if walking speed is similar |
| Load on head and spine | about 20 kg | none; about 24 to 61 N push on firm ground |

The time saving shrinks on sandy routes, where walking is slower and the push force is high, and it does not include queueing and filling time at the water point, which the carrier does not change.

## Key design choices

Items 1 to 6 were decided by Amish on 2026-09-25: go with recommendation (WWK-DDR-001). Items 7 to 10 came out of the TRL 3 calculations and were decided by Amish later on 2026-09-25: go with recommendation (WWK-DDR-002).

1. **Wheel size (decided).** 26 x 2.1 to 2.4 in all round, for sand performance, one spare tire size and wide availability in rural markets. WWK-CAL-001 shows that no practical tire width brings the sand push force down to 150 N; even 4 in fat-bike tires leave 177 to 269 N.
2. **No assist in the first prototype (decided).** The first prototype has mounting points for a later assist kit; the USD 450 value-engineering target covers exactly that. The later kit needs two hub motors, not one, to meet R3 on the loosest sand. The value-engineering target for that assist prototype is about USD 450 for the two-motor kit, with the shared SwapCell pack counted separately (decided by Amish, 2026-10-02, WWK-DEC-001).
3. **Steering (decided).** Full-swivel lockable front casters.
4. **User position (decided).** Between the rear wheels.
5. **Cradle (decided).** Four jerrycans or two clay pots, until co-design shows how often pots are used.
6. **Brakes (decided).** Drum brakes in both rear hubs with a parking latch. A hold-to-release (dead-man) brake is fitted on the first prototype: a spring applies both drums unless the user holds a bail on the grips (decided by Amish, 2026-10-02, WWK-DEC-001); users are asked about it in co-design.
7. **Rear wheels in fixed forks (decided).** A cantilevered M10 axle is overstressed (about 459 MPa at 2.5 g); a fixed rigid fork holds it on both sides (about 86 MPa). This needs 100 mm front-type drum hubs at the rear and a 770 mm track.
8. **Risers clear of the caster sweep (decided).** Risers at x = 1,150 mm, wheelbase 1,530 mm, cradle 780 mm long.
9. **Main tube 40 x 30 mm (decided).** The TRL 2 section had a yield factor of only 1.45 at the caster arm root. The wall is 1.2 mm under item 10, which gives a factor of 1.77.
10. **Mass and parking (decided).** The thinner cradle and the 1.2 mm main-tube wall are applied (empty mass 40.8 to 37.4 kg), puncture protection is kept, and R9 is to be revisited with users in co-design. A positive lock pin is added for parking, with the lever latch kept for short stops. See WWK-DDR-001 items 12 and 13 and WWK-DDR-002.
11. **Design for construction (made and accepted 2026-10-02).** The concept's parts were made buildable without changing what the carrier does: the cradle rests on two bearers hung from the cross members, each rear head tube is held by two brackets 60 mm behind the axle, all four forks run in headsets with lock collars and pins, the caster arms leave directly over the risers, and the guards, lock pin, brake arms and cradle have real fixings (WWK-DDR-003). The empty mass rose to 39.6 kg (40.3 kg with the decisions of 2026-10-02 carried in); Amish accepted the changes on 2026-10-02 (WWK-DEC-001). The build plan is WWK-BLD-001.

## Safety

> **Safety:** A loaded WaterWalker has a mass of about 125 kg (134 kg with the assist kit). On a 10 % slope it pulls downhill with about 61 to 97 N more than rolling resistance absorbs. Rated load and slope limits are marked on two plates on the frame, and the parking brake must hold a full load on the steepest rated slope. Parked facing downhill on a 20 % grade, the rear tires need a friction coefficient of about 0.41, which loose gravel or sand may not give.

- **Runaway on slopes.** If the user trips or lets go on a descent, the carrier rolls away. Mitigations: service brake on a grip, parking latch, a positive lock pin (decided, WWK-DDR-002), casters pinned straight on descents, and a hold-to-release (dead-man) brake: a spring applies both rear drums unless the user holds the bail under the left grip (decided 2026-10-02, BOM item 17). On paper the spring alone holds the loaded carrier on up to 12 % but not on 20 %, so the latch and lock pin stay the parking brakes, and the brake is tested before the first loaded descent. A wrist tether is an option to test in co-design.
- **Brakes.** The paper sizing needs about 192 N at the lever to set the parking latch on 20 %, which many users cannot give; the lock pin is for parking. The pin must be pulled before moving off, and it loads the spokes sideways, which needs a test. Sand and water in rim brakes are the main reason for choosing drums.
- **Tipping.** The low cradle gives a static side tip angle of about 47 degrees, but a wheel dropping into a rut or ditch on a cross-slope can still tip the carrier. Containers must be strapped so the load cannot shift. Do not carry children or people in the cradle.
- **Pinch and entanglement points.** Spokes, caster forks, the 400 mm caster sweep and brake levers can catch skirts, wraps, fingers and children's hands. Skirt guards cover the rear spokes. Caster swivel zones must be kept clear of feet and marked, and the hip bar telescopic joints must not pinch.
- **Structure.** The frame is sized for 2.5 g with a factor of about 1.8 on yield with the 1.2 mm wall. With the cradle hung from the cross members (WWK-DDR-003) the weld stress range in the rail is 61 MPa, below the 71 MPa reference for a typical fillet weld, but fatigue cracking on rough paths is still possible and only a test can confirm the life. The tabs welded to the steel rear forks must be welded with care and inspected, and the rear cross member and caster arm welds are inspected at every service until the TRL 4 fatigue test (decided 2026-10-02).
- **Lifting.** Lifting 20 kg to 364 mm is far safer than lifting to head height, but containers should be filled in place where possible and loaded from the side with a straight back. The empty carrier (about 40 kg) is a two-person lift over steps and ditches.
- **Lithium battery (later assist only).** The SwapCell pack has a battery management system, cell-level protection and a fuse (SwapCell interface v0.3). On the carrier it must sit in a latch class V1 receiver, be protected from water and sand while leaving its back and lid faces open to air, and never be charged if damaged or swollen. Charging is in a SwapCell dock on a non-combustible surface away from sleeping areas. The motor must run only while the push sensor detects the user pushing, with a hard cut-off when the brake lever is pulled or the bail is let go.
- **Single-sided drive (later assist only).** One hub motor makes a 46 N·m yaw moment, which is why the assist kit has two motors. If only one is ever run, the casters must be locked straight.

## Open questions

- Confirm rolling resistance and sinkage in loose sand on the users' routes; WWK-CAL-001 uses an assumed 25 to 55 mm.
- Confirm the sustained push force limits with the intended users, including girls and older women; R2 and R4 now miss by only 1.2 N and 2.6 N.
- Can a geared hub motor deliver about 40 N·m at 17 to 29 rpm without overheating? At 40 % efficiency each motor makes about 110 W of heat on sand.
- Are 100 mm front-type drum hubs sold and serviced in the first region's markets (R12)?
- Decide how often clay pots are used and their real diameter; the cradle fits two pots of up to about 384 mm.
- Approach the first partner for co-design through the Helpful Engineering network, with Kitui County, Kenya, as the first candidate region (decided by Amish, 2026-10-02, WWK-DEC-001).

Concept media: [blueprint sheet](../media/concept-blueprint.pdf), [interactive 3D model](../media/viewer.html).
