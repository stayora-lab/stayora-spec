# Object ownership versus surface responsibility

| Object | Canonical owner | Primary action surface | Secondary projections | Excluded shortcut |
|---|---|---|---|---|
| Property / Unit | Property | Host/Admin; Public reads | Sale, Guest, Butler, BQL | Surface ownership ≠ Property authority |
| Booking Request | Booking | Host/authorized Booking Authority | Sale, Guest, Admin | Sale creator cannot accept |
| Booking | Booking | Host/Guest/Admin as scoped | Sale, Butler, BQL | No duplicate actor Booking |
| External Accommodation | Inventory/Stay reference | Inventory-authorized Host/Admin | Host, Stay, Butler/BQL | Sale report ≠ authoritative fact |
| Stay | Stay | Host/Operations/Admin | Guest, Butler, BQL, Sale limited | No per-surface Stay objects |
| Inventory Commitment/Block | Inventory | Inventory-authorized Host/Admin | Host/Sale/Public derived views | Availability is not a stored surface truth |
| Incident | Incident/quality case | Operations/Host/Admin | Butler, Guest, BQL, Quality | Incident ≠ Block/consequence |
| Payment truth | Money | Guest/Host/Admin/Sale limited | Other contexts need-to-know | Visibility ≠ financial authority |
| Sale attribution | Distribution/Money policy | Sale/Admin, relevant Host | Booking/Stay projections | Attribution ≠ commission/Settlement |
| Butler Assignment | Identity/Authority/Operations relationship | Host/Admin/Destination function | Butler, Stay/Property | Assignment ≠ super-authority |
