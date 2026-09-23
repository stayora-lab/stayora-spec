# B4 — Detailed Stay Operations Journey

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

Each step is an operational reasoning step, not a screen, database event or new Stay state. Operational phases such as Preparation and Ready are deliberately kept separate from the canonical lifecycle.

## Phase A — Stay becomes operationally relevant

### B4-A01 — Establish operational Stay basis

| Field | Specification |
|---|---|
| Actor / Working Context | Host/authorized operational context or Stayora/Admin function with scoped recording authority. |
| Operational responsibility | Establish that upcoming accommodation is sufficiently truthful for Stay preparation. |
| User intent | Make a legitimate upcoming accommodation operationally actionable. |
| Entry condition | Accommodation Basis is supported: confirmed Stayora Booking (B1/B3) or accepted External Accommodation (B2). |
| Accommodation Basis / provenance | Stayora Booking origin or External Accommodation origin; preserve source, recorder and evidence. |
| Canonical objects | Accommodation Basis, Stay, Property, Bookable Unit, Staying Party, Destination. |
| Current relevant state | Stay may be represented as `SCHEDULED`; not Check-in or Completed. |
| Information required | Unit, accommodation range, party/access minimum, source/provenance and operational evidence required by policy. |
| Information visible | Host/operations see need-to-know basis and preparation data; Guest sees own upcoming accommodation where eligible. |
| Authority required | Stay/operational recording authority; operational assignment does not create commercial authority. |
| Action / domain effect | Represent or activate operational Stay truth; do not fabricate Booking for external origin. |
| Stay state effect | `SCHEDULED` only where canonical basis and lifecycle support it. |
| Inventory effect | None by Stay representation alone. |
| Guest-visible outcome | Upcoming accommodation can be prepared where eligible. |
| Other contexts affected | Host, Butler, Destination/BQL and scoped Guest Access projections. |
| Handoff | Accommodation Basis → Stay preparation. |
| Evidence / audit need | Basis, source, authority, recorder, timestamp, relevant corrections. |
| Failure / alternative | Insufficient basis/evidence: retain report/pending truth; do not claim an operational Stay. |
| Policy dependency | Stay creation, provenance, privacy and minimum operational data. |
| TBD / blocker | Exact evidence threshold, minimum fields and who may establish Stay from an external fact. |
| Source trace | [CP7 Stay](../../08-conceptual-data-model/05-stay-and-operations.md), [B2 convergence](../b2-external-booking-to-stay/README.md), [B3 overview](../b3-direct-guest-booking/01-journey-overview.md). |

## Phase B — Pre-arrival

### B4-B01 — Prepare upcoming Stay

| Field | Specification |
|---|---|
| Actor / Working Context | Host, assigned Butler and Destination/BQL operational contexts. |
| Operational responsibility | Review upcoming arrival, party, unit, access and known operational information. |
| User intent | Make the accommodation and support path ready for the expected Guest. |
| Entry condition | Stay `SCHEDULED`; assignment/function scope exists or Host retains responsibility. |
| Accommodation Basis / provenance | Basis remains attached; operations need not inspect full commercial source. |
| Canonical objects | Stay, Staying Party, Arrival, Access, Butler Assignment, Destination, Incident/Issue. |
| Current relevant state | `SCHEDULED`; Preparation is a phase, not a new state. |
| Information required | Dates, Unit, Guest/party data allowed by policy, access/arrival requirements, known issues. |
| Information visible | Each context receives need-to-know operational projection; no full ledger/economics. |
| Authority required | Assignment/function/Stay scope; no Booking Authority for routine preparation. |
| Action / domain effect | Prepare, coordinate and record operational notes/evidence. |
| Stay state effect | None; remains `SCHEDULED`. |
| Inventory effect | None. |
| Guest-visible outcome | Relevant arrival/access/help information may be available. |
| Other contexts affected | Guest, Host, Butler, Destination/BQL. |
| Handoff | Host/Stay → Butler/Destination preparation. |
| Evidence / audit need | Actor/capacity, scope, preparation observation and timestamp. |
| Failure / alternative | Missing assignment/data: Host responsibility remains; escalate without inventing auto-reassignment. |
| Policy dependency | Assignment, access, privacy and destination configuration. |
| TBD / blocker | Exact propagation, field visibility, notification and assignment-change rules. |
| Source trace | [CP6 Operations](../../07-information-architecture/06-operations-workspaces.md), [CP8-A Butler context](../02-actor-context-responsibility.md). |

## Phase C — Readiness

### B4-C01 — Report operational readiness

| Field | Specification |
|---|---|
| Actor / Working Context | Butler or Host/authorized operational actor within assigned Property/Stay scope. |
| Operational responsibility | Report whether known preparation tasks/conditions support arrival. |
| User intent | Give downstream contexts a truthful readiness signal. |
| Entry condition | Stay `SCHEDULED`; sufficient preparation observations exist. |
| Accommodation Basis / provenance | Retain Stay basis; readiness does not change origin. |
| Canonical objects | Stay, operational readiness milestone, Unit, Access, Incident/Issue. |
| Current relevant state | Still `SCHEDULED`; `READY` is not created as a Stay state. |
| Information required | Observed preparation/access conditions and unresolved issues. |
| Information visible | Host/operations see readiness and blockers; Guest sees only relevant instructions/status. |
| Authority required | Operational reporting capability; no commercial or Inventory authority. |
| Action / domain effect | Record readiness milestone/evidence and any issue/Incident according to policy. |
| Stay state effect | None. |
| Inventory effect | None unless a separate authorized block workflow exists. |
| Guest-visible outcome | Truthful preparation/access guidance, not a guarantee of Check-in. |
| Other contexts affected | Host, Butler, Destination/BQL, possibly Admin for exception. |
| Handoff | Readiness signal → arrival monitoring. |
| Evidence / audit need | Reporter, capacity, observed condition, timestamp, unresolved issue. |
| Failure / alternative | Unready/unknown: preserve blocker and escalation; do not add `READY` state or promise. |
| Policy dependency | Readiness criteria, escalation and access policy. |
| TBD / blocker | Exact readiness threshold and owner of unresolved readiness problem. |
| Source trace | [CP4 Stay lifecycle](../../05-state-machines-policies/04-stay-lifecycle.md), [CP6 Butler workspace](../../07-information-architecture/06-operations-workspaces.md). |

## Phase D — Arrival

### B4-D01 — Record expected or physical arrival

| Field | Specification |
|---|---|
| Actor / Working Context | Guest, Butler, Destination/BQL or other authorized operational context as supported. |
| Operational responsibility | Distinguish expected arrival from physical arrival and access observation. |
| User intent | Arrive and obtain relevant support/access. |
| Entry condition | Stay `SCHEDULED`; arrival window/context is known. |
| Accommodation Basis / provenance | Stay basis remains unchanged. |
| Canonical objects | Stay, Arrival event/observation, Access, Staying Party, Destination. |
| Current relevant state | `SCHEDULED`; arrival is an observation, not a core Stay state. |
| Information required | Arrival evidence, relevant party/access context and destination requirements. |
| Information visible | Guest sees instructions/help; operations see arrival status within scope. |
| Authority required | Operational observation/access function; arrival alone does not grant Check-in authority. |
| Action / domain effect | Record expected/physical arrival evidence and coordinate next step. |
| Stay state effect | None automatically. |
| Inventory effect | None. |
| Guest-visible outcome | Arrival/support path is understood. |
| Other contexts affected | Butler, Destination/BQL, Host and Guest. |
| Handoff | Arrival observation → Check-in evaluation or exception. |
| Evidence / audit need | Who observed, what was observed, time, source and scope. |
| Failure / alternative | Late/no arrival or access uncertainty: preserve observation; do not cancel, release or Complete. |
| Policy dependency | Arrival/access and local destination policy. |
| TBD / blocker | Exact arrival evidence, vehicle/access fields and escalation. |
| Source trace | [CP4 Stay](../../05-state-machines-policies/04-stay-lifecycle.md), [CP6 Destination operations](../../07-information-architecture/06-operations-workspaces.md). |

## Phase E — Check-in

### B4-E01 — Record authorized Check-in

| Field | Specification |
|---|---|
| Actor / Working Context | Butler/Host/authorized operational context with Check-in capability. |
| Operational responsibility | Confirm the Stay has entered the canonical Check-in condition. |
| User intent | Complete arrival into the accommodation and begin the Stay operationally. |
| Entry condition | Stay `SCHEDULED`; supported arrival/access/precondition evidence exists. |
| Accommodation Basis / provenance | Basis remains available for audit; no commercial mutation is required. |
| Canonical objects | Stay, Staying Party, Arrival, Access, Check-in evidence, Incident if issue exists. |
| Current relevant state | `SCHEDULED`. |
| Information required | Preconditions/evidence required by canonical policy; Guest/party/access details within scope. |
| Information visible | Guest receives check-in result/instructions; Host/operations receive status and evidence. |
| Authority required | Explicit operational Check-in authority; Butler assignment alone may not answer every grant—exact scope remains CP3/TBD. |
| Action / domain effect | Record Check-in when authorized and evidence supports it. |
| Stay state effect | `SCHEDULED → CHECKED_IN`. |
| Inventory effect | None by Check-in alone. |
| Guest-visible outcome | Stay is checked in or blocked with truthful reason/status. |
| Other contexts affected | Host, Butler, Destination/BQL, Guest, Admin/Quality only where relevant. |
| Handoff | Check-in → in-stay operations. |
| Evidence / audit need | Actual actor/capacity, authority, time, evidence and any exception. |
| Failure / alternative | Payment/compliance/access blocker may affect Check-in only under explicit policy; do not invent a payment-state transition. |
| Policy dependency | Check-in, access, privacy and compliance policy. |
| TBD / blocker | Exact preconditions, actor grants and whether any policy blocker prevents Check-in. |
| Source trace | [CP3 Butler capability](../../03-actor-authority/02-authority-capabilities.md), [CP4 Stay lifecycle](../../05-state-machines-policies/04-stay-lifecycle.md), [CP7 Stay](../../08-conceptual-data-model/05-stay-and-operations.md). |

## Phase F — In-Stay operations

### B4-F01 — Support and coordinate a checked-in Stay

| Field | Specification |
|---|---|
| Actor / Working Context | Guest, Host, Butler and Destination/BQL operational contexts. |
| Operational responsibility | Provide scoped support, access assistance, coordination and operational evidence. |
| User intent | Use the accommodation and obtain help when needed. |
| Entry condition | Stay `CHECKED_IN`. |
| Accommodation Basis / provenance | Origin remains available only for legitimate support/audit/policy needs. |
| Canonical objects | Stay, Staying Party, Access, Incident/Issue, Destination Services, operational notes. |
| Current relevant state | `CHECKED_IN`; no `IN_STAY` state added. |
| Information required | Current operational needs, access, support request and incident facts. |
| Information visible | Need-to-know Guest/Host/Butler/BQL projections; no full commerce ledger. |
| Authority required | Operational assignment/function/Stay scope; Guest may report, not administer the Stay. |
| Action / domain effect | Coordinate service/help and record evidence or Incident where applicable. |
| Stay state effect | Remains `CHECKED_IN`. |
| Inventory effect | None. |
| Guest-visible outcome | Support path and relevant status are available. |
| Other contexts affected | Host, Butler, Destination/BQL, Admin/Quality for qualifying case. |
| Handoff | Operational issue → Incident handling when needed. |
| Evidence / audit need | Report, actor, time, scope, response and correction history. |
| Failure / alternative | Missing assignment/data: escalate; do not create task-management suite or commercial consequence. |
| Policy dependency | Destination services, Incident, privacy and escalation policy. |
| TBD / blocker | Service catalogue, severity and response expectations. |
| Source trace | [CP6 Operations](../../07-information-architecture/06-operations-workspaces.md), [CP5 Incident journey](../../06-v0-scope/03-critical-journeys.md). |

## Phase G — Incident / exception

### B4-G01 — Report and handle operational Incident

| Field | Specification |
|---|---|
| Actor / Working Context | Guest, Butler, Host, Destination/BQL or authorized Staff context. |
| Operational responsibility | Record facts, route operational response and preserve evidence. |
| User intent | Report/resolve an operational problem during or around the Stay. |
| Entry condition | Observation or complaint with a plausible Stay/operational scope. |
| Accommodation Basis / provenance | Stay and source remain attached; Incident does not rewrite origin. |
| Canonical objects | Incident, evidence, Stay, Finding/Responsibility/Consequence only if later qualified by their own authority. |
| Current relevant state | Usually `CHECKED_IN`; may also concern `SCHEDULED` or `CHECKED_OUT` follow-up. |
| Information required | What happened, time, resource, reporter, evidence and immediate operational need. |
| Information visible | Each actor sees only facts/actions needed for role; Guest sees status/help appropriate to their issue. |
| Authority required | Incident reporting/handling capability; no automatic blame or financial/reputation authority. |
| Action / domain effect | Create/route/update Incident and response evidence. |
| Stay state effect | None automatically. |
| Inventory effect | None automatically; a separate authorized Block workflow is required. |
| Guest-visible outcome | Issue acknowledged/handled/escalated where policy allows. |
| Other contexts affected | Host, Butler, Destination/BQL, Admin/Quality and possibly Money only through separate policy. |
| Handoff | Report → Incident handling → escalation/follow-up. |
| Evidence / audit need | Original report, amendments, actors, response, timestamps and resolution evidence. |
| Failure / alternative | Insufficient facts or conflicting reports: preserve both, investigate/escalate; do not assign blame. |
| Policy dependency | Incident severity, escalation, privacy and follow-up policy. |
| TBD / blocker | Finding threshold, responsibility assignment, compensation and consequence policy. |
| Source trace | [CP2 Incident boundaries](../../02-domain/01-domain-glossary.md), [CP4 Incident lifecycle](../../05-state-machines-policies/07-incident-lifecycle.md), [CP7 quality/cases](../../08-conceptual-data-model/07-quality-and-cases.md). |

## Phase H/I — Checkout preparation and Checkout

### B4-H01 — Prepare and record authorized Checkout

| Field | Specification |
|---|---|
| Actor / Working Context | Guest, Butler, Host or authorized operational context. |
| Operational responsibility | Coordinate scheduled departure, Guest departure and Checkout evidence. |
| User intent | End the occupied accommodation period and complete departure steps. |
| Entry condition | Stay `CHECKED_IN`; departure context is reached or otherwise supported. |
| Accommodation Basis / provenance | Basis remains unchanged; unresolved incidents remain linked. |
| Canonical objects | Stay, Departure/Checkout evidence, Access, Incident, operational completion readiness. |
| Current relevant state | `CHECKED_IN`; scheduled departure and physical departure are observations. |
| Information required | Departure/condition evidence and unresolved operational issues relevant to completion. |
| Information visible | Guest sees checkout requirements/help; operations see departure and evidence. |
| Authority required | Checkout recording/confirmation capability; not payment authority. |
| Action / domain effect | Record authorized Checkout after supported evidence. |
| Stay state effect | `CHECKED_IN → CHECKED_OUT`. |
| Inventory effect | No direct release or Availability change from Checkout alone. |
| Guest-visible outcome | Departure/Checkout is recorded or remains pending with truthful reason. |
| Other contexts affected | Host, Butler, Destination/BQL, Incident/Quality. |
| Handoff | Checkout → completion evaluation. |
| Evidence / audit need | Actor/capacity, time, condition/issue evidence, access return where applicable. |
| Failure / alternative | Guest departs late/early or issue unresolved: preserve evidence; do not force completion or financial consequence. |
| Policy dependency | Checkout, access, incident and completion readiness policy. |
| TBD / blocker | Exact Checkout evidence, deposit handling and unresolved issue treatment. |
| Source trace | [CP4 Stay lifecycle](../../05-state-machines-policies/04-stay-lifecycle.md), [CP7 Stay](../../08-conceptual-data-model/05-stay-and-operations.md). |

## Phase J/K — Completion and post-stay handoff

### B4-J01 — Evaluate completion and preserve post-stay history

| Field | Specification |
|---|---|
| Actor / Working Context | Stay/Operations authority; Admin, Quality, Reputation, Review and Money contexts only when independently eligible. |
| Operational responsibility | Determine whether canonical completion conditions are satisfied and preserve history. |
| User intent | Close the operational Stay truthfully and continue eligible follow-up. |
| Entry condition | Stay `CHECKED_OUT`; Operational Completion Readiness/evidence exists. |
| Accommodation Basis / provenance | Preserve original basis, source, corrections, incidents and operational history. |
| Canonical objects | Stay, completion evidence, Incident, Review Right, Reputation/Verification evidence, Money/Settlement references. |
| Current relevant state | `CHECKED_OUT`; `COMPLETED` is not automatic. |
| Information required | Qualifying completion evidence and unresolved policy-defined exceptions. |
| Information visible | Guest/Host see completed outcome where allowed; downstream contexts consume scoped history. |
| Authority required | Stay completion authority; downstream domains use their own authority/policy. |
| Action / domain effect | Set `COMPLETED` only when canonical conditions pass; otherwise preserve unresolved readiness. |
| Stay state effect | `CHECKED_OUT → COMPLETED` when supported; no automatic `DID_NOT_OCCUR` after Check-in. |
| Inventory effect | None directly. |
| Guest-visible outcome | Stay is completed or remains under truthful follow-up. |
| Other contexts affected | Review/Quality/Reputation/Money only if independently eligible. |
| Handoff | Completion → eligible post-stay processes. |
| Evidence / audit need | Completion basis, unresolved exceptions, corrections and actual actor. |
| Failure / alternative | Open Incident does not automatically block completion; only qualifying policy-defined exceptions may. |
| Policy dependency | Completion, Review Right, Reputation, Verification and Settlement policies. |
| TBD / blocker | Exact completion blockers and post-stay timing/consequence rules. |
| Source trace | [CP4 Stay lifecycle](../../05-state-machines-policies/04-stay-lifecycle.md), [CP7 Stay](../../08-conceptual-data-model/05-stay-and-operations.md), [CP5 critical journeys](../../06-v0-scope/03-critical-journeys.md). |
