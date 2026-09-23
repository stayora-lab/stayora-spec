# Operations — Destination / BQL Context: Task Architecture

**Surface:** Operations—Destination/BQL · **V0:** MUST BUILD destination-scoped operational awareness and legitimate access/services.

| ID | Task | Type | Structural home | Authority boundary |
|---|---|---|---|---|
| BQL-T1 | Understand today's arrivals/departures | Primary | `BQL-01 Operations Today` | Destination/function scope |
| BQL-T2 | Understand active Stays and relevant external coverage | Primary | `BQL-02 Stay Operations Collection` | Need-to-know; no Booking ownership |
| BQL-T3 | Inspect operational exception/Incident | Attention | `BQL-03 Incident & Exception` | Escalate to responsible authority |
| BQL-T4 | Support legitimate local access/services | Supporting/manual-assisted | `BQL-04 Access & Services Context` | Canonical destination policy only |
| BQL-T5 | Coordinate within actual destination authority | Supporting | `BQL-01`/`BQL-03` | No super-admin, Host, Inventory or Butler workforce authority |

BQL is not a Host dashboard, Booking manager, Inventory controller or workforce suite.
