# B5 — TBD and Policy Register

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| ID | Known truth | Open question | Downstream behavior not finalizable | Classification |
|---|---|---|---|---|
| B5-T01 | Availability is derived from effective Commitments/Blocks. | Exact interval/freshness/projection policy? | Stale and boundary-date behavior. | POLICY TBD |
| B5-T02 | Owner Block is distinct basis. | Exact Owner/Host grant, scope, reason and precedence? | Establish/change/release action. | AUTHORITY / POLICY TBD |
| B5-T03 | Maintenance Block requires authorized decision. | Who assesses, what evidence and which capability? | Operational-to-Inventory handoff. | AUTHORITY / WORKFLOW TBD |
| B5-T04 | Incident/report does not create Block. | When may an operational signal become a Block? | Block creation, severity and escalation. | POLICY TBD |
| B5-T05 | Conflicts preserve legitimate truths. | Who resolves and what remedy is allowed? | Winner, cancellation, refund, relocation, compensation. | POLICY / LEGAL TBD |
| B5-T06 | Temporary/Confirmed/External Commitments differ. | Exact coexistence/prevention and effective-end rules? | Commitment creation/release. | POLICY TBD |
| B5-T07 | Block release may restore derived Availability. | What evidence ends/corrects a Block? | Recompute timing and disclosure. | POLICY / WORKFLOW TBD |
| B5-T08 | Availability ≠ Bookability. | Exact re-publication/eligibility after release? | Actor-specific actions. | MARKETPLACE TBD |
| B5-T09 | Existing Booking/Stay/External truth is protected. | Which downstream exception policies exist? | Cancellation/refund/relocation/support. | FOUNDER / POLICY TBD |
| B5-T10 | Corrections preserve history. | Late/retroactive correction recalculation and visibility? | Historical projections/audit. | DATA / POLICY TBD |
| B5-T11 | Butler/BQL report operational facts. | Exact Inventory read/report grants and escalation? | Destination operations. | AUTHORITY TBD |
| B5-T12 | Manual-assisted conflict handling is V0-compatible. | Which automation is deferred versus required? | V0 implementation scope. | V0-SCOPE TBD |

No row is a new requirement, state, aggregate, permission or priority rule.


## Current FD closure overlay

FD-08/09 close conflict responsibility and the explicit absence of universal precedence; FD-10/11 close Temporary Commitment lifecycle/release architecture; FD-12 closes External Recording Authority; FD-13 closes Owner Block authority; FD-14 closes Maintenance Block authority; FD-15/16 close Emergency Protective Hold architecture. Concrete durations, evidence standards, case remedies, Bookability, retention and operating procedures remain TBD. Historical rows are retained.
