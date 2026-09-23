# Journey × Surface matrix

| Journey | Entry | Intermediate | Decision | Operations | Guest | Exception/completion |
|---|---|---|---|---|---|---|
| B1 Sale-assisted Booking | Sale/Public | Sale → Request | Host/Co-host Booking Authority | Butler/BQL after confirmation | Guest Stay Access | Admin/Incident/Money as scoped |
| B2 External Booking → Stay | Host/Admin/external fact | Inventory/Stay representation | Authorized Inventory/Stay function | Host/Butler/BQL | Guest Stay Access | Conflict/Admin/Completion |
| B3 Direct Guest Booking | Public Marketplace | Guest Request | Host/Booking Authority | Butler/BQL | Guest Stay Access | Admin/Money/Completion |
| B4 Stay Operations | Host/Stay | Butler/BQL operations | Authorized Check-in/Checkout/completion | Butler/BQL/Host | Guest Stay Access | Incident/Admin/Quality |
| B5 Inventory Intervention | Host/operations report | Inventory evaluation | Inventory Authority | Host/Operations | Public/Sale derived view | Admin conflict/Booking exception |

Every accepted journey has a visible responsibility and exception handoff; no surface becomes a second source of truth.
