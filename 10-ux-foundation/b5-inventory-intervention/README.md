# CP8-B5 — Inventory Intervention Journey

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-B Critical Journeys**  
> Status: **ACCEPTED AS BASELINE FOR CP8-C2**  
> Freeze status: **NOT FROZEN**  
> Scope: **B5 only** · 2026-09-20

B5 specifies how an authorized actor or legitimate operational fact may intervene in accommodation Inventory for Oceanami V0. It covers Owner Blocks, Maintenance/Unusable Inventory, the Founder-approved Emergency Protective Hold, operational-to-Inventory handoff, overlapping commitments/blocks, derived Availability, conflict handling, correction/release and downstream Booking/Stay exception boundaries.

B5 is an Inventory truth and authority journey, not a calendar or screen design. Availability remains derived from effective Inventory Commitments and Blocks. There is no manual Availability boolean, generic `UNAVAILABLE` state, silent Booking cancellation, external-accommodation deletion, automatic Incident-to-Block transition or origin-specific Inventory model. Emergency Protective Hold is distinct from Maintenance Block and does not override an existing commitment.

## Reading order

1. [B5 journey overview](01-journey-overview.md)
2. [Detailed intervention journey](02-detailed-inventory-intervention-journey.md)
3. [Inventory basis mapping](03-inventory-basis-mapping.md)
4. [Owner Block journey](04-owner-block-journey.md)
5. [Maintenance Block journey](05-maintenance-block-journey.md)
6. [Operational → Inventory handoff](06-operational-inventory-handoff.md)
7. [Overlap/conflict matrix](07-overlap-conflict-matrix.md)
8. [Derived Availability mapping](08-derived-availability.md)
9. [Availability versus Bookability](09-availability-bookability.md)
10. [Cross-context projections](10-cross-context-projections.md)
11. [Responsibility handoffs](11-responsibility-handoffs.md)
12. [Booking/Stay protection](12-existing-truth-protection.md)
13. [Correction/release/history](13-correction-release-history.md)
14. [Alternative/failure boundaries](14-alternative-failure-boundaries.md)
15. [B1–B4 impact check](15-b1-b4-impact-check.md)
16. [TBD and policy register](16-tbd-policy-register.md)
17. [Domain/workflow/authority gaps](17-domain-gaps.md)
18. [V0/source traceability](18-traceability.md)
19. [B5 report](../CP8-B5-INVENTORY-INTERVENTION-REPORT.md)

## Canonical intervention chain

```text
Intent / operational fact
  → authority + Unit × Time basis/evidence
  → authorized Inventory intervention
  → canonical Commitment or Block truth
  → conflict detection where applicable
  → derived Availability
  → contextual projections / downstream exceptions
```

The intervention acts on a canonical basis: Owner Block, Maintenance Block, Temporary Exclusive Commitment, Confirmed Accommodation Commitment or External Accommodation-backed Commitment. It never acts on “set available = false”.

## Stop condition

B5 ends at this Inventory Intervention journey and review report. C1–C4 Onboarding are accepted baselines; D1 Workspace & Surface Architecture is documented separately as the current execution unit. Detailed screen UX, Detailed Interaction, Design System, Prototype, Acceptance Package and Implementation remain not started.
