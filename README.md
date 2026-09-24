# WaterWalker

**Area:** Mobility and Logistics · **Status:** Concept · **Prototype budget:** about $450 USD · **Difficulty:** 3 of 5

Four-wheel walk-inside water carrier. The user walks between large wheels, rollator style, pushing through a hip bar, while a low padded cradle holds four 20 L jerrycans or clay pots between the axles. Optional push-sensing hub motor assist for sand and slopes.

## Problem

Women and girls in rural sub-Saharan Africa and other low-income regions walk long distances carrying about 20 L of water on their heads per trip, which limits the quantity collected and causes neck and spine injuries. Design with, not for: requirements must come from co-design sessions and field trials with the intended users through a local partner.

## Concept

Four-wheel walk-inside water carrier. The user walks between large wheels, rollator style, pushing through a hip bar, while a low padded cradle holds four 20 L jerrycans or clay pots between the axles. Optional push-sensing hub motor assist for sand and slopes.

Full design precis: [docs/02-concept.md](docs/02-concept.md)

## Key components

- Steel tube frame (bent and bolted)
- Large-diameter wheels with puncture-proof tires (4)
- Hip and hand push bar
- Adjustable padded cradle for jerrycans or clay pots
- Parking brake
- Optional 250 W hub motor with push-force sensor
- Optional 36 V pack

The working bill of materials is in [bom/bom.csv](bom/bom.csv).

## Safety

> Rated load and slope limits must be marked on the frame. The brake must hold a full load on the steepest rated slope. Contains a lithium battery pack. Use a BMS with cell-level protection, fuse the pack, and charge on a non-combustible surface.

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

## Licenses

- **Hardware** (CAD, drawings, BOM, electronics): [CERN-OHL-S v2](LICENSE)
- **Software** (firmware, scripts, notebooks): [MIT](LICENSE-SOFTWARE)

Part of the open hardware portfolio at [amishchadha.com](https://amishchadha.com).
