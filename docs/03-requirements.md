---
doc_id: WWK-REQ-001
title: WaterWalker requirements
project: WaterWalker
doc_type: Requirements
version: "0.5"
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
  change: First measurable requirements for TRL 2
- version: "0.3"
  date: '2026-09-25'
  author: Amish Chadha
  change: TRL 3. Record Amish's decisions (WWK-DDR-001); redefine R1 (four jerrycans or two clay pots) and R11 (budget covers the unassisted first prototype with mounting points); add R13 (assist-ready to SwapCell interface v0.3); add status from WWK-CAL-001
- version: "0.4"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); R10 restated for the positive lock pin; status updated from WWK-CAL-001 v0.2
- version: "0.5"
  date: '2026-10-02'
  author: Amish Chadha
  change: Status from WWK-CAL-001 v0.3 for the constructable design (WWK-DDR-003); R11 reported against the value-engineering target
---

# WaterWalker requirements

Four of the thirteen requirements are not met on paper (R2, R3, R4 and R9), five are at risk and two are met, according to WWK-CAL-001 v0.3; R11 is over its value-engineering target and R13 cannot be verified at TRL 3. Targets are still desk proposals and must be revised from co-design sessions with the intended users (WWK-PRB-001) before the design is frozen. On 2026-09-25 Amish decided to build the first prototype without assist but with mounting points, keep the USD 450 figure, and carry four jerrycans or two clay pots (WWK-DDR-001); R1 and R11 were redefined to match, and R13 is new. Later the same day Amish accepted the remaining recommendations (WWK-DDR-002), including a positive parking lock pin, for which R10 is restated. On 2026-10-02 the design was made constructable (WWK-DDR-003, open for Amish's review): the parts added for construction make the carrier 2.2 kg heavier, which moves R2 and R4 from at risk to not met by 0.8 N and 1.5 N. Whether to accept that or recover mass is an open decision in WWK-DEC-001. On 2026-10-01 Amish set budgets as value-engineering targets, so R11 is reported against its target rather than as met or not met.

*Table 1. Requirements and status at TRL 3 (WWK-CAL-001).*

| ID | Requirement | Target | Verification (TRL 3 or later) | Status at TRL 3 |
| --- | --- | --- | --- | --- |
| R1 | Carry a household's water in one trip | 80 L of water in four 20 L jerrycans, or 40 L in two 20 L clay pots; rated gross payload 90 kg including containers (redefined 2026-09-25, WWK-DDR-001) | Cradle layout in the parametric model; later load test | At risk: two 380 mm pots fit with 12 mm to spare |
| R2 | Easy to push on firm ground | Sustained push force 60 N or less at rated load on a firm, level dirt path | Rolling resistance calculation; later force gauge on a field path | **Not met**: 24.3 to 60.8 N (by 0.8 N) |
| R3 | Usable on loose sand | Sustained push force 150 N or less at rated load on loose sand, with assist if fitted | Calculation from sinkage and rolling resistance; later field test | **Not met**: 240 to 365 N (no assist on the first prototype) |
| R4 | Climb and descend slopes | Climb a 10 % grade on firm ground with a push force of 180 N or less for up to 100 m; descend a 10 % grade under control with the service brake | Force calculation; brake sizing | **Not met**: 181.5 N at the rough end (by 1.5 N); descent met on paper |
| R5 | Turn without lifting | 180 degree turn within a 4.0 m diameter circle without lifting or skidding a wheel; reverse by pulling back | Geometry of the parametric model | Met: 3.66 m |
| R6 | Fit narrow paths and gates | Overall width 900 mm or less | Parametric model | At risk: 898 mm |
| R7 | Walk-in fit for all users | No step-over at the rear entry (50 mm or less); clear walking width 600 mm or more; hip bar height adjustable 850 to 1,050 mm; skirt guards on both rear wheels | Parametric model; later co-design fitting sessions | At risk: walking width 610 mm |
| R8 | Easy loading | Containers lifted no higher than 450 mm above the ground; loadable from either side without removing parts | Parametric model | Met: 364 mm |
| R9 | Light enough to handle empty | Empty mass 35 kg or less without assist, 42 kg or less with assist | Mass roll-up from the parametric model | **Not met**: 39.6 kg (46.1 kg); to be revisited with users in co-design (WWK-DDR-002) |
| R10 | Safe braking and parking | Service brake on both rear wheels operable while walking; a positive parking lock (lock pin through a rear wheel) that needs no sustained hand force holds the rated gross mass on a 20 % grade; the lever latch serves short stops (restated 2026-09-25, WWK-DDR-002) | Brake force calculation; later parking test | At risk: lock pin held at both ends; tire friction 0.41 needed; latch 187 N |
| R11 | Affordable first prototype | Parts for the first prototype, without assist and with assist mounting points, against a value-engineering target of USD 450 (`project.yaml` budget, kept 2026-09-25; a hypothetical control target, not a limit, 2026-10-01). The budget excludes the optional assist kit, which is a later second prototype, and the SwapCell pack, which is priced once in the SwapCell BOM (redefined 2026-09-25, WWK-DDR-001) | Priced BOM | Over the target by USD 12: USD 462 |
| R12 | Repairable in a rural market | All wear parts (tires, tubes, spokes, bearings, cables, brake shoes) are standard 26 in bicycle parts; mild steel frame repairable by a local welder; only common hand and bicycle tools needed | Design review of the BOM; later review with a local mechanic | At risk: 100 mm drum hubs are less common than rim-brake hubs |
| R13 | Assist-ready (new 2026-09-25) | The first prototype carries mounting points for a later assist kit built to SwapCell interface v0.3: a plate for a latch class V1 vehicle receiver above the tires, with the pack's back and lid faces open to air; rear dropouts that accept a 100 mm hub motor with a torque-arm tab; a boss for a push sensor at the hip bar. The receiver fits a 10 kΩ INTERLOCK coding resistor (item W), and the assist draws no more than the 15 A legacy-mode limit | Parametric model; later latch class V1 test | Not verifiable at TRL 3: geometry present, 7.5 A peak |

## Assumptions

- A 20 L jerrycan weighs about 1.1 kg empty and measures about 360 x 175 x 430 mm. A 20 L clay pot is assumed to be about 380 mm in diameter and 5 to 8 kg empty.
- Sustained push forces are set with reference to published manual-handling guidance, which suggests roughly 100 to 150 N for sustained pushing by women over long distances and more for short efforts. The limits must be confirmed with the users, including girls and older women.
- A household of five uses about 100 L per day (about 20 L per person).
- The first prototype has no assist (WWK-DDR-001), so R3 cannot be met by it; R3 stays as the target for the later assist prototype, which needs about 230 N of thrust (two hub motors) to meet it on the loosest sand (WWK-CAL-001).
- R5 allows a larger circle than a compact rollator because the concept needs a long wheelbase to keep the swivelling front wheels clear of the cradle (WWK-PRC-001). A three-point turn is expected on paths narrower than 4 m.
