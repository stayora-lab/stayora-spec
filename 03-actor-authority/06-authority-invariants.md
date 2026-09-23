# Các bất biến quyền hạn — Authority Invariants

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 5–17, 26–27.

## Mục đích và phạm vi

Tập hợp các ranh giới đã duyệt để đọc workflow không suy ra quyền mới. CONFIRMED ở mức business; policy chi tiết tiếp tục mở.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Invariants — CONFIRMED

1. Owner ≠ Primary Host ≠ Authority; Legal Owner không nhất thiết là Primary Host.
2. Mỗi Property có đúng một Primary Host tại một thời điểm trong Stayora authority context; nguồn authority phải chính đáng.
3. Primary Host ≠ automatic Financial Beneficiary; hosting không tự cấp Settlement/Payout authority.
4. Role ≠ Authority; Role ≠ Permission. Privileged action luôn cần authority context hợp lệ.
5. Một Identity có thể nhiều role/relationships; audit giữ acting capacity thực sự được dùng.
6. Co-host là delegated relationship; capability, resource scope, lifecycle, source và auditability phải rõ.
7. Không delegate quyền mình không có; possession không bảo đảm delegability.
8. Sale Platform Eligibility ≠ Sale–Host Distribution Relationship ≠ Transaction Eligibility.
9. NORMAL/WHITELIST/BLACKLIST thuộc Distribution Relationship Sale ↔ Commercial Authority holder trong scope hợp lệ, không property-only.
10. Whitelist không là Instant Book permission bundle và không là Record External Commitment authority.
11. Demand access không tạo Inventory Authority. Sale role không tự block hoặc accept thay Host.
12. Report External Booking không tự tạo BOOKED; ghi commitment cần explicit capability trong scope.
13. Butler Role ≠ Butler Assignment ≠ Stay Access; Butler không tự là Stayora staff.
14. Operational Visibility ≠ Commercial Visibility; evidence không cấp quyền áp financial/reputation consequence.
15. Destination Staff authority có destination/function scope; không có global BQL authority.
16. Guest authority từ Booking và/hoặc Stay relationship và lifecycle; không bắt buộc full account chỉ để tham gia Stay.
17. QR là credential/evidence dùng xét access, không authority tự thân.
18. Booking Creator ≠ Payer ≠ Lead Guest ≠ Staying Party.
19. Affiliate Attribution ≠ Transaction Authority; own economics không mở Host finance/Guest operations.
20. Administrative Access ≠ Business Authority ≠ Impersonation Authority; staff không âm thầm giả danh actor khác.
21. Privileged human action giữ actual actor, acting capacity, authority source, reason/policy, resource, time; platform policy actions cũng auditable.
22. Platform restriction không trao Property Commercial Authority cho platform.
23. Grant/restriction chỉ có hiệu lực với authority hợp lệ trên action/resource; không dùng “More restrictive authority always wins”.
24. Identity Verification ≠ Stayora Verified; hai trách nhiệm ở Identity & Authority và Verification.
25. Domain có thể consume truth của domain khác nhưng không tạo source of truth thứ hai.

## Còn mở

**TBD:** conflict precedence, non-delegable list, external commitment grant/revoke policy, financial delegation, field-level access và authority lifecycle propagation. Các invariants không đóng những câu hỏi đó.

Nguồn: [Foundation principles](../01-product-foundation/04-product-principles.md), [Domain invariants](../02-domain/03-domain-invariants.md). Liên quan: [Capability families](02-authority-capabilities.md), [Effective Permission](05-effective-permission.md), [Authority questions](07-open-authority-questions.md), [Cross-workflow invariants](../04-core-workflows/07-cross-workflow-invariants.md).
