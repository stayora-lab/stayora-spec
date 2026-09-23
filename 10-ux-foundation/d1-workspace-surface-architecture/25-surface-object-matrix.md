# Surface / Object matrix

Legend: **NONE**, **SUMMARY**, **NEED-TO-KNOW**, **ACTIONABLE**, **AUTHORITY-DEPENDENT**, **ADMIN/EXCEPTION**.

| Object | Public | Guest | Host | Sale | Butler | BQL | Admin |
|---|---|---|---|---|---|---|---|
| Property/Unit | SUMMARY | SUMMARY | ACTIONABLE | SUMMARY | NEED-TO-KNOW | NEED-TO-KNOW | AUTHORITY-DEPENDENT |
| Request | NONE | SUMMARY | ACTIONABLE | ACTIONABLE | NONE | NONE | ADMIN/EXCEPTION |
| Booking | NONE | SUMMARY | ACTIONABLE | SUMMARY | NEED-TO-KNOW | NEED-TO-KNOW | ADMIN/EXCEPTION |
| External Accommodation | NONE | NEED-TO-KNOW | ACTIONABLE | SUMMARY/report only | NEED-TO-KNOW | NEED-TO-KNOW | AUTHORITY-DEPENDENT |
| Stay | NONE | ACTIONABLE own | ACTIONABLE | SUMMARY | ACTIONABLE scoped | NEED-TO-KNOW | ADMIN/EXCEPTION |
| Inventory Commitment/Block | derived SUMMARY | NONE | ACTIONABLE if authorized | derived SUMMARY | NONE/report | SUMMARY derived | AUTHORITY-DEPENDENT |
| Incident | NONE | report/own NEED-TO-KNOW | ACTIONABLE scoped | NONE | ACTIONABLE report | ACTIONABLE scoped | ADMIN/EXCEPTION |
| Payment truth | NONE | NEED-TO-KNOW own | AUTHORITY-DEPENDENT | NEED-TO-KNOW scoped | NONE | NONE | ADMIN/EXCEPTION |
| Sale attribution | NONE | NONE/need | SUMMARY scoped | ACTIONABLE own | NONE | NONE | ADMIN/EXCEPTION |
| Butler Assignment | NONE | NEED-TO-KNOW if relevant | ACTIONABLE if authorized | NONE | ACTIONABLE own | NEED-TO-KNOW | AUTHORITY-DEPENDENT |

Matrix categories describe projection/action posture, not new permission. CP3 authority remains decisive.
