# B3 — V0 and Source Traceability

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| B3 claim/capability | CP5 V0 dimension | Actor/context | CP6 surface | Canonical truth | Authority/lifecycle source | B3 source |
|---|---|---|---|---|---|---|
| Guest discovers public accommodation | Supply Adoption; Guest Trust | Guest / Public Marketplace | Home, Destination, Search, Villa Detail | Destination, Property, Unit, Listing, public truth | CP2 marketplace; CP6 public IA | [B3-B01](02-detailed-journey-specification.md#phase-b--discovery) |
| Guest evaluates dates and derived Availability | Inventory Trust; Guest Trust | Guest / Marketplace | Search / Unit detail | Inventory Commitments → derived Availability | CP4 Inventory; CP8-A semantics | [B3-D01](02-detailed-journey-specification.md#phase-d--availability-evaluation) |
| Guest creates Request without Sale | Commerce; Guest Trust | Guest / Guest context | Public → Guest progression | Booking Request `PENDING` | CP3 capabilities; CP4 Request lifecycle | [B3-F01](02-detailed-journey-specification.md#phase-f--booking-request-creation) |
| Host/authorized Co-host decides | Supply Adoption; Commerce | Host / Booking Authority | Host Workspace | Request `ACCEPTED` / `REJECTED` | CP3 Booking Authority; CP4 policy | [B3-G01](02-detailed-journey-specification.md#phase-g--host--booking-authority-decision) |
| Accepted Request revalidates Inventory | Inventory Trust; Commerce | Inventory/Booking orchestration | Host / system projection | Temporary Exclusive Commitment where supported | CP4 Inventory/commitment model | [B3-H01](02-detailed-journey-specification.md#phase-h--inventory-revalidation--commitment) |
| Payer fulfils specific condition | Commerce | Guest/Payer / Money | Guest payment projection | Required Payment Condition, Obligation, Attempt | CP4 Payment; CP7 Money | [B3-I01](02-detailed-journey-specification.md#phase-i--required-payment-condition) |
| Booking is truthfully confirmed | Commerce; Guest Trust | Booking evaluation | Guest / Host | Booking `CONFIRMED` | CP4 Booking; CP7 aggregate principles | [B3-J01](02-detailed-journey-specification.md#phase-j--confirmation) |
| Guest receives scoped access | Destination Stay Coverage; Guest Trust | Guest / Stay Access | Guest Stay Access | Booking, Stay, access projection | CP6 Guest Access; CP8-A privacy semantics | [B3-K01](02-detailed-journey-specification.md#phase-k--guest-confirmation--stay-access) |
| Operations receives need-to-know truth | Destination Stay Coverage | Host / Butler / BQL | Operations | Stay, Arrival, Access, Incident | CP3 function scope; CP4 Stay; CP6 Operations | [B3-L01](02-detailed-journey-specification.md#phase-l--operations-handoff) |

## V0 discipline

B3 uses the CP5 direct marketplace, Booking Request, Host decision, applicable Inventory/Payment/Booking confirmation and scoped Guest access capabilities. It does not introduce full CRM, advanced Lead Distribution, Affiliate Network, dynamic pricing, PMS/Channel Manager, Managed Operations, advanced loyalty/reputation, native apps, marketing automation or workforce management.

## Source order

Founder decisions → canonical confirmed CP1–CP6 architecture → CP7 conceptual model → CP8-A/B1/B2 accepted baselines → B3 analysis. Supporting persistence is a constraint reference only. No source below this order silently resolves a TBD.
