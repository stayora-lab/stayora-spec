# CP8-C1 — Onboarding Architecture

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-C Onboarding**  
> Status: **ACCEPTED AS BASELINE FOR CP8-C2**  
> Freeze status: **NOT FROZEN**  
> Scope: **C1 only** · 2026-09-20

C1 defines the shared conceptual architecture for onboarding people, Parties, relationships, resources, Working Contexts, eligibility and authority into Stayora V0. It is the accepted baseline consumed by [CP8-C2 Host/Owner + Property Onboarding](../c2-host-owner-property-onboarding/README.md). It does not design detailed Sale or Butler onboarding flows.

## Reading order

1. [C1 overview](01-overview.md)
2. [Shared onboarding reasoning model](02-shared-reasoning-model.md)
3. [Identity / Party / Capacity](03-identity-party-capacity.md)
4. [Relationship architecture](04-relationship-architecture.md)
5. [Resource relationship mapping](05-resource-relationships.md)
6. [Entry modes](06-entry-modes.md)
7. [Invitation boundary](07-invitation-boundary.md)
8. [Claim / evidence boundary](08-claim-evidence-boundary.md)
9. [Working Context activation](09-working-context-activation.md)
10. [Authority establishment](10-authority-establishment.md)
11. [Platform eligibility](11-platform-eligibility.md)
12. [Property prerequisites](12-property-prerequisites.md)
13. [Host / Owner architecture](13-host-owner-architecture.md)
14. [Sale architecture](14-sale-architecture.md)
15. [Butler architecture](15-butler-architecture.md)
16. [Multi-capacity stress tests](16-multi-capacity-stress-tests.md)
17. [Completion outcomes](17-onboarding-completion-outcomes.md)
18. [Cross-context effects](18-cross-context-effects.md)
19. [Correction / revocation / history](19-correction-revocation-history.md)
20. [Alternative/failure boundaries](20-alternative-failure-boundaries.md)
21. [B1–B5 traceability](21-b1-b5-traceability.md)
22. [TBD and policy register](22-tbd-policy-register.md)
23. [Domain/workflow/authority gaps](23-domain-gaps.md)
24. [V0/source traceability](24-traceability.md)
25. [C1 report](../CP8-C1-ONBOARDING-ARCHITECTURE-REPORT.md)

## Canonical model under review

```text
Identity
  → Party / capacity / acting capacity
  → relationship to resource or Party
  → Working Context projection
  → platform eligibility and explicit authority/assignment
  → usable, scoped product context
```

This is a reasoning model, not a universal lifecycle or permission bundle. Identity, Party, Account, Role, Relationship, Capacity, Authority, Assignment, Working Context and Eligibility remain separate concepts.

## Stop condition

C1 ends at this shared onboarding architecture and review report. C2 is documented separately. Sale and Butler onboarding flows, Workspace/Surface UX, Detailed Interaction, Design System, Prototype, Acceptance Package and Implementation remain not started.
