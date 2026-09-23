# CP8-B2 — External Booking → Stay Journey

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-B Critical Journeys**  
> Status: **ACCEPTED AS BASELINE FOR CP8-B3**  
> Freeze status: **NOT FROZEN**  
> Scope: **B2 only** · 2026-09-19

B2 specifies how accommodation originating outside Stayora commerce may become truthful Inventory and operational Stay information. It tests Destination Stay Coverage without requiring Stayora-originated commerce.

It does not specify Stay Operations, Inventory Intervention, screens, interaction design, Design System, prototype or implementation.

**CP8-E closure reconciliation:** B2 is sufficiently covered for CP8-E exit by this journey plus E3 Stay Operations, E4 Inventory Intervention and FD-08/09, FD-12 and FD-15/16. The external commerce → Report/Evidence → authorized External Accommodation Fact → Inventory/Stay path remains canonical; no Stayora Booking or commerce is fabricated. Direct Guest Booking is documented separately in [CP8-B3](../b3-direct-guest-booking/README.md). The directory is a workstream grouping inside CP8 and does not create a new checkpoint.

## Reading order

1. [B2 journey overview](01-journey-overview.md)
2. [Detailed journey specification](02-detailed-journey-specification.md)
3. [Cross-context timeline](03-cross-context-timeline.md)
4. [Provenance and authority mapping](04-provenance-authority.md)
5. [Inventory effect mapping](05-inventory-effect.md)
6. [Operations handoff mapping](06-operations-handoffs.md)
7. [Alternative, failure and TBD boundaries](07-alternatives-tbd.md)
8. [Domain/workflow/authority gaps](08-domain-gaps.md)
9. [B1 versus B2](09-b1-vs-b2.md)
10. [V0/source traceability](10-traceability.md)
11. [B2 report](../CP8-B2-EXTERNAL-BOOKING-TO-STAY-REPORT.md)

## Non-negotiable chain

```text
External Commerce
  → External Accommodation Report / Fact
  → authoritative external accommodation truth where authority/evidence allow
  → Inventory Truth and/or Stay representation
  → Guest / Host / Butler / Destination Operations projections
```

This chain does not create a Stayora Booking, Booking Request, Stayora Payment, Sale attribution, commission, Settlement or Payout merely because an external accommodation is represented.

## Core distinction

`External Accommodation ≠ Stayora Booking`.

External commerce may become operationally first-class inside Stayora while preserving its source, provenance and external commercial lifecycle. A report is not automatically an authoritative fact; an authoritative fact is not automatically an Inventory Commitment; an Inventory Commitment is not Availability.

## Stop condition

B2 ends at this journey specification and review report. B3 is an accepted preceding journey and B4 Stay Operations is the current pass; Inventory Intervention and all screen/implementation work remain not started.
