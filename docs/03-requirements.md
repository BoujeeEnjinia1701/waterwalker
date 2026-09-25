---
doc_id: WWK-REQ-001
title: WaterWalker requirements
project: WaterWalker
doc_type: Requirements
version: "0.2"
status: Draft
date: '2026-09-24'
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
---

# WaterWalker requirements

These are first-pass requirements for the concept. Targets are desk proposals for review and must be revised from co-design sessions with the intended users (WWK-PRB-001) before the design is frozen. They will be checked by calculation at TRL 3. Concept estimates against each target are in WWK-PRC-001.

| ID | Requirement | Target | Verification (TRL 3 or later) |
| --- | --- | --- | --- |
| R1 | Carry a household's water in one trip | 80 L of water in four 20 L jerrycans; rated gross payload 90 kg including containers; also accept 20 L clay pots | Cradle layout in the parametric model; later load test |
| R2 | Easy to push on firm ground | Sustained push force 60 N or less at rated load on a firm, level dirt path | Rolling resistance calculation; later force gauge on a field path |
| R3 | Usable on loose sand | Sustained push force 150 N or less at rated load on loose sand, with assist if fitted | Calculation from sinkage and rolling resistance; later field test |
| R4 | Climb and descend slopes | Climb a 10 % grade on firm ground with a push force of 180 N or less for up to 100 m; descend a 10 % grade under control with the service brake | Force calculation; brake sizing |
| R5 | Turn without lifting | 180 degree turn within a 4.0 m diameter circle without lifting or skidding a wheel; reverse by pulling back | Geometry of the parametric model |
| R6 | Fit narrow paths and gates | Overall width 900 mm or less | Parametric model |
| R7 | Walk-in fit for all users | No step-over at the rear entry (50 mm or less); clear walking width 600 mm or more; hip bar height adjustable 850 to 1,050 mm; skirt guards on both rear wheels | Parametric model; later co-design fitting sessions |
| R8 | Easy loading | Containers lifted no higher than 450 mm above the ground; loadable from either side without removing parts | Parametric model |
| R9 | Light enough to handle empty | Empty mass 35 kg or less without assist, 42 kg or less with assist | Mass roll-up from the parametric model |
| R10 | Safe braking and parking | Service brake on both rear wheels operable while walking; parking brake holds the rated gross mass on a 20 % grade | Brake force calculation |
| R11 | Affordable prototype | Parts for one prototype $450 or less (`project.yaml` budget) | Priced BOM |
| R12 | Repairable in a rural market | All wear parts (tires, tubes, spokes, bearings, cables, brake shoes) are standard 26 in bicycle parts; mild steel frame repairable by a local welder; only common hand and bicycle tools needed | Design review of the BOM; later review with a local mechanic |

## Assumptions

- A 20 L jerrycan weighs about 1.1 kg empty and measures about 360 x 175 x 430 mm. A 20 L clay pot is assumed to be about 380 mm in diameter and 5 to 8 kg empty.
- Sustained push forces are set with reference to published manual-handling guidance, which suggests roughly 100 to 150 N for sustained pushing by women over long distances and more for short efforts. The limits must be confirmed with the users, including girls and older women.
- A household of five uses about 100 L per day (about 20 L per person).
- R5 allows a larger circle than a compact rollator because the concept needs a long wheelbase to keep the swivelling front wheels clear of the cradle (WWK-PRC-001). A three-point turn is expected on paths narrower than 4 m.
