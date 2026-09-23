# B4 — Destination / BQL Boundary

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Operational scope

Destination/BQL contexts may consume destination-scoped operational truth needed for:

- upcoming occupancy and arrivals/departures;
- Guest/staying-party information where allowed;
- access, registration and vehicle information where destination policy requires it;
- destination services and coordination;
- relevant Incidents, issues and exceptions.

The exact vehicle, gate, cart, QR and local-service behavior remains Destination configuration, not a universal Core invariant.

## Commercial boundary

BQL visibility does not grant Booking Authority, pricing, payment, refund, Settlement, Payout, Owner or Sale authority. Destination staff do not receive full Guest commerce, Owner economics, Sale commission, payment ledger, tax or private Host information without a canonical need-to-know basis.

## Operational truth

Operational Occupancy is distinct from Commercial Availability. BQL may validate or coordinate current Stay/access information without changing Inventory Truth. A gate/access observation is not automatically Check-in, Checkout, Incident consequence or Inventory release.

## Escalation

Destination staff may record or route an issue within function scope. A commercial or policy consequence requires the owning domain and explicit authority. Local destination rules must not silently become global Stayora lifecycle or permission rules.
