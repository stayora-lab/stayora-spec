# Constraints, Temporal Validity and Provenance

> Status: **SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL; NOT IMPLEMENTATION FREEZE**

Use three invariant levels:

1. **Database Hard Invariant** — relational/range/exclusion integrity where feasible.
2. **Transaction/Application Invariant** — atomic orchestration and idempotent operations.
3. **Domain/Policy Invariant** — authority, policy, evidence and consequence decisions.

Temporal convention is `[valid_from, valid_until)`; business validity differs from record creation timestamp. Database-level non-overlap protects effective Primary Host relationships and effective exclusive Inventory Commitments. Temporal history is preserved.

Reference strategy: small stable closed sets use typed nullable references plus checks; multi-subject concepts use typed association families; generic references are mainly for audit/integration/telemetry. Do not make `subject_type + subject_id` the default canonical strategy or build a Universal Resource Registry in V0.

Audit answers who, what, acting capacity, authority, resource, timestamp, reason/basis and result. Audit does not replace canonical domain history and must not become unrestricted PII payload storage. No universal `deleted_at`; corrections use amendment, supersession or reversal by domain semantics. Critical mutable aggregates may use optimistic concurrency; external side effects may use idempotency. Transactional Outbox is supported directionally but does not imply Event Sourcing.
