# CP8-E1 — Interaction Model & Behavioral Conventions Report

> Parent: **CP8 — UX / Design System** → **CP8-E Detailed Interaction**
> Status: **ACCEPTED — CP8-E CLOSED**
> Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · Scope: **E1** · 2026-09-21

## 1. Executive Summary

E1 defines Stayora V0's common behavioral grammar before screen-by-screen interaction design. It starts from canonical domain truth, projects it through context and scope, checks authority and preconditions, revalidates consequential truth, records outcomes, refreshes projections, preserves provenance and performs scoped handoffs. It treats stale truth, conflicts, unknown outcomes, manual assistance and partial contexts as first-class behavioral conditions.

**Readiness: ACCEPTED — CP8-E CLOSED.** The common model is accepted across the seven surfaces and B1–B5/C1–C4. FD-01 → FD-19 close the architecture boundaries; residual policy, privacy, economics and field-grant details remain explicit TBDs.

## 2. Sources Reviewed

- [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), CP1–CP7 canonical documentation and roadmap reconciliation.
- CP3 Actor Authority/Core Workflows, CP4 State Machines/Policies, CP5 V0 Scope, CP6 Information Architecture and CP7 Conceptual Data Model.
- Accepted CP8-A, B1–B5, C1–C4, D1, D2 and D3, including D3 TBD/policy/gap registers.

## 3. Files Created / Changed

Created `11-detailed-interaction/e1-interaction-model-behavioral-conventions/` with 50 linked documents covering the interaction grammar, action classes, authority, revalidation, outcomes, stale/conflict/unknown, correction, manual/Admin assistance, handoffs, attention, partial/empty/blocked behavior, boundaries, pattern library, stress tests, constraints, TBDs, blockers and traceability. Created this report. Updated CP8 indexes, D3/D2 status pointers, Start Here, Source of Truth and output pointers so E1 was the then-current execution unit; CP8-E is now closed. No domain, lifecycle, policy, authority, V0, persistence or screen-specific decision was changed.

## 4. Interaction Principles

Canonical truth precedes UI state. Acting capacity, scope and authority are clear before consequential action. Revalidation occurs at the action boundary. Unknown is never silently failed, and manual assistance is represented truthfully. Handoffs preserve object, scope, provenance and authority boundaries.

## 5. Generic Action Model

`CURRENT TRUTH → USER INTENT → ACTING CONTEXT → RESOURCE SCOPE → AUTHORITY CHECK → PRECONDITION CHECK → CURRENT-TRUTH REVALIDATION → ACTION INPUT → ACTION COMMITMENT → OUTCOME → UPDATED PROJECTION → AUDIT/PROVENANCE → HANDOFF/ATTENTION`.

Read-only, low-consequence, consequential, manual-assisted and reconciliation actions use the stages proportionally; this is behavioral architecture, not transaction/API design.

## 6. Action Classes

E1 defines Read/Inspect, Context/Resource Change, Create Intent/Request, Decision, Operational Recording, Authoritative Recording, Consequential Mutation, Correction/Supersession, Exception/Reconciliation and Manual-Assisted Handoff. They are behavioral categories, not commands or domain objects.

## 7. Consequential Action Model

Request decision, Owner Block, Inventory intervention, authoritative External Accommodation, Check-in/Checkout, publication, Butler assignment and relationship correction/revocation require visible truth, acting capacity, scope, authority, relevant preconditions, revalidation and a canonical outcome. Consequence preview and explicit confirmation are justified by material impact, without deciding modal/form behavior.

## 8. Authority Behavior

Interaction distinguishes Can See, Can Initiate, Can Act, Can Act if Authorized, Cannot Act and Authority Unknown/Requires Resolution. Missing, expired, revoked, changed or out-of-scope authority does not become a technical RBAC rule or a hidden permission assumption.

## 9. Acting Capacity

Owner, Host, Sale, Co-host, Butler and other capacities remain attributable. Context switch changes the acting projection, not the authority grant. Ambiguous capacity enters Authority Unknown rather than guessing.

## 10. Revalidation

Inventory, Booking Requests, confirmation conditions, publication, Assignment, authority, Payment conditions/attempts, Check-in/Checkout and Inventory Blocks require conceptual revalidation before consequential commitment. If truth changed, the action does not commit against the stale projection.

## 11. Stale Truth

E1 distinguishes stale-but-safe-to-view, stale requiring action revalidation, stale action no longer valid, conflicted truth and unknown current outcome. No freshness threshold is invented and stale is not automatically unavailable.

## 12. Outcome Model

Interaction outcomes are SUCCESS, REJECTED/NOT PERMITTED, VALIDATION FAILURE, CONFLICT, PROCESSING/PENDING, FAILED, UNKNOWN, PARTIAL/MANUAL FOLLOW-UP REQUIRED and CORRECTED/SUPERSEDED. These are not new domain lifecycle states.

## 13. Success / Failure

Success establishes canonical truth where applicable, refreshes projections, exposes next legitimate action, creates handoff/attention and preserves provenance. Failure distinguishes input, authority, policy/business rejection, conflict, technical failure, unknown and manual intervention; it never collapses to “something went wrong.”

## 14. Unknown Outcome

UNKNOWN means the system cannot safely claim success or failure. Payment Attempt UNKNOWN is the critical case: show known truth, unresolved outcome, attempt/provenance and reconciliation responsibility; avoid unsafe duplicate action; permit only safe recheck/reconciliation. UNKNOWN is never FAILED.

## 15. Conflict

Inventory, External Accommodation, relationship, stale Request and concurrent scope/authority conflicts preserve evidence and history, do not silently choose a winner, and route only authorized responsibility. Conflict resolution policy remains upstream/TBD.

## 16. Pending / Processing

Business pending (Booking Request PENDING), domain/payment processing and transient UI submission are distinct. UI processing cannot be presented as domain completion or failure.

## 17. Optimistic Behavior

Optimistic canonical success is unsafe for Booking confirmation, Inventory, Payment outcome, authoritative Check-in/Checkout and authority/relationship changes. The UI may acknowledge intent submission but must wait for authoritative truth before claiming consequential success.

## 18. Duplicate Intent

Repeated Request, decision, External Accommodation, Incident, Check-in/Checkout or Payment retry after UNKNOWN should expose the existing attempt/outcome, avoid duplicate commitment and route to recheck/reconciliation. No technical idempotency implementation is specified.

## 19. Correction / Supersession / Revocation

Correction preserves original history and establishes effective truth. EDIT, CORRECT, SUPERSEDE, REVOKE, RELEASE, EXPIRE and CANCEL are distinct semantics; generic Edit/Delete is not used. Revocation/relationship changes remain attributable and policy-bound.

## 20. Destructive Action Findings

No universal Delete is created for Booking, Stay, External Accommodation, Inventory Commitment, Incident, authority history or commercial truth. Removal uses canonical release, revocation, expiry, supersession or cancellation semantics where supported.

## 21. Manual-Assisted Interaction

At a boundary, the system records known truth/evidence/request, surfaces responsibility, lets an authorized human assist, records the canonical result and refreshes the originating context. Manual assistance is visible and does not become an automation promise or generic support-ticket domain.

## 22. Admin-Assisted Interaction

Admin assistance records requester, actor, staff function/authority, resource, reason, change, time and provenance. Admin does not impersonate arbitrary authority or bypass policy; the responsible business authority remains attributable.

## 23. Cross-Context Handoff

Sale Request → Host, Host Booking → Guest Stay Access, Host → Butler, Butler Incident → responsible Host/Inventory, External Accommodation → Stay/Operations, BQL issue → responsible context and Admin reconciliation → origin all preserve canonical object, resource scope, provenance, attention and authority. Handoff does not transfer authority automatically.

## 24. Attention Behavior

Attention is a projection and may be new, seen/acknowledged, resolved by domain change, no longer relevant or escalated/manual assist where canonical. No universal attention lifecycle or priority score is invented.

## 25. Partial Context

No relationship, no scope, no authority, pending relationship/eligibility, unassigned, unpublished, no data and out of scope remain behaviorally distinct. A partial context is not a failed context and does not receive fake defaults.

## 26. Empty vs Blocked

EMPTY is a valid scope with no objects; PARTIAL is incomplete setup; BLOCKED is an intended action prevented by authority/policy/precondition; CONFLICT is incompatible truth; UNKNOWN is an unresolved outcome. These states have different recovery and explanation categories.

## 27. Action Availability

Actions may be available, visible-but-unavailable, not shown, conditional, require a different context or require manual assistance. This is a contextual behavior choice; availability is not the permission model and disabled controls are not security.

## 28. Confirmation / Consequence Preview

Confirmation is consequence-based, not universal. It is justified for material financial, Inventory, external, Guest, authority/delegation or hard-to-reverse impact. Preview only canonical consequences; Checkout does not imply Inventory release and Incident escalation does not imply a Block.

## 29. Payment Boundary

Required Payment Condition, Payment Obligation, Payment Attempt and Payment Default remain distinct. Processing/Succeeded/Failed/Unknown may be interaction outcomes; Booking confirmation follows canonical conditions. Deposit, grace, retry, refund, cancellation, default or release timing is not invented.

## 30. Inventory Boundary

Effective commitments/blocks derive Availability, which informs contextual Bookability. UX never sets Availability directly. Inventory actions show basis/authority, revalidate, record a canonical intervention and refresh derived projections; conflicts do not choose winners automatically.

## 31. Request / Booking Boundary

Request decision is not Booking edit. Acceptance is followed by applicable conditions and canonical Booking confirmation only when conditions pass; acceptance does not always mean immediate Booking.

## 32. Stay Boundary

Preparation/Ready is a milestone; Arrival is not Check-in; Check-in is authorized action; Checkout is not Completion; Completion is not Inventory release; Incident is not a Stay state. E1 preserves these semantics without new lifecycle states.

## 33. Incident Boundary

Observation → Incident/evidence → escalation → authorized evaluation → possible downstream action. No automatic blame, refund, Block, reputation or Settlement is implied.

## 34. Onboarding Boundary

Identity, relationship, eligibility, resource association, authority and Working Context remain independent. Invitation is not relationship, claim is not truth and relationship is not authority. No universal ONBOARDED state or wizard is introduced.

## 35. Guest Access Boundary

Guest access remains scoped to the represented Stay. Account is optional where canonical. Credential/QR lifecycle, expiry, sharing, privacy and retention remain TBD and block only dependent branches.

## 36. Sale Economics Boundary

Attribution is not Commission Entitlement, Settlement or Payout. Permitted outcome may be shown, but no commission rate, formula, eligibility rule or timing is invented; SAL-05 remains partial where required.

## 37. Admin / BQL Boundary

Admin/BQL membership does not imply action authority. Function, grant and resource scope are required; unresolved grants remain Authority Unknown/manual assist rather than super-admin behavior.

## 38. Loading / Refresh

Initial truth loading, refresh/revalidation, action processing, stale refresh and unknown reconciliation are conceptually distinct. No skeleton, spinner, polling or transport behavior is defined.

## 39. History / Provenance

Authority-sensitive, corrective, Inventory, External Accommodation, Incident, Admin-assisted, financial/commercial and relationship interactions require provenance in the decision context where permitted: actor/capacity, resource, reason, evidence and time.

## 40. Notification Principle

Notifications point to current canonical projections. They are not truth and may be stale. Consequential action from a notification requires current projection and revalidation.

## 41. Recovery

Validation failure is corrected input; stale truth is refreshed; conflict routes to authorized responsibility; technical failure retries only when safe; unknown reconciles without duplicate mutation; lost authority changes legitimate context only; manual assistance records responsibility.

## 42. Pattern Library Summary

The pattern library covers Read/Inspect, Context/Resource Change, Request Intent, Consequential Decision, Authoritative/Operational Recording, Inventory Intervention, Check-in, Checkout, Incident, Correction, Revocation, Manual Handoff, Conflict, Unknown, Reconciliation, Partial Context, Attention and Cross-Context Handoff. Each pattern records truth, authority, preconditions, revalidation, outcomes, recovery, handoff, provenance and policy dependency.

## 43. B1–B5 Stress Test

B1 works through Request intent, Host decision, Inventory/payment conditions, Booking and Guest handoff. B2 uses authoritative External Accommodation recording, provenance and reconciliation without a Stayora Booking. B3 uses Request/Booking separation and scoped Guest access. B4 preserves readiness, arrival, Check-in, Incident, Checkout and completion boundaries. B5 uses evidence, authority, revalidation and derived Availability/Bookability. Payment, credential, conflict and field grants remain explicit blockers where unresolved.

## 44. C1–C4 Stress Test

Invitation, claim, pending relationship, eligibility, Property representation, authority grant, Sale relationship, Butler Assignment, revocation and multi-capacity Identity all follow independent-outcome conventions. No universal onboarding state or automatic context is introduced.

## 45. Surface Stress Test

Public uses read/intent; Guest uses scoped Stay access; Host uses authority-heavy consequential behavior; Sale uses distribution behavior; Butler uses field operations; BQL uses destination operations; Admin uses governance/manual reconciliation. The grammar is shared, but responsibility and data scope are not identical.

## 46. Mobile / Field Findings

Butler/BQL remain field-critical, Guest/Sale mobile-important, Host/Admin more desktop-consequential and Public device-neutral. Current truth, capacity, scope, consequence and recovery must remain clear across devices; no responsive or native implementation is defined.

## 47. Accessibility / Clarity

Critical state cannot depend on color alone. Consequential meaning, failure, conflict, unknown and unavailable-action reason categories should be explicit where safe. Hover-only discovery is unsuitable for field/mobile behavior. No visual token or component rule is created.

## 48. TBD / Policy Boundaries

Payment/confirmation/default/retry, Inventory conflict resolution, Guest credentials/privacy, Sale economics, Admin/BQL grants, attention semantics, correction/retention and Check-in/Checkout grants remain open. E1 carries them forward rather than resolving them.

## 49. Gap / Blocker Register

Gaps are classified as Policy, Privacy, Authority, Money, Workflow, State-Machine, Interaction and IA. E1 has no CP8-level blocker; local and journey blockers remain for detailed interaction branches. The full register records whether independent work can continue and whether CP8-E detail is blocked.

## 50. V0 Scope Check

All conventions serve accepted V0 capabilities and B1–B5/C1–C4. No PMS, Channel Manager, Managed Operations, CRM, Affiliate Network, workforce/maintenance suite, dynamic pricing, universal reputation, native app, enterprise IAM or generic workflow engine is introduced.

## 51. Contradictions Found

No new contradiction was introduced. Preserved: Identity ≠ Working Context ≠ Authority; Request ≠ Booking; Booking ≠ Stay; External Accommodation ≠ Stayora Booking; External Fact ≠ Inventory Commitment; Inventory Commitment ≠ Availability; Availability ≠ Bookability; Property ≠ Unit; Incident/Finding/Responsibility/Consequence distinctions; Payment Obligation/Attempt/Required Condition/Default distinctions; Payment ≠ Entitlement ≠ Settlement ≠ Payout; Attribution ≠ Commission; Owner ≠ Host; Assignment ≠ Authority; Visibility ≠ Authority.

## 52. Readiness Assessment

**ACCEPTED — CP8-E CLOSED.** E1 is accepted as the common interaction architecture. Residual policy, privacy, authority, payment, Sale economics, conflict and field details remain TBD; CP8-F is next and not started.

## 53. Validation

- Canonical truth precedes UI state.
- Authority is checked at action boundary; acting capacity remains explicit.
- Consequential actions revalidate; stale, conflict, failure and unknown remain distinct.
- Business pending and UI processing remain distinct; UNKNOWN is never FAILED.
- Duplicate intent is handled safely; corrections preserve history/provenance.
- Manual/Admin assistance is attributable; handoff does not transfer authority.
- Empty, partial, blocked, conflict and unknown remain distinct.
- Inventory does not directly set Availability; Request/Booking/Stay and all Money boundaries remain separate.
- Onboarding outcomes, Guest access, Sale attribution and Admin/BQL scope remain bounded.
- Notifications point to current truth.
- B1–B5, C1–C4 and all seven surfaces use the common model.
- No new lifecycle/domain object/permission/policy introduced.
- No screen-by-screen design, visual/design-system/prototype/implementation work started.
- Markdown links are validated after index updates; result is recorded in final handoff.
