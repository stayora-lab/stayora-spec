# B5 — Detailed Inventory Intervention Journey

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

Each step is a truth/authority reasoning step, not a calendar action, database event or screen. No generic `UNAVAILABLE` state is introduced.

## Phase A — Intervention need arises

### B5-A01 — Intent or operational fact is raised

| Field | Specification |
|---|---|
| Actor / Working Context | Owner/Host, Guest, Butler, BQL, Sale reporter or authorized Staff context. |
| Intent / observed fact | Owner use request, unusable condition, correction need or other operational signal. |
| Entry condition | A Unit × Time concern is observed or intended; no intervention is established yet. |
| Resource scope | Specific Property/Bookable Unit and candidate time range. |
| Canonical objects | Operational report/Incident, Owner intent, Unit, range, existing Inventory truth. |
| Current Inventory truth | Existing effective Commitments/Blocks remain authoritative. |
| Basis / provenance | Reporter/actor, acting capacity, source, time and initial reason/evidence. |
| Authority required | Reporting/intent capability only; not yet Inventory Authority. |
| Evidence / reason | Observation, owner request, source/reference and relevant operational evidence. |
| Action / domain effect | Record/report the need; do not mutate Availability. |
| Commitment / Block effect | None by report alone. |
| Derived Availability effect | None. |
| Bookability effect | Unknown until authorized basis is established. |
| Affected existing truth | None is deleted/overwritten. |
| Conflict / exception | Potential overlap is queued for evaluation. |
| Other contexts affected | Inventory/Host/Operations/Admin as scope permits. |
| User-visible outcome | Reporter sees submitted/pending truth, not confirmed block. |
| Handoff | Intent/report → authority and evidence evaluation. |
| Correction / release path | Correct the report through explicit amendment; no destructive deletion. |
| Policy dependency | Reporting, evidence, privacy and notification policy. |
| TBD / blocker | Minimum fields, report acceptance and exact source categories. |
| Source trace | [CP3 authority](../../03-actor-authority/02-authority-capabilities.md), [B4 Incident](../b4-stay-operations/10-incident-stress-test.md), [CP7 Inventory](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md). |

## Phase B — Authority evaluation

### B5-B01 — Resolve acting capacity and scope

| Field | Specification |
|---|---|
| Actor / Working Context | Inventory Authority / Host / authorized Staff evaluation context. |
| Intent / observed fact | Determine whether the actor may intervene over the Unit × Time. |
| Entry condition | Report/intent exists with identifiable actor/source. |
| Resource scope | Property, Bookable Unit, time range, action type and lifecycle. |
| Canonical objects | Identity, acting capacity, relationship/delegation, authority grant, Unit, range. |
| Current Inventory truth | Existing commitments/blocks remain unchanged. |
| Basis / provenance | Authority source, scope, effective time, reason and evidence. |
| Authority required | Explicit capability for Owner Block, Maintenance Block, external commitment or correction; role/visibility alone insufficient. |
| Evidence / reason | Valid relationship, grant, source and operational/owner reason where required. |
| Action / domain effect | Accept, reject, defer or escalate intervention request. |
| Commitment / Block effect | None until authorized decision. |
| Derived Availability effect | None. |
| Bookability effect | None. |
| Affected existing truth | Preserved for overlap evaluation. |
| Conflict / exception | Missing/revoked/ambiguous authority becomes exception; no automatic reassignment. |
| Other contexts affected | Requester, Host, Inventory, Admin. |
| User-visible outcome | Actor sees authorized/pending/rejected status where allowed. |
| Handoff | Authority evaluation → existing truth evaluation or closure. |
| Correction / release path | Correct authority evidence or supersede the request; preserve history. |
| Policy dependency | Authority lifecycle, delegation, resource scope and privacy. |
| TBD / blocker | Non-delegable actions, precedence and grant propagation. |
| Source trace | [CP3 authority invariants](../../03-actor-authority/06-authority-invariants.md), [CP4 Inventory policy](../../05-state-machines-policies/13-inventory-policy.md). |

## Phase C — Existing Inventory truth evaluation

### B5-C01 — Evaluate Unit × Time overlap

| Field | Specification |
|---|---|
| Actor / Working Context | Inventory/Booking/exception evaluation context. |
| Intent / observed fact | Understand whether proposed intervention overlaps effective truth. |
| Entry condition | Actor/scope is sufficiently authorized or evaluation is required. |
| Resource scope | Unit × Time and all relevant effective bases. |
| Canonical objects | Temporary Commitment, Confirmed Stayora Commitment, External Commitment, Owner Block, Maintenance Block, Stay/Booking/External Accommodation. |
| Current Inventory truth | Derived from effective Commitments and Blocks; no manual flag. |
| Basis / provenance | Each basis retains source, actor, authority, timestamps, reason/effective lifetime. |
| Authority required | Read/evaluation capability; mutation remains separate. |
| Evidence / reason | Existing records, sources and effective end/release basis. |
| Action / domain effect | Classify compatible coexistence, prevention or potential conflict. |
| Commitment / Block effect | No change during evaluation. |
| Derived Availability effect | No change until authorized basis becomes effective. |
| Bookability effect | Remains context-dependent. |
| Affected existing truth | All legitimate facts/commitments remain recorded. |
| Conflict / exception | Incompatible exclusive overlap is Inventory Conflict; no winner selected. |
| Other contexts affected | Host, Guest/Sale projections, Operations, Admin. |
| User-visible outcome | Relevant availability/conflict status is scoped and truthful. |
| Handoff | Truth evaluation → intervention decision or conflict path. |
| Correction / release path | Correct wrong Unit/range/source through explicit correction. |
| Policy dependency | Commitment exclusivity, effective interval and conflict policy. |
| TBD / blocker | True conflict resolution and source/channel behavior. |
| Source trace | [CP4 Inventory Commitment](../../05-state-machines-policies/01-inventory-commitment-model.md), [CP7 Inventory](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md). |

## Phase D — Intervention creation / decision

### B5-D01 — Establish canonical Block or Commitment effect

| Field | Specification |
|---|---|
| Actor / Working Context | Authorized Inventory/Host/Staff context. |
| Intent / observed fact | Protect Unit × Time for owner use, maintenance/unusable condition or legitimate accommodation. |
| Entry condition | Valid authority, basis, scope and sufficient evidence. |
| Resource scope | Unit × Time, basis type and effective lifetime. |
| Canonical objects | Owner Block, Maintenance Block, Temporary Commitment, Confirmed Accommodation Commitment or External Commitment. |
| Current Inventory truth | Existing truth has been evaluated. |
| Basis / provenance | Decision, actor/capacity, authority, reason/evidence, source and time. |
| Authority required | Explicit capability for the selected basis; report/role/assignment alone is insufficient. |
| Evidence / reason | Owner intent, accepted operational evidence or confirmed accommodation source. |
| Action / domain effect | Establish the correct canonical basis, reject or defer. |
| Commitment / Block effect | New effective Block/Commitment only where policy supports it. |
| Derived Availability effect | Recomputed from effective bases; no manual Availability state. |
| Bookability effect | Contextual and policy-dependent. |
| Affected existing truth | Overlapping truths are preserved. |
| Conflict / exception | Incompatible overlap creates/surfaces Inventory Conflict. |
| Other contexts affected | Host, Guest/Sale, Butler, BQL, Admin and Booking/Stay exception contexts. |
| User-visible outcome | Scoped status indicates effective/intervening/conflicted basis. |
| Handoff | Canonical basis → Availability projection/conflict handling. |
| Correction / release path | Authoritative release, expiry or amendment; history remains. |
| Policy dependency | Basis-specific authority, lifetime, conflict and release policy. |
| TBD / blocker | Exact grant, reason taxonomy, duration and conflict resolver. |
| Source trace | [CP4 Inventory policy](../../05-state-machines-policies/13-inventory-policy.md), [CP7 Inventory model](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md). |

## Phase E — Conflict detection

### B5-E01 — Preserve and surface incompatible overlap

| Field | Specification |
|---|---|
| Actor / Working Context | Inventory Conflict/exception context. |
| Intent / observed fact | Make incompatible legitimate truths visible for authorized resolution. |
| Entry condition | Effective exclusive bases overlap incompatibly. |
| Resource scope | Unit × Time and all overlapping bases. |
| Canonical objects | Inventory Conflict, Commitments/Blocks, Booking, External Accommodation, Stay. |
| Current Inventory truth | Both/all legitimate truths remain recorded. |
| Basis / provenance | Every source, actor, authority, evidence and timestamp retained. |
| Authority required | Conflict visibility/handling; resolution only where explicit policy/authority exists. |
| Evidence / reason | Overlap calculation and supporting records. |
| Action / domain effect | Record/surface conflict; do not choose winner. |
| Commitment / Block effect | No silent overwrite, cancellation or deletion. |
| Derived Availability effect | Availability is uncertain/conflicted or constrained per canonical projection; no invented state. |
| Bookability effect | Not safely inferred; actor-specific action may be blocked or unresolved. |
| Affected existing truth | Booking, External Accommodation, Stay, Blocks and Commitments remain intact. |
| Conflict / exception | Inventory Conflict is the exception itself; no channel priority. |
| Other contexts affected | Host, Guest/Sale, Butler/BQL, Admin, Booking/Stay exception owners. |
| User-visible outcome | Relevant conflict/uncertainty is disclosed only to need-to-know contexts. |
| Handoff | Conflict → authorized exception/policy resolution. |
| Correction / release path | Resolution/correction adds new authoritative fact; no destructive deletion. |
| Policy dependency | Conflict/reconciliation, cancellation/refund/relocation and privacy policies. |
| TBD / blocker | Winner/remediation/compensation and source priority are unresolved. |
| Source trace | [CP4 Inventory model](../../05-state-machines-policies/01-inventory-commitment-model.md), [B4 protection](../b4-stay-operations/12-inventory-relationship.md). |

## Phase F/G — Derived Availability and contextual projection

### B5-F01 — Project derived Availability and Bookability context

| Field | Specification |
|---|---|
| Actor / Working Context | Inventory projection consumed by Public Marketplace, Host, Sale, Guest, Butler, BQL and Admin. |
| Intent / observed fact | Show truthful effects of effective bases without exposing internal evidence. |
| Entry condition | Basis is effective, corrected, released or conflicted. |
| Resource scope | Unit × Time and actor/context relationship. |
| Canonical objects | Effective Commitments/Blocks, derived Availability, Searchability, Bookability. |
| Current Inventory truth | Derived from canonical bases, not a command flag. |
| Basis / provenance | Source/effective lifetime remains available to authorized contexts. |
| Authority required | Read/projection scope; no mutation from visibility. |
| Evidence / reason | Effective basis calculation and confidence/freshness where canonical. |
| Action / domain effect | Recompute/project Availability; contextual Bookability remains separate. |
| Commitment / Block effect | No new basis. |
| Derived Availability effect | Relevant range becomes constrained, Available or uncertain according to effective truth. |
| Bookability effect | May remain unavailable/not Bookable despite derived Availability. |
| Affected existing truth | None silently changed. |
| Conflict / exception | Conflicted/stale truth remains explicit. |
| Other contexts affected | Public, Guest, Sale, Host, Butler, BQL, Admin. |
| User-visible outcome | Need-to-know Availability/uncertainty; no private evidence/authority dump. |
| Handoff | Projection → booking/stay/operations exception where relevant. |
| Correction / release path | New correction/release recomputes projections with history. |
| Policy dependency | Disclosure, freshness, eligibility and Bookability policy. |
| TBD / blocker | Exact stale/conflict wording and actor-specific eligibility. |
| Source trace | [CP8-A semantics](../05-ux-language-semantics.md), [B3 Bookability](../b3-direct-guest-booking/09-tbd-policy-register.md), [CP4 Inventory](../../05-state-machines-policies/01-inventory-commitment-model.md). |

## Phase H/I — Release and downstream exception

### B5-H01 — Correct/release basis and hand off affected truth

| Field | Specification |
|---|---|
| Actor / Working Context | Authorized basis owner/Inventory context and relevant Booking/Stay exception context. |
| Intent / observed fact | End, correct or supersede an intervention without losing history. |
| Entry condition | Basis is no longer required, wrong, expired or corrected by authority. |
| Resource scope | Original Unit × Time and affected commitments/Bookings/Stays. |
| Canonical objects | Block/Commitment, correction/release, Conflict, Booking, External Accommodation, Stay. |
| Current Inventory truth | Existing basis remains effective until authoritative end/correction. |
| Basis / provenance | Original and replacement/release source, actor, authority, reason, time. |
| Authority required | Authority to end/change the original basis; downstream exception owners for affected commerce/Stay. |
| Evidence / reason | Maintenance resolved, Owner change, expiry, wrong Unit/range or reconciliation decision. |
| Action / domain effect | Release/amend/supersede basis; notify/route downstream exception. |
| Commitment / Block effect | Effective constraint ends/changes only according to authoritative rule. |
| Derived Availability effect | Recomputes; may become Available. |
| Bookability effect | Still subject to publication, eligibility, authority and policy. |
| Affected existing truth | Booking/External/Stay are not silently cancelled/deleted. |
| Conflict / exception | Existing affected truth routes to Booking/Stay/Guest/Host exception process. |
| Other contexts affected | Public/Sale/Guest/Host/Butler/BQL/Admin and domain owners. |
| User-visible outcome | Corrected/released/conflicted status with scoped explanation. |
| Handoff | Updated Inventory truth → contextual projections / exception owners. |
| Correction / release path | Amendment, supersession, replacement or explicit release; no destructive delete. |
| Policy dependency | Release/expiry, conflict, Booking/Stay exception, privacy and notification. |
| TBD / blocker | Cancellation/refund/relocation/compensation and late correction behavior. |
| Source trace | [CP4 Inventory policy](../../05-state-machines-policies/13-inventory-policy.md), [B4 correction](../b4-stay-operations/14-correction-historical-truth.md). |

