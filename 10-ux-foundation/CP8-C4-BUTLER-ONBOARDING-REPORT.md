# CP8-C4 — Butler Onboarding Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-C Onboarding**  
> Status: **ACCEPTED AS BASELINE FOR CP8-D2**  
> Freeze status: **NOT FROZEN**  
> Scope: **CP8-C4 only** · 2026-09-20

## 1. Executive Summary

C4 documents the minimum Oceanami V0 Butler onboarding architecture. It separates Butler capacity, operational eligibility, Assignment, resource/function scope, Working Context, operational responsibility, action authority, evidence and downstream consequence authority. It supports B4 Stay Operations and B5 Inventory handoff without making Butler a Host, Property manager, Booking/Inventory controller or financial/consequence authority. C4 remains an accepted baseline consumed by D1 and D2.

**Readiness: READY WITH CONDITIONS.** The architecture is coherent for Founder/Product Architect review. Eligibility criteria, assignment grantors/scope, Check-in/Checkout grants, active-Stay replacement, Incident escalation, need-to-know privacy and operational-to-Inventory handoff policy remain explicit TBDs. C4 is not frozen.

## 2. Sources Reviewed

- CP1–CP7 canonical Product Foundation, Domain, Actor Authority, Workflows, State/Policy, V0, IA and Conceptual Data Model.
- [Roadmap & Source-of-Truth Reconciliation Report](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- [CP3 actor catalog](../03-actor-authority/01-actor-catalog.md), [capabilities](../03-actor-authority/02-authority-capabilities.md), [delegation/scope](../03-actor-authority/04-delegation-and-scope.md).
- [CP4 Stay/Incident lifecycles](../05-state-machines-policies/04-stay-lifecycle.md), [Incident](../05-state-machines-policies/07-incident-lifecycle.md), [eligibility](../05-state-machines-policies/09-role-application-and-eligibility.md).
- [CP5 V0 critical journeys/boundaries](../06-v0-scope/03-critical-journeys.md), [CP6 operations workspace](../07-information-architecture/06-operations-workspaces.md), [CP7 provenance/quality](../08-conceptual-data-model/08-provenance-temporal-history.md).
- Accepted [CP8-A](README.md), [B4](b4-stay-operations/README.md), [B5](b5-inventory-intervention/README.md), [C1](c1-onboarding-architecture/README.md), [C2](c2-host-owner-property-onboarding/README.md) and [C3](c3-sale-onboarding/README.md).

## 3. Files Created / Changed

Created the C4 folder with overview, onboarding journey, entry modes, capacity/eligibility, Assignment architecture/authority, Property versus Stay scope, context activation, need-to-know, pre-arrival/readiness, arrival/Check-in, in-Stay operations, Incident/evidence, Inventory handoff, Checkout, completion handoff, multi-capacity stress tests, Assignment history, multiple Butler, BQL/Destination, Guest/privacy, projections, alternatives, C1–C3 and B1–B5 compatibility, TBD register, gaps, detailed step matrix and traceability. Updated CP8 indexes, C3 status/report, Start Here, Source of Truth, outputs README and historical current-pass pointers to identify C4 as current.

No CP1–CP8-C3 substantive product, domain, authority, workflow, lifecycle, policy, V0 or data-model decision was changed.

## 4. Canonical Butler Onboarding Architecture

`Identity → Butler capacity / operational relationship → operational eligibility → Assignment → resource/function scope → Butler Working Context → bounded operational responsibility`.

Assignment is a relationship, not unrestricted Authority. Separate action capabilities remain required.

## 5. Butler Entry Mode Findings

Existing Identity assignment, invitation, Host/delegated operational setup, Admin-assisted setup, Destination/BQL-assisted setup where explicitly supported and manual V0 setup are conceptual modes. Technical invitation and assignment mechanisms remain unspecified.

## 6. Butler Capacity / Eligibility Findings

Butler capacity, eligibility and Assignment are independent. C4 invents no training, ranking, HR, KYC, certification or performance criteria. Manual-assisted eligibility is acceptable with provenance and audit.

## 7. Assignment Architecture Findings

Assignment connects eligible Butler to a Property, Stay, Destination/function or other canonically supported scope with validity, responsibilities, information projection and history. It does not create a universal hierarchy or state machine.

## 8. Assignment Authority Findings

Host/Primary Host or delegated operational authority, Stayora Admin function and Destination/BQL function may participate only where explicit authority exists. Ownership and Destination visibility alone do not assign. Grantor, scope, consent and propagation remain TBD where silent.

## 9. Property vs Stay Assignment Findings

Property responsibility, Stay-specific assignment, multiple Stays and replacement are compatible with existing architecture. Temporary replacement and active-Stay handoff require workflow policy; no workforce scheduling is introduced.

## 10. Butler Context Activation

Context becomes useful after Identity, eligibility, Assignment and scope are sufficient. It projects operational truth but does not grant permission or create `BUTLER_ACTIVE`.

## 11. Need-to-Know Information Findings

Butler may need assigned Property/Unit, arrival/departure, permitted Guest contact, Stay status, access/readiness and Incident information. Owner/Sale economics, payment/settlement, unrelated Guest data, identity documents, unrelated Stays and private authority data remain outside automatic visibility.

## 12. Pre-Arrival / Readiness Findings

Butler may prepare and report readiness evidence. Preparation/Ready is a milestone/projection, not a Stay state and not a guarantee of Check-in or Availability.

## 13. Arrival / Check-in Findings

Expected arrival, physical arrival, access and Check-in remain distinct. Assignment does not automatically grant Check-in authority; explicit action scope and evidence are required where policy says so.

## 14. In-Stay Operations Findings

Assigned Butler may support Guests, coordinate operations, observe issues and record evidence within scope. Butler is not Property manager, Host, commercial decision-maker, financial resolver or Inventory controller.

## 15. Incident / Evidence Boundary

Observation → report/Incident/evidence → operational escalation → authorized decision → possible downstream action. Incident, Finding, Responsibility and Consequence remain separate. No automatic refund, blame, Block, penalty or Verification/Reputation change.

## 16. Operational → Inventory Handoff

Butler evidence may be evaluated by authorized Inventory actors for a Maintenance/Unusable Block or other canonical basis. Butler does not mark unavailable or create/release a Block from Assignment/report alone.

## 17. Checkout Findings

Physical departure, Checkout, Stay Completion and Inventory release remain distinct. Butler may record Checkout where explicitly authorized; Checkout does not release Inventory or complete Stay automatically.

## 18. Completion Handoff Findings

Butler contributes departure/condition/Incident evidence to Stay/Operations completion evaluation. Butler cannot settle, refund, assign damage liability, deduct Owner, change Reputation or change Verification.

## 19. Butler + Host Findings

One Identity can act as Butler and Host under separate contexts. A Butler Incident report and a Host-authorized action remain separately attributable; Assignment does not create Host Authority.

## 20. Butler + Owner Findings

Ownership and Butler Assignment remain distinct. Owner does not automatically become Butler; Butler does not become Owner or gain Owner/financial authority.

## 21. Butler + Sale Findings

Sale and Butler capacities remain independent. Sale attribution does not affect Butler authority; Butler Assignment does not affect Sale eligibility or attribution.

## 22. Assignment Change / Historical Truth

Creation, replacement, expiry, scope correction and revocation affect future context/actions. Valid prior operational actions retain Identity, capacity, Assignment, authority, resource, time and result.

## 23. Multiple Butler Findings

Multiple Butlers and operational participants are compatible where canonical scope permits. Each Assignment is scoped and auditable; C4 does not invent hierarchy, primary Butler state, shifts or allocation engine.

## 24. BQL / Destination Boundary

Destination/BQL may consume scoped operational information. Visibility does not grant Assignment, Booking, Inventory or commercial authority. Any legitimate assignment role requires explicit function and grantor.

## 25. Guest / Privacy Boundary

Butler receives only need-to-know Guest/Stay operational information. Exact fields, consent, retention, QR/access linkage and privacy implementation remain TBD.

## 26. Cross-Context Projection Findings

Butler, Host/Owner, Guest, Destination/BQL, Admin, Sale and Public Marketplace projections change only with their own truth and scope. Incident and Inventory handoff do not automatically create public or commercial consequences.

## 27. Alternative / Failure Paths

Existing Identity, pending/denied eligibility, missing/out-of-scope Assignment, wrong resource, unauthorized Booking/Inventory/financial action, Incident reporting, active-Stay replacement, multiple reports, Host unavailable, BQL escalation and Guest privacy restrictions are covered. Open behavior remains policy/workflow/authority TBD.

## 28. C1–C3 Compatibility

C4 preserves C1's chain and does not modify C2 Owner/Host/Property or C3 Sale semantics. Assignment is not a Relationship/Authority shortcut; multi-capacity Identity remains independent.

## 29. B1–B5 Compatibility

B1/B3 commerce remains independent; B2 External Accommodation can produce operational Stay truth; B4 receives a legitimate Butler context without changing Stay lifecycle; B5 receives evidence for authorized evaluation, never direct Inventory mutation. No accepted journey is silently changed.

## 30. TBD / Policy Boundaries

Eligibility, assignment grantors, scope hierarchy, validity/propagation, Check-in/Checkout grants, readiness, Incident escalation, Inventory handoff, multiple Butler responsibility, Guest privacy and completion policy remain registered in [C4 TBD register](c4-butler-onboarding/28-tbd-policy-register.md).

## 31. Domain / Workflow / Authority Gaps

Gaps include eligibility policy, assignment authority/scope, active-Stay handoff, milestone/state boundary, privacy, Incident-to-Inventory handoff and manual V0 assignment operations. C4 adds no concepts to close them.

## 32. V0 Scope Check

C4 stays within Oceanami V0 operational participation and manual-assisted assignment where CP5 permits it. It excludes workforce/HR, shifts, task/maintenance suites, payroll, scoring, training platforms, Managed Operations, PMS, Channel Manager, CRM, native apps and general Incident management.

## 33. Contradictions Found

No new contradiction was introduced. Protected distinctions remain intact: capacity/eligibility/Assignment, Assignment/Authority, evidence/Inventory, Incident/Finding/Responsibility/Consequence, Check-in/Checkout/Completion/Availability and visibility/authority.

## 34. Readiness Assessment

**READY WITH CONDITIONS** for Founder/Product Architect review. C4 is not frozen. After review, perform a separate CP8-C convergence review across C1–C4 before CP8-D.

## 35. Validation

- Butler capacity, eligibility, Assignment, scope, context and authority remain distinct: passed by cross-document review.
- C1–C3 and B1–B5 compatibility: passed; no accepted journey semantics changed.
- Incident/Inventory/Stay boundary check: passed; no automatic Block, Completion, Availability or consequence introduced.
- TBD/product-decision check: passed; unresolved grantors, scope, privacy, handoff and eligibility rules remain registered.
- Markdown links: **passed** — `MARKDOWN_LINK_VALIDATION files=316 errors=0`.

## Current CP8-E closure overlay

The historical readiness assessment above is retained. C4 is covered for CP8-E exit by C1–C4 and E1–E4; Butler Assignment remains distinct from Check-in/Checkout, Inventory and other authority. Exact grants, privacy, Incident escalation, active-Stay replacement and operational-to-Inventory procedure remain TBD.
