# CP8-D2 — Task & Screen Architecture Report

> Parent: **CP8 — UX / Design System** → **CP8-D Workspace / Surface UX**
> Status: **ACCEPTED AS BASELINE FOR CP8-D3**
> Freeze status: **NOT FROZEN** · Scope: **CP8-D2 baseline for CP8-D3** · 2026-09-20

## 1. Executive Summary

D2 translates accepted D1 responsibilities into a minimum coherent V0 task and screen architecture. It gives every V0 primary task a structural home across the seven canonical surfaces, maps canonical objects and projections, and preserves authority, privacy, lifecycle and handoff boundaries. The inventory intentionally stops before final navigation, detailed interactions, visual layout, design system, prototypes or implementation.

**Readiness: ACCEPTED AS BASELINE FOR CP8-D3.** D2 provides the task/screen input for convergence. Founder/Product Architect review remains required for documented policy and IA gaps, especially Owner perspective, attention ordering, Guest credential/privacy, Admin/BQL grants, Sale economics and External Accommodation reconciliation. No TBD is closed.

## 2. Sources Reviewed

- [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), CP1–CP7 canonical documentation and [roadmap/source reconciliation](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- CP5 Oceanami V0 Scope, especially capability matrix, critical journeys and domain boundaries.
- CP6 Information Architecture: seven surfaces, context model, responsibility navigation and V0 sitemap.
- CP7 Conceptual Data Model: object semantics, Inventory/Booking/External Accommodation/Stay, Money, Incident, Verification and projections.
- Accepted CP8-A, B1–B5 and C1–C4; D1 Workspace & Surface Architecture.

Source priority remains Founder decisions → canonical confirmed product decisions → CP1–CP6 → CP7 conceptual model → accepted CP8 → supporting persistence → working models/hypotheses/references/legacy.

## 3. Files Created / Changed

Created `d2-task-screen-architecture/` with 31 linked documents covering overview, principles, seven task architectures, derivation rules, inventory, cards, consolidation, mappings, traces, hierarchy, action/attention, home/today, navigation inputs, device priority, empty states, Money, privacy, TBDs, gaps and traceability. Created this report. Updated CP8 indexes and D1 status pointers to make D2 the current draft execution unit; no upstream product/domain/authority/lifecycle/policy decision was changed.

## 4. Canonical Task → Screen Architecture

`V0 requirement → journey/onboarding outcome → surface responsibility → user job → information need → action need → screen/view concept`.

The seven surfaces remain Public Marketplace, Guest Stay Access, Host Workspace, Sale Workspace, Operations—Butler Context, Operations—Destination/BQL Context and Stayora Admin. Owner remains a Host/Property perspective. Screens are contextual projections of one canonical truth.

## 5. Screen Derivation Rules

The screen justification test requires a V0 requirement, actor/context, responsibility, unsolved job, canonical anchor, authority-dependent action, accepted journey/onboarding entry and a reason not to merge. Screen types are conceptual categories, not route or implementation page types. No screen is derived from a database table or competitor convention.

## 6. Public Marketplace Findings

`PUB-01` through `PUB-05` cover destination discovery, destination/accommodation truth, date/availability intent and Direct Guest Request entry. Public Price, public trust and derived Availability are visible at the permitted level. No checkout, private economics, authority, operational notes or fake availability state is introduced.

## 7. Guest Stay Access Findings

`GST-01` Stay Hub, `GST-02` Arrival & Access, `GST-03` Help & Operational Contact and `GST-04` Review Entry cover scoped Guest needs. A full account remains optional where canonical; QR/credential is a scoped credential, not authority. Stay remains distinct from Booking and External Accommodation.

## 8. Host Workspace Findings

`HST-01`–`HST-12` cover current responsibility, Property/Unit, Request decision, Booking, Stay operations, External Accommodation, Inventory intervention, Incidents, Butler coordination and authorized Money truth. Request Detail is the consequential decision home; Booking and Stay remain separate; Inventory remains derived.

## 9. Owner Perspective Findings

No Owner Workspace is added. Owner-specific views may project from Host/Property context only with valid relationship and authority. Owner economics, Owner Blocks and any separate IA remain explicit gaps rather than silently granting Host actions.

## 10. Sale Workspace Findings

`SAL-01`–`SAL-06` cover supply discovery, option preparation, Request creation, outcome monitoring, permitted attribution/earnings and exceptions. Sale requires eligibility, active Distribution Relationship and scope. Sale cannot accept Requests, mutate Inventory, operate Stays or see unrelated Owner economics. CRM, Affiliate Network and advanced Lead Distribution remain out of V0.

## 11. Butler Context Findings

`BUT-01`–`BUT-05` prioritize field operations: Today/Assignments, assigned Stay, readiness, Check-in, Incident/evidence and Checkout. Butler authority comes from eligibility and Assignment; no Booking, Inventory, commercial or settlement authority is implied.

## 12. Destination / BQL Findings

`BQL-01`–`BQL-04` cover arrivals/departures, active Stays, incidents, access/services and escalation within actual destination/function scope. BQL is not a Host dashboard, Booking manager, Inventory controller or workforce suite.

## 13. Stayora Admin Findings

`ADM-01`–`ADM-06` are exception/governance/manual-assist oriented: eligibility, Property/Verification, Inventory/External conflicts, Incident governance, Money exceptions and audit/provenance. Admin is function/resource scoped and not a universal super-user.

## 14. Screen Inventory Summary

The inventory contains 5 Public, 4 Guest, 12 Host, 6 Sale, 5 Butler, 4 BQL and 6 Admin concepts (42 total conceptual references). These are the minimum coherent V0 set after consolidation review; identifiers are documentation references, not routes. Manual-assisted concepts remain marked and do not imply automation.

## 15. Screen Consolidation Findings

The review kept separate concepts where canonical objects or responsibilities differ: Request vs Booking, Booking vs Stay, Property vs Unit, Incident vs Maintenance Block, and Money categories. It consolidates Sale exception attention into the activity projection where possible and keeps Today/Detail distinctions conceptual for later mobile composition. No screen remains without a justified task.

## 16. Object → Screen Findings

Destination, Property, Unit, Request, Booking, External Accommodation, Stay, Inventory Commitment/Block, Incident, Payment truth, Sale attribution and Butler Assignment each have a primary detail/home and contextual projections. No projection duplicates or owns the canonical object; external commerce can create Inventory/Stay truth without a Stayora Booking.

## 17. Task → Screen Findings

The task matrix proves a structural home for every primary V0 task: Public and Guest conversion/access, Host decisions and operations, Sale-assisted Requests, Butler field work, BQL operations and Admin exception handling. Action visibility remains authority-dependent and is never inferred from screen presence.

## 18. B1–B5 Journey → Screen Trace

- **B1 Sale-assisted Booking:** Sale discovery → option → Request → Host decision → Booking/outcome → Guest Stay Access → operations.
- **B2 External Booking → Stay:** authorized External Accommodation entry → Inventory/external conflict projection → Stay/operations/Guest → Admin reconciliation where required; no Stayora Booking required.
- **B3 Direct Guest Booking:** Public discovery → date/intent → Request → Host decision → Booking → Stay Access/operations.
- **B4 Stay Operations:** upcoming → preparation → arrival/Check-in → in-Stay → Incident → Checkout → completion handoff.
- **B5 Inventory Intervention:** evidence/Host intent → authorized Inventory intervention → derived Availability/Bookability → public/Sale projections and exceptions.

## 19. C1–C4 Onboarding → Screen Trace

Pending eligibility, partial Owner/Host relationships, unpublished Property, Sale relationship pending, unassigned Butler, active Assignment and Verification cases all have structural homes or partial-context projections. No onboarding wizard, lifecycle state or permission shortcut is invented.

## 20. Information Hierarchy Findings

Each card identifies primary, supporting, attention/exception, action-decision and provenance information semantically. D2 deliberately omits tabs, cards, columns, visual emphasis, component choices, copy and pixel hierarchy.

## 21. Detail View Findings

Detail is justified for truth/context/history, consequential decisions, handoffs and exception inspection. Request, Booking, Stay, Incident and scoped accommodation detail are justified; every database entity is not promoted to a page.

## 22. Action Placement Findings

Accept/Reject Request, record External Accommodation, Inventory intervention, Check-in, Checkout, Incident reporting, Butler assignment and publication actions have structural homes. D2 records action category, object effect and authority dependency only. Confirmation, forms, control placement and interaction sequences remain unstarted.

## 23. Attention Architecture Findings

Attention projects pending Requests, Inventory conflicts, Payment `UNKNOWN`, Incidents, external conflicts, onboarding pending and Stay exceptions into the responsible surface. No generic Task domain or priority algorithm is created; a separate attention view exists only when exception triage is the primary job.

## 24. Home / Today Findings

Host Responsibility Overview, Butler Today & Assignments, BQL Operations Today, Guest Stay Hub and Admin governance attention are justified by current-action responsibilities. Sale uses activity/outcome projections rather than a generic dashboard; Public uses discovery. These are structural concepts, not final navigation.

## 25. Navigation Inputs

D2 supplies responsibility groups and context/resource-switching needs for each surface. It does not finalize sidebar, bottom navigation, tabs, menu labels or routes.

## 26. Mobile / Field Priority

Guest access and Sale are mobile-important; Butler and BQL field operations are field-critical; Host supports mobile where operational but is desktop-important for consequential decisions; Admin is desktop-important; Public is device-neutral. No responsive breakpoint or native app is defined.

## 27. Empty / Partial / Unavailable Findings

NO DATA, NO RELATIONSHIP, NO SCOPE, NO AUTHORITY, PENDING, CONFLICT/EXCEPTION and OUT OF SCOPE are distinguished. Examples include no Requests, pending Sale relationship, unassigned Butler, unpublished Property, Payment `UNKNOWN` and Stay exception. These conditions do not create fake data or UI statuses.

## 28. Money Boundary

Money views are contextual and only where V0 requires them. Payment, Entitlement, Settlement and Payout remain separate; Attribution is not Commission Entitlement. No commission rate, collection policy, tax conclusion or payout dashboard is invented.

## 29. Privacy / Need-to-Know

Cards classify information as PUBLIC, RELATIONSHIP-SCOPED, RESOURCE-SCOPED, OPERATIONAL NEED-TO-KNOW, COMMERCIAL NEED-TO-KNOW, ADMIN/EXCEPTION-SCOPED or PRIVATE. Exact QR/contact/retention and field permissions remain policy/TBD. Screen visibility does not bypass authority.

## 30. TBD / Policy Boundaries

The D2 register preserves Owner IA, Guest credential/privacy, attention ordering, Request/payment interaction, Sale economics, Admin/BQL grants, Verification/publication presentation and External Accommodation reconciliation as unresolved. The method is known truth → required task → policy boundary → open question → interaction not finalizable.

## 31. Screen / IA / UX / Domain / Authority Gaps

Documented gaps are Owner IA, privacy/QR, attention priority, payment/confirmation policy, Admin/BQL grants, External Accommodation reconciliation, Sale economics, mobile grouping and detailed interaction. They are classified as IA, UX interaction, policy, workflow, authority or V0-scope gaps and escalated without upstream edits.

## 32. V0 Scope Check

All concepts trace to CP5 MUST BUILD or MANUAL-ASSISTED capabilities and B1–B5/C1–C4. Explicitly excluded are full PMS, Channel Manager, Managed Operations, advanced CRM, Affiliate Network, advanced Lead Distribution, workforce management, maintenance suite, universal reputation, dynamic pricing, native apps and enterprise IAM. D2 does not expand V0.

## 33. Contradictions Found

No new contradiction was introduced. The architecture preserves Request ≠ Booking, Booking ≠ Stay, External Accommodation ≠ Stayora Booking, Inventory ≠ Availability, Availability ≠ Bookability, Incident ≠ Maintenance Block, Payment ≠ Entitlement ≠ Settlement ≠ Payout, Attribution ≠ Commission Entitlement and Owner ≠ Host. Remaining upstream/policy ambiguities are recorded as TBD, not resolved.

## 34. Readiness Assessment

**READY WITH CONDITIONS** for Founder/Product Architect review. D2 is not frozen, does not close CP8-D, and does not authorize CP8-D3, CP8-E, CP8-F, CP8-G, CP8-H or implementation. Review should decide whether a small D-level convergence/navigation pass or corrective documentation is needed.

## 35. Validation

- Seven canonical surfaces represented; no new top-level workspace.
- Every inventory concept has a justified task; every V0 primary task has a structural home.
- Shared canonical objects remain single truth with contextual projections.
- B1–B5 and C1–C4 trace end-to-end.
- Request/Booking/Stay/External Accommodation/Inventory, Incident/Maintenance Block, Money and attribution boundaries preserved.
- No generic Task domain, invented lifecycle/UI status, permission shortcut, policy closure, persistence assumption, detailed interaction, layout, component, wireframe, Figma artifact, prototype, API, schema or implementation created.
- Markdown link validation is run after index updates; result recorded in final handoff.

## Current CP8-E closure overlay

The historical D2 readiness language is retained. D2/D3 V0 screen/task architecture is sufficient for CP8-E exit with E1–E4; no remaining D2/D3 family requires a new consequential interaction family. Owner remains a perspective, and attention, credential/privacy, payment/economics, Admin/BQL and external procedure details remain TBD.
