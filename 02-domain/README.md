# STAYORA CHECKPOINT 2 — DOMAIN MAP & DOMAIN GLOSSARY — REOPENED FOR RECONCILIATION — 2026-09-18

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint: 2 — Domain Map + Domain Glossary  
> Product Foundation: **STAYORA PRODUCT FOUNDATION — REOPENED FOR RECONCILIATION — 2026-09-18**
> Ngôn ngữ: Vietnamese-first + English canonical mapping

## Mục tiêu

Checkpoint này trả lời:

> Stayora gồm những business domain nào, mỗi domain sở hữu loại business truth nào, boundary giữa chúng ở đâu, và Stayora dùng thuật ngữ nào?

Tài liệu này chưa định nghĩa database, aggregate, API, UI, technical enum, detailed workflow, detailed permission matrix hay implementation architecture.

## Đọc theo thứ tự

1. [Domain Map](00-domain-map.md)
2. [Domain Glossary](01-domain-glossary.md)
3. [Domain Ownership Matrix](02-domain-ownership.md)
4. [Domain Invariants](03-domain-invariants.md)
5. [Open Domain Questions](04-open-domain-questions.md)

## Nguồn và ranh giới

- [Product Foundation overview](../01-product-foundation/00-overview.md)
- [Foundation decisions](../00-start-here/DECISIONS.md)
- [Foundation glossary](../00-start-here/GLOSSARY.md)
- [Foundation source of truth](../00-start-here/SOURCE_OF_TRUTH.md)

Foundation là nguồn ưu tiên cho các quyết định đã xác nhận. Tài liệu Domain không tự sửa Foundation để làm domain map dễ hơn. Nếu domain reasoning phát hiện ambiguity hoặc contradiction, ghi nhận tại [Open Domain Questions](04-open-domain-questions.md).

## Domain map tóm tắt

Stayora có 12 top-level business domains:

1. Identity & Authority
2. Property
3. Inventory
4. Marketplace & Discovery
5. Booking
6. Stay
7. Destination
8. Destination Operations
9. Distribution
10. Money — Payment & Settlement
11. Verification
12. Reputation

Visual grouping `Commerce Network`, `Operating Network` và `Trust System` chỉ giúp đọc hệ thống. Đây không phải bounded context hay technical architecture.

## Những điều checkpoint này không được làm

- Không nhập domain model cũ của Stayora 2.0.
- Không biến actor thành account type.
- Không biến conceptual state thành enum hoặc state machine kỹ thuật.
- Không đưa Lead Management hoặc Incident & Resolution thành top-level domain.
- Không tạo một domain “Trust” khổng lồ.
- Không dùng Marketplace làm nguồn sự thật thứ hai cho Property, Inventory, Verification hoặc Reputation.
- Không giải các câu hỏi TBD bằng cách chọn phương án có vẻ tiện triển khai.

## Kiểm tra cuối checkpoint

Tất cả tài liệu phải giữ được: marketplace mở; Owner Listed khác Stayora Verified; Managed ngoài current core; Sale khác Affiliate; One Public Price; 10% Sale base commission; request không reserve; External Booking là external concept được Inventory/Stay tham chiếu, không mặc định thuộc Stayora Booking; external booking có inventory authority; Booking khác Stay; Destination first-class; access theo role + relationship + resource scope; Identity Verification khác Stayora Verified; Verification khác Reputation; và legal/tax/payment implementation vẫn `legal-validation-required / TBD`.
