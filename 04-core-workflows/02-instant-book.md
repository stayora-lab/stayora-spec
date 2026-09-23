# WF-02 — Instant Book

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 19, 26–27.

## Mục đích và phạm vi

Ghi cơ chế Booking theo Host pre-authorization thể hiện qua policy. Áp dụng cho eligible Direct Guest và Sale, với eligibility khác nhau; không thiết kế locking.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Purpose

**CONFIRMED:** Instant Book là Booking capability, không chỉ Guest feature. Host pre-authorization qua policy thay cho accept từng request; Host authority vẫn tồn tại.

## Actors

Direct Guest hoặc Sale eligible; Primary Host/authority hợp lệ phía Host làm căn cứ pre-authorization; Money thực hiện financial execution; Stay/Butler/Destination Operations tiếp nhận sau confirmation.

## Preconditions — CONFIRMED

Sale cần đồng thời:

```text
Sale Platform Eligibility / ELIGIBLE (older CP3 `ACTIVE` wording maps to this effective eligible capability)
+ appropriate Distribution Relationship
+ WHITELIST
+ Property Instant Book enabled
+ transaction eligible
```

Eligibility được xét tại transaction time. WHITELIST không là permission bundle. Direct Guest có thể sử dụng khi eligible; không tự áp Sale whitelist rule cho Direct Guest. Exact transaction eligibility policy **TBD**.

## Trigger

Eligible actor chọn commitment Instant Book trên Offer và thể hiện explicit consent đối với material price/conditions.

## Happy Path — CONFIRMED

```text
Actor → Offer → Instant Book eligibility → explicit consent
→ Payment Session / Attempt
→ Required Payment Condition satisfied
→ other applicable Booking Confirmation Conditions satisfied
→ Booking Confirmed → Inventory Availability recomputed → Stay Created/Scheduled
```

1. Xét eligibility và Host pre-authorization/policy trên Property/context phù hợp.
2. Thể hiện material price/conditions và lấy explicit auditable consent. Confirmed commercial intent không hủy/không đổi phải rõ trước commitment; exact wording/remedies vẫn TBD · legal-validation-required.
3. Revalidate Inventory ngay trước commitment. Inventory phải được bảo vệ đủ để tránh conflicting confirmed commitments; không tạo Sale-controlled long hold.
4. Required Payment Condition phải được thỏa mãn cho normal Instant Book confirmation; không mặc định là 100% payment. Booking giữ commercial snapshot, Inventory giữ commitment/availability truth.
5. Tạo/schedule Stay; cùng lifecycle vận hành như commerce paths khác sau confirmation.

Sơ đồ không định nghĩa technical ordering/locking hoặc cách xử lý atomicity; không suy Temporary Inventory Commitment duration hay Payment Session implementation từ flow này.

## Alternative Paths

**CONFIRMED:** Direct Guest và eligible Sale dùng cùng commitment model nhưng khác eligibility rules. Một Offer qua Sale có thể có Sale-funded discount hợp lệ theo [WF-01](01-sale-assisted-request-booking.md); không mặc định có discount Direct Instant Book.

## Failure Paths

Không đủ eligibility, thiếu consent, Required Payment Condition không được thỏa mãn hoặc Inventory không còn hợp lệ không đủ cơ sở cho normal confirmation. **TBD:** exact failure handling, inventory/payment conflict, timeout, late payment, cancellation/remediation. Không tự chọn locking strategy, refund amount hoặc winner rule.

## Authority

Pre-authorization bắt nguồn Host authority qua policy; không có nghĩa Sale nhận Booking acceptance authority. Hành động privileged và consent phải auditable. [Effective Permission](../03-actor-authority/05-effective-permission.md) xét authority lifecycle, relationship và context hiện tại.

## Domain Truth Changes

**CONFIRMED:** Booking owns commercial snapshot; Money owns financial execution; Inventory owns availability/commitment truth; Stay owns operational truth. Distribution giữ Sale relationship/attribution khi có. Marketplace trình bày Offer nhưng không thành authoritative availability source.

## Money Changes

Payment success không tự là revenue hoặc Earned/Paid economics. Booking Confirmed tạo expected/pending economics; downstream theo [WF-06](06-completion-settlement-payout.md). Collection rails và xác minh payment cụ thể còn **TBD / legal-validation-required**; facilitated collection 100% vẫn **WORKING MODEL** theo Foundation.

## Notifications

**TBD:** recipient/channel/timing cho payment result, confirmation và preparation. Explicit consent là requirement business đã duyệt, không tự chuyển thành screen hoặc notification design.

## Audit Events

Các mốc cần trace về business: eligibility/context được dùng, Host pre-authorization/policy, material price/conditions và consent, inventory validation, payment evidence, commercial snapshot/confirmation và Stay scheduling. Privileged action giữ actual actor/authority; exact audit representation **TBD**.

## Invariants

Host pre-authorization không biến mất; eligibility tại transaction time; Inventory revalidation ngay trước commitment; Required Payment Condition cần cho normal confirmation; chống conflicting commitments không trao long hold cho Sale; consent explicit/auditable; Booking/Money/Stay sở hữu truth riêng; commerce paths hội tụ Stay; Direct Guest/Sale khác eligibility.

## Open Questions

Technical Instant Book locking: **TBD — future implementation**, không thiết kế. Transaction rules, failure remedy, consent wording và cancellation/refund percentages: **TBD**, legal parts `legal-validation-required`. Nguồn: [ADR-P017–019](../00-start-here/DECISIONS.md#adr-p017), [Domain map](../02-domain/00-domain-map.md), [Workflow questions](08-open-workflow-questions.md).
