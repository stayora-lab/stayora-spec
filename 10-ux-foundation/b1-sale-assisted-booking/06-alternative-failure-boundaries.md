# B1 — Alternative and Failure Boundaries

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

These branches identify the correct boundary without selecting missing policy. “Supported” means the existing architecture gives a truthful path; “TBD / policy boundary” means the journey cannot specify the final outcome yet.

| Situation | Known truth | Classification | Safe journey behavior | Not decided here |
|---|---|---|---|---|
| No suitable supply | Sale may find no eligible/searchable option fitting the need. | SUPPORTED by existing discovery boundaries | Tell Sale/Guest no suitable current option; continue discovery or stop without Request. | Ranking, alternatives and Lead behavior. |
| Searchable but not Available | Searchability is not Availability. | SUPPORTED | Do not present as available/bookable for the requested dates; continue search or explain constraint. | Copy and ranking. |
| Available but not actor-specific Bookable | Availability does not guarantee Sale transaction eligibility. | SUPPORTED | Keep context/relationship/eligibility check explicit; do not create Request if action is not permitted. | Exact eligibility reason and routing. |
| Availability stale or unknown | Derived Availability may be stale/uncertain; final authority revalidates at commitment. | TBD / policy boundary | Mark uncertainty and revalidate before commitment; do not promise or reserve. | Sync-health thresholds, stale window and UX remediation. |
| Availability changes before Request | Request has not reserved Inventory. | SUPPORTED | Re-evaluate at Request/acceptance; no automatic winner or hidden hold. | Exact conflict outcome. |
| Request rejected | Request lifecycle supports `REJECTED`; no Booking exists. | SUPPORTED | Show rejected/pending alternate path; do not charge or create Stay. | Rejection reason, appeal and alternate-supply behavior. |
| Request unanswered | Request can remain pending; no timeout/SLA is confirmed. | TBD / policy boundary | Keep responsibility/action-required visible without inventing expiry or auto-rejection. | Notification, timeout, escalation and expiry. |
| Missing Host authority | Sale role does not authorize acceptance; authority must resolve. | SUPPORTED + TBD details | Route to valid Host/Co-host authority or exception; do not auto-accept/reject. | Authority precedence and reassignment. |
| Inventory conflict | Preserve both facts/commitments and surface conflict; no channel priority. | TBD / policy boundary | Stop confirmation branch, show unresolved conflict and owner of next decision. | Winner/remediation, guest outcome and compensation. |
| Payment required but not initiated | Required Payment Condition is unmet; Booking does not exist. | SUPPORTED + TBD expiry | Keep Request/commitment pre-confirmation and show required action where policy supports. | Deadline, expiry, grace and release. |
| Payment succeeds | Attempt may be `SUCCEEDED`; condition still needs evaluation with all confirmation conditions. | SUPPORTED | Continue confirmation evaluation; do not equate Payment Received with Booking. | Partial/late payment mechanics. |
| Payment fails | Attempt `FAILED`; not automatically Booking cancellation/default. | SUPPORTED + TBD consequences | Keep no-confirmation truth and route to policy-supported retry/assistance. | Retry, expiry, refund/default. |
| Payment uncertain | Attempt `UNKNOWN`; unresolved provider truth. | SUPPORTED + TBD reconciliation | Surface uncertainty; do not label failure, Payment Default, cancellation or release automatically. | Reconciliation, grace and responsible actor. |
| Payment requirement not satisfied by deadline | Payment Obligation may remain due; Required Payment Condition is action-specific. | TBD / policy boundary | Do not confirm; hold the unresolved policy branch and retain provenance. | Payment Default, grace, cancellation, refund and commitment release. |
| Guest abandons before Request | No Request/Booking needs to be created. | SUPPORTED | Stop with no commercial commitment; preserve only already-authorized records. | Lead closure/retention. |
| Guest abandons after Request | Request remains its own lifecycle; no silent cancellation policy. | TBD / policy boundary | Show current Request truth and any required next action; do not invent Guest cancellation. | Request withdrawal/expiry and commitment release. |
| Booking cannot confirm | One or more confirmation conditions fail or remain unresolved. | SUPPORTED + TBD branch | Keep Booking absent; show condition category and route to responsible context. | Remediation, re-request, expiry and economics. |
| System/integration uncertainty | Provider, sync or destination integration may not establish authoritative truth. | TBD / policy boundary | Preserve UNKNOWN/exception and provenance; manual assistance may resolve without overwrite. | Retry, reconciliation SLA and fallback. |

## B1 rule

No failure branch turns a Request into a Booking, turns a Sale into an accepting authority, or turns an uncertain payment/inventory result into a confirmed truth by convenience.
