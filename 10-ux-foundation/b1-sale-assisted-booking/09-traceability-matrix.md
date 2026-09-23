# B1 — V0 and Source Traceability Matrix

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Journey capability / evidence | CP5 V0 dimension | Actor / context | CP6 surface | Canonical truth | Authority source | CP4 state/policy | B1 source |
|---|---|---|---|---|---|---|---|
| Sale finds suitable real supply | Inventory Trust; Network Adoption | Sale Context | Sale Workspace | Property/Unit, derived Availability, Public Price | Sale eligibility + relationship; no Inventory Authority | Inventory derived model; Distribution relationship | [B1-B01/B02](02-detailed-journey-specification.md#phase-b--discovery) |
| Guest understands option and chooses to proceed | Commerce Validation | Guest + Sale | Sale Workspace / communication handoff | Conceptual Offer/terms, Public Price, trust signals | Sale presentation; Guest consent/participation | Offer/terms policy; no reservation | [B1-C01/C02](02-detailed-journey-specification.md#phase-c--option--guest-choice) |
| Sale creates truthful Request | Commerce Validation; Network Adoption | Sale Context | Sale Workspace | Booking Request `PENDING`, provenance, Guest/party link | Sale Request capability; not Booking Authority | Request lifecycle; Request does not reserve | [B1-D01](02-detailed-journey-specification.md#phase-d--booking-request-creation) |
| Host receives decision responsibility | Inventory Trust; Network Adoption | Host/Primary Host/Co-host | Host Workspace | Request + authority scope | Booking Authority/delegation | Request `PENDING`; notification/timeout TBD | [B1-D02/E01](02-detailed-journey-specification.md#phase-e--host-decision) |
| Authorized accept/reject | Commerce Validation; Inventory Trust | Host/authorized Co-host | Host Workspace | Request `ACCEPTED`/`REJECTED`; no Booking on decision alone | Valid Booking Authority | Request lifecycle; confirmation conditions | [B1-E02/E03](02-detailed-journey-specification.md#phase-e--host-decision) |
| Finite commitment and revalidation | Inventory Trust; Commerce Validation | Inventory/Booking orchestration | Host / Admin projections | Temporary Exclusive Commitment where applicable | Inventory authority + authorized Host decision | Commitment/conflict/expiry policy | [B1-F01](02-detailed-journey-specification.md#phase-f--inventory-commitment) |
| Payment condition and attempt | Commerce Validation; Inventory Trust | Guest/Payer, Sale/Host support, Money | Guest/Sale/Host scoped views | Required Payment Condition, Obligation, Attempt | Payer/payment authority + Money execution | Attempt `INITIATED/PROCESSING/SUCCEEDED/FAILED/UNKNOWN` | [B1-G01/G02](02-detailed-journey-specification.md#phase-g--payment-requirement) |
| Booking confirmation | Commerce Validation | Shared projections | Guest, Sale, Host | Booking `CONFIRMED`, Confirmed Accommodation Commitment, snapshot | Valid confirmation conditions under recorded authority | Booking begins at `CONFIRMED` | [B1-H01/H02](02-detailed-journey-specification.md#phase-h--confirmation) |
| Confirmation to operations | Destination Stay Coverage; Network Adoption | Guest, Host, Butler, BQL | Guest Stay Access / Operations | Booking → Accommodation Basis → Stay/access projection | Guest scoped relation; operational assignment/destination scope | Stay separate from Booking; no automatic Check-in | [B1-I01/I02](02-detailed-journey-specification.md#phase-i--booking--stay-access--operations-handoff) |

## V0 boundary check

The matrix uses only CP5 MUST BUILD and MANUAL-ASSISTED capabilities: Sale inventory search, Public Price/basic Offer/quote, Booking Request, Host accept/reject, applicable commitment/payment condition, Booking confirmation, scoped Guest access and operational handoff. It does not introduce Affiliate Network, advanced Lead Distribution, dynamic pricing, full PMS, Managed Operations or other deferred capability.

## Source hierarchy

The detailed source trail is CP1–CP7 plus [CP8-A UX Foundation](../README.md). Supporting persistence is not used as a product-policy source.
