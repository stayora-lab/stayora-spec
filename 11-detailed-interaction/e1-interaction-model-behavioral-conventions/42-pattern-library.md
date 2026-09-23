# Interaction Convention Pattern Library

Each pattern follows: **Purpose · Used when · Canonical truth · Intent · Authority · Preconditions · Revalidation · Outcomes · Recovery · Handoff · Provenance · Policy dependencies**.

| Pattern | Canonical use | Behavioral summary |
|---|---|---|
| Read / Inspect | Property, Stay, Request | show current scoped truth; stale may be safe to view |
| Context Change | Host → Sale | reproject and re-evaluate; no permission grant |
| Resource Change | Property A → B | change scope; re-evaluate authority |
| Create Request / Intent | Guest/Sale Request | record intent; downstream authority decides |
| Consequential Decision | accept/reject Request | show truth/capacity, revalidate, record outcome |
| Authoritative Recording | External Accommodation | authority + provenance; reconcile conflicts |
| Operational Recording | readiness/Incident | record evidence; no automatic consequence |
| Inventory Intervention | Block/commitment | basis + authority + revalidation; derive Availability |
| Check-in | Butler/authorized ops | Arrival and readiness distinct; record milestone/action |
| Checkout | Butler/authorized ops | not Completion or Inventory release |
| Incident Reporting | Butler/BQL/Host | evidence → escalation; no blame/Block automatic |
| Correction | fact/evidence | preserve original; establish effective correction |
| Revocation / Relationship Change | access/assignment | attributable authority change; future action scope changes |
| Manual-Assisted Handoff | policy/conflict | known truth → responsibility → human result |
| Conflict Handling | Inventory/external/claim | preserve evidence; no silent winner |
| Unknown Outcome | Payment Attempt | unresolved truth; no duplicate retry |
| Reconciliation | Admin/Money/external | inspect evidence; canonical correction/supersession |
| Partial Context | onboarding/assignment | distinguish pending/no scope/no authority |
| Attention | pending/conflict/exception | projection of domain fact; no generic Task |
| Cross-Context Handoff | Sale→Host, Host→Guest/Ops | object/scope/provenance preserved; authority stays local |

These are behavioral cards, not technical command classes or screen designs.
