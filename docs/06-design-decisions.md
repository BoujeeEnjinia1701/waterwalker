---
doc_id: WWK-DEC-001
title: WaterWalker design decisions register
project: WaterWalker
doc_type: Design decisions register
version: "0.3"
status: Draft
date: '2026-10-02'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-02'
  author: Amish Chadha
  change: Register opened with the design made constructable (WWK-DDR-003); budget treated as a value-engineering target
- version: "0.2"
  date: '2026-10-02'
  author: Amish Chadha
  change: Amish approved the recommendations for open items 1 to 8 on 2026-10-02 (WWK-DDR-003 accepted with A1 and A2, Kitui County as first candidate region, dead-man brake, two-motor assist target, weld fatigue, appearance choices); moved to decisions made
- version: "0.3"
  date: '2026-10-02'
  author: Amish Chadha
  change: Decisions carried into the design; value engineering restated for the hold-to-release brake (USD 492) and the two-motor assist kit (USD 450); item 4 to confirm now names the cable yoke
---

# WaterWalker design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`, WWK-BLD-001) describes the design as it stands and does not list open decisions.

## Open decisions

None. All open decisions were decided on 2026-10-02.

## To confirm when parts are bought

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The rigid 26 in forks: steel, 1 1/8 in steerer at least 170 mm above the crown, 100 mm dropouts, and their offset (the model uses 60 mm) | The offset is the caster trail and sets where the rear head tubes sit; steel blades take the welded tabs | WWK-DDR-003, P3, P13 |
| 2 | External-cup (EC34) headsets fit the 34 mm head tube bore | The head tubes are cut and reamed to suit | WWK-DDR-003, P7 |
| 3 | 100 mm front-type drum hubs are sold and serviced in the region, and their reaction arm and clip fit the fork blade | R12; the reaction arm must lie along the blade | WWK-REQ-001 R12; WWK-DDR-003, P9 |
| 4 | The brake lever with parking latch and the bail lever clamp on 22.2 mm tube, and a cable yoke that lets either input pull both outputs fits inside the 26 mm spring unit with a spring of about 390 N | The grip tubes and the spring unit are sized for them | WWK-DDR-003, P8; WWK-CAL-001 v0.4 section 6 |
| 5 | A 10 mm ball-lock pin with about 140 mm usable length | It must reach the outer tab and stay inside the axle nuts | WWK-DDR-003, P10 |
| 6 | The tires chosen (2.1 to 2.4 in) clear the fork crown by 25 mm or more | The model has 33 mm with 2.1 in tires | `cad/src/model.py` |
| 7 | The real diameter of the clay pots users carry | Two 380 mm pots fit with 12 mm to spare (R1) | WWK-REQ-001 R1 |

## Value engineering

Value-engineering target: USD 450. Estimated cost of the constructable design: USD 492 (USD 42 over the target). This is the first prototype without assist and with mounting points; the target is a hypothetical control target, not a limit. For the later assist prototype: value-engineering target: USD 450. Estimated cost of the two-motor kit: USD 450 (on the target), pack excluded. Main cost drivers and savings worth trying:

- The largest lines are the wheels and forks (USD 168 for four built wheels in forks, BOM lines 2 and 3), the tires, tubes and liners (USD 96, line 14), the frame weldment (USD 62, line 1), the four headset and steering lock sets (USD 32, line 16) and the hold-to-release brake (USD 30, line 17).
- Making the design constructable added USD 36: the four headset and lock sets (line 16, USD 32, of which USD 12 was in line 3 before), the cradle carrier and second rear brackets (line 1, USD 6), cradle brackets and bolts (line 5, USD 5), guard clips (line 8, USD 2), the second lock pin tab (line 15, USD 1) and fixings (line 12, USD 2).
- The decisions of 2026-10-02 added USD 30: the hold-to-release brake (line 17, USD 30) less the splitter it replaces (line 7, USD 4), the second torque-arm tab and the spring unit tab (line 1, USD 1) and two rating plates (line 12, USD 3).
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
| 2026-10-02 | Design for construction accepted: the changes P1 to P16 of WWK-DDR-003, as made | Amish: "APPROVED: The open decisions from the last wave (TremorTrace to ZeerBox) came in after the review and aren't on the page either." | WWK-DDR-003, Table 1 |
| 2026-10-02 | R2 and R4: accepted as not met on paper by 0.8 N and 1.5 N; the puncture protection chosen on 2026-09-25 is kept, and the push limits are confirmed with users in co-design | Amish: "APPROVED: The open decisions from the last wave (TremorTrace to ZeerBox) came in after the review and aren't on the page either." | WWK-DDR-003, A1 |
| 2026-10-02 | Ground clearance: 125 mm under the cradle carrier accepted; a clearance figure is added to the requirements after the first route survey | Amish: "APPROVED: The open decisions from the last wave (TremorTrace to ZeerBox) came in after the review and aren't on the page either." | WWK-DDR-003, A2 |
| 2026-10-02 | First co-design partner and region: the Helpful Engineering network is the route to a first partner, a university engineering department or water and sanitation NGO in semi-arid eastern Kenya, where water is carried along sandy routes and dry riverbeds; Kitui County is the first candidate region | Amish: "APPROVED: The open decisions from the last wave (TremorTrace to ZeerBox) came in after the review and aren't on the page either." | WWK-DDR-001 item 7 |
| 2026-10-02 | Dead-man brake: a hold-to-release (dead-man) brake is fitted on the first prototype: a spring applies both rear drum brakes unless the user holds a bail on the grips, kept alongside the service lever, parking latch and lock pin; users are asked about it in co-design, and it is dropped only if descent trials and users show the latch and pin are reliably used | Amish: "APPROVED: The open decisions from the last wave (TremorTrace to ZeerBox) came in after the review and aren't on the page either." | WWK-DDR-001 item 8 |
| 2026-10-02 | Value-engineering target for the later assist prototype: about USD 450 for the two-motor assist kit (two rear hub motors with their controller and push sensor), with the shared SwapCell pack counted separately; the USD 260 one-motor kit is used only if sand trials show one motor meets R3 | Amish: "APPROVED: The open decisions from the last wave (TremorTrace to ZeerBox) came in after the review and aren't on the page either." | WWK-DDR-002 item 14 |
| 2026-10-02 | Weld fatigue: the frame joints are accepted without gussets until a fatigue test at TRL 4 (61 MPa stress range in the rail, below the 71 MPa reference), and the rear cross member and caster arm welds are inspected at every service until then | Amish: "APPROVED: The open decisions from the last wave (TremorTrace to ZeerBox) came in after the review and aren't on the page either." | `docs/REVIEW.md` (2026-09-25); WWK-CAL-001 v0.3 section 7 |
| 2026-10-02 | Appearance-model choices: the left brake cable along the hip bar, the hand holds in the cradle side walls and the rated load and slope plates are adopted; grip position and spacing are asked of users at the first co-design session | Amish: "APPROVED: The open decisions from the last wave (TremorTrace to ZeerBox) came in after the review and aren't on the page either." | `docs/REVIEW.md` (2026-09-26), items 1 to 5 |
