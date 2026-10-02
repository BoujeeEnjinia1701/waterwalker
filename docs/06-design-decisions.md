---
doc_id: WWK-DEC-001
title: WaterWalker design decisions register
project: WaterWalker
doc_type: Design decisions register
version: "0.1"
status: Draft
date: '2026-10-02'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-02'
  author: Amish Chadha
  change: Register opened with the design made constructable (WWK-DDR-003); budget treated as a value-engineering target
---

# WaterWalker design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`, WWK-BLD-001) describes the design as it stands and does not list open decisions.

## Open decisions

*Table 1. Open decisions, Proposed, awaiting Amish.*

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Accept the design-for-construction changes P1 to P16 | Accept; accept with changes; return to the concept layout | Accept: every change keeps what the carrier does and is needed for it to be built | The whole build plan | WWK-DDR-003, Table 1 |
| 2 | R2 (firm path, 60.8 N against 60 N) and R4 (10 % climb, 181.5 N against 180 N) now not met, because the constructable carrier is 2.2 kg heavier | (a) accept on paper and confirm the push limits with users in co-design; (b) apply the open mass options: tires without a puncture belt, no liners (1.6 kg; R2 60.0 N, R4 179.2 N); (c) 1.2 mm wall for the bearers and rear brackets (about 0.5 kg) | (a), keeping the puncture protection chosen on 2026-09-25 | Tires and liners (BOM line 14) or the carrier tube | WWK-DDR-003, A1 |
| 3 | Ground clearance under the cradle carrier: 125 mm (the concept floor was 150 mm up, with nothing under it) | (a) accept; (b) raise the cradle 25 mm (lift height 389 mm, centre of mass 25 mm higher) | (a); set a clearance requirement after the first route survey | Hanger lengths, cradle height | WWK-DDR-003, A2 |
| 4 | First co-design partner and region | Helpful Engineering network, an NGO or a university in a region with sandy routes | None; partners are picked per area later | None in this build; sets the push-force limits, routes and pot sizes the build is tested against | WWK-DDR-001 item 7 |
| 5 | Dead-man brake | Ask users in co-design; a spring-applied brake released by the hip bar; or rely on the lever, latch and lock pin | None until users are asked | Brake lever and cables | WWK-DDR-001 item 8 |
| 6 | Value-engineering target for the later assist prototype | Kit about USD 260 with one motor, about USD 450 with two, plus a shared SwapCell pack | None | Not part of the first build; the mounting points are | WWK-DDR-002 item 14 |
| 7 | Weld fatigue at the frame joints | Gussets at the rear cross member and caster arm joints; a local 1.5 mm wall; accept until a fatigue test | Accept until a TRL 4 fatigue test: the stress range in the rail is now 61 MPa, below the 71 MPa reference, with the cradle hung from the cross members | Frame weldment | `docs/REVIEW.md` (2026-09-25); WWK-CAL-001 v0.3 section 7 |
| 8 | Appearance-model choices from the product renders: grips at the front of the grip tubes, inboard grips on the hip bar, left brake cable along the hip bar, hand holds in the cradle side walls, the rated load and slope plate on the right rail and a second inside the left rail | Adopt each or not | Adopt the cable routing, hand holds and plates; ask users about grip position and spacing at the first co-design session | Grip tubes, cradle walls, labels | `docs/REVIEW.md` (2026-09-26), items 1 to 5 |

## To confirm when parts are bought

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The rigid 26 in forks: steel, 1 1/8 in steerer at least 170 mm above the crown, 100 mm dropouts, and their offset (the model uses 60 mm) | The offset is the caster trail and sets where the rear head tubes sit; steel blades take the welded tabs | WWK-DDR-003, P3, P13 |
| 2 | External-cup (EC34) headsets fit the 34 mm head tube bore | The head tubes are cut and reamed to suit | WWK-DDR-003, P7 |
| 3 | 100 mm front-type drum hubs are sold and serviced in the region, and their reaction arm and clip fit the fork blade | R12; the reaction arm must lie along the blade | WWK-REQ-001 R12; WWK-DDR-003, P9 |
| 4 | The brake lever with parking latch clamps on 22.2 mm tube and a cable splitter feeds both drums | The grip tubes are sized for it | WWK-DDR-003, P8 |
| 5 | A 10 mm ball-lock pin with about 140 mm usable length | It must reach the outer tab and stay inside the axle nuts | WWK-DDR-003, P10 |
| 6 | The tires chosen (2.1 to 2.4 in) clear the fork crown by 25 mm or more | The model has 33 mm with 2.1 in tires | `cad/src/model.py` |
| 7 | The real diameter of the clay pots users carry | Two 380 mm pots fit with 12 mm to spare (R1) | WWK-REQ-001 R1 |

## Value engineering

Value-engineering target: USD 450 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 462 for the first prototype without assist and with mounting points (USD 12 over the target). Main cost drivers and savings worth trying:

- The largest lines are the wheels and forks (USD 168 for four built wheels in forks, BOM lines 2 and 3), the tires, tubes and liners (USD 96, line 14), the frame weldment (USD 61, line 1) and the four headset and steering lock sets (USD 32, line 16).
- Making the design constructable added USD 36: the four headset and lock sets (line 16, USD 32, of which USD 12 was in line 3 before), the cradle carrier and second rear brackets (line 1, USD 6), cradle brackets and bolts (line 5, USD 5), guard clips (line 8, USD 2), the second lock pin tab (line 15, USD 1) and fixings (line 12, USD 2).
- Savings worth trying: plain bushed rear head tubes held by a cross bolt instead of rear headsets (about USD 10, but two kinds of head tube to make); buying the four wheels as one built set (often USD 10 to 20 less than four singles); tire liners only on the rear wheels (USD 8), if co-design shows punctures are rare on the routes.

## Decisions made

*Table 3. Decisions made.*

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-09-25 | TRL 2 review items 1 to 6: 26 in wheels; no assist in the first prototype, with mounting points; full-swivel lockable casters; user between the rear wheels; four jerrycans or two clay pots; rear drum brakes with a parking latch | Amish: "proceed with all of your recommendations across all batches. Make sure we don't proceed to TRL 4 on any of them." | WWK-DDR-001 |
| 2026-09-25 | Cross-cutting: assist mounting points to SwapCell interface v0.3 (items W and V); SwapCell pack priced once in the SwapCell BOM; co-design partners picked per area later | Amish, same instruction | WWK-DDR-001 |
| 2026-09-25 | Items 9 to 13: rear wheels in fixed forks with 100 mm drum hubs and a 770 mm track; risers at 1,150 mm and a 1,530 mm wheelbase; 40 x 30 mm main tube; 1.2 mm main wall and thinner cradle, puncture protection kept, R9 revisited with users; positive parking lock pin | Amish: "i accept all your recommendations, go with them across all repos." | WWK-DDR-002 |
| 2026-09-30 | Build plan format with pictures for every component and step; open decisions kept out of the build plan and in this register; the design made physically buildable as the pictures are drawn | Amish: "fix the design assumptions to match and be physically feasible as you draw the illustrations" and "don't log outstanding decisions in this build plan" | WWK-DDR-003 (changes open for review, Table 1 item 1) |
| 2026-10-01 | `budget_usd` is a value-engineering target, not a limit | Amish: "the budgets are a hypothethical control target to ensure we are thinking along a value engineering lens" | `.kit/STANDARDS.md` section 18 |
