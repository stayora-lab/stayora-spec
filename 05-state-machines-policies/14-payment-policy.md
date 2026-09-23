# Payment Policy

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

Payment Policy determines obligations and consequences. A payment transaction is evidence of processing, not direct Booking cancellation authority.

Conceptually, Payment Default requires: obligation due + required amount unsatisfied + deadline passed + no valid extension/change/cancellation + no unresolved qualifying transaction + applicable reconciliation/grace completed. FAILED Attempt ≠ Payment Default. UNKNOWN ≠ FAILED; unresolved qualifying UNKNOWN blocks automatic default. Exact reconciliation/grace duration remains **TBD**.

Oceanami configuration: more than 24h before Check-in uses 50% Initial Payment and 50% Remaining Balance due T-24h; at or inside 24h, 100% is required for the Required Payment Condition. T-48h is Payment Assurance; T-24h is the Commercial Commitment Checkpoint, not primarily an anti-Sale rule. Butler is not the primary debt collector. Booking Payment and Security/Damage Deposit are separate. Refund is a separate event. Terms/schedules require transaction snapshot and audit. Exact forfeiture/refund/commission consequences remain **TBD**.
