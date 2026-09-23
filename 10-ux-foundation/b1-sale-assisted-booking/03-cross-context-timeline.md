# B1 — Cross-Context Timeline

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

This timeline is conceptual. It shows responsibility and truth handoffs, not a technical sequence, event stream or promise that every step is synchronous.

```text
Guest                 Sale                    Host / Authority       Inventory Truth       Payment                  Stay / Operations
  │                     │                         │                      │                   │                         │
  │ need / request help │                         │                      │                   │                         │
  ├────────────────────>│                         │                      │                   │                         │
  │                     │ search / compare        │                      │                   │                         │
  │                     │─────────────────────────┼─────────────────────>│ read derived     │                         │
  │                     │<────────────────────────┼──────────────────────│ Availability      │                         │
  │ option / terms      │                         │                      │                   │                         │
  │<────────────────────│                         │                      │                   │                         │
  │ intent to proceed   │                         │                      │                   │                         │
  ├────────────────────>│                         │                      │                   │                         │
  │                     │ create Request          │                      │                   │                         │
  │                     │────────────────────────>│ PENDING              │                   │                         │
  │                     │                         │ receives responsibility│                  │                         │
  │                     │                         │ review authority     │                   │                         │
  │                     │                         ├─────────────────────>│ revalidate        │                   │                         │
  │                     │                         │ accept or reject     │                   │                         │
  │                     │<────────────────────────│                      │                   │                         │
  │                     │                         │ ACCEPTED             │                   │                         │
  │                     │                         ├─────────────────────>│ temporary commitment where applicable
  │                     │                         │                      │ finite protection │                   │                         │
  │ payment instruction │<────────────────────────┼──────────────────────┼──────────────────>│ obligation / attempt   │                         │
  │                     │                         │                      │                   │ INITIATED/PROCESSING  │                         │
  │ payment outcome     │                         │                      │                   │ SUCCEEDED / FAILED / UNKNOWN
  │                     │                         │                      │                   │                         │
  │                     │                         │ evaluate confirmation conditions      │                         │
  │                     │                         │──────────────────────────────────────>│                         │
  │                     │                         │ if all satisfied: Booking CONFIRMED   │                         │
  │<────────────────────┼────────────────────────┼──────────────────────┼───────────────────┤                         │
  │ scoped confirmation │                         │ Confirmed commitment│ protected dates   │                         │
  │                     │                         │                      │                   │ operational relevance →│
  │                     │                         │                      │                   │                         │ Host / Butler / BQL
```

## What the timeline makes explicit

- Sale reads shared Availability but does not own Inventory Truth.
- Creating a Request moves responsibility to the Host/authorized Booking Authority; it does not create a reservation.
- Acceptance is a Host-authorized decision and is not `Booking CONFIRMED`.
- A Temporary Exclusive Inventory Commitment, where applicable, is separate from Payment Attempt and Request.
- Payment `UNKNOWN` is a first-class unresolved outcome; the timeline does not choose retry/default/release behavior.
- Booking confirmation is the commercial boundary. Stay/Operations becomes relevant afterward without equating Booking with Check-in or Completed.
- Butler and BQL appear only when a confirmed/represented Stay creates operational responsibility; they do not enter to accept a Request.

## Timing boundaries intentionally left open

The diagram does not choose lead SLA, notification timing, temporary commitment window, payment deadline/grace, conflict resolution, provider reconciliation, QR lifecycle, or Stay scheduling. Those are listed in [B1 TBD register](07-tbd-policy-register.md).
