# PostgreSQL and Drizzle Mapping Directions

> Status: **SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL; NOT IMPLEMENTATION FREEZE**

V0 topology is one PostgreSQL transactional database in a modular monolith. The following are table-family directions only; they do not authorize final columns, schemas, migrations or ORM contracts.

| Family | Directional concepts |
|---|---|
| Identity / Authority | identities, parties, party representations, platform eligibilities/decisions, ownerships, host relationships, Sale relationships, Butler assignments, authority grants/capabilities/scopes |
| Supply | destinations/configuration, properties, destination memberships, bookable units |
| Commerce | booking requests/decisions, bookings/amendments, external accommodations/reports where needed |
| Inventory | availability blocks, inventory commitments, inventory conflicts |
| Operations | stays, staying parties, stay access credentials |
| Money | commercial snapshots, commercial adjustments, payment obligations/transactions, payment allocations (working), entitlements, economic adjustments, settlements/lines, payouts/attempts, refund representation TBD |
| Trust / Quality | incidents/observations, evidence, findings/typed subjects, verification cases/decisions, review rights, reviews/typed components |
| Infrastructure | audit records, outbox messages, idempotency records |

UUIDv7 is preferred for canonical business IDs; human-readable references remain separate from PKs. Use real PostgreSQL FKs and restrictive deletion for historical transactions; cascade only for proven dependent ownership. PostgreSQL enums suit stable structural vocabulary; evolving policy vocabulary uses controlled codes/reference structures. Use DATE for accommodation business dates, TIMESTAMPTZ for absolute events, and store Destination IANA timezone. Range/exclusion constraints protect Inventory. Raw PostgreSQL migration SQL is allowed later where Drizzle cannot express an invariant. Indexes follow actual query patterns; partial indexes must not use volatile `now()` truth. Constraint names should be business-readable and violations map to domain errors. Production migrations remain append-forward history.
