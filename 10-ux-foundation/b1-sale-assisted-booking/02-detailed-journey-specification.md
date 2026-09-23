# B1 — Detailed Sale-Assisted Booking Specification

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

Each step below is a UX journey reasoning step, not a database event, screen or new lifecycle transition. “Visible outcome” means what the responsible context may understand; it is not final copy.

## Phase A — Demand / Guest Need

### B1-A01 — Guest need reaches Sale

| Field | Specification |
|---|---|
| Actor / Working Context | Guest, communicating with an eligible Sale Context; communication may remain external such as Zalo where CP6 allows. |
| User intent | Find suitable Oceanami accommodation for a real need. |
| Entry condition | Guest has a need; no Stayora Booking or Inventory Commitment exists from this step. |
| Canonical objects | Guest/Identity relationship, Sale relationship, destination/property discovery context; Lead only if an existing Lead workflow applies. |
| Current relevant state | No Booking Request yet; Lead state/assignment only if already represented. |
| Information required | Minimum dates, destination/supply fit, party/operational information needed to search; do not create a CRM schema. |
| Authority required | Sale platform eligibility and relevant Sale–Host Distribution Relationship for supply discovery; no Booking Authority. |
| Action | Sale understands and qualifies the demand sufficiently to search. |
| Domain effect | None on Inventory, Booking or Payment. A Lead/Assignment is not silently created. |
| User-visible outcome | Guest understands that Sale is helping find an option; Sale has a scoped demand context. |
| Other contexts affected | None yet; Host is not responsible for a Request until one exists. |
| Handoff | Guest need → Sale discovery. |
| Failure / alternative | No suitable understanding or no eligible Sale: remain outside the Booking path or use an existing lead/assignment path. Exact lead handling is TBD. |
| Policy dependency | Distribution relationship, lead policy and privacy/minimum data policy. |
| TBD / blocker | Whether a particular communication becomes a Lead and exact information minimum. |
| Source trace | [CP5 pilot actors](../../06-v0-scope/02-pilot-actors.md), [CP6 Sale Workspace](../../07-information-architecture/05-sale-workspace.md), [CP4 Lead](../../05-state-machines-policies/08-lead-and-distribution-lifecycle.md). |

## Phase B — Discovery

### B1-B01 — Sale searches supply

| Field | Specification |
|---|---|
| Actor / Working Context | Sale Context. |
| User intent | Find Property / Bookable Unit options that fit the Guest need. |
| Entry condition | Demand context is sufficient to search; Sale is eligible for the relevant scope. |
| Canonical objects | Destination, Property, Bookable Unit, Listing, derived Availability, Public Price, Trust/Verification signals. |
| Current relevant state | Supply may be searchable/listed; Availability is derived from effective Inventory Commitments. |
| Information required | Destination, dates, fit/capacity and relevant trust signals; Public Price in the applicable Offer context. |
| Authority required | Sale discovery capability from platform eligibility + relevant relationship/transaction context; no Inventory Authority. |
| Action | Search and compare suitable supply. |
| Domain effect | Read/projection only; no Request, Commitment, Booking or Payment. |
| User-visible outcome | Sale can distinguish options that are visible/searchable from those with relevant Availability information. |
| Other contexts affected | Host truth is read; no Host action is created. |
| Handoff | Sale discovery → availability evaluation / option preparation. |
| Failure / alternative | No suitable supply: report no match or continue discovery; do not invent a Reservation or force a Host Request. |
| Policy dependency | Marketplace eligibility, One Public Price, Distribution Relationship and discovery policy. |
| TBD / blocker | Search ranking, exact stale-data signaling and detailed fit fields remain open. |
| Source trace | [CP2 domain map](../../02-domain/00-domain-map.md), [CP5 capability matrix](../../06-v0-scope/04-capability-matrix.md), [CP6 Sale Workspace](../../07-information-architecture/05-sale-workspace.md). |

### B1-B02 — Sale evaluates actor-specific Bookability

| Field | Specification |
|---|---|
| Actor / Working Context | Sale Context. |
| User intent | Avoid presenting an option as actionable when it is only searchable or visible. |
| Entry condition | Candidate supply and dates are known. |
| Canonical objects | Derived Availability, Inventory Commitments, Property/Bookable Unit, Sale eligibility/relationship. |
| Current relevant state | Availability projection; no Request/Booking yet. |
| Information required | Effective availability for the dates, source/provenance where material, Sale relationship and transaction context. |
| Authority required | Sale demand access; Inventory Authority remains with Host/authorized actor or explicit granted capability. |
| Action | Assess whether the Sale may responsibly discuss/request the option. |
| Domain effect | None; Sale cannot create a hold by viewing or discussing. |
| User-visible outcome | Sale sees a qualified option or an explicit reason it is not currently actionable. |
| Other contexts affected | Host/Inventory truth is not modified. |
| Handoff | Availability evaluation → option/Offer presentation. |
| Failure / alternative | Availability changed, conflict or unknown: surface uncertainty and recheck; do not select a channel winner or silently promise the dates. |
| Policy dependency | Inventory commitment/conflict policy and actor-specific transaction eligibility. |
| TBD / blocker | Exact conflict, stale/sync and unknown interaction policy. |
| Source trace | [CP4 Inventory Commitment](../../05-state-machines-policies/01-inventory-commitment-model.md), [CP7 Inventory model](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md), [CP8-A language](../05-ux-language-semantics.md). |

## Phase C — Option / Guest Choice

### B1-C01 — Sale prepares and shares an option

| Field | Specification |
|---|---|
| Actor / Working Context | Sale Context. |
| User intent | Help the Guest understand a suitable option and its material terms. |
| Entry condition | Sale has a candidate with relevant Availability/Bookability information. |
| Canonical objects | Conceptual Offer, Property/Bookable Unit, Public Price, dates, conditions and trust signals. |
| Current relevant state | Offer is a conceptual proposition; no Booking Request or Inventory Commitment. |
| Information required | Public Price, date/resource fit, material conditions and provenance/trust information needed for Guest decision. |
| Authority required | Sale may compose/present an Offer within eligible distribution context; no Host acceptance authority. |
| Action | Share or discuss the option. |
| Domain effect | Presentation only; no inventory reservation and no Booking. |
| User-visible outcome | Guest can choose whether to proceed with this option. |
| Other contexts affected | No Host or Operations responsibility yet. |
| Handoff | Sale option → Guest intent to proceed. |
| Failure / alternative | Guest declines or option changes: no Booking Request is created; Sale may continue discovery. |
| Policy dependency | Offer/terms, One Public Price, discount/funding and disclosure policies. |
| TBD / blocker | Offer ownership/lifecycle and discount limits/funding remain open. |
| Source trace | [CP2 Offer glossary](../../02-domain/01-domain-glossary.md), [CP4 booking policy](../../05-state-machines-policies/12-booking-and-commitment-policy.md), [CP5 critical journey](../../06-v0-scope/03-critical-journeys.md). |

### B1-C02 — Guest confirms intent to request

| Field | Specification |
|---|---|
| Actor / Working Context | Guest intent mediated by Sale Context. |
| User intent | Ask the Host/authorized actor to decide whether the option can proceed. |
| Entry condition | Guest agrees to proceed on the option's known material terms. |
| Canonical objects | Guest relationship/party data, conceptual Offer/terms and future Booking Request. |
| Current relevant state | No Booking Request until the Sale creates it; no Inventory Commitment. |
| Information required | Guest/staying-party information required for Request and later operations, material terms and consent basis. Payer, creator, lead guest and staying party remain distinct. |
| Authority required | Guest supplies consent/participation; Sale needs valid Request-creation capability. Neither has Host acceptance authority. |
| Action | Confirm intent to Sale and authorize creation of a Request on the Guest's behalf where supported. |
| Domain effect | Enables Request creation; does not itself create Request, Commitment, Payment or Booking until the next authorized action. |
| User-visible outcome | Guest understands the next step is Host/authorized decision, not confirmed accommodation. |
| Other contexts affected | Sale becomes accountable for creating a truthful Request if it proceeds. |
| Handoff | Guest intent → Sale creates Request. |
| Failure / alternative | Guest abandons or material terms cannot be confirmed: stop without inventing a Request/Booking. |
| Policy dependency | Consent, required Guest data, privacy and Offer/terms policy. |
| TBD / blocker | Exact consent/participant and communication behavior. |
| Source trace | [CP3 actor boundaries](../../03-actor-authority/01-actor-catalog.md), [CP7 Money/parties](../../08-conceptual-data-model/06-money-payment-settlement-payout.md), [CP8-A actor model](../02-actor-context-responsibility.md). |

## Phase D — Booking Request Creation

### B1-D01 — Sale creates Booking Request

| Field | Specification |
|---|---|
| Actor / Working Context | Sale Context, acting for the Guest demand context. |
| User intent | Submit a truthful request for Host/authorized decision. |
| Entry condition | Relevant option/terms and Guest intent exist; Sale is eligible and transaction context is valid. |
| Canonical objects | Booking Request, Guest/Staying Party relationship, Property, Bookable Unit, dates, conceptual Offer/terms, Sale attribution. |
| Current relevant state | Request is created as `PENDING`; no Booking exists; Request does not reserve Inventory. |
| Information required | Resource/dates, Guest/party identity as required, material terms, source/acting Sale context, provenance and any required evidence. |
| Authority required | Sale capability to create Request under platform eligibility + Sale–Host relationship + transaction context. No Booking Authority needed to create the Request. |
| Action | Create and submit Booking Request. |
| Domain effect | Booking domain records commercial intent awaiting authorized decision. Inventory remains derived from existing commitments. |
| User-visible outcome | Guest and Sale can see a Request awaiting Host/authorized decision; neither sees a confirmed Booking. |
| Other contexts affected | Host/authorized Booking Authority receives responsibility; Admin may receive notification/exception only where canonical workflow requires. |
| Handoff | Sale → Host/authorized Booking Authority. |
| Failure / alternative | Missing authority/eligibility or incomplete information: do not create a misleading Request; return for correction or stop. |
| Policy dependency | Request creation, required data, Distribution Relationship and privacy policy. |
| TBD / blocker | Exact field minimum, notification timing and lead/request linkage. |
| Source trace | [CP3 capabilities](../../03-actor-authority/02-authority-capabilities.md), [CP4 Request lifecycle](../../05-state-machines-policies/02-booking-request-and-booking.md), [CP7 Booking Request](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md). |

### B1-D02 — Host responsibility is notified / located

| Field | Specification |
|---|---|
| Actor / Working Context | Host / Primary Host or valid delegated Booking Authority context becomes the action owner. |
| User intent | Understand that a Request requires a decision within the authorized Property scope. |
| Entry condition | Request is `PENDING` and linked to a resource for which an authority context can be resolved. |
| Canonical objects | Booking Request, Property/Bookable Unit, authority relationship/delegation and resource scope. |
| Current relevant state | Request `PENDING`; no reservation/Booking. |
| Information required | Request terms, dates, relevant availability/commitment context, Guest information needed for decision and authority basis. |
| Authority required | Host/Primary Host or delegated Booking Authority; Sale role alone is insufficient. |
| Action | Receive/locate the Request for decision. |
| Domain effect | Responsibility handoff only; no acceptance yet. |
| User-visible outcome | Host sees a decision-required Request; Sale/Guest see pending responsibility, subject to notification policy. |
| Other contexts affected | Sale and Guest remain observers of Request progress; Inventory is still unchanged. |
| Handoff | Request creation → Host decision. |
| Failure / alternative | Authority cannot be resolved: surface missing-authority exception; do not auto-accept, auto-reject or reassign without policy. |
| Policy dependency | Authority resolution, notification and assignment policy. |
| TBD / blocker | Exact no-authority and unanswered-request handling. |
| Source trace | [CP3 authority model](../../03-actor-authority/00-authority-model.md), [CP6 Host Workspace](../../07-information-architecture/04-host-workspace.md), [CP8-A handoff principles](../01-ux-principles.md). |

## Phase E — Host Decision

### B1-E01 — Authorized Host reviews Request

| Field | Specification |
|---|---|
| Actor / Working Context | Primary Host or Co-host acting under explicit delegated Booking Authority. |
| User intent | Decide whether the commercial request can proceed. |
| Entry condition | Request `PENDING`; actor has valid capability, resource scope, lifecycle and policy context. |
| Canonical objects | Booking Request, Offer/terms, Property/Unit, derived Availability, Inventory Commitments, authority grant. |
| Current relevant state | Request `PENDING`; Availability may have changed; no Booking. |
| Information required | Request/terms, current effective commitment view, relevant Guest/party information and policy conditions. |
| Authority required | Booking Authority on the relevant Property/Unit; Sale capacity alone cannot perform this action. |
| Action | Review and choose accept or reject. |
| Domain effect | A valid decision can move Request to `ACCEPTED` or `REJECTED`; acceptance authorizes proceeding but is not Booking confirmation. |
| User-visible outcome | Host sees the decision recorded; Sale/Guest see accepted/rejected status when visibility policy permits. |
| Other contexts affected | Inventory may need revalidation; Money conditions may become relevant only after accepted authorization. |
| Handoff | Host decision → commitment/payment conditions or Request closure. |
| Failure / alternative | Authority revoked/invalid or availability conflict: no unauthorized decision; route to exception/TBD handling. |
| Policy dependency | Booking/commitment conditions, authority lifecycle, conflict policy. |
| TBD / blocker | Precedence among multiple valid authorities and late conflict resolution. |
| Source trace | [CP3 Booking Authority](../../03-actor-authority/02-authority-capabilities.md), [CP4 Booking policy](../../05-state-machines-policies/12-booking-and-commitment-policy.md), [CP4 Request lifecycle](../../05-state-machines-policies/02-booking-request-and-booking.md). |

### B1-E02 — Request is rejected

| Field | Specification |
|---|---|
| Actor / Working Context | Host / authorized Booking Authority. |
| User intent | Decline the requested commercial path. |
| Entry condition | Request `PENDING`; rejection is authorized. |
| Canonical objects | Booking Request and any linked conceptual Offer/terms. |
| Current relevant state | Request `PENDING`; no Booking or Commitment created by the rejection. |
| Information required | Request identity, authority and reason where policy requires. |
| Authority required | Booking Authority. |
| Action | Reject Request. |
| Domain effect | Request → `REJECTED`; no Booking, no Temporary Commitment and no payment requirement created by this step. |
| User-visible outcome | Guest/Sale learn that this request will not proceed, subject to notification policy. |
| Other contexts affected | No Stay/Butler/BQL responsibility begins. |
| Handoff | Host decision → Sale/Guest communication or alternate discovery. |
| Failure / alternative | If no valid authority, do not record rejection as Host decision; escalate missing-authority path. |
| Policy dependency | Rejection reason/notification policy. |
| TBD / blocker | Exact message, appeal or alternate-supply behavior. |
| Source trace | [CP4 Request lifecycle](../../05-state-machines-policies/02-booking-request-and-booking.md), [CP6 cross-surface navigation](../../07-information-architecture/08-cross-surface-navigation.md). |

### B1-E03 — Request is accepted for progression

| Field | Specification |
|---|---|
| Actor / Working Context | Host / authorized Co-host acting under Booking Authority. |
| User intent | Allow the request to proceed toward a commercial accommodation commitment. |
| Entry condition | Request `PENDING`; valid authority and relevant terms exist. |
| Canonical objects | Booking Request, Offer/terms, Inventory Commitment, Payment Obligation/Attempt and Required Payment Condition. |
| Current relevant state | Request `PENDING`; no Booking. |
| Information required | Accepted terms, current effective Inventory state, required payment condition and consent/evidence requirements. |
| Authority required | Booking Authority plus any required Inventory authority/policy evaluation. |
| Action | Accept Request. |
| Domain effect | Request → `ACCEPTED`; acceptance authorizes subsequent commitment/payment orchestration. It is not `Booking CONFIRMED`. |
| User-visible outcome | Guest/Sale see accepted/proceeding status and required next condition when policy permits; Host sees next responsibility. |
| Other contexts affected | Inventory may create a finite Temporary Exclusive Commitment where canonical policy allows; Money may create/evaluate an obligation/attempt. |
| Handoff | Host acceptance → Inventory/payment progression. |
| Failure / alternative | Inventory no longer exclusive, authority invalid, terms changed or required conditions unavailable: do not confirm Booking; preserve Request/exception truth. |
| Policy dependency | Commitment window, Required Payment Condition, Booking Confirmation Conditions and conflict policy. |
| TBD / blocker | Exact acceptance-to-commitment timing and expiry behavior. |
| Source trace | [CP3 cross-workflow invariants](../../04-core-workflows/07-cross-workflow-invariants.md), [CP4 booking policy](../../05-state-machines-policies/12-booking-and-commitment-policy.md), [CP7 aggregate map](../../08-conceptual-data-model/09-aggregate-and-projection-map.md). |

## Phase F — Inventory Commitment

### B1-F01 — Revalidate and establish applicable commitment

| Field | Specification |
|---|---|
| Actor / Working Context | Inventory/Booking orchestration under the authorized Host decision; not a Sale-created reservation. |
| User intent | Protect the accommodation opportunity only for the finite period and scope supported by policy. |
| Entry condition | Request `ACCEPTED`; valid authority and relevant exclusivity remain available. |
| Canonical objects | Inventory Commitment, Bookable Unit × Time, Request, Offer/terms. |
| Current relevant state | Availability derived from effective commitments; Request accepted. |
| Information required | Unit/date range, existing effective commitments, authority basis, expiry/conditions where defined. |
| Authority required | Inventory Authority or orchestration using an authorized decision; Sale role alone cannot create it. |
| Action | Revalidate and, where supported, create Temporary Exclusive Inventory Commitment. |
| Domain effect | A finite Inventory Commitment may exist; Request remains a separate lifecycle; no Booking yet. |
| User-visible outcome | Guest/Sale may see that progression has a finite commitment/payment condition, not a confirmed Booking. |
| Other contexts affected | Host sees protected progression; Inventory projections change; Admin may see conflict/exception if applicable. |
| Handoff | Temporary commitment → Required Payment Condition/payment. |
| Failure / alternative | Existing incompatible commitment or conflict: preserve both truth/evidence and surface conflict; do not choose a winner automatically. |
| Policy dependency | Temporary commitment window, exclusivity, expiry/release and conflict policy. |
| TBD / blocker | Exact duration, conflict resolution and late-discovery behavior. |
| Source trace | [CP4 Inventory Commitment](../../05-state-machines-policies/01-inventory-commitment-model.md), [CP2 invariants](../../02-domain/03-domain-invariants.md), [CP5 critical journey](../../06-v0-scope/03-critical-journeys.md). |

## Phase G — Payment Requirement

### B1-G01 — Present Required Payment Condition

| Field | Specification |
|---|---|
| Actor / Working Context | Guest/Payer-facing payment context coordinated by Sale/Host/Stayora as applicable. |
| User intent | Understand what payment condition must be satisfied for Booking Confirmation. |
| Entry condition | Request accepted and applicable commercial terms/commitment path exists. |
| Canonical objects | Required Payment Condition, Payment Obligation, Commercial Snapshot/Offer terms, Payment Session/Attempt. |
| Current relevant state | Request `ACCEPTED`; Booking not confirmed; Temporary Commitment may exist. |
| Information required | Total/accepted terms, specific condition, amount due and deadline only where canonical policy provides them. |
| Authority required | Money/Booking policy execution and explicit Guest/Payer consent; Sale does not own payment ledger. |
| Action | Disclose and obtain required payment action/consent. |
| Domain effect | Evaluates whether a specific commercial action may proceed; it does not represent all future obligations. |
| User-visible outcome | Guest/Payer knows what is required for confirmation; Sale/Host can monitor scoped progress. |
| Other contexts affected | Money records an Obligation/Attempt; Inventory commitment may remain finite while condition is pending. |
| Handoff | Required condition → payment attempt/outcome. |
| Failure / alternative | Condition not initiated or terms no longer valid: do not confirm Booking; exact expiry/default path remains policy boundary. |
| Policy dependency | Payment schedule, Required Payment Condition, disclosures and transaction snapshot. |
| TBD / blocker | Exact percentages, deadline, grace, default, cancellation/refund and provider behavior. |
| Source trace | [Foundation Money](../../01-product-foundation/09-money-model.md), [CP4 Payment](../../05-state-machines-policies/03-payment-lifecycle.md), [CP5 Oceanami policy](../../01-product-foundation/10-oceanami-pilot.md). |

### B1-G02 — Payment Attempt progresses

| Field | Specification |
|---|---|
| Actor / Working Context | Payer/Guest payment interaction; Money/Stayora system records Attempt outcome. |
| User intent | Satisfy the applicable payment condition. |
| Entry condition | A Payment Obligation/condition is presented and an attempt is initiated. |
| Canonical objects | Payment Obligation, Payment Session/Attempt, provider transaction where represented. |
| Current relevant state | Attempt `INITIATED` or `PROCESSING`; Booking not confirmed. |
| Information required | Amount/condition, transaction context and consent; provider details only as needed. |
| Authority required | Payer/payment authority and Money execution; Sale/Host may assist but do not rewrite ledger. |
| Action | Initiate/complete an attempt or await reconciliation. |
| Domain effect | Attempt may become `SUCCEEDED`, `FAILED` or `UNKNOWN`; obligation satisfaction remains a separate evaluation. |
| User-visible outcome | Success, failure or unresolved outcome is shown distinctly; `UNKNOWN` is not presented as failure/default. |
| Other contexts affected | Host/Sale may need assurance status; Inventory commitment may await policy outcome. |
| Handoff | Payment outcome → confirmation evaluation or policy exception. |
| Failure / alternative | Failed/UNKNOWN/partial outcome: do not invent Booking cancellation/default or release inventory. |
| Policy dependency | Reconciliation, provider and Required Payment Condition policy. |
| TBD / blocker | Exact user action, retry and escalation for `UNKNOWN`; grace/default behavior. |
| Source trace | [CP4 Payment lifecycle](../../05-state-machines-policies/03-payment-lifecycle.md), [CP7 Money model](../../08-conceptual-data-model/06-money-payment-settlement-payout.md). |

## Phase H — Confirmation

### B1-H01 — Evaluate Booking Confirmation Conditions

| Field | Specification |
|---|---|
| Actor / Working Context | Booking/Money/Inventory policy evaluation under the recorded Host authority and transaction context. |
| User intent | Know whether the commercial accommodation commitment is established. |
| Entry condition | Request accepted; valid terms/authority; inventory and Required Payment Condition outcomes available. |
| Canonical objects | Request, Offer/terms snapshot, Inventory Commitment, Payment Obligation/Attempt, Booking Confirmation Conditions. |
| Current relevant state | Request `ACCEPTED`; Booking does not yet exist; Payment may be succeeded but not necessarily sufficient. |
| Information required | Valid terms, authority, exclusivity, condition satisfaction, consent and other required compliance. |
| Authority required | Domain/policy evaluation; no Sale role-based acceptance. |
| Action | Evaluate whether all confirmation conditions are met. |
| Domain effect | If satisfied, establish Commercial Accommodation Commitment and create Booking `CONFIRMED`; otherwise no Booking. |
| User-visible outcome | Confirmed or still unresolved/blocked with a truthful reason category; no false confirmation. |
| Other contexts affected | Inventory gets Confirmed Accommodation Commitment; Money preserves snapshot/obligation; Sale/Host/Guest receive scoped outcome. |
| Handoff | Confirmation → Guest/Host/Sale confirmation and operational readiness. |
| Failure / alternative | Condition fails or remains UNKNOWN: remain pre-confirmation and follow applicable policy/TBD. |
| Policy dependency | Booking Confirmation Conditions and transaction snapshot. |
| TBD / blocker | Exact handling of partially satisfied, late, uncertain or changed conditions. |
| Source trace | [CP4 Booking/Booking Request](../../05-state-machines-policies/02-booking-request-and-booking.md), [CP4 Booking policy](../../05-state-machines-policies/12-booking-and-commitment-policy.md), [CP7 invariants](../../08-conceptual-data-model/10-invariants-and-stress-tests.md). |

### B1-H02 — Booking is confirmed

| Field | Specification |
|---|---|
| Actor / Working Context | Shared commercial truth; Guest, Sale and Host receive context-specific projections. |
| User intent | Rely on confirmed accommodation and next responsibilities. |
| Entry condition | All Booking Confirmation Conditions satisfied. |
| Canonical objects | Booking `CONFIRMED`, Confirmed Accommodation Commitment, Commercial Snapshot, Payment Obligation/Attempt and attribution. |
| Current relevant state | Booking begins at `CONFIRMED`; Request remains historical/request truth; Payment/Settlement/Stay remain separate. |
| Information required | Confirmed terms, dates/unit, material payment condition/status, Guest access preparation and provenance. |
| Authority required | Booking domain confirmation under valid authority/policy; recipients do not gain new authority from visibility. |
| Action | Communicate/store confirmed commercial truth. |
| Domain effect | Confirmed Accommodation Commitment is effective; Booking exists; no automatic `CHECKED_IN` or `COMPLETED` Stay. |
| User-visible outcome | Guest/Sale see confirmed Booking; Host sees fulfillment responsibility; downstream Operations can prepare when applicable. |
| Other contexts affected | Butler/BQL gain only need-to-know operational responsibility once a represented Stay becomes relevant; Admin may audit. |
| Handoff | Booking → Guest Stay Access / Stay readiness. |
| Failure / alternative | Confirmation cannot be established: do not show confirmed Booking; retain underlying Request/payment/exception truth. |
| Policy dependency | Confirmation disclosure, access and operational handoff policy. |
| TBD / blocker | Exact notification timing, QR/privacy, access credential lifecycle and Stay scheduling details. |
| Source trace | [CP5 Sale-assisted journey](../../06-v0-scope/03-critical-journeys.md), [CP6 Guest Access](../../07-information-architecture/03-public-and-guest-ia.md), [CP7 Stay model](../../08-conceptual-data-model/05-stay-and-operations.md). |

## Phase I — Booking → Stay Access / Operations Handoff

### B1-I01 — Guest receives scoped confirmation / Stay Access preparation

| Field | Specification |
|---|---|
| Actor / Working Context | Guest Stay Access context; Sale/Host may support communication. |
| User intent | Know the confirmed accommodation and prepare for the Stay. |
| Entry condition | Booking `CONFIRMED` and the relevant Stay/access relationship is represented. |
| Canonical objects | Booking, Confirmed Accommodation Commitment, Stay or Accommodation Basis, scoped QR/link/access credential. |
| Current relevant state | Booking `CONFIRMED`; Stay is separate and may be scheduled/operationally relevant, not automatically Checked In. |
| Information required | Need-to-know confirmation, arrival/access, villa/destination and help information; exact QR/privacy fields remain open. |
| Authority required | Guest relationship/scoped credential; access authority remains destination/policy scoped. |
| Action | Use/view scoped confirmation and prepare arrival. |
| Domain effect | Access projection/handoff only; does not alter Booking, Inventory, Payment or Stay state by viewing. |
| User-visible outcome | Guest can access the information needed for the valid Stay without a mandatory account where canonical policy allows. |
| Other contexts affected | Butler/BQL/Host may receive need-to-know operational preparation. |
| Handoff | Confirmed Booking → Guest Stay Access / Butler/BQL preparation. |
| Failure / alternative | Invalid/expired/unresolved credential: escalate to responsible context; do not infer universal denial or expose unrelated data. |
| Policy dependency | Guest access, QR/privacy, destination configuration and operational data policy. |
| TBD / blocker | Credential fields, expiry/revocation, consent and guest/vehicle data visibility. |
| Source trace | [CP6 Guest Access](../../07-information-architecture/03-public-and-guest-ia.md), [CP6 Operations](../../07-information-architecture/06-operations-workspaces.md), [CP8-A blocker register](../07-ux-blocker-register.md). |

### B1-I02 — Operational responsibility becomes relevant

| Field | Specification |
|---|---|
| Actor / Working Context | Host, assigned Butler and destination/BQL contexts as applicable to the represented Stay. |
| User intent | Prepare and coordinate a confirmed accommodation without changing commercial truth. |
| Entry condition | Confirmed Booking provides an Accommodation Basis for a represented/scheduled Stay and relevant assignments/scopes exist. |
| Canonical objects | Stay, Booking/Accommodation Basis, Arrival, Access, Staying Party, operational issues. |
| Current relevant state | Stay is independent; not automatically `CHECKED_IN` from Booking confirmation. |
| Information required | Need-to-know dates, party/arrival/access/preparation data and operational issues. |
| Authority required | Host/operations authority, Butler assignment, destination function/capability; no commercial authority from operational visibility. |
| Action | Prepare/coordinate future operational work. |
| Domain effect | Operations projections/records may become relevant; no automatic Booking, Payment or Settlement mutation. |
| User-visible outcome | Host/Butler/BQL understand their next operational responsibility; Guest can receive relevant preparation information. |
| Other contexts affected | Sale can monitor attributed progress; Admin may audit exceptions. |
| Handoff | Commercial confirmation → operational preparation. |
| Failure / alternative | Missing assignment/data or operational exception: record/escalate within scope; do not silently cancel Booking or mark Stay complete. |
| Policy dependency | Stay preparation/access/destination policy and assignment rules. |
| TBD / blocker | Exact scheduling, notification and exception criteria; later Stay journey is out of B1. |
| Source trace | [CP3 actor catalog](../../03-actor-authority/01-actor-catalog.md), [CP4 Stay lifecycle](../../05-state-machines-policies/04-stay-lifecycle.md), [CP6 Operations](../../07-information-architecture/06-operations-workspaces.md). |
