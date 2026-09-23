# B2 — Alternative, Failure and TBD Boundaries

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Situation | Known truth | Classification | Safe behavior | Not decided |
|---|---|---|---|---|
| External report arrives from Host/Owner/authorized Co-host | Relationship may support reporting; authority scope still matters. | SUPPORTED + authority boundary | Preserve reporter/capacity/source and evaluate. | Exact grants/evidence. |
| Ordinary Sale reports an External Booking | Sale may report/submit; report alone does not change Inventory Truth. | SUPPORTED | Keep pending until explicit authority/evaluation. | Processing workflow. |
| Report lacks authority | Identity/relationship is not authority. | SUPPORTED + TBD handling | Preserve report as unresolved; do not establish commitment. | Escalation/reassignment. |
| Report lacks provenance/evidence | External fact cannot be trusted by entry alone. | POLICY TBD | Keep source/confidence unresolved; no automatic Inventory/Stay. | Threshold/reviewer. |
| Wrong Bookable Unit | Inventory is Unit × Time; wrong Unit cannot protect the intended Unit. | WORKFLOW/POLICY TBD | Flag for correction; do not silently move or rewrite. | Amendment and conflict handling. |
| Wrong dates/range | Commitment and Stay require a truthful range. | WORKFLOW/POLICY TBD | Preserve submitted history; request correction; no silent overwrite. | Date correction/release. |
| Duplicate report | Same external fact may be submitted more than once. | WORKFLOW TBD | Preserve provenance and identify possible duplicate; do not double-commit. | Deduplication/canonical merge. |
| Correction/amendment/source change | CP7 prefers amendment, supersession, replacement or correction. | SUPPORTED principle + policy TBD | Add replacement/correction truth; retain original. | Exact operational procedure. |
| External fact conflicts with Stayora Booking | Both truths/commitments must be preserved. | POLICY TBD | Surface Inventory Conflict; no automatic winner/cancel. | Resolution, Guest remediation, economics. |
| External fact conflicts with Temporary Commitment | Temporary commitment and external fact both retain evidence. | POLICY TBD | Surface conflict; revalidate/authorized resolution. | Priority, expiry and compensation. |
| External fact conflicts with Owner Block | Owner Block is separate Inventory Commitment. | POLICY TBD | Preserve both and surface conflict. | Whether block is corrected/released. |
| External fact conflicts with Maintenance Block | Maintenance Block is separate operational restriction. | POLICY TBD | Preserve both; do not assume accommodation is safe/available. | Resolution and operational response. |
| External fact conflicts with another external fact | No channel/source priority is canonical. | POLICY TBD | Preserve both sources and conflict context. | Resolution/winner/remediation. |
| Guest details incomplete | Operational data minimum is not fully specified. | PRIVACY/WORKFLOW TBD | Represent only what is supported; do not invent identity/vehicle data. | Required fields and access consequences. |
| Stay already started before registration | External fact may arrive late. | SUPPORTED principle + policy TBD | Preserve source/time; represent current operational truth if authority/evidence support it. | Late registration and current-state handling. |
| Stay completed before registration | Historical external Stay may still be represented for coverage/evidence. | SUPPORTED principle + policy TBD | Record historical fact/Stay without fake Booking or automatic commission. | Completion evidence/review eligibility. |
| Integration information delayed/uncertain | No integration or realtime SLA is canonical. | POLICY/INTEGRATION TBD | Preserve delayed/UNKNOWN status and provenance. | Sync health, thresholds, retries. |
| Report withdrawn/corrected | Historical input should not disappear destructively. | SUPPORTED principle + policy TBD | Record correction/supersession and recompute downstream truth only through authority. | Release/correction side effects. |

## Boundary method

For every unresolved branch: **known fact → policy boundary → open question → downstream behavior not finalized**. Independent happy-path operations may continue without solving the branch.


## Current FD closure overlay

FD-08/09 close Inventory conflict responsibility/no-universal-precedence architecture; FD-12 closes External Accommodation Recording Authority; FD-15/16 close the Emergency Protective Hold architecture for serious operational evidence. Evidence standards, reconciliation procedure, privacy and commercial detail remain TBD. The historical rows above are preserved.
