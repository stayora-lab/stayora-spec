# Inventory Commitment model

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

Inventory Availability is derived truth computed from effective Inventory Commitments over a Bookable Unit and time range. `AVAILABLE`, `HELD`, `BOOKED`, and `BLOCKED` are projections/semantics, not an authoritative persisted lifecycle.

## Commitment types

- **Temporary Exclusive Inventory Commitment** — finite, scope-bound commitment after authorized acceptance.
- **Confirmed Accommodation Commitment** — confirmed accommodation right.
- **Availability Block** — authorized operational/owner/maintenance block.

Request, Lead, Offer, and Stay are not Inventory Commitments. Conceptual exclusivity may be `NON_EXCLUSIVE`, `TEMPORARY_EXCLUSIVE`, or `EXCLUSIVE`; these are not technical enums.

An existing effective exclusive commitment plus a proposed incompatible overlapping commitment creates **INVENTORY CONFLICT**. Release requires an authoritative end. Late arrival, no arrival, lack of Check-in, or No-show does not itself release Inventory. True and late-discovered double-commitment resolution remains **TBD**.
