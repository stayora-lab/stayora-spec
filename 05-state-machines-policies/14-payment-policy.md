# Payment Policy

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

Payment Policy determines obligations and consequences. A payment transaction is evidence of processing, not direct Booking cancellation authority.

Conceptually, Payment Default requires: obligation due + required amount unsatisfied + deadline passed + no valid extension/change/cancellation + no unresolved qualifying transaction + applicable reconciliation/grace completed. FAILED Attempt ≠ Payment Default. UNKNOWN ≠ FAILED; unresolved qualifying UNKNOWN blocks automatic default. Exact reconciliation/grace duration remains **TBD**.

Oceanami configuration values are recorded in [13-destination-operations/oceanami/configuration.md](../13-destination-operations/oceanami/configuration.md) (decision: [ADR-P061](../00-start-here/DECISIONS.md#adr-p061)). Butler is not the primary debt collector. Booking Payment and Security/Damage Deposit are separate. Refund is a separate event. Terms/schedules require transaction snapshot and audit. Exact forfeiture/refund/commission consequences remain **TBD**.
