# Surface architecture principles

- Navigation follows responsibility, not database tables.
- Shared domain truth remains shared; contextual projection is not duplicate ownership.
- Working Context changes perspective, never permission.
- Visibility is not authority; actionability requires the CP3 effective-permission test.
- Resource scope is explicit: Destination, Property, Unit, Request, Booking, Stay, Incident, Inventory, relationship or case.
- `Searchability ≠ Availability ≠ Bookability`.
- `Request ≠ Booking ≠ Stay`; `Incident ≠ Maintenance Block`.
- Milestones such as Preparation/Ready remain projections, not lifecycle states.
- Money visibility follows function and need-to-know; Attribution ≠ Commission ≠ Settlement ≠ Payout.
- A handoff changes responsibility or perspective, not the canonical object or its domain owner.
