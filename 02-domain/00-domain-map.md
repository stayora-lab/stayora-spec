# Domain Map — Stayora

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**

## 1. Bản đồ cấp cao

```text
FOUNDATIONAL CAPABILITY
└── Identity & Authority

COMMERCE NETWORK
├── Property
├── Inventory
├── Marketplace & Discovery
├── Booking
├── Distribution
└── Money — Payment & Settlement

OPERATING NETWORK
├── Stay
├── Destination
└── Destination Operations

TRUST SYSTEM
├── Verification
└── Reputation
```

`Commerce Network`, `Operating Network` và `Trust System` là grouping để giải thích mối quan hệ. Chúng không phải bounded contexts và không được dùng để suy ra technical service boundaries.

## 2. Mười hai top-level business domains

| Domain | Câu hỏi domain trả lời | Truth domain sở hữu |
|---|---|---|
| Identity & Authority | Ai là ai và người đó có authority nào? | Identity, role activation, delegation, platform eligibility, resource authority và scope |
| Property | Cơ sở lưu trú nào tồn tại và cấu trúc ra sao? | Accommodation structure, Bookable Unit definition, attributes, capacity, amenities, media, listing và associations |
| Inventory | Khi nào một Bookable Unit có thể được commit và availability được derived ra sao? | Bookable Unit × Time Inventory Truth, effective Inventory Commitments, Inventory Availability, temporary/confirmed commitments, blocks và external inventory signals |
| Marketplace & Discovery | Guest và demand nhìn thấy, tìm và so sánh gì? | Discovery/search composition và marketplace presentation |
| Booking | Commercial commitment nào đã được tạo? | Commercial parties, dates, Offer/price snapshot, conditions, source và booking commitment lifecycle |
| Stay | Ai thực sự đến/ở và operational lifecycle diễn ra thế nào? | Staying Party, actual arrival/departure, check-in/out, operational evidence |
| Destination | Địa điểm và local context nào đang được tổ chức? | Destination identity, membership, local capabilities/configuration, local policies và BQL relationships |
| Destination Operations | Stay được vận hành trong destination như thế nào? | Arrival, access, QR/gate, security, cart, checkout và operational coordination |
| Distribution | Demand, relationship và attribution được phân phối ra sao? | Sale/Affiliate networks, Sale ↔ Commercial Authority relationship, whitelist/blacklist, Lead và Attribution |
| Money — Payment & Settlement | Tiền di chuyển và được phân bổ thế nào? | Payment, refund, entitlement, commission, adjustment, reconciliation, settlement và payout |
| Verification | Stayora đã kiểm tra điều gì về Property-supply quality theo standard nào? | Application, inspection, evidence, standard/version và Verified lifecycle; không sở hữu Identity verification/platform eligibility |
| Reputation | Lịch sử interaction/stay nói gì về actor/property? | Review rights, reviews, dimensions, history và aggregated reputation signals |

## 3. Supporting và cross-cutting capabilities

### Distribution capabilities

Sale Network, Affiliate Network, Lead Management, Attribution và Sale ↔ Commercial Authority Holder relationship nằm dưới Distribution trong checkpoint này. Lead Management chưa phải top-level domain.

### Supporting capability

Incident & Resolution là capability hỗ trợ gắn với Stay / Destination Operations. Incident có thể phát sinh signal cho Reputation, Verification, Operations và support/remediation nhưng không sở hữu các truth đó.

### Cross-cutting capabilities

Policy, Audit, Notifications và Integration là cross-cutting mechanisms. Mỗi business domain sử dụng policy thuộc phạm vi của mình; không tạo một Policy domain khổng lồ.

## 4. Các boundary quan trọng

### Property ↔ Inventory

Property định nghĩa **WHAT** accommodation và Bookable Unit tồn tại. Inventory định nghĩa **WHEN** Bookable Unit có thể được commit. Property không phải nguồn availability truth.

Inventory Availability là derived truth từ effective Inventory Commitments trên Bookable Unit + time range. `AVAILABLE / HELD / BOOKED / BLOCKED` chỉ là conceptual availability semantics/projections; Checkpoint 2 không đóng chúng thành technical lifecycle enum. Inventory Commitment gồm Temporary Exclusive Commitment, Confirmed Accommodation Commitment và Availability Block. Request, Lead, Offer và Stay không phải Inventory Commitments.

### Booking ↔ Stay

Booking trả lời “commercial commitment nào đã được tạo?”. Stay trả lời “ai thực sự ở và lifecycle vận hành diễn ra thế nào?”. A Stay may exist without a Stayora Booking.

```text
Stayora Booking ──────┐
Airbnb Booking ───────┤
Booking.com Booking ──┤
Owner Direct ─────────┼──► Stay ──► Destination Operations
Sale / Zalo ──────────┘
```

External Booking là commerce record tạo bên ngoài; Inventory và/hoặc Stay chỉ reference hoặc ghi nhận tối thiểu khi cần để thiết lập Inventory Truth và/hoặc tạo operational Stay. Không cần tạo Stayora Booking cho External Booking.
Không ép External Stay đi qua Stayora Booking chỉ để thuận tiện mô hình hóa.

### Identity & Authority ↔ Distribution

Identity & Authority biết một người là approved Sale và authority nào người đó có. Distribution biết Sale có relationship whitelist/blacklist nào với Owner / Authorized Host. Platform eligibility không đồng nghĩa Host trust.

### Destination ↔ Destination Operations

Destination định nghĩa local capabilities/configuration và context. Destination Operations thực thi arrival, QR, gate, security, cart và checkout theo context đó.

### Booking ↔ Money

Booking giữ commercial commitment và snapshot liên quan. Money giữ payment, entitlement, commission, reconciliation, settlement và payout. `Booking Confirmed` không đồng nghĩa `Payment Received`, `Stay Completed`, `Commission Earned` hoặc `Paid`.

### Verification ↔ Reputation ↔ Incident

Identity & Authority sở hữu Identity verification và platform eligibility. Verification sở hữu evidence/standards/inspection cho các chương trình Property-supply quality như Stayora Verified. Reputation sở hữu lịch sử tương tác/stay tích lũy. Incident ghi nhận chuyện đã xảy ra và cách xử lý. Incident không trực tiếp rewrite Verified hoặc Reputation.

### Marketplace ↔ authoritative domains

Marketplace composes and presents. Property, Inventory, Verification và Reputation vẫn là source of truth tương ứng. Marketplace không tạo bản sao authoritative của availability, rating, Verified status hoặc Property information.

## 5. Offer không phải top-level domain

`Đề nghị đặt chỗ (Offer)` là conceptual business object dùng để mô tả một proposition trong context:

```text
Bookable Unit + dates + occupancy/context + Public Price + booking conditions
```

Marketplace có thể compose/present Offer. Khi Booking được commit, Booking giữ commercial snapshot liên quan. Ownership/aggregate design của Offer vẫn là open question; không thiết kế tại checkpoint này.

## 6. Money naming

Trong Checkpoint 2, `Money` là business area rộng gồm `Payment` và `Settlement`. Việc Payment và Settlement có trở thành hai bounded contexts riêng hay không vẫn là domain modeling question, không được ép thành technical split.
