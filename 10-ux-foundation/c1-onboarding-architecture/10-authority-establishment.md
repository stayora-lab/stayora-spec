# C1 — Authority Establishment Mapping

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Authority source | Grantor/source | Grantee | Resource scope | Actions enabled conceptually | Not enabled automatically | Revocation/change | Audit need |
|---|---|---|---|---|---|---|---|
| Ownership-derived relationship | Valid Owner/Party evidence and policy | Identity/Party | Property/related resources | Ownership-related actions where explicitly supported | Hosting, Booking, Inventory, Payout | Relationship/authority change affects future actions | Actor, basis, evidence, scope/time |
| Hosting / Primary Host authority | Valid hosting authority anchor | Primary Host Identity/Party | Property/Units and delegated scope | Hosting/commercial responsibility and allowed delegation | Financial Beneficiary, every finance action | Host change/revocation | Authority source, resource, time |
| Delegated Co-host authority | Primary Host/valid grantor | Co-host Identity | Named Property/Unit/Booking/Stay capability | Only granted capability/action/lifecycle | Unrestricted delegation, finance or other resources | Revoke/change future actions | Grantor, grant, scope, time, acting capacity |
| Distribution relationship | Platform eligibility + commercial relationship | Sale Identity | Eligible supply/transaction context | Search, Offer, Request, attribution | Booking acceptance, Inventory, Host, operations, finance | Eligibility/relationship end | Relationship/source/scope/time |
| Inventory Authority | Explicit capability/grant or canonical Inventory policy | Authorized Identity/context | Bookable Unit × Time | Establish/change/end canonical Commitments/Blocks | Universal Availability or other Units | Capability/authority lifecycle | Basis, reason, Unit × Time, actor |
| Operations assignment | Host/Destination authority | Butler/Destination Staff | Property/Stay/Destination function | Preparation, access, operational evidence | Commercial authority, Booking, pricing, Inventory | Assignment end/change | Assignment, function, resource/time |
| Platform/Admin function | Authorized Staff/domain function | Staff context | Assigned domain/resource | Support, review, policy action in scope | Silent impersonation or Property authority | Staff/function change | Human function, reason, resource/time |

Effective permission remains the CP3 model: Identity + Platform Eligibility + Actor Relationship + Authority Capability + Resource Scope + lifecycle + policy + transaction context. C1 does not create RBAC tables or new authority types.
