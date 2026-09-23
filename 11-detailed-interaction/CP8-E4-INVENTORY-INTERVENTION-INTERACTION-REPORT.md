# CP8-E4 — Inventory Intervention Interaction Report

> Parent: **CP8 — UX / Design System** → **CP8-E Detailed Interaction**
> Status: **ACCEPTED — CP8-E CLOSED**
> Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · Execution unit: **CP8-E4** · 2026-09-21

## 1. Executive Summary

E4 defines the V0 interaction family for B5 Inventory Intervention. It is accepted as the final E4 architecture baseline. It preserves canonical Inventory truth as the source, uses Unit × Time scope, requires effective authority and revalidation, keeps facts/evidence separate from decisions and commitments, derives Availability, keeps Bookability contextual, preserves conflicts/provenance and routes unresolved consequences to attention or reconciliation. **Readiness: ACCEPTED.** Founder decisions FD-01 → FD-19 close the architecture while preserving explicit policy/configuration TBDs. No prototype or implementation work was started.

## 2. Sources Reviewed

CP8-E1 accepted behavioral conventions; CP8-E2 accepted Request→Booking; CP8-E3 accepted Stay Operations; CP8-B5 Inventory Intervention; CP3 Actor Authority/Core Workflows; CP4 State Machines/Policies; CP5 V0 Scope; CP6 Information Architecture; CP7 Conceptual Data Model; CP8-A, B1–B4, C1–C4, D1–D3; current Start Here, Source of Truth and policy/TBD registers. E4 uses no legacy Stayora 2.0 or Grok content as source of truth.

## 3. Files Created / Changed

Created `11-detailed-interaction/e4-inventory-intervention-interaction/` with 55 linked documents plus its README, and this report. Added the Founder-approved Emergency Protective Hold boundary, reconciled FD-01 → FD-19 and updated CP8-E/source-of-truth pointers to close E4. No upstream domain, lifecycle, authority, policy, V0, persistence or visual decision was invented.

## 4. Canonical Inventory Interaction

The contract is `current truth → intent/evidence → acting context → Unit × Time → authority → basis → preconditions → revalidation → intervention → canonical outcome → derived projection → provenance → handoff/attention`. Inventory UX is an intervention/projection surface, not editable Availability truth.

## 5. Inventory Truth for UX

Fact/evidence, block, commitment, conflict, freshness, provenance and effective result remain distinguishable. Owner Block, Maintenance Block, Emergency Protective Hold, Temporary Exclusive Commitment, Confirmed Accommodation Commitment and External-backed Commitment are not collapsed into generic availability labels.

## 6. Unit × Time Scope

Every consequential path names Unit/resource and effective time range. Property ≠ Unit. Property-wide semantics, inheritance and fan-out remain undefined unless upstream policy later supplies them.

## 7. Inventory Projection

Projection refreshes from canonical truth and reports basis, freshness, conflicts and next legitimate action. Projection does not mutate Inventory or create a second source of truth.

## 8. Calendar Boundary

Calendar cells are visual Unit × Time projections. Click/drag/color/bulk selection does not confer authority or write Availability. No calendar UI, daily rows or algorithm is designed.

## 9. Actor Entry Paths

Host Inventory, authorized Owner perspective, Request/Booking, External Accommodation, Incident/evidence and scoped Admin governance are entry points. Butler/BQL enter through evidence/handoff. All paths converge on one contract.

## 10. Owner Interaction

Owner and Host may be the same identity, but Owner status alone is not unrestricted Inventory Authority. Owner without a grant, explicit Inventory authority and overlapping Owner Block are separately represented.

## 11. Host Interaction

Host action depends on effective capacity, relationship, resource and time scope. Host relationship/listing responsibility does not grant every Inventory mutation.

## 12. Butler / BQL Evidence Handoff

`observation → evidence/report → responsible attention → authorized evaluation`. Assignment and destination visibility are not Inventory Authority; reporting does not create a Block.

## 13. Admin Interaction

Admin sees scoped governance/reconciliation context and can record an authorized manual outcome where the responsible business authority is explicit. Admin is not universal CRUD or super-admin override.

## 14. Owner Block

Owner Block requires legitimate initiator, authority, Unit × Time, basis/reason/evidence, revalidation, conflict detection, canonical outcome, projection and provenance. Duration, priority, override and commercial effects remain policy TBD.

## 15. Maintenance Block

Maintenance Block is a separate authorized decision. Incident/evidence can hand off for evaluation but is not a Maintenance Block automatically. Emergency Protective Hold is a distinct Founder-approved protective intervention that prevents new conflicting commitments, escalates immediately and does not prove uninhabitability or override existing commitments. No repair suite, vendor, SLA or duration is invented.

## 16. Temporary Exclusive Commitment

Request is not a reservation. Authorized acceptance may establish a Temporary Exclusive Commitment where upstream policy permits; duration, hold release, extension, payment deadline and precedence remain TBD.

## 17. Confirmed Accommodation Commitment

Booking/confirmed accommodation basis may establish a scoped commitment. It remains separate from Booking, Stay, Payment, Availability and settlement.

## 18. External-Backed Commitment

External Commerce is created outside Stayora. Stayora may reference/minimally record External Booking for Inventory Truth and/or Stay; a Stayora Booking is not required. External Fact is not Commitment, and report is not authoritative fact.

## 19. Intervention Action Model

Action categories are inspect, report evidence, request intervention, perform intervention, correct and release. Emergency Protective Hold is an intervention outcome with its own scoped capability, revalidation, escalation and policy-defined review/expiry boundary. Generic Edit/Delete and silent overwrite are excluded.

## 20. Authority

CAN SEE, CAN REPORT EVIDENCE, CAN INITIATE REQUEST, CAN PERFORM, CAN CORRECT, CAN RELEASE and AUTHORITY UNKNOWN are separate. Effective grants are evaluated at action time.

## 21. Revalidation

Authority, scope, commitments/blocks, accommodation facts, basis/evidence and conflict posture are revalidated before consequential action. Stale actions become blocked/conflict/unknown/manual, not success.

## 22. Conflict Detection

Overlap and incompatible truth among Owner/Maintenance Blocks, Emergency Protective Holds, temporary/confirmed/external commitments, corrections and concurrent actions is detected by scoped Unit × Time comparison. Detection preserves all sources.

## 23. Conflict Representation

Conflict view includes resource/time, competing truth/evidence, actor/capacity, provenance, freshness, downstream impact and responsible context. Public/Sale receive privacy-safe derived outcomes only.

## 24. Conflict Resolution Boundary

E4 defines detection, representation, responsibility and reconciliation entry. It does not define precedence or a conflict winner, cancellation, compensation, refund or force override.

## 25. Availability Derivation

Availability is derived from effective Inventory truth; it is not an editable boolean or commitment. Conflicted/stale/incomplete truth remains visibly non-certain.

## 26. Bookability

Bookability is contextual by Availability, actor/source, distribution, policy and commercial context. Searchability is distinct. Block removal does not guarantee universal Bookability.

## 27. Release / Removal

No generic Delete. Release, expiry, correction, supersession and revocation retain their distinct canonical meanings. Release is scoped and authorized and does not imply checkout, completion or Bookability.

## 28. Correction / Expiry

Correction preserves original evidence/truth, actor/capacity, reason/time, effective result and history. Expiry exists only where upstream lifecycle/policy defines it; UI timers do not create truth.

## 29. Checkout / Completion Boundary

Departure, Checkout and Completion do not release Inventory. Inventory release/Availability requires a separate canonical Inventory rule.

## 30. Incident Handoff

Incident handoff carries source context, resource/time, evidence, reporter, responsible Inventory context, authority posture and attention. Reporter authority and intervention authority remain distinct.

## 31. Request / Booking Handoff

E4 consumes E2 Request, acceptance, Temporary Commitment and Booking truth. Request does not reserve Inventory; confirmation uses current Inventory truth and conflict feedback.

## 32. External Accommodation Handoff

External Commerce flows to Inventory Truth and/or Stay without mandatory Stayora Booking. External evaluation and reconciliation remain distinct from operational Stay creation.

## 33. Public Projection

Public/Guest surfaces receive permitted derived Availability, contextual Bookability and trust signals, never private block reasons, Owner intent, Guest identity, Incident evidence or internal conflict.

## 34. Sale Projection

Sale sees permitted supply and outcomes for assisted conversion. Sale does not receive Inventory mutation authority or private Owner/Incident detail; economics remain upstream policy.

## 35. Host / Owner Projection

Host/Owner see richer scoped commitments, blocks, evidence, conflicts, attention and provenance where relationship/authority permits. Rich visibility does not grant action authority.

## 36. Operations Projection

Butler/BQL see operational impact, evidence and responsible attention within assignment/destination scope, not full Inventory controls or private commercial truth.

## 37. Admin Projection

Admin sees scoped conflict/reconciliation/provenance required for governance. This is not a global control plane.

## 38. Attention

Attention represents conflict, evidence awaiting evaluation, required authority, stale commitment, external inconsistency, manual reconciliation or affected accommodation. It is not a Task domain or priority algorithm.

## 39. Manual-Assisted Inventory

Known truth/evidence can be surfaced to an authorized human, who evaluates/intervenes/reconciles, after which canonical projections and originating attention refresh. Manual assistance remains attributable and bounded.

## 40. Duplicate / Concurrent Intervention

Second actions revalidate current truth and cannot duplicate or silently overwrite canonical intervention. Unknown acknowledgement routes to reconciliation; technical locking/idempotency is not selected.

## 41. Partial / Unknown Truth

Known available, known blocked/committed, conflicted, stale, incomplete external reconciliation and unknown authoritative outcome are distinct postures. No fabricated certainty or default availability is shown.

## 42. Screen Interaction Contracts

Contracts are defined for Host Inventory, Inventory projection/context, intervention entry, Owner/Maintenance Block, Request/Booking, External Accommodation, Incident→Inventory, Admin conflict, Public Availability/Bookability and Sale supply. Each includes truth, intent, authority, scope, revalidation, outcome, attention and handoff.

## 43. Interaction Sequence Findings

The A–Q sequence family is covered from Host inspect through public/Sale refresh, including Owner conflict, evidence, Maintenance/Temporary/Confirmed/External commitments, correction, release, stale/concurrent and reconciliation. Policy-dependent branches stop explicitly.

## 44. Inventory Truth × Projection Matrix

The matrix distinguishes no blocking, Owner/Maintenance Block, Temporary/Confirmed, External-backed, conflict/stale/unknown across Public/Guest, Sale, Host/Owner, Butler/BQL and Admin. It is a visibility guide, not a precedence algorithm.

## 45. Authority × Action Findings

Inspect/report/request/perform/correct/release are separate action categories. Explicit grants are required for consequential actions; no actor receives a new grant from E4.

## 46. Conflict Matrix Findings

Block/Hold vs confirmed, external vs confirmed, temporary vs confirmed, overlapping blocks and correction vs commitment are detected and preserved. Resolution remains TBD.

## 47. Information Visibility Findings

Private reasons, Owner intent, Guest data, Incident evidence, commercial conflict and authority history are role/relationship/resource scoped. Public/Sale projections are deliberately narrower.

## 48. Error / Recovery Findings

Missing basis/scope, no authority, stale truth, conflict, unknown outcome, technical failure and incomplete external data have distinct blocked/retry/reconcile paths. No silent mutation or business consequence is inferred.

## 49. Consequence Preview

Preview names Unit × Time, affected truth, authority, basis, conflicts, downstream accommodation impact and projected result. It is informational and does not reserve, release, cancel, refund or establish Bookability.

## 50. Mobile / Field

Butler/BQL evidence and Host/Owner urgent intervention are field-critical. The contract keeps scope, authority, evidence, revalidation and recovery available in constrained contexts. Native/offline design is not created.

## 51. Accessibility / Clarity

Conflict, blocked, stale, incomplete, unknown, committed and derived availability must be distinguishable without color, hover or calendar position alone. Final components/microcopy are out of scope.

## 52. TBD / Policy Boundaries

Architecture is closed for authority categories, Owner/Maintenance/Hold authority, Temporary lifecycle/release, External recording authority and the absence of universal conflict precedence. Concrete grants, block/Hold duration, Temporary duration/extension, evidence standards, Property-wide semantics, release/expiry timing, correction/retention, public conflict treatment and checkout/completion commercial effects remain explicit policy/configuration TBDs.

## 53. Cross-Family Blocker Convergence

E1–E4 blockers were reconciled against FD-01 → FD-19. The architecture blockers listed in the Founder brief are CLOSED. Remaining items are policy/configuration/operating detail: credentials/security, payment amounts/deadlines/retry/refund, Sale economics, attention mechanics, Request expiry/amendment, external evidence standards, specific Admin/BQL grants, correction/retention and connectivity. The historical table remains for provenance; current closure status is in [CP8-E Founder Decision Reconciliation](CP8-E-FOUNDER-DECISION-RECONCILIATION.md). No D-level CP8 blocker remains.

## 54. Prototype Readiness Gate

All listed paths are ready for later prototype work with explicit TBD placeholders: Direct Guest Request→Booking; Sale-assisted Request→Booking; External Accommodation→Inventory/Stay; Confirmed Booking→Guest Stay Access; Stay preparation→Check-in; In-Stay Incident handling; Checkout→completion; DID_NOT_OCCUR; Owner Block; Maintenance Block; Emergency Protective Hold; and Inventory Conflict/reconciliation entry. Ready means UX architecture is closed, not implementation-ready. No prototype starts in this task.

## 55. Founder Decision Queue

FD-01 → FD-19 is complete. The former Founder Decision Queue is closed as a review activity; remaining open items are deliberately preserved policy/configuration/TBD boundaries listed in the reconciliation register. No new business-policy answer is chosen.

## 56. CP8-E Coverage Review

B1 and B3 are covered by E2; B2 is sufficiently covered for CP8-E exit by B2 + E3 + E4 + FD-08/09 + FD-12 + FD-15/16; B4 is E3; B5 is E4. C1–C4 onboarding plus E1 generic interaction grammar provide sufficient V0 interaction architecture for CP8-E exit. No remaining D2/D3 V0 screen/task family requires a new consequential interaction family. E5 is not created.

## 57. V0 Scope Check

E4 supports Destination Stay Coverage, Inventory Trust, Network Adoption and Commerce Validation within MUST BUILD/MANUAL-ASSISTED. It does not add editable calendar truth, PMS, Channel Manager, maintenance/workforce suite, CRM, Affiliate Network, dynamic pricing, native app, generic workflow engine or advanced conflict automation.

## 58. Contradictions Found

No new contradiction is introduced. The package explicitly preserves: Inventory Fact/Evidence ≠ Inventory Decision; External Accommodation Fact ≠ Inventory Commitment; a Stayora Booking is not required for External Booking; Fact/Evidence ≠ Decision; External Fact ≠ Commitment; Request ≠ Commitment; Commitment ≠ Availability; Availability ≠ Bookability; Incident ≠ Maintenance Block; Owner/Host/Assignment/visibility ≠ unrestricted Authority; Checkout/Completion ≠ release; release ≠ universal Bookability; calendar ≠ canonical truth.

## 59. Readiness Assessment

**ACCEPTED — CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE.** FD-01 → FD-19 close the architecture. Remaining policy/configuration/legal/privacy TBDs are preserved and do not reopen E4. CP8-F is next and remains not started.

## 60. Validation

Verified that canonical truth starts each intervention; Unit × Time is explicit; calendar is projection only; Owner/Host/assignment/BQL/Admin visibility do not imply unrestricted authority; evidence/report/Incident/External Fact/Request remain distinct from intervention/commitment; Availability is derived; Bookability is contextual; conflicts preserve sources without a winner; release/correction preserve provenance; Public/Sale are privacy-safe; duplicate/concurrent actions are safe; cross-family blockers and prototype readiness are assessed; no visual, prototype, API, schema or code work began. Markdown links are validated after index updates.

