# Review note: WaterWalker

## Session 2026-09-24: /populate to a strong TRL 2

### What was done

- `docs/01-problem.md` (WWK-PRB-001 v0.2): co-design placed first with the existing checklist kept and first-session questions added; the problem, users and context, constraints (terrain, sand, slopes, narrow paths, local repair), prior work (head carrying, Hippo Roller, Wello WaterWheel, loaded bicycles, carts, Lopifit, rollators) and out of scope.
- `docs/03-requirements.md` (WWK-REQ-001 v0.2): 12 measurable requirements (R1 to R12) with targets, planned verification and assumptions.
- `docs/02-concept.md` (WWK-PRC-001 v0.2): how it works, components numbered to match the exploded view and BOM, first-order numbers with assumptions, comparison with head carrying, six proposed design choices, safety and open questions.
- `cad/src/concept_media.py`: massing model (steel frame open at the rear, four 26 in wheels with full-swivel front casters, hip bar and grips, low padded cradle with four jerrycans, drum brakes, skirt guards, and optional hub motor, SwapCell pack and push sensor) with the 1.75 m scale figure.
- `media/`: hero, blueprint sheet (PNG, SVG and PDF), exploded view with BOM callouts, water-per-trip flow diagram (estimates), `model.glb` and `viewer.html`. No cutaway, because the inside does not matter for this concept.
- `bom/bom.csv`: 12 lines with indicative prices, numbered to match the exploded view; `bom/bom-notes.md`.
- `README.md`: hero image and links line added.
- `docs/pdf/`: branded PDFs of the three controlled documents.

### Key results (estimates, to be checked at TRL 3)

| Quantity | Estimate | Requirement |
| --- | --- | --- |
| Water per trip | 80 L (four jerrycans), four times a head load | R1 met for jerrycans only |
| Push force, firm level path | about 25 to 55 N | R2 (60 N) met |
| Push force, loose sand | about 225 to 340 N unassisted; about 120 to 240 N with assist | R3 (150 N) **not met** |
| Push force, 10 % climb | about 135 to 170 N unassisted; about 25 to 60 N with assist | R4 (180 N) met, thin margin |
| Turning circle | about 3.8 m | R5 (4.0 m) met, thin margin |
| Size | about 860 mm wide, 2.2 m long | R6 met |
| Empty mass | about 31 kg (38 kg with assist) | R9 met |
| Parts cost | about $300 without assist; about $600 with assist | R11 met without assist, **not met** with assist |
| Trips for 100 L per day | 2, versus 5 by head (3 trips saved) | |

Requirements not met:

- **R3 (sand).** Unassisted push force on loose sand is about 1.5 to 2.3 times the 150 N target. A single 250 W hub motor only brings the firmer end of the range within target.
- **R1 (clay pots).** The 430 mm cradle holds four jerrycans but only two 20 L clay pots. Four pots would make the carrier about 1.1 m wide and break R6.
- **R11 with assist.** The assisted version is about $600, over the $450 budget.

### Proposed, awaiting Amish

Status update (2026-09-25): items 1 to 6 are Decided by Amish, 2026-09-25: go with recommendation (WWK-DDR-001). Item 7 has no recommendation and remains Proposed, awaiting Amish.

1. Wheel size: 26 x 2.1 to 2.4 in all round. Alternatives: 20 in, 26 in rear with 20 in front, 28 in.
2. First prototype without assist, with mounting points for it. Keep the $450 budget. No budget change is proposed.
3. Steering: full-swivel lockable front casters. This choice is why the wheelbase is long (1.52 m).
4. User position between the rear wheels rather than behind the rear axle.
5. Cradle for four jerrycans or two clay pots until co-design shows how often pots are used. If accepted, the pitch in `project.yaml` ("four 20 L jerrycans or clay pots") should be reworded. That wording is for Amish to decide.
6. Drum brakes with a parking latch; ask users about a dead-man brake.
7. First co-design partner and region.

### Safety concerns

- Runaway on descents: about 55 to 90 N net downhill pull on a 10 % slope when loaded. Needs a service brake on a grip, a parking latch and possibly a dead-man brake.
- Tipping when a wheel drops into a rut on a cross-slope, and shifting loads. Containers must be strapped, and people must not ride.
- Pinch and entanglement at spokes, caster forks and telescopic posts, especially for skirts and children's hands.
- Lithium pack (assist only): BMS, fuse, sand and water protection, and safe charging location. The motor must run only while the user pushes and must cut out when the brake is pulled.
- A single rear hub motor with free casters will yaw the carrier. Lock the casters while assisting, or use two motors.

### Problems found this session

- A shorter frame with limited-swivel casters was modelled first. It could not turn tighter than about 6 m, so the layout was changed to full-swivel casters ahead of the cradle, which lengthened the carrier to 2.2 m.

### Recommended next step

Review this note and the media, and decide the proposed items above. Before `/advance-trl3`, start co-design with a local partner so that the load, container, path width and push-force targets come from users. If approved, `/advance-trl3` should verify the sand rolling resistance, brake sizing, frame stiffness and hub motor torque at walking speed by calculation, and produce the parametric model and drawing sheet.

## Session 2026-09-25: TRL 3

Amish's instruction for this session (2026-09-25): "proceed with all of your recommendations across all batches. Make sure we don't proceed to TRL 4 on any of them." He also approved the SwapCell interface v0.3 additions (wake for hosts without CAN, charge-while-discharging mode, latch vibration rating for vehicles), pricing shared SwapCell packs once, and picking co-design partners per area later. **TRL 4 is on hold by his instruction.**

### What was done

- `docs/decisions/0001-trl2-review-decisions.md` (WWK-DDR-001 v0.1): the six decided TRL 2 items, the cross-cutting approvals as they apply here, and seven open items.
- `docs/04-calcs/01-sizing.md` (WWK-CAL-001 v0.1) with `docs/04-calcs/sizing.py` and `docs/04-calcs/results.csv`: geometry, mass roll-up, push force on firm ground, slopes and sand (sinkage model), assist kit and SwapCell energy, brakes and parking with traction, frame and axle stresses, torsion, turning, stability, cost, and a table of every requirement. The script reads the model parameters and the BOM.
- `cad/src/model.py`: parametric build123d model of the first prototype and the optional assist kit, exporting `cad/step/waterwalker-first-prototype.step`, `-frame.step`, `-assist-kit.step`, `-assembly.step` and `cad/stl/waterwalker-frame.stl`, `-cradle.stl`, `-assembly.stl`.
- `cad/src/sheets.py` and `cad/drawings/WWK-DWG-001.svg`, `.pdf`, `.png`: general arrangement, Rev P1, marked "CONCEPT, NOT FOR FABRICATION" and "PRELIMINARY, NOT FOR FABRICATION". The concept blueprint keeps WWK-DWG-010.
- `bom/bom.csv` (14 lines, every line priced, supplier types) and `bom/bom-notes.md`.
- `cad/src/concept_media.py` now builds from the model; `media/` refreshed (hero, blueprint, exploded with the optional assist kit, flow, `model.glb`, `viewer.html`). Hero, blueprint and viewer show the first prototype without assist. Every image was checked; the temporary `media/_views*` folders were deleted.
- WWK-PRB-001, WWK-PRC-001 and WWK-REQ-001 moved to v0.3 with the decisions, checked numbers and new requirement R13. `project.yaml` is at `trl: 3`, `trl_target: 3` with the evidence listed; the pitch and README are updated.

### Requirements (WWK-CAL-001)

Two met, six at risk, four **not met**, one not verifiable at TRL 3.

| ID | Status | Value against target |
| --- | --- | --- |
| R2 | **Not met** | Firm path 24.6 to 61.4 N against 60 N |
| R3 | **Not met** | Loose sand 242 to 368 N against 150 N; no assist on the first prototype. One motor leaves 135 to 267 N; two motors give 15 to 148 N |
| R4 | **Not met** | 10 % climb 146.7 to 183.4 N against 180 N; descent met on paper (73 N at the lever) |
| R9 | **Not met** | Empty 40.8 kg against 35 kg (47.3 kg against 42 kg with assist) |
| R1 | At risk | Four jerrycans fit with 44 mm spare; two 380 mm clay pots with only 8 mm |
| R6 | At risk | 898 mm wide against 900 mm |
| R7 | At risk | Walking width 610 mm against 600 mm; no step-over |
| R10 | At risk | 189 N at the lever to set the parking latch on 20 %; tire friction 0.41 needed facing downhill |
| R11 | At risk | First prototype $430 against $450 |
| R12 | At risk | 100 mm drum hubs may be scarce in rural markets |
| R5 | Met | Turning circle 3.66 m against 4.0 m |
| R8 | Met | Lift 364 mm against 450 mm |
| R13 | Not verifiable at TRL 3 | Mounting points modelled; latch class V1 retention needs a test |

Key numbers: loaded mass 125.2 kg; centre of mass 364 mm high; side tip angle 47 degrees; frame stress 112 MPa at 2.5 g (factor 2.09); assist 83 Wh/km per motor on sand, 5.4 km per SwapCell pack.

Corrections to TRL 2: empty mass 31 to 40.8 kg (tires, tubes, liners, a second pair of forks and a heavier frame were missing), parts cost $300 to $430 (tires and forks were missing), width 860 to 898 mm, walking width 660 to 610 mm, turning circle 3.8 to 3.66 m, and the assist pack is SwapCell's 46.8 V, not 36 V. Two layout faults were found and fixed in the model as proposals: the cantilevered rear stub axles (about 472 MPa in an M10 axle at 2.5 g) and front risers inside the caster sweep.

### Decisions recorded

Decided by Amish, 2026-09-25: go with recommendation (WWK-DDR-001): 26 x 2.1 to 2.4 in wheels all round; no assist in the first prototype, with mounting points, keeping `budget_usd: 450` and redefining it in R11 as the unassisted first prototype with mounting points; full-swivel lockable casters; user between the rear wheels; four jerrycans or two clay pots (R1 redefined; pitch and README reworded to "four 20 L jerrycans or two clay pots"); rear drum brakes with a parking latch. Cross-cutting: assist mounting points built to SwapCell interface v0.3 items W and V (item C not used), new R13; SwapCell pack priced once in the SwapCell BOM and excluded here.

### Still awaiting Amish

Status update (2026-09-25, WWK-DDR-002): items 3 to 7 are Decided by Amish, 2026-09-25: go with recommendation. Items 1, 2 and 8 have no recommendation and remain Proposed, awaiting Amish.

1. First co-design partner and region (no recommendation; per area later).
2. Dead-man brake (no recommendation until users are asked).
3. Rear wheels in fixed rigid forks with 100 mm drum hubs and a 770 mm track. Recommended; already in the model. Decided by Amish, 2026-09-25: go with recommendation.
4. Front risers moved to x = 1,150 mm, wheelbase 1,530 mm, cradle 780 mm. Recommended; already in the model. Decided by Amish, 2026-09-25: go with recommendation.
5. Main tube 40 x 30 x 1.5 mm. Recommended; already in the model. Decided by Amish, 2026-09-25: go with recommendation (section kept; wall 1.2 mm under item 6).
6. Mass: apply the thinner cradle and 1.2 mm main-tube wall (35.6 kg with all four options, still over 35 kg), and revisit R9 with users. Recommended. Decided by Amish, 2026-09-25: go with recommendation.
7. Parking: add a positive lock pin. Recommended. Decided by Amish, 2026-09-25: go with recommendation.
8. Budget for the later assist prototype (kit $260, or about $450 with two motors, plus a shared pack). No recommendation. Proposed, awaiting Amish.

### Safety concerns

- Runaway and parking on slopes: 61 to 98 N downhill pull on 10 %; the parking latch needs about 189 N at the lever, and on loose ground the rear tires may slide (friction 0.41 needed). A lock pin and chocks help with the first, not the second.
- Weld fatigue at the cradle hangers and caster arm roots is at risk (63 MPa stress range against about 71 MPa for a typical fillet weld detail). Only a test can show it.
- Caster sweep (about 400 mm radius), spokes and forks are pinch and entanglement points for feet, skirts and children's hands.
- The empty carrier weighs about 41 kg, a two-person lift over steps and ditches.
- Later assist: lithium pack in a class V1 receiver, sealed from sand and water but open to air on two faces; motor heat at walking speed (about 107 W per motor on sand); one-motor yaw needs locked casters.

### Existing TRL 4 material

None found. No test articles, test plans, build procedures or purchasing lists exist in this repo, and none were created. `build-log/` holds only its README.

### Citations

The earlier review note listed no unchecked citations. WWK-CAL-001 relies on stated assumptions and standard relations (rigid-wheel sinkage geometry, Bekker's pressure-sinkage scaling, Bredt torsion) and on the SwapCell interface v0.3 values in the SwapCell repo; no new external sources were cited, so no web check was needed.

### Recommended next step

Amish reviews WWK-DDR-001 open items 3 to 8, above all the mass and parking proposals, and decides whether R2, R4 and R9 should be relaxed or the design lightened. Co-design with a local partner (item 1) should then confirm push-force limits, sand sinkage on real routes, clay pot sizes and the brake arrangement before any build. **TRL 4 is on hold by Amish's instruction.** For the record only, TRL 4 would need: the open decisions settled, a first-prototype build budget confirmed, sourcing of 100 mm drum hubs checked, a built frame and carrier, lab test reports (TST, `environment: lab`) for push force, parking on 20 %, frame strength and fatigue, and turning, and build-log entries.

## Session 2026-09-25: recommendations accepted

Amish wrote on 2026-09-25: "i accept all your recommendations, go with them across all repos." Every item with a recommendation is now **Decided by Amish, 2026-09-25: go with recommendation**; items without one stay open. Recorded in `docs/decisions/0002-recommendations-accepted.md` (WWK-DDR-002 v0.1).

### Decisions applied and what changed

| Item | Decision | Change in the repo |
| --- | --- | --- |
| Rear wheels in fixed forks (DDR-001 item 9) | Decided | Already modelled; status only |
| Risers at x = 1,150 mm, wheelbase 1,530 mm (item 10) | Decided | Already modelled; status only |
| Main tube 40 x 30 mm (item 11) | Decided | Section kept; wall set by item 12 |
| Mass (item 12) | Decided: 1.2 mm main wall, thinner cradle, keep puncture protection, revisit R9 with users | Main wall 1.5 to 1.2 mm; cradle floor 9 to 6 mm, walls 6 to 4 mm, pad 4 to 2 mm. Empty mass 40.8 to 37.4 kg; loaded 125.2 to 121.8 kg. Revisiting R9 with users waits for co-design |
| Parking (item 13) | Decided: positive lock pin, latch kept for short stops | New BOM item 15 ($5, 0.10 kg), modelled on the left rear fork, through the left skirt guard and spokes; R10 restated |

Numbers before and after (WWK-CAL-001 v0.1 to v0.2): firm push 61.4 to 59.7 N; 10 % climb 183.4 to 178.3 N; loose sand 242 to 368 N to 236 to 358 N; caster arm stress 112 to 133 MPa (factor 2.09 to 1.77); weld stress range at the rear hanger 63 to 75 MPa; clay pot spare length 8 to 12 mm; parts $430 to $426. Budget: `budget_usd` unchanged at 450; no recommendation changed it.

Files changed: `cad/src/model.py` and all STEP and STL exports; `cad/src/sheets.py` and WWK-DWG-001 (Rev P1 to P2); `cad/src/concept_media.py` and `media/` (hero, blueprint, exploded with callout 15, flow, `model.glb`, `viewer.html`; images checked, `media/_views*` deleted); `bom/bom.csv` and `bom/bom-notes.md`; `docs/04-calcs/sizing.py`, `results.csv` and WWK-CAL-001 v0.2; WWK-PRC-001 v0.4; WWK-REQ-001 v0.4; WWK-PRB-001 v0.4; WWK-DDR-001 v0.2; `project.yaml` (evidence list); `README.md` (concept numbers and the four write-up sections, with a new "What sparked the idea": Aina Wifalk's 1978 rollator). All PDFs regenerated with the designmolecule.com footer.

### Requirement status (WWK-CAL-001 v0.2)

3 met, 7 at risk, 2 **not met**, 1 not verifiable at TRL 3 (was 2, 6, 4 and 1).

| ID | Status | Value against target |
| --- | --- | --- |
| R3 | **Not met** | Loose sand 236 to 358 N against 150 N; no assist on the first prototype |
| R9 | **Not met** | Empty 37.4 kg against 35 kg (43.9 kg against 42 kg with assist) |
| R1 | At risk | Two 380 mm clay pots fit with 12 mm spare |
| R2 | At risk | Firm path 59.7 N against 60 N |
| R4 | At risk | 10 % climb 178.3 N against 180 N |
| R6 | At risk | 898 mm against 900 mm |
| R7 | At risk | Walking width 610 mm against 600 mm |
| R10 | At risk | Lock pin for parking; tire friction 0.41 needed on 20 % |
| R12 | At risk | 100 mm drum hubs may be scarce in rural markets |
| R5 | Met | 3.66 m against 4.0 m |
| R8 | Met | 364 mm against 450 mm |
| R11 | Met | $426 against $450 |
| R13 | Not verifiable at TRL 3 | Mounting points modelled; latch class V1 retention needs a test |

### Still awaiting Amish

1. First co-design partner and region (no recommendation; per area later).
2. Dead-man brake (no recommendation until users are asked).
3. Budget for the later assist prototype (no recommendation).
4. New finding: with the 1.2 mm wall the weld stress range at the cradle hangers is 75 MPa, above the 71 MPa of a typical fillet-welded detail at 2 million cycles. Options: gussets at the hanger and caster arm joints (recommended, small mass), a local 1.5 mm wall at those joints, or accept the risk until a fatigue test. Proposed, awaiting Amish; not applied.

### Cross-repo actions

None. No accepted recommendation for WaterWalker needs a change in another repo; the SwapCell interface v0.3 items were already handled in the previous session.

### Safety concerns

- Weld fatigue at the cradle hangers is now past the reference value (item 4 above).
- The lock pin must be pulled before moving off, and it loads the spokes sideways (about 410 N when parked on 20 %); the pull ring sits at the inner face of the left side rail in the walking space.
- Runaway, traction on loose ground when parked, caster sweep pinch points and the lithium pack of the later assist kit are unchanged from the previous session.

### TRL 4

**TRL 4 remains on hold by Amish's instruction.** `trl: 3` and `trl_target: 3` are unchanged. Revisiting R9 with users, the lock pin and spoke test, and any weld fatigue test are decided in direction but on hold. No build, test, purchasing or firmware work was done.

## Session 2026-09-26: sources strengthened

Amish asked to fix the weaker sources in the README (2026-09-26). Every link below was fetched and checked against the claim it supports. No controlled document changed; `docs/01-problem.md` did not cite the replaced sources.

| Where | Old source | New source |
| --- | --- | --- |
| Burning platform | WHO drinking-water fact sheet (kept) | Same; the 2.2 billion figure is now dated 2022, as the fact sheet states |
| Country row, Niger (was "Niger and the Sahel") | None | [UNICEF Niger, WASH](https://www.unicef.org/niger/water-sanitation-and-hygiene): 56 % have access to a drinking water source. The uncited claim about sandy routes was removed |
| Country row, India (was "Rajasthan and other dry states") | None | [UNICEF India, clean drinking water](https://www.unicef.org/india/what-we-do/clean-drinking-water): 54 % of rural women spend about 35 min a day fetching water; under 49 % of rural people use safely managed water. The uncited claims about desert villages and bicycle repair were removed |
| Country row, Peru (was "Peru and Bolivia") | None | Peer-reviewed study of peri-urban Lima shanty towns ([ScienceDirect, 2025](https://www.sciencedirect.com/science/article/pii/S2667010025003051)): about 350 tanker trucks a day serve some 250,000 homes; a hillside household gets about 1,100 L a month. Bolivia dropped (no verified source) |
| Country row, Japan (Noto) | Wikipedia, 2024 Noto earthquake | [The Japan Times, 23 February 2024](https://www.japantimes.co.jp/news/2024/02/23/japan/society/noto-quake-sparks-water-debate/): up to 135,000 households without running water; nearly 24,000 still without it. The Shika six-litre ration could not be verified and was removed |
| What sparked the idea (Aina Wifalk's rollator) | Wikipedia, Aina Wifalk | [Swedish Institute, sharingsweden.se](https://sharingsweden.se/materials/the-invention-of-the-walker) (1978 prototype, Västerås, polio, never patented) and [Svenskt UppfinnareMuseum](https://svensktuppfinnaremuseum.se/aina-wifalk/) (never patented so it would reach as many people as possible). "Presented in 1978" became "designed the prototype in 1978", as the sources state |

Inspiration unchanged (same event, stronger sources). No budget change.

## Session 2026-09-26: product appearance model and photoreal renders

Amish chose this repo for the first batch of product renders on 2026-09-26. This session adds `cad/src/product_model.py`, a finished-product appearance model for photoreal renders, and points the README hero at `media/render-hero.png` with a link to `media/render-exploded.png`. The render files are produced later by the orchestrator. `cad/src/model.py`, the BOM, the drawings and the controlled documents are unchanged.

### What product_model.py adds

- `product_parts()` in the portfolio format (name, shape, colour, material, BOM line, group, explode offset), with `TITLE` and three `RENDER_VIEWS`: hero (front right, with the person), exploded (front right, with the optional assist kit) and detail (rear right, without the person, showing the walk-in rear).
- Frame from `frame_members()` with rounded tube corners, head tubes with headset cups and top caps, dropout tabs, the galvanized receiver plate, torque-arm tab and sensor boss, black tube end caps, red rear and white front reflectors, a rated load and slope plate and a wordmark on the right side rail.
- Four wheels with treaded tires, alloy rims with a rim bed, 36 laced spokes, hub flanges, axles, axle nuts and valves; round-bladed rigid rear forks and swivel caster forks with red drop-pin knobs; finned drum brake plates with reaction arms.
- Hip bar with a stitched fabric-covered foam pad, telescopic posts with height holes, clamp collars and height pins, rubber hand grips with ribs and end plugs, the brake lever with its parking latch, and brake cables to both rear drums.
- Plywood cradle with a rubber pad, removable divider, zinc corner brackets, two webbing straps with cam buckles, and four jerrycans with handles, ribbed caps and side ribs.
- HDPE skirt guards with rounded corners and bolts; the parking lock pin with its tab, a red pull ring and a lanyard.
- Optional assist kit, shown only in the exploded view: hub motor with flanges and cable, SwapCell pack with handle, accent band and lit charge lights, receiver with guides and preload lever, push sensor with a lit status light.
- Context: the shared clay mannequin (1.75 m, "push" pose with arm angles overridden) walking inside the frame with both hands on the grips and the feet on the ground.

### Where the appearance model differs from model.py

Every main dimension and interface is taken from `PARAMS`, `derived()` and `frame_members()`. The differences below are appearance choices that model.py does not define; none is adopted into the design.

1. **Rubber grips at the front of the grip tubes.** The grips cover x = -110 to 40 mm, next to the hip bar posts, so the hands can sit beside the pad while the hips push on it. model.py shows a plain tube from x = -230 to 60 mm. Proposed, awaiting Amish. Recommendation: keep the grips at the front end and confirm the hand position in co-design.
2. **Grip spacing against the user's shoulders.** The grips follow the side rails, 640 mm apart, about twice shoulder width. With hands on them at 950 mm the mannequin's elbows bend back and its pelvis stands about 140 mm behind the pad, so the hips reach the pad only when leaning in. Proposed, awaiting Amish. Options: keep the grips on the rails (no change), or add inboard grips on the hip bar. Recommendation: no change now; ask users at the first co-design session.
3. **Brake cable routing.** model.py has no cables. The left rear cable is drawn along the underside of the hip bar and down the left post, so no cable crosses the open walk-in rear. Proposed, awaiting Amish. Recommendation: adopt this routing.
4. **Hand holds in the cradle side walls** (two 90 x 26 mm slots per side) and the removable divider drawn between the two rows of jerrycans. The BOM lists dividers but not their position; model.py has neither. Proposed, awaiting Amish. Recommendation: keep both; the hand holds make the empty cradle easier to lift out.
5. **Marking positions.** The rated load and slope plate is drawn on the outer face of the right side rail, with red rear reflectors on the hip bar sleeves and white front reflectors on the front risers (BOM item 12). Proposed, awaiting Amish. Recommendation: adopt, and add a second plate on the inside of the left rail where the user can read it.
6. **Representation only.** Rounded tube corners, round fork blades in place of model.py's rectangular blocks, 36 laced spokes in place of six bars, tire tread, and the jerrycan handles and caps inside the same envelopes. The hip bar is drawn graphite and the cradle natural plywood, rather than the concept media colours. No action needed.

### TRL

This is an appearance model only: no tolerances, no fabrication detail. `trl` stays 3 and `trl_target` stays 3. TRL 4 remains on hold by Amish's instruction. No build, test, purchasing or firmware work was done.

## Session 2026-09-27: kit 1.5.0 and image quality

- Kit 1.5.0 synced: STANDARDS v1.5 (sections 12 to 15: product renders, storefront images and image quality, public release, authorship and signing), `.kit/cards.py`, `.kit/image_qc.py`, `.kit/release_gate.py`, issue templates, and the `/render-product` and `/release` commands. `CLAUDE.md` now matches `.kit/CLAUDE.md`.
- Every `media/render-*.png` recaptioned from its original render with the new layout: the title, concept label and repository sit in a band above the render and the view note in a band below it, each line wrapped to the image width, so no text overlaps other text or the render or runs off the image. `media/card.png` and `media/social-preview.png` regenerated with the same rules.
- `python .kit/image_qc.py` and `python .kit/release_gate.py` pass. trl stays 3.

## Session 2026-10-02: design made constructable and prototype build plan (kit 1.7.0)

Amish approved the build plan format on 2026-09-30 and asked for it in every repo, with outstanding decisions kept in a separate design decisions register. He also wrote: "If you are realising that the design cannot be built as per concept - fix the design assumptions to match and be physically feasible as you draw the illustrations." On 2026-10-01 he set budgets as value-engineering targets. TRL stays 3; nothing was built or bought.

### What was done

- Kit 1.7.0 installed (`.kit/`, `.claude/commands/`); `CLAUDE.md` now matches `.kit/CLAUDE.md`.
- `cad/src/model.py` rewritten so every component is modelled as it is made or bought (`build_components()`), with 79 build123d constructability checks (`python cad/src/model.py --check`, all pass). STEP and STL regenerated.
- `docs/decisions/0003-design-for-construction.md` (WWK-DDR-003 v0.1, Draft): every change below, made under Amish's 2026-09-30 instruction to make the design physically buildable; open for his review.
- `cad/src/build_plan_media.py`: the overview, eight making sketches (`cad/drawings/WWK-DWG-101` to `108`), ten joint close-ups and eleven assembly step pictures in `docs/05-build-plan/`. Every picture was looked at and the unclear ones redrawn.
- `docs/05-build-plan.md` (WWK-BLD-001 v0.1) and `docs/06-design-decisions.md` (WWK-DEC-001 v0.1).
- `docs/04-calcs/sizing.py` and WWK-CAL-001 v0.3: new load path, rear head tube brackets, cradle bearers, lock pin and mass; R11 against the value-engineering target. WWK-REQ-001 v0.5, WWK-PRC-001 v0.5, `bom/bom.csv` (line 16 added) and `bom/bom-notes.md` updated.
- WWK-DWG-001 Rev P3; concept media regenerated (`media/hero.png`, blueprint, exploded, flow, `model.glb`, `viewer.html`).
- `project.yaml`: `design_state: constructable`, the build plan, register and WWK-DDR-003 in `trl_evidence`. README: links line and a "Building the prototype" section.

### Design changes made for construction (WWK-DDR-003)

| # | Change |
| --- | --- |
| P1 | Side rails end at the hip sleeves instead of running through the rear forks; old dropout tabs removed |
| P2 | Each rear head tube held by two brackets 60 mm apart, not one, so parking on one pinned wheel is carried |
| P3 | Rear head tubes 60 mm behind the rear axle, matching the fork offset; one fork part for all four corners |
| P4 | Cradle carrier added: two bearers under the floor on four hangers from the cross members; cradle bolted to it (ground clearance 125 mm) |
| P5 | Rear cross member moved 17.5 mm back, clear of the rear jerrycans |
| P6 | Caster arms run from the top of each riser, angled 8.6 degrees outward, to the side of the head tube; stubs removed |
| P7 | Headsets at all four forks, a lock collar and plate on each steerer, pins into guides on the frame (BOM line 16) |
| P8 | Hip sleeves as tubes with 364 mm posts (150 mm left in at full height), nine height holes and a pin; 22.2 mm grip tubes; sensor tab replaces the solid boss |
| P9 | Drum brake reaction arm clipped along the outer fork blade |
| P10 | Parking lock pin held by tabs on both fork blades; a 10 mm ball-lock pin ending inside the axle nuts |
| P11 | Skirt guards bolted to rail tabs and clipped to the inner blade; slot for the hub so they go on before the wheel |
| P12 | Fork dropouts 6 mm at the axle so the blades clear the hubs |
| P13 | Torque-arm tab welded to the right rear fork, not the frame |
| P14 | Cradle walls with end walls between the side walls and 14 outside angle brackets |
| P15 | Frame members butt on each other's faces with real cut lengths |
| P16 | Receiver plate laps 15 mm onto the upper cross member |

### Key results (WWK-CAL-001 v0.3)

- Empty mass 37.4 to 39.6 kg (+2.2 kg); loaded 124.0 kg.
- **Not met:** R2 firm path 60.8 N against 60 N (was at risk); R3 loose sand 240 to 365 N against 150 N; R4 10 % climb 181.5 N against 180 N (was at risk); R9 39.6 kg against 35 kg.
- At risk: R1, R6, R7, R10, R12. Met: R5, R8. R13 not verifiable at TRL 3.
- Value-engineering target USD 450; estimated cost of the constructable design USD 462 (USD 12 over the target; USD 36 added for construction).
- Frame: caster arm root 129 MPa (factor 1.82); weld stress range in the rail 61 MPa, now below the 71 MPa reference; rear brackets 95 MPa when parked on one pinned wheel (factor 2.5); bearers factor 2.2; lock pin factor 2.0 held at both ends (1.1 at one end, as in the concept).

### Proposed, awaiting Amish (in WWK-DEC-001)

1. Accept the design-for-construction changes P1 to P16. Recommended.
2. R2 and R4 now not met by 0.8 N and 1.5 N: accept on paper and confirm push limits in co-design (recommended), apply the open tire mass options, or lighten the carrier tube.
3. Ground clearance 125 mm under the carrier: accept (recommended) or raise the cradle 25 mm.
4. Unchanged from earlier sessions: co-design partner, dead-man brake, value-engineering target for the assist prototype, weld fatigue (now recommended to wait for a TRL 4 test), and the appearance-model choices of 2026-09-26.

### Safety concerns

- Tabs are now welded to the steel rear forks (lock pin and torque arm); the welds need a skilled welder and inspection (build plan safety stop S1).
- Runaway and parking on slopes are unchanged: tire friction 0.41 needed on 20 %; the lock pin is held at both ends now, but the spokes still take its load in bending.
- The caster sweep (about 400 mm radius, 22.5 mm clear of the risers), spokes and forks remain pinch points; the skirt guards are now fixed at four points.

### Stale media (made on Amish's Mac, not regenerated here)

`media/render-hero.png`, `media/render-exploded.png`, `media/render-detail.png`, `media/card.png` and `media/social-preview.png`, and the appearance model `cad/src/product_model.py`, still show the concept: one rear bracket with the axle under the head tube, caster arms on stubs, 32 mm grip tubes and no cradle carrier. The design changed visibly, so they are stale and need re-rendering with `/render-product`.

### Recommended next step

Amish reviews WWK-DDR-003 and the three new items in WWK-DEC-001. **TRL 4 remains on hold.** For the record only, TRL 4 would start by buying the forks and drum hubs to confirm the items in WWK-DEC-001 Table 2, then building to WWK-BLD-001 and recording the first checks in a test report.

## Session 2026-10-02: open decisions decided

Amish, 2026-10-02: "APPROVED: The open decisions from the last wave (TremorTrace to ZeerBox) came in after the review and aren't on the page either." This approves the recommendation written for each open decision in the design decisions register (WWK-DEC-001), as he did for the other 555 open decisions ("i approve your recommendations for all 555 open decisions."). trl stays 3; no build or test work was done, and the model, BOM quantities and prices, and pictures are unchanged.

### Decisions recorded

Eight decisions, all moved to Decisions made in WWK-DEC-001, dated 2026-10-02:

1. Design for construction accepted: the changes P1 to P16 of WWK-DDR-003, as made.
2. R2 and R4: accepted as not met on paper by 0.8 N and 1.5 N; the puncture protection chosen on 2026-09-25 is kept, and the push limits are confirmed with users in co-design.
3. Ground clearance: 125 mm under the cradle carrier accepted; a clearance figure is added to the requirements after the first route survey.
4. First co-design partner and region: the Helpful Engineering network is the route to a first partner, a university engineering department or water and sanitation NGO in semi-arid eastern Kenya, where water is carried along sandy routes and dry riverbeds; Kitui County is the first candidate region.
5. Dead-man brake: a hold-to-release (dead-man) brake is fitted on the first prototype: a spring applies both rear drum brakes unless the user holds a bail on the grips, kept alongside the service lever, parking latch and lock pin; users are asked about it in co-design, and it is dropped only if descent trials and users show the latch and pin are reliably used.
6. Value-engineering target for the later assist prototype: about USD 450 for the two-motor assist kit (two rear hub motors with their controller and push sensor), with the shared SwapCell pack counted separately; the USD 260 one-motor kit is used only if sand trials show one motor meets R3.
7. Weld fatigue: the frame joints are accepted without gussets until a fatigue test at TRL 4 (61 MPa stress range in the rail, below the 71 MPa reference), and the rear cross member and caster arm welds are inspected at every service until then.
8. Appearance-model choices: the left brake cable along the hip bar, the hand holds in the cradle side walls and the rated load and slope plates are adopted; grip position and spacing are asked of users at the first co-design session.

### Documents changed

- `docs/06-design-decisions.md` (WWK-DEC-001 v0.2): open decisions moved to Decisions made.
- `docs/decisions/0003-design-for-construction.md` (WWK-DDR-003 v0.2): acceptance recorded in the status line; A1 and A2 decided (record stays Draft).
- `docs/decisions/0001-trl2-review-decisions.md` (WWK-DDR-001 v0.3): items 7 and 8 recorded as decided.
- `docs/decisions/0002-recommendations-accepted.md` (WWK-DDR-002 v0.2): items 7, 8 and 14 recorded as decided.
- `docs/01-problem.md` (WWK-PRB-001 v0.5): partner and region answered.
- `docs/02-concept.md` (WWK-PRC-001 v0.6): brake choice, runaway safety note, assist target and partner.
- `docs/03-requirements.md` (WWK-REQ-001 v0.6): R2 and R4 notes; no status changed.
- `bom/bom-notes.md`: assist prototype target; dead-man brake noted as not yet a BOM line.
- `README.md`: the build plan paragraph says the decisions are all made.

### Follow-up actions to carry approved decisions into the design

1. Decision 5 (model): Model the hold-to-release brake: a bail on the grips, a return spring and the cable route to both rear drums alongside the service lever, with clearance checks.
2. Decision 5 (BOM): Add the hold-to-release brake parts (bail lever, spring, cable and splitter) to the BOM with a price basis.
3. Decision 5 (calculations): Add the brake's mass to the roll-up and re-run the push forces (R2, R4, R9) and the descent and parking checks in WWK-CAL-001.
4. Decision 5 (pictures): Add the dead-man brake to the general arrangement, the build plan's brake step, wiring and cable picture, and a safety stop that tests it before the first loaded descent.
5. Decision 6 (model): Add a torque-arm tab to the left rear fork as well, so the two-motor assist kit bolts on, and update the assist mounting description.
6. Decision 6 (calculations): State the assist prototype's value-engineering target (about USD 450, two motors, pack excluded) in WWK-CAL-001 and the concept cost row.
7. Decision 7 (docs): Add a weld inspection of the rear cross member and caster arm joints to the build plan's checks and service notes, pending the TRL 4 fatigue test.
8. Decision 8 (model): Add the hand holds in the cradle side walls, the left brake cable along the hip bar and the rated load and slope plates to the model and drawing.
9. Decision 4 (docs): Approach a university engineering department or water and sanitation NGO in Kitui County through the Helpful Engineering network.

### Points found in the review

- A dead-man brake (item 5) adds a little mass, so R2 and R4 move slightly further from their limits; the push-force calculation needs re-running when it is modelled.
- Item 6 is labeled a budget in WWK-DDR-002 item 14; under the 2026-10-01 rule it is a value-engineering target, not a limit.
- The concept's assist description (one hub motor in a rear wheel, step 6) and BOM notes (USD 260 kit) describe one motor, while the calculation and R3 note say two are needed on the loosest sand.

## Session 2026-10-02: approved follow-ups carried out

Amish, 2026-10-02: "497 follow-up actions that need CAD, drawing, picture, BOM or calculation work ... APPROVED CHANGES, COMPLETE THESE", and for the renders: "Photoreal renders are out of date in most repos ... COMPLETE THESE". trl stays 3; nothing was built, bought or tested.

### Follow-ups

1. Decision 5 (model): **done.** `cad/src/model.py` adds the hold-to-release brake (BOM line 17): a bail lever clamped on the left grip tube, a spring unit (26 mm tube, 132 mm long, with toggle and cable yoke) held by two saddle clips on a 4 mm tab welded to the outer face of the left hip sleeve, a bail cable, the service lever cable along the front of the hip bar to the yoke, and a cable from the yoke to each rear drum, passing in front of and outside each rear head tube and down the front of the outer fork blade, inside the width over the axle nuts. 18 new constructability checks (bail on the grip tube and clear of the grip, unit on its tab and clear of the brackets, height pin, wheel, fork and collar, cables clear of frame, hip bar, wheels, forks, tabs, lock pin, guards, headsets, sensor and motors, cables meeting the unit): 104 of 104 pass. STEP and STL regenerated.
2. Decision 5 (BOM): **done.** New line 17, USD 30, with a price basis per part; line 7 USD 20 to USD 16 (splitter replaced by the yoke); see `bom/bom-notes.md`.
3. Decision 5 (calculations): **done.** WWK-CAL-001 v0.4: brake 0.60 kg in the roll-up; R2 61.2 N, R4 182.6 N, R9 40.3 kg; spring 390 N (hold on 10 % with the assisted mass, margin 1.25), holds up to 12 % alone, stops in about 2.6 m if let go at 1.0 m/s on 10 %; squeeze 98 N, hold 24 N (toggle factor is an estimate); parking on 20 % still needs the latch or lock pin (192 N latch, friction 0.41).
4. Decision 5 (pictures): **done.** WWK-DWG-001 Rev P4; overview; new joint 11 (spring unit); step 8 (bail and grips) and new step 9 (spring unit and cables); old steps 9 to 11 are now 10 to 12; safety stop S4 tests the brake before the first loaded descent; WWK-BLD-001 v0.2 section 3.9 describes it.
5. Decision 6 (model): **done.** Torque-arm tab on the left rear fork as well (checks: on the blade, clear of wheel, brake arm, lock pin tabs and pin); two hub motors in the assist kit; mounting description updated in WWK-PRC-001 v0.7 and WWK-DWG-105.
6. Decision 6 (calculations): **done.** WWK-CAL-001 v0.4 section 5 and the precis: "Value-engineering target: USD 450. Estimated cost of the two-motor kit: USD 450 (on the target)", pack excluded; BOM line 9 quantity 2.
7. Decision 7 (docs): **done.** Weld inspection of the rear cross member and caster arm joints added to the build plan's first checks and as safety stop S6 (every service until the TRL 4 fatigue test).
8. Decision 8 (model): **done.** Hand holds (two 90 x 26 mm slots per side wall), the left brake cable along the hip bar (the service cable now crosses along the front of the pad to the left-side unit) and two rated load and slope plates (right rail outside, left rail inside) are in the model, the GA and WWK-DWG-108.
9. Decision 4 (outreach): **not done:** outreach by Amish through the Helpful Engineering network.

### Requirement status

No status changed. R2 not met by 1.2 N (was 0.8 N), R4 by 2.6 N (was 1.5 N), R9 40.3 kg (49.6 kg with the two-motor kit), R10 at risk, R11 over the target by USD 42. With the second motor's mass counted, the two-motor kit leaves 154 N on the loosest sand, 4 N over R3 (144 N in v0.3); a motor of about 41 N·m closes it.

### Cost and mass

Value-engineering target: USD 450. Estimated cost of the constructable design: USD 492 (USD 42 over the target). Empty mass 40.3 kg; loaded 124.7 kg.

### Documents changed and new versions

`cad/src/model.py`; `cad/step/*`, `cad/stl/*`; `bom/bom.csv`, `bom/bom-notes.md`; `docs/04-calcs/sizing.py`, `results.csv`, WWK-CAL-001 v0.4; WWK-REQ-001 v0.7; WWK-PRC-001 v0.7; WWK-DEC-001 v0.3; WWK-BLD-001 v0.2; README; `cad/src/sheets.py` and WWK-DWG-001 Rev P4; `cad/src/build_plan_media.py` with WWK-DWG-101, 102, 105 and 108, overview, joints 1, 5, 7 and 11, steps 2, 4, 5 and 7 to 12; `cad/src/concept_media.py` (blueprint Rev P3, hero, exploded, flow, `model.glb`, `viewer.html`); `cad/src/product_model.py`. The drawing scripts share `patch_svg_export()` in `model.py`, which draws the few degenerate arcs the cables project to as short lines.

### Appearance model and render scenes

`cad/src/product_model.py` now builds the frame, brackets, carrier, forks, headsets, collars, tabs, guards, hip bar, brakes, cradle, plates, lock pin and assist kit directly from `model.build_components()`, so it matches the constructable design; wheels, jerrycans, straps, pad, grips, reflectors and end caps are drawn on model.py's dimensions. RENDER_VIEWS kept (hero, exploded, detail). Scenes exported to `/home/claude/renders/waterwalker` (one .npz and .json per view and `waterwalker__jobs.json`). Photoreal renders, `card.png` and `social-preview.png` are to be made on Amish's Mac. Proposed, awaiting Amish: the rubber grips and the mannequin's hands now sit on model.py's grips (230 to 100 mm behind the axle), so the figure stands about 165 mm further back than in the 2026-09-26 renders and its hips do not touch the pad; recommendation: keep, since grip position is asked of users at the first co-design session.

### Cross-repo actions

- SwapCell: the WaterWalker assist kit now draws up to 7.8 A from the pack through two controllers; no change to interface v0.3 is needed (for information only).

### Safety

The hold-to-release brake does not park on 20 %; the latch and lock pin remain the parking brakes. The hold force depends on an estimated toggle factor and must be measured at TRL 4 before users rely on it.

### Recommended next step

Amish reviews the renders made from the new scenes. TRL 4 remains on hold.

## 2026-10-02: photoreal renders redone on the constructable design

Rendered with Blender Cycles on Amish's Mac from the updated appearance model; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` regenerated with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes. Appearance deviations are those logged above as proposed, awaiting Amish.
