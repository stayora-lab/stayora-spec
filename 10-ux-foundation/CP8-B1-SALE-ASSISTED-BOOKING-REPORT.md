# CP8-B1 — Sale-Assisted Booking Journey Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-B Critical Journeys → B1 Sale-assisted Booking**  
> Status: **ACCEPTED AS BASELINE FOR CP8-B2 / CP8-B3**  
> Freeze status: **NOT FROZEN**  
> Date: 2026-09-19

## 1. Executive Summary

CP8-B1 specifies the conceptual Oceanami V0 Sale-assisted Booking journey from Guest need through Sale discovery, Guest intent, Booking Request, Host decision, applicable Inventory Commitment, payment condition, Booking confirmation and the handoff into scoped Guest Stay Access/operations.

The architecture supports a coherent path with one important discipline: Sale can discover, prepare an option and create a Booking Request when eligible, but Sale capacity alone cannot accept that Request. Acceptance requires Host/Primary Host authority or valid delegated Booking Authority. Request remains separate from Booking and does not reserve Inventory. Payment remains separate from Booking until all canonical confirmation conditions pass. Booking confirmation does not become Check-in or Completed Stay.

The B1 deliverables are **READY WITH CONDITIONS** for later journey work. The successful-payment branch is sufficiently defined to continue conceptually, while inventory conflicts, unanswered Requests, payment `UNKNOWN`, grace/default, exact commitment windows, access/privacy and other policy branches remain explicit. No later journey, screen design or implementation work has started.

## 2. Sources Reviewed

- [Start Here](../00-start-here/README.md), [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), [Glossary](../00-start-here/GLOSSARY.md), [Decision Register](../00-start-here/DECISIONS.md) and [Roadmap Reconciliation Report](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- CP1 Product Foundation: Marketplace, actors, destination, trust, money, Oceanami Pilot, success metrics, scope and open questions.
- CP2 [Domain Map/Glossary/Invariants](../02-domain/README.md).
- CP3 [Actor Authority](../03-actor-authority/README.md) and [Core Workflows](../04-core-workflows/README.md), especially Sale-assisted Request Booking, authority and cross-workflow invariants.
- CP4 [State Machines and Policies](../05-state-machines-policies/README.md), especially Request/Booking, Inventory, Payment, Stay, Booking policy, Distribution and cross-policy reconciliation.
- CP5 [Oceanami V0 Scope](../06-v0-scope/README.md), critical journeys, capability matrix, domain boundaries and pilot metrics.
- CP6 [Information Architecture](../07-information-architecture/README.md), especially Sale, Host, Guest Access, Operations and cross-surface navigation.
- CP7 [Conceptual Data Model](../08-conceptual-data-model/README.md), especially Inventory/Booking, Money, Stay, provenance and invariants.
- CP7 [Supporting Persistence Architecture](../09-database-design/README.md) only as a constraint reference.
- Accepted [CP8-A UX Foundation](README.md) and its principles, actor/context model, surface model, semantics, traceability and blocker register.

Source priority remains Founder decisions → canonical confirmed product decisions → CP1–CP6 architecture → CP7 conceptual model → CP8-A → supporting persistence → working models/hypotheses/references.

## 3. Files Created / Changed

### Created

Inside [B1 Sale-assisted Booking](b1-sale-assisted-booking/README.md):

- Journey overview and canonical boundary.
- Detailed journey specification.
- Cross-context timeline.
- Responsibility handoffs.
- State/domain truth mapping.
- Alternative/failure boundaries.
- TBD/policy boundary register.
- Domain/workflow/authority gap findings.
- V0/source traceability matrix.

This report is the required `CP8-B1-SALE-ASSISTED-BOOKING-REPORT.md`.

### Changed

- [CP8-A README](README.md) now links to the current B1 workstream and records CP8-A as the accepted baseline for CP8-B.
- CP8-A component documents and its report now carry the accepted-baseline metadata; their UX content is unchanged.
- [Start Here README](../00-start-here/README.md), [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md) and [outputs README](../../README.md) now identify D1 as the current execution unit; B1 remains an accepted journey baseline.

These index/status edits do not change CP1–CP7 product, domain, authority, workflow, lifecycle, policy, V0 or data-model decisions.

## 4. Canonical Journey Summary

```text
Guest need
  → Sale searches actual Availability and Public Price
  → Sale presents/discusses conceptual Offer
  → Guest intent to proceed
  → Sale creates Booking Request (`PENDING`)
  → Host / authorized Co-host accepts or rejects
  → revalidate Inventory; Temporary Exclusive Commitment where applicable
  → Required Payment Condition and Payment Attempt
  → evaluate Booking Confirmation Conditions
  → Booking `CONFIRMED` + Confirmed Accommodation Commitment
  → Guest confirmation/scoped Stay Access
  → Host/Butler/BQL operational relevance
```

The sequence is a UX reasoning path, not a new state machine. Offer ownership, Lead timing, exact payment rules, conflict policy and access details remain open where upstream documents say so.

## 5. Journey Phases

The detailed specification covers:

- Demand / Guest Need — understand minimum demand without creating a CRM.
- Discovery — Sale searches supply and distinguishes searchable, Available and actor-specific Bookable.
- Option / Guest Choice — present conceptual Offer/terms; Guest intent does not create a new object by assumption.
- Booking Request Creation — Sale creates a truthful `PENDING` Request on the Guest demand context.
- Host Decision — valid Host/Co-host authority accepts or rejects; `ACCEPTED` is not a Booking.
- Inventory Commitment — revalidate and establish a finite Temporary Exclusive Commitment only where supported.
- Payment Requirement — evaluate a specific Required Payment Condition and separate Payment Obligation/Attempt.
- Confirmation — create Booking only when canonical conditions pass.
- Booking → Stay Access / Operations — hand off confirmed commerce without equating it with Check-in or Completed Stay.

## 6. Actor / Context Findings

- Guest provides demand, consent and relevant party information; Guest, Payer, Booking Creator, Lead Guest and Staying Party are not collapsed.
- Sale discovers supply, presents options and creates/monitors Request within eligibility, relationship and transaction scope. Sale does not accept.
- Host/Primary Host is the action owner for commercial acceptance where valid authority exists.
- Co-host may accept only under explicit delegated Booking Authority and scope.
- Butler and Destination/BQL appear after confirmed/represented Stay becomes operationally relevant; they do not decide commercial Requests.
- Stayora/Admin appears only for canonical support, exception, reconciliation or audit paths; no super-user authority is invented.

## 7. Authority Findings

The critical B1 authority rule is preserved:

```text
Sale capability → discover / offer / create Request
Host or delegated Booking Authority → accept / reject Request
```

If one Identity is both Sale and Co-host, acceptance is valid only when performed under the Co-host authority context and recorded as such. Screen visibility, whitelist, attribution, ownership or operational assignment does not substitute for Booking Authority. No technical RBAC/ABAC is specified.

## 8. Domain Object / State Findings

- Offer is a conceptual proposition; its ownership/lifecycle remain TBD.
- Request lifecycle uses existing `PENDING`, `ACCEPTED`, `REJECTED`, `EXPIRED`, `CONFLICTED` conceptual outcomes. B1 does not add one.
- Request does not reserve Inventory.
- Inventory is derived from effective Commitments; Temporary Exclusive Commitment is distinct from Request, Availability and Payment Attempt.
- Payment Attempt uses existing `INITIATED`, `PROCESSING`, `SUCCEEDED`, `FAILED`, `UNKNOWN` reasoning; `UNKNOWN` is not failure.
- Booking begins at `CONFIRMED` after confirmation conditions; there is no pre-confirmation Booking.
- Stay remains independent and is not automatically Check-in or Completed after Booking confirmation.

## 9. Inventory Findings

Sale can read relevant derived Availability and should distinguish it from Searchability and actor-specific Bookability. Final revalidation is required at the commitment boundary. Authorized acceptance may enable a finite Temporary Exclusive Commitment where policy supports it; Request creation alone never does.

Existing conflicts must preserve both facts/commitments and surface an Inventory Conflict/exception. B1 does not select channel priority, a conflict winner, stale-data threshold, release behavior or remediation economics.

## 10. Payment Boundary Findings

Required Payment Condition is a condition for a specific commercial action such as Booking Confirmation. It is not all future Payment Obligations. Payment Obligation, Payment Attempt, provider outcome, condition satisfaction and Booking confirmation remain distinct.

The successful branch can conceptually proceed from a satisfied condition to confirmation. `FAILED` and especially `UNKNOWN` do not authorize automatic cancellation, Payment Default, release or Booking creation. Exact amount, percentage, deadline, grace, reconciliation, refund, cancellation, default, provider retry and legal treatment remain policy/legal boundaries.

## 11. Responsibility Handoffs

The handoff document records Guest → Sale, Sale → shared discovery, Sale → Guest option, Guest → Sale intent, Sale → Host Request, Host → Inventory/Payment progression, payment → confirmation evaluation, confirmation → Guest/Sale/Host projections and confirmation → Guest Stay Access/Operations.

The most important receiving-context rule is that Host/authorized Booking Authority receives the Request decision responsibility, while Butler/BQL receive only later operational responsibility. A failed handoff remains visible as missing authority, unresolved policy or exception; it is not silently completed.

## 12. Cross-Context Projection Findings

The same truth projects differently:

- **Request created:** Guest sees pending decision; Sale sees accountability/progress; Host sees action responsibility; Butler/BQL normally see nothing operational yet; Admin sees only assigned exceptions.
- **Host decision:** Guest/Sale see accepted/rejected status; Host sees authority/result; Inventory revalidates; no Booking exists merely because accepted.
- **Payment required:** Guest/Payer sees the specific condition; Sale/Host see scoped assurance; Money owns obligation/attempt; no one may treat it as all future obligations or Booking confirmation.
- **Booking confirmed:** Guest sees confirmed accommodation/access preparation; Sale sees attributed commerce; Host sees fulfillment responsibility; Butler/BQL may receive need-to-know operational work; Stay remains separate.

## 13. Alternative / Failure Paths

The B1 register covers no suitable supply, searchable/not available, stale/unknown availability, rejection, unanswered Request, missing authority, conflicts, payment not initiated, succeeded, failed, uncertain, unmet conditions, Guest abandonment, inability to confirm and system/integration uncertainty.

Existing architecture supports truthful handling for no match, rejection, no automatic reservation, explicit authority, payment outcome distinction and no false confirmation. Policy remains open for timeout/SLA, commitment expiry, conflict resolution, Payment Default/grace, refund/cancellation, provider reconciliation and access details.

## 14. TBD / Policy Boundaries

The central open boundaries are Offer ownership/validity, Request timeout/withdrawal, temporary commitment window, inventory conflict/stale behavior, Required Payment Condition economics/timing, Payment `UNKNOWN` reconciliation, confirmation condition exceptions, QR/privacy/access lifecycle, Sale economics and manual-assist authority. The complete register is [07-tbd-policy-register.md](b1-sale-assisted-booking/07-tbd-policy-register.md).

Each entry preserves known truth and names the downstream behavior that cannot yet be finalized. No TBD was silently closed.

## 15. Domain / Workflow / Authority Gaps

The findings are:

- Offer ownership/lifecycle — existing upstream conceptual object, unresolved boundary; do not add an aggregate here.
- Request unanswered/missing authority outcome — policy/workflow gap; do not invent SLA or auto-reassignment.
- Payment/inventory behavior — policy gap, not missing domain concepts; do not add states or rules.
- Guest access data — UX/privacy gap at the later handoff; do not design QR fields here.

No new domain entity, actor, permission, state, lifecycle or V0 capability is required to express the B1 happy path.

## 16. Contradictions Found

No new contradiction was introduced. B1 explicitly reconciles the likely journey simplifications that could have caused contradictions:

- “Sale accepts” is corrected to Sale creates Request; Host/authorized Co-host accepts.
- “Request reserves” is corrected to Request pending with no automatic Inventory reservation.
- “Payment means Booking” is corrected to Payment condition/Attempt evaluated with all confirmation conditions.
- “Confirmed Booking means Stay” is corrected to a separate Booking → Stay Access/Operations handoff.
- “Available means bookable” is corrected to derived Availability plus actor/context eligibility.
- External Accommodation is not imported into this Sale-assisted Booking path or converted into Stayora Booking.

## 17. V0 Scope Check

The journey uses CP5 MUST BUILD and MANUAL-ASSISTED capabilities only: Sale inventory search, Public Price/basic Offer/quote, Booking Request, Host/authorized Co-host accept/reject, Temporary Commitment where applicable, Required Payment Condition, basic Payment Obligation/Attempt/evidence, Booking Confirmation, scoped Guest access and operational handoff.

It does not expand into full CRM, advanced Lead Distribution, Affiliate Network, dynamic pricing, full PMS/Channel Manager, Managed Operations, advanced loyalty/reputation, native apps or workforce management.

## 18. Readiness Assessment

**READY WITH CONDITIONS** for proceeding beyond B1.

Conditions:

1. Preserve all upstream status labels and policy boundaries.
2. Resolve or explicitly scope the C-level blockers before detailed interaction work: conflicts, Request timeout, payment `UNKNOWN`/Default, commitment expiry, exception economics and access/privacy.
3. Keep Offer ownership/lifecycle as a documented open boundary.
4. Do not interpret this journey specification as screen design, visual approval or implementation authorization.

CP8-B1 is the Sale-assisted journey baseline. Direct Guest Booking is now documented in CP8-B3; Stay Operations and Inventory Intervention have not started.

## 19. Validation

- Every authority claim traces to CP3 and CP8-A: **PASS**.
- Every lifecycle/state claim traces to CP4/CP7: **PASS**.
- Every V0 capability claim traces to CP5: **PASS**.
- Every surface/context claim traces to CP6/CP8-A: **PASS**.
- Every domain-object claim traces to CP2/CP7: **PASS**.
- Request not collapsed into Booking: **PASS**.
- Request not treated as automatic Inventory reservation: **PASS**.
- Sale capacity not treated as Booking Authority: **PASS**.
- Availability not collapsed into Bookability: **PASS**.
- Payment not collapsed into Booking: **PASS**.
- Booking not collapsed into Stay: **PASS**.
- Supporting persistence not promoted to product policy: **PASS**.
- No TBD silently closed: **PASS**.
- No new domain concept silently introduced: **PASS**.
- No screen, wireframe, visual UI, prototype, Figma artifact, component, token, code, API, schema or migration created: **PASS**.
- No later journey started: **PASS**.
- Markdown links after B1 expansion: **PASS — 136 Markdown files, 0 broken file/anchor links**.

Return this report to the Founder and Product Architect as the accepted B1 journey baseline. Do not mark CP8 complete or begin B4/B5 until explicitly directed.

## Current CP8-E closure overlay

The historical readiness assessment above predates FD-01 → FD-19. For CP8-E closure, B1 is covered by E2 and the accepted E1–E4 architecture. FD-08/09, FD-10/11 and FD-17/18/19 close the relevant interaction architecture; payment amounts/deadlines/grace/retry/refund/default, Sale economics, self-dealing and specific grants remain TBD.
