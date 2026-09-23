# Mô hình quyền hạn — Authority Model

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 5–8, 14, 16–17.

## Mục đích và phạm vi

Định nghĩa cách authority phát sinh và được dùng trong một hành động. Giữ phân biệt giữa Identity, Role, relationship và quyền thực tế trên resource.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Những phân biệt — CONFIRMED

| Khái niệm | Ranh giới phải giữ |
|---|---|
| Danh tính (Identity) / Tác nhân (Actor) | Một Identity có thể tham gia nhiều vai trò (Role) và relationship; actor là người/tổ chức thực sự hành động. |
| Owner ≠ Primary Host ≠ Authority | Legal Owner không nhất thiết là Chủ nhà chính (Primary Host); ownership không tự cấp mọi capability. |
| Primary Host ≠ Financial Beneficiary | Authority anchor của Property không mặc nhiên nhận Owner entitlement, Settlement hay Payout. |
| Role ≠ Authority; Role ≠ Permission | Nhãn Sale/Butler/Staff không trực tiếp cấp quyền hành động. |
| Sale Platform Eligibility ≠ Sale–Host Distribution Relationship ≠ Transaction Eligibility | Approval, trust relationship và điều kiện giao dịch là ba lớp khác nhau. |
| Butler Role ≠ Butler Assignment ≠ Stay Access | Approved Butler còn cần assignment và phạm vi Stay phù hợp. |
| Affiliate Attribution ≠ Transaction Authority | Mang demand không tạo quyền thương lượng, Booking hoặc Inventory. |
| Operational Visibility ≠ Commercial Visibility | Dữ liệu phục vụ arrival không bao gồm ledger hoặc economics mặc định. |
| Identity Verification ≠ Stayora Verified | Identity & Authority sở hữu xác minh danh tính/eligibility; Verification sở hữu Property-supply quality assurance. |
| Booking Creator ≠ Payer ≠ Lead Guest ≠ Staying Party | Người tạo, người trả tiền, khách đầu mối và nhóm khách lưu trú có thể khác nhau. Không suy quyền của người này từ người khác. |
| Administrative Access ≠ Business Authority ≠ Impersonation Authority | Quyền quản trị không thay nguồn authority hay cho phép âm thầm hành động dưới tên Host. |

## Công thức khái niệm — CONFIRMED

```text
Identity
+ Platform Eligibility
+ Actor Relationship
+ Authority Capability
+ Resource Scope
+ Authority Lifecycle
+ Resource / Destination Policy
+ Transaction Context
──────────────────────────────
Effective Permission
```

Dấu cộng biểu thị các thành phần cần xem xét cùng nhau, không là phép cộng quyền. Mọi privileged action phải giải thích được actor nào, trong tư cách nào, dùng capability từ nguồn nào, đối với resource nào và trong lifecycle/context nào. [Effective Permission](05-effective-permission.md) ghi các tình huống cụ thể.

## Authority anchor và acting capacity — CONFIRMED

Mỗi Property có đúng một Primary Host tại một thời điểm trong Stayora authority context. Primary Host là authority anchor, phải có nguồn authority chính đáng; không nhất thiết là Legal Owner và không tự có mọi financial capability.

Ví dụ Nguyễn A vừa là Sale, vừa là Co-host Villa 07. Nếu A quản lý Inventory nhờ delegation Co-host, audit phải ghi acting capacity Co-host và authority đó. Không ghi hành động như quyền có sẵn của Sale, cũng không mặc định hợp nhất mọi role thành quyền trên mọi villa.

Audit của privileged action giữ actual actor, acting capacity, authority source, reason/policy, resource và time. Platform Policy Enforcement có provenance policy riêng; không gán giả cho Host.

## Chưa quyết định

**TBD:** chứng cứ nguồn authority, transfer Primary Host, precedence giữa nhiều authority hợp lệ và danh mục non-delegable capabilities. Không dùng quy tắc đã bị loại “More restrictive authority always wins”. Grant/restriction chỉ có hiệu lực khi người ban hành/thực hiện có authority hợp lệ trên đúng action và resource scope.

## Nguồn và liên kết

[Foundation Actors](../01-product-foundation/06-ecosystem-and-actors.md), [Domain Glossary](../02-domain/01-domain-glossary.md), [Delegation](04-delegation-and-scope.md), [Open Authority Questions](07-open-authority-questions.md).
