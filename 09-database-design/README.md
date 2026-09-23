# CP7 — Supporting Persistence Architecture

> **STATUS: SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL**  
> **NOT IMPLEMENTATION FREEZE**  
> **SUBJECT TO UX / IMPLEMENTATION VALIDATION**

This document retains the approved physical database design direction as the persistence portion of [CP7 Data Model](../08-conceptual-data-model/README.md). It defines PostgreSQL responsibility, table-family directions, hard invariant boundaries, temporal/provenance strategy, projections, transaction boundaries and Drizzle mapping guidance.

It does not create final columns, SQL, Drizzle schemas, migrations, APIs, services, repositories, routes or implementation code. Aggregate boundaries remain distinct from table boundaries. This supporting architecture is not an implementation baseline and remains subject to UX and implementation validation. CP8 — UX / Design System is the next canonical checkpoint and has not started.

## Reading order

1. [Architecture principles](01-architecture-principles.md)
2. [Identity, Party and Authority](02-identity-party-authority.md)
3. [Property, Inventory and Concurrency](03-property-inventory-concurrency.md)
4. [Booking, External Stay](04-booking-external-stay.md)
5. [Money and Financial History](05-money-financial-history.md)
6. [Trust, Quality and Reputation](06-trust-quality-reputation.md)
7. [Constraints, Temporal and Provenance](07-constraints-temporal-provenance.md)
8. [Projections and Read Models](08-projections-read-models.md)
9. [PostgreSQL and Drizzle Mapping](09-postgresql-drizzle-mapping.md)
10. [Open Decisions](10-open-decisions.md)
11. [CP7 Persistence Completion Report](CP7-PERSISTENCE-COMPLETION-REPORT.md)

Use this persistence direction with CP1–CP7; do not use it to infer unresolved product policy.
