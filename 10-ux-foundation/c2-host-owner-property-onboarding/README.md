# CP8-C2 — Host / Owner + Property Onboarding

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-C Onboarding**  
> Status: **ACCEPTED AS BASELINE FOR CP8-C3**  
> Freeze status: **NOT FROZEN**  
> Scope: **C2 only** · 2026-09-20

C2 documents the V0 conceptual onboarding journeys that establish truthful Owner/Host relationships around a Property and its Bookable Units. It is the accepted baseline consumed by [CP8-C3 Sale Onboarding](../c3-sale-onboarding/README.md). It covers actor-first and resource-first entry, their convergence, authority effects, readiness outcomes, corrections and unresolved boundaries. It does not design screens, forms, technical invitations, data fields, API, schema, or implementation.

## Reading order

1. [Overview](01-overview.md)
2. [Actor-first journey](02-actor-first-journey.md)
3. [Resource-first journey](03-resource-first-journey.md)
4. [Convergence model](04-convergence-model.md)
5. [Identity, Party, Owner and Host](05-identity-party-owner-host.md)
6. [Property, Destination and Unit](06-property-destination-unit.md)
7. [Relationship and authority](07-relationship-authority.md)
8. [Entry modes, invitations and claims](08-entry-modes-invitations-claims.md)
9. [Property prerequisites](09-property-prerequisites.md)
10. [Owner/Host architecture](10-owner-host-architecture.md)
11. [Publication, Verification and Managed boundary](11-publication-verification-managed.md)
12. [Inventory readiness](12-inventory-readiness.md)
13. [Booking participation](13-booking-participation.md)
14. [Stay operations prerequisites](14-stay-operations-prerequisites.md)
15. [Entry-mode matrix](15-entry-mode-matrix.md)
16. [Cross-context projections](16-cross-context-projections.md)
17. [Change, transfer and history](17-change-transfer-history.md)
18. [Duplicate and claim conflict](18-duplicate-claim-conflict.md)
19. [C1 compatibility](19-c1-compatibility.md)
20. [B1–B5 compatibility](20-b1-b5-compatibility.md)
21. [TBD and policy register](21-tbd-policy-register.md)
22. [Domain/workflow/authority gaps](22-domain-workflow-authority-gaps.md)
23. [V0 and source traceability](23-traceability.md)
24. [C2 report](../CP8-C2-HOST-OWNER-PROPERTY-ONBOARDING-REPORT.md)

## Canonical guardrails

`Identity ≠ Party ≠ Account`; `Owner ≠ Primary Host ≠ Co-host`; Ownership, Hosting Authority, Booking Authority, Inventory Authority and Financial Beneficiary remain separate. A Property creator, claim, invitation or association does not create truth or authority by itself. `Property ≠ Bookable Unit`; existence, publication, Availability, Bookability, Verification and Managed are separate outcomes. Destination membership does not grant BQL or commercial authority. C2 introduces no onboarding state machine.

## Stop condition

C2 ends at this Host/Owner + Property onboarding documentation pass. C3 is documented separately. CP8-C4 Butler onboarding, Workspace/Surface UX, Detailed Interaction, Design System, Prototype, Acceptance Package and implementation remain not started.
