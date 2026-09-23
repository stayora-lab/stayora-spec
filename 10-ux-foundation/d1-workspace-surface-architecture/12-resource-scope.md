# Resource scope model

| Scope | Surfaces that may project it | Boundary |
|---|---|---|
| Destination | Public, BQL, Host/Sale/Guest as relevant, Admin | Membership/visibility is not authority |
| Property / Unit | Public, Host, Sale, Butler, Guest, BQL, Admin | Action requires relationship/capability |
| Request / Booking | Host, Sale, Guest, Admin; Butler/BQL only need-to-know | Request ≠ Booking; Sale cannot accept by creation |
| External Accommodation | Host/Admin/Inventory-authorized context, Stay/Operations projections | External concept; no fake Stayora Booking |
| Stay | Guest, Host, Butler, BQL, Sale limited, Admin | Contextual projection of one Stay truth |
| Inventory Commitment/Block | Host/Inventory-authorized, Admin conflict, derived projections elsewhere | Availability is derived; visibility ≠ mutation authority |
| Incident | Butler, Host, BQL, Guest, Admin/Quality as scoped | Incident ≠ Finding/Responsibility/Consequence |
| Sale/Butler Assignment and relationships | Subject context, Host/Admin/Destination function as scoped | Relationship/Assignment ≠ authority |

No object is globally visible by default; scope is a prerequisite for projection and action.
