# Object Detail Relationships

| Detail | Reached from | Related objects | Handoff/action posture |
|---|---|---|---|
| Property/Unit (`HST-02`/`PUB-03`) | Public discovery, Host responsibility, Sale supply | Destination, Inventory, Verification | publication/representation or date intent; Property ≠ Unit |
| Request (`HST-04`) | Host Requests, Sale activity | Unit, Inventory, Payment Condition | accept/reject only with Host authority |
| Booking (`HST-05`) | accepted Request/outcome | Request, Payment, Commitment | commercial outcome; separate from Stay |
| External Accommodation (`HST-08`) | B2 reporting/Host operations | Inventory, Stay, provenance | record/reconcile; no Stayora Booking required |
| Stay (`GST-01`, `HST-07`, `BUT-02`) | Booking/External Stay handoff, Today | accommodation basis, Assignment, Incident | operations and access; separate from Booking |
| Incident (`HST-10`, `BUT-04`, `BQL-03`, `ADM-04`) | attention/Stay/Today | Finding, responsibility, possible Inventory action | evidence/escalation; Incident ≠ Maintenance Block |
| Inventory projection (`HST-09`) | Property/attention/operations | Commitments/Blocks, Availability, Bookability | authorized intervention only |
| Payment projection (`HST-12`, ADM-05) | Request/Booking/exception | Obligation, Attempt, Entitlement, Settlement, Payout | no Money category collapse |
| Sale attribution (`SAL-05`) | Sale activity | Request/Booking outcome | Attribution ≠ Commission Entitlement |
| Butler Assignment (`BUT-01/02`, HST-11) | Host/Admin relationship | Stay, Property, function | assignment-scoped operations |

Back/context relationship is conceptual; no visual breadcrumb or route is specified.
