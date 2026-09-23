# Payment lifecycle

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

Payment is not one giant state machine. Separate financial obligation from transaction processing:

```text
Payment Obligation / Intent → Payment Attempt(s) → Provider Transaction(s)
```

Payment Attempt lifecycle:

```text
INITIATED → PROCESSING → SUCCEEDED
                      ↘ FAILED
                      ↘ UNKNOWN
```

`UNKNOWN` is first-class and is not `FAILED`. Obligation truth is conceptually `Amount Due − Valid Collections + Refund effects ± Authorized Adjustments`. Unpaid/partial/paid/overpaid are derived labels, not transaction states.

The lifecycle above is a conceptual attempt/outcome model, not a complete provider transition graph. UNKNOWN is unresolved provider truth and remains subject to reconciliation; it must not be treated as a normal terminal failure or used as automatic Payment Default.

Booking Confirmation requires applicable Booking Confirmation Conditions. Required Payment Condition may be less than 100%; Payment Received ≠ Booking Confirmed and Payment Received ≠ Fully Paid. Booking Deposit and Security/Damage Deposit have separate economics and lifecycles. Refund is a separate economic event and does not rewrite an original successful payment.
