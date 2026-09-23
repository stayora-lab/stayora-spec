# STAYORA CHECKPOINT 3 — ACTOR AUTHORITY & CORE WORKFLOWS — REOPENED FOR RECONCILIATION — 2026-09-18

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 0–4, 18–30.

## Mục đích và phạm vi

Tài liệu hóa các workflow cốt lõi dựa trên quyết định đã duyệt. Mô tả authority, domain truth và economics; không phải state machine triển khai.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Nguồn và status

Thứ tự đọc: [Foundation](../00-start-here/README.md) → [Domain](../02-domain/README.md) → [Actor Authority](../03-actor-authority/README.md) → workflows hiện tại → reference tương thích.

**CONFIRMED:** chỉ ghi lại quyết định đã có. Checkpoint baseline đang được reconciliation; artifact status không nâng TBD/WORKING MODEL thành requirement. Các chữ uppercase trong flows là conceptual milestones, không technical enums.

## Đọc tài liệu

1. [Workflow map](00-workflow-map.md).
2. [WF-01 — Sale-assisted Request Booking](01-sale-assisted-request-booking.md).
3. [WF-02 — Instant Book](02-instant-book.md).
4. [WF-03 — External Booking → Stay](03-external-booking-to-stay.md).
5. [WF-04 — Stay Lifecycle](04-stay-lifecycle.md).
6. [WF-05 — Incident → Resolution](05-incident-resolution.md).
7. [WF-06 — Completion → Settlement → Payout](06-completion-settlement-payout.md).
8. [Cross-workflow invariants](07-cross-workflow-invariants.md).
9. [Open Workflow Questions](08-open-workflow-questions.md).
10. [WF-07 — Owner / Host Onboarding](09-owner-onboarding.md).
11. [WF-08 — Property and Bookable Unit Onboarding](10-property-onboarding.md).
12. [WF-09 — Sale Onboarding](11-sale-onboarding.md).
13. [WF-10 — Butler Onboarding](12-butler-onboarding.md).

Đọc cùng [Actor Authority](../03-actor-authority/README.md). Mỗi flow chỉ ra tác nhân và domain sở hữu truth; mũi tên không cấp quyền và không cam kết triển khai đồng bộ.

## Cách đọc workflow

Purpose, Actors, Preconditions, Trigger, Happy Path, Alternative Paths, Failure Paths, Authority, Domain Truth Changes, Money Changes, Notifications, Audit Events và Open Questions tách rõ nội dung đã duyệt với chỗ thiếu.

Notifications chưa có recipient/channel/timing policy đầy đủ trong nguồn; các mục này giữ TBD, chỉ ghi business context cần làm rõ. Audit Events là những mốc business cần trace theo invariants đã duyệt, không event schema/bus.

## Kết quả validation

**Documentation pass đang ở trạng thái REOPENED FOR RECONCILIATION — 2026-09-18.** Bộ này gồm authority và workflow documentation; các TBD/WORKING MODEL vẫn giữ nguyên.

Markdown validation kiểm tra toàn bộ 43 file trong năm vùng tài liệu, cả relative paths và heading/explicit anchors: **PASS**. Không có liên kết nội bộ hỏng. Đã kiểm tra status, purpose/scope, source links và đủ 15 mục nội dung của từng workflow.

**Cross-document consistency: hoàn tất, có các source discrepancies giữ OPEN REVIEW.** Không phát hiện regression mới trong Checkpoint 3 đối với các boundaries dưới đây. Các mục SUPERSEDED và ví dụ bị phủ định trong nguồn không được coi là current requirements.

| Regression được rà soát | Boundary được giữ trong Checkpoint 3 |
|---|---|
| Owner = Primary Host | Hai khái niệm riêng; Primary Host có authority source hợp lệ |
| Role = Permission | Effective Permission cần context hợp lệ |
| Property = Bookable Unit | Property structure khác unit có thể commit |
| Booking = Stay | Commercial truth khác operational truth |
| Request = Inventory Commitment | Request không reserve; authorized acceptance có thể tạo Temporary Inventory Commitment; Payment Session/Attempt tách riêng |
| Whitelist = Instant Book permission | Cần đồng thời eligibility, relationship, Property enabled và transaction rules |
| Whitelist = Record External Commitment authority | Cần explicit capability grant riêng |
| Sale controlling Inventory | Demand/Sale role không cấp quyền block; external commitment capability phải được grant |
| Stayora Staff impersonating Host | Actual actor/acting capacity/authority source được bảo toàn |
| External Stay requiring Stayora Booking | External Commerce → Inventory Truth và/hoặc Stay |
| External Stay generating commission automatically | Representation/completion không tự tạo commission |
| Checkout = Completed | Có completion readiness; exact criteria còn TBD |
| Completed = Settled | Completed là normal eligibility boundary; exception economics vẫn là policy/TBD |
| Settlement = Payout | Phân bổ final positions khác thực thi settled payable |
| Incident = Fault | Evidence/Incident chưa kết luận responsibility |
| Incident directly changing Reputation | Reputation giữ downstream authority riêng |
| Incident directly changing Verification | Signal có thể dẫn tới review, không trực tiếp sửa Verified |
| Identity Verification = Stayora Verified | Identity & Authority khác Verification |
| Guest = Payer = Staying Party | Booking Creator/Payer/Lead Guest/Staying Party riêng |
| Primary Host = Financial Beneficiary | Financial capabilities và entitlement được xét riêng |

### Reconciliation corrections hoàn tất

R-01–R-04 đã được sửa trong current source history ở đúng phạm vi metadata/status/count/progressive-disclosure distinction. Chi tiết resolution và provenance nằm tại [Authority source review](../03-actor-authority/07-open-authority-questions.md). WQ-15 đã được resolve về ownership: [Operational Completion Readiness](04-stay-lifecycle.md) thuộc Stay; [Financial Reconciliation](06-completion-settlement-payout.md) thuộc Money. Normal reconciliation diễn ra sau STAY COMPLETED, còn policy-driven Economic Eligibility có thể mở exception path mà không tạo Completed giả.

**Status audit:** không phát hiện TBD/WORKING MODEL bị vô tình biến thành CONFIRMED trong tài liệu mới. Hold duration, commission base, fees/splits/incentive, refund/deposit mechanics, authority precedence, Lead timings, Affiliate approval và legal/tax tiếp tục có nhãn chưa chốt.

**Nguồn chưa đủ:** Notifications recipient/channel/timing; payment evidence/confirmation actor; completion authority/qualifying blockers; external evidence/conflict handling; Incident severity/resolution authority; detailed delegation và financial/Guest data scope. Các mục này được ghi TBD ngay trong file liên quan, không điền policy thay Founder.

Không đưa DB/ORM/schema, API, UI/navigation, permission middleware/JWT, RBAC/ABAC/ReBAC implementation, event bus/queue, technical locking hoặc infrastructure vào tài liệu. Không tạo ADR freeze, không bắt đầu Checkpoint 4.

**Trạng thái bàn giao: REOPENED — AWAITING FOUNDER/SOL FREEZE REVIEW.**
