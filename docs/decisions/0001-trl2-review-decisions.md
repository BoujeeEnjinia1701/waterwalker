---
doc_id: WWK-DDR-001
title: WaterWalker TRL 2 review decisions
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
  change: Record Amish's 2026-09-25 decisions on the TRL 2 review and the items that remain open
---

# 0001: TRL 2 review decisions

- **Date:** 2026-09-25
- **Status:** accepted (items 1 to 6 and the cross-cutting items); items 7 to 13 remain proposed, awaiting Amish

## Context

The TRL 2 review note (`docs/REVIEW.md`, session 2026-09-24) listed seven items as "Proposed, awaiting Amish". On 2026-09-25 Amish reviewed the review points for every portfolio repo and wrote: "proceed with all of your recommendations across all batches. Make sure we don't proceed to TRL 4 on any of them." He also approved three cross-cutting additions to the SwapCell interface (issued as SwapCell interface v0.3) and a portfolio pricing rule for shared SwapCell packs.

This record lists what that instruction decides and what it leaves open. Items with no recommendation stay open, and so do the new engineering proposals that came out of the TRL 3 calculations (WWK-CAL-001). TRL 4 is on hold by Amish's instruction.

## Options considered

The options for items 1 to 7 are in `docs/REVIEW.md` (2026-09-24) and in the key design choices of WWK-PRC-001 v0.2. They are not repeated here.

## Decision

Each row in Table 1 is "Decided by Amish, 2026-09-25: go with recommendation".

*Table 1. Decided items.*

| # | Item | Decision | Where it now lives |
| --- | --- | --- | --- |
| 1 | Wheel size | Decided by Amish, 2026-09-25: go with recommendation. 26 x 2.1 to 2.4 in wheels all round | WWK-PRC-001 v0.3, WWK-REQ-001 R12, `cad/src/model.py` |
| 2 | Assist in the first prototype | Decided by Amish, 2026-09-25: go with recommendation. The first prototype has no assist but keeps mounting points for it; the $450 budget is kept. The budget now covers the unassisted first prototype with mounting points; the assist kit is a later second prototype | WWK-REQ-001 R11 and R13, `bom/bom.csv`, `project.yaml` (budget unchanged) |
| 3 | Steering | Decided by Amish, 2026-09-25: go with recommendation. Full-swivel lockable front casters | WWK-PRC-001 v0.3, WWK-DWG-001 |
| 4 | User position | Decided by Amish, 2026-09-25: go with recommendation. Between the rear wheels | WWK-PRC-001 v0.3, WWK-DWG-001 |
| 5 | Cradle and clay pots | Decided by Amish, 2026-09-25: go with recommendation. Four 20 L jerrycans or two 20 L clay pots per trip, until co-design shows how often pots are used. The review said the pitch should then be reworded; the pitch and README now read "four 20 L jerrycans or two clay pots" | WWK-REQ-001 R1, `project.yaml`, `README.md` |
| 6 | Brake type | Decided by Amish, 2026-09-25: go with recommendation. Drum brakes on both rear wheels with a parking latch. Whether users want a dead-man brake is a question for co-design (item 8) | WWK-PRC-001 v0.3, WWK-REQ-001 R10 |

Cross-cutting approvals from the same instruction, recorded here as they apply to WaterWalker:

- **SwapCell interface v0.3.** Decided by Amish, 2026-09-25 (cross-cutting): the SwapCell interface adds a wake method for hosts without CAN (item W), a charge-while-discharging mode (item C) and a latch vibration rating for vehicles (item V). WaterWalker's assist mounting points are drawn to SwapCell interface v0.3: a class V1 vehicle receiver on a mounting plate above the tires, with the pack's back and lid faces open to air, and a 10 kΩ INTERLOCK coding resistor in the receiver so a controller without CAN can wake the pack (item W) and draw legacy discharge-only current (15 A limit). WaterWalker does not use item C: the carrier never charges the pack. New requirement R13 (WWK-REQ-001).
- **Shared packs are priced once.** Decided by Amish, 2026-09-25 (cross-cutting): the SwapCell pack is priced in the SwapCell BOM (about $414) and excluded from this repo's budget. BOM item 10 carries a zero price with that note.
- **Co-design partners.** Decided by Amish, 2026-09-25 (cross-cutting): community designs pick co-design partners per area later. The partner stays open (item 7).

### Items that remain open

These are **Proposed, awaiting Amish**. Items 7 and 8 had no recommendation in the TRL 2 review. Items 9 to 13 are new proposals from WWK-CAL-001; the first two are already drawn in the model and drawing because the TRL 2 layout could not be built as drawn.

| # | Item | Options | Recommendation |
| --- | --- | --- | --- |
| 7 | First co-design partner and region | Helpful Engineering network, an NGO or a university in a region with sandy routes | None; for Amish to decide, per the portfolio rule on partners |
| 8 | Dead-man brake | Ask users in co-design; fit a spring-applied brake released by the hip bar; or rely on the lever and latch | None until users are asked |
| 9 | Rear wheel mounting | Keep the TRL 2 cantilever stub axles (a standard M10 axle reaches about 472 MPa at 2.5 g, above a bicycle axle's strength); or hold each rear wheel in a fixed rigid bicycle fork with 100 mm dropouts (about 89 MPa) | **Fixed forks**, as modelled. This needs 100 mm front-type drum hubs on the rear wheels and a track of 770 mm (was 800 mm) to stay within the 900 mm width |
| 10 | Caster arm and front riser position | Keep the TRL 2 riser position (the swivelling tire hits the riser); or move the risers back to x = 1,150 mm, lengthen the wheelbase to 1,530 mm and shorten the cradle to 780 mm | **Move the risers**, as modelled. Two clay pots then fit with 8 mm to spare |
| 11 | Main frame section | 30 x 30 x 1.5 mm square (yield factor 1.4 at 2.5 g); 40 x 30 x 1.5 mm rectangular (2.1); 40 x 30 x 1.2 mm (1.7, 1.8 kg lighter) | **40 x 30 x 1.5 mm** for the prototype, as modelled |
| 12 | Mass (R9 not met at 40.8 kg) | Apply the four mass options in WWK-CAL-001 (to about 35.6 kg, still over 35 kg); relax R9; or both | Apply the thinner cradle and the 1.2 mm wall, keep the puncture protection, and revisit R9 with users in co-design |
| 13 | Parking brake | Lever latch alone (about 189 N hand force at the latch); a positive lock pin through a rear wheel or drum; wheel chocks on loose ground | **Add a positive lock pin** and keep the lever latch for short stops |

## Consequences

- The first prototype is priced at about $430 against the $450 budget (R11 at risk, $20 margin). The optional assist kit (motor, sensor, receiver) adds about $260, outside the first-prototype budget, plus a shared SwapCell pack.
- The requirement set changes as follows (WWK-REQ-001 v0.3): R1 is redefined to four jerrycans or two clay pots; R11 is redefined to the unassisted first prototype with mounting points, excluding the SwapCell pack and the assist kit; R13 is added for assist readiness to SwapCell interface v0.3.
- The pitch in `project.yaml` and the README now says "four 20 L jerrycans or two clay pots" and calls the assist a later option with mounting points in the first prototype.
- TRL 4 (building and testing the prototype) is on hold by Amish's instruction.
