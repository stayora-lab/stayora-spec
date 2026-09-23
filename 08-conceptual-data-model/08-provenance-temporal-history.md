# Provenance, Temporal Validity and Immutable History

> Status: **STABLE — CP7 ARCHITECTURE REVIEWED; NOT IMPLEMENTATION FREEZE**

Important relationships and authority grants support effective lifetime: Ownership, Primary Host, Co-host, Commercial Authority, Authority Grant and other significant Actor Relationships. A later ownership transfer does not rewrite historical Bookings to make the new Owner appear historical.

Critical business actions must answer:

```text
WHO did WHAT acting AS WHAT under WHICH AUTHORITY
to WHICH RESOURCE WHEN WHY/BASIS with WHAT RESULT
```

This includes Request acceptance; Inventory Commitment creation/release; authority changes; external accommodation recording; price adjustment; refund; settlement correction; Verification decisions; Platform Eligibility suspension; and Admin corrections. Admin actions preserve Admin Identity, administrative capability, reason, original fact, corrected/replacement fact, provenance and time. Admin does not impersonate another business actor.

Historical financial and business facts are corrected through new events, adjustments, supersession, replacement facts or explicit correction actions rather than destructive rewriting. This applies to relationships, grants, ownership, Inventory Commitments, Booking amendments, external facts, Payment Transactions, Settlements, Payouts, Findings, Verification Decisions and Admin Corrections. CP7 does not select event sourcing, CQRS or any physical history mechanism.
