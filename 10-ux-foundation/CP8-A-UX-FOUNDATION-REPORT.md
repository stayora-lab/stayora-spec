# CP8-A — UX Foundation Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Status: **ACCEPTED AS BASELINE FOR CP8-B**  
> Freeze status: **NOT FROZEN**  
> Date: 2026-09-19

## 1. Executive Summary

CP8-A has created the UX reasoning layer needed before Critical Journey and visual work. It translates CP1–CP7 into an explicit chain:

```text
Identity → Working Context → Resource Scope → Responsibility
→ User Goal / Task → Domain Object → Authority → Surface → Interaction
```

The work preserves the product's most important separations: Identity/Role/Permission, relationship/authority, ownership/hosting authority, Request/Booking/Stay, External Accommodation/Stayora Booking, Inventory/Availability, Payment/Entitlement, Settlement/Payout, Incident/Finding/Responsibility/Consequence and Verification Review/Status.

The result is **READY WITH CONDITIONS** for a later CP8-B Critical Journeys pass. The CP8-A deliverables are present for Founder/Product Architect review; they do not close upstream TBDs, create screens or start CP8-B.

## 2. Sources Reviewed

The review read the canonical source layers required by the task:

- [Start Here](../00-start-here/README.md), [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), [Glossary](../00-start-here/GLOSSARY.md), [Decision Register](../00-start-here/DECISIONS.md) and [Roadmap Reconciliation Report](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- CP1 Product Foundation, including principles, actors, destination, trust, money, Oceanami Pilot, metrics, scope and open questions.
- CP2 [Domain Map, Glossary and Invariants](../02-domain/README.md).
- CP3 [Actor Authority](../03-actor-authority/README.md) and [Core Workflows](../04-core-workflows/README.md).
- CP4 [State Machines and Policies](../05-state-machines-policies/README.md).
- CP5 [Oceanami V0 Scope](../06-v0-scope/README.md), success thesis, critical journeys, capability matrix, domain boundaries and pilot metrics.
- CP6 [Information Architecture](../07-information-architecture/README.md), including context, surfaces, workspaces, navigation and journey validation.
- CP7 [Conceptual Data Model](../08-conceptual-data-model/README.md), including object ownership, projections, provenance, temporal validity and invariants.
- CP7 [Supporting Persistence Architecture](../09-database-design/README.md) as a constraint reference only; it was not treated as superior product truth.

Source priority follows the canonical Source of Truth. Existing `CONFIRMED`, `WORKING MODEL`, `HYPOTHESIS`, `TBD`, `OUT OF SCOPE — V0` and `SUPERSEDED` statuses remain unchanged.

## 3. Files Created / Changed

### Created

- [CP8-A README](README.md)
- [UX Principles](01-ux-principles.md)
- [Actor, Working Context and Responsibility Model](02-actor-context-responsibility.md)
- [Surface Responsibility Model](03-surface-responsibility.md)
- [Cross-Context Domain Truth](04-cross-context-objects.md)
- [UX Language and Semantics](05-ux-language-semantics.md)
- [V0 UX Traceability Map](06-v0-traceability.md)
- [UX Blocker / TBD Register](07-ux-blocker-register.md)
- [V0 Onboarding Prerequisites](08-onboarding-prerequisites.md)
- This report.

### Upstream index files changed

- [`outputs/README.md`](../../README.md) — current-position index now points to CP8-A.
- [`00-start-here/README.md`](../00-start-here/README.md) — checkpoint table and reading order now identify CP8-A as the current draft pass.
- [`00-start-here/SOURCE_OF_TRUTH.md`](../00-start-here/SOURCE_OF_TRUTH.md) — current checkpoint pointer now identifies CP8-A; CP8-B remains not started.

These are status/index corrections only. No CP1–CP7 product, domain, authority, workflow, state, policy, V0 or data-model decision was edited. The prior roadmap report remains a historical reconciliation artifact; its statement that CP8 had not started is true at the time it was written.

## 4. UX Principles Derived

The principles are documented in [01-ux-principles.md](01-ux-principles.md):

1. Make decision-relevant truth visible.
2. Make authority legible at the action boundary.
3. Organize around responsibility, not actor labels or database shape.
4. Show one shared truth through contextual projections.
5. Keep commitment states visibly distinct.
6. Keep external accommodation operationally first-class without fabricating commerce.
7. Treat manual assistance as an integrity-preserving path.
8. Use progressive complexity without hiding material risk.
9. Make exceptions and uncertainty actionable.
10. Keep V0 focused on pilot evidence.
11. Separate trust, verification and reputation signals.
12. Preserve privacy and information minimization by relationship.

Each principle includes its source rationale, affected actors/surfaces, UX implication and explicit non-authorization boundary. In particular, the principles do not grant permissions, add state, create V0 capability or choose unresolved policy.

## 5. Actor / Working Context Model

[02-actor-context-responsibility.md](02-actor-context-responsibility.md) models Guest, Owner/Legal Owner, Primary Host, Co-host, Sale, Butler, Destination/BQL and Stayora Admin. It explicitly permits one Identity to hold multiple capacities and contexts while retaining acting capacity and authority basis per critical action.

For each context the document records purpose, responsibilities, resource scope, domain objects, action families, normal visibility, information that should normally remain out of scope, dependencies and open questions. Visibility is repeatedly qualified as relationship/lifecycle/need-to-know visibility; it is never presented as permission.

No technical RBAC/ABAC, new actor, new role, permission bundle or authority precedence was introduced.

## 6. Responsibility Model

The responsibility model follows the CP3 and CP6 boundary:

- Guest understands demand/Booking/Stay/access and reports or reviews within scope.
- Owner/Legal Owner represents ownership; it does not automatically imply Primary Host, beneficiary or payout authority.
- Primary Host anchors hosting/commercial responsibility and may delegate only valid scoped capability.
- Co-host acts only within explicit delegated scope.
- Sale helps a Guest discover supply and progress attributable commerce; Sale does not accept a Request merely by role.
- Butler executes assigned Stay operations; Butler approval is not assignment and operational visibility is not commercial authority.
- Destination/BQL coordinates destination-scoped operations; destination scope is not global commercial authority.
- Stayora Admin handles assigned cases/policy/audit actions; Admin is not an unrestricted super-user or silent impersonator.

The task families are responsibility-oriented and do not prescribe screen layout, navigation labels or workflow transitions.

## 7. Surface Responsibility Model

[03-surface-responsibility.md](03-surface-responsibility.md) preserves CP6 surfaces:

- Public Marketplace — discovery, Availability, Public Price, trust and Request/consultation entry.
- Guest Stay Access — valid Stay arrival, access, operations, help and review.
- Host Workspace — supply, Inventory, Requests, Bookings/Stays, external records, relationships, quality and scoped Money.
- Sale Workspace — demand-led discovery, Request, attributed Booking/Stay and own economics.
- Operations — Butler and Destination/BQL responsibilities for Stay/access/issues.
- Stayora Admin — applications, eligibility, Verification, Incidents, conflicts, Money/Settlement, Leads, Destinations and Audit.

For each surface, the report document identifies who enters, why, supported responsibilities, canonical objects, actions that belong, actions that do not belong, cross-surface handoffs, privacy/authority boundaries and V0 scope. No screen or route has been created.

## 8. Cross-Context Domain Truth Findings

[04-cross-context-objects.md](04-cross-context-objects.md) traces the same Booking Request, Booking, Stay, Inventory/Availability, Property/Bookable Unit and Incident through Guest, Host, Sale, Butler, BQL and Admin contexts.

The main findings are:

- A Request is visible to Guest/Sale/Host for different reasons but remains commercial intent, not a pending Booking or Inventory hold.
- A Booking is confirmed commercial truth; it can provide an Accommodation Basis without becoming the Stay.
- A Stay is operational truth and can arise from Stayora Booking or External Accommodation.
- Inventory/Availability is one derived truth over effective commitments; Searchability and actor-specific Bookability remain separate.
- Property and Bookable Unit are supply concepts, not authority shortcuts.
- Incident supports evidence and response; downstream Finding, Responsibility and Consequence remain separate domain outcomes.

External Booking is explicitly treated as a commerce/booking record created outside Stayora that may be referenced by Inventory and/or Stay. UX must not route it through Stayora Booking merely for convenience.

## 9. Traceability to V0

[06-v0-traceability.md](06-v0-traceability.md) uses the exact CP5 validation dimensions:

1. **Inventory Trust** — truthful effective Availability, conflict visibility and correct Host/Sale/Guest decisions.
2. **Network Adoption** — voluntary return by Host, Sale, Butler and BQL to role-appropriate shared truth.
3. **Destination Stay Coverage** — representation and operations for actual stays regardless of booking source.
4. **Commerce Validation** — real Request → authorized commitment/payment condition → confirmed Booking → Stay paths.

Each row maps actor/context, responsibility, CP5 critical journey, CP6 surface, CP2/CP7 domain truth, CP3 authority source, CP4 state/policy and an open question. Numeric metric targets remain hypotheses and were not converted into UX requirements.

## 10. UX Terminology Findings

[05-ux-language-semantics.md](05-ux-language-semantics.md) recommends qualified canonical language rather than renaming concepts. Terms that must remain distinct in user-facing behavior include Request vs Booking, Booking vs Stay, External Accommodation/External Booking vs Stayora Booking, Availability vs Bookable, temporary commitment vs confirmed Booking, Payment Required vs Payment Received/Paid, Payment `UNKNOWN` vs failure/default, Completed Stay vs Checkout, Stayora Verified vs Identity Verification/Verified Stay, Review Right vs Review, and Incident vs Finding/Responsibility/Consequence.

This register deliberately does not finalize public copy for payment, cancellation, QR/privacy, Verification evidence or Incident consequences.

## 11. Onboarding Prerequisites

[08-onboarding-prerequisites.md](08-onboarding-prerequisites.md) identifies minimum truth required before V0 participation:

- Host/Owner: Identity/Party relationship, valid Primary Host/delegated authority, eligibility/publish conditions and scoped resource access.
- Property/Bookable Unit: Property/Destination representation, V0 Unit scope, listing/Public Price, Inventory source/action authority and relationships.
- Sale: application/eligibility, Sale–Host relationship, scoped discovery/Request access and manual lead path; no Host acceptance authority from role alone.
- Butler: application/eligibility, valid Property/Stay assignment, operational need-to-know access and no default commercial/financial authority.

These are prerequisites, not forms or onboarding flows. Legal/KYC/compliance policy remains unresolved where the upstream documents mark it unresolved.

## 12. UX Blockers / TBDs

[07-ux-blocker-register.md](07-ux-blocker-register.md) classifies unresolved issues:

- **A — Not a UX blocker:** Affiliate economics, Commissionable Booking Value/tax treatment, Verification and Reputation mechanics, lead automation, split stay/unit move/extension and all visual/implementation work.
- **B — Local UX blocker:** Guest QR/privacy fields and lifecycle, concrete authority edge-case handling, Payment `UNKNOWN` action language and minimum external operational fields.
- **C — Journey blocker:** inventory conflict resolution, Payment Default grace/reconciliation, cancellation/no-show/refund/exception Settlement, and Completion blockers/authority.
- **D — CP8 blocker:** none for CP8-A.

The absence of a D blocker means the UX reasoning system can be documented. It does not mean the C-level policy questions are solved; they must be revisited before affected Critical Journeys are specified.

## 13. Contradictions or Missing Upstream Truth

No new contradiction was introduced by CP8-A. The following upstream gaps remain visible and are carried forward:

- External commerce must remain an External Accommodation/External Booking concept referenced by Inventory and/or Stay; it must not become a Stayora Booking by UX naming.
- CP7's one-Unit/continuous-range V0 persistence direction is qualified and does not close split-stay, unit-move or extension semantics.
- Guest QR/link field, lifecycle, privacy and consent details are not fully selected.
- True/late Inventory Conflict handling, Payment `UNKNOWN`/Default reconciliation, grace duration and exception economics remain open.
- Exact authority precedence, delegation propagation, dual-capacity/self-dealing and financial grants remain open.
- Verification assessment/review evidence and Reputation weighting are not final policy.
- Owner vs Primary Host, legal owner/beneficiary and payout visibility remain distinct; onboarding cannot collapse them.
- CP5 records manual-assisted policy paths; CP8-A does not turn them into automation.

These are not documentation errors to solve in CP8-A. They are explicit inputs to later Founder/Product Architect decisions.

## 14. Readiness for CP8-B Critical Journeys

**READY WITH CONDITIONS.**

CP8-A provides the actor/context/responsibility chain, surface boundaries, cross-context truth model, UX terminology, V0 traceability and onboarding prerequisites needed to begin CP8-B. Conditions are:

1. Preserve all upstream status labels and unresolved blockers.
2. Revisit C-level payment, conflict, exception and completion rules before designing the affected journeys.
3. Keep Guest QR/privacy and field-level access decisions explicit rather than allowing prototypes to choose them silently.
4. Do not treat this foundation as a screen specification or visual design approval.

CP8-B has **not started**.

## 15. Validation

- Required CP1–CP7 and Start Here sources reviewed: **PASS**.
- Actor/context model traces to CP3/CP6 and preserves multi-capacity Identity: **PASS**.
- Authority statements trace to CP3; no technical permission model added: **PASS**.
- Lifecycle/semantic statements trace to CP4 and CP7; no new state or transition added: **PASS**.
- V0 claims trace to CP5's four validation dimensions, critical journeys and capability boundary: **PASS**.
- Surface claims trace to CP6; no screen, route or component created: **PASS**.
- Domain-object semantics trace to CP2/CP7; External Booking is not routed through Stayora Booking: **PASS**.
- Supporting persistence architecture remains a constraint reference only: **PASS**.
- Existing TBD/WORKING MODEL/HYPOTHESIS/OUT OF SCOPE/SUPERSEDED statuses were not silently closed: **PASS**.
- New product actor, permission, capability, state, lifecycle transition or V0 scope added: **NONE**.
- Wireframe, screen design, visual styling, Figma artifact, prototype, API, migration or code created: **NONE**.
- CP8-B Critical Journeys started: **NO**.
- Markdown links in the expanded canonical tree: **PASS — 125 Markdown files, 0 broken relative links**.

## Review request

Return this CP8-A artifact to the Founder and Product Architect for review. Do not mark CP8 complete or freeze CP8-A until that review is explicitly accepted.
