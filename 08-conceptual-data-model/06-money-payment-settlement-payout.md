# Money, Payment, Settlement and Payout

> Status: **STABLE — CP7 ARCHITECTURE REVIEWED; NOT IMPLEMENTATION FREEZE**

Keep separate: Commercial Snapshot, Payment Obligation, Payment Attempt/Transaction, Economic Entitlement, Adjustment, Settlement and Payout. Payment answers what money is due or moved; economics answers who is entitled to what. Cash custody does not determine economic ownership or revenue.

At confirmation, preserve the Commercial Snapshot. Example: Public Price 10m, Sale-funded discount -0.3m, Guest Booking Price 9.7m. Do not rewrite Public Price as 9.7m; preserve funding attribution. A lower Guest price does not itself determine whose entitlement is reduced.

Payment Obligation and Payment Attempt are separate; one obligation may have multiple attempts. Attempt direction is `INITIATED → PROCESSING → SUCCEEDED / FAILED / UNKNOWN`; UNKNOWN is unresolved provider truth and not automatic failure/default. Required Payment Condition is separate and evaluates whether a specific commercial action may proceed.

Economic Entitlement derives from Commercial Snapshot, Economic Policy, qualified outcome, adjustments and responsibility/exception handling. Sale base distribution commission remains CONFIRMED at 10% of Commissionable Booking Value; exact CBV rules remain TBD. Entitlement direction is `PENDING → EARNED → PAID` or `PENDING → NOT_EARNED`; later correction uses Adjustment/Reversal and never rewrites Earned history.

Settlement determines entitlement; Payout fulfills it. Settlement may be READY while Payout is pending. Wrong payout is corrected through new recovery/offset truth, not by rewriting successful historical movement. Refund preserves amount, executor, economic bearer(s), reason, provenance and related adjustments. Security/Damage Deposit and Add-ons are separate economics and are not automatically Booking Value, CBV or Stayora Revenue.
