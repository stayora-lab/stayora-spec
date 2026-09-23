# Policy architecture

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

State Machine describes what happened to domain truth. Policy determines when an action/transition is allowed and what consequences follow.

```text
CORE INVARIANT → PLATFORM POLICY → DESTINATION CONFIGURATION
```

Override scopes are `CORE_LOCKED`, `PLATFORM_DEFAULT`, `DESTINATION_CONFIGURABLE`, `PROPERTY_CONFIGURABLE`, and `TRANSACTION_SNAPSHOT`.

Examples: Request does not hold Inventory is CORE_LOCKED; an Oceanami QR gate is DESTINATION_CONFIGURABLE; villa Instant Book ON/OFF is PROPERTY_CONFIGURABLE; accepted cancellation/payment terms are TRANSACTION_SNAPSHOT. Configuration may specialize Policy but may not violate Domain Invariants. Commercial terms generally require snapshots; operational policies may be effective-date driven unless contractual rights require snapshots.

Use the scopes as documentation boundaries, not as an invented global precedence engine. Each policy statement should identify its layer/scope where known: CORE_LOCKED invariants cannot be configured; PLATFORM_DEFAULT rules may be specialized by a narrower permitted configuration; DESTINATION/PROPERTY configuration may vary only within those invariants; TRANSACTION_SNAPSHOT preserves the terms accepted for that commercial commitment. Operational rules may use effective dates where appropriate, but cannot silently remove an already-protected contractual right. Where the responsible policy owner, precedence among independently valid authorities, or exact snapshot/effective-date behavior is not confirmed, retain an explicit TBD.

## Eight policy families

1. Booking & Commitment — confirmation, request, Instant Book, change, cancellation, no-show.
2. Inventory — commitment, exclusivity, conflict, expiry/release, external commitment.
3. Payment — Required Payment Condition, schedule, default, refund, security deposit.
4. Settlement & Economics — eligibility, reconciliation, entitlement, commission, affiliate, adjustments, payout.
5. Stay & Operations — check-in/out, arrival/no-arrival, completion, access, evidence.
6. Verification & Reputation — eligibility, assessment, suspension/removal, reviews, computation.
7. Distribution — Sale eligibility, relationships, dispatch/SLA, affiliate attribution.
8. Authority, Access & Platform — delegation, Guest data, staff scope, enforcement, audit/retention.
