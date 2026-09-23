# Sale Workspace — Task Architecture

**Surface:** Sale Workspace · **V0:** MUST BUILD Sale-assisted booking and approved Sale relationship outcomes.

| ID | Task | Type | Structural home | Authority boundary |
|---|---|---|---|---|
| SAL-T1 | Find supply truthful for Guest dates and intent | Primary | `SAL-01 Supply Discovery` | Active Distribution Relationship + scope; no Inventory mutation |
| SAL-T2 | Prepare/share an accommodation option | Primary | `SAL-02 Option & Offer Context` | Permitted commercial information; no invented quote policy |
| SAL-T3 | Capture Guest intent and create a Booking Request | Primary | `SAL-03 Request Entry` | Sale may initiate; Host/authorized Co-host decides |
| SAL-T4 | Track Request outcome and confirmed result | Primary | `SAL-04 Sale Activity & Outcome` | Projection only; Booking remains canonical |
| SAL-T5 | Understand permitted attribution/earnings outcome | Supporting | `SAL-05 Attribution & Earnings Summary` | Attribution ≠ commission entitlement ≠ settlement/payout |
| SAL-T6 | Resolve a Sale-relevant exception | Attention/manual-assisted | `SAL-04` or `SAL-06 Sale Exception` | No CRM/lead suite; escalate to responsible authority |

No Sale screen grants Booking, Inventory, Stay or Owner-economic authority. Affiliate network and advanced CRM remain OUT OF SCOPE — V0.
