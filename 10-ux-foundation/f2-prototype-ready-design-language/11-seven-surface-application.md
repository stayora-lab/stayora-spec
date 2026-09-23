# F2. Seven-surface application

One design language is shared through tokens, type roles, outcome language and primitives. The composition profile varies by responsibility.

| Surface | Density | Dominant information character | Action emphasis | Likely primitive/pattern emphasis |
|---|---|---|---|---|
| **Public Marketplace** | Comfortable / visual | Property/unit, destination, dates, public price, derived Availability/Bookability, trust/quality signal | Discover and create Request intent | Card, image surface, Link, Button, Date/Calendar, RequestSummary, Status/Callout. |
| **Guest Stay Access** | Comfortable / action-focused | Scoped Stay, access, arrival/departure, services/help, unresolved operational attention | Legitimate access/operational actions | Card/Panel, Alert, Button, GuestStayHub, StaySummary, AttentionProjection. |
| **Host Workspace** | Medium-to-dense | Working Context, Requests, Booking/Stay, Unit × Time, Inventory basis, authorized Money projection | Decide Request, intervene in Inventory, coordinate Stay | Table/List, Dialog, Sheet, WorkingContextBar, RequestSummary, InventoryTruthView, ConsequentialAction. |
| **Sale Workspace** | Medium-to-dense | Scoped supply, relationships, options, attribution, Request outcome | Prepare/share/submit Request and follow handoff | Card/List, Select/Combobox, Status, RequestSummary, AuthorityHint. |
| **Operations — Butler** | Mobile/action-priority | Assignment, Today/Stay readiness, arrival/check-in, Incident evidence, checkout handoff | Field-safe operational actions | List, Button, Alert, Sheet, StaySummary, Incident/evidence composition, AttentionProjection. |
| **Operations — Destination/BQL** | Dense operational overview | Destination-scoped occupancy, access, services, issues and responsibility handoffs | Coordinate destination operations within scope | Table/List, Date/Calendar projection, Status/Alert, Inventory/Stay projections. |
| **Stayora Admin** | Dense exception/governance | Evidence, provenance, conflict, manual assistance and scoped money/quality views | Review, reconcile, correct/supersede where authorized | Table, Dialog/Sheet, Callout, Status, InventoryConflictPresentation, PaymentOutcome, AuthorityHint. |

Owner has no separate surface. Owner-facing perspective is composed within Host/Property patterns and remains subject to relationship and authority evaluation.
