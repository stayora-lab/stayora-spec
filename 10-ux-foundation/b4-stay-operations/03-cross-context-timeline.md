# B4 — Cross-Context Timeline

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

This is a conceptual timeline. Operational phases are not automatically lifecycle states.

| Point | Guest | Stay truth | Host / Primary Host | Butler | Destination / BQL | Incident / Quality | Inventory / Commerce |
|---|---|---|---|---|---|---|---|
| Basis established | Sees upcoming Stay where eligible | Accommodation Basis → `SCHEDULED` | Retains hosting responsibility | Receives assigned preparation scope | Receives destination-relevant upcoming occupancy | None unless exception | Provenance retained; no Inventory mutation |
| Pre-arrival | Provides allowed party/arrival information; sees help/access | `SCHEDULED`; Preparation projection | Coordinates readiness and unresolved responsibility | Prepares villa/access; reports evidence | Prepares registration/access/service context | Known issues remain separate | Availability remains commitment-derived |
| Readiness | Receives relevant instructions, not a Check-in promise | Readiness milestone; no `READY` state | Owns/coordinates blocker within authority | May report operational readiness | Consumes destination readiness need-to-know | May receive qualifying issue | No automatic block |
| Expected / physical arrival | Arrives and requests support | Arrival observation; still `SCHEDULED` until authorized Check-in | Supports exceptions | Coordinates arrival/access | Validates destination access/function data | Incident if issue | No release or commitment mutation |
| Check-in | Participates and receives result | `SCHEDULED → CHECKED_IN` when conditions/evidence pass | Sees operational result | May coordinate/record if authorized | Sees destination operational status | Exception if blocked | No payment/Availability transition |
| In-stay | Uses accommodation/help path; reports issue | `CHECKED_IN`; operational events | Fulfils hosting responsibility | Supports and records evidence | Coordinates services/issues | Incident may be opened | No `IN_STAY` state; no automatic Inventory action |
| Incident | Sees own issue status as allowed | Stay unchanged; Incident separate | Receives relevant facts/responsibility | Reports/handles within scope | Handles destination issue scope | Incident → response/escalation | No automatic blame, refund, block or Reputation |
| Departure / Checkout | Follows requirements and departs | Departure observation → `CHECKED_OUT` only with authorized evidence | Reviews operational outcome | Coordinates Checkout/evidence | Updates destination departure context | Open issues remain linked | Checkout does not release Availability by itself |
| Completion | Sees completed outcome when eligible | `CHECKED_OUT → COMPLETED` only when conditions pass; otherwise follow-up | Consumes history | Provides evidence | Retains operational history | Review/Quality may consume qualifying evidence | No automatic Settlement/Payout/Availability |
| Post-stay | May receive Review Right/help/follow-up | Historical Stay and provenance retained | Reviews relevant property history | Assignment/history remains scoped | Destination history retained | Separate Review/Verification/Reputation cases | Commerce/Money consume only independent truth/policy |

## Main invariant

Each lane changes only through its owning domain or an explicitly authorized cross-domain action. A contextual projection never silently becomes a new lifecycle state or authority grant.
