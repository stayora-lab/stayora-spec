# CP8-E3 — Stay Operations Interaction Report

> Parent: **CP8 — UX / Design System** → **CP8-E Detailed Interaction**
> Status: **ACCEPTED — CP8-E CLOSED**
> Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · Execution unit: **CP8-E3** · 2026-09-21

## 1. Executive Summary

E3 defines detailed V0 interaction behavior for B4 Stay Operations across Host, Guest Stay Access, Butler and Destination/BQL, with Admin only for canonical exception governance. It preserves the separation between accommodation/commercial basis, Stay truth, operational observations, authority, Incident evidence and Inventory truth.

**Readiness: ACCEPTED — CP8-E CLOSED.** The canonical flow, projections, Check-in/Checkout actions, Incident boundaries, completion and external-based Stay convergence are accepted. FD-01 → FD-07 close the E3 architecture; residual grants, credentials/privacy, Incident, no-show and connectivity details remain explicit TBDs.

## 2. Sources Reviewed

- [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), CP3 Authority/Core Workflows, CP4 State Machines/Policies, CP5 V0 Scope, CP6 IA and CP7 Conceptual Data Model.
- Accepted CP8-A, B1–B5, C1–C4, D1–D3, E1 and E2.
- B4 Stay Operations, B2 External Booking → Stay, B5 Inventory Intervention, C4 Butler Onboarding and E1/E2 TBD/policy/blocker registers.

## 3. Files Created / Changed

Created `e3-stay-operations-interaction/` with 51 linked documents covering Stay basis/relevance, Host/Guest/Butler/BQL behavior, preparation, arrival, Check-in, In-Stay, Incident, Inventory/commercial boundaries, Checkout, completion, DID_NOT_OCCUR, external convergence, contracts, sequences, matrices, field/connectivity/accessibility boundaries, TBDs, blockers and traceability. Created this report. Updated E2/E1 status pointers, CP8-E index, Start Here, Source of Truth and output pointers so E3 was reviewed and accepted as the baseline for E4. No upstream domain, lifecycle, policy, authority, V0, persistence or visual decision was changed.

## 4. Canonical Stay Interaction

`Accommodation Basis → SCHEDULED → preparation/Ready milestone → arrival observation → authorized Check-in → CHECKED_IN → operational support/Incident → authorized Checkout → CHECKED_OUT → completion evaluation → COMPLETED where canonical`, with separate `SCHEDULED → DID_NOT_OCCUR`. Preparation/Ready and observations are not invented lifecycle states.

## 5. Accommodation Basis

Stay may derive from Stayora Booking or External Accommodation. Basis is provenance/legitimacy context, not Stay itself. External-based Stay does not fabricate Stayora Booking, Payment, Sale attribution, commission, Settlement or Payout.

## 6. Stay Operational Relevance

Booking confirmed, Stay exists/SCHEDULED and operational responsibility becoming relevant are distinct. E3 does not invent automatic Stay creation timing; unresolved timing remains a workflow boundary.

## 7. Upcoming Stay Projection

Guest, Host, assigned Butler, BQL and Admin receive different scoped projections of Property/Unit, dates, basis, Guest data, arrival information, readiness and exceptions. Need-to-know remains explicit.

## 8. Host Stay Interaction

Host coordinates upcoming Stays, preparation, Butler, arrival/Check-in truth, issues, Checkout, completion evaluation and exceptions only where authorized. Host visibility does not grant unrestricted operational authority or workforce controls.

## 9. Guest Stay Hub

Guest sees scoped Stay truth before arrival, arrival/access context, operational help while checked in and post-checkout/completion projection where relevant. Account remains optional; Guest Hub is not Booking administration.

## 10. Butler Today / Assignment

Butler Today projects valid Assignment-scoped responsibility: select Stay, report preparation, support arrival, perform Check-in/Checkout only with explicit grants, record Incident and receive completion handoff. Assignment is not authority.

## 11. BQL Operations Today

BQL sees destination/function-scoped arrivals, departures, active Stays, Incidents, exceptions and canonical services/access. BQL is not Host, Booking manager, Inventory controller or Butler manager.

## 12. Preparation / Readiness

Preparation and Ready are operational milestones/projections. Reports require canonical observer/evidence posture; incomplete preparation creates attention, not a Stay state, Check-in authority or Inventory mutation.

## 13. Arrival Observation

Expected/observed arrival and Guest presence/access are observations. Arrival is not an ARRIVED state or Check-in and cannot mutate Inventory.

## 14. Check-in Authority

Check-in uses current Stay truth → acting capacity → Assignment/resource scope → explicit grant → preconditions → revalidation → action → canonical outcome/provenance. Assignment, BQL visibility or Host relationship alone do not grant authority.

## 15. Check-in Preconditions

Only canonical needs are considered: actionable Stay, correct resource/date, valid basis, relevant Guest/staying-party basis, authority and readiness where canonical. ID, deposit, documents, arrival windows and fees are not invented.

## 16. Check-in Revalidation

Revalidate Stay state, scope, authority, basis and relevant exceptions/conflicts. Stale actions do not commit. Outcomes distinguish not permitted, wrong resource, already checked in, no longer actionable, conflict, manual and technical failure.

## 17. Check-in Outcome

Successful Check-in updates only canonical Stay truth, scoped projections and provenance; it does not mutate Booking, Inventory, Payment settlement or Completion.

## 18. Duplicate / Concurrent Check-in

Repeated/second actions revalidate and show existing truth; they do not create duplicate authoritative Check-in. Unknown outcomes route to safe reconciliation; actor histories remain attributable.

## 19. Guest Credential Boundary

Credential/QR is scoped access, not authority. Generation, expiry, sharing, revocation, offline behavior, contact exposure and retention remain open and block only dependent branches.

## 20. In-Stay Operation

During CHECKED_IN, Guest help/access, Butler support, Host awareness, BQL service and Incident reporting are supported. No IN_STAY lifecycle state, service marketplace, messaging platform or workforce suite is created.

## 21. Operational Contact

Guest reaches legitimate scoped operational responsibility. Contact visibility is not unrestricted personal data visibility; channel/privacy/consent rules remain TBD.

## 22. Incident Entry

`observation → Incident/evidence → canonical Incident truth → responsible attention → escalation → authorized evaluation`. Reporter and decision authority can differ; no consequence follows automatically.

## 23. Incident Information Contract

Stay/resource, observation/time and reporter/provenance are canonical categories where recorded. Evidence, affected context, category/severity and retention remain optional/contextual or policy-bound. Commercial consequence is not required by Incident alone.

## 24. Incident Projections

Guest sees relevant impact/help; Butler sees assigned evidence; Host sees authorized responsibility; BQL sees destination issue; Admin sees governed exception/provenance. Blame, economics and sensitive evidence remain need-to-know.

## 25. Incident → Inventory Boundary

`Incident/evidence → escalation → authorized Inventory evaluation → possible intervention → derived Availability → contextual Bookability`. No automatic unavailable, Block or Availability mutation is created; E3 hands off to B5.

## 26. Incident → Commercial Boundary

Incident does not automatically create refund, compensation, Owner charge, blame, reputation, Settlement or Payout changes.

## 27. Incident Correction

Correction preserves original evidence/history where canonical, records actor/time/reason and establishes effective corrected truth. No retention policy is invented.

## 28. Checkout Authority

Checkout is consequential and requires explicit authority. Butler Assignment, BQL visibility, Guest departure or Host relationship alone do not grant it.

## 29. Checkout Preconditions

Canonical needs are Stay CHECKED_IN, correct resource, valid authority, departure context and relevant exception. Damage, payment, deposit, housekeeping, key return and late fee rules are not invented.

## 30. Departure Observation

Observed departure may precede or occur without Checkout. It is awareness/attention, not DEPARTED state, Checkout, Completion or Inventory release.

## 31. Checkout Revalidation

Revalidate Stay, authority, resource and exceptions. Stale/concurrent Checkout cannot overwrite truth; current outcome and safe recovery are shown.

## 32. Checkout Outcome

Successful Checkout records canonical Stay transition, actor/capacity/time/provenance and hands off to completion evaluation. It does not complete Stay, release Inventory, mark Unit available, settle money, close Incident or create Review Right.

## 33. Completion Evaluation

Checkout ≠ Completion. Only canonical completion conditions/authority may establish COMPLETED; unresolved evaluation remains pending/manual attention.

## 34. Completed

Where canonical conditions pass, Stay COMPLETED is projected. It does not imply Availability, Inventory release, Settlement, Payout or Review Right without separate canonical rules.

## 35. Did Not Occur

SCHEDULED → DID_NOT_OCCUR is used only where canonical. No no-show timing, declaring authority, penalty, financial consequence or release behavior is invented.

## 36. Stay Exceptions

Missing authority, wrong resource, access issue, blocked Check-in/Checkout/completion, Incident escalation and External conflict are projections of underlying truth, not a generic Exception domain.

## 37. External Accommodation Stay

External Accommodation supports the same legitimate operations without fake Booking, Payment, commission, Settlement or Payout. Operational semantics converge with Booking-based Stay.

## 38. Booking vs External Convergence

Commercial provenance and Booking detail may differ; Stay truth, Guest operational access, Butler/BQL operations, Incident, Check-in/Checkout and completion semantics converge where legitimate. There are not two Stay domain variants.

## 39. Screen Interaction Contracts

Contracts cover GST Stay Hub/Access/Help, Host Stay/Butler coordination, Butler Today/Stay/Check-in/Incident/Checkout, BQL Today/Stay/Incident and Admin exception context. Each includes purpose, entry, truth, action categories, authority/revalidation, outcomes, attention, handoff and blocked conditions without layout/components.

## 40. Interaction Sequence Findings

The required sequences from upcoming relevance through Check-in, Incident, Checkout, completion, DID_NOT_OCCUR, External Stay and manual exception are specified behaviorally and stop at unresolved policy.

## 41. Stay Projection Matrix

Guest, Host, Butler, BQL and Admin projections distinguish SCHEDULED, preparation, Ready, arrival observation, CHECKED_IN, Incident, departure observation, CHECKED_OUT, completion pending, COMPLETED, DID_NOT_OCCUR and manual exception. Milestones/observations are not lifecycle states.

## 42. Authority × Action Findings

Preparation/readiness, arrival observation, Check-in, Incident, escalation, Checkout, completion, DID_NOT_OCCUR and reconciliation each require explicit context/capacity, authority, scope and revalidation. No grant is inferred.

## 43. Information Visibility Findings

Need-to-know categories constrain Guest identity/contact, Property/Unit, basis, provenance, readiness, Check-in/out, Incident evidence, commercial/payment truth, Owner economics and authority history. Exact field-level privacy remains open.

## 44. Attention Findings

Preparation, readiness issues, arrival, blocked Check-in, Incidents, Checkout/completion blockers, access problems and manual assistance project into responsible contexts. Attention is not a Task domain or priority algorithm.

## 45. Error / Recovery Findings

Validation, authority, Assignment, resource, stale, already checked-in/out, conflict, technical, unknown, credential/access and manual conditions have distinct safe recovery. Duplicate authoritative actions are not encouraged.

## 46. Consequence Preview

Check-in exposes Stay operational consequence, Incident escalation exposes evaluation responsibility, Correction exposes effective truth, Checkout exposes CHECKED_OUT/evaluation handoff and Admin action exposes attributable result. None implies Inventory release, Completion or commercial consequence automatically.

## 47. Mobile / Field

Butler/BQL are Field-Critical; Guest Mobile-Important; Host mixed; current Stay/resource, Assignment, authority, evidence and recovery remain clear with shallow operational paths.

## 48. Connectivity Boundary

No offline architecture or sync is invented. Check-in/Checkout cannot show canonical success without authoritative confirmation; future offline/retry behavior remains a technical/interaction boundary.

## 49. Accessibility / Clarity

SCHEDULED, CHECKED_IN, CHECKED_OUT and COMPLETED remain distinct; Ready, arrival, departure and Incident do not mimic lifecycle/Inventory status. Blocked/no-authority/unknown/conflict are distinguishable without color or hover-only behavior.

## 50. TBD / Policy Boundaries

Stay creation timing, preparation/arrival authority, Check-in/Checkout grants and preconditions, credential/privacy, Incident taxonomy/consequence, completion/no-show, Admin/BQL grants, connectivity and correction/retention remain unresolved.

## 51. Gap / Blocker Register

Gaps are classified workflow, authority, privacy, policy, domain/workflow, technical/interaction and state-machine. No D-level CP8 blocker is introduced; local/journey blockers remain.

## 52. Cross-Family Blocker Review

Credential/privacy affects E1/E2/E3; authority grants affect E1/E2/E3 and C4; Inventory conflict affects E2/E3/B5; attention semantics recur across E1–E3; connectivity is local/journey-specific. Recurrence is recorded, not silently resolved.

## 53. V0 Scope Check

E3 supports Destination Stay Coverage, Inventory Trust, Network Adoption and operational Commerce Validation within MUST BUILD/MANUAL-ASSISTED scope. No housekeeping workforce, maintenance suite, service marketplace, PMS, Channel Manager, Managed Operations, CRM, messaging platform, dynamic pricing, native app or generic Task engine is introduced.

## 54. Contradictions Found

No new contradiction was introduced. Booking ≠ Stay; External Accommodation can support Stay; Accommodation Basis ≠ Stay; Preparation/Ready ≠ lifecycle; Arrival ≠ Check-in; Assignment ≠ authority; Incident ≠ Stay/Block/commercial consequence; Departure ≠ Checkout; Checkout ≠ Completion; Completion ≠ Inventory release/Availability; DID_NOT_OCCUR policy remains open.

## 55. Readiness Assessment

**ACCEPTED — CP8-E CLOSED.** E3 architecture is closed by FD-01 → FD-07 and FD-15/16 where applicable; residual policy/privacy/connectivity details remain explicit TBDs. CP8-F is next and remains not started.

## 56. Validation

- Booking, External Accommodation, Accommodation Basis and Stay remain separate.
- Preparation/Ready/arrival/departure are milestones/observations, not invented states.
- Check-in/Checkout require actual authority and current-truth revalidation.
- Assignment, BQL visibility and Host relationship do not imply action authority.
- Duplicate/concurrent authoritative actions are safe; credential is not authority.
- Incident remains evidence/exception; no automatic Inventory or commercial consequence.
- Checkout ≠ Completion; Completion ≠ Inventory release/Availability/Settlement.
- DID_NOT_OCCUR/no-show policy is not invented.
- Booking-based and External-based Stays converge operationally where legitimate.
- Guest/Host/Butler/BQL/Admin use one Stay truth with need-to-know projections.
- Attention remains a projection; field behavior remains viable.
- Cross-family blockers are identified.
- No visual/prototype/implementation work started.
- Markdown links are validated after index updates; result is recorded in final handoff.
