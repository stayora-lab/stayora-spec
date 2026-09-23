# Stay and Operations

> Status: **STABLE — CP7 ARCHITECTURE REVIEWED; NOT IMPLEMENTATION FREEZE**

Stay is an independent operational Aggregate candidate:

```text
SCHEDULED → CHECKED_IN → CHECKED_OUT → COMPLETED
SCHEDULED → DID_NOT_OCCUR
```

Stay may arise from a Stayora Booking or External Accommodation. Conceptually:

```text
Accommodation Basis (Stayora Booking | External Accommodation) → Stay
```

Accommodation Basis is a conceptual relationship, not an automatic database entity/table. Every represented Stay has an authoritative accommodation basis. Booking does not become Stay; External Accommodation does not become Stayora Booking.

Owner Block and Maintenance Block do not create Booking, Guest, Stay or fake accommodation transactions. Incident and operational resolution remain separate from responsibility, refund, Verification consequence and commercial authority. Open Incident does not automatically block completion; only qualifying policy-defined unresolved exceptions may do so. A complaint after Completed does not reopen Stay.
