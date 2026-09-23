# B5 — Domain, Workflow and Authority Gap Findings

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Classification | Observed need | Existing canonical concept | Why insufficient | Affected phase/actors | Impact | Evidence | Recommended escalation |
|---|---|---|---|---|---|---|---|
| AUTHORITY GAP | Owner requests a Block over Unit × Time. | Owner/Host authority and Inventory capability. | Identity/ownership does not specify exact grant/precedence. | A–D · Owner/Host/Inventory | Unauthorized override risk. | CP3/CP4 | Decide scope/grant; no universal Owner precedence. |
| WORKFLOW GAP | Operational signal must be assessed before Block. | Incident/report + Maintenance Block. | Assessment/decision flow is not fully specified. | A/B/D · Butler/BQL/Host/Staff | Incident could mutate Inventory accidentally. | CP7/B4 | Define handoff later; retain separation. |
| POLICY GAP | Multiple effective bases overlap. | Inventory Conflict. | Resolver/remediation is TBD. | C/E/I · Inventory/Booking/Stay | Silent cancellation or winner risk. | CP4 Inventory policy | Founder/policy decision; no priority. |
| DOMAIN GAP | Need to express corrected/released basis with history. | Provenance/temporal history and corrections. | Exact projection/recalculation semantics open. | H · Inventory/Admin | Destructive overwrite/drift risk. | CP7 provenance | Define correction policy; no new entity here. |
| POLICY GAP | Block ending may restore Availability but not Bookability. | Derived Availability and actor-specific Bookability. | Eligibility/publication policy incomplete. | F/G · Public/Sale/Guest | False bookability promise. | CP8-A/B3 | Define contextual projection rules. |
| WORKFLOW GAP | Existing Booking/Stay/External truth is affected. | Domain-owned exception paths. | No single B5 remedy authority. | I · Booking/Stay/External | Accidental cancellation/refund/removal. | CP5/CP7/B4 | Route to owning policy; no B5 remedy. |
| V0-SCOPE GAP | Need operational support without maintenance suite. | Manual-assisted V0 operations. | Exact manual boundary remains open. | A–I · Operations | Scope creep/ERP behavior. | CP5 | Keep manual-assisted; defer automation. |

These are escalation points, not new aggregates, entities, states, permissions or maintenance software.


## Current FD closure overlay

The historical gaps remain valid as procedure/policy detail. FD-08/09, FD-10/11, FD-12, FD-13/14 and FD-15/16 close the corresponding architecture gaps; no universal Owner/Maintenance/External priority or Admin override is inferred.
