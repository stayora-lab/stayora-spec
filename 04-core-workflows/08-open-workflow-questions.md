# Câu hỏi workflow và review nguồn

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 0, 18–30.

## Mục đích và phạm vi

Giữ rõ các policy, evidence và workflow details chưa có quyết định. Không tự giải từ giả định implementation hoặc reference cũ.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Register — các câu hỏi vẫn mở

| ID | Status | Nội dung cần quyết định / nguồn chưa đủ | Workflow |
|---|---|---|---|
| WQ-01 | TBD — POLICY | Exact Temporary Inventory Commitment window, late/partial/overpayment, acceptance/payment race và release exceptions; Payment Session/Attempt UNKNOWN handling | WF-01 |
| WQ-02 | TBD — future implementation | Technical Instant Book locking, concurrency implementation; checkpoint chỉ giữ business protection invariant | WF-02 |
| WQ-03 | TBD — POLICY | Record External Commitment grant/revoke criteria; evidence/report adjudication, creation timing của external Stay | WF-03; [AQ-02](../03-actor-authority/07-open-authority-questions.md) |
| WQ-04 | WORKING MODEL / future-policy question | Lead dispatch 5–10s, Lead SLA 24h/+24h chưa final; exact timings/algorithm TBD | WF-01 / Distribution |
| WQ-05 | TBD | Affiliate onboarding approval; attribution eligibility/window/fraud details | Authority / Distribution |
| WQ-06 | TBD — POLICY | Incident taxonomy/severity; response/resolution authority, appeals và consequence eligibility | WF-05 |
| WQ-07 | TBD — POLICY | Exact exceptions blocking completion; ai xác nhận completion, evidence và dispute window | WF-04/WF-06 |
| WQ-08 | TBD — POLICY | Partial settlement during disputes, cancellation/no-show/early-departure/Payment Default/chargeback economics, exception eligibility and payout failures | WF-06 |
| WQ-09 | TBD | Commissionable Booking Value definition; discount/tax/base treatment | WF-01/WF-02/WF-06 |
| WQ-10 | WORKING MODEL; exact values TBD | Affiliate/Sale split, Stayora platform fee, performance incentive; không final hóa ~3%/~5%/~2% | WF-06 |
| WQ-11 | TBD — POLICY; legal-validation-required khi liên quan | Cancellation/refund percentages, deadlines, Instant Book wording và supplier failure remedies | WF-01/WF-02/WF-06 |
| WQ-12 | TBD — POLICY | Exact Security/Damage Deposit amount/claim/refund mechanics, add-on economics | WF-05/WF-06 |
| WQ-13 | TBD — future implementation | RBAC/ABAC/ReBAC, exact data model/entities/tables; không thiết kế DB/API/UI/infrastructure | Toàn checkpoint |
| WQ-14 | TBD — future-policy question | Authority conflict precedence giữa nhiều valid authorities | Toàn checkpoint; [AQ-01](../03-actor-authority/07-open-authority-questions.md) |
| WQ-16 | TBD | Recipient/channel/timing của Notifications; business audit retention/evidence details | Cả sáu workflow |
| WQ-17 | TBD | External evidence threshold, duplicates/conflict, sync health và inventory confidence mechanics; cadence iCal 15 phút chỉ WORKING MODEL | WF-03 |
| WQ-18 | TBD | Review Right eligibility/recipient/evidence; Verification consuming signals/lifecycle criteria | WF-03/WF-04/WF-05 |
| WQ-19 | TBD · legal-validation-required | Payment confirmation authority/evidence, Required Payment Condition, collection/holding rights, provider/rails and UNKNOWN/reconciliation handling, legal entity, tax/accounting/invoice/privacy | WF-01/WF-02/WF-06 |
| WQ-20 | TBD — future-policy question | Guest/Butler/Destination lifecycle access, offline/QR, assignment changes và actual Stay deviations | WF-03/WF-04 |

WQ IDs chỉ là mục tra cứu tài liệu, không technical enums hoặc quyết định đã đóng. Các missing details không ngăn documentation pass nhưng không cho phép implementation tự chọn policy.

<a id="wq-15"></a>
## WQ-15 — Reconciliation boundary — RESOLVED / CONFIRMED

Operational Completion Readiness thuộc Stay và chỉ trả lời liệu Stay đã đủ operational closure để trở thành STAY COMPLETED. Financial Reconciliation thuộc Money. Normal path xảy ra sau STAY COMPLETED; policy-driven Economic Eligibility có thể mở exception path cho commercially fulfilled/no-use hoặc trường hợp được policy cho phép mà không tạo Completed giả. Operational readiness không tính payout, commission, revenue, refund allocation hoặc settlement positions.

## Source discrepancies và status risks

[Authority source review](../03-actor-authority/07-open-authority-questions.md) ghi resolution notes cho R-01–R-04. Các điểm đó đã được sửa trong scope correction pass; các TBD khác vẫn mở.

Ngoài những điểm trên, regression review phải phân biệt current rules với lịch sử SUPERSEDED/negative examples. Foundation có nhắc 30/70, Request reserve hoặc Direct premium dưới lịch sử đã supersede; không nhập lại vào workflow.

## Phạm vi status đã có

**CONFIRMED:** authorized acceptance có thể tạo Temporary Inventory Commitment hữu hạn; Payment Session/Attempt tách khỏi commitment; Required Payment Condition không đồng nghĩa Fully Paid; 10% Sale base, external inventory authority, Checkout ≠ Completed, Completed là normal eligibility boundary, Financially Reconciled ≠ Settled, Settled ≠ Paid, Settlement khác Payout. Các nguyên tắc đó không xác nhận commitment window, commission base definition, exact exception economics hoặc tax treatment.

**WORKING MODEL/TBD:** facilitated collection là collection rail, không mặc định 100% tại confirmation; Affiliate split, platform fee, incentive, lead timings, provider UNKNOWN/reconciliation và exception economics giữ nguyên. Source insufficiency về notifications, evidence, actor completion authority và failure remedy được nêu ngay trong từng workflow, không invent answers.

## Nguồn và liên kết

[Foundation open questions](../01-product-foundation/13-open-questions.md), [Domain open questions](../02-domain/04-open-domain-questions.md), [Money Model](../01-product-foundation/09-money-model.md), [Workflow README](README.md), [Cross-workflow invariants](07-cross-workflow-invariants.md), [Authority questions](../03-actor-authority/07-open-authority-questions.md).
