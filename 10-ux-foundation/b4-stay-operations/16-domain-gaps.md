# B4 — Domain, Workflow and Authority Gap Findings

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Classification | Observed need | Existing canonical concept | Why insufficient | Affected phase/actors | Impact | Evidence | Recommended escalation |
|---|---|---|---|---|---|---|---|
| WORKFLOW GAP | External accommodation must become operationally actionable. | External Accommodation → Stay. | Exact acceptance/evidence workflow is open. | A · Host/Admin/Operations | Fake or unsupported Stay risk. | CP7 Stay; B2 | Decide evidence/authority workflow; no new aggregate. |
| POLICY GAP | Readiness needs a useful signal without a new state. | READY is an operational milestone. | Criteria/owner/projection not fully specified. | C · Butler/Host/BQL | False arrival promise or unclear escalation. | CP4 Stay; CP6 Operations | Define readiness policy later; retain milestone only. |
| AUTHORITY GAP | Arrival observation and Check-in transition differ. | Arrival event; Stay state machine. | Exact Check-in grants/preconditions remain open. | D/E · Guest/Butler/Host | Unauthorized or false Check-in. | CP3/CP4 | Reconcile authority/policy; do not add state. |
| PRIVACY GAP | BQL/Butler need operational data. | Need-to-know scoped projections. | Exact fields/retention/local requirements open. | B–F · Butler/BQL/Guest | Overexposure or operational failure. | CP6/CP8-A | Resolve field-level policy later. |
| POLICY GAP | Incidents may lead to follow-up without blame. | Incident/Quality/Responsibility/Consequence separation. | Thresholds/owner/escalation open. | G · Guest/Host/Butler/Quality | Automatic penalty/reputation risk. | CP4/CP7 | Define case policy; no automatic consequence. |
| STATE-MACHINE GAP | Checkout and completion may be separated by blockers. | `CHECKED_OUT`, Operational Completion Readiness, `COMPLETED`. | Qualifying blocker set is open. | H–J · Stay/Operations | Premature closure or indefinite pending. | CP4/CP7 | Founder/policy decision; no new state. |
| INVENTORY POLICY GAP | Operational unusability may affect future Availability. | Blocks and Inventory authority. | Event-to-Block rule is not defined in B4. | F/G · Butler/Inventory | Accidental availability mutation. | CP5/CP7 | Defer to B5/Inventory policy. |
| V0-SCOPE GAP | Need support without PMS/workforce suite. | Manual-assisted V0 operations. | Exact service/task boundaries open. | B–F · Operations | Scope creep. | CP5/CP6 | Keep manual-assisted and defer advanced tooling. |

These are escalations, not new entities, states, permissions or product decisions.
