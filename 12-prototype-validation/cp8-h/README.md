# CP8-H — V0 Acceptance Package

> Status: **ACCEPTED — CP8-H COMPLETE**
> Last reviewed: 2026-09-30 · Owner: Product Architect
> Canonical input baseline: `b71833fff68c8178eb7d4683e8d76e4d3d4ad308`
> CP8-G: **ACCEPTED — CLOSED** · CP8-H: **ACCEPTED — CLOSED** · Implementation Planning: **READY TO BEGIN**

## 1. Purpose, baseline and exit boundary

CP8-H packages the accepted Oceanami V0 product and UX baseline for [Implementation Planning](../../00-start-here/README.md#cp8-g-and-cp8-h). It summarizes constraints and links their canonical owners; it does not design another UX pass, iterate the prototype, choose implementation mechanisms, author the Implementation Plan or certify production readiness. CP8-H is complete; the existing roadmap proceeds CP8-G → CP8-H → Implementation Planning → Implementation → Oceanami Pilot → Validation / Learning → Post-V0 Roadmap.

CP8-H was reviewed and accepted as the implementation handoff under the existing [CP8-H boundary](../README.md#boundary): V0 UX baseline, validated journeys, V0 user stories and acceptance criteria derived from canonical sources, remaining TBD/Hypothesis register, deferred scope, Protected Baseline verification and handoff references are present. This is a review condition for the package, not a new product gate. The [Public Exposure Review](../../00-start-here/SOURCE_OF_TRUTH.md#public-exposure-review) is recorded as completed; repository privatization remains an operational access-recovery task.

## 2. V0 scope and non-goals

The controlling implementation classes are [CP5 MUST BUILD / MANUAL-ASSISTED / DEFER](../../06-v0-scope/README.md) and [CP5 critical journeys](../../06-v0-scope/03-critical-journeys.md), refined by later CONFIRMED ADRs. Manual assistance still preserves authoritative facts, action-time authority, provenance and audit.

| Class | V0 package boundary | Canonical source |
|---|---|---|
| **MUST BUILD** | Marketplace discovery and Public Price; direct and Sale-assisted Request → authorized acceptance → applicable Inventory/Payment conditions → Booking Confirmation → Stay; derived Availability, commitments/blocks, external accommodation recording, conflict detection, Guest confirmation/scoped access, Butler/BQL operations, Checkout and Completion truth, audit. | [CP5 capability matrix](../../06-v0-scope/04-capability-matrix.md), [critical journeys](../../06-v0-scope/03-critical-journeys.md) |
| **MUST BUILD — narrowed decisions** | V0 Host direct external recording without a Report stage; Host onboarding and Primary transfer with standard unit-scoped authority; Guest Request minimum name + email-or-phone without mandatory Account, protected by Guest Credential/access eligibility; Villa Readiness independent of Stay; V0 Checkout Assessment. | [ADR-P074–P077](../../00-start-here/DECISIONS.md), [ADR-P072/P073](../../00-start-here/DECISIONS.md) |
| **MANUAL-ASSISTED / CONTROLLED** | Conflict resolution, Incident consequences, complex refunds/adjustments, Settlement/Payout execution, Sale/Butler eligibility review, Verified assessment, minimal Lead assignment, Admin-assisted hosting verification and exceptions, transfer payout handling. Manual actors never acquire authority through a role label alone. | [CP5 capability matrix](../../06-v0-scope/04-capability-matrix.md), [ADR-P075/P076](../../00-start-here/DECISIONS.md) |
| **OPTIONAL / PILOT** | Instant Book is architecture-supported but not a V0 MUST; eligibility and conditions remain open. | [CP5 Direct Guest journey](../../06-v0-scope/03-critical-journeys.md), [B3-T08](../../10-ux-foundation/b3-direct-guest-booking/09-tbd-policy-register.md) |
| **OUT OF SCOPE — V0 / POST-V0** | External Report→Fact workflow (ADR-P074); independent-property onboarding (ADR-P075); full Affiliate network/payout, sophisticated CRM, PMS, Channel Manager, dynamic pricing, native apps, automated Verified enforcement, advanced reputation/scoring, Stayora Managed and other [CP5 deferred subsystems](../../06-v0-scope/07-out-of-scope.md). Listed/open supply is not Managed; minimal Verified assessment can be manual-assisted. | [CP5 exclusions](../../06-v0-scope/07-out-of-scope.md), [domain boundaries](../../06-v0-scope/05-domain-boundaries.md), [ADR-P074/P075](../../00-start-here/DECISIONS.md) |

## 3. Actor, authority and required journey matrix

Every privileged action uses the actual actor's valid capability, relationship, resource and lifecycle scope. Role ≠ Authority; Owner ≠ Primary Host ≠ Authority; Butler Assignment ≠ Stay Access; Working Context/Visibility ≠ Authority; Guest Credential ≠ Host/Admin grant. See [CP3 authority invariants](../../03-actor-authority/06-authority-invariants.md), [Effective Permission](../../03-actor-authority/05-effective-permission.md) and [ADR-P077](../../00-start-here/DECISIONS.md#adr-p077).

| Journey and starting condition | Actor / authorized action boundary | Intended outcome and critical truth | Current evidence / source |
|---|---|---|---|
| Discovery → available unit/dates → Request → waiting → confirmation → upcoming Stay | Guest submits a commercial Request with name and email-or-phone; accountless protected access requires recognized Guest Credential/access eligibility. Host/authorized Co-host, not Guest or Sale, makes the commercial decision. | Request is not a Booking or Inventory reservation; applicable conditions and authoritative confirmation establish Booking/Stay. | [CP5 Direct Guest](../../06-v0-scope/03-critical-journeys.md), [ADR-P077](../../00-start-here/DECISIONS.md#adr-p077), [CP8-G mandatory journeys](../README.md#mandatory-v0-prototype-journeys). G1/G4 representative-user evidence is carried, not PASS. |
| Sale demand → Request → Host acceptance → exclusive or competitive confirmation | Sale searches/quotes/creates Request; Host or authorized Co-host selects handling and accepts/rejects. Sale eligibility/relationship does not grant Host Booking Authority. | Exclusive handling may establish a finite hold; competitive acceptance alone establishes none. One qualifying confirmation creates Booking; conflicting overlapping Requests become CONFLICTED, not REJECTED. | [CP5 Sale](../../06-v0-scope/03-critical-journeys.md), [ADR-P070/P071](../../00-start-here/DECISIONS.md), [CP8-G rows 20–21](../README.md#v2-baseline-coverage--commit-5c39748). |
| Butler Today → Prepare → Arrival → Check-in → In-stay → Departure → Checkout | Assigned Butler acts only under applicable operational authority; villa's Host has only the supporting Villa Readiness path in ADR-P072. | Arrival/Departure observations differ from Check-in/Checkout; Checkout Assessment precedes Completion evaluation; readiness does not block Completion. | [CP8-G Butler](../README.md#mandatory-v0-prototype-journeys), [ADR-P072/P073](../../00-start-here/DECISIONS.md), rows 6–8; row 8 remains PARTIAL. |
| Incident → attention/intervention; Inventory conflict → reconciliation | Authorized Host/BQL/operations actor by function and resource; visibility or reporting does not grant Inventory/financial consequence authority. | Protective Hold, Maintenance Block and Commitment remain separate; conflicting truths stay visible until authorized resolution. | [CP5 Incident/Availability](../../06-v0-scope/03-critical-journeys.md), [CP8-G Exception](../README.md#mandatory-v0-prototype-journeys), rows 11–12. |
| External accommodation information → direct record → applicable commitment/Stay | Appropriately scoped Host records authoritatively; ordinary Sale/Butler do not submit V0 External Reports. | Fact and applicable External-backed Commitment are distinct truths in one workflow; no fake Stayora Booking or automatic commission. | [CP5 External journey](../../06-v0-scope/03-critical-journeys.md), [ADR-P074](../../00-start-here/DECISIONS.md#adr-p074), [reconciled WF-03](../../04-core-workflows/03-external-booking-to-stay.md), CP8-G row 14. Row 13 is OUT OF SCOPE — V0. |
| Destination Today → arrivals/in-house/departures → detail → attention | Destination-scoped BQL sees and acts only within granted operational function; Admin-assisted exceptions use attributable Admin authority, never silent impersonation. | Operational visibility is not commercial/financial visibility or Host authority. | [CP8-G BQL](../README.md#mandatory-v0-prototype-journeys), [CP5 actors](../../06-v0-scope/02-pilot-actors.md), row 17; full BQL-attention evidence is a recorded limit. |
| In-Destination hosting request or valid Primary-transfer designation → approved relationship / accepted transfer | Destination-authorized Admin approves onboarding; current Primary designates; recipient accepts normal transfer without a new Admin approval. | Exactly one Primary; accepted transfer atomically establishes the new relationship and standard capability set, preserving Booking/Stay history. | [ADR-P075/P076](../../00-start-here/DECISIONS.md), [WF-07](../../04-core-workflows/09-owner-onboarding.md), [CP5 manual-assisted matrix](../../06-v0-scope/04-capability-matrix.md). Not separately labeled a mandatory CP8-G prototype journey. |

### V0 user-story and acceptance trace

These are compact handoff statements derived from the linked canonical journeys, not new product decisions or a claim that independent users validated them.

| Actor need | Acceptance boundary to carry into Implementation Planning |
|---|---|
| As a Guest, understand what is requested, what happens next and whether a Booking is confirmed. | The experience distinguishes Request from Booking; creation enforces ADR-P077 minimum contact; accountless protected access requires recognized eligibility. |
| As a Sale, follow the Guest's demand; as a Host, decide on the Request. | Sale does not gain Host authority; exclusive and competitive handling produce the distinct Inventory/confirmation outcomes of ADR-P070. |
| As a Butler, know which villa needs preparation, arrival and departure actions today. | Assignment and action authority are checked; observations, Stay transitions, Checkout Assessment and Villa Readiness remain distinct. |
| As an authorized operations actor, surface an Incident or conflict for intervention. | Protective Hold, Maintenance Block, Commitment and financial consequence are not collapsed into one action or state. |
| As a scoped Host, record external accommodation for shared operations. | One direct V0 workflow establishes distinct Fact and applicable Commitment without an External Report stage or fake Stayora Booking. |
| As BQL, see destination operations and matters needing attention. | Need-to-know operational projection does not grant Host/Admin or financial authority; representative journey validation remains carried. |
| As an incoming Primary, accept a valid transfer. | Acceptance atomically establishes the relationship, Primary status and standard unit authority; exceptional outgoing grants are not copied. |

## 4. Lifecycle, state and critical-invariant contract

This is a handoff index, not a new transition graph. Use the linked canonical policy for exact action conditions.

| Domain truth / source | Implementation-sensitive boundary |
|---|---|
| [Request and Booking](../../05-state-machines-policies/02-booking-request-and-booking.md); ADR-P070/P071 | Request PENDING/ACCEPTED/REJECTED/EXPIRED/CONFLICTED is separate from Booking CONFIRMED/CANCELLED. Acceptance ≠ Confirmation. Request, temporary commitment and payment have separate clocks. |
| [Inventory commitment model](../../05-state-machines-policies/01-inventory-commitment-model.md), [domain invariants](../../02-domain/03-domain-invariants.md) | Availability derives from effective commitments over Bookable Unit × time; no persisted four-state Availability enum. Fact ≠ Commitment. No-show/physical absence does not release an effective accommodation right. External confirmed inventory has equal authority. |
| [Stay lifecycle](../../05-state-machines-policies/04-stay-lifecycle.md), [Completion policy](../../05-state-machines-policies/16-stay-completion-policy.md), ADR-P073 | Booking ≠ Stay; arrival observation ≠ Check-in; departure observation ≠ Checkout; Checkout ≠ Completion. Only qualifying unresolved checkout damage/compensation Incident blocks V0 Completion; not every open Incident. |
| [Villa Readiness](../../05-state-machines-policies/23-villa-readiness-lifecycle.md), ADR-P072 | DIRTY → CLEANING → READY persists across Stays. It is neither Stay state, Completion blocker, Availability Block nor Inventory Commitment. |
| [Payment](../../05-state-machines-policies/03-payment-lifecycle.md), [Settlement/Payout](../../05-state-machines-policies/05-settlement-and-payout.md), ADR-P076 | Payment UNKNOWN ≠ FAILED; required payment condition need not mean fully paid. Payment Received ≠ Settlement/Payout. Settlement determines entitlement; payout executes it. Primary-transfer payout choice is narrowly cohort-scoped and does not rewrite historical Money truth. |
| [Incident](../../05-state-machines-policies/07-incident-lifecycle.md), ADR-P073 | Observation/Complaint ≠ Incident ≠ Finding ≠ Responsibility ≠ Consequence. RESOLVED ≠ CLOSED; damage resolution does not itself execute Money. |
| [Hosting/transfer](../../00-start-here/DECISIONS.md#adr-p075), [authority capabilities](../../03-actor-authority/02-authority-capabilities.md) | Hosting Relationship Request outcome, hosting relationship, Primary status and authority grants are distinct. Normal transfer acceptance establishes the standard set atomically; actor-specific grants are not copied. |
| [Guest access](../../00-start-here/DECISIONS.md#adr-p077), [need-to-know invariant](../../02-domain/03-domain-invariants.md) | Contact Identity ≠ Guest Credential ≠ Resource Identifier; URL or matching email/phone does not authorize Guest data access. Credential/access eligibility is scoped by relationship/lifecycle and is not Host/Admin authority. |

Domain states above belong to their own aggregates. `ARRIVAL`, `PREPARATION`, `READY` and `IN_STAY` may be observations, operational milestones or presentation labels rather than extra Stay states; unpaid/partial/paid are derived obligation labels, not Payment Attempt states. [The lifecycle map](../../05-state-machines-policies/00-lifecycle-map.md) classifies modeling form without defining transitions.

## 5. IA, data and UX handoff map

| Input | Consume in Implementation Planning | Boundary |
|---|---|---|
| [CP6 IA](../../07-information-architecture/README.md): seven surfaces, workspaces, working contexts, handoffs, V0 sitemap | Preserve responsibility-based navigation and resource-scoped projections. | CP6 ≠ API/routes or permission implementation. |
| [CP7 conceptual model](../../08-conceptual-data-model/README.md): identity/relationships, aggregates, Inventory/Booking/Stay/Money, provenance and projections | Preserve domain ownership, temporal validity and historical truth. | Aggregate candidate ≠ database table. |
| [CP7 supporting persistence direction](../../09-database-design/README.md) | Use its constraint/transaction/projection direction as supporting architecture. | CP7 ≠ final physical schema, migration or implementation freeze. |
| [CP8-E Detailed Interaction](../../11-detailed-interaction/README.md) and [CP8-F design language](../../10-ux-foundation/f2-prototype-ready-design-language/README.md) | Carry action grammar, outcome copy, consequential-action and seven-surface presentation patterns. | CP8-F ≠ production component library or global UX freeze. |
| [CP8-G accepted validation record](../README.md), with prototype SHAs in its iteration log | Carry reviewed guardrail states, journey learnings, historical failures and prototype assumptions with provenance. | CP8-G acceptance ≠ production readiness; prototype behavior does not decide TBD policy. |

## 6. Accepted open TBDs and decision gates

**Safe to carry into Implementation Planning** means the fixed canonical invariant, unresolved choice and affected build decision gate are explicit. It never authorizes an implementation default before that gate. These are seven grouped handoff items, not seven new product decisions.

| Carried V0 TBD group | Must resolve before affected build | Source |
|---|---|---|
| Guest Credential mechanism, delivery/recovery, expiry/revocation and field-level disclosure | Before protected accountless Request/Stay access or related personal data exposure is implemented. Preserve ADR-P077 access invariant meanwhile. | [ADR-P077](../../00-start-here/DECISIONS.md#adr-p077), [B3-T09](../../10-ux-foundation/b3-direct-guest-booking/09-tbd-policy-register.md), [AQ-06](../../03-actor-authority/07-open-authority-questions.md) |
| Request/hold/payment timing, confirmation conditions, UNKNOWN retries and refund/default economics | Before the affected commerce/payment path uses a concrete value or automated consequence. Separate clocks and Money truth remain fixed. | [B3 register](../../10-ux-foundation/b3-direct-guest-booking/09-tbd-policy-register.md), [CP7 open decisions](../../09-database-design/10-open-decisions.md), ADR-P071 |
| Grant/revoke propagation, authority precedence and invitation expiry | Before implementing affected privileged actions or normal-transfer invitation lifecycle; retain action-time checks and ADR-P075 atomic transfer. | [AQ register](../../03-actor-authority/07-open-authority-questions.md), [C2 register](../../10-ux-foundation/c2-host-owner-property-onboarding/21-tbd-policy-register.md) |
| Villa Readiness freshness period and local operational configuration | Before automatic decay or destination timing is activated; retain ADR-P072 states and Host/Butler scope. | [ADR-P072](../../00-start-here/DECISIONS.md#adr-p072), [Oceanami configuration](../../13-destination-operations/oceanami/configuration.md#villa-readiness) |
| Stay Completion automation/timing and unrelated Incident SLA/taxonomy | Before automating those policies; retain ADR-P073's minimum V0 Checkout Assessment and only qualifying damage blocker. | [Completion policy](../../05-state-machines-policies/16-stay-completion-policy.md), [Incident lifecycle](../../05-state-machines-policies/07-incident-lifecycle.md) |
| Exact privacy masking/retention and Owner/Host projections | Before exposing affected financial/Guest fields or setting retention behavior; preserve need-to-know. | [Authority/access policy](../../05-state-machines-policies/20-authority-access-privacy-policy.md), [C2 register](../../10-ux-foundation/c2-host-owner-property-onboarding/21-tbd-policy-register.md) |
| Physical schema/API, temporal/concurrency implementation, provider integration details | Before committing the corresponding implementation design; CP7 is direction, not a frozen table/API contract. | [CP7 persistence README](../../09-database-design/README.md), [open decisions](../../09-database-design/10-open-decisions.md) |

Instant Book is optional/controlled, not a required open gate. Full Affiliate, advanced CRM/PMS/Channel Manager, dynamic pricing, native apps, Managed and External Report persistence are out of V0 or post-V0 under [CP5 exclusions](../../06-v0-scope/07-out-of-scope.md), [ADR-P074](../../00-start-here/DECISIONS.md#adr-p074) and [ADR-P075](../../00-start-here/DECISIONS.md#adr-p075). No current evidence requires a new Founder product decision merely to carry the seven groups into Implementation Planning; any later choice that changes protected semantics still follows governance.

## 7. Protected Baseline verification and residual evidence limits

At this input SHA, CP8-G is [ACCEPTED — READY FOR CP8-H](../README.md#current-disposition), with 19 TESTED — PASS, 1 PARTIAL (row 8), 1 OUT OF SCOPE — V0 (row 13 under ADR-P074), 0 TESTED — FAIL and 0 NOT REPRESENTED. KD-01 and KD-02 are resolved at the prototype SHAs in the [Known Deviations](../README.md#known-deviations) table. The earlier v1 failed validation and G-v2 baseline failures remain historical, not erased by the final checkpoint disposition. The [Protected Baseline](../../AGENTS.md) and CONFIRMED ADRs govern if a prototype snapshot differs.

**G1/G4 independent representative-user validation is a CARRIED VALIDATION ACTION — NON-BLOCKING FOR CP8-H / IMPLEMENTATION PLANNING.** The current record does not establish that evidence; it is neither PASS nor waived. Do not call an affected journey pilot-ready or independently validated by representative actors until that evidence exists. Row 17 does not independently close the historical BQL operational-attention journey gap. Keep these limits in the handoff; do not reopen CP8-G solely to relabel them.

ADR-P074 makes the External Report workflow **OUT OF SCOPE — V0**. The current path is authorized Host direct recording, with Fact ≠ applicable External-backed Commitment even when one action writes both. Earlier `submitExternalReport` evidence is historical only; [row 14's current presentation](../README.md#v2-baseline-coverage--commit-5c39748) and [WF-03](../../04-core-workflows/03-external-booking-to-stay.md) reflect that distinction. No optional [PR #20](https://github.com/stayora-lab/stayora-spec/pull/20) extractor salvage is needed to accept this package.

## 8. Implementation Plan entry checklist

This is the existing [CP8-H → Implementation Planning](../../00-start-here/README.md#cp8-g-and-cp8-h) handoff, not a new checkpoint. Mark each item with review evidence before declaring CP8-H complete or beginning the plan:

- [x] Product Architect / required governance review accepts the CP8-H package; completion is recorded by this reconciliation.
- [x] CP5 V0 classes and explicit non-goals are present, including later ADR-P074–P077 corrections; optional Instant Book is not promoted to MUST BUILD.
- [x] Required journeys, actor/action scope, lifecycle contracts and Protected Baseline references are linked; no unresolved contradiction would force implementers to invent product policy.
- [x] Remaining V0 TBDs and hypotheses are visible with a decision gate before the affected build, without requiring all of them to close before Implementation Planning.
- [x] CP6/CP7/CP8-E/F sources and CP8-G validation limits, including the G1/G4 carried action, are handed off with their provenance.
- [x] The [Public Exposure Review](../../00-start-here/SOURCE_OF_TRUTH.md#public-exposure-review) is completed before Implementation Planning; repository visibility changes follow its recorded outcome.

The existing roadmap now proceeds to **CP8 COMPLETE → Implementation Planning**. This file does not author that plan.
