# Host Workspace Convergence

Host structure is responsibility-driven:

- **Current Responsibility & Attention:** `HST-01` primary destination. It receives pending Requests, conflicts, Payment `UNKNOWN`, Stay exceptions and property responsibility signals.
- **Requests:** `HST-03` primary collection; `HST-04` contextual Request detail/action entry.
- **Bookings & Stays:** `HST-06` primary operational collection; `HST-05` Booking detail and `HST-07` Stay detail remain contextual children. Booking and Stay are related but distinct.
- **Properties & Units:** `HST-02` primary Property/Unit responsibility; Unit remains a contextual child, not a separate global destination.
- **Inventory:** `HST-09` contextual/action destination from Property, attention or operations; `HST-10` is the operations/exception projection rather than a generic issue suite.
- **Operations & Incidents:** `HST-10` contextual exception destination and `HST-11` coordination projection from Stay/Property; Incident remains separate from Maintenance Block.
- **Money:** `HST-12` is an embedded/contextual projection reached from relevant Booking, Stay, Property or attention context. No generic Finance/Wallet/Earnings destination is created.

Twelve D2 concepts therefore do not become twelve navigation items. Host actions remain CP3-authority dependent.
