---
doc_id: WWK-DDR-003
title: WaterWalker design for construction
project: WaterWalker
doc_type: Design decision record
version: "0.2"
status: Draft
date: '2026-10-02'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-02'
  author: Amish Chadha
  change: Changes that make the concept physically buildable, with the reason for each; made under Amish's 2026-09-30 instruction to make the design physically buildable; open for his review
- version: "0.2"
  date: '2026-10-02'
  author: Amish Chadha
  change: Accepted by Amish on 2026-10-02, with A1 and A2 decided as option (a)
---

# 0003: Design for construction

- **Date:** 2026-10-02
- **Status:** Draft; accepted. Amish, 2026-10-02: "APPROVED: The open decisions from the last wave (TremorTrace to ZeerBox) came in after the review and aren't on the page either." This approves the recommendation written for each open decision in the design decisions register (WWK-DEC-001 v0.1): every change in Table 1 is accepted as made, and A1 and A2 in Table 3 are decided as recorded there. Nothing here changes what the carrier does, its pitch or its safety case.

## Context

On 2026-09-30 Amish asked for an illustrated build plan for every repo and wrote: "If you are realising that the design cannot be built as per concept - fix the design assumptions to match and be physically feasible as you draw the illustrations." The concept model of WWK-DDR-002 showed what WaterWalker does, with correct main dimensions and interfaces, but it was a massing model: its parts were solid blocks placed where they work, not parts that can be cut, welded, bought and bolted together.

A build123d check of the concept model (each part against its neighbours, and each frame member against the cradle, the jerrycans and the rear forks) found the problems P1 to P16 below. Every one is fixed in `cad/src/model.py`, which now models each component as it is made or bought (`build_components()`) and runs 79 constructability checks (`python cad/src/model.py --check`): parts that must touch do touch, parts that must not touch are apart by at least the stated clearance, nothing overlaps, and the swept front tires stay clear of the risers. All 79 pass.

The changes keep what the carrier does: the same wheels, track, wheelbase, caster trail, hip bar height range, cradle size and height, lift height, walk-in rear, drum brakes, parking lock pin and assist mounting points.

## Decision

*Table 1. Changes made to the model, the BOM and the calculations.*

| # | Problem in the concept (build123d check) | Change made | Why this way |
| --- | --- | --- | --- |
| P1 | The side rails ran back to 15 mm behind the rear axle, through the inner blade and dropout of each rear fork (6,333 mm³ overlap per side), and carried two dropout tabs left over from the TRL 2 stub axles. | The rails end flush with the rear face of the hip sleeve, 45 mm ahead of the rear axle line. The dropout tabs are removed. | Since WWK-DDR-002 the fork holds the wheel on both sides; the rail has no job behind the sleeve, and stopping there keeps the walk-in rear open. |
| P2 | Each rear head tube hung on one 25 mm bracket, which ran into the head tube and the steerer (7,378 mm³). Parking on 20 % with the lock pin through one wheel puts about 195 N·m into that one bracket (about 190 MPa). | Two brackets, centred 745 and 805 mm above the ground, each an arm along the rail line from the sleeve's rear face and a short stub coped to the head tube (WWK-DWG-102). | The two brackets turn the parking moment into push and pull 60 mm apart: 95 MPa in the stubs, factor 2.5 on yield (WWK-CAL-001 v0.3). |
| P3 | The rear axle sat directly under the rear head tube, which needs a fork with no offset; rigid bicycle forks have an offset. | The rear head tube stands 60 mm behind the rear axle, the same offset as the front forks, so all four forks are the same part. | One fork part for all four corners; the axle position, wheelbase and track are unchanged. |
| P4 | The cradle had nothing under it. The four hangers stood on the plywood floor inside the cradle and cut through its end walls (about 13,000 mm³ each); the front pair ended 5 mm short of any frame member. | A cradle carrier: two 25 x 25 x 1.5 mm bearers under the floor, 300 mm apart, hung by four 20 x 20 x 1.5 mm hangers from the rear and front lower cross members, outside the cradle (WWK-DWG-103). The cradle bolts to the bearers with four M6 bolts. | The floor now rests on steel; the bearers are at 2.2 times yield at 2.5 g. The cradle floor stays 150 mm up, so the lift height and centre of mass are unchanged; ground clearance under the bearers is 125 mm. |
| P5 | The rear cross member, at rail height, passed through the two rear jerrycans (56,875 mm³). | It moves 17.5 mm back, to 332.5 mm ahead of the rear axle, just behind the cradle; the cans clear it by 8 mm. | Smallest move that clears the cans and still carries the rear hangers. |
| P6 | Each caster arm ran into the centre of its front head tube, through the steerer, and its root sat on a stub 65 mm outboard of the riser, so the root moment twisted the upper cross member end. | Each caster arm runs from the upper cross member's front face directly over its riser, angled 8.6 degrees outward, to the head tube, where it is coped to the tube wall. The stubs are gone; the upper cross member is one 670 mm tube on the riser tops. | The arm's bending goes straight down the riser; the head tube bore stays clear for the steerer. |
| P7 | The head tubes were solid and nothing held the forks in them; the front swivel lock pin stood in the air beside the head tube with nothing to engage. | All four head tubes are 44 mm tube with a 34 mm bore for external-cup headsets. Each steerer carries a lock collar with a 3 mm lock plate; an 8 mm pin drops through the plate into a guide welded on the frame (WWK-DWG-104). Front pins lift out to let the casters swivel; rear pins stay in, R-clipped. New BOM line 16. | One headset and lock set for all four corners; standard bicycle parts that a market mechanic knows (R12). |
| P8 | The hip bar posts filled the sleeves (solid parts overlapping, 187,500 mm³), were 280 mm long (50 mm left in the sleeve at full height), and the 32 mm grip tubes take no standard grip or lever. The push sensor's box sat where the post comes out of the sleeve. | Sleeves are tubes with a 1 mm sliding clearance on 364 mm posts (150 mm in the sleeve at full height) with nine height holes and a 6 mm pin. Grip tubes are 22.2 mm. The sensor mount is a 4 mm tab on the right sleeve, and the sensor sits outboard of it (WWK-DWG-107). | Enough insertion to carry the hip push; standard bicycle grips and brake lever fit 22.2 mm tube. |
| P9 | The drum brake reaction arm stopped in the air 120 mm ahead of the axle. | The reaction arm lies along the outer fork blade and is held by its clip, as drum hubs are fitted to forks. | It must react the brake torque on the fork. |
| P10 | The parking lock pin was held only by one tab on the inner blade, so the spokes bent it as a cantilever: about 213 MPa when parked on 20 %, a factor of 1.1. | A second tab on the outer blade holds the pin's far end (WWK-DWG-105). The pin is a 10 mm ball-lock pin about 140 mm long that ends inside the axle nuts. | Held at both ends the pin sees 119 MPa, a factor of 2.0; nothing projects beyond the axle nuts (R6). |
| P11 | The skirt guards had no fixing, and their round hub hole meant they could not go on with the wheel in place. | Each guard bolts to two tabs on the side rail (5 mm out from the rail) and is held by two rubber-lined clips on the inner fork blade. The hub hole is a 120 mm slot open at the bottom (WWK-DWG-106). | The guard is fitted before the wheel and the hub rises into the slot; it stays 15 mm from the spokes. |
| P12 | The fork blades, 12 mm thick, overlapped the hubs by 3 mm. | Dropouts 6 mm thick at the axle, blades outside the hub's over-locknut width. | Matches a real fork; overall width over the axle nuts stays 898 mm. |
| P13 | The torque-arm tab for the later motor was part of the frame weldment but sat on the bought fork blade. | It is welded to the back of the right rear fork's outer blade by the frame builder, with the lock pin tabs (WWK-DWG-105). | It has to be on the fork the motor sits in. |
| P14 | The cradle walls overlapped at the corners and had no fixings. | End walls fit between the side walls; 14 zinc angle brackets with M4 bolts outside the walls; strap anchors through the side walls (WWK-DWG-108). | 4 mm plywood is too thin for screws in its edge. |
| P15 | Frame members overlapped one another at every joint. | Members butt on each other's faces, so each has a real cut length (WWK-BLD-001, Table 2). | A welder needs a cut list. |
| P16 | The receiver plate lapped 5 mm onto the upper cross member. | It laps 15 mm. | Room for a fillet weld. |

*Table 2. Knock-on changes (WWK-CAL-001 v0.3).*

| Item | Change | Reason |
| --- | --- | --- |
| Mass | Empty 37.4 to 39.6 kg (46.1 kg with the assist kit); loaded 121.8 to 124.0 kg. | Carrier, second rear brackets, rear headsets, lock collars, fixings and brackets added (+2.2 kg). |
| Push force | Firm path 59.7 to 60.8 N (R2 now not met, by 0.8 N); 10 % climb 178.3 to 181.5 N (R4 now not met, by 1.5 N); sand 236 to 358 N to 240 to 365 N. | Follows the mass. See Table 3. |
| Frame | The rail is now carried on the hip sleeve at the rear, and the cradle hangs from the cross members: rail at the rear cross member 102 MPa (factor 2.30), front riser 115 MPa (2.04), caster arm root 129 MPa (1.82). The weld stress range in the rail falls from 75 to 61 MPa, below the 71 MPa reference. | The load path follows the constructable layout. |
| Cost | First prototype $426 to $462: USD 12 over the USD 450 value-engineering target. BOM lines 1, 3, 5, 8, 12 and 15 repriced; line 16 added. | Parts added for construction. |
| Drawings | WWK-DWG-001 Rev P3; making sketches WWK-DWG-101 to 108 added. | Follows the model. |
| Documents | WWK-CAL-001 v0.3, WWK-REQ-001 v0.5, WWK-PRC-001 v0.5, BOM line 16. | Follows the model. |

*Table 3. Decided by Amish, 2026-10-02.*

| # | Question | Options | Recommendation |
| --- | --- | --- | --- |
| A1 | R2 and R4 move from at risk to not met by 0.8 N and 1.5 N, because the constructable carrier is 2.2 kg heavier. | (a) accept on paper and confirm the push limits with users in co-design, as for R9; (b) apply the two mass options left open in WWK-DDR-002 (tires without a puncture belt, no liners: 1.6 kg, which brings R2 to 60.0 N and R4 to 179.2 N, both at risk); (c) lighter bearers and rear brackets in 1.2 mm wall (about 0.5 kg). | (a), keeping puncture protection, which Amish chose to keep on 2026-09-25. **Decided by Amish, 2026-10-02: (a).** |
| A2 | Ground clearance under the cradle carrier is 125 mm, not the 150 mm under the concept's floor. No requirement covers it. | (a) accept; (b) raise the cradle 25 mm (lift height 389 mm, centre of mass 25 mm higher). | (a); add a clearance figure to the requirements after the first route survey. **Decided by Amish, 2026-10-02: (a).** |

## Consequences

- `design_state: constructable` in `project.yaml`. The build plan WWK-BLD-001 shows every component and step in pictures generated from the model (`cad/src/build_plan_media.py`).
- Requirement status (WWK-CAL-001 v0.3): 2 met, 5 at risk, 4 not met (R2, R3, R4, R9), R11 over the value-engineering target by USD 12, R13 not verifiable at TRL 3.
- The photoreal renders (`media/render-*.png`), `media/card.png`, `media/social-preview.png` and the appearance model `cad/src/product_model.py` still show the concept: one rear bracket, rear axles under the head tubes, straight caster arms on stubs, 32 mm grip tubes and no cradle carrier. They need updating on Amish's Mac.
- The fork offset, the headset standard and the drum hub's reaction arm are to be confirmed when parts are bought (WWK-DEC-001).
