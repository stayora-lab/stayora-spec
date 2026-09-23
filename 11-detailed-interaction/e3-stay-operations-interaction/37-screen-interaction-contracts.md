# Screen Interaction Contracts

| Context | Purpose/entry | Truth | Actions | Authority/revalidation | Outcomes/handoff |
|---|---|---|---|---|---|
| GST-01 Stay Hub | scoped Guest Stay before/during/after | Stay, basis, dates, milestones | access/help/review entry | Guest scope; no Check-in authority | pending/checked-in/out/completion |
| GST-02 Arrival & Access | arrival/access | Property/Unit, credential projection | access/help | credential ≠ authority | access issue → operations |
| GST-03 Help/Contact | operational help | Stay/contact need-to-know | contact/escalate | scoped privacy | Butler/Host/BQL |
| HST-07 Stay Detail | Host operations | Stay, basis, milestones, exceptions | coordinate/authorized ops | Host/resource authority | Butler/BQL/Guest handoff |
| HST-11 Butler Coordination | assignment context | Assignment/Stay | coordinate/assign if authorized | explicit grant | Butler |
| BUT-01 Today | field responsibility | assignments/upcoming Stays | select/report | Assignment scope | BUT-02 |
| BUT-02 Assigned Stay | assigned operations | Stay/readiness/Incident | evidence/support | Assignment + action grant | Check-in/Incident/Checkout |
| BUT-03 Check-in | authoritative action | current Stay truth | Check-in | explicit authority + revalidation | checked-in/blocked/unknown |
| BUT-04 Incident | evidence/attention | Incident/Stay/resource | report/escalate | operational scope | Host/BQL/Admin |
| BUT-05 Checkout | authoritative action | current Stay truth | Checkout | explicit authority + revalidation | checked-out/evaluation |
| BQL-01 Today | destination ops | arrivals/departures/active Stays | coordinate/escalate | destination/function scope | Stay/Incident |
| BQL-02/03 | active Stay/Incident context | Stay/Incident | inspect/escalate | scoped | responsible context |
| ADM exception | governance | evidence/provenance | reconcile/assist | staff function/resource | origin context |

No layout, components or copy are specified.
