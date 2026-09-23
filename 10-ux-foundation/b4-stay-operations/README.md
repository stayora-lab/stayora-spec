# CP8-B4 — Stay Operations Journey

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-B Critical Journeys**  
> Status: **ACCEPTED AS BASELINE FOR CP8-B5**  
> Freeze status: **NOT FROZEN**  
> Scope: **B4 only** · 2026-09-20

B4 specifies how a legitimate accommodation becomes an operational Stay and moves through Oceanami V0 pre-arrival, readiness, arrival, Check-in, in-stay support, Incident/exception handling, Checkout, completion and post-stay follow-up.

Stay is an independent operational truth. B4 does not turn Booking into Stay, create a fake Booking for External Accommodation, or make every operational actor understand or mutate the commerce source. B1, B2 and B3 origins converge on coherent Stay operations while retaining provenance.

## Reading order

1. [B4 journey overview](01-journey-overview.md)
2. [Detailed Stay Operations journey](02-detailed-stay-operations-journey.md)
3. [Cross-context timeline](03-cross-context-timeline.md)
4. [Operational responsibility matrix](04-operational-responsibility-matrix.md)
5. [Butler boundary](05-butler-boundary.md)
6. [Destination / BQL boundary](06-destination-bql-boundary.md)
7. [Guest operational outcomes](07-guest-operational-outcomes.md)
8. [Stay lifecycle/domain mapping](08-stay-lifecycle-domain-mapping.md)
9. [Responsibility handoffs](09-responsibility-handoffs.md)
10. [Incident stress test](10-incident-stress-test.md)
11. [Stay-origin comparison](11-stay-origin-comparison.md)
12. [Inventory relationship](12-inventory-relationship.md)
13. [Alternative and failure boundaries](13-alternative-failure-boundaries.md)
14. [Correction and historical truth](14-correction-historical-truth.md)
15. [TBD and policy register](15-tbd-policy-register.md)
16. [Domain/workflow/authority gaps](16-domain-gaps.md)
17. [V0/source traceability](17-traceability.md)
18. [B4 report](../CP8-B4-STAY-OPERATIONS-REPORT.md)

## Canonical operational chain

```text
Accommodation Basis
  (Stayora Booking | External Accommodation)
        ↓
       Stay
        ↓
Operational projection
  ├ Guest
  ├ Host / Primary Host
  ├ Butler
  └ Destination / BQL
        ↓
Incident / evidence / completion history where applicable
```

The lifecycle remains the CP4/CP7 model:

```text
SCHEDULED → CHECKED_IN → CHECKED_OUT → COMPLETED
SCHEDULED → DID_NOT_OCCUR
```

`PREPARATION` and `READY` are operational readiness milestones, not core Stay states. `ARRIVAL` is an event/observation. `IN_STAY` is not added. Arrival is not automatically Check-in; Checkout is not automatically Completed.

## Stop condition

B4 ends at this Stay Operations journey and review report. B5 Inventory Intervention and C1–C4 Onboarding are accepted baselines; D1 Workspace & Surface Architecture is the current execution unit. Detailed screen UX, interaction, Design System, prototype and implementation remain not started.
