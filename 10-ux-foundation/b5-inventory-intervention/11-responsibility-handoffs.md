# B5 — Responsibility Handoffs

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| From | To | Trigger | Object | Authority basis | Information transferred | Responsibility transferred | Evidence | Failure condition | Policy dependency | TBD |
|---|---|---|---|---|---|---|---|---|---|---|
| Owner/Reporter | Authority evaluation | Intent/report submitted | Report/Owner intent | Reporting capability | Actor, capacity, Unit, range, reason/source | Evaluate whether action is authorized | Source/time/reason | Missing identity/scope | Reporting/privacy | Minimum fields |
| Butler/BQL/Guest | Evidence context | Operational problem observed | Incident/report/evidence | Operational/reporting scope | Condition, Unit, range, time, urgency | Preserve observation; no Block authority | Observation/source | Insufficient/conflicting fact | Incident policy | Evidence threshold |
| Evidence | Inventory Authority | Evidence accepted for decision | Assessment/intervention candidate | Explicit Inventory capability | Authority, basis, scope, lifetime, reason | Decide Block/Commitment/correction | Decision/authority/time | No valid authority | Inventory policy | Assessor/grant |
| Inventory decision | Derived Availability | Basis established/changed | Block/Commitment | Basis-specific authority | Effective Unit × Time truth | Recompute/project Availability | Effective basis | Conflict/stale truth | Derived model/freshness | Threshold/projection |
| Conflict | Exception owner | Incompatible overlap | Inventory Conflict | Resolution authority if defined | Both truths/source/evidence | Reconcile/route without winner | Conflict calculation | No resolver | Conflict/Booking/Stay policy | Winner/remediation |
| Correction/release | Context projections | Authoritative end/change | Replacement/release history | End/change authority | Original + replacement/reason/time | Update effective truth/history | Amendment/audit | Revoked authority/late correction | Release/history/privacy | Recalculation |
| Inventory exception | Booking/Stay owner | Existing commerce/Stay affected | Booking, External Accommodation, Stay | Domain-specific authority | Affected commitment, Guest/party, operational impact | Handle cancellation/change/support only under own policy | Basis/conflict | No commercial resolution | Booking/Stay exception policy | Refund/relocation/compensation |

No handoff converts a report into authority or an Inventory conflict into a commercial decision.
