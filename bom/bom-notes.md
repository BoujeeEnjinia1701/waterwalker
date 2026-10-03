# BOM notes

Every line in `bom/bom.csv` is priced (TRL 3). Prices are estimates for a one-off purchase in 2026 US dollars, with a supplier or supplier type; they are not quotes. Item numbers match the exploded view (`media/exploded.png`), the components table in WWK-PRC-001 and drawing WWK-DWG-001; items 12 and 14 are not modelled; item 15 is the parking lock pin; item 16 (headset and steering lock sets) was added when the design was made constructable (WWK-DDR-003); item 17 (hold-to-release brake) was added when Amish's decisions of 2026-10-02 were carried into the design; the rating plates in item 12 are modelled. The totals below are printed by `docs/04-calcs/sizing.py` (WWK-CAL-001 v0.4).

| Build | Items | Parts cost |
| --- | --- | --- |
| First prototype, no assist, with mounting points | 1 to 5, 7, 8, 12, 14 to 17 | USD 492 |
| Optional two-motor assist kit (later prototype) | 9 (two), 11, 13 | USD 450 |
| SwapCell pack | 10 | USD 0 here; about USD 414 in the SwapCell BOM |

- **Value-engineering target.** `budget_usd: 450` in `project.yaml` is a hypothetical control target, not a limit (Amish, 2026-10-01). Value-engineering target: USD 450. Estimated cost of the constructable design: USD 492 (USD 42 over the target). Cost drivers and savings worth trying are in the design decisions register (WWK-DEC-001).
- **Changes from the decisions of 2026-10-02.** New item 17, hold-to-release brake, USD 30 (bail lever about USD 8 as a long bicycle or mower-style lever; tube, end caps and toggle about USD 8 from a welder; spring about USD 4 from a spring stockist; cable yoke about USD 5; cables and housing about USD 5); item 7 USD 20 to USD 16 (the splitter is replaced by the yoke in item 17); item 1 USD 61 to USD 62 (second torque-arm tab and the spring unit tab); item 12 USD 22 to USD 25 (two rating plates from a local sign maker); item 9 quantity 1 to 2 (two-motor assist kit). Net USD 30 on the first prototype; USD 190 on the assist kit.
- **Changes from WWK-DDR-003 (2026-10-02, design for construction).** Item 1 USD 55 to USD 61 (cradle carrier, second rear brackets, pin guides, guard tabs); item 3 USD 38 to USD 32 each (headset and swivel lock moved to item 16); item 5 USD 20 to USD 25 (angle brackets and bolts); item 8 USD 6 to USD 7 each (clips and bolts); item 12 USD 20 to USD 22; item 15 USD 5 to USD 6 (second tab, ball-lock pin); new item 16, four headset and steering lock sets at USD 8. Net USD 36.
- **Changes from WWK-DDR-002 (2026-09-25).** Amish accepted the remaining recommendations: the main tube wall drops from 1.5 to 1.2 mm (item 1), the cradle is thinner (item 5), and a parking lock pin is added (item 15).
- **Assist kit.** The two motors, sensor and receiver are outside the first prototype. Meeting R3 on loose sand needs two motors, so Amish set the assist prototype's value-engineering target at about USD 450 for the two-motor kit, pack excluded (2026-10-02, WWK-DEC-001). Value-engineering target: USD 450. Estimated cost of the two-motor kit: USD 450 (on the target). The USD 260 one-motor kit is used only if sand trials show one motor meets R3.
- **Shared packs.** By Amish's 2026-09-25 portfolio rule, the SwapCell pack is priced once in the SwapCell BOM and excluded here.
- The jerrycans (item 6) are the users' own containers and are not purchased.
- All wear parts are standard 26 in bicycle parts (R12), but 100 mm drum hubs are less common in rural markets than rim-brake hubs, so R12 is at risk until checked with a local mechanic.
