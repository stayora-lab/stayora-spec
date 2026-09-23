# Surface / Action matrix

Legend: **CAN INITIATE**, **CAN ACT IF AUTHORIZED**, **VIEW ONLY**, **NOT APPLICABLE**, **TBD**.

| Action | Public | Guest | Host | Sale | Butler | BQL | Admin |
|---|---|---|---|---|---|---|---|
| Create Booking Request | CAN INITIATE | CAN INITIATE where supported | CAN ACT IF AUTHORIZED | CAN INITIATE | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF AUTHORIZED |
| Accept/reject Request | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF AUTHORIZED | NOT APPLICABLE | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF AUTHORIZED |
| Record External Accommodation | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF Inventory-authorized | VIEW/REPORT only | REPORT only | VIEW/REPORT | CAN ACT IF AUTHORIZED |
| Create Owner Block | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF Inventory-authorized | NOT APPLICABLE | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF AUTHORIZED |
| Authorize Maintenance Block | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF Inventory-authorized | NOT APPLICABLE | VIEW/REPORT | VIEW/REPORT | CAN ACT IF AUTHORIZED |
| Record Incident | NOT APPLICABLE | CAN INITIATE own issue | CAN ACT IF AUTHORIZED | NOT APPLICABLE | CAN INITIATE/ACT scoped | CAN INITIATE/ACT scoped | CAN ACT IF AUTHORIZED |
| Check-in | NOT APPLICABLE | VIEW/PARTICIPATE | CAN ACT IF AUTHORIZED | NOT APPLICABLE | CAN ACT IF explicitly authorized | CAN ACT IF authorized function | CAN ACT IF authorized |
| Checkout | NOT APPLICABLE | VIEW/PARTICIPATE | CAN ACT IF AUTHORIZED | NOT APPLICABLE | CAN ACT IF explicitly authorized | CAN ACT IF authorized function | CAN ACT IF authorized |
| View payment requirement | NONE | NEED-TO-KNOW own | AUTHORITY-DEPENDENT | NEED-TO-KNOW scoped | NOT APPLICABLE | NOT APPLICABLE | AUTHORITY-DEPENDENT |
| Manage Sale attribution | NOT APPLICABLE | NOT APPLICABLE | VIEW/participate per policy | CAN INITIATE own | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF AUTHORIZED |
| Assign Butler | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF delegated authority | NOT APPLICABLE | NOT APPLICABLE | TBD/function-authorized | CAN ACT IF AUTHORIZED |
| Change publication | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF Property-authorized | NOT APPLICABLE | NOT APPLICABLE | NOT APPLICABLE | CAN ACT IF authorized |
| Correct Property relationship | NOT APPLICABLE | NOT APPLICABLE | CAN INITIATE/VIEW | NOT APPLICABLE | NOT APPLICABLE | VIEW/REPORT | CAN ACT IF authorized |

The matrix is not a role permission table. Each action still evaluates actual Identity, capacity, capability, resource, lifecycle and policy.
