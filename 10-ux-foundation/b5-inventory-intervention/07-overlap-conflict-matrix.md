# B5 — Overlap and Conflict Matrix

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

`Conflict` means incompatible effective truths are preserved and surfaced. The matrix does not invent a source/channel priority or automatic winner.

| Overlap | Can truths coexist as records? | Inventory Conflict? | Does one prevent creation of another? | Next responsibility | Must not happen automatically |
|---|---|---|---|---|---|
| Owner Block × Temporary Commitment | Yes, preserve both. | Yes if incompatible/effective. | Later intervention may be blocked or escalated under policy; no assumed precedence. | Inventory/exception owner. | Cancel Request, release hold or favor Owner silently. |
| Owner Block × Confirmed Stayora Commitment | Yes. | Yes if incompatible. | No automatic override. | Booking/Stay and Inventory exception contexts. | Cancel Booking, refund or relocate Guest. |
| Owner Block × External Commitment | Yes. | Yes if incompatible. | No automatic override. | Inventory + External/Stay exception owner. | Delete External Accommodation or choose channel winner. |
| Owner Block × Maintenance Block | Yes. | Potentially overlapping constraints; conflict if bases require incompatible action. | Policy may consolidate projection but B5 does not choose. | Inventory/Operations authority. | Treat Owner reason as Maintenance or vice versa. |
| Maintenance Block × Temporary Commitment | Yes. | Yes if incompatible. | No silent overwrite. | Inventory/Booking exception. | Cancel payment/Request or assign blame. |
| Maintenance Block × Confirmed Stayora Commitment | Yes. | Yes if incompatible. | No automatic cancellation. | Inventory + Booking/Stay exception. | Cancel Stay, refund or compensate automatically. |
| Maintenance Block × External Commitment | Yes. | Yes if incompatible. | No automatic deletion. | Inventory + External/Stay exception. | Remove external fact or choose external priority. |
| Maintenance Block × active/upcoming Stay | Yes as history/truth. | Potential conflict with operational accommodation. | No automatic Stay cancellation. | Stay/Operations + Inventory exception. | Check-out, cancel or relocate automatically. |
| External Commitment × Stayora Commitment | Yes, preserve sources. | Yes if incompatible. | No channel priority. | Inventory Conflict resolver where authorized. | Cancel either commitment silently. |

Exact coexistence semantics, remediation, release, compensation, refund, relocation and precedence remain policy/TBD. `Inventory Conflict` does not itself choose a commercial outcome.
