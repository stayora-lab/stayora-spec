# Product Principles

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P001](../00-start-here/DECISIONS.md#adr-p001), [ADR-P002](../00-start-here/DECISIONS.md#adr-p002), [ADR-P004](../00-start-here/DECISIONS.md#adr-p004), [ADR-P006](../00-start-here/DECISIONS.md#adr-p006), [ADR-P013](../00-start-here/DECISIONS.md#adr-p013), [ADR-P015](../00-start-here/DECISIONS.md#adr-p015), [ADR-P020](../00-start-here/DECISIONS.md#adr-p020), [ADR-P021](../00-start-here/DECISIONS.md#adr-p021), [ADR-P025](../00-start-here/DECISIONS.md#adr-p025), [ADR-P027](../00-start-here/DECISIONS.md#adr-p027), [ADR-P029](../00-start-here/DECISIONS.md#adr-p029), [ADR-P035](../00-start-here/DECISIONS.md#adr-p035)

## Principles đã xác nhận

| Principle — CONFIRMED | Hệ quả trong Foundation | Không tự suy ra |
|---|---|---|
| Marketplace mở | Owner Listed và Verified đều có chỗ trong marketplace | Không cần identity/compliance |
| Reputation đi theo trách nhiệm | Tách villa/Host, Sale, Butler, destination services | Mọi incident tự trừ sao mọi bên |
| Verified là trust, không luxury | Đúng mô tả/chất lượng cam kết quan trọng hơn phân khúc giá | Checklist final hoặc badge vĩnh viễn |
| Sale là actor trung tâm | Bảo vệ vai trò tư vấn/distribution và commission minh bạch | Sale được tự accept thay Host |
| Một identity có nhiều role | Role và relationship được phân biệt | Gộp quyền mọi role cho mọi resource |
| Request không reserve | Pending request không chiếm villa-night | Authorized acceptance phải revalidate availability; Payment Session/Attempt không tự tạo Inventory Commitment |
| Một villa-night một truth | External confirmed có cùng inventory authority | Bảo đảm realtime trên mọi OTA |
| Booking, Payment, Stay, Settlement riêng | Accept, tiền đến, lưu trú và payout không cùng một trạng thái | State machine đã hoàn tất |
| Completed là normal settlement eligibility boundary | Confirmation/check-in không tự kích hoạt payout | Checkout lập tức chuyển tiền; no-show/default exception economics vẫn TBD |
| Access theo role/relationship | Financial và Guest data chỉ trong scope cần thiết | Minh bạch là công khai tất cả |
| Core khác destination policy | Oceanami configuration không định nghĩa toàn platform | Destination tự override mọi global rule |
| Operational penetration trước commerce dominance | External operations có giá trị trong pilot | Không cần đo commerce/economics |
| Không ép price floor | Owner chọn chiến lược; Guest nhìn thấy chất lượng và giá | Hidden spread được chấp nhận |

## Principles diễn đạt ở mức working model

**WORKING MODEL.** “Utility before enforcement”; “Stayora không cần sở hữu booking để biết operational truth”; “dữ liệu tương xứng với trách nhiệm”. Đây là cách tổng hợp các quyết định hiện hành, không tạo quyền mới hoặc cơ chế thương mại mới.

## Quy tắc biên tập và triển khai về sau

**CONFIRMED — governance của checkpoint.** Giữ decision status tại nơi rule được dùng. Không copy con số reference thành requirement. Không dùng UI/schema/code cũ để lấp TBD. Khi hai nguồn xung đột, ghi cả hai và nêu quyết định cần founder; không tự “chọn cách hợp lý nhất”.

Trước khi viết spec phụ thuộc, đọc [Decision register](../00-start-here/DECISIONS.md), [scope](12-scope-boundaries.md) và [open questions](13-open-questions.md). Khi domain và code khác nhau phải reconcile công khai; không để implementation âm thầm đổi product.
