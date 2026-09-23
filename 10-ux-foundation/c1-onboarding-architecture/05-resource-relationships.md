# C1 — Resource Relationship Mapping

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Resource | May be established by | Relationships to investigate | What does not follow automatically |
|---|---|---|---|
| Destination | Destination domain / authorized platform or destination context | Staff/function, Property membership, local capability/configuration | Property ownership, Booking economics or global platform authority. |
| Property | Property domain from authorized representation | Destination membership, Owner, Primary Host, Co-host, Listing, Units, Verification | Ownership = hosting, publication, Inventory or Payout. |
| Bookable Unit | Property domain / authorized Property structure | Property, Inventory, Listing, Commitments, Blocks | Unit creation = Available, Bookable, Verified or Booking Authority. |
| Stay | Stay/operations from Booking or External Accommodation basis | Guest/Staying Party, Butler, Destination operations | Stay = Booking, Inventory Commitment or commercial origin. |
| Booking / Request | Booking domain under actor capability | Guest, Host authority, Sale attribution where genuine, Money | Guest visibility or Sale role = acceptance. |
| Inventory scope | Inventory domain | Unit × Time, Commitments, Blocks, external signals | Owner/Butler/BQL observation = Inventory Authority. |

For every resource association, later detailed onboarding must identify actor, basis/evidence, scope, validity, resulting context/authority and what remains pending. C1 does not design resource forms.
