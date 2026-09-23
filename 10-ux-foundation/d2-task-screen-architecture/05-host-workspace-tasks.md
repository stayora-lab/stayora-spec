# Host Workspace — Task Architecture

**Surface:** Host Workspace · **V0:** MUST BUILD property, request, inventory, booking, stay and operational responsibility; MANUAL-ASSISTED exceptions where CP5 says so.

| ID | Task | Type | Anchor | Structural home | Action posture |
|---|---|---|---|---|---|
| HST-T1 | Understand current Property/Unit responsibility and attention | Primary | Property, Unit, attention projections | `HST-01 Responsibility Overview` | Scope/authority checked |
| HST-T2 | Decide whether to accept or reject a Booking Request | Primary | Booking Request | `HST-03 Request Collection` → `HST-04 Request Detail` | Host/authorized Co-host only |
| HST-T3 | Understand resulting Inventory, Payment and Booking truth | Primary | Request, Commitment, Payment truth, Booking | `HST-04` / `HST-05 Booking Detail` | No collapse of domains |
| HST-T4 | Understand upcoming/current Stays and coordinate operations | Primary | Stay | `HST-06 Stay Collection` → `HST-07 Stay Detail` | Host responsibility only |
| HST-T5 | Record External Accommodation or external fact when authorized | Primary/manual-assisted | External Accommodation, Inventory effect | `HST-08 External Accommodation Entry` | Authorized recorder; no Stayora Booking implied |
| HST-T6 | Evaluate/record an Owner Block or authorized operational block | Primary/manual-assisted | Inventory Commitment/Block | `HST-09 Inventory Intervention` | Explicit authority and policy |
| HST-T7 | Respond to operational evidence requiring Inventory decision | Attention | Incident/Finding + Inventory | `HST-10 Incident & Inventory Exception` | Consequence authority remains separate |
| HST-T8 | Coordinate Butler/Stay operations | Supporting | Butler Assignment, Stay | `HST-07` / `HST-11 Operations Coordination` | Assignment/authority scoped |
| HST-T9 | View authorized Money truth | Supporting | Payment/Entitlement/Settlement/Payout projections | `HST-12 Money & Reconciliation` | Need-to-know; policy unresolved |
| HST-T10 | Maintain Property/Unit representation/readiness/publication outcome | Supporting/manual-assisted | Property, Unit, Verification/quality | `HST-02 Property & Unit` | Publication and verification policies apply |

No calendar is a second inventory calculator. No Host view makes Owner authority universal; see [Owner perspective](06-owner-perspective-tasks.md).
