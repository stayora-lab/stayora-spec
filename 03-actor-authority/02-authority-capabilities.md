# Nhóm năng lực quyền hạn — Authority Capabilities

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 8–10, 12–16.

## Mục đích và phạm vi

Ghi các capability family đã được duyệt ở mức business. Các ví dụ không phải technical permission enums hoặc fixed role bundles.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Capability families — CONFIRMED

| Family | Capability khái niệm | Giới hạn |
|---|---|---|
| Property Authority | View Property; edit information; publish/unpublish khi authorized | Ownership của thông tin thuộc Property; xem không tự có quyền sửa/publish |
| Inventory Authority | View availability; block/unblock; manage availability; establish authorized external commitments | Demand access không tạo quyền thay Inventory Truth |
| Booking Authority | View relevant Booking; accept/reject Request Booking; eligible booking actions | Co-host cần delegation rõ; Sale role không tự accept |
| Distribution Authority | Manage Sale relationships; whitelist/blacklist; relevant distribution delegation | Relationship Sale ↔ Commercial Authority holder trong scope của holder |
| Operations Authority | Assign/change Butler; manage stay preparation; coordinate operational information | Butler assignment không tự cho quyền đổi assignment của người khác |
| Financial Authority | Financial visibility; Settlement authority; Payout authority | Ba capability riêng; xem tiền không tự phân bổ hoặc chi tiền |
| Delegation Authority | Appoint Co-host; grant allowed capabilities; restrict/update; revoke | Không grant quyền mình không có; có thể có quyền non-delegable |

Mọi authority phải có capability, resource scope, lifecycle, source và auditability. Quyền kinh doanh (Commercial Authority) không đồng nghĩa legal ownership hoặc financial beneficiary.

## Record External Commitment — CONFIRMED

Đây là explicit authority capability thuộc Inventory Authority: ghi nhận external confirmed commitment hợp lệ trong granted scope. Sale role hoặc WHITELIST đơn lẻ đều không đủ. Sale được cấp rõ capability này có thể dùng đúng scope; audit giữ authority thực sự được dùng.

Sale thông thường có thể report/submit External Booking. Report đó chưa được tự đổi Inventory Truth thành BOOKED. Việc ghi nhận hợp lệ không được âm thầm overwrite inventory commitment không tương thích. External commerce vẫn nằm ngoài Booking domain Stayora.

**TBD — POLICY:** tiêu chí grant/revoke, evidence threshold và người xử lý report không đủ authority. Không đặt ra một approval workflow mới. Xem [WF-03](../04-core-workflows/03-external-booking-to-stay.md).

## Financial và operational boundaries — CONFIRMED

Primary Host không tự có financial visibility, Settlement authority hay Payout authority trên mọi khoản. Sale chỉ có economics thuộc Sale; Affiliate chỉ own economics cần thiết. Butler/Destination Staff ghi evidence không được tự áp financial/reputation consequences. Money sở hữu financial execution/ledger; actor cần authority tài chính phù hợp để thực hiện hành động liên quan.

## Phần còn mở và liên kết

**TBD:** danh mục non-delegable; exact finance grants; capability granularity và delegation policy. Xem [Delegation](04-delegation-and-scope.md), [Authority questions](07-open-authority-questions.md), [Domain Ownership](../02-domain/02-domain-ownership.md) và [Foundation financial boundaries](../01-product-foundation/06-ecosystem-and-actors.md).
