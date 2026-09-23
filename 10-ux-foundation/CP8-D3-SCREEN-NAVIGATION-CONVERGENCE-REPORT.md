# CP8-D3 — Screen & Navigation Convergence Report

> Parent: **CP8 — UX / Design System** → **CP8-D Workspace / Surface UX**
> Status: **ACCEPTED AS BASELINE FOR CP8-E1**
> Freeze status: **NOT FROZEN** · Scope: **D3 baseline for CP8-E1** · 2026-09-21

## 1. Executive Summary

D3 converges the 42 D2 conceptual screen references into a responsibility-driven V0 product structure. It identifies primary destinations, contextual details, embedded projections, action entries, scoped access views and attention projections; defines context/resource switching; validates B1–B5 and C1–C4; and explicitly retains all canonical domain distinctions.

**Assessment: CP8-D ACCEPTED AS BASELINE FOR CP8-E1.** D3 is not a product freeze; Founder/Product Architect review remains required for the bounded Owner IA, Guest credential/privacy, attention ordering, payment/confirmation, Sale economics, Admin/BQL grants and External Accommodation reconciliation gaps carried into E1.

## 2. Sources Reviewed

- [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), CP1–CP7 canonical documentation and [roadmap/source reconciliation](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- CP5 Oceanami V0 Scope and CP6 Information Architecture.
- CP7 Conceptual Data Model and supporting persistence direction as constraint only.
- Accepted CP8-A, B1–B5, C1–C4, D1 and D2, including D2 inventory, cards, mappings, traces, attention, Home/Today, navigation inputs, device priorities, empty states, TBDs and gaps.

Source priority remains Founder decisions → canonical confirmed product decisions → CP1–CP6 → CP7 conceptual model → accepted CP8 → supporting persistence → working models/hypotheses/references/legacy.

## 3. Files Created / Changed

Created `d3-screen-navigation-convergence/` with 38 linked documents covering convergence principles, economy review, seven surfaces, Owner stress test, responsibility groups, navigation/context/resource architecture, object relationships, semantic stress tests, attention, Home/Today, depth, entry paths, handoff validation, empty states, device and Money/privacy boundaries, structure maps, all 42 dispositions, matrices, TBDs, gaps, exit assessment and traceability. Created this report. Updated UX indexes, Start Here/Source of Truth, D2 status and output pointers so D3 is the current draft execution unit. No CP1–CP7 or accepted CP8 product/domain/policy decision was changed.

## 4. Convergence Principles

Navigation follows durable responsibility, not tables or role labels. Contextual composition may share a structural container but never merges canonical truth. Context/resource selection is not permission. Object details and consequential actions remain reachable from the responsible context rather than becoming global destinations by default. Attention is a projection of domain facts, not a generic Task domain.

## 5. Screen Economy Findings

D3 does not optimize an arbitrary raw count. All 42 D2 references remain accounted for, but only durable responsibility groups become primary destinations. Host is reduced from 12 possible items to a small set of responsibility groups; Guest is Stay-centered; Butler and BQL are Today-centered; Admin is governance/exception-centered. No concept disappears without disposition.

## 6. Public Marketplace Convergence

`PUB-01` is the public discovery entry. `PUB-02` is contextual Destination detail; `PUB-03` is Property/Unit detail; `PUB-04` is date/Availability/Bookability intent; `PUB-05` is Request action entry. Destination, Property and Unit remain distinct; Searchability, Availability and Bookability remain distinct. No checkout or private information is introduced.

## 7. Guest Stay Access Convergence

`GST-01` is the primary scoped Stay Hub. Arrival/access is contextual `GST-02`; help/contact is contextual `GST-03`; Review is conditional action `GST-04`. Guest navigates a scoped Stay rather than a Booking workspace, and full account remains optional where canonical.

## 8. Host Workspace Convergence

Primary responsibility groups are Current Responsibility (`HST-01`), Properties & Units (`HST-02`), Requests (`HST-03`), Bookings & Stays (`HST-06`), and Inventory/operations projections (`HST-09`/`HST-10`). Request Detail (`HST-04`), Booking Detail (`HST-05`), Stay Detail (`HST-07`), External Accommodation entry (`HST-08`), Operations Coordination (`HST-11`) and Money (`HST-12`) remain contextual. Booking and Stay are related but never merged.

## 9. Owner Perspective Stress Test

Owner Identity → valid relationship → Property scope → Owner-relevant responsibility → legitimate information/action is supported through scoped Host/Property projections. Owner without Host authority cannot accept Requests or mutate Inventory. Owner economics and Owner Block actions require explicit authority. Same Identity with Host capacity switches context; it does not grant permission. No Owner Workspace is invented. The remaining Owner IA question is explicit and bounded.

## 10. Sale Workspace Convergence

`SAL-01` Supply Discovery and `SAL-04` Activity & Outcome are primary destinations. Option preparation (`SAL-02`), Request (`SAL-03`), attribution (`SAL-05`) and Sale exception (`SAL-06`) are contextual/action/attention projections. Sale remains a distribution context and cannot accept Booking Requests, mutate Inventory or operate Stays. No CRM, pipeline or commission system is created.

## 11. Butler Context Convergence

`BUT-01` Today & Assignments is the primary field destination. `BUT-02` is assigned Stay detail; `BUT-03` Check-in and `BUT-05` Checkout are action flows; `BUT-04` is Incident entry/detail. Butler remains Assignment-scoped and operational, not a workforce or Inventory manager.

## 12. Destination/BQL Convergence

`BQL-01` Operations Today is primary. `BQL-02` active Stay collection, `BQL-03` Incident/Exception and `BQL-04` Access/Services are contextual. BQL remains destination/function scoped and does not become Host, Booking, Inventory, Butler or Admin.

## 13. Admin Convergence

`ADM-01` Governance & Attention and `ADM-06` Audit & Provenance are durable Admin destinations. Property/Verification, Inventory/External, Incident and Money exception views (`ADM-02`–`ADM-05`) are contextual governance projections. Admin remains function/resource scoped, manual-assisted and auditable; it is not universal CRUD or super-user authority.

## 14. Responsibility Groups

Responsibility groups are documented for all seven surfaces. Each states why it exists, tasks, concepts, canonical objects, attention inputs and authority dependencies. They are conceptual navigation inputs, not visual menus.

## 15. Navigation Architecture Findings

The product structure has four conceptual layers: Working Context, primary responsibility destination, contextual object entry and action/attention entry. No sidebar, bottom navigation, icons, routes, tabs, colors or visual hierarchy is defined.

## 16. Context / Resource Switching

Host → Sale changes responsibility projection; Property A → Property B changes resource projection; BQL Destination A → B changes destination scope; Butler Assignment changes operational scope; Guest scoped access opens a Stay. Each switch re-evaluates effective authority, relationship, resource scope, state and policy. Switching is never a permission grant.

## 17. Object Detail Relationships

Property/Unit, Request, Booking, External Accommodation, Stay, Incident, Inventory, Payment, attribution and Butler Assignment each have a responsible parent context and contextual handoff. Details are not global navigation by default. External Accommodation can establish Inventory/Stay truth without a Stayora Booking.

## 18. Booking ↔ Stay Stress Test

Host may group Bookings and Stays structurally, but each retains its own collection/detail and lifecycle. Guest sees Stay; Operations enters Stay/Assignment; Sale follows Request/Booking outcome. Booking and Stay remain separate, including for External Accommodation-originated Stays.

## 19. Property ↔ Unit Stress Test

Property and Unit can share a Property/Unit responsibility context while preserving separate semantic anchors. Unit remains explicit where Inventory, dates and booking intent depend on it. No one-nav-item-per-entity pattern is introduced.

## 20. Request ↔ Booking Stress Test

Requests live in a Host Request collection and Sale activity projection. Request Detail is the decision home. A canonical accepted Request may hand off to Booking Detail, but the objects do not share a lifecycle or status. Confirmed Booking remains separate from Request.

## 21. Incident ↔ Inventory Stress Test

Incidents are operational evidence/exception contexts. Inventory Intervention is a separate authorized action context. Evidence can hand off to an Inventory decision, but Incident never becomes a Maintenance Block automatically.

## 22. Attention Convergence

Pending Request, Inventory conflict, Payment `UNKNOWN`, Incident, External conflict, onboarding pending and Stay exception are embedded in responsibility destinations or contextual exception entries for each relevant surface. No generic Task domain or priority algorithm is created.

## 23. Home / Today Convergence

Guest Stay Hub, Host Current Responsibility, Butler Today, BQL Operations Today and Admin Governance/Attention are justified by current responsibility. Public uses discovery; Sale uses supply and activity/outcome rather than a generic dashboard. No vanity metrics or role dashboards are added.

## 24. Navigation Depth

Conceptual depth is limited to Context → Primary Responsibility → Collection/Detail → Action/Attention. It is not route depth. Field-critical Butler/BQL paths remain shallow; Guest and Sale paths remain mobile-important; Host and Admin retain deeper detail only for consequential work.

## 25. Entry Paths

Users enter via public discovery, responsibility destination, attention, scoped Guest access, contextual handoff/deep link concept, or context/resource selection. No notification system, URL structure or unauthorized redirect is designed.

## 26. B1–B5 Handoff Validation

B1 Sale → Host → Guest/Operations, B2 External Accommodation → Inventory/Stay → Operations/Guest, B3 Public/Guest → Host → Guest/Operations, B4 Host → Butler/BQL/Guest → completion and B5 operational evidence → authorized Inventory action → derived projections remain traversable through the converged structure.

## 27. C1–C4 Handoff Validation

Identity-only, Owner relationship, Host/Property scope, unpublished Property, Sale eligibility/relationship, Butler eligibility/Assignment and multi-capacity Identity all map to legitimate partial or active contexts. No context appears merely to satisfy navigation.

## 28. Empty / Partial Context Findings

NO DATA, NO RELATIONSHIP, NO SCOPE, NO AUTHORITY, PENDING, CONFLICT/EXCEPTION and OUT OF SCOPE remain distinct structural outcomes. No fake default Property, Stay, Request, financial record or unauthorized context is introduced.

## 29. Mobile / Field Findings

Guest/Sale remain mobile-important. Butler/BQL Today → detail → action paths are field-critical and shallow. Host is desktop-important with operational mobile entry; Admin is desktop-important; Public is device-neutral. No responsive design or native app work begins.

## 30. Money Boundary

No Finance, Wallet, Earnings, Payout or Commission destination is added automatically. Money remains contextual in HST-12, SAL-05 and ADM-05. Payment, Entitlement, Settlement and Payout remain distinct; Attribution is not Commission Entitlement.

## 31. Privacy / Need-to-Know

Structural composition does not widen data access. Guest information is Stay-scoped; Owner economics are relationship/authority scoped; Sale commercial information is permitted-scope only; Butler and BQL are operational/destination scoped; Admin is staff-function/exception scoped. QR, contact, retention and field rules remain TBD.

## 32. Converged Product Structure

The full conceptual structure map is in [29-converged-product-structure-map.md](d3-screen-navigation-convergence/29-converged-product-structure-map.md). It shows primary destinations with contextual children and action/attention entries for every surface, without becoming a route tree.

## 33. Screen Disposition Findings

All 42 D2 concepts have explicit dispositions in [30-screen-disposition-matrix.md](d3-screen-navigation-convergence/30-screen-disposition-matrix.md). No concept is silently removed. The matrix records parent responsibility, anchor, reason, preserved distinctions, authority and V0 trace.

## 34. Primary Destination Findings

Primary destinations are minimal and responsibility-driven: Public Discovery; Guest Stay Hub; Host Responsibility, Properties, Requests, Bookings & Stays; Sale Supply and Activity; Butler Today; BQL Operations Today; Admin Governance and Audit. They are justified by repeated or responsibility-critical tasks.

## 35. Navigation Input Findings

The input matrix records context selectors, resource selectors, primary sets, contextual detail model, attention entry, device priority and policy dependencies. It does not define visual navigation.

## 36. Journey × Structure Findings

The journey matrix proves each B1–B5 step has a context, primary destination, detail, action entry, handoff and authority dependency. Critical steps are not hidden by grouping.

## 37. Onboarding × Structure Findings

The onboarding matrix proves each C1–C4 outcome has an available/partial context, destination, unavailable action posture, authority dependency and next legitimate handoff.

## 38. TBD / Policy Boundaries

Owner IA, Guest credential/privacy, attention ordering, payment/confirmation, Sale economics, Admin/BQL grants, Verification/publication and External Accommodation reconciliation remain unresolved. The method is known truth → structural need → policy boundary → open question → detailed interaction not finalizable.

## 39. Remaining Gaps

Remaining gaps are classified as IA, navigation architecture, screen composition, UX interaction, policy, workflow, privacy and authority gaps. The main possible CP8-E blockers are access/privacy, consequential payment/confirmation, Sale economics and field-level action grants; no gap requires D3 to invent policy.

## 40. V0 Scope Check

D3 stays within CP5 MUST BUILD/MANUAL-ASSISTED capabilities and accepted B1–B5/C1–C4. It adds no PMS, Channel Manager, Managed Operations, CRM, workforce, maintenance, dynamic pricing, universal reputation, native app, enterprise IAM or Affiliate Network structure.

## 41. Contradictions Found

No new contradiction was introduced. Preserved: Request ≠ Booking; Booking ≠ Stay; External Accommodation ≠ Stayora Booking; Property ≠ Unit; Inventory Commitment ≠ Availability; Availability ≠ Bookability; Incident ≠ Maintenance Block; Payment ≠ Entitlement ≠ Settlement ≠ Payout; Attribution ≠ Commission Entitlement; Owner ≠ Host; context/resource switching ≠ permission/authority.

## 42. CP8-D Exit Assessment

**CP8-D ACCEPTED AS BASELINE FOR CP8-E1.** This report does not freeze the UX architecture or authorize work beyond E1. Conditions are to preserve Owner as a perspective until an explicit decision, carry policy/privacy/authority gaps into CP8-E boundaries, and keep E1 limited to common behavioral conventions.

## 43. Validation

- All 42 D2 concepts have explicit disposition.
- Seven canonical surfaces remain; no new top-level workspace.
- Primary destinations are responsibility-driven; screen count is not arbitrarily optimized.
- Owner ≠ Host; Request/Booking/Stay, Property/Unit, External Accommodation/Booking, Incident/Maintenance Block, Availability/Bookability and Money/Attribution distinctions remain.
- Context switch ≠ permission; resource switch ≠ authority; screen visibility ≠ authority.
- Guest access remains scoped; Sale remains distribution; Butler remains operational; BQL remains destination operational; Admin remains function/resource scoped.
- B1–B5 and C1–C4 remain traversable.
- Attention does not become a Task domain; no Home/Today is unjustified.
- No policy/TBD was silently closed.
- No detailed interaction, visual navigation, layout, wireframe, component, design system, prototype, API, code, schema or persistence change was created.
- Markdown links are validated after index updates; result is recorded in final handoff.

## Current CP8-E closure overlay

The historical D3 exit language is retained. D3 remains the accepted baseline for E1, and the completed E1–E4 pass closes the CP8-E architecture. Seven canonical surfaces remain; no Owner top-level workspace or E5 is introduced.
