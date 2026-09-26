---
doc_id: WWK-REQ-001
title: WaterWalker requirements
project: WaterWalker
doc_type: Requirements
version: "0.4"
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
  change: First measurable requirements for TRL 2
- version: "0.3"
  date: '2026-09-25'
  author: Amish Chadha
  change: TRL 3. Record Amish's decisions (WWK-DDR-001); redefine R1 (four jerrycans or two clay pots) and R11 (budget covers the unassisted first prototype with mounting points); add R13 (assist-ready to SwapCell interface v0.3); add status from WWK-CAL-001
- version: "0.4"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); R10 restated for the positive lock pin; status updated from WWK-CAL-001 v0.2
---

# WaterWalker requirements

Two of the thirteen requirements are not met on paper (R3 and R9), seven are at risk and three are met, according to the TRL 3 calculations in WWK-CAL-001 v0.2. Targets are still desk proposals and must be revised from co-design sessions with the intended users (WWK-PRB-001) before the design is frozen. On 2026-09-25 Amish decided to build the first prototype without assist but with mounting points, keep the $450 budget, and carry four jerrycans or two clay pots (WWK-DDR-001); R1 and R11 are redefined to match, and R13 is new. Later the same day Amish accepted the remaining recommendations (WWK-DDR-002): a 1.2 mm main-tube wall and a thinner cradle, which bring R2 and R4 from not met to at risk and R11 to met, and a positive parking lock pin, for which R10 is restated. R9 stays not met and is to be revisited with users in co-design.

*Table 1. Requirements and status at TRL 3 (WWK-CAL-001).*

| ID | Requirement | Target | Verification (TRL 3 or later) | Status at TRL 3 |
| --- | --- | --- | --- | --- |
| R1 | Carry a household's water in one trip | 80 L of water in four 20 L jerrycans, or 40 L in two 20 L clay pots; rated gross payload 90 kg including containers (redefined 2026-09-25, WWK-DDR-001) | Cradle layout in the parametric model; later load test | At risk: two 380 mm pots fit with 12 mm to spare |
| R2 | Easy to push on firm ground | Sustained push force 60 N or less at rated load on a firm, level dirt path | Rolling resistance calculation; later force gauge on a field path | At risk: 23.9 to 59.7 N |
| R3 | Usable on loose sand | Sustained push force 150 N or less at rated load on loose sand, with assist if fitted | Calculation from sinkage and rolling resistance; later field test | **Not met**: 236 to 358 N (no assist on the first prototype) |
| R4 | Climb and descend slopes | Climb a 10 % grade on firm ground with a push force of 180 N or less for up to 100 m; descend a 10 % grade under control with the service brake | Force calculation; brake sizing | At risk: 178.3 N at the rough end; descent met on paper |
| R5 | Turn without lifting | 180 degree turn within a 4.0 m diameter circle without lifting or skidding a wheel; reverse by pulling back | Geometry of the parametric model | Met: 3.66 m |
| R6 | Fit narrow paths and gates | Overall width 900 mm or less | Parametric model | At risk: 898 mm |
| R7 | Walk-in fit for all users | No step-over at the rear entry (50 mm or less); clear walking width 600 mm or more; hip bar height adjustable 850 to 1,050 mm; skirt guards on both rear wheels | Parametric model; later co-design fitting sessions | At risk: walking width 610 mm |
| R8 | Easy loading | Containers lifted no higher than 450 mm above the ground; loadable from either side without removing parts | Parametric model | Met: 364 mm |
| R9 | Light enough to handle empty | Empty mass 35 kg or less without assist, 42 kg or less with assist | Mass roll-up from the parametric model | **Not met**: 37.4 kg (43.9 kg); to be revisited with users in co-design (WWK-DDR-002) |
| R10 | Safe braking and parking | Service brake on both rear wheels operable while walking; a positive parking lock (lock pin through a rear wheel) that needs no sustained hand force holds the rated gross mass on a 20 % grade; the lever latch serves short stops (restated 2026-09-25, WWK-DDR-002) | Brake force calculation; later parking test | At risk: lock pin fitted; tire friction 0.41 needed; latch 184 N |
| R11 | Affordable first prototype | Parts for the first prototype, without assist and with assist mounting points, $450 or less (`project.yaml` budget, kept 2026-09-25). The budget excludes the optional assist kit, which is a later second prototype, and the SwapCell pack, which is priced once in the SwapCell BOM (redefined 2026-09-25, WWK-DDR-001) | Priced BOM | Met: $426 |
| R12 | Repairable in a rural market | All wear parts (tires, tubes, spokes, bearings, cables, brake shoes) are standard 26 in bicycle parts; mild steel frame repairable by a local welder; only common hand and bicycle tools needed | Design review of the BOM; later review with a local mechanic | At risk: 100 mm drum hubs are less common than rim-brake hubs |
| R13 | Assist-ready (new 2026-09-25) | The first prototype carries mounting points for a later assist kit built to SwapCell interface v0.3: a plate for a latch class V1 vehicle receiver above the tires, with the pack's back and lid faces open to air; rear dropouts that accept a 100 mm hub motor with a torque-arm tab; a boss for a push sensor at the hip bar. The receiver fits a 10 kΩ INTERLOCK coding resistor (item W), and the assist draws no more than the 15 A legacy-mode limit | Parametric model; later latch class V1 test | Not verifiable at TRL 3: geometry present, 7.3 A peak |

## Assumptions

- A 20 L jerrycan weighs about 1.1 kg empty and measures about 360 x 175 x 430 mm. A 20 L clay pot is assumed to be about 380 mm in diameter and 5 to 8 kg empty.
- Sustained push forces are set with reference to published manual-handling guidance, which suggests roughly 100 to 150 N for sustained pushing by women over long distances and more for short efforts. The limits must be confirmed with the users, including girls and older women.
- A household of five uses about 100 L per day (about 20 L per person).
- The first prototype has no assist (WWK-DDR-001), so R3 cannot be met by it; R3 stays as the target for the later assist prototype, which needs about 230 N of thrust (two hub motors) to meet it on the loosest sand (WWK-CAL-001).
- R5 allows a larger circle than a compact rollator because the concept needs a long wheelbase to keep the swivelling front wheels clear of the cradle (WWK-PRC-001). A three-point turn is expected on paths narrower than 4 m.
