# B1 — State and Domain Truth Mapping

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

This mapping uses existing CP4 models. A blank or “not yet” entry is intentional; it prevents the journey from fabricating a Booking, Inventory state or Stay.

| Journey point | Request | Inventory | Payment | Booking | Stay / Operations | Canonical meaning |
|---|---|---|---|---|---|---|
| Discovery | Not created | Derived Availability from effective commitments | None | None | None | Searchable supply is not necessarily Available or Bookable for this Sale/context. |
| Option/Offer shared | Not created | Read only | No obligation from presentation alone | None | None | Offer is conceptual; no reservation or Booking. |
| Request created | `PENDING` | No automatic reservation; existing commitments still govern | None or separate context | Does not exist | None | Commercial intent awaits authorized decision. |
| Request rejected | `REJECTED` | No commitment created by rejection | No new obligation from rejection | Does not exist | None | Request path ends or returns to discovery. |
| Request accepted | `ACCEPTED` | Revalidation; Temporary Exclusive Commitment may follow where applicable | Required condition/obligation may become relevant | Does not exist | None | Acceptance authorizes proceeding; it is not confirmation. |
| Temporary commitment | Request remains separate (`ACCEPTED` unless policy says otherwise) | Finite Temporary Exclusive Inventory Commitment may be effective | Attempt/obligation separate | Does not exist | None | Inventory protection and payment are distinct truths. |
| Payment initiated/processing | Request/commitment remain pre-confirmation | Commitment behavior depends on policy; not chosen here | Attempt `INITIATED`/`PROCESSING` | Does not exist | None | Payment activity is not Booking. |
| Payment succeeded | Request/commitment remain pre-confirmation | Revalidation still matters | Attempt `SUCCEEDED`; condition may or may not be satisfied | Does not exist until confirmation conditions pass | None | Payment Received/Attempt success is not automatically Booking. |
| Payment failed | Request/commitment remain separate | No automatic release/default selected | Attempt `FAILED` | Does not exist | None | Do not invent cancellation/default/release. |
| Payment unknown | Request/commitment remain separate | No automatic release selected | Attempt `UNKNOWN` | Does not exist | None | Unknown provider truth is unresolved, not failure/default. |
| Confirmation conditions pass | Request history retained | Confirmed Accommodation Commitment established | Required condition satisfied under policy; obligations remain distinct | `CONFIRMED` begins | Stay separate; may become relevant | Commercial accommodation commitment is canonical Booking truth. |
| Guest access handoff | Request history retained | Confirmed commitment protects dates | Payment/settlement separate | `CONFIRMED` | Stay/access projection may be scheduled/relevant | Confirmation does not equal Check-in or Completed. |

## Domain ownership summary

- Marketplace/Discovery composes and presents options; it does not own authoritative Availability.
- Booking owns Request/Booking commercial truth and terms snapshot; it does not own Payment ledger or actual Stay.
- Inventory owns Commitments and derived Availability; it does not own Request/Lead/Offer.
- Money owns Obligation/Attempt/financial execution; it does not own Booking confirmation by payment alone.
- Stay owns operational truth; Butler/BQL consume scoped projections.
- Distribution owns Sale relationship/attribution; Sale attribution does not grant Booking Authority.

## State guardrails

The journey must never display or imply:

- `PENDING Request` as a pending Booking;
- an Availability projection as an Inventory Commitment;
- a payment attempt as a confirmed Booking;
- a confirmed Booking as `CHECKED_IN` or `COMPLETED` Stay;
- Sale acceptance as Host acceptance;
- a visible Guest confirmation as universal access or business authority.
