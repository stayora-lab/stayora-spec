# B2 — Detailed External Booking → Stay Specification

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

The steps below are UX reasoning steps, not database events, screens or new lifecycle states. They distinguish reported information, accepted external truth, Inventory Commitment and Stay.

## Phase A — External Commerce Exists

### B2-A01 — Commerce occurs outside Stayora

| Field | Specification |
|---|---|
| Actor / Working Context | External Guest/Payer/commerce source; source may be Host Direct, Owner Direct, OTA, Sale/Zalo or another legitimate channel named by canonical architecture. |
| User intent | Obtain accommodation through the external source. |
| Entry condition | External commerce exists outside Stayora Booking domain. |
| Source / provenance | External source and reference where available; provenance remains external. |
| Canonical domain objects | External Commerce concept; no Stayora Booking, Request or Payment is implied. |
| Current relevant state | No Stayora Booking lifecycle; no Stayora Payment state. |
| Information required | Only what the external source/Stay operations later legitimately provides. |
| Authority required | External source's own authority; Stayora authority does not arise merely from commerce occurring. |
| Action | Complete or record external commerce outside Stayora. |
| Domain effect | None on Stayora commercial truth. |
| Inventory effect | None until a valid report/authority establishes an external commitment/fact. |
| User-visible outcome | External parties may believe they have accommodation; Stayora does not claim to have created the commerce. |
| Other contexts affected | None yet; operations may later need a representation. |
| Handoff | External source → authorized reporter or supported integration signal. |
| Failure / alternative | No report or insufficient source information: no Stayora Inventory/Stay is created by assumption. |
| Policy dependency | External source/provenance and data-sharing policy. |
| TBD / blocker | Source evidence, minimum data and whether a specific input method is V0-supported. |
| Source trace | [CP1 external stays](../../01-product-foundation/10-oceanami-pilot.md), [CP3 WF-03](../../04-core-workflows/03-external-booking-to-stay.md), [CP7 External Accommodation](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md). |

## Phase B — Stayora Learns About It

### B2-B01 — External report or registration is submitted

| Field | Specification |
|---|---|
| Actor / Working Context | Host/Primary Host, Owner, authorized Co-host, ordinary Sale reporter or Stayora/Admin function only where canonical capability permits; integration is a possible source signal, not a designed system. |
| User intent | Inform Stayora that a legitimate external accommodation may affect Inventory and/or Stay operations. |
| Entry condition | External source/fact is known to a reporter or supported source. |
| Source / provenance | Reporter Identity, acting capacity, source/channel, external reference where available, time and submitted evidence. |
| Canonical domain objects | External Accommodation Report/record candidate, Property, Bookable Unit, dates, Staying Party minimum information. |
| Current relevant state | Report is unaccepted/unresolved; it is not yet authoritative fact by entry alone. |
| Information required | Unit/date range, source, minimum operational party/access information, reporter relationship and any evidence required by policy. |
| Authority required | Reporting capability may differ from Record External Commitment capability. Property relationship alone is not enough; ordinary Sale may report but cannot change Inventory Truth merely by reporting. |
| Action | Submit/report external accommodation information. |
| Domain effect | A report/provenance record exists for evaluation; no fake Booking/Payment/commission. |
| Inventory effect | No automatic BOOKED/blocked outcome; Inventory may remain unchanged pending evaluation. |
| User-visible outcome | Reporter sees submitted/pending status; Host/Admin can see a report requiring evaluation where scope permits. |
| Other contexts affected | Potential Host/Inventory/Admin evaluation; Butler/BQL not yet operationally responsible. |
| Handoff | Reporter/source → authority/provenance evaluation. |
| Failure / alternative | Missing relationship, wrong scope or insufficient data: retain report as unresolved/invalid input; do not silently trust it. |
| Policy dependency | Grant/revoke, evidence threshold, reporter handling and privacy policy. |
| TBD / blocker | Who may submit which source, required fields/evidence and reviewer/automation boundary. |
| Source trace | [CP3 Record External Commitment](../../03-actor-authority/02-authority-capabilities.md), [CP3 actor-resource matrix](../../03-actor-authority/03-actor-resource-matrix.md), [CP8-A actor model](../02-actor-context-responsibility.md). |

## Phase C — Provenance / Authority Evaluation

### B2-C01 — Evaluate reporter, source and scope

| Field | Specification |
|---|---|
| Actor / Working Context | Authorized Host/Inventory authority, delegated actor or Stayora/Admin function with explicit scoped review capability. |
| User intent | Determine whether the submitted information can be relied on for a specific Property/Unit/time scope. |
| Entry condition | External report exists with traceable reporter/source data. |
| Source / provenance | Identity + acting capacity + relationship + authority basis + source/evidence + timestamp. |
| Canonical domain objects | External report, Actor Relationship/Authority Grant, Property, Bookable Unit, evidence/provenance. |
| Current relevant state | Report unresolved; no authoritative external fact yet. |
| Information required | Resource scope, dates, source, report history, evidence/confidence if policy requires. |
| Authority required | Explicit Record External Commitment capability for Inventory effect; operational authority for Stay handling; these are not interchangeable. |
| Action | Evaluate/accept/reject/escalate according to existing policy; exact workflow remains open. |
| Domain effect | May establish an authoritative External Accommodation Fact or preserve report as unresolved. |
| Inventory effect | No effect until an authorized external commitment/fact is accepted for Inventory; no automatic availability change. |
| User-visible outcome | Reporter/Host/Admin can distinguish pending, accepted/authoritative, rejected or conflict/unresolved categories where supported. |
| Other contexts affected | Inventory and operations only after valid authority/evidence outcome. |
| Handoff | Evaluation → External Accommodation Fact or exception. |
| Failure / alternative | Authority/evidence insufficient: preserve source/report history, do not discard or promote silently. |
| Policy dependency | Record External Commitment grant/revoke, evidence threshold, confidence, correction and review policy. |
| TBD / blocker | Exact acceptance criteria and who decides when report becomes authoritative. |
| Source trace | [CP3 authority model](../../03-actor-authority/00-authority-model.md), [CP3 capability](../../03-actor-authority/02-authority-capabilities.md), [CP7 provenance](../../08-conceptual-data-model/08-provenance-temporal-history.md). |

## Phase D — External Accommodation Fact

### B2-D01 — Establish External Accommodation Fact

| Field | Specification |
|---|---|
| Actor / Working Context | Actor with accepted authority/capability or authorized manual/Admin function. |
| User intent | Represent the external accommodation truth sufficiently for Inventory and/or operations. |
| Entry condition | Source/provenance/authority outcome supports canonical representation; exact threshold remains policy-dependent. |
| Source / provenance | External source, reference where available, recorder/capacity, Property/Unit, dates, minimum Staying Party information, evidence and time. |
| Canonical domain objects | External Accommodation candidate aggregate, Property, Bookable Unit, Staying Party, Accommodation Range and provenance/history. |
| Current relevant state | Authoritative external fact exists as a distinct external concept; it is not Booking. |
| Information required | Operationally necessary facts only; external revenue/margin/payment are not required merely for truth representation. |
| Authority required | Valid scoped capability to record/establish external commitment and/or valid operational recording authority. |
| Action | Record/establish external accommodation fact with provenance. |
| Domain effect | External Accommodation becomes a canonical reference for Inventory and/or Stay where accepted. |
| Inventory effect | May support a Confirmed Accommodation Commitment only through explicit Inventory authority and compatible commitment rules; fact itself is not commitment. |
| User-visible outcome | Host/Admin can distinguish external source and trust/authority status; no Stayora commerce badge is implied. |
| Other contexts affected | Inventory evaluation and potential Stay preparation. |
| Handoff | External Fact → Inventory effect and/or Stay representation. |
| Failure / alternative | Insufficient evidence/authority: keep report unresolved; do not create fake Booking or commitment. |
| Policy dependency | Fact acceptance, evidence, source confidence, correction and operational minimum-data policy. |
| TBD / blocker | Exact fact acceptance timing, confidence and whether a fact can create a Stay without Inventory commitment. |
| Source trace | [CP7 External Accommodation](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md), [CP3 WF-03](../../04-core-workflows/03-external-booking-to-stay.md). |

## Phase E — Inventory Effect

### B2-E01 — Establish compatible external Inventory Commitment

| Field | Specification |
|---|---|
| Actor / Working Context | Inventory authority/orchestration using an authoritative external fact. |
| User intent | Protect the Bookable Unit × Time from incompatible commitments. |
| Entry condition | External fact is authoritative enough and an authorized commitment action is available. |
| Source / provenance | External fact + recorder authority + evidence + effective dates. |
| Canonical domain objects | External Accommodation, Inventory Commitment, Bookable Unit × Time, existing commitments. |
| Current relevant state | External fact accepted; Inventory Commitment may not yet exist. |
| Information required | Unit/date range, effective external commitment, existing commitments, authority and authoritative end/release basis. |
| Authority required | Explicit Record External Commitment/Inventory Authority; Sale report or whitelist alone is insufficient. |
| Action | Establish compatible Confirmed Accommodation Commitment or equivalent external commitment effect where canonical policy supports it. |
| Domain effect | Inventory records a commitment linked to external provenance; no Booking is created. |
| Inventory effect | Derived Availability recomputes from effective commitments; external confirmed commitment has equivalent inventory effect to a valid confirmed source, without channel priority. |
| User-visible outcome | Host/Sale/Admin can see dates protected by external source; public/actor-facing availability can reflect derived truth where policy allows. |
| Other contexts affected | Sale search/Host calendar projections; conflict handling if overlap exists. |
| Handoff | Inventory effect → conflict check or Stay representation. |
| Failure / alternative | Incompatible overlap: preserve external fact and existing commitment; surface conflict/exception; no silent overwrite/cancel. |
| Policy dependency | Commitment type, effective end, conflict, sync health and confidence. |
| TBD / blocker | Whether every accepted fact creates commitment, conflict precedence/remediation and release rules. |
| Source trace | [CP4 Inventory model](../../05-state-machines-policies/01-inventory-commitment-model.md), [CP7 Inventory](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md), [CP3 capability](../../03-actor-authority/02-authority-capabilities.md). |

## Phase F — Stay Representation

### B2-F01 — Represent an externally originated Stay

| Field | Specification |
|---|---|
| Actor / Working Context | Host/authorized operational actor or Stayora/Admin function with Stay recording authority; Guest/Butler/BQL are consumers as scope permits. |
| User intent | Make a real upcoming/current external accommodation operationally visible. |
| Entry condition | External Accommodation fact and sufficient operational basis/evidence exist; a Stayora Booking is not required. |
| Source / provenance | External Accommodation basis, source, recorder, dates, Staying Party minimum data and timestamps. |
| Canonical domain objects | External Accommodation, Accommodation Basis, Stay, Staying Party, Property/Unit, Destination. |
| Current relevant state | Stay may be represented as `SCHEDULED`; it is not automatically `CHECKED_IN` or `COMPLETED`. |
| Information required | Arrival/departure, party/access/readiness data needed for operations; no unnecessary external economics. |
| Authority required | Stay/operations authority and relationship; operational assignment does not create commercial authority. |
| Action | Create/record an operational Stay representation linked to external basis. |
| Domain effect | Stay truth exists independently from Booking; external provenance remains attached. |
| Inventory effect | Existing commitment/history remains; Stay does not itself create a new commitment or release one. |
| User-visible outcome | Host/operations can prepare; Guest may receive scoped access where eligible; commercial origin remains external. |
| Other contexts affected | Butler/BQL operational work becomes relevant; Admin may audit. |
| Handoff | Stay representation → Guest Access and Operations. |
| Failure / alternative | Insufficient evidence/operational data: keep external fact/report pending; do not claim a checked-in/completed Stay. |
| Policy dependency | Stay creation/evidence, access, assignment, destination policy and privacy. |
| TBD / blocker | Exact minimum data/evidence and timing for Stay creation. |
| Source trace | [CP7 Stay](../../08-conceptual-data-model/05-stay-and-operations.md), [CP3 WF-04](../../04-core-workflows/04-stay-lifecycle.md), [CP5 external journey](../../06-v0-scope/03-critical-journeys.md). |

## Phase G — Guest Stay Access and Operations

### B2-G01 — Provide scoped Guest Stay Access where eligible

| Field | Specification |
|---|---|
| Actor / Working Context | Guest Stay Access; Guest may be external to Stayora commerce. |
| User intent | Access the operational information/credential needed for the represented Stay. |
| Entry condition | Valid Stay relationship, eligible scoped access and applicable destination policy. |
| Source / provenance | Stay + External Accommodation basis + access/Guest relationship. |
| Canonical domain objects | Stay, Staying Party, scoped Guest Access/QR/link concept, Destination. |
| Current relevant state | Stay scheduled/current according to Stay lifecycle; not automatically checked in. |
| Information required | Need-to-know arrival/access/villa/destination/help information. |
| Authority required | Guest relationship and destination/access policy; QR/link is not underlying business Authority. |
| Action | Use/view scoped access information. |
| Domain effect | Access projection only; no Booking, Payment or commerce provenance mutation. |
| Inventory effect | None; access does not release or create commitment. |
| User-visible outcome | Guest can prepare/use the Stay without implying Stayora-originated commerce. |
| Other contexts affected | Butler/BQL can validate current Stay/access as scoped. |
| Handoff | Stay → Guest Access / destination operations. |
| Failure / alternative | Missing/invalid access data: escalate; do not resolve QR/privacy policy here or universally deny. |
| Policy dependency | QR/privacy, destination access, consent and data-sharing policy. |
| TBD / blocker | Exact fields, credential lifecycle and Guest/vehicle data. |
| Source trace | [CP6 Guest Access](../../07-information-architecture/03-public-and-guest-ia.md), [CP8-A semantics](../05-ux-language-semantics.md). |

### B2-G02 — Butler / Destination operations consume scoped Stay truth

| Field | Specification |
|---|---|
| Actor / Working Context | Assigned Butler and Destination/BQL contexts; Host remains operationally responsible within scope. |
| User intent | Prepare, support and coordinate the actual Stay. |
| Entry condition | Stay is represented and operationally relevant; assignments/function scopes exist. |
| Source / provenance | Stay, External Accommodation basis, arrival/access/party operational data and incident evidence. |
| Canonical domain objects | Stay, Arrival, Access, Staying Party, Incident/Issue, Destination. |
| Current relevant state | `SCHEDULED`/arrival/in-stay semantics according to Stay lifecycle; no automatic completion. |
| Information required | Need-to-know operational occupancy, arrivals/departures, access, guest counts, services and issues. |
| Authority required | Butler assignment/Operations Authority and Destination Staff relationship/function; no commercial authority from visibility. |
| Action | Prepare/coordinate, record operational evidence/incident, support access/check-in/out. |
| Domain effect | Stay/Operations records update; Incident remains separate from Finding/Responsibility/Consequence. |
| Inventory effect | None unless a separately authorized Inventory action occurs; Butler observation alone does not create a Block. |
| User-visible outcome | Operations understands current work; Guest receives operational support; no Owner/Sale economics exposed. |
| Other contexts affected | Host, Admin, Guest and downstream Reputation/Verification may consume qualifying evidence. |
| Handoff | Operations → incident/completion/review paths, all outside B2 detail. |
| Failure / alternative | Missing assignment/data or issue: escalate/record; do not impose commercial or financial consequence. |
| Policy dependency | Destination configuration, operational access, Incident and completion policy. |
| TBD / blocker | Assignment changes, local access rules, incident severity and completion blockers. |
| Source trace | [CP3 actor-resource matrix](../../03-actor-authority/03-actor-resource-matrix.md), [CP6 Operations](../../07-information-architecture/06-operations-workspaces.md), [CP4 Stay](../../05-state-machines-policies/04-stay-lifecycle.md). |

## Phase H — Completion / Historical Truth

### B2-H01 — Preserve external provenance through checkout/completion

| Field | Specification |
|---|---|
| Actor / Working Context | Stay/Operations authority with downstream Admin/Quality/Money consumers only where eligible. |
| User intent | Retain truthful history of an external Stay after it ends. |
| Entry condition | Operational Stay reaches checkout/completion readiness according to Stay policy. |
| Source / provenance | Original External Accommodation source, recorder, authority, dates, Stay evidence, incidents and corrections. |
| Canonical domain objects | Stay, External Accommodation, Inventory Commitment/history, Incident/Finding where applicable, Review Right/Reputation signals. |
| Current relevant state | `CHECKED_OUT` may precede `COMPLETED`; no automatic settlement/commission. |
| Information required | Actual operations/completion evidence and correction history; external economics remain external unless separate service policy applies. |
| Authority required | Stay completion authority; downstream domains use their own authority/policy. |
| Action | Record completion/correction through canonical history mechanisms. |
| Domain effect | Stay/history remains represented; provenance is not rewritten as Stayora commerce. |
| Inventory effect | Commitment ends only with authoritative end/release; physical absence alone does not release it. |
| User-visible outcome | Host/Guest/Operations/Admin see appropriate historical truth; qualifying external evidence may support Review Right. |
| Other contexts affected | Reputation/Verification may consume qualifying evidence; Money does not receive automatic commission. |
| Handoff | Completed external Stay → historical/reputation/admin projections. |
| Failure / alternative | Late correction/dispute: add amendment/supersession/replacement/correction truth; do not destructively rewrite origin. |
| Policy dependency | Completion, Review Right, Incident, Reputation and correction/history policy. |
| TBD / blocker | Completion blockers, review evidence threshold, retention and dispute rules. |
| Source trace | [CP7 provenance](../../08-conceptual-data-model/08-provenance-temporal-history.md), [CP7 quality](../../08-conceptual-data-model/07-quality-and-cases.md), [CP4 Stay](../../05-state-machines-policies/04-stay-lifecycle.md). |
