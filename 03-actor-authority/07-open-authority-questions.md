# Câu hỏi quyền hạn và review nguồn

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 0, 17, 27–30.

## Mục đích và phạm vi

Giữ công khai phần authority còn thiếu và source discrepancy. Chỉ ghi nhận; không chọn bên khi có status conflict.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Authority questions

| ID | Status | Phần còn mở | Dependency |
|---|---|---|---|
| AQ-01 | TBD | Precedence giữa nhiều authorities hợp lệ trên cùng action/resource | Conflict policy; không dùng restrictive-wins |
| AQ-02 | TBD — POLICY | Tiêu chí/người có quyền grant/revoke Record External Commitment; evidence nguồn | [WF-03](../04-core-workflows/03-external-booking-to-stay.md) |
| AQ-03 | TBD — future-policy question | Chứng cứ authority Primary Host, transfer/offboarding/dispute, propagation khi source đổi | Delegation và continuity của Booking/Stay |
| AQ-04 | TBD — future-policy question | Danh mục non-delegable; financial visibility/settlement/payout grants; beneficiaries | Sensitive authority, không mặc định Primary Host nhận tiền |
| AQ-05 | TBD | Affiliate onboarding approval, attribution/eligibility chi tiết | Không auto-activate hoặc miễn approval |
| AQ-06 | TBD — future-policy question | Guest recognition, QR expiry/revoke/forwarding, field-level disclosure/retention | Privacy: legal-validation-required |
| AQ-07 | TBD — future-policy question | Butler assignment change/shift, Destination Staff onboarding và local policy authority | Không global hóa Oceanami max-two rule |
| AQ-08 | TBD — future-policy question | Staff function grants, agency/delegation hợp lệ, authority xác nhận payment/completion | Không silent impersonation hoặc admin-all |
| AQ-09 | TBD — future implementation | RBAC/ABAC/ReBAC, data model/entities/tables | Ngoài documentation pass; không thiết kế ở đây |

## Discrepancies của current source historys — OPEN REVIEW

### R-01 — Freeze metadata — RESOLVED

Cả 18 file trong [00-start-here](../00-start-here/README.md) và [01-product-foundation](../01-product-foundation/00-overview.md) nay thống nhất metadata REOPENED FOR RECONCILIATION — 2026-09-18 và wording current reconciliation status.

Các vị trí prose cụ thể khác:

Các stale status/prose đã được sửa ở đúng các file nêu trên. TBD/WORKING MODEL/HYPOTHESIS bên trong vẫn giữ nguyên; freeze artifact không freeze từng policy.

### R-02 — ADR-P036 status — RESOLVED

[DECISIONS](../00-start-here/DECISIONS.md), “Decision index”, [phần ADR-P036](../00-start-here/DECISIONS.md#adr-p036) và [Money Model](../01-product-foundation/09-money-model.md) nay cùng ghi ADR-P036 là WORKING MODEL. Nội dung chỉ là product intent; legal entity/intermediary treatment vẫn legal-validation-required/TBD.

<a id="review-status"></a>
### R-03 — Progressive disclosure: principle vs policy — RESOLVED

[Foundation Actors](../01-product-foundation/06-ecosystem-and-actors.md) nay ghi rõ CONFIRMED PRINCIPLE: Guest operational data được progressive disclosure theo relationship, lifecycle, operational need và authority/scope. Exact fields, actors, timing, retention, masking và implementation là TBD / POLICY; không phải field-level matrix đã freeze. WF-01 dùng đúng distinction này.

### R-04 — Số lượng ADR — RESOLVED

[Start Here README](../00-start-here/README.md), “Đọc theo thứ tự”, nay tham chiếu [Decision register](../00-start-here/DECISIONS.md) mà không nhắc lại số lượng ADR. Cách này loại bỏ cả lớp lỗi số lượng bị lệch mỗi khi register thay đổi, không chỉ sửa một lần. Đây chỉ là documentation correction.

## Điều không phải contradiction mới

Blacklist trong [Domain Invariants](../02-domain/03-domain-invariants.md), mục 3 invariant 17, có hiệu lực trong commercial scope hợp lệ. Rule này không tự giải conflict precedence giữa nhiều valid authorities. Không biến nó thành global restrictive-wins.

Các câu hỏi frozen về detailed delegation được refinement bởi prompt chỉ trong phần principle đã duyệt; phần policy còn mở ở bảng AQ. Source history differences không bị xóa chỉ vì tài liệu mới đã viết.

## Liên kết

[Authority model](00-authority-model.md), [Delegation](04-delegation-and-scope.md), [Foundation open questions](../01-product-foundation/13-open-questions.md), [Domain questions](../02-domain/04-open-domain-questions.md), [Workflow review](../04-core-workflows/08-open-workflow-questions.md).
