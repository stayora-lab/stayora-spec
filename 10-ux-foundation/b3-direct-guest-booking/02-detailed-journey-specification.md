# B3 — Detailed Direct Guest Booking Specification

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

Each step is a journey-analysis step, not a screen, database event or new lifecycle state. “Visible outcome” is a contextual projection and does not grant authority.

The records below use compact cells for readability. The completion matrix at the end makes the required fields explicit for every step: information required, information visible to Guest, domain effect, user-visible outcome, other contexts affected, handoff, failure/alternative, policy dependency and TBD/blocker. No cell introduces a database field or screen.

## Phase A — Guest demand / entry

### B3-A01 — Guest enters accommodation discovery

| Field | Specification |
|---|---|
| Actor / Working Context | Guest in Public Marketplace context. |
| User intent | Find accommodation for a destination, range and staying party. |
| Entry condition | Guest has a demand; no Request, Booking, Commitment, Payment or Stay is created by entry. |
| Canonical objects | Guest person/party as available, Destination, Property, Bookable Unit, Listing. |
| Current relevant state | Supply may be searchable; no commercial lifecycle has started. |
| Information required | Enough destination/date/occupancy context to begin discovery; exact minimum remains UX/policy dependent. |
| Information visible to Guest | Public Marketplace truth suitable for discovery. |
| Authority required | Public discovery access; no Booking Authority. |
| Action / domain effect | Browse or search; read/projection only. |
| Inventory effect | None. |
| Outcome / handoff | Guest demand → discovery; no Host responsibility yet. |
| Failure / policy / TBD | No suitable supply remains a discovery outcome; acquisition and marketing funnel are out of scope. |
| Source trace | [CP5 critical journeys](../../06-v0-scope/03-critical-journeys.md), [CP6 public IA](../../07-information-architecture/03-public-and-guest-ia.md), [CP8-A surface model](../03-surface-responsibility.md). |

## Phase B — Discovery

### B3-B01 — Guest evaluates Destination, Property and Unit

| Field | Specification |
|---|---|
| Actor / Working Context | Guest in Public Marketplace. |
| User intent | Understand whether a listed unit fits the intended stay. |
| Entry condition | Candidate supply is searchable and public content is available. |
| Canonical objects | Destination, Property, Bookable Unit, Listing, Verification/quality signals, Public Price/Offer concept. |
| Current relevant state | Searchability and published content; Availability may be unknown until range evaluation. |
| Information required / visible | Unit description, relevant trust signal, public commercial terms and restrictions canonical for Guest view. |
| Authority required | Read access only; visibility is not Hosting or Booking Authority. |
| Action / domain effect | Inspect and compare; no Request or Booking. |
| Inventory effect | None. |
| Outcome / handoff | Guest chooses a candidate → date/occupancy evaluation. |
| Failure / policy / TBD | Missing, stale or private information remains a projection/policy issue; do not fill with internal assumptions. |
| Source trace | [CP2 domain map](../../02-domain/00-domain-map.md), [CP5 marketplace boundaries](../../06-v0-scope/05-domain-boundaries.md), [CP6 public IA](../../07-information-architecture/03-public-and-guest-ia.md). |

## Phase C — Date / occupancy evaluation

### B3-C01 — Guest supplies range and staying-party context

| Field | Specification |
|---|---|
| Actor / Working Context | Guest in Public Marketplace. |
| User intent | Test whether a candidate fits the intended accommodation range and party. |
| Entry condition | Candidate Unit is known; no Request exists. |
| Canonical objects | Bookable Unit, Accommodation Range, Staying Party/occupancy context. |
| Current relevant state | No commitment or Booking; date evaluation is a query/projection. |
| Information required / visible | Range, relevant occupancy information and material restrictions; do not invent capacity rules. |
| Authority required | Public evaluation; no Inventory mutation authority. |
| Action / domain effect | Evaluate candidate dates; no new commitment. |
| Inventory effect | Read derived truth only. |
| Outcome / handoff | Range/party input → Availability evaluation. |
| Failure / policy / TBD | Exact occupancy validation and restrictions remain policy/UX boundaries if not canonical. |
| Source trace | [CP4 Inventory lifecycle](../../05-state-machines-policies/01-inventory-commitment-model.md), [CP7 Inventory model](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md). |

## Phase D — Availability evaluation

### B3-D01 — Guest sees derived Availability and Bookability context

| Field | Specification |
|---|---|
| Actor / Working Context | Guest Marketplace projection backed by canonical Inventory truth. |
| User intent | Know whether the requested range can proceed to a legitimate action. |
| Entry condition | Range and Unit are known. |
| Canonical objects | Inventory Commitments, derived Availability, Searchability, actor/context Bookability. |
| Current relevant state | No Request, Booking or Payment. |
| Information required / visible | Available, unavailable or uncertain status and material next-step conditions. |
| Authority required | Inventory authority remains canonical; Guest has no authority to alter it. |
| Action / domain effect | Read/revalidate as supported; no reservation. |
| Inventory effect | None from viewing. |
| Outcome / handoff | Available and Bookable candidate → Guest choice; otherwise no promise or supported recheck. |
| Failure / policy / TBD | Stale/unknown behavior, conflict display and exact actor-specific eligibility remain open where upstream policy is open. |
| Source trace | [CP8-A language](../05-ux-language-semantics.md), [B3 public mapping](04-public-truth-and-bookability.md), [CP7 invariants](../../08-conceptual-data-model/10-invariants-and-stress-tests.md). |

## Phase E — Guest choice / intent

### B3-E01 — Guest chooses to request the Unit

| Field | Specification |
|---|---|
| Actor / Working Context | Guest in Public Marketplace. |
| User intent | Ask the responsible Host/Booking Authority to decide whether accommodation can proceed. |
| Entry condition | Guest has evaluated material public information and chooses to continue. |
| Canonical objects | Guest person/party, Unit, range, conceptual Offer/terms and future Booking Request. |
| Current relevant state | No Request yet; no Inventory Commitment, Payment or Booking. |
| Information required / visible | Request minimum, staying-party information, material terms and consent basis; no mandatory account implied. |
| Authority required | Guest can express intent/participation; Guest cannot accept for the Host. |
| Action / domain effect | Proceed to Request creation; intent alone does not create an object. |
| Inventory effect | None. |
| Outcome / handoff | Guest intent → Request creation. |
| Failure / policy / TBD | Abandonment or incomplete information stops the path; exact minimum and consent remain policy/UX TBD. |
| Source trace | [CP5 direct journey](../../06-v0-scope/03-critical-journeys.md), [CP3 actor catalog](../../03-actor-authority/01-actor-catalog.md), [CP7 party model](../../08-conceptual-data-model/06-money-payment-settlement-payout.md). |

## Phase F — Booking Request creation

### B3-F01 — Guest creates a Booking Request

| Field | Specification |
|---|---|
| Actor / Working Context | Guest, or an explicitly supported representative acting for the Guest context; no Sale is required. |
| User intent | Submit a truthful request for authorized Host decision. |
| Entry condition | Required Request information and consent/participation basis are present; no confirmation yet. |
| Canonical objects | Booking Request, Guest/Staying Party relationship, Unit, range, Offer/terms, source/provenance. |
| Current relevant state | Request is `PENDING`; no Booking; Request does not reserve Inventory. |
| Information required / visible | Unit/range, Guest/party information required by policy, material terms, source and acting context. |
| Authority required | Request-creation capability; no Booking Authority is needed to submit, but Host authority is needed to decide. |
| Action / domain effect | Create and submit Request. |
| Inventory effect | None; existing commitments continue to determine derived Availability. |
| Outcome / handoff | Guest sees pending decision; Host/authorized Booking Authority receives responsibility. |
| Failure / policy / TBD | Missing/invalid information or capability prevents a misleading Request; no automatic Sale attribution, reassignment or reservation. |
| Source trace | [CP3 capabilities](../../03-actor-authority/02-authority-capabilities.md), [CP4 Request lifecycle](../../05-state-machines-policies/02-booking-request-and-booking.md), [CP8-A object model](../04-cross-context-objects.md). |

## Phase G — Host / Booking Authority decision

### B3-G01 — Authorized Host reviews Request

| Field | Specification |
|---|---|
| Actor / Working Context | Host/Primary Host or Co-host under explicit delegated Booking Authority. |
| User intent | Decide whether the direct Guest request can proceed. |
| Entry condition | Request `PENDING`; authority, resource scope, terms and current context can be evaluated. |
| Canonical objects | Request, Unit, Offer/terms, Availability, Inventory Commitments, authority grant. |
| Current relevant state | Request pending; Availability may have changed; no Booking. |
| Information required / visible | Request terms, current Inventory context, Guest/party data needed for decision and authority basis. |
| Authority required | Booking Authority for relevant resource/time scope. Guest visibility, Sale capacity, Butler assignment or whitelist is insufficient. |
| Action / domain effect | Accept or reject when authorized. |
| Inventory effect | Acceptance may trigger final revalidation; Request itself remains non-reserving. |
| Outcome / handoff | Authorized decision → Request outcome and next Inventory/payment step. |
| Failure / policy / TBD | Missing authority, unanswered Request and late conflict remain explicit exceptions; no SLA/reassignment invented. |
| Source trace | [CP3 authority model](../../03-actor-authority/00-authority-model.md), [CP4 booking policy](../../05-state-machines-policies/12-booking-and-commitment-policy.md), [CP5 capability matrix](../../06-v0-scope/04-capability-matrix.md). |

### B3-G02 — Request is accepted or rejected

| Field | Specification |
|---|---|
| Actor / Working Context | Authorized Host/Co-host context. |
| User intent | Permit progression or close the requested path. |
| Entry condition | Valid decision authority and `PENDING` Request. |
| Canonical objects | Request, terms, authority evidence. |
| Current relevant state | `PENDING`. |
| Information required / visible | Decision and material next condition subject to notification policy. |
| Authority required | Booking Authority. |
| Action / domain effect | Request → `ACCEPTED` or `REJECTED`; acceptance authorizes progression, not Booking confirmation. |
| Inventory effect | Revalidation may be required; rejection creates no commitment. |
| Outcome / handoff | Accepted → Inventory/payment progression; rejected → Guest alternate discovery/closure. |
| Failure / policy / TBD | Exact unanswered/timeout, reason and conflict handling remain open. |
| Source trace | [CP4 Request and Booking](../../05-state-machines-policies/02-booking-request-and-booking.md), [CP3 Booking Authority](../../03-actor-authority/02-authority-capabilities.md). |

## Phase H — Inventory revalidation / commitment

### B3-H01 — Revalidate and establish applicable commitment

| Field | Specification |
|---|---|
| Actor / Working Context | Inventory/Booking orchestration under authorized Host decision. |
| User intent | Protect the accommodation opportunity only for a finite policy-supported period. |
| Entry condition | Request `ACCEPTED`; authority and relevant exclusivity remain valid. |
| Canonical objects | Unit × Time, existing Inventory Commitments, Request, Temporary Exclusive Commitment where supported. |
| Current relevant state | Request accepted; no Booking until confirmation conditions pass. |
| Information required / visible | Effective commitments, range, authority and applicable terms. |
| Authority required | Inventory/Booking authority as established by upstream architecture; Guest cannot create a commitment. |
| Action / domain effect | Final revalidation and, where supported, establish finite Temporary Exclusive Commitment. |
| Inventory effect | Derived Availability recomputes; Request remains a separate object. |
| Outcome / handoff | Commitment/condition → Required Payment Condition. |
| Failure / policy / TBD | Conflict, expiry and exact duration remain policy boundaries; no winner or duration invented. |
| Source trace | [CP4 Inventory](../../05-state-machines-policies/01-inventory-commitment-model.md), [CP4 cross-workflow invariants](../../04-core-workflows/07-cross-workflow-invariants.md), [CP7 inventory model](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md). |

## Phase I — Required Payment Condition

### B3-I01 — Evaluate the action-specific payment condition

| Field | Specification |
|---|---|
| Actor / Working Context | Guest/Payer payment context and Money/Booking evaluation. |
| User intent | Fulfil the payment condition required for the next commercial action where applicable. |
| Entry condition | Request accepted and applicable commitment/terms known. |
| Canonical objects | Required Payment Condition, Payment Obligation, Payment Attempt, Guest/Payer, Booking Confirmation Conditions. |
| Current relevant state | No Booking confirmation yet; Payment Attempt may be `INITIATED`, `PROCESSING`, `SUCCEEDED`, `FAILED` or `UNKNOWN`. |
| Information required / visible | Specific condition, amount/terms where canonical, payment status and next action. |
| Authority required | Payer supplies payment; Booking/Payment policies evaluate satisfaction. Guest identity and payer may differ. |
| Action / domain effect | Initiate/observe a Payment Attempt and evaluate the specific condition. |
| Inventory effect | Any commitment remains subject to its own policy and expiry; payment alone does not confirm Booking. |
| Outcome / handoff | Satisfied condition plus all other conditions → confirmation evaluation. |
| Failure / policy / TBD | Do not invent percentage, deadline, grace, default, refund, retry or provider behavior; `UNKNOWN` is unresolved, not silently failed/defaulted. |
| Source trace | [CP4 Payment lifecycle](../../05-state-machines-policies/03-payment-lifecycle.md), [CP4 Booking policy](../../05-state-machines-policies/12-booking-and-commitment-policy.md), [CP7 Money model](../../08-conceptual-data-model/06-money-payment-settlement-payout.md). |

## Phase J — Confirmation

### B3-J01 — Evaluate Booking Confirmation Conditions

| Field | Specification |
|---|---|
| Actor / Working Context | Booking confirmation evaluation using canonical authority, Inventory and Money truth. |
| User intent | Determine whether accommodation can truthfully become a Booking. |
| Entry condition | Accepted Request and all available condition evidence. |
| Canonical objects | Request, valid Offer/terms, authority, exclusive Inventory Commitment, Required Payment Condition, Payment Attempt/outcome, consent/compliance evidence. |
| Current relevant state | No pre-confirmation Booking exists. |
| Information required / visible | Guest sees only a truthful progressing or blocked outcome; internal evidence remains scoped. |
| Authority required | Booking confirmation follows canonical Booking authority/policy evaluation; Guest cannot self-confirm. |
| Action / domain effect | If all conditions pass, create Booking at `CONFIRMED`; otherwise preserve Request/payment/exception truth. |
| Inventory effect | Confirmed Accommodation Commitment/Booking effect applies only when canonical confirmation occurs. |
| Outcome / handoff | Booking `CONFIRMED` → Guest confirmation and Stay Access preparation. |
| Failure / policy / TBD | Payment success alone, Guest intent or acceptance alone cannot bypass conditions. No pre-confirmation Booking or false confirmation. |
| Source trace | [CP4 Booking lifecycle](../../05-state-machines-policies/02-booking-request-and-booking.md), [CP7 aggregate principles](../../08-conceptual-data-model/09-aggregate-and-projection-map.md). |

## Phase K — Guest confirmation / Stay Access

### B3-K01 — Provide confirmation and scoped Stay Access where eligible

| Field | Specification |
|---|---|
| Actor / Working Context | Guest confirmation and Guest Stay Access contexts. |
| User intent | Know that accommodation is confirmed and access relevant information where eligible. |
| Entry condition | Booking `CONFIRMED` and applicable Stay/access relationship exists. |
| Canonical objects | Booking, confirmed accommodation, Stay where represented, Guest/Staying Party, scoped Access concept. |
| Current relevant state | Booking confirmed; Stay may be scheduled/not started according to its own lifecycle. |
| Information required / visible | Confirmation, material accommodation truth and need-to-know access/arrival information. |
| Authority required | Guest relationship and access policy; access link/QR/token, if later used, is not underlying authority. |
| Action / domain effect | Read confirmation/access projection; no new commercial commitment from viewing. |
| Inventory effect | None. |
| Outcome / handoff | Guest confirmation → operations preparation. |
| Failure / policy / TBD | No account, authentication, QR, token or privacy design is selected here; exact eligibility and credential lifecycle remain open. |
| Source trace | [CP6 Guest Access](../../07-information-architecture/03-public-and-guest-ia.md), [CP8-A language](../05-ux-language-semantics.md), [CP7 Stay](../../08-conceptual-data-model/05-stay-and-operations.md). |

## Phase L — Operations handoff

### B3-L01 — Confirmed accommodation becomes operationally relevant

| Field | Specification |
|---|---|
| Actor / Working Context | Host, assigned Butler, Destination/BQL and Admin only within their scoped contexts. |
| User intent | Prepare and support the confirmed accommodation. |
| Entry condition | Booking confirmed and operational Stay representation/assignment is supported. |
| Canonical objects | Booking, Stay, Arrival, Access, Staying Party, Destination, Incident/Issue where applicable. |
| Current relevant state | Booking `CONFIRMED`; Stay remains on its own lifecycle. |
| Information required / visible | Need-to-know dates, party/access and operational requirements; not unnecessary economics or internal conflict. |
| Authority required | Operational assignment/function/destination scope; no commercial authority is created by handoff or visibility. |
| Action / domain effect | Project confirmed accommodation into operational contexts. |
| Inventory effect | None unless a separately authorized Inventory action occurs. |
| Outcome / handoff | Operations prepares; Guest receives support; commercial origin remains direct Stayora commerce. |
| Failure / policy / TBD | Stay operations, Incident consequences and access details belong to later work; do not start B4 here. |
| Source trace | [CP3 actor-resource matrix](../../03-actor-authority/03-actor-resource-matrix.md), [CP4 Stay lifecycle](../../05-state-machines-policies/04-stay-lifecycle.md), [CP6 Operations](../../07-information-architecture/06-operations-workspaces.md). |

## Cross-step field completion

| Step | Information required | Information visible to Guest | Domain effect | User-visible outcome | Other contexts affected | Handoff | Failure / alternative | Policy dependency | TBD / blocker |
|---|---|---|---|---|---|---|---|---|---|
| B3-A01 | Destination/range/occupancy context as available. | Public discovery truth. | None. | Candidate discovery begins. | Public Marketplace only. | Demand → discovery. | No suitable supply; remain in discovery. | Public discovery eligibility. | Acquisition funnel and exact minimum context. |
| B3-B01 | Unit content, public terms, trust signals. | Published content and eligible public signals. | Read projection only. | Guest can compare candidates. | Listing/Verification projections. | Discovery → date evaluation. | Missing/stale/private truth. | Public disclosure and trust-display policy. | Exact ranking/field minimum. |
| B3-C01 | Range and relevant staying-party context. | Material restrictions/fit where canonical. | Query only; no commitment. | Guest can test fit. | Inventory read model. | Date evaluation → Availability. | Occupancy/range invalid or unsupported. | Capacity and restriction policy. | Exact occupancy rules. |
| B3-D01 | Effective commitments and context eligibility. | Available/unavailable/uncertain and next supported action. | No mutation from viewing. | Guest understands whether to proceed. | Inventory/Marketplace projection. | Availability → Guest intent or stop. | Stale, conflict or not Bookable. | Revalidation and actor eligibility. | Thresholds and disclosure. |
| B3-E01 | Request minimum, terms and consent basis. | Next step is a Request, not confirmation. | No object or commitment yet. | Guest chooses whether to request. | None until Request. | Intent → Request creation. | Abandonment/incomplete data. | Consent and required-data policy. | Exact minimum and representation. |
| B3-F01 | Unit, range, party, terms, source and consent/provenance. | `PENDING` Request and truthful status. | Request created; no Booking/hold. | Guest knows Host decision is pending. | Host authority context; no operations. | Guest → Host/Booking Authority. | Invalid capability/data; stop or correct. | Request creation, privacy and notification. | Accountless continuity and exact fields. |
| B3-G01 | Request, current Inventory context, authority evidence. | Pending/accepted/rejected projection where allowed. | Decision evaluation only. | Host responsibility is understood. | Inventory may be revalidated. | Request → authorized decision. | Missing/revoked authority, unanswered. | Authority resolution and notification. | SLA, reassignment and precedence. |
| B3-G02 | Decision, terms and authority evidence. | Accepted progression or rejection. | Request outcome only. | Guest knows whether path continues. | Inventory/Money may become relevant after acceptance. | Decision → Inventory/payment or closure. | Conflict, invalid authority or rejection. | Request lifecycle and conflict policy. | Reasons, timeout and appeal. |
| B3-H01 | Unit × Time, commitments, authority and terms. | Progressing/blocked outcome; no false hold promise. | Possible finite Temporary Commitment. | Guest knows whether payment condition can follow. | Inventory and Booking orchestration. | Acceptance → commitment/payment. | Conflict, expiry or no exclusivity. | Commitment, conflict and expiry policy. | Duration and release rule. |
| B3-I01 | Specific condition, payer, terms and attempt state. | Action-specific amount/status/next step where canonical. | Payment Obligation/Attempt state; not Booking. | Guest/Payer knows payment outcome. | Money/provider reconciliation. | Payment condition → confirmation evaluation. | Failed/unknown/other condition unmet. | Payment, refund, default and provider policy. | Economics, grace, retry and reconciliation. |
| B3-J01 | Terms, authority, exclusive Inventory, payment and consent evidence. | Confirmed or blocked truth. | Booking created only at `CONFIRMED`. | Guest receives truthful confirmation or no confirmation. | Inventory, Money, Host and later Stay. | Conditions → Booking/access. | Any condition fails; preserve separate truth. | Booking confirmation policy. | Exceptions and remediation. |
| B3-K01 | Confirmed Booking, Guest/Staying Party and access eligibility. | Confirmation and need-to-know access information. | Access projection only. | Guest can prepare/use eligible Stay. | Stay/Operations projections. | Booking → Guest access/operations. | Missing access/auth/privacy basis. | Access, authentication and privacy policy. | Credential lifecycle and recovery. |
| B3-L01 | Confirmed accommodation, Stay basis, assignment and operational data. | Relevant confirmation/support only. | Operational projection; no commercial mutation. | Operations can prepare/support. | Host, Butler, BQL, Incident/Stay contexts. | Booking/Stay → Operations. | Missing assignment/data or issue. | Operations, destination and incident policy. | B4 lifecycle and access details. |
