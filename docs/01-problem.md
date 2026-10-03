---
doc_id: WWK-PRB-001
title: WaterWalker problem statement
project: WaterWalker
doc_type: Problem statement
version: "0.5"
status: Draft
date: '2026-10-02'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-24'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-09-24'
  author: Amish Chadha
  change: Populate to TRL 2 (users, context, constraints, prior work, co-design first)
- version: "0.3"
  date: '2026-09-25'
  author: Amish Chadha
  change: TRL 3. Record Amish's decisions (WWK-DDR-001) on the budget scope, the cradle and the co-design partner; add the questions raised by WWK-CAL-001
- version: "0.4"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); co-design questions updated for the lighter carrier and the parking lock pin
- version: "0.5"
  date: '2026-10-02'
  author: Amish Chadha
  change: Partner and region answered by Amish's decision of 2026-10-02 (WWK-DEC-001)
---

# WaterWalker problem statement

Women and girls in rural sub-Saharan Africa and other low-income regions walk long distances carrying about 20 L of water on their heads per trip, which limits the quantity collected and causes neck and spine injuries. Design with, not for: requirements must come from co-design sessions and field trials with the intended users through a local partner.

## Co-design comes first

This design is for communities the author is not part of. Every number in this repo is a desk estimate until the women and girls who carry water have shaped it. Co-design is the first piece of work, not a final check, and it can change the concept, including whether a wheeled carrier is wanted at all.

## User research and co-design

This design is for communities the author is not part of, so requirements come from the people who will use it.

- [ ] Identify a local partner organization (Helpful Engineering network, NGO or university)
- [ ] Run co-design sessions with intended users; record who, where and what was learned
- [ ] Validate load, distance, terrain and cost assumptions in the field
- [ ] Revise requirements (REQ) from findings before freezing the design

Partner and region: decided by Amish on 2026-10-02 (WWK-DEC-001). The Helpful Engineering network is the route to a first partner, a university engineering department or water and sanitation NGO in semi-arid eastern Kenya; Kitui County is the first candidate region. None has been approached yet.

Questions to bring to the first sessions:

- Which containers are used: jerrycans, clay pots, buckets or a mix, and how often each?
- Who fetches water, at what times, with whom, and would a shared carrier work for several households?
- What are the paths like: width, sand, slopes, steps, ditches, stream crossings?
- Where would the carrier be stored at night, and who would repair it?
- Is pushing a wheeled carrier socially acceptable for women and girls, and does anything about its look or use carry stigma or risk (for example theft or being taken over by others)?
- What would a household or women's group pay, and would it be bought, shared or rented?
- Added at TRL 3 (WWK-CAL-001): How heavy a carrier can users lift over a step or ditch when empty (the design is about 37 kg)? How long are the sandy stretches on the route, and would users carry two jerrycans there and make two passes? Is the parking lock pin, pushed through the rear spokes, easy to use and remember to pull before moving off (WWK-DDR-002)? Is 37 kg empty acceptable, or must R9 (35 kg) hold? Would users want a brake that applies when they let go (a dead-man brake)?

## The problem

Where there is no piped supply at home, water is carried from a borehole, tap stand, well or river. The load is usually a 20 L jerrycan or clay pot on the head, about 20 kg of water per trip. Carrying this every day places a large compressive load on the neck and spine and is associated with pain and musculoskeletal injury. Because one person can only carry one container, the household's water use is limited by the number of trips, and the time spent walking and queueing falls mostly on women and girls, often at the expense of school, paid work and rest.

A household of five using about 20 L per person per day (a commonly used basic-access figure) needs about 100 L per day, which is five head-carried trips. Wheels can move several containers per trip, but existing rolling carriers struggle in exactly the places where the walk is hardest: loose sand, slopes and narrow, uneven paths.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Women and girls who fetch water (primary) | Bring home more water in fewer trips with less strain on the neck and back, on the paths they already use | Daily trips of about 1 to 6 km round trip, often more than once a day; walking in long skirts or wraps; sometimes with a child on the back |
| Household | Enough water for drinking, cooking, washing and hygiene | Rural homestead, 4 to 8 people |
| Women's group or community water committee | A carrier that can be shared, kept working and repaired locally | Village or cluster of homesteads |
| Local bicycle mechanic or welder | Parts and repairs they already know how to do | Market town workshop |
| Partner organization | An open design that can be adapted, built and trialled locally | NGO, university or maker network |

## Constraints

- Garage-buildable first prototype, about $450 USD (`project.yaml`). Amish decided on 2026-09-25 that this budget covers the first prototype without assist but with mounting points for it; the assist kit is a later prototype, and a SwapCell pack, if used, is priced once in the SwapCell project (WWK-DDR-001).
- Terrain: dirt footpaths with ruts, roots and stones; loose sand in dry riverbeds and sandy regions; slopes of about 10 % on routes to water points, occasionally steeper for short distances.
- Narrow paths: many footpaths and gates are under 1 m wide, and some are narrower.
- Walking, not riding: no balance or riding skill needed, usable on slopes and in long skirts, and culturally acceptable for women and girls of all ages.
- Containers: must carry the users' own 20 L jerrycans (four per trip), and should accept clay pots, which are heavy and fragile (two per trip, decided 2026-09-25).
- Local repair: wear parts must be standard bicycle parts sold in rural markets, and the frame must be mild steel that a local welder can repair.
- Storage: small enough to keep inside or beside a house at night.
- Optional electric assist must be removable, and the carrier must work fully without it.

## Prior work

- **Head carrying** remains the most common method. It needs no equipment and works on any path, but limits each trip to about 20 L.
- **Hippo Roller.** A rolling drum of about 90 L pushed or pulled with a steel handle. It moves far more water per trip than head carrying and is widely deployed. Reported weaknesses include high effort on sand and uphill, difficulty turning because the drum must be skidded sideways, control on descents, and cost for a single household.
- **Wello WaterWheel.** A rolling container of about 45 L pushed with a handle, designed in India. It shares the rolling-drum approach and, with it, the same limits on sand, slopes and turning.
- **Bicycles loaded with jerrycans.** Common in East Africa: several jerrycans hung on a bicycle that is pushed by hand. It shows that standard bicycle wheels and parts are accepted and repairable locally, but the load sits high and the bicycle is unstable when pushed.
- **Wheelbarrows and hand carts.** Available and familiar, but one-wheeled barrows need lifting and balance, and carts are wide and heavy.
- **Lopifit walking bike.** A Dutch walking bike on which the rider walks on a treadmill between the wheels, with a motor driving the bike. It inspired the walk-inside layout. WaterWalker deliberately has no treadmill: a treadmill needs a motor to be useful and wastes energy on rough ground.
- **Rollators.** Walking frames where the user stands inside a U-frame and pushes. They show that walking inside a wheeled frame is intuitive and needs no training.

## Out of scope

- Water treatment, storage at home and water source development.
- Pedalled or ridden vehicles, and anything that carries people.
- Animal-drawn or motor vehicles for road use.
- Large-scale manufacturing and distribution, which depend on a partner and on co-design results.

## Open questions

- Which partner and which region for the first co-design sessions? Decided by Amish, 2026-10-02 (WWK-DEC-001): through the Helpful Engineering network, with Kitui County, Kenya, as the first candidate region.
- How common are clay pots relative to jerrycans in the first region, and what size are they? The cradle takes two pots of up to about 384 mm diameter (WWK-CAL-001).
- What path width must the carrier fit? Proposed target 0.9 m, awaiting field data.
