# CP8-B3 — Direct Guest Booking Journey

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-B Critical Journeys**  
> Status: **ACCEPTED AS BASELINE FOR CP8-B4**  
> Freeze status: **NOT FROZEN**  
> Scope: **B3 only** · 2026-09-20

B3 specifies the direct Guest journey from Public Marketplace discovery through a truthful Booking Request, authorized decision, applicable Inventory and Payment conditions, Booking confirmation, Guest Stay Access and operational handoff. It tests whether a Guest can originate Stayora commerce without mandatory Sale attribution and without silently turning the journey into Instant Book.

The documents are journey analysis, not screens, database events, new domain concepts or new lifecycle states. They preserve the CP1–CP7 and CP8-A/B1/B2 boundaries: Request is not Booking, Request does not reserve Inventory, Payment is not Booking, Booking is not Stay, and Guest visibility is not authority.

## Reading order

1. [B3 journey overview](01-journey-overview.md)
2. [Detailed journey specification](02-detailed-journey-specification.md)
3. [Cross-context timeline](03-cross-context-timeline.md)
4. [Public truth and Bookability mapping](04-public-truth-and-bookability.md)
5. [Responsibility handoffs](05-responsibility-handoffs.md)
6. [State/domain truth mapping](06-state-domain-truth.md)
7. [Alternative and failure boundaries](07-alternative-failure-boundaries.md)
8. [Guest without mandatory account](08-guest-without-account.md)
9. [TBD and policy register](09-tbd-policy-register.md)
10. [Domain/workflow/authority gaps](10-domain-gaps.md)
11. [B1 versus B3](11-b1-vs-b3.md)
12. [B2 convergence note](12-b2-convergence.md)
13. [V0/source traceability](13-traceability.md)
14. [B3 report](../CP8-B3-DIRECT-GUEST-BOOKING-REPORT.md)

## Canonical B3 chain

```text
Public Marketplace truth
  → Guest evaluates dates, occupancy, Availability and Bookability
  → Guest intent
  → Booking Request (`PENDING`)
  → Host / authorized Booking Authority decision
  → final Inventory revalidation
  → applicable Temporary Exclusive Commitment where supported
  → action-specific Required Payment Condition / Payment Attempt
  → Booking Confirmation Conditions
  → Booking (`CONFIRMED`)
  → Guest confirmation and scoped Stay Access
  → Host / Butler / Destination Operations handoff
```

Guest intent does not create a Booking, Inventory Commitment, Payment or Stay. Sale attribution is optional and is not created merely because the Guest entered the public journey. The direct path is Stayora-originated commerce; it is not External Booking and it is not automatically Instant Book.

## Stop condition

B3 ends at this journey specification and review report. B4 Stay Operations is documented separately as the current workstream. B5 Inventory Intervention, onboarding, workspace/surface UX, detailed interaction, Design System and implementation remain not started.
