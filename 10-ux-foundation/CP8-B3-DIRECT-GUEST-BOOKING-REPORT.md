# CP8-B3 — Direct Guest Booking Journey Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-B Critical Journeys**  
> Status: **ACCEPTED AS BASELINE FOR CP8-B4**  
> Freeze status: **NOT FROZEN**  
> Scope: **B3 only** · 2026-09-20

## 1. Executive Summary

B3 defines the direct Guest journey from Public Marketplace discovery to a truthful Stayora Booking and later operational handoff. The journey is viable as a documented path while preserving the existing architecture: Guest intent is not a Booking; a Booking Request is not an Inventory reservation; Host/authorized Booking Authority remains explicit; Payment remains separate from Booking; and Booking remains separate from Stay.

The direct path does not require Sale attribution or a registered Guest account. It is also not Instant Book. The default path remains `Request → authorized decision → Inventory revalidation/commitment where supported → action-specific payment condition → all confirmation conditions → Booking CONFIRMED`. Instant Book, accountless recovery, conflict handling, payment reconciliation and access/privacy mechanics remain explicit open boundaries.

**Readiness: READY WITH CONDITIONS.** The journey is an accepted baseline for B4 and later B5/C1 work; later interaction work still requires the listed policy and authority boundaries to be decided or explicitly scoped. This report does not freeze CP8 or begin detailed onboarding/Workspace/Interaction/Design System work.

## 2. Sources Reviewed

- [Start Here](../00-start-here/README.md), [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), [Glossary](../00-start-here/GLOSSARY.md), [Decision Register](../00-start-here/DECISIONS.md) and the [Roadmap reconciliation report](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- CP1 Product Foundation, CP2 Domain Map/Glossary/Invariants, CP3 Actor Authority/Core Workflows, CP4 State Machines/Policies, CP5 Oceanami V0 Scope, CP6 Information Architecture and CP7 Conceptual Data Model.
- Accepted [CP8-A UX Foundation](README.md), [CP8-B1 Sale-assisted Booking](CP8-B1-SALE-ASSISTED-BOOKING-REPORT.md) and [CP8-B2 External Booking → Stay](CP8-B2-EXTERNAL-BOOKING-TO-STAY-REPORT.md) baselines.

Source priority remains Founder decisions → canonical confirmed product decisions → CP1–CP6 architecture → CP7 conceptual model → CP8-A/B1/B2 → supporting persistence constraints → working models/hypotheses/references.

## 3. Files Created / Changed

### Created

Inside [B3 Direct Guest Booking](b3-direct-guest-booking/README.md):

- Journey overview.
- Detailed A–L journey specification.
- Cross-context timeline.
- Public truth/Searchability/Availability/Bookability mapping.
- Responsibility handoffs.
- State/domain truth mapping.
- Alternative/failure boundaries.
- Guest-without-mandatory-account outcomes.
- TBD/policy register.
- Domain/workflow/authority gap findings.
- B1 versus B3 comparison.
- B2 convergence note.
- V0/source traceability matrix.

This report is the required `CP8-B3-DIRECT-GUEST-BOOKING-REPORT.md`.

### Changed

- CP8 UX indexes now point to D1 as the current draft execution unit; CP8-A, B1, B2, B3, B4, B5 and C1–C4 remain accepted baselines.
- Start Here, Source of Truth and the outputs README now identify D1 as the current CP8 execution unit.

No CP1–CP7 product, domain, authority, workflow, lifecycle, policy, V0 or data-model decision was changed.

## 4. Canonical Journey Summary

```text
Guest demand
  → Public Marketplace discovery
  → dates / occupancy / public truth
  → Searchability ≠ Availability ≠ Bookability
  → Guest intent
  → Booking Request (`PENDING`)
  → Host / authorized Booking Authority accepts or rejects
  → final Inventory revalidation / finite commitment where supported
  → Required Payment Condition + Payment Attempt
  → all Booking Confirmation Conditions
  → Booking (`CONFIRMED`)
  → Guest confirmation / scoped Stay Access
  → Host / Butler / Destination Operations
```

Removing Sale changes the initiating context and attribution, not the underlying Request/Inventory/Payment/Booking/Stay truth.

## 5. Public Marketplace Findings

Public truth must be sufficient for a Guest to evaluate Destination, Property, Unit, dates, relevant public terms, trust signals and derived availability without exposing Owner economics, Sale economics, settlement, private notes or authority structures. Searchability is discovery eligibility only. Availability is derived Inventory truth. Bookability adds Guest/context/action eligibility. No public view may collapse the three.

## 6. Guest / Identity Findings

The Guest is the direct demand initiator and may be represented as a person/party without a mandatory account. Guest, payer, Request creator, lead guest and Staying Party remain distinct. The mechanism for authentication, recovery, consent and privacy is not selected. A link, visible object or account status cannot substitute for authority or prove operational eligibility.

## 7. Searchability / Availability / Bookability Findings

The journey explicitly handles searchable-but-unavailable, available-but-not-bookable and stale/unknown conditions as separate projections. Viewing and intent never mutate Inventory. Revalidation occurs at the authorized progression boundary. Conflict policy, stale thresholds and actor-specific eligibility remain open where CP4/CP5 do not decide them.

## 8. Booking Request Findings

The Guest (or explicitly supported representative) may create a `PENDING` Request without Sale attribution. Request creation requires the applicable minimum party/terms/consent context but not a confirmed Booking. The Request does not reserve Inventory and does not create Payment or Stay. Acceptance authorizes progression only.

## 9. Authority Findings

Host/Primary Host or Co-host acting under explicit delegated Booking Authority accepts or rejects the Request. Guest, Sale, Butler, BQL, visibility, whitelist and operational assignment do not substitute for that authority. Missing, revoked, multiple or unanswered authority remains an exception/TBD; B3 invents no reassignment, SLA or precedence.

## 10. Inventory Findings

The canonical sequence remains `Request → authorized decision → final revalidation → applicable finite Temporary Exclusive Commitment where supported`. A Request or Guest intent is never a reservation. B3 selects no commitment duration, conflict winner, release behavior, stale threshold or remediation economics.

## 11. Payment Boundary Findings

Required Payment Condition is specific to a commercial action such as Booking Confirmation. Payment Obligation and Payment Attempt remain separate. `SUCCEEDED` is evidence for evaluation, not Booking by itself. `UNKNOWN` remains unresolved and is not silently failed, defaulted, released or confirmed. Deposit, deadline, grace, refund, retry, provider and legal treatment remain policy/legal boundaries.

## 12. Booking Confirmation Findings

Booking begins only at `CONFIRMED` after valid terms, authority, exclusive Inventory truth, applicable payment condition and required consent/compliance conditions pass. There is no pre-confirmation Booking. If one condition fails, preserve Request/payment/exception truth without false confirmation.

## 13. Guest Stay Access Findings

After confirmation, an eligible Guest/Staying Party may receive scoped confirmation and Stay Access information. B3 does not decide account creation, authentication, QR/token mechanics, privacy disclosure or credential lifecycle. Access is a projection and does not create Inventory, Payment, Booking Authority or operational authority.

## 14. Operations Handoff Findings

Confirmed accommodation may become operationally relevant to Host, Butler and Destination/BQL through a separate Stay representation and scoped assignment. They receive need-to-know dates, party/access and issue information; they do not gain commercial authority. Stay lifecycle remains separate from Booking; B4 now specifies this operational handoff.

## 15. Cross-Context Projection Findings

The same canonical truth projects differently: Guest sees progress and eligible access; Host sees decision responsibility; Inventory sees effective commitments; Money sees obligations/attempts; Booking sees confirmation conditions; Operations sees a scoped Stay. No projection can be treated as another domain’s source of truth.

## 16. Responsibility Handoffs

The handoff chain is Marketplace truth → Guest decision → Request → Host/Booking Authority → Inventory revalidation → Payment condition → Booking confirmation → Guest access → Operations. Each handoff transfers only the bounded responsibility described in [05-responsibility-handoffs.md](b3-direct-guest-booking/05-responsibility-handoffs.md).

## 17. Alternative / Failure Paths

The B3 register covers no suitable supply, unavailable/stale/unknown availability, incomplete Request, rejection, unanswered Request, missing authority, conflicts, payment not initiated/processing/failed/unknown/succeeded-with-other-failure, Guest abandonment, duplicate Request, lost session and inability to confirm. Every unresolved branch is classified as supported behavior or policy/workflow/authority/UX/domain/integration TBD.

## 18. Guest Without Mandatory Account

The journey preserves the Request, Payment and Booking relationship independently of a browser session or registered account. Required outcomes are identification, status, payment completion/reconciliation, confirmation and eligible access. Mechanisms remain undecided and must not be inferred from persistence convenience.

## 19. Instant Book Boundary

Direct Guest Booking is not Instant Book. The B3 default keeps the Request and authorized Host decision. Instant Book remains an optional, controlled branch requiring explicit eligibility, authority, inventory, payment and conflict policy before it can be treated as a requirement or V0 default.

## 20. TBD / Policy Boundaries

The main open boundaries are Request timeout/withdrawal, authority resolution, commitment window/expiry, conflict precedence, payment economics/reconciliation/default, direct/Sale attribution, Instant Book eligibility, accountless recovery, public disclosure, Stay creation/access timing and operational projection. See [09-tbd-policy-register.md](b3-direct-guest-booking/09-tbd-policy-register.md). No TBD was silently closed.

## 21. Domain / Workflow / Authority Gaps

The gaps are missing policy or workflow detail around accountless continuity, direct Request capability, actor-specific Bookability, payment exception handling, operational projections and provenance. B3 does not create an aggregate, entity, permission, state or subsystem to fill a gap.

## 22. B1 vs B3 Findings

B1 uses Sale as discovery/option/Request creator; B3 uses Guest/Public Marketplace. Both converge on the same Host authority, Inventory, Payment, Booking and Stay semantics. Direct B3 must not inherit Sale attribution or create a second commercial model.

## 23. B2 Convergence Findings

B3 and B2 converge at Inventory truth, Stay representation, Guest access and Operations projections. B3 remains Stayora-originated commerce. B2 remains External Commerce → Inventory Truth and/or Stay, without requiring a Stayora Booking. Operational convergence does not erase commercial origin.

## 24. V0 Scope Check

B3 stays within CP5’s direct marketplace, Booking Request, Host decision, applicable Inventory/Payment/Booking confirmation, scoped Guest access and operational handoff capabilities. It does not expand into CRM, advanced Lead Distribution, Affiliate Network, dynamic pricing, PMS/Channel Manager, Managed Operations, advanced loyalty/reputation, native apps, marketing automation or workforce management.

## 25. Contradictions Found

No new contradiction was introduced. B3 explicitly prevents these common contradictions:

- Direct Guest discovery is not Sale attribution.
- Direct Booking is not Instant Book.
- Guest intent/Request is not Inventory reservation.
- Payment success is not Booking confirmation by itself.
- Guest account is not Guest identity/party.
- Booking is not Stay or Check-in.
- Butler/BQL visibility is not commercial authority.
- B3 direct commerce is not B2 External Booking.

Existing upstream TBDs remain unresolved rather than being treated as contradictions.

## 26. Readiness Assessment

**READY WITH CONDITIONS** for Founder/Product Architect review.

Conditions:

1. Preserve the explicit Request, Authority, Inventory, Payment, Booking and Stay boundaries in any later interaction work.
2. Decide or explicitly scope Request timeout/authority, Inventory conflict/commitment, payment reconciliation/economics, accountless recovery/privacy and access timing before implementation-level specification.
3. Keep Instant Book as a separate controlled branch; do not make it the direct default.
4. Do not interpret this report as screen design, visual approval, implementation authorization or Founder Freeze.

## 27. Validation

- Direct Booking does not require Sale: **PASS**.
- No unsupported Sale attribution: **PASS**.
- Direct Booking not converted into Instant Book: **PASS**.
- Guest account not made mandatory: **PASS**.
- Request remains separate from Booking and does not automatically reserve Inventory: **PASS**.
- Searchability, Availability and Bookability remain distinct: **PASS**.
- Booking Authority remains explicit: **PASS**.
- Inventory revalidation occurs after authorized progression: **PASS**.
- Payment remains separate; `UNKNOWN` is not silently failed/defaulted: **PASS**.
- Booking begins only at canonical confirmation: **PASS**.
- Booking remains separate from Stay: **PASS**.
- Guest access does not resolve authentication, QR or privacy: **PASS**.
- Butler/BQL do not gain commercial authority: **PASS**.
- Authority/lifecycle/object/V0 claims trace to CP3–CP7 and CP8 baselines: **PASS**.
- No persistence assumption became product policy: **PASS**.
- No TBD silently closed: **PASS**.
- No new domain concept or lifecycle state introduced: **PASS**.
- No screen, wireframe, prototype, Figma, component, token, code, API, schema or migration created: **PASS**.
- B4 and B5 are documented as separate workstreams; no later CP8 journey started: **PASS**.
- Markdown file/anchor links: **PASS — 163 Markdown files, 0 broken file/anchor links**.

Return this report to the Founder and Product Architect as the accepted B3 journey baseline. Do not mark CP8 complete or begin B5 until explicitly directed.

## Current CP8-E closure overlay

The historical readiness assessment above predates FD-01 → FD-19. For CP8-E closure, B3 is covered by E2 and the accepted E1–E4 architecture. FD-06/07, FD-08/09, FD-10/11 and FD-17/18/19 close the relevant architecture; credential/security, Request expiry/amendment, payment details, economics and privacy remain TBD.
