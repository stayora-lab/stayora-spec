# C1 — B1–B5 Traceability

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Journey | C1 must support | C1 result | Protected boundary |
|---|---|---|---|
| B1 Sale-assisted Booking | Sale Identity/eligibility, Distribution Relationship, Host and delegated Booking Authority. | Sale context can discover/Offer/create Request; Host/Co-host authority remains separate. | Sale capacity does not accept or block Inventory. |
| B2 External Booking → Stay | Authorized external reporter/recorder and scoped Record External Commitment capability. | Report/relationship/authority are separate; explicit Inventory capability required for commitment effect. | No universal Inventory Authority or fake Booking. |
| B3 Direct Guest Booking | Guest participation without mandatory registered account. | Guest/Party/Stay relationship can be represented independently from Account; direct Request remains possible where CP5 supports it. | Account ≠ Identity/Party; Guest ≠ Host authority. |
| B4 Stay Operations | Butler assignment and Destination/BQL function scope. | Operational context/access can be activated without commercial authority. | Assignment/visibility ≠ Booking, pricing, Inventory or finance. |
| B5 Inventory Intervention | Owner/Host/authorized actor and operational reporter/Inventory decision relationships. | Unit × Time authority is explicit; Incident/report does not auto-block. | Ownership/assignment/evidence ≠ unrestricted Inventory Authority. |

C1 does not change B1–B5 semantics or create a second authority model.
