# B4 — Stay and Inventory Relationship

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Separate sources of truth

| Concern | Canonical owner | B4 rule |
|---|---|---|
| Stay lifecycle | Stay | Check-in, Checkout and completion are Stay truth. |
| Inventory availability | Inventory derived model | Availability derives from effective Inventory Commitments and Blocks, not Stay display state. |
| Accommodation provenance | Booking or External Accommodation | Stay retains the legitimate basis/source. |
| Operational readiness | Stay/Operations projection | Readiness may be reported without `READY` Stay state. |
| Payment/settlement | Money/Settlement | Payment or completion does not silently become one another. |

## Protected non-transitions

- Check-in does not create an Inventory Commitment.
- Checkout does not release Inventory merely because a UI event was recorded.
- Completion does not make a Unit Available; effective commitment/block semantics determine Availability.
- A Butler incident report does not create a Maintenance Block or commercial restriction by itself.
- A Stay does not overwrite a Booking, External Accommodation fact or Inventory source of truth.

Operational events may be consumed by a separately authorized Inventory or policy workflow where canonical rules support it. B4 does not start B5 or choose that policy.
