# Money and Financial History

> Status: **SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL; NOT IMPLEMENTATION FREEZE**

Keep Commercial Truth, Payment Truth, Economic Entitlement, Settlement and Payout separate. Booking Confirmation preserves a Commercial Snapshot; current listing price must not rewrite historical price. Commercial Adjustments preserve funding/economic attribution. Sale-funded discount does not silently reduce Owner entitlement.

Transactional money uses exact integer minor units and controlled currency; no FLOAT/REAL/DOUBLE. V0 Booking has one canonical commercial/settlement currency. Payment Obligation ≠ Payment Transaction; one obligation may have multiple attempts/transactions. UNKNOWN is first-class unresolved provider truth. Required Payment Condition remains separate from Payment Obligation.

Economic Entitlement is first-class historical truth. Pending may become Earned or Not Earned; Earned correction uses Adjustment/Reversal. Settlement reconciles entitlement; Payout fulfills it. Successful payout is historical cash movement and is not rewritten. Refund executor ≠ economic bearer; preserve amount, executor, bearer(s), reason, provenance and related effects.

Security/Damage Deposit is separate from accommodation value, CBV and revenue. Add-ons do not automatically belong to accommodation CBV. External Accommodation does not require fake financial records. Provider operations need idempotency/uniqueness protection.

Exact CBV, payment allocation, refund family, cancellation/default/no-show and supplier-failure economics remain open.
