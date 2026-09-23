# CP8-D1 — Workspace & Surface Architecture

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-D Workspace / Surface UX**  
> Status: **ACCEPTED AS BASELINE FOR CP8-D2**  
> Freeze status: **NOT FROZEN**  
> Scope: **D1 baseline for D2** · 2026-09-20

D1 refines the accepted CP6 Information Architecture into a V0 surface-responsibility model. It defines what each Working Context is responsible for, which shared canonical objects it projects, which actions may originate there, what authority remains required, and how handoffs work. It does not define screens, wireframes, final navigation, visual design, components, prototypes, APIs or implementation.

## Reading order

1. [Overview](01-overview.md)
2. [Surface architecture principles](02-surface-architecture-principles.md)
3. [Public Marketplace](03-public-marketplace.md)
4. [Guest Stay Access](04-guest-stay-access.md)
5. [Host Workspace](05-host-workspace.md)
6. [Owner perspective](06-owner-perspective.md)
7. [Sale Workspace](07-sale-workspace.md)
8. [Butler Context](08-butler-context.md)
9. [Destination/BQL Context](09-destination-bql-context.md)
10. [Stayora Admin](10-stayora-admin.md)
11. [Working Context switching](11-context-switching.md)
12. [Resource scope](12-resource-scope.md)
13. [Object ownership vs surface responsibility](13-object-surface-responsibility.md)
14. [Cross-surface handoffs](14-cross-surface-handoffs.md)
15. [Journey × Surface matrix](15-journey-surface-matrix.md)
16. [Onboarding × Surface matrix](16-onboarding-surface-matrix.md)
17. [Surface entry conditions](17-surface-entry-conditions.md)
18. [Empty and partial contexts](18-empty-partial-contexts.md)
19. [Attention and exception model](19-attention-exception-model.md)
20. [Status presentation](20-status-presentation.md)
21. [Money visibility](21-money-visibility.md)
22. [Privacy and need-to-know](22-privacy-need-to-know.md)
23. [Device and usage context](23-device-usage-context.md)
24. [Surface responsibility cards](24-surface-responsibility-cards.md)
25. [Surface/Object matrix](25-surface-object-matrix.md)
26. [Surface/Action matrix](26-surface-action-matrix.md)
27. [Shared Object Detail](27-shared-object-detail.md)
28. [Navigation responsibility](28-navigation-responsibility.md)
29. [TBD/policy register](29-tbd-policy-register.md)
30. [Gap register](30-gap-register.md)
31. [V0/source traceability](31-traceability.md)
32. [D1 report](../CP8-D1-WORKSPACE-SURFACE-ARCHITECTURE-REPORT.md)

## Canonical model

`Actor / Identity → Working Context → Responsibility → Resource Scope → Canonical Object / Projection → User Task → Authorized Action → System Response → Cross-Context Handoff`.

One canonical truth can have contextual projections. A surface is not a domain owner, a role dashboard or a permission bundle.

## Stop condition

D1 is the accepted surface-responsibility baseline for [CP8-D2 Task & Screen Architecture](../d2-task-screen-architecture/README.md). Detailed interaction, wireframes, CP8-E Detailed Interaction, CP8-F/G/H and implementation remain not started.
