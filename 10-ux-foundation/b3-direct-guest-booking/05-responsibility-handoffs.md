# B3 — Responsibility Handoffs

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Handoff | Trigger | Canonical object | Authority basis | Information transferred | Responsibility transferred | Failure / policy boundary |
|---|---|---|---|---|---|---|
| Public Marketplace → Guest decision | Guest finds a candidate | Listing, Unit, Public Price, Availability projection | Public discovery access | Material public truth and conditions | Guest decides whether to proceed | Stale/unknown or private truth remains unresolved; no promise |
| Guest → Booking Request | Guest supplies intent and required Request information | Booking Request | Request-creation capability; no Booking Authority | Unit, range, party, terms, consent/provenance | Guest submits truthful demand | No account requirement, minimum data and consent details remain TBD |
| Request → Host / Booking Authority | Request becomes `PENDING` | Request + authority/resource scope | Host/Primary Host or delegated Booking Authority | Terms, dates, current Inventory context, party data needed for decision | Host receives accept/reject responsibility | Missing authority, unanswered Request and reassignment are not invented |
| Host decision → Inventory | Request becomes `ACCEPTED` | Request + Inventory Commitment candidate | Authorized Host decision plus Inventory authority/policy | Accepted terms, Unit × Time, effective commitments | Inventory revalidation / finite commitment where supported | Conflict, expiry and duration remain policy boundaries |
| Inventory / terms → Payment | Applicable action condition exists | Required Payment Condition, Payment Obligation, Payment Attempt | Money/Booking policy; Payer supplies payment | Specific condition, amount/terms where canonical, status | Payer and payment context fulfil/evaluate condition | Payment rules, grace/default/refund/retry remain TBD |
| Payment / conditions → Booking | All confirmation conditions pass | Booking | Canonical confirmation evaluation | Valid terms, authority, exclusive commitment, consent, payment condition | Booking becomes `CONFIRMED` | Payment success alone is insufficient; no pre-confirmation Booking |
| Booking → Guest Stay Access | Booking confirmed and access eligibility exists | Booking, Stay, Access projection | Guest relationship + access policy | Confirmation, accommodation and need-to-know access information | Guest can prepare/use access where eligible | Authentication, QR/token and privacy design remain TBD |
| Booking / Stay → Operations | Operational representation/assignment exists | Stay, Arrival, Access, Incident | Operational assignment/function scope | Need-to-know arrival, party and issue data | Host/Butler/BQL prepare/support | Operations cannot gain commercial authority by visibility |

## Receiving-context rule

Each handoff transfers a bounded responsibility, not ownership of every related domain. In particular, Host authority decides the Request; Inventory determines effective commitment truth; Money determines payment state; Booking determines confirmation; Stay/Operations determines operational progress. Guest, Butler, BQL and Sale visibility never substitutes for the relevant authority.
