# CP8-D1 — Workspace & Surface Architecture Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-D Workspace / Surface UX**  
> Status: **ACCEPTED AS BASELINE FOR CP8-D2**  
> Freeze status: **NOT FROZEN**  
> Scope: **CP8-D1 baseline for CP8-D2** · 2026-09-20

## 1. Executive Summary

D1 refines accepted CP6 Information Architecture into a V0 surface-responsibility architecture. It preserves seven canonical surfaces, one shared domain truth per object, Working Context as perspective rather than permission, explicit resource scope and CP3 authority checks. It maps B1–B5 journeys and C1–C4 onboarding outcomes across Public Marketplace, Guest Stay Access, Host, Sale, Butler, Destination/BQL and Admin contexts.

**Readiness: ACCEPTED AS BASELINE FOR CP8-D2.** The architecture is sufficient as the responsibility baseline for D2. Owner perspective split, field-level privacy, attention ordering, Admin/BQL grants, empty-context behavior and navigation labels remain explicit TBD/IA gaps. No screens, wireframes, final navigation, design system, prototype or implementation were created in D1.

## 2. Sources Reviewed

- CP1–CP7 canonical Product Foundation, Domain, Actor Authority, Workflows, State/Policy, V0, IA and Conceptual Data Model.
- [Roadmap & Source-of-Truth Reconciliation](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- CP6 [surface architecture](../07-information-architecture/01-surface-architecture.md), [context model](../07-information-architecture/02-context-model.md), Public/Guest, Host, Sale, Operations, Admin and navigation documents.
- Accepted CP8-A, B1–B5 and C1–C4 documentation.

Source priority remains Founder decisions → CP1–CP6 → CP7 conceptual model → accepted CP8 → supporting persistence → working models/references.

## 3. Files Created / Changed

Created the D1 folder with overview, principles, seven surface responsibilities, Owner perspective, context switching, scope, object ownership, handoffs, journey/onboarding matrices, entry conditions, partial contexts, attention, status, Money, privacy, device constraints, responsibility cards, Surface/Object and Surface/Action matrices, shared detail, navigation, TBD, gaps and traceability. Updated CP8 indexes, C4 status/report, Start Here, Source of Truth, outputs README and historical pointers to identify D1 as current.

No CP1–CP8-C4 substantive product, domain, authority, workflow, lifecycle, policy, V0 or data-model decision was changed. D1 is carried forward as the accepted baseline for D2; this does not imply Founder Freeze.

## 4. Canonical Surface Architecture

`Actor/Identity → Working Context → Responsibility → Resource Scope → Canonical Object/Projection → User Task → Authorized Action → System Response → Cross-Context Handoff`.

The seven CP6 surfaces remain canonical. D1 adds no top-level workspace and does not turn a surface into a domain owner.

## 5. Public Marketplace Findings

Public discovery projects Destination, Property/Unit, public trust, Public Price and derived Availability, with Request/consultation entry. It does not expose private authority, economics, conflicts or operational notes. Searchability, Availability and Bookability remain distinct.

## 6. Guest Stay Access Findings

Guest Stay Access is a scoped Booking/External Stay → Stay projection for arrival, access, Property/Unit, Butler, Destination, help and eligible review. Full account is not mandatory where canonical. QR/access is a scoped credential, not authority; privacy lifecycle remains TBD.

## 7. Host Workspace Findings

Host Workspace projects Property, Unit, Inventory, Requests, Bookings, Stays, Butler, Incidents, Quality and authorized Money. Actions remain Owner/Host/Co-host/resource-authority dependent. Calendar is derived Inventory projection, not a second calculator.

## 8. Owner Perspective Findings

CP6 does not require a separate Owner Workspace. D1 keeps Owner as a perspective within Host/Property context where appropriate, without collapsing Owner and Host. A separate Owner surface remains an IA/UX gap if later requirements establish a distinct responsibility set.

## 9. Sale Workspace Findings

Eligible Sale with active Distribution Relationship and scope can discover, prepare/share options, create/track Requests and view permitted attribution/outcomes. Sale remains separate from Host, Booking Authority, Inventory and Stay Operations.

## 10. Butler Context Findings

Eligible assigned Butler projects assigned Property/Stay/function, readiness, arrival, operations, Incident/evidence and authorized Check-in/Checkout. Assignment and visibility do not grant commercial, Booking, Inventory, financial or consequence authority.

## 11. Destination / BQL Findings

Destination/BQL projects destination-scoped arrivals, in-house operations, access, services and issues. Visibility does not create Host, Booking, Inventory, Butler Assignment or commercial authority; local Oceanami configuration remains local.

## 12. Stayora Admin Findings

Admin is exception/governance-oriented: applications/eligibility, Verification cases, Incidents, Inventory conflicts, Money exceptions, Leads, Destinations and Audit. Admin action requires function, resource, reason and provenance; Admin is not a universal super-user or impersonation shortcut.

## 13. Working Context Switching

One Identity can switch among independent Owner/Host, Sale, Butler, Guest and other contexts. Switching changes perspective, scope projection and acting-capacity label, not permission. Every action re-evaluates CP3 effective permission.

## 14. Resource Scope Findings

Destination, Property, Unit, Request, Booking, External Accommodation, Stay, Inventory Commitment/Block, Incident, Guest relationship, Sale relationship and Butler Assignment are scoped projections. No object is globally visible by default.

## 15. Object Ownership vs Surface Responsibility

CP2/CP7 domain owners remain authoritative. Surfaces own task responsibility and projection: Booking remains Booking truth even when projected to Host, Sale, Guest, Butler, BQL or Admin; Stay and Incident are not duplicated per context.

## 16. Cross-Surface Handoffs

Public/Sale → Request → Host; Host → confirmed Booking → Guest Stay Access; External Commerce → Inventory/Stay → Host/Operations/Guest; Host → Butler; Butler → Incident/evidence → responsible authority; Operations → authorized Inventory; Stay → completion; Admin ↔ scoped exceptions. Handoff transfers responsibility/perspective, not authority or object ownership.

## 17. Journey × Surface Findings

B1–B5 are mapped end-to-end: B1 Public/Sale → Host → Guest/Operations; B2 Host/Admin/Inventory → Stay/Operations/Guest; B3 Public/Guest → Host → Operations/Guest; B4 Host/Butler/BQL/Guest; B5 Host/Operations → Inventory → derived public/Sale views and exceptions. No journey disappears between surfaces.

## 18. Onboarding × Surface Findings

C1–C4 outcomes map to partial or usable contexts: identity alone has no private workspace; Owner without Host authority has partial Host/Property context; Sale eligibility without relationship has no supply scope; Butler eligibility without Assignment has no operational context; unpublished Property stays outside Public Marketplace. No UX convenience shortcut creates permission.

## 19. Surface Entry Conditions

Public is open; Guest requires scoped Stay/access basis; Host requires relationship and scope; Sale requires eligibility, Distribution Relationship and scope; Butler requires eligibility and Assignment; BQL requires Destination/function relationship; Admin requires explicit staff function/resource authority. These are conceptual, not authentication implementations.

## 20. Empty / Partial Context Findings

Partial contexts are legitimate and should communicate known truth and pending outcomes without fake objects, fake data or automatic permissions. D1 does not define copy or CTA behavior.

## 21. Attention / Exception Findings

Attention projects domain-owned pending Request, Inventory conflict, Payment `UNKNOWN`, Incident, external conflict, onboarding pending and Stay exception. D1 creates no generic Task domain or priority algorithm.

## 22. Status Presentation Findings

Surfaces present canonical statuses and milestones without inventing UI states. Availability is derived; Bookability contextual; Preparation/Ready is a milestone; Request/Booking/Stay/Payment states remain domain-owned; onboarding completion is per outcome.

## 23. Money Visibility Findings

Guest sees own requirements/transactions; Host/Owner sees authorized economics; Sale sees permitted attribution/earnings; Butler/BQL normally see no unrelated economics; Admin sees functionally required exceptions; Public sees Public Price only. Attribution, Commission, Settlement and Payout stay separate.

## 24. Privacy / Need-to-Know Findings

The seven surfaces use PUBLIC, relationship/resource-scoped, operational/commercial need-to-know, Admin/exception and private categories. Exact fields, QR, consent, retention and relationship-specific privacy remain TBD.

## 25. Device / Usage Context Findings

Guest Stay Access, Sale, Butler and BQL have important mobile/field usage constraints. D1 records this at architecture level only; no responsive layout or native app is defined.

## 26. Surface Responsibility Summary

Responsibility cards cover primary users, scope, objects, tasks, authorized action categories, attention, handoffs, excluded responsibilities, entry/partial conditions and V0 classification for all seven surfaces.

## 27. Surface / Object Matrix Findings

The matrix distinguishes NONE, SUMMARY, NEED-TO-KNOW, ACTIONABLE, AUTHORITY-DEPENDENT and ADMIN/EXCEPTION. It describes projections and action posture; it does not create a permission model.

## 28. Surface / Action Matrix Findings

Major Request, Booking, External Accommodation, Inventory, Incident, Check-in/Checkout, Money, attribution, Butler assignment and Property actions are mapped across contexts. Every “actionable” entry remains conditional on CP3 effective authority.

## 29. Shared Object Detail Findings

One canonical object can show distinct responsibility projections: Stay is access for Guest, commercial/responsibility for Host, outcome for Sale, operations for Butler/BQL and exception/audit for Admin. No duplicate domain objects are created.

## 30. Navigation Responsibility Findings

D1 identifies responsibility groups (Today, Requests, Bookings, Stays, Inventory, Properties, Incidents, Operations, Sales activity, Attention) without final labels, routes or sidebar design. Navigation follows responsibility, not tables.

## 31. TBD / Policy Boundaries

Owner surface split, privacy/QR, attention order, empty-context behavior, Money projection, Admin/BQL grants, local services, navigation labels and unresolved upstream behavior remain in [D1 TBD register](d1-workspace-surface-architecture/29-tbd-policy-register.md).

## 32. IA / UX / Domain / Authority Gaps

Gaps include Owner IA, contextual detail/interaction, privacy and Money policy, action grants, exception routing, Offer/Attribution/External projections and manual-assist depth. No upstream gap is silently fixed.

## 33. V0 Scope Check

D1 stays within the seven CP6 V0 surfaces and accepted CP8 journeys/onboarding. It excludes PMS, Channel Manager, Managed Operations, advanced CRM/Affiliate/lead distribution, workforce/maintenance suites, universal reputation, dynamic pricing, native apps and enterprise IAM.

## 34. Contradictions Found

No new contradiction was introduced. CP6 remains upstream; D1 preserves shared truth, contextual projections, explicit authority, separate lifecycles, privacy and Money boundaries.

## 35. Readiness Assessment

**ACCEPTED AS BASELINE FOR CP8-D2.** D1 is not frozen and does not authorize CP8-E or later work. D2 is accepted as the baseline for D3; D3 is the current execution unit.

## 36. Validation

- All seven CP6 canonical surfaces represented; no new top-level surface added.
- Shared objects remain single canonical truth with contextual projections.
- B1–B5 and C1–C4 mapped across surfaces; authority and privacy boundaries preserved.
- TBD/policy check passed; no unresolved policy was closed through UX architecture.
- Markdown links: **passed** — `MARKDOWN_LINK_VALIDATION files=349 errors=0`.
