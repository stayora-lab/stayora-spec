# B3 — Alternative and Failure Boundaries

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

For each branch, B3 records known truth first and leaves unresolved downstream behavior open.

| Situation | Known truth | Classification | Safe B3 behavior | Not decided |
|---|---|---|---|---|
| No suitable supply | Discovery cannot find a fit. | SUPPORTED | End/continue discovery; do not create Request or Booking. | Ranking and alternate-market behavior. |
| Searchable but unavailable | Public supply exists; derived Availability blocks the range. | SUPPORTED | Explain unavailable/offer re-evaluation; no reservation. | Exact alternative UI/message. |
| Available but not Bookable | Availability does not establish actor/action eligibility. | POLICY / AUTHORITY TBD | Keep distinction visible; do not create unauthorized Request. | Eligibility reason and routing. |
| Availability stale/unknown | Canonical Inventory truth is uncertain. | POLICY TBD | Surface uncertainty and revalidate where supported. | Threshold, retry and promise behavior. |
| Availability changes before Request | Guest intent has not created commitment. | SUPPORTED | Re-evaluate; no automatic reservation or false confirmation. | Revalidation interaction. |
| Availability changes after Request | Request is separate from Inventory. | POLICY TBD | Preserve Request and conflict truth; follow existing policy. | Conflict winner/remediation. |
| Request data incomplete | Request minimum/consent is not satisfied. | WORKFLOW / PRIVACY TBD | Do not create misleading Request; allow correction/stop. | Exact minimum and consent evidence. |
| Request rejected | Authorized Host declines. | SUPPORTED | Request becomes rejected; Guest may return to discovery. | Reason, appeal and recommendations. |
| Request unanswered | No canonical answer is available by a deadline. | POLICY TBD | Preserve pending truth; no invented SLA, auto-reject or auto-reassign. | Timeout and escalation. |
| Booking Authority missing/revoked | Identity/relationship does not supply authority. | AUTHORITY GAP | Do not accept/reject as authorized; surface exception. | Resolution/reassignment. |
| Inventory conflict | Multiple commitments/facts overlap. | POLICY TBD | Preserve evidence and surface conflict; no source/channel winner. | Priority, release and remediation. |
| Payment not initiated | Required condition is unmet. | SUPPORTED + policy | Do not confirm Booking. | Expiry and notifications. |
| Payment `INITIATED` / `PROCESSING` | Provider outcome is incomplete. | SUPPORTED | Keep attempt state; do not confirm or default. | Polling/reconciliation. |
| Payment `FAILED` | Attempt failed. | SUPPORTED + policy | Preserve failure; do not confirm. | Retry, expiry and refund behavior. |
| Payment `UNKNOWN` | Outcome is unresolved. | SUPPORTED | Preserve `UNKNOWN`; do not silently fail, default, release or confirm. | Reconciliation and time boundary. |
| Payment `SUCCEEDED`, other condition fails | Payment is only one confirmation input. | SUPPORTED | Preserve payment and blocked confirmation; no Booking. | Refund/hold/exception handling. |
| Guest abandons Request | Guest intent stops. | WORKFLOW TBD | Preserve truthful Request history; no silent confirmation. | Withdrawal semantics. |
| Duplicate Request | Multiple requests may express same demand. | WORKFLOW TBD | Do not double-reserve or double-confirm; preserve provenance. | Deduplication/merge. |
| Guest loses browser/session | Interaction continuity is interrupted. | UX / AUTH TBD | Preserve Request/Payment/Booking truth independently of session. | Recovery mechanism. |
| System/integration uncertainty | Supporting provider or signal is delayed. | INTEGRATION TBD | Preserve uncertainty and audit evidence. | Retry/SLA/reconciliation. |
| Booking cannot be confirmed | One or more conditions fail. | SUPPORTED | Do not create pre-confirmation Booking; retain relevant Request/payment truth. | Guest remediation/economics. |

## Boundary method

**Known truth → policy boundary → open question → downstream behavior not finalizable.** Independent discovery, Request review and operations analysis may continue without silently closing a blocked branch.
