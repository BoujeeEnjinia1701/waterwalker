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

1. First co-design partner and region (no recommendation; per area later).
2. Dead-man brake (no recommendation until users are asked).
3. Rear wheels in fixed rigid forks with 100 mm drum hubs and a 770 mm track. Recommended; already in the model.
4. Front risers moved to x = 1,150 mm, wheelbase 1,530 mm, cradle 780 mm. Recommended; already in the model.
5. Main tube 40 x 30 x 1.5 mm. Recommended; already in the model.
6. Mass: apply the thinner cradle and 1.2 mm main-tube wall (35.6 kg with all four options, still over 35 kg), and revisit R9 with users. Recommended.
7. Parking: add a positive lock pin. Recommended.
8. Budget for the later assist prototype (kit $260, or about $450 with two motors, plus a shared pack). No recommendation.

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
