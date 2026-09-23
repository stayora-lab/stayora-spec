# Inventory Policy

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

Inventory authority comes from a valid commitment over Bookable Unit + time, not from the sales channel. A valid external confirmed commitment has the same inventory effect as a valid Stayora confirmed commitment.

Default principle: the first valid effective exclusive commitment prevents a later incompatible exclusive commitment over the same scope while valid. This is not channel precedence; a valid Temporary Exclusive Commitment is respected during its lifetime. Late-discovered external commitments require conflict/reconciliation, not silent overwrite. True conflict resolution remains **TBD**.

Conflict records should preserve commitments, source, actor, timestamps, evidence, authority basis, resolution, and resolver. Actor authority controls creation/end/change. Sale whitelist alone does not create Inventory Authority; ordinary Sale may report an external booking, while authoritative recording requires explicit capability. Butler/BQL lack commercial Inventory Authority by default. Availability Blocks preserve source, reason, authority, scope, and lifetime. Inventory confidence/sync freshness supplements, but is not, Availability state.
