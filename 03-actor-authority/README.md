# STAYORA CHECKPOINT 3 — ACTOR AUTHORITY & CORE WORKFLOWS — REOPENED FOR RECONCILIATION — 2026-09-18

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 0–17, 27–30.

## Mục đích và phạm vi

Tổ chức các quyết định đã duyệt về quyền hạn kinh doanh (Business Authority). Phạm vi là actor, relationship, capability, resource scope và lifecycle; không phải mô hình phân quyền triển khai.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Nguồn ưu tiên và vị trí tài liệu

1. [Product Foundation](../00-start-here/README.md), gồm [Decision register](../00-start-here/DECISIONS.md).
2. [Domain Map + Domain Glossary](../02-domain/README.md).
3. Các quyết định Checkpoint 3 đã duyệt trong yêu cầu Founder; mỗi file chỉ rõ số mục nguồn.
4. Reference chỉ dùng khi không mâu thuẫn ba lớp trên. Stayora 2.0 và Grok không quyết định authority.

Canonical relationship: Foundation → Domain → Actor Authority → Core Workflows. Mỗi vùng liên kết trực tiếp tới vùng kế tiếp bằng relative links.

**CONFIRMED:** tài liệu ghi lại reasoning đã được duyệt; không tự quyết policy và không đóng các TBD.

## Đọc theo thứ tự

1. [Authority model](00-authority-model.md) — các phân biệt và công thức chung.
2. [Actor catalog](01-actor-catalog.md) — chín nhóm actor, nguồn authority và giới hạn.
3. [Capability families](02-authority-capabilities.md) — phân biệt inventory, booking, operations và finance.
4. [Actor–resource matrix](03-actor-resource-matrix.md) — business relationship, không phải bảng role cấp quyền.
5. [Delegation and scope](04-delegation-and-scope.md) — nguồn, phạm vi và vòng đời ủy quyền.
6. [Effective Permission](05-effective-permission.md) — xét quyền trên hành động cụ thể.
7. [Authority invariants](06-authority-invariants.md).
8. [Open questions và source discrepancies](07-open-authority-questions.md).
9. [Core Workflows](../04-core-workflows/README.md) — nơi authority được sử dụng.

## Ranh giới tài liệu

**CONFIRMED:** Role ≠ Authority ≠ Permission. Mỗi privileged action phải có authority context hợp lệ. Primary Host không tự thành financial beneficiary; staff không có quyền giả danh actor khác. Quyền vận hành không tự cho thấy commerce.

**TBD:** precedence giữa nhiều authority hợp lệ; policy cấp Record External Commitment; financial delegation; Affiliate approval; field-level access. Các capability là ngôn ngữ business, không là permission enums.

## Review và validation

Kết quả kiểm tra toàn gói được ghi tại [Workflow README](../04-core-workflows/README.md). Discrepancies của nguồn được ghi tại [Open Authority Questions](07-open-authority-questions.md); các timing, money và workflow gaps nằm tại [Open Workflow Questions](../04-core-workflows/08-open-workflow-questions.md).
