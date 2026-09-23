# B4 — TBD and Policy Register

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| ID | Known truth | Open policy/question | Downstream behavior not finalizable | Classification |
|---|---|---|---|---|
| B4-T01 | Stay has a legitimate Accommodation Basis. | Who may establish Stay from which external evidence? | External Stay creation and review. | DOMAIN / AUTHORITY TBD |
| B4-T02 | `SCHEDULED` is the pre-Check-in state. | Exact operational readiness criteria/owner? | Readiness projection and escalation. | POLICY TBD |
| B4-T03 | READY is not a core Stay state. | How should destination-specific readiness be shown? | Contextual projections/copy. | UX TBD |
| B4-T04 | Arrival is an event/observation. | What evidence and actor scope records physical arrival? | Arrival/check-in handoff. | WORKFLOW / AUTHORITY TBD |
| B4-T05 | Check-in is a canonical transition. | Preconditions, authorized actors and access/compliance blockers? | Check-in and exception behavior. | STATE / POLICY TBD |
| B4-T06 | Payment is separate from Stay. | Can an applicable unpaid/unknown condition block Check-in? | Cross-domain blocking/escalation. | POLICY / LEGAL TBD |
| B4-T07 | Butler is operational, not commercial. | Exact assignment grants, replacement and escalation? | Preparation, Check-in/out, Incident work. | AUTHORITY TBD |
| B4-T08 | BQL is destination/function scoped. | Exact data fields/retention/local integrations? | Access, registration and service projections. | DESTINATION / PRIVACY TBD |
| B4-T09 | Incident ≠ Finding ≠ Responsibility ≠ Consequence. | Thresholds and owners for downstream cases? | Quality, blame, compensation and consequences. | POLICY TBD |
| B4-T10 | Checkout precedes completion. | Which unresolved conditions block `COMPLETED`? | Completion timing and follow-up. | POLICY TBD |
| B4-T11 | `DID_NOT_OCCUR` is pre-Check-in/final-policy outcome. | Exact evidence/disposition rule? | No-use handling. | STATE / POLICY TBD |
| B4-T12 | Inventory is commitment-derived. | Which operational events may trigger separate Blocks? | Availability effects and B5 scope. | INVENTORY POLICY TBD |
| B4-T13 | Historical truth uses correction/supersession. | Visibility and downstream recalculation rules? | Projections, audits and cases. | DATA / POLICY TBD |
| B4-T14 | Post-stay domains own their outcomes. | Review Right, Reputation, Verification, Settlement timing? | Eligible follow-up. | DOMAIN / POLICY TBD |

No row is a new requirement, state, aggregate or permission.


## Current FD closure overlay

FD-01 closes Check-in/Checkout authority architecture; FD-02/03/04 close Completion semantics and minimal conditions; FD-05 closes DID_NOT_OCCUR authority; FD-06/07 close Guest access architecture. Credential mechanics, exact grants, Incident procedure/consequence, no-show effects, privacy, retention and connectivity remain TBD. Historical rows are retained.
