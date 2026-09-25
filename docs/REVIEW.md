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
