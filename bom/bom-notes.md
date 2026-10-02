# BOM notes

Every line in `bom/bom.csv` is priced (TRL 3). Prices are estimates for a one-off purchase in 2026 US dollars, with a supplier or supplier type; they are not quotes. Item numbers match the exploded view (`media/exploded.png`), the components table in WWK-PRC-001 and drawing WWK-DWG-001; items 12 and 14 are not modelled; item 15 is the parking lock pin; item 16 (headset and steering lock sets) was added when the design was made constructable (WWK-DDR-003). The totals below are printed by `docs/04-calcs/sizing.py` (WWK-CAL-001 v0.3).

| Build | Items | Parts cost |
| --- | --- | --- |
| First prototype, no assist, with mounting points | 1 to 5, 7, 8, 12, 14, 15, 16 | USD 462 |
| Optional assist kit (later prototype) | 9, 11, 13 | USD 260 |
| SwapCell pack | 10 | USD 0 here; about USD 414 in the SwapCell BOM |

- **Value-engineering target.** `budget_usd: 450` in `project.yaml` is a hypothetical control target, not a limit (Amish, 2026-10-01). Value-engineering target: USD 450. Estimated cost of the constructable design: USD 462 (USD 12 over the target). Cost drivers and savings worth trying are in the design decisions register (WWK-DEC-001).
- **Changes from WWK-DDR-003 (2026-10-02, design for construction).** Item 1 USD 55 to USD 61 (cradle carrier, second rear brackets, pin guides, guard tabs); item 3 USD 38 to USD 32 each (headset and swivel lock moved to item 16); item 5 USD 20 to USD 25 (angle brackets and bolts); item 8 USD 6 to USD 7 each (clips and bolts); item 12 USD 20 to USD 22; item 15 USD 5 to USD 6 (second tab, ball-lock pin); new item 16, four headset and steering lock sets at USD 8. Net USD 36.
- **Changes from WWK-DDR-002 (2026-09-25).** Amish accepted the remaining recommendations: the main tube wall drops from 1.5 to 1.2 mm (item 1), the cradle is thinner (item 5), and a parking lock pin is added (item 15).
- **Assist kit.** The motor, sensor and receiver (USD 260) are outside the first prototype. A value-engineering target for the assist prototype has not been set. Meeting R3 on loose sand would need a second motor kit (about USD 190 more).
- **Shared packs.** By Amish's 2026-09-25 portfolio rule, the SwapCell pack is priced once in the SwapCell BOM and excluded here.
- The jerrycans (item 6) are the users' own containers and are not purchased.
- All wear parts are standard 26 in bicycle parts (R12), but 100 mm drum hubs are less common in rural markets than rim-brake hubs, so R12 is at risk until checked with a local mechanic.
