# WF-04 — Vòng đời kỳ lưu trú (Stay Lifecycle)

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 12–14, 21, 24, 26–27.

## Mục đích và phạm vi

Ghi nhận quá trình vận hành và actual Stay truth từ mọi commerce source. Tách arrival/access/check-in, checkout/completion và eligibility downstream.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Purpose

**CONFIRMED:** Stay là operational lifecycle của kỳ lưu trú dự kiến/thực tế. Stay không phải Booking commerce lifecycle; source không quyết định chất lượng hay quyền vận hành mặc định.

## Actors

Primary Host/operationally authorized Co-host, Butler assigned, recognized Guest/Staying Party, Destination Staff theo function; staff hỗ trợ trong scope. Ai xác nhận Completed và exact exception authority còn **TBD**.

## Preconditions

Stay được tạo/schedule từ confirmed Stayora Booking hoặc external participation có evidence theo điều kiện còn phải đặc tả. Actor vận hành có relationship/capability hợp lệ. Không có Butler không loại bỏ Host responsibility.

## Trigger

Stay tới giai đoạn cần preparation/arrival, và các diễn biến thực tế được ghi nhận xuyên suốt kỳ lưu trú.

## Happy Path — CONFIRMED conceptual flow

```text
SCHEDULED → CHECKED_IN → CHECKED_OUT
→ Operational Completion Readiness → COMPLETED
```

Alternative: `SCHEDULED → DID_NOT_OCCUR` only when the upstream accommodation commitment legitimately ends before Check-in or policy determines the Stay will not occur. PREPARATION/READY are operational readiness milestones, ARRIVAL is an event/observation, and IN_STAY is not required as a separate core lifecycle state. These are conceptual directions, not technical state enums; Incident/service/damage may be events/cases.

1. PREPARATION/READY có thể được ghi như operational milestones; Ready là auditable assertion, không zero-defect guarantee.
2. ARRIVAL, Access và Check-in được phân biệt nơi Destination operations cần; qua cổng không tự chứng minh Check-in/Completed.
3. Actual Staying Party, arrival/departure và events được ghi đúng thực tế. Booking expected truth không overwrite actual Stay truth.
4. Check-out thực tế được ghi; expected checkout time không tự tạo actual Checked-out.
5. Operational Completion Readiness xem actual checkout, operational facts/evidence và qualifying unresolved exceptions; exact criteria còn TBD. Đây không phải Financial Reconciliation.
6. CHECKED_OUT ≠ COMPLETED. Completed Stay là downstream eligibility boundary, không đồng nghĩa reviews/Settlement/Payout đã xong.

## Alternative Paths

**CONFIRMED:** external/direct/Sale commerce paths dùng cùng Stay lifecycle. Late arrival, no arrival yet, lack of Check-in và No-show observation trong lúc valid accommodation right còn hiệu lực là operational observations; không tự cancel Booking, terminate commitment, release Inventory, tạo Payment Default hoặc tạo Stay COMPLETED. Guest có thể đến muộn và Check-in bình thường. Nếu toàn bộ committed period kết thúc không sử dụng, final did-not-stay/no-show disposition có thể được ghi; representation/state vẫn TBD cho State Machine/Data Model sau.

## Failure Paths

Incident/damage đi qua [WF-05](05-incident-resolution.md); evidence chưa là fault hoặc consequence. Chỉ qualifying unresolved exceptions có thể block completion; không giữ mọi Stay vô thời hạn vì mọi complaint. Exact blocker list, authority xử lý, thiếu assignment/data và operational fallback là **TBD**; không invent escalation/SLA.

## Authority

Butler assignment-scoped có thể prepare, assert Ready, coordinate Check-in/out, record events/report damage. Không tự có Booking acceptance, commission visibility hoặc Settlement authority. Destination Staff chỉ scope/function liên quan; QR là credential/evidence, không authority. [Actor matrix](../03-actor-authority/03-actor-resource-matrix.md) giữ các boundaries.

## Domain Truth Changes

Stay sở hữu Staying Party/actual arrival/departure/operations/completion. Destination Operations dùng Stay truth cho QR/gate/cart/security/coordination. Booking giữ commercial history; Incident ghi case/evidence trong Stay/Operations. Reputation/Verification nhận qualifying signals nhưng không tự rewrite từ thao tác Stay.

## Money Changes

**CONFIRMED:** Ready/Check-in/Checkout không tự tạo Earned/Settled/Paid. Operational Completion Readiness thuộc Stay và dẫn tới STAY COMPLETED khi đủ điều kiện; Financial Reconciliation thuộc Money và xảy ra sau Completed theo [WF-06](06-completion-settlement-payout.md). Physical absence ≠ Inventory Release. Damage record chưa là financial adjustment. External completion không automatic settlement.

## Notifications

**TBD:** preparation/Ready/arrival/change/checkout/completion communications, recipient/channel/timing. Data disclosure theo operational need và relationship; không gửi economics cho Butler/BQL chỉ vì họ vận hành Stay.

## Audit Events

Các mốc business cần trace: assignment/capacity khi hành động, Ready assertion, actual arrival/access/check-in/out, Staying Party deviations, operational events/evidence, completion readiness và authorized completion khi policy được xác định. Không invent người có quyền completion; audit model chi tiết **TBD**.

## Invariants

Source-independent lifecycle; actual Stay truth không bị Booking expected truth overwrite; Host responsibility còn khi thiếu Butler; Ready không zero-defect guarantee; Arrival/Access/Check-in khác nhau theo nhu cầu; evidence không fault/consequence; expected checkout không actual checkout; Check-out ≠ Completed; physical absence ≠ Inventory Release; Payment Default ≠ No-show; Completed không downstream completion; deviations không rewrite Booking history.

## Open Questions

Completion authority, exact blocker exceptions, no-show/early-departure handling, evidence và notifications: **TBD**. Nguồn: [Foundation Actors](../01-product-foundation/06-ecosystem-and-actors.md), [Destination Model](../01-product-foundation/07-destination-model.md), [Domain Ownership](../02-domain/02-domain-ownership.md), [Workflow questions](08-open-workflow-questions.md).
