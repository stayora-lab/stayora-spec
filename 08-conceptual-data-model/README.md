# Checkpoint 7 — Conceptual Data Model

> Status: **STABLE — CP7 ARCHITECTURE REVIEWED; NOT IMPLEMENTATION FREEZE**

CP7 — Data Model documents the conceptual business objects, lifecycle ownership, aggregate candidates, relationship and authority boundaries, consistency boundaries, derived projections, provenance, temporal validity and immutable historical truth. Its persistence portion is documented separately as supporting Persistence Architecture.

This conceptual portion does not define PostgreSQL tables, Drizzle, SQL, foreign keys, indexes, constraint implementation, APIs, services, migrations, repositories or event infrastructure. The supporting persistence portion is documented in [`../09-database-design/README.md`](../09-database-design/README.md) as part of CP7; neither portion is an implementation freeze.

## Reading order

1. [Conceptual model principles](01-conceptual-model-principles.md)
2. [Identity, Party, Relationships and Authority](02-identity-party-relationship-authority.md)
3. [Destination, Property and Bookable Unit](03-destination-property-bookable-unit.md)
4. [Inventory, Booking and External Accommodation](04-inventory-booking-external-accommodation.md)
5. [Stay and Operations](05-stay-and-operations.md)
6. [Money, Payment, Settlement and Payout](06-money-payment-settlement-payout.md)
7. [Incident, Verification, Review and Reputation](07-quality-and-cases.md)
8. [Provenance, Temporal Validity and History](08-provenance-temporal-history.md)
9. [Aggregate and Projection Map](09-aggregate-and-projection-map.md)
10. [Invariants and Stress Tests](10-invariants-and-stress-tests.md)

### CP7 persistence portion

[Supporting Persistence Architecture](../09-database-design/README.md) documents the physical database direction retained under CP7 Data Model. CP8 — UX / Design System follows the full CP7 checkpoint and has not started.

Conceptual candidates are not ORM or persistence decisions. Shared truth remains owned by the CP1–CP6 domains.
