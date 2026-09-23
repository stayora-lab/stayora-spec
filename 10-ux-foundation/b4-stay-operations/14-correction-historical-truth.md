# B4 — Correction and Historical Truth

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Correction principles

Operational records are corrected by an explicit amendment, supersession, replacement or correction record. The original actor, source, timestamp and prior value remain auditable. B4 does not design persistence implementation.

| Correction | Preserve | Safe effect |
|---|---|---|
| Incorrect arrival | Original observation and corrected evidence. | Update operational projection; do not silently Check-in. |
| Incorrect Check-in | Actual actor, authority, time and reason. | Correct/void through owning Stay policy; do not rewrite payment or Booking. |
| Wrong Guest/Staying Party | Original relationship/provenance and corrected basis. | Reconcile access/operations within privacy policy; do not expose unrelated parties. |
| Incorrect Checkout | Original Checkout evidence and correction authority. | Re-evaluate completion; do not release Inventory by convenience. |
| Late operational entry | Source time versus entry time. | Represent current/historical truth without fabricating a Booking or state sequence. |
| Incident correction | Original report, amendment and response history. | Preserve Incident audit; do not turn correction into blame. |
| Assignment change | Prior/current assignment and effective time. | Update responsibility/access scope; do not grant commercial authority. |

## Post-completion boundary

A later complaint or correction may create a follow-up case or history amendment. It does not automatically reopen a Completed Stay. Review, Reputation, Verification, Money and Settlement consume qualifying truth under their own policies.
