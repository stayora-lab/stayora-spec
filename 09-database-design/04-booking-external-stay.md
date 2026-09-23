# Booking, External Accommodation and Stay

> Status: **SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL; NOT IMPLEMENTATION FREEZE**

Booking ≠ External Accommodation ≠ Stay. Booking is Stayora commercial truth and begins only at `CONFIRMED`; no fake pending Booking represents a Request. External Accommodation is an external commercial/accommodation fact known to Stayora, not Booking with `source=external`. Stay is operational fulfillment truth.

Booking preserves contractual/commercial snapshot facts and does not duplicate Stay lifecycle. External Accommodation requires only minimum authoritative operational facts: source, external reference where available, Bookable Unit, date range, minimum Staying Party information, authoritative recorder, provenance and timestamps. External price/payment/commission disclosure is not required merely to represent operations.

Every represented Stay has exactly one authoritative Accommodation Basis: Booking or External Accommodation. V0 preference is explicit typed nullable references with an XOR invariant; this is a conceptual mapping direction, not final column design. Staying Party need not have a Stayora Identity. Booker/transaction actor differs from Staying Party. Scheduled dates differ from actual check-in/check-out timestamps.

Commercially significant change uses amendment/supersession: validate replacement, establish it safely, then supersede the old commitment. Cancellation does not delete Booking. No-show does not require fake cancellation or fake Stay completion. A late authoritative external fact survives an inventory conflict. External Accommodation Report is not authoritative External Accommodation; a report may be retained where needed, but exact V0 persistence remains open.

Stayora Booking confirmation and Confirmed Inventory Commitment require strong atomic consistency. Current V0 persistence direction favors one Booking mapped to one Bookable Unit and one continuous accommodation range, normally producing one Stay. This is a persistence simplification for the current V0 direction, not a closure of upstream product decisions about split stays, unit moves, extensions or related accommodation behavior; those remain TBD and must be validated before persistence is finalized.
