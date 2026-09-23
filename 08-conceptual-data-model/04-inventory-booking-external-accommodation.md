# Inventory, Booking Request, Booking and External Accommodation

> Status: **STABLE — CP7 ARCHITECTURE REVIEWED; NOT IMPLEMENTATION FREEZE**

## Inventory

Inventory Commitment is a candidate Aggregate Root. Availability is a derived projection:

```text
Inventory Commitments + Bookable Unit + Time Range → Derived Availability
```

Conceptual commitment types are Temporary Exclusive Commitment, Confirmed Accommodation Commitment and Availability Block. `AVAILABLE`, `HELD`, `BOOKED` and `BLOCKED` are semantics/projections, not canonical lifecycle records. Request does not reserve Inventory. Physical absence does not release it; release requires an authoritative end.

Owner and authorized maintenance/operational blocks create Availability Blocks. Butler observation alone does not create one without required authority or policy.

## Booking Request and Booking

Booking Request is a candidate Aggregate Root representing commercial intent awaiting authorized decision. Multiple Requests may coexist; it is never a “Pending Booking”. Authorized acceptance may create authorization to commit, Temporary Exclusive Commitment and payment requirements.

Booking is a candidate Aggregate Root and begins at `CONFIRMED`. There is no fake pre-confirmation Booking. Before confirmation, Request, authorized acceptance, temporary commitment, Payment Obligation, Payment Attempt and Required Payment Condition remain distinct truths. Confirmation establishes Booking plus Confirmed Accommodation Commitment. Booking is commercial truth, not Stay.

## External Accommodation

External Accommodation is a candidate Aggregate Root for externally originated accommodation fact/record. It is not a fake Stayora Booking. It may contain source, external reference where available, Bookable Unit, dates, minimum Staying Party information, authoritative recorder, provenance and timestamps. External revenue, margin and payment data are not required merely to represent operational truth.

An external fact can conflict with an existing commitment. Preserve both the historical fact and the commitment; surface an Inventory Conflict/Exception and require authorized resolution. External factual truth is not automatically successful establishment of a new Inventory Commitment.
