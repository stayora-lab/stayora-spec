# CP8-B1 — Sale-Assisted Booking Journey

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-B Critical Journeys**  
> Status: **ACCEPTED AS CP8-B BASELINE**  
> Freeze status: **NOT FROZEN**  
> Scope: **B1 only** · 2026-09-19

This workstream specifies the conceptual Oceanami V0 Sale-assisted Booking journey before screens are designed. It answers who acts, in which Working Context, over which canonical object, under which authority, with which information, domain effect, visible outcome, handoff and unresolved policy.

It does not begin Direct Guest Booking, External Booking → Stay, Stay Operations, Inventory Intervention, Onboarding UX, Screen Architecture, Design System or Implementation Plan. The directory name is a workstream grouping inside CP8; it does not create a new roadmap checkpoint.

## Reading order

1. [Journey overview and canonical boundary](01-journey-overview.md)
2. [Detailed journey specification](02-detailed-journey-specification.md)
3. [Cross-context timeline](03-cross-context-timeline.md)
4. [Responsibility handoffs](04-responsibility-handoffs.md)
5. [State and domain truth mapping](05-state-domain-truth.md)
6. [Alternative and failure boundaries](06-alternative-failure-boundaries.md)
7. [TBD / policy boundary register](07-tbd-policy-register.md)
8. [Domain-gap findings](08-domain-gap-findings.md)
9. [V0 and source traceability](09-traceability-matrix.md)
10. [B1 report](../CP8-B1-SALE-ASSISTED-BOOKING-REPORT.md)

## Canonical chain under investigation

```text
Guest need
  → Sale discovery / availability evaluation
  → option or Offer presentation where supported
  → Guest intent to proceed
  → Sale creates Booking Request
  → Host / authorized Booking Authority decides
  → applicable Inventory Commitment behavior
  → Required Payment Condition and payment progression
  → Booking CONFIRMED
  → Guest confirmation / scoped Stay Access
  → operational responsibility becomes relevant
```

This is a journey structure, not a new state machine. Each transition is checked against CP2–CP7 and CP8-A. Existing `TBD`, `WORKING MODEL`, `HYPOTHESIS`, `OUT OF SCOPE — V0` and `SUPERSEDED` statuses remain open.

## Non-negotiable boundaries

- Sale capacity alone does not accept a Booking Request.
- Request is not Booking and does not reserve Inventory.
- Searchability, Availability and actor-specific Bookability remain distinct.
- Inventory Commitment is not Availability.
- Payment Requirement/Condition is not Payment; Payment is not Booking unless canonical confirmation conditions are satisfied.
- Booking is not Stay.
- Sale attribution is not Booking Authority.
- External Accommodation is not Stayora Booking; this journey does not route external commerce into the Sale-assisted path.

## B1 stop condition

B1 ends after this conceptual journey specification and review report. It does not create screens, wireframes, visual UI, Figma artifacts, components, design tokens, prototypes, APIs, code, schema or migrations.
