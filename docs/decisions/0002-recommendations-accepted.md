---
doc_id: WWK-DDR-002
title: WaterWalker recommendations accepted
project: WaterWalker
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-09-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); record the newly decided items, what changed in the repo and the items still open
---

# 0002: Recommendations accepted

- **Date:** 2026-09-25
- **Status:** accepted (items 9 to 13 of WWK-DDR-001); items 7, 8 and 14 remain proposed, awaiting Amish

## Context

WWK-DDR-001 decided the six TRL 2 review items and left seven items open. Five of them (items 9 to 13) came out of the TRL 3 calculations (WWK-CAL-001 v0.1) and each carried a recommendation; the other two (items 7 and 8) had none. The review note (`docs/REVIEW.md`, session 2026-09-25) also listed the budget for the later assist prototype with no recommendation.

On 2026-09-25 Amish wrote: "i accept all your recommendations, go with them across all repos." This record applies that instruction to WaterWalker. Items with a recommendation are now decided; items without one stay open. TRL 4 remains on hold by Amish's instruction, and nothing here goes past TRL 3.

## Decision

Each row in Table 1 is "Decided by Amish, 2026-09-25: go with recommendation".

*Table 1. Newly decided items and what changed in the repo.*

| # | Item | Decision | What changed in the repo |
| --- | --- | --- | --- |
| 9 | Rear wheel mounting | Decided by Amish, 2026-09-25: go with recommendation. Each rear wheel sits in a fixed rigid bicycle fork with 100 mm dropouts and a 100 mm front-type drum hub; track 770 mm | Already in the model and drawing; status changed from proposed to decided in WWK-PRC-001 v0.4 and WWK-CAL-001 v0.2 |
| 10 | Caster arm and front riser position | Decided by Amish, 2026-09-25: go with recommendation. Risers at x = 1,150 mm, wheelbase 1,530 mm, cradle 780 mm long | Already in the model and drawing; status changed to decided |
| 11 | Main frame section | Decided by Amish, 2026-09-25: go with recommendation. 40 x 30 mm rectangular tube for the side rails, front risers and caster arms | Section kept. Its wall is set by item 12 (1.2 mm), which is the later and more specific recommendation on the same member |
| 12 | Mass (R9) | Decided by Amish, 2026-09-25: go with recommendation. Apply the thinner cradle and the 1.2 mm main-tube wall, keep the puncture protection, and revisit R9 with users in co-design | `cad/src/model.py`: main tube 40 x 30 x 1.5 mm to 40 x 30 x 1.2 mm; cradle floor 9 to 6 mm, walls 6 to 4 mm, pad 4 to 2 mm. Empty mass 40.8 to 37.4 kg; loaded 125.2 to 121.8 kg. BOM items 1 ($60 to $55) and 5 ($24 to $20). Revisiting R9 with users waits for co-design (item 7) |
| 13 | Parking brake | Decided by Amish, 2026-09-25: go with recommendation. Add a positive lock pin; keep the lever latch for short stops | New BOM item 15 ($5, 0.10 kg): a 10 mm pin pushed from the walking space through the left skirt guard and the left rear spokes, on a tab welded to the inner fork blade, projecting nothing beyond the axle nuts. Modelled in `cad/src/model.py`; WWK-REQ-001 R10 restated |

### Effect on the numbers (WWK-CAL-001 v0.2)

*Table 2. Before and after.*

| Quantity | v0.1 | v0.2 |
| --- | --- | --- |
| Empty mass (with assist kit) | 40.8 kg (47.3 kg) | 37.4 kg (43.9 kg) |
| Push force, firm level path | 24.6 to 61.4 N | 23.9 to 59.7 N |
| Push force, 10 % climb | 146.7 to 183.4 N | 142.6 to 178.3 N |
| Push force, loose sand | 242 to 368 N | 236 to 358 N |
| Caster arm root stress at 2.5 g | 112 MPa (factor 2.09) | 133 MPa (factor 1.77) |
| Weld stress range at the rear hanger | 63 MPa | 75 MPa, above the 71 MPa detail category |
| Clay pot spare length | 8 mm | 12 mm |
| First-prototype parts | $430 | $426 |

Requirement status changes: R2 and R4 move from not met to at risk; R11 moves from at risk to met ($24 margin); R9 stays not met (2.4 kg over). Summary: 3 met, 7 at risk, 2 not met (R3 and R9), 1 not verifiable at TRL 3.

### Budget

`budget_usd` stays at 450. No recommendation changed the budget figure or what it covers; R11 already covers the unassisted first prototype with mounting points (WWK-DDR-001 item 2).

### Items on hold (TRL 4)

Revisiting R9 with users, and checking weld fatigue and lock pin fit, need co-design sessions, a build or tests. They are decided in direction but on hold, because TRL 4 is on hold by Amish's instruction.

## Items still open

These stay **Proposed, awaiting Amish**, because no recommendation was given.

| # | Item | Status |
| --- | --- | --- |
| 7 | First co-design partner and region | Proposed, awaiting Amish (no recommendation; partners are picked per area later) |
| 8 | Dead-man brake | Proposed, awaiting Amish (no recommendation until users are asked) |
| 14 | Budget for the later assist prototype (kit $260, or about $450 with two motors, plus a shared SwapCell pack) | Proposed, awaiting Amish (no recommendation) |

New finding for Amish, not decided: the thinner main-tube wall raises the weld stress range at the cradle hangers to 75 MPa, above the 71 MPa of a typical fillet-welded detail at 2 million cycles (WWK-CAL-001 v0.2 section 7). Options are gussets at the hanger and caster arm joints, a local 1.5 mm wall at those joints, or accepting the risk until a TRL 4 fatigue test. This is recorded in `docs/REVIEW.md` for Amish and is not applied.

## Consequences

- `cad/src/model.py`, the STEP and STL exports, drawing WWK-DWG-001 (Rev P1 to P2), the concept media, `bom/bom.csv` and WWK-CAL-001 (v0.1 to v0.2) now reflect items 12 and 13.
- WWK-PRC-001 and WWK-REQ-001 move to v0.4 and WWK-DDR-001 to v0.2 with the decided status.
- No other repo is affected by these items.
- TRL stays at 3 (`trl: 3`, `trl_target: 3`). TRL 4 is on hold by Amish's instruction.
