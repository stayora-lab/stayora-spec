# Property, Inventory and Concurrency

> Status: **SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL; NOT IMPLEMENTATION FREEZE**

```text
DESTINATION → PROPERTY → BOOKABLE UNIT
```

Property ≠ Bookable Unit. Oceanami V0 models an entire Villa as one Bookable Unit. Inventory targets Bookable Unit plus destination-local date range using `[start_date, end_date)` semantics.

Availability is derived from Inventory Commitments. Do not create canonical daily availability rows or `is_available`. Commitment types are `TEMPORARY_EXCLUSIVE`, `CONFIRMED_ACCOMMODATION` and `AVAILABILITY_BLOCK`. Request has no inventory effect. Owner/Maintenance blocks use Availability Block, not fake Booking.

Effective exclusive commitments for one Bookable Unit may not overlap. PostgreSQL is the final concurrency boundary; application availability checks are advisory. Do not implement SELECT-then-IF-available-then-INSERT as the integrity mechanism. Temporary → Confirmed preserves history through safe supersession/replacement. External Accommodation uses the same confirmed commitment mechanism. No channel has implicit priority.

Temporary expiration is explicit and reconciled. As a safety-oriented persistence direction, delayed reconciliation should avoid silently permitting a double booking and may fail closed; the final conflict/concurrency policy remains TBD and this implementation preference is not a universal product rule. Property publication/status changes do not silently destroy commitments. Destination membership is temporal when historical membership matters.
