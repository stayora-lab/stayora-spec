# C1 — Multi-Capacity Identity Stress Tests

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Case | One Identity model | Correct context/authority | Must not happen |
|---|---|---|---|
| Owner + Host | One Identity; Owner and Hosting relationships/capacities. | Host actions require Hosting Authority; Owner actions use Owner basis. | Owner identity silently grants every Host/finance action. |
| Sale + Co-host with delegated Booking Authority | One Identity; Sale context and Co-host acting capacity. | Accept Request only under delegated Co-host authority and resource scope. | Sale role accepts or whitelist becomes authority. |
| Butler + another capacity | One Identity; Butler assignment plus other relationship. | Operational actions under Butler assignment; other actions under their own basis. | Butler assignment grants Booking/Inventory/finance. |
| Guest later becomes Owner/Host/Sale | Same Identity gains new relationships/capacities over time. | Guest Stay context remains scoped; new context requires its own eligibility/authority. | Account duplication or Guest data leakage. |
| Existing Identity invited to another resource | Same Identity resolves invitation and proposed relationship. | New resource scope/authority only after valid acceptance/grant. | Invitation alone grants resource authority. |

Audit must retain Identity, acting capacity, authority source, resource, action and time for each privileged action.
