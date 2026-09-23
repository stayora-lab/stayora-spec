# B2 — Cross-Context Timeline

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

Conceptual only: this is a responsibility and truth timeline, not an integration sequence or UI design.

```text
External Source   Reporter / Host   External Fact Truth   Inventory       Guest        Butler        Destination/BQL   Admin
      │                 │                  │                 │              │             │                 │              │
      │ external       │                  │                 │              │             │                 │              │
      │ commerce       │                  │                 │              │             │                 │              │
      ├───────────────>│ report/register  │                 │              │             │                 │              │
      │                 ├────────────────>│ unresolved       │              │             │                 │              │
      │                 │ source/identity/authority/evidence evaluation    │             │                 │              │
      │                 │                  ├───────────────>│ if authorized │             │                 │              │
      │                 │                  │ external fact  │ evaluate     │             │                 │              │
      │                 │                  │                │ commitment   │             │                 │              │
      │                 │                  │                │ derived      │             │                 │              │
      │                 │                  │                │ Availability │             │                 │              │
      │                 │                  │                │              │             │                 │              │
      │                 │                  │────────────────────────────────────────────>│ conflict / exception if overlap
      │                 │                  │                │              │             │                 │              │
      │                 │                  ├───────────────────────────────────────────────────────────────>│ operational fact/audit
      │                 │                  │                │              │             │                 │              │
      │                 │                  │ Stay representation / Accommodation Basis   │                 │              │
      │                 │                  │────────────────────────────────────────────>│             │              │
      │                 │                  │                │              │ scoped      │ assigned      │ destination  │
      │                 │                  │                │              │ access      │ operations    │ operations   │
      │                 │                  │                │              ├────────────>│             ├──────────────>│
      │                 │                  │                │              │             │ evidence    │ operational  │
      │                 │                  │                │              │             │ / incident  │ response     │
      │                 │                  │                │              │             │             │              │
      │                 │                  │                │              │ checkout / completion / correction history
```

## Timeline guardrails

- External commerce is the source of the original commercial lifecycle; Stayora learns about it through a report/source signal.
- A reporter does not automatically establish an authoritative External Accommodation Fact.
- An accepted fact does not automatically create an Inventory Commitment; explicit Inventory Authority and compatibility are required.
- A valid commitment affects derived Availability; it is not itself Availability.
- A conflict preserves external fact and existing commitments; the timeline contains an exception point rather than a winner.
- Stay representation is independent of Booking and does not imply Check-in or Completed.
- Guest, Butler and BQL receive scoped projections only when the Stay and access/assignment conditions make them operationally relevant.
- Completion and corrections preserve source/history; no Stayora commercial provenance is fabricated.
