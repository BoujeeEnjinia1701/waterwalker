---
doc_id: WWK-PRC-001
title: WaterWalker design precis
project: WaterWalker
doc_type: Design precis
version: "0.3"
status: Draft
date: '2026-09-25'
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
---

# WaterWalker design precis

WaterWalker is a four-wheel water carrier that the user walks inside and pushes, like a rollator. Four 20 L jerrycans, or two 20 L clay pots, ride low in a padded cradle between the axles, so one trip carries up to 80 L, four times a head load, with no weight on the head or spine. The TRL 3 calculations (WWK-CAL-001) show that the carrier is easy to push on firm ground (about 25 to 61 N) and turns in 3.7 m, but it is heavier than estimated at TRL 2 (40.8 kg empty against a 35 kg target), and loose sand takes about 242 to 368 N, far above the 150 N target. Amish decided on 2026-09-25 to build the first prototype without assist but with mounting points for it, within the $450 budget; the priced first prototype is about $430. All numbers are paper estimates that co-design with the intended users must test (WWK-PRB-001).

![Hero render](../media/hero.png)

*Figure 1. First prototype with four jerrycans, no assist fitted, beside a 1.75 m person.*

## How it works

1. **Walk in.** The frame is open at the rear. The user steps in between the rear wheels with no step-over and stands behind a padded hip bar, with a hand grip on each side, as in a rollator. Skirt guards sit between the user and the spokes of both rear wheels.
2. **Load.** Four 20 L jerrycans (or two clay pots) are lifted from the side, over a side rail at 364 mm, into a low padded cradle between the rear and front wheels.
3. **Push.** The user walks normally and pushes through the hip bar and grips. There is no pedalling, balancing or treadmill, so it works on slopes, in long skirts and for any walking user.
4. **Steer.** The rear wheels are fixed in rigid bicycle forks. The front wheels are on full-swivel caster forks, so the carrier follows the hip bar and turns about the user. The casters can be pinned straight for sand, cross-slopes and descents.
5. **Brake and park.** Drum brakes in both rear hubs are worked from a lever on the right grip, which has a latch for parking.
6. **Assist (later, optional).** The first prototype has mounting points but no assist. A later kit adds a hub motor in a rear wheel, powered by a removable SwapCell pack built to SwapCell interface v0.3, and gives thrust only while a sensor in the hip bar mount feels the user pushing, so the carrier never moves on its own.

![Water delivered per trip and per day](../media/flow.png)

*Figure 2. Water delivered per trip and per day (estimates, WWK-CAL-001).*

## Main components

Item numbers match `bom/bom.csv`, the exploded view (Figure 3) and drawing WWK-DWG-001.

*Table 1. Main components.*

| # | Component | Choice | Notes |
| --- | --- | --- | --- |
| 1 | Frame | Mild steel: 40 x 30 x 1.5 mm rectangular tube for the side rails, front risers and caster arms; 25 x 25 x 1.5 mm for cross members and rear fork brackets; 30 x 30 x 1.5 mm hip bar sleeves; welded | Open rear for walk-in entry; repairable by a local welder. Carries the assist mounting points: a receiver plate above the front cross member, a torque-arm tab at the right rear dropout and a sensor boss at the right hip bar sleeve |
| 2 | Rear wheels (2) | 26 x 2.1 to 2.4 in wheels with 100 mm front-type drum-brake hubs, in rigid bicycle forks clamped in fixed head tubes | Wheel size decided 2026-09-25. Forks replace the TRL 2 stub axles (proposed, WWK-DDR-001 item 9) |
| 3 | Front wheels (2) | 26 in wheels in rigid bicycle forks turned into caster forks, 60 mm trail, standard headset bearings, drop-pin swivel lock | Full swivel, decided 2026-09-25 |
| 4 | Hip bar and hand grips | Padded steel bar on telescopic posts, 850 to 1,050 mm, rear-facing grips | Push through the hips as well as the hands |
| 5 | Cradle | Plywood tray 780 x 430 mm, 4 mm rubber pad from used tires, 160 mm walls, straps and removable dividers | Four jerrycans 2 x 2, or two clay pots in line (decided 2026-09-25) |
| 6 | Containers | The user's own 20 L jerrycans (four) | Shown for scale; not purchased |
| 7 | Brakes | Drum brakes in both rear hubs, one lever with a parking latch, cable splitter | Decided 2026-09-25 |
| 8 | Skirt guards (2) | 3 mm HDPE panels between the inner fork blade and the spokes | Keep skirts, wraps and hands out of the spokes |
| 9 | Hub motor (optional, later) | 250 W, 48 V geared front-type hub motor (100 mm) in a 26 in rim, controller, torque arm, disc brake for the motor wheel | Not in the first prototype |
| 10 | Battery (optional, later) | SwapCell pack, interface v0.3 (13S2P, 46.8 V, about 450 Wh, 2.85 kg) | Priced once in the SwapCell BOM, excluded here |
| 11 | Push sensor and controller (optional, later) | 50 kg load cell in the hip bar mount, amplifier, microcontroller, brake cut-off | Motor runs only while the user pushes |
| 12 | Hardware and consumables | Bolts, axle nuts, paint, reflectors | Not modelled |
| 13 | SwapCell receiver (optional, later) | Vehicle receiver to latch class V1 with a 10 kΩ INTERLOCK coding resistor | Bolts to the item 1 receiver plate |
| 14 | Tires, tubes and liners (4 sets) | 26 x 2.1 to 2.4 in puncture-resistant tires, thorn-resistant tubes, liners | Not modelled separately |

![Exploded view](../media/exploded.png)

*Figure 3. Exploded view with BOM callouts; the optional assist kit (items 9 to 11 and 13) is shown for its mounting points.*

The general arrangement is drawing WWK-DWG-001 Rev P1 (`cad/drawings/WWK-DWG-001.pdf`), generated from the parametric model `cad/src/model.py`. STEP files of the first prototype, the frame, the assist kit and the full assembly are in `cad/step/`.

## Assist mounting points and SwapCell interface v0.3

The first prototype carries mounting points so that a later assist kit bolts on without re-welding the frame (R13):

- **Pack receiver.** A 140 x 300 x 3 mm plate on the upper front cross member, about 835 mm above the ground and clear of the caster sweep, takes a SwapCell vehicle receiver built to latch class V1 (interface v0.3 item V: no release and no contact interruption under the UN 38.3 T3 vibration profile, 330 N preload through an over-centre lever). The pack lies across the carrier with its back and lid faces open to air, as the interface asks for vehicle mounts.
- **Wake without CAN.** The receiver fits the 10 kΩ INTERLOCK coding resistor (item W), which wakes the pack with no supply from the host. A simple assist controller without CAN then gets the pack's legacy discharge-only output (15 A limit); the assist needs at most about 7.6 A. A CAN controller may send the host heartbeat instead.
- **No charging on the carrier.** WaterWalker does not use the charge-while-discharging mode (item C); the pack is charged in a SwapCell dock.
- **Motor and sensor.** The right rear fork's 100 mm dropouts accept a front-type geared hub motor, with a torque-arm tab on the dropout. A boss on the right hip bar sleeve takes the push sensor.

## Checked numbers

All values are from WWK-CAL-001 and were checked against `docs/04-calcs/sizing.py`.

Assumptions: four 20 L jerrycans (84.4 kg with the cans); empty mass 40.8 kg from the mass roll-up of the model; loaded mass 125.2 kg (131.7 kg with the assist kit); g = 9.81 m/s²; rolling resistance coefficient 0.02 to 0.05 on firm dirt, and 0.197 to 0.300 on loose sand from a sinkage of 25 to 55 mm; one 250 W geared hub motor gives 40 N·m (120 N of thrust); walking at 1.0 m/s on firm ground and 0.6 m/s on sand.

*Table 2. Checked numbers against the requirements.*

| Quantity | Value | Requirement and status |
| --- | --- | --- |
| Water per trip | 80 L (four jerrycans) or 40 L (two clay pots, 8 mm spare length) | R1 at risk (pot size) |
| Push force, firm level path | 24.6 to 61.4 N | R2 (60 N) **not met** at the rough end |
| Push force, loose sand, unassisted | 242 to 368 N | R3 (150 N) **not met** |
| Push force, loose sand, one or two motors (later) | 135 to 267 N (one); 15 to 148 N (two) | R3 needs two motors |
| Push force, 10 % climb, firm | 146.7 to 183.4 N | R4 (180 N) **not met** at the rough end |
| Hold-back force, 10 % descent | 61 to 98 N; about 73 N at the brake lever | R4 descent met on paper |
| Parking on 20 % | 253 N at the tires; 189 N at the lever latch; tire friction 0.41 needed | R10 at risk |
| Turning circle | 3.66 m about the inner rear wheel | R5 met |
| Overall size | 898 mm wide, 2.2 m long | R6 at risk (2 mm margin) |
| Walk-in fit | 0 mm step-over; 610 mm clear walking width; hip bar 850 to 1,050 mm | R7 at risk (10 mm margin) |
| Container lift height | 364 mm over the side rail | R8 met |
| Side tip angle, loaded | 47 degrees | Static only |
| Empty mass | 40.8 kg (47.3 kg with the assist kit) | R9 **not met** |
| Frame stress at 2.5 g | 112 MPa at the caster arm root; factor 2.09 on yield | Weld fatigue at risk |
| Assist energy (later) | 83 Wh/km (one motor) on sand; 5.4 km per SwapCell pack | R13 not verifiable at TRL 3 |
| Parts cost | $430 first prototype; assist kit $260 more, pack excluded | R11 at risk ($20 margin) |

### Comparison with head carrying

For a household of five using about 100 L per day, on a 3 km round trip (estimates):

*Table 3. Head carrying and WaterWalker.*

| | Head carrying | WaterWalker |
| --- | --- | --- |
| Water per trip | 20 L | 80 L |
| Trips per day for 100 L | 5 | 2 (1.25 rounded up) |
| Trips saved per day | | 3 |
| Walking time per day at 4 km/h | about 3.75 h | about 1.5 h, if walking speed is similar |
| Load on head and spine | about 20 kg | none; about 25 to 61 N push on firm ground |

The time saving shrinks on sandy routes, where walking is slower and the push force is high, and it does not include queueing and filling time at the water point, which the carrier does not change.

## Key design choices

Items 1 to 6 were decided by Amish on 2026-09-25: go with recommendation (WWK-DDR-001). Items 7 to 10 are new, came out of the TRL 3 calculations, and are **proposed, awaiting Amish**; the model already reflects items 7 to 9 because the TRL 2 layout could not be built as drawn.

1. **Wheel size (decided).** 26 x 2.1 to 2.4 in all round, for sand performance, one spare tire size and wide availability in rural markets. WWK-CAL-001 shows that no practical tire width brings the sand push force down to 150 N; even 4 in fat-bike tires leave 182 to 276 N.
2. **No assist in the first prototype (decided).** The first prototype has mounting points for a later assist kit and stays within the $450 budget, which now covers exactly that. The later kit needs two hub motors, not one, to meet R3 on the loosest sand.
3. **Steering (decided).** Full-swivel lockable front casters.
4. **User position (decided).** Between the rear wheels.
5. **Cradle (decided).** Four jerrycans or two clay pots, until co-design shows how often pots are used.
6. **Brakes (decided).** Drum brakes in both rear hubs with a parking latch. Whether users want a dead-man brake is a co-design question.
7. **Rear wheels in fixed forks (proposed).** A cantilevered M10 axle is overstressed (about 472 MPa at 2.5 g); a fixed rigid fork holds it on both sides (about 89 MPa). This needs 100 mm front-type drum hubs at the rear and a 770 mm track.
8. **Risers clear of the caster sweep (proposed).** Risers at x = 1,150 mm, wheelbase 1,530 mm, cradle 780 mm long.
9. **Main tube 40 x 30 x 1.5 mm (proposed).** The TRL 2 section had a yield factor of only 1.41 at the caster arm root.
10. **Mass and parking (proposed).** Apply the thinner cradle and the 1.2 mm main-tube wall; add a positive lock pin for parking. See WWK-DDR-001 items 12 and 13.

## Safety

> **Safety:** A loaded WaterWalker has a mass of about 125 kg (132 kg with the assist kit). On a 10 % slope it pulls downhill with about 61 to 98 N more than rolling resistance absorbs. Rated load and slope limits must be marked on the frame, and the parking brake must hold a full load on the steepest rated slope. Parked facing downhill on a 20 % grade, the rear tires need a friction coefficient of about 0.41, which loose gravel or sand may not give.

- **Runaway on slopes.** If the user trips or lets go on a descent, the carrier rolls away. Mitigations: service brake on a grip, parking latch, a positive lock pin (proposed), casters pinned straight on descents, and a possible dead-man brake (co-design question). A wrist tether is an option to test in co-design.
- **Brakes.** The paper sizing needs about 189 N at the lever to set the parking latch on 20 %, which many users cannot give. Sand and water in rim brakes are the main reason for choosing drums.
- **Tipping.** The low cradle gives a static side tip angle of about 47 degrees, but a wheel dropping into a rut or ditch on a cross-slope can still tip the carrier. Containers must be strapped so the load cannot shift. Do not carry children or people in the cradle.
- **Pinch and entanglement points.** Spokes, caster forks, the 400 mm caster sweep and brake levers can catch skirts, wraps, fingers and children's hands. Skirt guards cover the rear spokes. Caster swivel zones must be kept clear of feet and marked, and the hip bar telescopic joints must not pinch.
- **Structure.** The frame is sized for 2.5 g with a factor of about 2 on yield, but weld fatigue on rough paths is at risk and can only be checked by test.
- **Lifting.** Lifting 20 kg to 364 mm is far safer than lifting to head height, but containers should be filled in place where possible and loaded from the side with a straight back. The empty carrier (about 41 kg) is a two-person lift over steps and ditches.
- **Lithium battery (later assist only).** The SwapCell pack has a battery management system, cell-level protection and a fuse (SwapCell interface v0.3). On the carrier it must sit in a latch class V1 receiver, be protected from water and sand while leaving its back and lid faces open to air, and never be charged if damaged or swollen. Charging is in a SwapCell dock on a non-combustible surface away from sleeping areas. The motor must run only while the push sensor detects the user pushing, with a hard cut-off when the brake lever is pulled.
- **Single-sided drive (later assist only).** One hub motor makes a 46 N·m yaw moment. Casters must be locked straight while one motor runs, or two motors fitted.

## Open questions

- Confirm rolling resistance and sinkage in loose sand on the users' routes; WWK-CAL-001 uses an assumed 25 to 55 mm.
- Confirm the sustained push force limits with the intended users, including girls and older women; R2 and R4 miss by 1.4 N and 3.4 N.
- Can a geared hub motor deliver about 40 N·m at 17 to 29 rpm without overheating? At 40 % efficiency each motor makes about 107 W of heat on sand.
- Are 100 mm front-type drum hubs sold and serviced in the first region's markets (R12)?
- Decide how often clay pots are used and their real diameter; the cradle fits two pots of up to about 384 mm.
- Identify the local partner and region for the first co-design sessions (WWK-PRB-001; open, per area later).

Concept media: [blueprint sheet](../media/concept-blueprint.pdf), [interactive 3D model](../media/viewer.html).
