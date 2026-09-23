# CP8-E4 — Inventory Intervention Interaction

> Parent: **CP8 — UX / Design System** → **E — Detailed Interaction**
> Status: **ACCEPTED — CP8-E CLOSED**
> Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · Execution unit: **CP8-E4** · 2026-09-21

E4 defines V0 interaction behavior for B5 Inventory Intervention. It is accepted as the final E4 architecture baseline. It treats Inventory UX as a projection and intervention interface over canonical Inventory truth. It preserves Unit × Time scope, authority, evidence, commitments, blocks, derived Availability, contextual Bookability, conflict, provenance and downstream handoffs.

## Reading order

1. [Overview](01-overview.md)
2. [Canonical Inventory Interaction](02-canonical-inventory-interaction.md)
3. [Inventory Truth for UX](03-inventory-truth-for-ux.md)
4. [Unit × Time Scope](04-unit-time-scope.md)
5. [Inventory Projection](05-inventory-projection.md)
6. [Calendar Boundary](06-calendar-boundary.md)
7. [Actor Entry Paths](07-actor-entry-paths.md)
8. [Owner Interaction](08-owner-interaction.md)
9. [Host Interaction](09-host-interaction.md)
10. [Butler / BQL Evidence Handoff](10-butler-bql-evidence-handoff.md)
11. [Admin Interaction](11-admin-interaction.md)
12. [Owner Block](12-owner-block.md)
13. [Maintenance Block](13-maintenance-block.md)
14. [Temporary Exclusive Commitment](14-temporary-exclusive-commitment.md)
15. [Confirmed Accommodation Commitment](15-confirmed-accommodation-commitment.md)
16. [External-backed Commitment](16-external-backed-commitment.md)
17. [Intervention Action Model](17-intervention-action-model.md)
18. [Authority](18-authority.md)
19. [Revalidation](19-revalidation.md)
20. [Conflict Detection](20-conflict-detection.md)
21. [Conflict Representation](21-conflict-representation.md)
22. [Conflict Resolution Boundary](22-conflict-resolution-boundary.md)
23. [Availability Derivation](23-availability-derivation.md)
24. [Bookability](24-bookability.md)
25. [Release / Removal](25-release-removal.md)
26. [Correction / Expiry](26-correction-expiry.md)
27. [Checkout / Completion Boundary](27-checkout-completion-boundary.md)
28. [Incident Handoff](28-incident-handoff.md)
29. [Request / Booking Handoff](29-request-booking-handoff.md)
30. [External Accommodation Handoff](30-external-accommodation-handoff.md)
31. [Public Projection](31-public-projection.md)
32. [Sale Projection](32-sale-projection.md)
33. [Host / Owner Projection](33-host-owner-projection.md)
34. [Operations Projection](34-operations-projection.md)
35. [Admin Projection](35-admin-projection.md)
36. [Attention](36-attention.md)
37. [Manual-Assisted Inventory](37-manual-assisted-inventory.md)
38. [Duplicate / Concurrent Intervention](38-duplicate-concurrent-intervention.md)
39. [Partial / Unknown Truth](39-partial-unknown-truth.md)
40. [Screen Interaction Contracts](40-screen-interaction-contracts.md)
41. [Interaction Sequences](41-interaction-sequences.md)
42. [Projection Matrix](42-projection-matrix.md)
43. [Authority × Action Matrix](43-authority-action-matrix.md)
44. [Conflict Matrix](44-conflict-matrix.md)
45. [Visibility Matrix](45-visibility-matrix.md)
46. [Error / Recovery Matrix](46-error-recovery-matrix.md)
47. [Consequence Preview](47-consequence-preview.md)
48. [Mobile / Field](48-mobile-field.md)
49. [Accessibility / Clarity](49-accessibility-clarity.md)
50. [Policy Register](50-policy-register.md)
51. [Cross-Family Blocker Convergence](51-cross-family-blocker-convergence.md)
52. [Prototype Readiness Gate](52-prototype-readiness.md)
53. [Founder Decision Queue](53-founder-decision-queue.md)
54. [CP8-E Coverage Review](54-cp8-e-coverage-review.md)
55. [V0 / Source Traceability](55-traceability.md)
56. [E4 report](../CP8-E4-INVENTORY-INTERVENTION-INTERACTION-REPORT.md)

## Canonical flow

`Intent / operational fact → authority + Unit × Time + basis/evidence → Inventory truth evaluation → authorized intervention → conflict detection → derived Availability → contextual Bookability/projection → correction, release or expiry where canonical → downstream handoff`.

Calendar cells are projections only. Emergency Protective Hold is a Founder-approved extension: a scoped protective intervention that prevents new conflicting commitments, escalates immediately and remains distinct from Maintenance Block. Request, Incident, External Fact, Checkout and Completion do not automatically create or release Inventory.

## Stop condition

E4 closes the Detailed Interaction architecture. E5 does not exist. [CP8-F1 Thin Design System Foundation](../../10-ux-foundation/f1-thin-design-system-foundation/README.md) is in progress; CP8-F2, CP8-G/H, prototypes, APIs, persistence and implementation remain not started.
