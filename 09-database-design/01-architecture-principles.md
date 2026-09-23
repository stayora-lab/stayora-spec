# Database Architecture Principles

> Status: **SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL; NOT IMPLEMENTATION FREEZE**

```text
CANONICAL WRITE MODEL
Business facts + authority + commitments + financial truth
        ├── DB constraints protect hard invariants
        └── Domain/Application orchestration applies workflow/policy
                         ↓
DERIVED / READ MODELS
Calendar / Availability / Search / Dashboard / Reputation …
```

PostgreSQL is the canonical transactional store. Critical invariants should be protected at the database boundary when feasible; domain policy should not be stuffed into constraints. Aggregate boundary is not table boundary. Canonical write truth is distinct from read projections. No Event Sourcing is introduced as foundational architecture.

Historical truth uses temporal records, immutable transactions, amendment/adjustment and supersession rather than destructive overwrite. Money uses exact integer minor units and controlled currency. Event timestamps use absolute time; accommodation dates use destination-local business semantics. Relational-first design is preferred; JSONB is for appropriate extensibility/integration and not an escape hatch for core relational truth. Provenance is not reduced to one giant events JSONB table.

There is no canonical `is_available`. No binary floating-point money. Critical writes preserve provenance/auditability.
