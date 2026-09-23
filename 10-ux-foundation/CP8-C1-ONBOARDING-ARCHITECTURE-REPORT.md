# CP8-C1 — Onboarding Architecture Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-C Onboarding**  
> Status: **ACCEPTED AS BASELINE FOR CP8-C2**  
> Freeze status: **NOT FROZEN**  
> Scope: **C1 only** · 2026-09-20

## 1. Executive Summary

C1 defines the shared conceptual architecture for onboarding people, Parties, relationships, resources, Working Contexts, platform eligibility, assignments and authority into Stayora V0. It prevents Host/Owner, Property, Sale and Butler onboarding from independently inventing incompatible identity or permission models.

The architecture is not `choose role → get dashboard permissions`. One Identity may hold multiple capacities; Party, Account, Relationship, Authority, Assignment, Eligibility and Working Context remain separate. Resource scope and acting capacity are explicit and auditable. Invitation and claim are proposals/evidence inputs, not authority. Onboarding completion is per outcome, not one global status.

**Readiness: READY WITH CONDITIONS.** The shared model is sufficient to proceed to later detailed onboarding journeys after Founder/Product Architect review. Identity matching, evidence thresholds, authority grants, eligibility, privacy, transfer/revocation and per-flow completion policies remain explicit TBDs. C1 does not design detailed actor flows or freeze CP8.

## 2. Sources Reviewed

- [Start Here](../00-start-here/README.md), [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), [Glossary](../00-start-here/GLOSSARY.md), [Decision Register](../00-start-here/DECISIONS.md) and [Roadmap reconciliation](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- CP1 Product Foundation, CP2 Domain Map/Glossary/Invariants, CP3 Actor Authority/Core Workflows, CP4 State Machines/Policies, CP5 Oceanami V0 Scope, CP6 Information Architecture and CP7 Conceptual Data Model.
- Accepted [CP8-A UX Foundation](README.md), [CP8-B1](CP8-B1-SALE-ASSISTED-BOOKING-REPORT.md), [CP8-B2](CP8-B2-EXTERNAL-BOOKING-TO-STAY-REPORT.md), [CP8-B3](CP8-B3-DIRECT-GUEST-BOOKING-REPORT.md), [CP8-B4](CP8-B4-STAY-OPERATIONS-REPORT.md) and [CP8-B5](CP8-B5-INVENTORY-INTERVENTION-REPORT.md).

Source priority remains Founder decisions → canonical confirmed product decisions → CP1–CP6 → CP7 conceptual model → accepted CP8 work → supporting persistence → working models/hypotheses/references.

## 3. Files Created / Changed

### Created

Inside [C1 Onboarding Architecture](c1-onboarding-architecture/README.md):

- C1 overview and shared reasoning model.
- Identity/Party/Capacity mapping.
- Relationship and resource relationship architecture.
- Entry modes.
- Invitation and claim/evidence boundaries.
- Working Context activation.
- Authority establishment and platform eligibility.
- Property prerequisites.
- Host/Owner, Sale and Butler architecture.
- Multi-capacity stress tests.
- Per-outcome onboarding completion.
- Cross-context effects.
- Correction/revocation/history.
- Alternative/failure boundaries.
- B1–B5 traceability.
- TBD/policy register.
- Domain/workflow/authority gaps.
- V0/source traceability.

This report is the required `CP8-C1-ONBOARDING-ARCHITECTURE-REPORT.md`.

### Changed

- CP8 indexes now identify C1–C4 as accepted baselines and D1 as the current draft execution unit; CP8-A and CP8-B1–B5 remain accepted baselines.
- Start Here, Source of Truth and outputs README now point to C1 as current.
- C2 consumes C1 as its shared architecture; no C1 substantive decision changed.

No CP1–CP8-B5 product, domain, authority, workflow, lifecycle, policy, V0 or data-model decision was changed.

## 4. Canonical Onboarding Architecture

```text
Identity
  → Party / capacity / acting capacity
  → relationship to Party/resource
  → platform eligibility / assignment where applicable
  → explicit authority and resource scope
  → Working Context projection
  → usable, bounded product action
```

The sequence is a reasoning model, not a universal lifecycle. Some paths begin with a resource, invitation, assignment, Admin-assisted representation or existing relationship; each still resolves identity, relationship, scope, eligibility and authority independently.

## 5. Identity / Party / Capacity Findings

Identity represents a person/account capable of acting. Party represents an individual, organization, legal or economic subject. Account is an interaction mechanism. One Identity may hold Owner, Host, Sale, Co-host, Butler and Guest capacities through separate relationships. No account-per-role duplication or enterprise organization model is introduced.

## 6. Relationship Findings

Ownership, hosting, Co-host delegation, Sale Distribution Relationship, Butler Assignment, Destination Staff relationship and Guest Booking/Stay relationship are distinct. Relationships may influence effective permission but are not automatically Authority.

## 7. Resource Relationship Findings

Destination, Property, Bookable Unit, Booking/Request, Stay and Inventory scope each require explicit association and scope. Property creation does not establish ownership, hosting, publication, Verification, Inventory or Payout. Stay association does not become Booking or Inventory authority.

## 8. Entry Mode Findings

Self-entry, invitation, authorized assignment, Admin-assisted onboarding, existing relationship discovery/claim, Property-first and actor-first entry can all be legitimate conceptual modes. C1 does not require one sequence or universal onboarding mode.

## 9. Invitation Boundary

Invitation is a proposal to an intended recipient. It is not Identity, Relationship, Authority or completed Assignment. Acceptance can establish consent/participation but only an explicit relationship/grant establishes authority. Technical invitation mechanisms remain TBD.

## 10. Claim / Evidence Boundary

Claims such as “I own this Property”, “I host this Villa”, “I work as Sale” or “I am assigned Butler” require separate evidence/relationship/eligibility/authority evaluation. Claim is not truth and C1 invents no evidence threshold or verification workflow.

## 11. Working Context Activation Findings

Guest, Owner, Host, Sale, Butler, Destination/BQL and Admin contexts become useful from scoped relationships/capacities/assignments and may project resources needed for the function. Context visibility is not permission; every privileged action still requires capability, scope, lifecycle and policy.

## 12. Authority Establishment Findings

Authority may arise from valid ownership-related, hosting, delegated Co-host, Distribution, explicit Inventory, Operations assignment or Staff function bases. Each has a grantor/source, grantee, resource scope, validity, actions enabled/not enabled, revocation boundary and audit need. No new authority type or RBAC model was created.

## 13. Platform Eligibility Findings

Known Identity, platform eligibility, commercial relationship, resource authority, Property publication eligibility, Verification and operational eligibility are separate. Verification owns supply-quality programs; Identity & Authority owns identity verification/platform eligibility. No scoring, universal KYC or universal account approval is invented.

## 14. Property Onboarding Architecture Findings

Later Property onboarding must separately establish Property existence, Destination membership, Owner/Host relationships, Units, publication eligibility, Inventory responsibility, Verification where relevant and commercial relationships. `Exists ≠ published ≠ Verified ≠ Managed`; Stayora Managed remains outside current core.

## 15. Host / Owner Architecture Findings

Owner and Host remain distinct. One Identity may hold both, or different Identities may hold them. Ownership does not automatically establish Primary Host, Booking Authority, Inventory Authority, Financial Beneficiary or Payout. Co-host authority is explicit, scoped and delegated.

## 16. Sale Architecture Findings

Sale onboarding must eventually establish Identity/capacity, platform eligibility and relevant Distribution Relationship before Sale context actions. Sale may search, prepare Offers, create Requests and receive legitimate attribution. Sale capacity does not grant Host, Booking, Inventory, payment/refund, settlement or Stay operational authority.

## 17. Butler Architecture Findings

Butler onboarding must establish eligibility, valid assignment, resource/function scope and operational context. Butler may prepare/coordinate Stay operations and record evidence where granted. Butler does not automatically gain Booking, pricing, Inventory, payment/refund, Owner, financial or Reputation/Verification consequence authority.

## 18. Multi-Capacity Identity Stress Test

Owner + Host, Sale + Co-host, Butler + another capacity, Guest later becoming Owner/Host/Sale and existing Identity invited to another resource all work with one Identity and separate acting capacities. Privileged actions remain attributable to the capacity and authority actually used.

## 19. Onboarding Completion Findings

Identity established, Party represented, relationship established, resource associated, platform eligible, assignment active, authority granted, context usable, Property represented, publication-eligible and operationally ready are independent outcomes. There is no universal `ONBOARDED` state.

## 20. Cross-Context Projection Findings

At each milestone, subject, grantor/assigner, resource context and authority projection differ. Authority grant changes only the named capability/scope. Revocation affects future actions and context, not historical valid actions. Private evidence and unrelated economics remain need-to-know.

## 21. Correction / Revocation / Historical Truth

Wrong relationships, resources, assignments, duplicate linkage, incorrect grants, revocation, Owner/Host changes, Butler reassignment and Sale relationship end use correction, supersession, replacement or explicit revocation. Prior valid actions retain actor, basis, resource and time.

## 22. Alternative / Failure Paths

The register covers existing identities, duplicate contacts, wrong recipients, invitation decline/revocation, disputed claims, unclear ownership, Owner/Host divergence, missing/revoked authority, duplicate Properties, no Host, Sale not eligible, Butler without assignment, assignment end, multiple contexts and changing resource relationships.

## 23. B1–B5 Traceability

C1 supports Sale/Host/Co-host authority for B1, external reporting/Record External Commitment scope for B2, accountless Guest participation for B3, Butler/BQL operational context for B4 and Unit × Time Inventory authority for B5. No B1–B5 semantics are changed.

## 24. TBD / Policy Boundaries

Open boundaries include identity matching, organization representation, evidence thresholds, invitation/claim workflow, context privacy, eligibility/approval, Owner/Host transfer, Sale attribution, Butler assignments, completion outcomes, revocation propagation and appeals. See [22-tbd-policy-register.md](c1-onboarding-architecture/22-tbd-policy-register.md).

## 25. Domain / Workflow / Authority Gaps

Gaps are classified as identity/domain, authority, workflow, policy, privacy, Property prerequisite and V0-scope gaps. C1 creates no aggregate, entity, actor, state, permission, enterprise IAM or technical authentication design to fill them.

## 26. V0 Scope Check

C1 stays within CP5 actors, manual-assisted approval/assignment, Property/Unit prerequisites, Guest/Host participation, Sale eligibility/relationships and Butler/Destination operational assignment. It does not expand into enterprise IAM, organization management, complex RBAC, HR/workforce, universal KYC, CRM, PMS, Channel Manager, Managed Operations, native apps or Affiliate/lead networks.

## 27. Contradictions Found

No new contradiction was introduced. C1 explicitly prevents:

- choose-role → permissions onboarding;
- Identity/Party/Account collapse;
- Relationship/Capacity → automatic authority;
- Owner → automatic Host/finance/Inventory authority;
- Invitation/claim → truth or authority;
- Assignment → commercial authority;
- Property existence → publication/Verification/Managed;
- Sale capacity → Booking/Inventory authority;
- Butler/BQL context → commercial authority;
- a universal onboarding state.

## 28. Readiness Assessment

**READY WITH CONDITIONS** for Founder/Product Architect review.

Conditions:

1. Preserve the shared reasoning model in every later onboarding journey.
2. Decide or explicitly scope identity matching, evidence, eligibility, authority grants, privacy, revocation and per-flow completion before detailed interaction/implementation work.
3. Keep detailed Host/Owner, Property, Sale and Butler journeys as later execution units.
4. Do not interpret this report as screen design, implementation authorization or Founder Freeze.

## 29. Validation

- Identity remains separate from Party and Account: **PASS**.
- One Identity can hold multiple capacities: **PASS**.
- Relationship/Capacity remains separate from Authority: **PASS**.
- Ownership remains separate from Hosting Authority: **PASS**.
- Working Context remains separate from Permission: **PASS**.
- Assignment remains separate from Commercial Authority: **PASS**.
- Invitation and Claim do not grant authority/truth automatically: **PASS**.
- Account creation is not onboarding completion: **PASS**.
- No universal Onboarding Status introduced: **PASS**.
- Resource scope and authority basis remain explicit/auditable: **PASS**.
- Revocation/correction preserves history: **PASS**.
- Property existence/publication/Verification/Managed remain distinct: **PASS**.
- Sale/Butler/Guest boundaries remain intact: **PASS**.
- C1 supports B1–B5 without changing semantics: **PASS**.
- Authority claims trace to CP3; lifecycle/status claims to CP4/CP7; V0 claims to CP5; context claims to CP6/CP8-A: **PASS**.
- No persistence assumption became product policy: **PASS**.
- No TBD silently closed: **PASS**.
- No new domain concept, actor, authority type or universal state introduced: **PASS**.
- No screen, form, wireframe, prototype, Figma, component, token, API, code, schema or migration created: **PASS**.
- No detailed actor onboarding journey or later CP8 work started: **PASS**.
- Markdown file/anchor links: **PASS — 228 Markdown files, 0 broken file/anchor links**.

Return this report to the Founder and Product Architect for review. Do not proceed automatically to detailed Host/Owner, Property, Sale or Butler onboarding, CP8-D or later work.

## Current CP8-E closure overlay

The historical readiness assessment above predates the Closure Coverage Pass. C1–C4 plus E1 generic interaction grammar provide sufficient V0 interaction architecture for CP8-E exit. Identity/capacity/relationship/eligibility/assignment/authority boundaries remain intact; eligibility, privacy, transfer/revocation and per-flow policy details remain TBD.
