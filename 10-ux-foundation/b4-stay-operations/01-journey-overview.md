# B4 — Stay Operations Journey Overview

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Purpose

B4 tests whether Oceanami V0 can operate a legitimate upcoming/current accommodation from Stay truth, regardless of whether the accommodation originated from Sale-assisted commerce, Direct Guest commerce or External Accommodation.

## Canonical journey

```text
Accommodation Basis is sufficient
  → Stay is represented as `SCHEDULED`
  → pre-arrival preparation and need-to-know projections
  → operational readiness milestone (not a new Stay state)
  → expected arrival / physical arrival observation
  → authorized Check-in evidence and transition
  → in-stay support and coordination
  → Incident / exception reporting where needed
  → scheduled departure / Guest departure
  → authorized Checkout evidence and transition
  → Operational Completion Readiness
  → `COMPLETED` only when canonical completion conditions pass
  → historical and eligible post-stay processes
```

## Origin convergence

- **B1:** Sale-assisted Stayora Booking → confirmed accommodation → Stay.
- **B3:** Direct Guest Stayora Booking → confirmed accommodation → Stay.
- **B2:** External Accommodation → represented Stay without fake Stayora Booking.

Operational actors primarily use Stay, access, arrival, party and issue truth. Commercial provenance remains available only where a legitimate operational, audit or policy need exists.

## Core boundaries

`Booking ≠ Stay`, `Accommodation Basis ≠ Stay lifecycle`, `Inventory Commitment ≠ Stay`, `Availability ≠ readiness`, `Arrival ≠ Check-in`, `Check-in ≠ payment confirmation`, `Checkout ≠ Completed`, and `Incident ≠ Finding ≠ Responsibility ≠ Consequence`.

Butler and Destination/BQL receive operational scope; neither receives Booking Authority, pricing, payment, settlement or reputation-consequence authority merely by assignment or visibility.
