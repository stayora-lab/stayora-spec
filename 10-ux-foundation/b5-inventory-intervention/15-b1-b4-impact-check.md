# B5 — B1–B4 Impact Check

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Accepted journey | B5 relationship | Preserved truth | No silent change |
|---|---|---|---|
| B1 Sale-assisted Booking | Owner/Maintenance Block may affect discovery, Request progression or a confirmed accommodation commitment. | Request, Temporary Commitment, Booking and Confirmed Accommodation Commitment remain distinct. | No Sale cancellation authority, no automatic Booking cancellation, no channel priority. |
| B2 External Booking → Stay | External Fact/Commitment may overlap a Block or other commitment. | External provenance and External Accommodation/Stay remain intact. | No fake Stayora Booking, external deletion or automatic commission. |
| B3 Direct Guest Booking | Derived Availability/Bookability may change before/after Guest Request. | Same Request/Inventory/Payment/Booking truth; no second direct inventory model. | No automatic Instant Book, no false confirmation, no Guest intent reservation. |
| B4 Stay Operations | Operational evidence may reveal unusable condition and initiate handoff. | Incident/Stay and Inventory remain separate. | No Butler/BQL Inventory Authority, no Incident→Block, no Check-in/Checkout/Completion Availability control. |

## Contradiction test

No B1–B4 architecture requires a generic Availability boolean or a commerce-origin-specific inventory lifecycle. Any future implementation that needs one must be escalated as a contradiction rather than silently added.
