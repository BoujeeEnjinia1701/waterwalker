# BOM notes

Every line in `bom/bom.csv` is priced (TRL 3). Prices are estimates for a one-off purchase in 2026 US dollars, with a supplier or supplier type; they are not quotes. Item numbers match the exploded view (`media/exploded.png`), the components table in WWK-PRC-001 and drawing WWK-DWG-001; items 12 and 14 are not modelled; item 15 is the parking lock pin. The totals below are printed by `docs/04-calcs/sizing.py` (WWK-CAL-001).

| Build | Items | Parts cost |
| --- | --- | --- |
| First prototype, no assist, with mounting points | 1 to 5, 7, 8, 12, 14, 15 | $426 |
| Optional assist kit (later prototype) | 9, 11, 13 | $260 |
| SwapCell pack | 10 | $0 here; about $414 in the SwapCell BOM |

- **Budget.** Amish decided on 2026-09-25 to keep `budget_usd: 450` for the first prototype without assist but with mounting points (WWK-DDR-001, WWK-REQ-001 R11). The first prototype is $426, a margin of $24, so R11 is met.
- **Changes from WWK-DDR-002 (2026-09-25).** Amish accepted the remaining recommendations: the main tube wall drops from 1.5 to 1.2 mm (item 1, $60 to $55), the cradle is thinner (item 5, $24 to $20), and a parking lock pin is added (item 15, $5).
- **Assist kit.** The motor, sensor and receiver ($260) are outside the first-prototype budget. A budget for the assist prototype has not been set and is for Amish to decide. Meeting R3 on loose sand would need a second motor kit (about $190 more).
- **Shared packs.** By Amish's 2026-09-25 portfolio rule, the SwapCell pack is priced once in the SwapCell BOM and excluded from this budget.
- **Changes since TRL 2.** The TRL 2 total of about $300 left out the tires, tubes and liners (item 14, $96) and the rear forks. Rear wheels now sit in fixed forks with 100 mm drum hubs (item 2), the frame uses heavier tube and carries the assist mounting points (item 1), and the hub motor is now a 48 V unit to match SwapCell's 46.8 V pack (item 9).
- The jerrycans (item 6) are the users' own containers and are not purchased.
- All wear parts are standard 26 in bicycle parts (R12), but 100 mm drum hubs are less common in rural markets than rim-brake hubs, so R12 is at risk until checked with a local mechanic.
