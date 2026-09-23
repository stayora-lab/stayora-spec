# Settlement and Payout

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

Normal path:

```text
STAY COMPLETED → Economic Eligibility → RECONCILING → READY → SETTLED
```

Exception path:

```text
Policy-driven Economic Eligibility → RECONCILING → READY → SETTLED
```

Settlement determines entitlement. Payout fulfills entitlement. Payout lifecycle:

```text
PENDING → PROCESSING → SUCCEEDED
                   ↘ FAILED
                   ↘ UNKNOWN
```

One Settlement may create multiple payout obligations. `SETTLED` is terminal Settlement truth; payout failure does not revert it. Payment Received ≠ Booking Confirmed ≠ Stay Completed ≠ Settlement Eligible ≠ Settled ≠ Paid. A fully paid/commercially fulfilled no-use commitment may follow an exception path without falsifying Stay as Completed.

These are conceptual lifecycle paths. `UNKNOWN` is unresolved payout-provider truth, not equivalent to `FAILED`; exact retry/reconciliation rules remain TBD. Settlement states describe entitlement determination, while Payout states describe execution and do not rewrite terminal Settlement truth.
