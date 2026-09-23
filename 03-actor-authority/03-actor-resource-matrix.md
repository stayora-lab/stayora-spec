# Ma trận Actor–Resource ở mức business

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 5–16.

## Mục đích và phạm vi

Làm rõ actor cần relationship nào với resource nào. Mỗi hàng là điều kiện business cần xét, không phải kết quả cấp quyền tự động từ Role.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Ma trận — CONFIRMED boundaries

| Actor / acting capacity | Resource scope | Căn cứ authority cần có | Hành động / visibility có thể liên quan | Ranh giới |
|---|---|---|---|---|
| Legal Owner | Property liên quan | Authority chính đáng được xác lập | Theo capability được xác lập | Legal title không tự cấp mọi quyền platform |
| Primary Host | Property và phạm vi hợp lệ | Primary Host authority có nguồn hợp lệ | Hosting/commercial responsibility, delegation được phép | Không suy ra finance beneficiary |
| Co-host | Property / Bookable Unit / Booking / Stay được grant | Delegation capability + scope + lifecycle | Chỉ các việc được grant, có thể gồm Inventory hoặc accept/reject | Không sao chép mọi quyền Primary Host |
| Sale — distribution | Offer, Lead, relevant Booking/availability | Platform eligibility + Sale–Commercial Authority relationship + transaction context | Search, Offer, Request; Instant Book khi đủ toàn bộ điều kiện | Không block/accept từ Sale role |
| Sale — external commitment capability | Inventory trong granted scope | Explicit Record External Commitment authority | Ghi external confirmed commitment hợp lệ | WHITELIST không thay grant; report thường không đổi BOOKED |
| Sale — own economics | Entitlement liên quan của chính Sale | Own economic relationship | Xem phần mình, fund discount từ phần mình | Không Owner ledger/payout hoặc economics Sale khác |
| Butler | Property/Stay được assign | Operational assignment còn phù hợp + capability | Preparation, Ready, events, Check-in/out coordination, Incident report | Không commercial acceptance/finance hoặc tự áp hậu quả |
| Guest | Booking và/hoặc Stay liên quan | Recognized relationship + lifecycle + context | Narrow access/participation, eligible Review Rights | QR không là authority; participant không tự là Payer |
| Affiliate | Attribution/own entitlement | Attributed relationship; onboarding policy TBD | Own economics cần thiết | Không Guest operations, Inventory hoặc transaction authority |
| Destination Staff | Destination và functions được giao | Destination Staff Relationship + capability | Access/QR/guest/vehicle data phục vụ function | Không global BQL, Owner payout hoặc Sale commission |
| Stayora Staff | Domain/resource theo function | Legitimate Human Authority | Hành động đặc quyền trong scope | Audit actual staff; không giả danh Host/Sale/Guest/Butler |
| Platform Policy Enforcement | Resource mà policy hợp lệ áp dụng | Policy và domain sở hữu | Eligibility restrictions, hold expiry, eligible review generation | Auditable; không nhận Commercial Authority Property |

Property và Đơn vị có thể đặt (Bookable Unit) không đồng nhất: Property scope không được dùng để bỏ qua scope cụ thể của hành động. Inventory Truth thuộc Bookable Unit × Time; exact interval semantics vẫn TBD từ Domain.

## Ví dụ kiểm tra authority — CONFIRMED

Nguyễn A có Sale role và Co-host relationship Villa 07 với Inventory capability được grant. A quản lý availability Villa 07 bằng Co-host authority; audit không quy hành động cho Sale. Không từ đó suy ra A có Inventory Authority Villa 08.

Security Oceanami có thể cần QR/guest/vehicle information phục vụ access. Cùng thông tin Stay không cho phép mở commercial economics. Từng hành động tiếp tục đi qua [Effective Permission](05-effective-permission.md).

## Phần chưa có ma trận cuối

**TBD:** field-level visibility, retention, delegation propagation, finance capabilities cụ thể và conflict precedence. Không điền ô trống bằng allow/deny kỹ thuật. Tham chiếu [Foundation Actors](../01-product-foundation/06-ecosystem-and-actors.md), [Domain Glossary](../02-domain/01-domain-glossary.md), [Capability families](02-authority-capabilities.md), [Open Authority Questions](07-open-authority-questions.md).
