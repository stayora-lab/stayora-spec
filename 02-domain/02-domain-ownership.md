# Domain Ownership Matrix — Stayora

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**

“Owns” ở đây nghĩa là business source of truth, không phải database ownership. “References” nghĩa là domain dùng sự thật của domain khác để thực hiện trách nhiệm của mình.

| Domain | Owns | References | Must not own |
|---|---|---|---|
| Identity & Authority | Identity, role activation, delegation, resource authority, platform eligibility | Property, Destination, Distribution relationships | Booking, commission, Inventory, reviews |
| Property | Accommodation structure, Bookable Units, attributes, capacity, amenities, media, listing, destination membership, host/property associations | Identity, Destination, Verification | Availability truth, Booking state, reviews, financial ledger |
| Inventory | Bookable Unit × Time Inventory Truth, effective Inventory Commitments, derived Inventory Availability, valid temporary/confirmed commitments and blocks, external inventory signals | Property/Bookable Unit, Booking, Money payment context, external sources | Property content, Guest profile, financial ledger, Payment Session / Attempt |
| Marketplace & Discovery | Discovery/search composition và marketplace presentation | Property, Inventory, Destination, Verification, Reputation, Offer | Authoritative availability, rating truth, Verified truth, Property truth |
| Booking | Commercial commitment, Request/Instant Book lifecycle, commercial parties, dates, conditions/policy snapshot, Offer/booked-price snapshot | Inventory, Identity, Distribution, Money | Actual Stay operations, payment ledger, Reputation |
| Stay | Actual operational stay, Staying Party, actual arrival/departure, check-in/out, operational evidence | Booking khi có, external booking evidence, Property, Destination | Commerce ledger, commission, Property definition |
| Destination | Destination identity, membership, local capabilities/configuration, local policies, BQL/management relationships | Property, Identity | Individual Booking economics, global platform rules |
| Destination Operations | Arrival/access/QR/gate/security/cart/checkout operational workflows | Stay, Destination, operational actors | Commercial price, Sale commission, Owner payout |
| Distribution | Sale/Affiliate relationships, Sale ↔ Commercial Authority holder relationship, whitelist/blacklist, Lead lifecycle, Attribution, distribution entitlement basis | Identity, Property authority, Booking | Platform Identity, legal/property ownership, payment ledger |
| Money — Payment & Settlement | Payments, refunds, entitlements, commissions, adjustments, reconciliation, Settlement, Payout | Booking, Stay completion, Distribution attribution | Booking lifecycle, actual Stay state |
| Verification | Property-supply quality standards/programs, applications, inspections, evidence, Verified lifecycle | Property, relevant Identity/Incident signals | Identity verification, platform eligibility, reviews, marketplace rating |
| Reputation | Review Rights, reviews, rating dimensions, reputation history, aggregated reputation signals | Stay evidence, Actors, Property | Verification certification, Booking/payment lifecycle |

## Boundary clarifications

### Identity & Authority versus Distribution

`Nguyễn A = approved Sale` thuộc Identity & Authority. `Nguyễn A ↔ Host B = WHITELIST` thuộc Distribution. Platform approval không tạo Host trust; blacklist trong một commercial authority scope không xóa Sale role toàn platform.

### Property, Primary Host và Commercial Authority

Property có thể tham chiếu các Host/Owner associations. Identity & Authority xác định authority thực tế. Distribution dùng holder của Commercial Authority để tạo Sale relationship. Không dùng một khái niệm `owner_id` duy nhất để đại diện cho legal owner, Primary Host và commercial authority holder.

### Booking, Stay và External sources

Stayora Booking sở hữu commercial truth của booking được tạo trên Stayora. External Booking là commerce record tạo bên ngoài; Inventory và/hoặc Stay chỉ reference hoặc ghi nhận tối thiểu khi cần. Stay có thể đến từ Stayora Booking, Airbnb, Booking.com, Owner Direct hoặc Sale/Zalo. Không tạo Booking Stayora giả chỉ để mọi Stay có cùng nguồn.

### Destination và Destination Operations

Destination định nghĩa context/capability/configuration. Destination Operations thực thi workflows trong context đó. Destination Operations không sở hữu commercial pricing, Sale commission hoặc Owner payout.

### Verification, Reputation và Incident

Identity & Authority giữ Identity verification và platform eligibility. Verification và Reputation giữ authority riêng cho Property-supply quality programs và accumulated reputation. Incident có thể tạo evidence/signal cho cả hai nhưng không trực tiếp sửa status, rating hay review. Resolution/accountability cần được ghi nhận ở Incident capability và được các domain liên quan tiêu thụ theo policy sau này.

## Relationship-level Sale access

Whitelist/Blacklist thuộc Distribution Relationship giữa Sale và Owner / Authorized Host trong inventory scope mà actor đó có Commercial Authority. Effective Permission còn phụ thuộc Property Policy và platform eligibility. Domain + Actor Authority checkpoint sau sẽ tinh chỉnh delegation, scope change và offboarding; Checkpoint 2 không tạo permission matrix kỹ thuật.

## Money naming question

Money được dùng như business area bao gồm Payment và Settlement. Chưa quyết định Payment và Settlement có tách thành bounded contexts riêng hay không. Không dùng bảng này để suy ra ledger schema, event model hoặc service boundary.
