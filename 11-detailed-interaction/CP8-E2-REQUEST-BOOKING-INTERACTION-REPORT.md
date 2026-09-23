# CP8-E2 — Request → Booking Interaction Report

> Parent: **CP8 — UX / Design System** → **CP8-E Detailed Interaction**
> Status: **ACCEPTED — CP8-E CLOSED**
> Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · Scope: **E2** · 2026-09-21

## 1. Executive Summary

E2 defines the common V0 interaction family from accommodation intent through Booking confirmation for B1 Sale-assisted Booking and B3 Direct Guest Booking. Both paths converge on one canonical Request model, one Host authority model, one Inventory truth and one Booking truth. E2 stops at unresolved payment, Inventory conflict, Request expiry/withdrawal, Guest credential, Sale economics and authority-policy boundaries.

**Readiness: ACCEPTED — CP8-E CLOSED.** All primary paths and outcomes are structurally specified. FD-08/09, FD-10/11, FD-12 and FD-17/18/19 close the E2 architecture; unresolved commercial/payment, expiry, credential, economics and grant details remain explicit TBDs. No visual screen design, component, API, code or persistence change was created.

## 2. Sources Reviewed

- [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), CP3 Actor Authority/Core Workflows, CP4 State Machines/Policies, CP5 V0 Scope, CP6 IA and CP7 Conceptual Data Model.
- Accepted CP8-A, B1, B3, B2/B4/B5 boundary material, C1–C4, D1–D3 and E1 Interaction Model.
- Relevant TBD/policy/blocker registers, especially payment, Inventory, Guest access, Sale economics and authority boundaries.

## 3. Files Created / Changed

Created `e2-request-booking-interaction/` with 46 linked documents covering the canonical flow, both entry branches, Availability/Bookability, Request contract/submission/pending/attention/detail, decision authority, accept/reject, revalidation, Inventory, Payment, confirmation, projections/handoffs, correction/expiry/duplicates/concurrency, screen contracts, sequences, matrices, consequence preview, device/accessibility, TBDs, blockers and traceability. Created this report. Updated E1/D3 status pointers, CP8-E index, Start Here, Source of Truth and output pointers so E2 was the then-current execution unit; CP8-E is now closed. No upstream domain, lifecycle, policy, authority, V0, persistence or visual decision was changed.

## 4. Canonical Request → Booking Interaction

`Discovery/intent → canonical Request → Request PENDING → Host decision → revalidation → ACCEPTED/REJECTED → applicable Inventory/payment/confirmation conditions → Booking CONFIRMED only when canonical conditions pass → scoped Guest/Host/Sale/Operations projections`.

Guest intent, Offer, Request, Booking and Stay remain distinct. Request does not reserve Inventory, and acceptance is not automatically Booking.

## 5. Sale-Assisted Entry

Sale discovers relationship-scoped supply, derived Availability and contextual Bookability, prepares permitted option information, captures Guest intent and creates a Request. Sale attribution is independent from Booking Authority and Commission Entitlement. Sale cannot accept, mutate Inventory or gain operational authority.

## 6. Direct Guest Entry

Public discovery exposes Destination, Property/Unit, Public Price, trust, derived Availability and contextual Bookability. Guest selects date/intent and creates a Request through the same canonical path. Account remains optional where canonical; Direct Guest does not become Instant Book and no checkout is invented.

## 7. Availability / Bookability

Discovery shows derived Availability. Bookability depends on actor/source/context and current conditions. Searchability, Availability and Bookability remain separate. No stored AVAILABLE state or freshness threshold is created. Revalidation occurs at submission and decision where truth can change.

## 8. Request Information Contract

Property/Unit, date range, canonical staying-party/Guest information, Request Creator, acting capacity and applicable source/attribution are categorized as canonical where required. Contact, notes, price/terms snapshots and payer details remain optional/contextual or policy-bound unless canonical. Request Creator, Lead Guest, Staying Party and Payer do not collapse.

## 9. Request Creation / Submission

`input validation → acting context → scope → preconditions → revalidation → submission → authoritative Request existence → Request PENDING`. UI submitting is not Request PENDING. If canonical creation is uncertain, no duplicate Request is encouraged.

## 10. Request Pending

PENDING is domain/business truth after a Request exists. Guest, Sale and Host receive different scoped projections; Host receives actionable attention. Expiry/timeout/withdrawal behavior remains unresolved.

## 11. Host Attention

Host attention identifies decision need, Property/Unit/date, permitted source/creator, Inventory truth, authorized commercial context, Request state, authority posture and known consequence. It is a projection, not a Task object or priority algorithm.

## 12. Request Detail

Host Request Detail is the decision home. It exposes primary Request truth, supporting accommodation, Guest/Creator context, Inventory, commercial context, authority/provenance and exceptions semantically. It does not become Booking or Inventory reservation.

## 13. Decision Authority

Host/Primary Host/delegated Co-host with valid Booking Authority may decide within scope. Sale, Guest, Butler and BQL capacities cannot accept/reject. Dual-capacity actions use the actual accepting Host/Co-host capacity; Sale attribution remains independent. Unknown/revoked/out-of-scope authority blocks action.

## 14. Accept / Reject Interaction

Decision behavior is acting capacity → authority → Request state → scope → Inventory/conditions → revalidation → commitment → outcome. Control placement and confirmation UI are not specified.

## 15. Decision Revalidation

Revalidate Request actionability, authority, Property/Unit/date, effective Inventory commitments/blocks and applicable conditions. Stale truth cannot be overwritten. Outcomes include stale, conflict, no authority, no longer actionable and manual assistance.

## 16. Reject Branch

Reject preserves Request history and updates Host/Sale/Guest projections. It does not mutate Inventory without canonical basis, does not create Booking and does not invent rejection reasons where policy is absent.

## 17. Accept Branch

Accept establishes Request ACCEPTED and moves to applicable Inventory/payment/confirmation conditions. Request ACCEPTED remains distinct from Booking CONFIRMED. No automatic condition or immediate Booking is invented.

## 18. Inventory Commitment Boundary

A Temporary Exclusive Commitment may be enabled by canonical acceptance flow where policy supports it. E2 does not define duration, release, priority, extension, cancellation or conflict winner. Availability remains derived; Bookability contextual.

## 19. Inventory Conflict

Decision-time conflict preserves Request, facts, commitments and evidence, surfaces responsibility and avoids fabricated Availability or silent overwrite. Remediation/winner policy remains open.

## 20. Payment Condition Boundary

Required Payment Condition, Payment Obligation, Payment Attempt and Payment Default remain distinct. E2 can present a condition and stop at unresolved economics. No deposit, amount formula, deadline, grace, retry, refund, cancellation, default or release timing is introduced.

## 21. Payment Attempt

Where canonical, the interaction presents condition and payer context where known, records attempt, shows PROCESSING and then SUCCEEDED, FAILED or UNKNOWN from authoritative outcome. Provider/account/retry implementation is not selected.

## 22. Payment UNKNOWN

UNKNOWN never becomes FAILED. Guest/payer sees unresolved outcome without unsafe duplicate payment; Host sees authorized reconciliation responsibility; Sale sees permitted outcome; Admin sees exception/reconciliation where required. Attempt/provenance is preserved.

## 23. Booking Confirmation

Booking begins only when canonical confirmation conditions pass. Booking truth, Confirmed Accommodation Commitment where canonical, Request/Booking relationship, Host/Sale/Guest projections and operational relevance update. No fake Stay lifecycle transition occurs.

## 24. Confirmation Pending / Failure

Accepted Request pending conditions, Payment PROCESSING, Payment FAILED, Payment UNKNOWN, Inventory conflict, authority/precondition change, manual assistance and technical failure remain distinct. None is collapsed into Booking failed, cancellation or auto-release.

## 25. Host Outcome Projection

Host sees Request outcome, Booking only if confirmed, Inventory consequence/commitment where canonical, authorized Payment condition, Guest/Stay handoff relevance and changed attention. It is a canonical projection, not a second state machine.

## 26. Sale Outcome Projection

Sale sees permitted Request/Booking outcome, attribution and canonical Guest follow-up context. No Owner economics, Commission Entitlement or operations authority is implied.

## 27. Guest Outcome Projection

Guest sees Request received/submitting, PENDING, REJECTED, ACCEPTED/confirmation pending, applicable condition, Booking CONFIRMED and Payment UNKNOWN/reconciliation as distinct outcomes. Stay access is not promised before legitimate basis.

## 28. Guest Stay Access Handoff

Confirmed Booking may hand off to scoped Guest Stay Access, preserving Booking ≠ Stay. No fake Stay state or unfinalized credential/QR lifecycle is introduced.

## 29. Operations Handoff

Host, assigned Butler and legitimate BQL receive operational relevance where canonical. Handoff does not grant Booking, Inventory, commercial or financial authority and does not begin detailed B4 interaction design.

## 30. Attention Resolution

Request attention changes because underlying truth changes: rejection, acceptance, confirmation pending, Booking confirmation, conflict or manual assistance. There is no universal attention state machine.

## 31. Request Correction

Incorrect Request information may be correctable, require replacement/supersession or remain policy TBD. Original provenance and effective new truth are preserved; changed conditions require revalidation. No universal Edit/amendment policy is assumed.

## 32. Withdrawal / Expiry

Request withdrawal, timeout and expiry are not invented. If later canonically defined, the interaction will use the domain outcome and preserve history. Until then they are explicit workflow/policy boundaries.

## 33. Duplicate Request

E2 does not auto-merge legitimate intents or create duplicate canonical Requests. Safe recheck/manual reconciliation may be represented; matching/merge/deduplication policy remains open.

## 34. Concurrent Decision

The second actor revalidates and cannot overwrite the first canonical result. Current truth and both actors' provenance remain visible within scope. No technical lock model is defined.

## 35. Multi-Capacity Stress Test

A Sale + delegated Co-host Identity may create under Sale capacity, switch context and accept only under explicit Co-host Booking Authority. Actual accepting capacity is recorded; attribution remains separate. Self-dealing policy is not invented.

## 36. Direct vs Sale Convergence

Entry context, creator, attribution, commercial projection and communication may differ. Request semantics, Host authority, Inventory truth, confirmation conditions, Booking truth and Stay handoff converge. There are no Direct Booking or Sale Booking domain variants.

## 37. Screen Interaction Contracts

Contracts cover Public discovery/date/Request, Sale supply/option/Request, Sale activity/outcome, Host responsibility/Requests, Host Request Detail, Host Booking Detail and Guest outcome/Stay. Each states purpose, entry, truth, actions, authority/revalidation, outcomes, attention, handoff and blocked conditions without layout or components.

## 38. Interaction Sequence Findings

The 12 required sequences—Sale Request, Direct Guest Request, Host inspect/reject/accept, accepted boundary, Payment Attempt, Payment UNKNOWN, Booking confirmation, Inventory conflict, stale/concurrent decision and manual exception—are specified at behavioral step level and stop at unresolved policy boundaries.

## 39. Outcome Projection Matrix Findings

Guest, Sale, Host, Operations and Admin projections distinguish intent, processing, Request PENDING/ACCEPTED/REJECTED/CONFLICTED, confirmation pending, Payment outcomes, Booking CONFIRMED, manual assistance and Inventory conflict. Matrix entries are projections, not new domain states.

## 40. Authority × Action Findings

Direct Request, Sale Request, Accept/Reject, Inventory commitment, Payment attempt, Booking confirmation, correction and reconciliation each have context, capacity, authority, scope/revalidation and unauthorized behavior. Sale/Guest/Butler/BQL cannot accept; Host authority remains effective and scoped.

## 41. Information Visibility Findings

Public, Guest, Sale, Host, Butler, BQL and Admin visibility follows existing PUBLIC, relationship/resource, operational, commercial and admin/exception need-to-know. Guest contact, Owner economics, Payment detail, attribution and provenance remain scope-bound; exact fields are not invented.

## 42. Error / Recovery Findings

Validation, no authority, wrong scope, stale, conflict, technical failure, unknown and manual assistance each have safe recovery. Unknown never recommends duplicate payment/action.

## 43. Consequence Preview

Request submission exposes intent, not reservation. Acceptance exposes accepted Request and known conditions, not immediate Booking. Inventory commitment exposes canonical basis without timing assumptions. Payment exposes condition/attempt outcome. Confirmation exposes Booking truth, not fake Stay transition.

## 44. Mobile / Field

Guest/Sale are mobile-important; Host decisions are desktop-important but must remain understandable where mobile-supported. Current Property/Unit/date truth, acting context, consequence and recovery remain clear across devices.

## 45. Accessibility / Clarity

Request PENDING/ACCEPTED and Booking CONFIRMED are semantically distinct; UNKNOWN differs from FAILED; unavailable decisions have safe reason categories where appropriate; canonical terminology remains consistent and does not rely on color alone.

## 46. TBD / Policy Boundaries

Request expiry/withdrawal/amendment, Offer validity, Temporary Commitment duration/release, Inventory conflict remediation, Payment economics/deadline/grace/retry/UNKNOWN, confirmation exception/cancellation/default/release, Guest credentials/privacy, Sale economics, self-dealing and manual override authority remain unresolved.

## 47. Gap / Blocker Register

Policy, workflow, money, privacy, authority and interaction gaps are classified A/B/C. No D-level CP8 blocker is introduced; independent Request/authority/revalidation work continues while affected detailed branches remain bounded.

## 48. V0 Scope Check

E2 supports Inventory Trust, Network Adoption, Destination Stay Coverage and Commerce Validation using CP5 MUST BUILD/MANUAL-ASSISTED capabilities. No Instant Book default, CRM, quote engine, commission engine, dynamic pricing, PMS, Channel Manager, Affiliate Network, Managed Operations, native app or generic workflow engine is introduced.

## 49. Contradictions Found

No new contradiction was introduced. Guest intent ≠ Request; Offer ≠ Request; Request ≠ Booking/reservation; Booking ≠ Stay; Inventory Commitment ≠ Availability; Availability ≠ Bookability; payment distinctions, attribution/authority and context/visibility boundaries remain intact.

## 50. Readiness Assessment

**ACCEPTED — CP8-E CLOSED.** E2 Request→Booking architecture is accepted; residual commercial/payment, credential, expiry, Sale economics and authority policy details remain explicit TBDs. CP8-F is next and remains not started.

## 51. Validation

- B1/B3 converge on one Request model and one Booking truth.
- Submission processing is distinct from Request PENDING.
- Sale/Guest/Butler/BQL cannot accept; dual-capacity action uses actual Host authority.
- Decision revalidates Request, authority, scope and Inventory.
- Reject does not mutate Inventory without canonical basis; Accept does not automatically create Booking.
- Availability remains derived and Bookability contextual; conflicts preserve truth/evidence.
- Payment Condition/Obligation/Attempt/Default remain distinct; UNKNOWN is never FAILED.
- Duplicate/unknown outcomes do not encourage unsafe mutation.
- Booking confirmation requires canonical conditions; Booking ≠ Stay; handoffs do not grant authority.
- Attribution does not become commission; attention remains projection; corrections preserve provenance.
- All relevant screen concepts have contracts; E1 recovery conventions apply.
- No unresolved expiry, withdrawal, payment, conflict or privacy rule was closed.
- No visual design, prototype, implementation or CP8-F/G/H work started.
- Markdown links are validated after index updates; result is recorded in final handoff.
