# CP8-E2 — Request → Booking Interaction

> Parent: **CP8 — UX / Design System** → **E — Detailed Interaction**
> Status: **ACCEPTED — CP8-E CLOSED**
> Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · Scope: **E2** · 2026-09-21

E2 defines the shared V0 interaction family from accommodation intent through Booking confirmation for B1 Sale-assisted Booking and B3 Direct Guest Booking. It applies E1's behavioral grammar and stops at unresolved payment, Inventory, credential, authority and policy boundaries. It does not define visual layout, components, final microcopy, APIs, code or implementation.

## Reading order

1. [Overview](01-overview.md)
2. [Canonical Request → Booking](02-canonical-request-booking.md)
3. [Sale-assisted entry](03-sale-assisted-entry.md)
4. [Direct Guest entry](04-direct-guest-entry.md)
5. [Availability/Bookability](05-availability-bookability.md)
6. [Request information contract](06-request-information-contract.md)
7. [Request creation/submission](07-request-creation-submission.md)
8. [Request pending](08-request-pending.md)
9. [Host attention](09-host-attention.md)
10. [Request detail](10-request-detail.md)
11. [Decision authority](11-decision-authority.md)
12. [Accept/reject behavior](12-accept-reject.md)
13. [Decision revalidation](13-decision-revalidation.md)
14. [Reject branch](14-reject-branch.md)
15. [Accept branch](15-accept-branch.md)
16. [Inventory commitment boundary](16-inventory-commitment.md)
17. [Inventory conflict](17-inventory-conflict.md)
18. [Payment condition boundary](18-payment-condition.md)
19. [Payment attempt](19-payment-attempt.md)
20. [Payment UNKNOWN](20-payment-unknown.md)
21. [Booking confirmation](21-booking-confirmation.md)
22. [Confirmation delay/failure](22-confirmation-delay-failure.md)
23. [Host projection](23-host-outcome-projection.md)
24. [Sale projection](24-sale-outcome-projection.md)
25. [Guest projection](25-guest-outcome-projection.md)
26. [Guest Stay Access handoff](26-guest-stay-access-handoff.md)
27. [Operations handoff](27-operations-handoff.md)
28. [Attention resolution](28-attention-resolution.md)
29. [Request correction](29-request-correction.md)
30. [Withdrawal/expiry](30-withdrawal-expiry.md)
31. [Duplicate Request](31-duplicate-request.md)
32. [Concurrent decision](32-concurrent-decision.md)
33. [Multi-capacity](33-multi-capacity.md)
34. [Direct vs Sale convergence](34-direct-sale-convergence.md)
35. [Screen interaction contracts](35-screen-interaction-contracts.md)
36. [Interaction sequences](36-interaction-sequences.md)
37. [Outcome projection matrix](37-outcome-projection-matrix.md)
38. [Authority × action matrix](38-authority-action-matrix.md)
39. [Information visibility matrix](39-information-visibility-matrix.md)
40. [Error/recovery matrix](40-error-recovery-matrix.md)
41. [Consequence preview](41-consequence-preview.md)
42. [Mobile/field](42-mobile-field.md)
43. [Accessibility/clarity](43-accessibility-clarity.md)
44. [TBD/policy register](44-tbd-policy-register.md)
45. [Gap/blocker register](45-gap-blocker-register.md)
46. [V0/source traceability](46-traceability.md)
47. [E2 report](../CP8-E2-REQUEST-BOOKING-INTERACTION-REPORT.md)

## Canonical interaction grammar

`CURRENT TRUTH → USER INTENT → ACTING CONTEXT → RESOURCE SCOPE → AUTHORITY CHECK → PRECONDITION CHECK → CURRENT-TRUTH REVALIDATION → ACTION INPUT → ACTION COMMITMENT → OUTCOME → UPDATED PROJECTION → AUDIT / PROVENANCE → HANDOFF / ATTENTION`.

B1 and B3 converge on one Request model and one Booking truth. Distribution source changes context, attribution and projections; it does not create a different Booking object or lifecycle. E2 is the accepted interaction baseline for [CP8-E3 Stay Operations](../e3-stay-operations-interaction/README.md).
