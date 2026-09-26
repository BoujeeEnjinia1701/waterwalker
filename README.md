# WaterWalker

![TRL 3](https://img.shields.io/badge/TRL-3%20of%209-0F766E) ![Hardware: CERN-OHL-S-2.0](https://img.shields.io/badge/hardware-CERN--OHL--S--2.0-111827) ![Software: MIT](https://img.shields.io/badge/software-MIT-111827)

**Area:** Mobility and Logistics · **TRL:** 3 of 9 (proof of concept on paper) · **Prototype budget:** about $450 USD · **Difficulty:** 3 of 5

Four-wheel walk-inside water carrier. The user walks between large wheels, rollator style, pushing through a hip bar, while a low padded cradle holds four 20 L jerrycans or two clay pots between the axles. Mounting points for a later push-sensing hub motor assist for sand and slopes.

![WaterWalker concept](media/hero.png)

[Interactive 3D model](media/viewer.html) · [Concept blueprint (PDF)](media/concept-blueprint.pdf) · [General arrangement WWK-DWG-001 (PDF)](cad/drawings/WWK-DWG-001.pdf) · [Sizing calculations WWK-CAL-001](docs/04-calcs/01-sizing.md) · [Review note](docs/REVIEW.md)

## Concept rationale

Wheels move water far better than heads do, but the rolling drums and carts already in use struggle on sand, on slopes and in tight turns, and a one-wheeled barrow asks for lifting and balance. WaterWalker puts the user inside a four-wheeled frame, the way a rollator does, so she walks normally, pushes with her hips as well as her hands, and steers by turning her body. The load rides low between the axles, where it cannot tip onto her or strain her neck, and the carrier works with the 20 L jerrycans households already own.

The design is open (CERN-OHL-S) and garage-buildable because the people who would use it live far from any factory. Everything is mild steel tube that a village welder can cut and repair, plus standard 26 in bicycle wheels, forks, cables and drum hubs sold in rural markets. An open design lets a local partner change the cradle, the width or the brakes after co-design sessions without asking anyone's permission, and lets repairs happen where the carrier breaks.

## Burning platform

According to the [WHO](https://www.who.int/news-room/fact-sheets/detail/drinking-water), 2.2 billion people still lack safely managed drinking water services. Where water is not piped to the home, the carrying falls mostly on women: the 2023 WHO/UNICEF Joint Monitoring Programme report found that women and girls are primarily responsible for water collection in [7 out of 10 households](https://www.unicef.org/press-releases/women-and-girls-bear-brunt-water-and-sanitation-crisis-new-unicef-who-report) without water on the premises, and that 1.8 billion people live in such households.

The time lost is vast. [UNICEF estimates](https://www.unicef.org/press-releases/unicef-collecting-water-often-colossal-waste-time-women-and-girls) that women and girls spend 200 million hours every day collecting water, time taken from school, paid work and rest. Each head-carried trip moves a single 20 L container, about 20 kg.

## Where it could be used

### By industry

| Industry | Use |
| --- | --- |
| Rural water supply and WASH programmes | Last-mile carriage from boreholes, tap stands and water kiosks to homes, alongside new water points |
| Humanitarian response and refugee settlements | Moving water from distribution points to shelters over sandy or unpaved ground |
| Disaster response and civil protection | Carrying water from tanker trucks and supply points to homes while piped supply is cut |
| Smallholder farming | Watering seedlings and kitchen gardens, and moving produce or feed on footpaths |
| Schools and health posts without piped water | Bringing enough water for drinking, cooking and handwashing in fewer trips |

### By country or region

| Country or region | Why it matters there |
| --- | --- |
| Ethiopia | Only [49.6 % of people have basic water supply](https://www.unicef.org/ethiopia/water-sanitation-and-hygiene-wash), so many households walk to a water point on dirt paths in highlands and lowlands |
| Niger and the Sahel | Routes to wells and boreholes cross loose sand, the hardest case for any wheeled carrier and the one R3 targets |
| India (Rajasthan and other dry states) | Women in desert and semi-arid villages carry water from wells and tanks, and bicycles are a familiar vehicle that local mechanics already repair |
| Peru and Bolivia (Andean and peri-urban hillsides) | Households without piped supply carry water up steep paths, where the brake, parking lock and slope limits matter |
| Japan (Noto Peninsula) | After the January 2024 Noto earthquake [more than 110,000 households were left without water](https://en.wikipedia.org/wiki/2024_Noto_earthquake), some for months, and in Shika water was rationed at six litres per person a day |

## What sparked the idea

The idea traces back to the rollator, the four-wheeled walking frame that the Swedish inventor [Aina Wifalk](https://en.wikipedia.org/wiki/Aina_Wifalk) presented in 1978 after polio had limited her own mobility. She chose not to patent it so that it could reach as many disabled people as possible, and today people of almost any age walk inside one without training. WaterWalker borrows that stance, walking inside a wheeled frame and pushing with the body, and her open approach, and applies both to the 20 L jerrycan instead of a person's own weight.

## Problem

Women and girls in rural sub-Saharan Africa and other low-income regions walk long distances carrying about 20 L of water on their heads per trip, which limits the quantity collected and causes neck and spine injuries. Design with, not for: requirements must come from co-design sessions and field trials with the intended users through a local partner.

## Concept

Four-wheel walk-inside water carrier. The user walks between large wheels, rollator style, pushing through a hip bar, while a low padded cradle holds four 20 L jerrycans or two clay pots between the axles. Mounting points for a later push-sensing hub motor assist for sand and slopes.

At TRL 3 the sizing calculations (WWK-CAL-001 v0.2) show the first prototype is easy to push on firm ground (24 to 60 N) and turns in 3.7 m. With the lighter main tube and cradle that Amish accepted on 2026-09-25 (WWK-DDR-002), two requirements are still not met on paper: loose sand (236 to 358 N against 150 N) and empty mass (37.4 kg against 35 kg). The first prototype has no assist but keeps mounting points for a kit built to SwapCell interface v0.3, parks with a positive lock pin, and its parts are about $426 against the $450 budget.

Full design precis: [docs/02-concept.md](docs/02-concept.md)

## Key components

- Welded mild steel tube frame with assist mounting points
- 26 in bicycle wheels in rigid forks, with puncture-resistant tires (4); front forks swivel
- Hip and hand push bar
- Padded cradle for four jerrycans or two clay pots
- Rear drum brakes with a lever latch for short stops, and a parking lock pin
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

A project of the [Design Molecule](https://designmolecule.com) lab.
