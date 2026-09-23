# B4 — Alternative and Failure Boundaries

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Situation | Known truth | Classification | Safe behavior | Not decided |
|---|---|---|---|---|
| Basis insufficient | Accommodation cannot yet support a truthful Stay. | WORKFLOW / DOMAIN boundary | Preserve pending source/evidence; do not create fake Booking/Stay. | External acceptance threshold. |
| External source lacks authority/evidence | Report is not authoritative operational truth. | AUTHORITY / POLICY TBD | Retain provenance; do not promote silently. | Reviewer/grant/evidence threshold. |
| No Butler assignment | Host operational responsibility remains. | SUPPORTED | Escalate/coordinate without automatic reassignment. | Assignment propagation/SLA. |
| Stay data incomplete | Minimum party/access/arrival data is missing. | PRIVACY / WORKFLOW TBD | Expose only supported data; keep blocker visible. | Required fields and access consequence. |
| Stay is not ready | Preparation condition is unresolved. | POLICY TBD | Report readiness blocker; no `READY` state or false promise. | Readiness threshold/owner. |
| Guest arrives early/late | Arrival observation differs from schedule. | SUPPORTED + policy | Record observation; do not auto Check-in/cancel/Complete. | Local handling and notification. |
| Access fails | Access/credential does not work or is unverified. | DESTINATION / PRIVACY TBD | Escalate through operational support; do not universally deny or grant. | Credential lifecycle/remediation. |
| Arrival but no Check-in | Physical arrival is known; transition evidence/authority absent. | STATE / AUTHORITY boundary | Preserve `SCHEDULED`; resolve authorized Check-in. | Exact preconditions and timeout. |
| Check-in blocked by payment/compliance | Potential cross-domain blocker. | POLICY / LEGAL TBD | Preserve Stay/Payment truth separately; do not make payment a Stay state. | Blocking policy and escalation. |
| Incident reported | Operational issue needs response. | SUPPORTED | Create/route Incident if accepted; preserve evidence. | Severity, owner and escalation. |
| Conflicting Incident reports | Facts are inconsistent. | POLICY TBD | Preserve both and investigate; no automatic blame. | Finding/responsibility standard. |
| Stay becomes unusable | Operational condition may affect future Inventory. | INVENTORY / POLICY TBD | Escalate to separately authorized Block workflow; no Butler auto-block. | Block authority and timing. |
| Guest departs without Checkout | Departure observation exists; Checkout evidence absent. | WORKFLOW / STATE TBD | Preserve `CHECKED_IN`; seek authorized record; no auto-completion. | Evidence and late correction. |
| Checkout with open Incident | Stay is departed; issue remains. | SUPPORTED + policy | Record `CHECKED_OUT`; evaluate completion separately. | Qualifying completion blocker. |
| Open Incident after Checkout | Follow-up remains. | SUPPORTED | Keep Incident separate; do not reopen Stay automatically. | Follow-up and visibility. |
| Completion evidence incomplete | `CHECKED_OUT` but conditions unresolved. | POLICY TBD | Keep completion readiness unresolved; no `COMPLETED`. | Completion criteria/timing. |
| Stay does not occur before Check-in | Accommodation commitment ends legitimately. | SUPPORTED | Use `DID_NOT_OCCUR` only under canonical final policy. | Exact disposition evidence. |
| Corrections arrive late | Original operational fact is wrong/incomplete. | SUPPORTED principle | Amendment/supersession/replacement/correction; preserve history. | Exact procedure and visibility. |

Boundary method: **known truth → policy boundary → open question → downstream behavior not finalizable**.
