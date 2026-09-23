# CP8-E1 — Interaction Model & Behavioral Conventions

> Parent: **CP8 — UX / Design System** → **E — Detailed Interaction**
> Status: **ACCEPTED — CP8-E CLOSED**
> Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · Scope: **E1** · 2026-09-21

E1 defines the common behavioral grammar for Stayora V0 before any screen-by-screen interaction design. It covers action initiation, authority checks, truth revalidation, outcomes, stale/conflict/unknown behavior, correction, handoffs, attention and manual assistance. It does not define individual screen flows, layouts, visual components, microcopy, prototype, design system or implementation.

## Reading order

1. [Overview](01-overview.md)
2. [Interaction principles](02-interaction-principles.md)
3. [Generic action model](03-generic-action-model.md)
4. [Action classes](04-action-classes.md)
5. [Consequential action model](05-consequential-action-model.md)
6. [Authority behavior](06-authority-behavior.md)
7. [Acting capacity](07-acting-capacity.md)
8. [Revalidation](08-revalidation.md)
9. [Stale truth](09-stale-truth.md)
10. [Outcome model](10-outcome-model.md)
11. [Success and failure](11-success-failure.md)
12. [Unknown outcome](12-unknown-outcome.md)
13. [Conflict](13-conflict.md)
14. [Pending and processing](14-pending-processing.md)
15. [Optimistic behavior](15-optimistic-behavior.md)
16. [Duplicate intent](16-duplicate-intent.md)
17. [Correction](17-correction.md)
18. [Supersession and revocation](18-supersession-revocation.md)
19. [Destructive actions](19-destructive-actions.md)
20. [Manual-assisted interaction](20-manual-assisted-interaction.md)
21. [Admin-assisted interaction](21-admin-assisted-interaction.md)
22. [Cross-context handoff](22-cross-context-handoff.md)
23. [Attention behavior](23-attention-behavior.md)
24. [Partial context](24-partial-context.md)
25. [Empty versus blocked](25-empty-vs-blocked.md)
26. [Action availability](26-action-availability.md)
27. [Action explanation](27-action-explanation.md)
28. [Confirmation and consequence preview](28-confirmation-consequence-preview.md)
29. [Payment boundary](29-payment-boundary.md)
30. [Inventory boundary](30-inventory-boundary.md)
31. [Request/Booking boundary](31-request-booking-boundary.md)
32. [Stay boundary](32-stay-boundary.md)
33. [Incident boundary](33-incident-boundary.md)
34. [Onboarding boundary](34-onboarding-boundary.md)
35. [Guest access boundary](35-guest-access-boundary.md)
36. [Sale economics boundary](36-sale-economics-boundary.md)
37. [Admin/BQL boundary](37-admin-bql-boundary.md)
38. [Loading and refresh](38-loading-refresh.md)
39. [History and provenance](39-history-provenance.md)
40. [Notification principle](40-notification-principle.md)
41. [Recovery](41-recovery.md)
42. [Pattern library](42-pattern-library.md)
43. [B1–B5 stress test](43-b1-b5-stress-test.md)
44. [C1–C4 stress test](44-c1-c4-stress-test.md)
45. [Surface stress test](45-surface-stress-test.md)
46. [Mobile/field constraints](46-mobile-field-constraints.md)
47. [Accessibility and clarity](47-accessibility-clarity.md)
48. [TBD/policy register](48-tbd-policy-register.md)
49. [Gap/blocker register](49-gap-blocker-register.md)
50. [V0/source traceability](50-traceability.md)
51. [E1 report](../CP8-E1-INTERACTION-MODEL-BEHAVIORAL-CONVENTIONS-REPORT.md)

## Core grammar

`DOMAIN TRUTH → CONTEXTUAL PROJECTION → USER INTENT → AUTHORITY CHECK → VALIDATION / REVALIDATION → ACTION → SYSTEM OUTCOME → UPDATED PROJECTION → AUDIT / PROVENANCE → HANDOFF / ATTENTION`.

UI state is never a replacement for domain truth. E1 is the accepted common behavioral baseline for [CP8-E2 Request → Booking Interaction](../e2-request-booking-interaction/README.md); it is not screen-by-screen design.
