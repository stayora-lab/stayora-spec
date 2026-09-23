# B5 — Alternative and Failure Boundaries

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Situation | Known truth | Classification | Safe behavior | Not decided |
|---|---|---|---|---|
| Unauthorized Owner/Host request | Identity/ownership alone may not establish action authority. | AUTHORITY TBD | Reject/defer/escalate; no Block. | Exact grant and appeal. |
| Butler reports issue without Inventory Authority | Report is operational evidence. | SUPPORTED | Preserve/evaluate; no automatic Maintenance Block. | Assessor/SLA. |
| BQL reports issue | Destination observation is scoped. | SUPPORTED | Route to authorized Inventory/Host context. | Local escalation. |
| Insufficient evidence | Basis cannot be trusted. | POLICY TBD | Keep pending/uncertain; no Availability mutation. | Threshold/reviewer. |
| Wrong Unit/range | Inventory is Unit × Time. | WORKFLOW TBD | Preserve and correct explicitly. | Correction/impact. |
| Duplicate intervention | Multiple records may express one event. | WORKFLOW TBD | Preserve provenance; avoid double-counting effective constraint. | Dedup/merge. |
| Overlap with confirmed Booking | Booking is protected truth. | POLICY TBD | Preserve and surface conflict; no cancellation. | Commercial remedy. |
| Overlap with External Accommodation | External fact/commitment remains external truth. | POLICY TBD | Preserve source and conflict. | Resolution/remediation. |
| Overlap with active/upcoming Stay | Stay is independent operational truth. | POLICY TBD | Preserve Stay; hand off exception. | Guest/operations remedy. |
| Overlap with another Block | Blocks remain distinct bases. | POLICY TBD | Preserve; project constraints; no winner. | Consolidation/priority. |
| Late intervention entry | Event time may precede record time. | SUPPORTED principle | Record both; evaluate authoritative effective range. | Retroactivity. |
| Maintenance resolves early | Block may end before planned range. | POLICY TBD | Explicit release/correction; no universal Bookability. | Readiness proof. |
| Authority revoked mid-process | Pending action loses basis. | AUTHORITY TBD | Stop/flag; preserve prior truth. | In-flight behavior. |
| Conflicting reports | Facts disagree. | POLICY TBD | Preserve both; investigate; no blame. | Evidence standard. |
| Stale Availability projection | Derived view may lag effective truth. | UX / POLICY TBD | Surface freshness/uncertainty; no manual flag. | Threshold/recompute. |
| Unknown/conflicted truth | No safe winner. | POLICY TBD | Keep conflict/uncertainty visible to authorized contexts. | Resolution/remediation. |

Boundary method: **known truth → policy boundary → open question → downstream behavior not finalizable**.
