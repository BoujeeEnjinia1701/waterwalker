# WaterWalker

![TRL 3](https://img.shields.io/badge/TRL-3%20of%209-0F766E) ![Hardware: CERN-OHL-S-2.0](https://img.shields.io/badge/hardware-CERN--OHL--S--2.0-111827) ![Software: MIT](https://img.shields.io/badge/software-MIT-111827) [![DOI](https://zenodo.org/badge/1386426481.svg)](https://zenodo.org/badge/latestdoi/1386426481) [![REUSE compliant](https://github.com/BoujeeEnjinia1701/waterwalker/actions/workflows/reuse.yml/badge.svg)](https://github.com/BoujeeEnjinia1701/waterwalker/actions/workflows/reuse.yml) [![Archived in Software Heritage](https://archive.softwareheritage.org/badge/origin/https://github.com/BoujeeEnjinia1701/waterwalker/)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/BoujeeEnjinia1701/waterwalker)

**Area:** Mobility and Logistics · **TRL:** 3 of 9 (proof of concept on paper) · **Value-engineering target:** USD 450 (estimated USD 492) · **Difficulty:** 3 of 5

Four-wheel walk-inside water carrier. The user walks between large wheels, rollator style, pushing through a hip bar, while a low padded cradle holds four 20 L jerrycans or two clay pots between the axles. Mounting points for a later push-sensing hub motor assist for sand and slopes.

![WaterWalker: walk-inside four-wheel water carrier, product render](media/render-hero.png)

[Exploded render](media/render-exploded.png) · [Detail render](media/render-detail.png) · [Interactive 3D model](media/viewer.html) · [Concept blueprint (PDF)](media/concept-blueprint.pdf) · [General arrangement WWK-DWG-001 (PDF)](cad/drawings/WWK-DWG-001.pdf) · [Sizing calculations WWK-CAL-001](docs/04-calcs/01-sizing.md) · [Prototype build plan WWK-BLD-001](docs/05-build-plan.md) · [Design decisions register WWK-DEC-001](docs/06-design-decisions.md) · [Review note](docs/REVIEW.md)

## Concept rationale

Wheels move water far better than heads do, but the rolling drums and carts already in use struggle on sand, on slopes and in tight turns, and a one-wheeled barrow asks for lifting and balance. WaterWalker puts the user inside a four-wheeled frame, the way a rollator does, so she walks normally, pushes with her hips as well as her hands, and steers by turning her body. The load rides low between the axles, where it cannot tip onto her or strain her neck, and the carrier works with the 20 L jerrycans households already own.

The design is open (CERN-OHL-S) and garage-buildable because the people who would use it live far from any factory. Everything is mild steel tube that a village welder can cut and repair, plus standard 26 in bicycle wheels, forks, cables and drum hubs sold in rural markets. An open design lets a local partner change the cradle, the width or the brakes after co-design sessions without asking anyone's permission, and lets repairs happen where the carrier breaks.

## Burning platform

According to the [WHO](https://www.who.int/news-room/fact-sheets/detail/drinking-water), 2.2 billion people still lacked safely managed drinking water services in 2022. Where water is not piped to the home, the carrying falls mostly on women: the 2023 WHO/UNICEF Joint Monitoring Programme report found that women and girls are primarily responsible for water collection in [7 out of 10 households](https://www.unicef.org/press-releases/women-and-girls-bear-brunt-water-and-sanitation-crisis-new-unicef-who-report) without water on the premises, and that 1.8 billion people live in such households.

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
| Niger | [Only 56 % of the population has access to a source of drinking water](https://www.unicef.org/niger/water-sanitation-and-hygiene), so the rest must carry water from a source farther away |
| India | [Close to 54 % of rural women spend an estimated 35 minutes getting water every day](https://www.unicef.org/india/what-we-do/clean-drinking-water), equivalent to 27 days' lost wages a year, and less than 49 % of rural people use safely managed drinking water |
| Peru (hillside settlements of peri-urban Lima) | About 350 tanker trucks a day supply some 250,000 homes on the outskirts of Lima, and [a hillside household gets about 1,100 L of water a month](https://www.sciencedirect.com/science/article/pii/S2667010025003051) from tanks and trucks rather than household taps; on steep paths the brake, parking lock and slope limits matter |
| Japan (Noto Peninsula) | The January 2024 Noto earthquake [left up to 135,000 households without running water](https://www.japantimes.co.jp/news/2024/02/23/japan/society/noto-quake-sparks-water-debate/), and nearly 24,000 homes in Ishikawa Prefecture were still without water seven weeks later |

## What sparked the idea

The idea traces back to the rollator, the four-wheeled walking frame whose prototype the Swedish inventor Aina Wifalk designed in 1978 while working at an orthopedic clinic in Västerås, after polio had limited her own mobility ([Swedish Institute](https://sharingsweden.se/materials/the-invention-of-the-walker)). She never patented it, so that it could reach as many people as possible ([Svenskt UppfinnareMuseum](https://svensktuppfinnaremuseum.se/aina-wifalk/)), and today people of almost any age walk inside one without training. WaterWalker borrows that stance, walking inside a wheeled frame and pushing with the body, and her open approach, and applies both to the 20 L jerrycan instead of a person's own weight.

## Problem

Women and girls in rural sub-Saharan Africa and other low-income regions walk long distances carrying about 20 L of water on their heads per trip, which limits the quantity collected and causes neck and spine injuries. Design with, not for: requirements must come from co-design sessions and field trials with the intended users through a local partner.

## Concept

Four-wheel walk-inside water carrier. The user walks between large wheels, rollator style, pushing through a hip bar, while a low padded cradle holds four 20 L jerrycans or two clay pots between the axles. Mounting points for a later push-sensing hub motor assist for sand and slopes.

At TRL 3 the design is constructable: every part can be cut, welded, bought and fitted, and the build plan (WWK-BLD-001) shows how. Making it buildable added a cradle carrier, two-level rear head tube brackets, headsets and steering locks at all four forks and the fixings the concept lacked (WWK-DDR-003, accepted by Amish on 2026-10-02). His decisions of that day added a hold-to-release brake (let go of the bail under the left grip and a spring applies both rear brakes), a torque-arm tab on each rear fork for a two-motor assist kit, rated load and slope plates and hand holds in the cradle walls, which raised the empty mass to 40.3 kg. The sizing calculations (WWK-CAL-001 v0.4) show the carrier turns in 3.7 m and lifts containers only 364 mm, but four requirements are not met on paper: firm-path push (61.2 N against 60 N), loose sand (241 to 367 N against 150 N), the 10 % climb (182.6 N against 180 N) and empty mass (40.3 kg against 35 kg). The first prototype has no assist but keeps mounting points for a kit built to SwapCell interface v0.3, and parks with a positive lock pin. Value-engineering target: USD 450. Estimated cost of the constructable design: USD 492 (USD 42 over the target).

Full design precis: [docs/02-concept.md](docs/02-concept.md)

## Key components

- Welded mild steel tube frame with a cradle carrier and assist mounting points
- 26 in bicycle wheels in rigid forks on headsets, with puncture-resistant tires (4); front forks swivel and pin straight, rear forks are pinned straight
- Hip and hand push bar
- Padded plywood cradle for four jerrycans or two clay pots, bolted to two steel bearers
- Rear drum brakes with a lever latch for short stops, a hold-to-release brake and a parking lock pin
- Later, optional: two 250 W, 48 V hub motors with push-force sensor
- Later, optional: SwapCell pack (interface v0.3) in a class V1 receiver

The working bill of materials is in [bom/bom.csv](bom/bom.csv).

## Building the prototype

![WaterWalker prototype: every component pulled apart and numbered in build order](docs/05-build-plan/overview.png)

The [prototype build plan](docs/05-build-plan.md) (WWK-BLD-001) takes a welder and a bicycle mechanic through the first prototype component by component, with a making sketch for each of the eight made components, close-ups of the joints and a picture for every assembly step. The frame is welded from mild steel tube on a flat floor; the forks, wheels, headsets and brakes are standard 26 in bicycle parts; the cradle is plywood bolted to two steel bearers. It is a plan, not yet built: building and testing to it is TRL 4 work, and the decisions, all made as of 2026-10-02, are in the [design decisions register](docs/06-design-decisions.md).

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

## Credits

Designed by Amish Chadha. See [CONTRIBUTORS.md](CONTRIBUTORS.md) for roles. To cite this design, use [CITATION.cff](CITATION.cff) (GitHub shows it as "Cite this repository").

AI assistance (Claude) was used to accelerate concept renders, prototype documentation and first-pass sizing calculations. Design direction and all decisions are Amish Chadha's, recorded in this repository's decision records (`docs/decisions/`).

## Licenses

- **Hardware** (CAD, drawings, BOM, electronics): [CERN-OHL-S v2](LICENSE)
- **Software** (firmware, scripts, notebooks): [MIT](LICENSE-SOFTWARE)

A project of the [Design Molecule](https://designmolecule.com) lab.
