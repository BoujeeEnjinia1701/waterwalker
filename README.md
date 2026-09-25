# WaterWalker

![TRL 3](https://img.shields.io/badge/TRL-3%20of%209-0F766E) ![Hardware: CERN-OHL-S-2.0](https://img.shields.io/badge/hardware-CERN--OHL--S--2.0-111827) ![Software: MIT](https://img.shields.io/badge/software-MIT-111827)

**Area:** Mobility and Logistics · **TRL:** 3 of 9 (proof of concept on paper) · **Prototype budget:** about $450 USD · **Difficulty:** 3 of 5

Four-wheel walk-inside water carrier. The user walks between large wheels, rollator style, pushing through a hip bar, while a low padded cradle holds four 20 L jerrycans or two clay pots between the axles. Mounting points for a later push-sensing hub motor assist for sand and slopes.

![WaterWalker concept](media/hero.png)

[Interactive 3D model](media/viewer.html) · [Concept blueprint (PDF)](media/concept-blueprint.pdf) · [General arrangement WWK-DWG-001 (PDF)](cad/drawings/WWK-DWG-001.pdf) · [Sizing calculations WWK-CAL-001](docs/04-calcs/01-sizing.md) · [Review note](docs/REVIEW.md)

## Problem

Women and girls in rural sub-Saharan Africa and other low-income regions walk long distances carrying about 20 L of water on their heads per trip, which limits the quantity collected and causes neck and spine injuries. Design with, not for: requirements must come from co-design sessions and field trials with the intended users through a local partner.

## Concept

Four-wheel walk-inside water carrier. The user walks between large wheels, rollator style, pushing through a hip bar, while a low padded cradle holds four 20 L jerrycans or two clay pots between the axles. Mounting points for a later push-sensing hub motor assist for sand and slopes.

At TRL 3 the sizing calculations (WWK-CAL-001) show the first prototype is easy to push on firm ground and turns in 3.7 m, but four requirements are not met on paper: firm-ground and 10 % climb push force (just over target), loose sand (242 to 368 N against 150 N) and empty mass (40.8 kg against 35 kg). The first prototype has no assist but keeps mounting points for a kit built to SwapCell interface v0.3; its parts are about $430 against the $450 budget.

Full design precis: [docs/02-concept.md](docs/02-concept.md)

## Key components

- Welded mild steel tube frame with assist mounting points
- 26 in bicycle wheels in rigid forks, with puncture-resistant tires (4); front forks swivel
- Hip and hand push bar
- Padded cradle for four jerrycans or two clay pots
- Rear drum brakes with a parking latch
- Later, optional: 250 W, 48 V hub motor with push-force sensor
- Later, optional: SwapCell pack (interface v0.3) in a class V1 receiver

The working bill of materials is in [bom/bom.csv](bom/bom.csv).

## Safety

> Rated load and slope limits must be marked on the frame. The brake must hold a full load on the steepest rated slope; on loose ground the rear tires may slide before the brake slips. The later assist kit contains a lithium battery pack: use a SwapCell pack with its BMS, cell-level protection and fuse, and charge it in a dock on a non-combustible surface.

## Repository layout

| Folder | Contents |
| --- | --- |
| `docs/` | Problem, concept, requirements, calculations and design decisions |
| `cad/src/` | build123d Python source, the source of truth for all geometry |
| `cad/step/`, `cad/stl/` | Exported models for FreeCAD, other CAD tools and printing |
| `cad/drawings/` | 2D sketches and dimensioned drawings |
| `bom/` | Bill of materials |
| `electronics/` | KiCad schematics and PCB layouts |
| `firmware/` | Microcontroller code |
| `media/` | Renders, perspectives and photos |
| `build-log/` | Dated prototyping notes |

## Documentation

Controlled documents follow the portfolio [documentation standard](.kit/STANDARDS.md). Each carries a document ID (WWK-PRC-001 for the precis), a version and a revision history. Branded PDFs are built with `python .kit/render.py` and attached to GitHub Releases when a document is tagged, for example `WWK-PRC-001/v1.0`.

## Licenses

- **Hardware** (CAD, drawings, BOM, electronics): [CERN-OHL-S v2](LICENSE)
- **Software** (firmware, scripts, notebooks): [MIT](LICENSE-SOFTWARE)

Part of the open hardware portfolio at [amishchadha.com](https://amishchadha.com).
