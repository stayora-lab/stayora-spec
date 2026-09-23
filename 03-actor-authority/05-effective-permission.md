# Quyền hiệu lực — Effective Permission

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 5, 10, 14, 16–19.

## Mục đích và phạm vi

Diễn đạt việc đánh giá authority theo từng hành động cụ thể. Công thức là khái niệm business, không thiết kế RBAC/ABAC/ReBAC.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Thành phần — CONFIRMED

```text
Identity + Platform Eligibility + Actor Relationship
+ Authority Capability + Resource Scope + Authority Lifecycle
+ Resource / Destination Policy + Transaction Context
= Effective Permission
```

Role không trực tiếp imply permission. Cần xác định actual actor/acting capacity; relationship và nguồn authority; capability, scope và lifecycle còn hợp lệ; policy/context của hành động. Đây là các chiều cần xét, không phải thuật toán ưu tiên hoặc thứ tự triển khai bắt buộc.

## Các tình huống — CONFIRMED

| Tình huống | Kết luận đã có từ nguồn | Điều chưa được tự suy ra |
|---|---|---|
| Sale muốn tạo Request Booking | Có thể khi eligibility, relationship và transaction hợp lệ; Request không giữ inventory | Request không thành Inventory Commitment |
| Sale dùng Instant Book | Cần Sale Platform Eligibility/ELIGIBLE (CP3 `ACTIVE` wording maps to this effective eligible capability) + appropriate Distribution Relationship + WHITELIST + Property Instant Book enabled + transaction eligible | WHITELIST riêng lẻ không đủ; exact eligibility policy TBD |
| Direct Guest dùng Instant Book | Có thể khi eligible; Host đã pre-authorize qua policy | Không áp Sale whitelist cho Guest |
| Sale muốn record external confirmed | Explicit Record External Commitment authority trong scope là điều kiện | Sale role/whitelist/report không tự đổi Inventory Truth |
| Sale đồng thời là Co-host accept Request | Chỉ accept bằng delegated Booking Authority hợp lệ | Audit không nói Sale role có authority accept |
| Butler assert Ready | Operational assertion trong assignment/capability hợp lệ | Ready không đảm bảo zero defects và không chốt trách nhiệm tài chính |
| Guest có QR | Dùng credential/evidence cùng recognized Stay relationship/lifecycle để xét access | QR không tạo authority vô hạn hoặc công khai PII |
| Staff hỗ trợ Host | Cần legitimate function/domain/resource authority; actual staff được audit | Administrative Access không đồng nghĩa impersonation |

Instant Book được mô tả tại [WF-02](../04-core-workflows/02-instant-book.md); eligibility phải được đánh giá tại transaction time, không kế thừa vĩnh viễn từ lúc whitelist.

## Human Authority và Platform Policy Enforcement — CONFIRMED

Policy enforcement không là một người giả danh Host. Mỗi hành động policy phải có căn cứ và audit được, ví dụ hold expiry do policy, Verification lifecycle enforcement trong Verification hoặc Review Right generation trong Reputation. Restrict platform eligibility không chuyển Commercial Authority của Property cho platform.

## Data access — CONFIRMED boundary

Operational Visibility ≠ Commercial Visibility. Financial/Guest data theo relationship, capability, resource và lifecycle. Booking Creator, Payer, Lead Guest và Staying Party có thể khác nhau; access phải xét đúng relationship. Nhánh Guest operational disclosure của WF-01 đi theo relationship/operational need; field-level timing, expiry và retention vẫn **TBD**, xem [source-status note](07-open-authority-questions.md#review-status).

## Xung đột chưa giải

**TBD:** precedence khi có nhiều valid authorities; policy cụ thể cho eligibility và data fields. Grant/restriction không hợp lệ không có hiệu lực. Nguyên tắc đó không cung cấp winner rule cho các nguồn authority đều hợp lệ.

Nguồn: [Foundation Actors](../01-product-foundation/06-ecosystem-and-actors.md), [Domain invariants](../02-domain/03-domain-invariants.md), [Authority Model](00-authority-model.md), [Delegation](04-delegation-and-scope.md), [Open questions](07-open-authority-questions.md).
