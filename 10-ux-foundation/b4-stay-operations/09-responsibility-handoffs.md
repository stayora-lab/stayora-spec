# B4 — Responsibility Handoffs

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| From | To | Trigger | Canonical object/state | Authority basis | Information transferred | Responsibility transferred | Evidence | Failure condition | Policy dependency | TBD |
|---|---|---|---|---|---|---|---|---|---|---|
| Accommodation Basis | Stay Operations | Basis/evidence sufficient | Stay `SCHEDULED` | Stay recording authority | Unit, range, party, provenance, operational minimum | Prepare a legitimate Stay | Basis/source/actor/time | Insufficient basis/evidence | Stay creation/provenance/privacy | Threshold and external recording |
| Host / Stay | Butler | Assignment and upcoming Stay | Stay `SCHEDULED` | Butler assignment/function scope | Need-to-know arrival, access, unit, issues | Prepare/coordinate | Assignment and preparation evidence | No assignment/data | Assignment/access policy | Propagation/change |
| Stay | Destination/BQL | Destination-relevant upcoming/current Stay | Stay and operational projection | Destination staff function scope | Occupancy, arrival/departure, access, services | Coordinate destination operations | Access/registration records | Missing scope or data | Destination/privacy policy | Local fields/retention |
| Guest arrival | Check-in context | Arrival/access evidence | Stay `SCHEDULED` | Check-in capability | Arrival, party/access, preconditions | Evaluate and record Check-in | Actual actor/time/evidence | Arrival not sufficient | Check-in/access policy | Exact preconditions |
| Butler / Guest / BQL | Incident context | Operational report/observation | Incident + Stay | Incident report/handling capability | Facts, scope, urgency, evidence | Record, respond, escalate | Original/amended reports | Conflicting/insufficient facts | Incident/privacy/escalation | Severity and owner |
| Check-in | In-stay operations | Stay transition | Stay `CHECKED_IN` | Stay/operational authority | Current Stay/access/issue truth | Support and coordinate | Events/issues | Missing assignment/support | Operations policy | Service expectations |
| Guest departure | Checkout context | Departure/evidence | Stay `CHECKED_IN` | Checkout capability | Departure, condition, unresolved issues | Record Checkout | Time/condition/access evidence | Early/late/uncertain departure | Checkout/access policy | Exact evidence |
| Checkout | Completion evaluation | Checkout recorded | Stay `CHECKED_OUT` | Completion authority | Completion readiness, exceptions, history | Determine `COMPLETED` or follow-up | Completion basis | Open qualifying blocker | Completion policy | Blocker list/timing |
| Completion | Post-stay domains | Stay `COMPLETED` | Stay/Review Right/Incident/etc. | Each domain’s authority | Scoped history and evidence | Eligible review/quality/follow-up | Provenance/history | Domain eligibility absent | Review/Quality/Money policy | Timing and consequences |

No handoff transfers commercial authority merely because an operational projection is shared.
