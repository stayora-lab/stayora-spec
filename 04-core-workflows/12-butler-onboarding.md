# WF-10 — Butler Onboarding

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW — 2026-09-23**  
> Checkpoint 3 — Onboarding workflow gap · 2026-09-23  
> Nguồn: derived từ [CP8-C1](../10-ux-foundation/c1-onboarding-architecture/README.md), [CP8-C4](../10-ux-foundation/c4-butler-onboarding/README.md), CP4 và ADR-P005, ADR-P006, ADR-P008. Không tạo quyết định mới.

## Mục đích và phạm vi

Ghi luồng một Identity trở thành Butler: capacity → operational eligibility → Butler Assignment có scope → Butler Working Context. Luồng không thiết kế workforce management, HR, scheduling hay certification. Nó cũng không cấp authority về commercial, Inventory hoặc Money.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle có trong ADR, CP3 hoặc CP4. Trình tự bước lấy từ baseline CP8-C1/C4 đã được chấp nhận. Mọi điểm mà nguồn chưa quyết định được ghi TBD.

## Purpose

**CONFIRMED:** Butler đăng ký vai trò và phải được Stayora duyệt. Butler đã được duyệt còn cần quan hệ assignment với villa. Approval không tự biến Butler thành nhân viên Stayora ([ADR-P008](../00-start-here/DECISIONS.md#adr-p008)).

## Actors

Identity có ý định làm Butler; assigning actor hợp lệ: Host/Primary Host hoặc delegated operational authority, Stayora Admin function, hoặc Destination/BQL function khi authority tường minh; Stayora Staff cho eligibility review.

## Preconditions

**CONFIRMED:** một Identity có thể giữ nhiều role ([ADR-P006](../00-start-here/DECISIONS.md#adr-p006)). Không hard-code QR, xe điện hay "tối đa hai Butler" cho mọi nơi; những điểm đó là destination policy ([ADR-P005](../00-start-here/DECISIONS.md#adr-p005)). Để có Assignment, phải có Property/Stay/Destination-function scope được hỗ trợ.

## Trigger

Identity nộp Butler application; được invite; được Host assign; được Stayora Admin hoặc Destination hỗ trợ; hoặc thiết lập thủ công V0 có provenance ([C4 entry modes](../10-ux-foundation/c4-butler-onboarding/03-entry-modes.md)).

## Happy Path — CONFIRMED

```text
Resolve Identity + Butler-intending capacity
→ Application: SUBMITTED → UNDER_REVIEW → APPROVED
→ operational Platform Eligibility: ELIGIBLE
→ Butler Assignment proposed / established by valid assigner
   (Property / Stay / Destination-function scope + validity)
→ Butler Working Context (assigned operational projection)
→ bounded responsibility; separate action authority where required
```

1. Resolve Identity và Butler-intending capacity (C4 BTL1). Tự mô tả không tạo Butler capacity được công nhận.
2. Thiết lập operational eligibility (BTL2) theo `SUBMITTED → UNDER_REVIEW → APPROVED` và `ELIGIBLE ↔ SUSPENDED → REVOKED` ([CP4 eligibility](../05-state-machines-policies/09-role-application-and-eligibility.md)). Butler Approval Policy tách riêng khỏi Sale Approval Policy.
3. Assigner hợp lệ đề xuất hoặc thiết lập Assignment kèm scope, hiệu lực và provenance (BTL3) ([C4 assignment](../10-ux-foundation/c4-butler-onboarding/05-assignment-architecture.md)).
4. Kích hoạt Butler Working Context với thông tin vận hành được assign (BTL4). Visibility không phải permission.
5. Thực hiện trách nhiệm có giới hạn (BTL5): chuẩn bị, điều phối, quan sát, ghi evidence trong scope. Check-in, Checkout và access có thể cần authority riêng.
6. Handoff truth vận hành tới authority chịu trách nhiệm (BTL6). Report không tự tạo Block, Finding hay Completion ([C4 journey](../10-ux-foundation/c4-butler-onboarding/02-butler-onboarding-journey.md)).

## Alternative Paths

**CONFIRMED:** Butler có thể được assign cho Property, Stay hoặc Destination function trong phạm vi architecture hỗ trợ; không có hierarchy chung. Identity đã tồn tại có thể nhận thêm Butler capacity mà các capacity khác không đổi. Owner không được assign chỉ vì là Owner; BQL không được assign chỉ vì có destination visibility; không ai delegate capability mà mình không giữ ([C4 assignment authority](../10-ux-foundation/c4-butler-onboarding/06-assignment-authority.md)).

**V0:** C4 ghi rằng manual-assisted V0 evaluation và manual V0 setup chấp nhận được nếu actor, basis, quyết định, scope, hiệu lực và audit rõ ràng ([C4 capacity/eligibility](../10-ux-foundation/c4-butler-onboarding/04-capacity-eligibility.md)). CP5 không liệt kê Butler approval/assignment trong MANUAL-ASSISTED một cách tường minh; xem Open Questions.

## Failure Paths

**CONFIRMED boundary:** eligibility pending/rejected/suspended/revoked thì không có Assignment đang hoạt động. Invitation bị từ chối thì không có Assignment/authority. Assignment thiếu, ngoài scope, hết hạn hoặc bị revoke thì không có context/hành động về sau; lịch sử được giữ. Sai Property/Stay thì sửa/supersede. Butler thử hành động Booking, Inventory/Maintenance Block hoặc tài chính thì bị từ chối nếu không có authority riêng. Report được giữ và route tới evaluator có authority ([C4 failure](../10-ux-foundation/c4-butler-onboarding/25-failure-alternatives.md)).

**TBD:** thay Butler trong lúc Stay đang diễn ra, nhiều Butler xung đột, Host không liên lạc được, BQL escalation.

## Authority

Dùng [Effective Permission](../03-actor-authority/05-effective-permission.md). Butler Eligibility ≠ Butler Assignment ≠ Authority. Assignment có thể cho phép chuẩn bị, điều phối arrival/Check-in/Checkout, Guest support, readiness/evidence và báo Incident. Nó không cấp Booking acceptance, pricing, Inventory, payment/refund, Settlement/Payout, Owner authority hay consequence authority ([C1 Butler architecture](../10-ux-foundation/c1-onboarding-architecture/15-butler-architecture.md)). Grantor, acceptance và propagation khi nguồn im lặng: **AUTHORITY GAP / TBD**.

## Domain Truth Changes

| Domain | Truth liên quan — boundary |
|---|---|
| Identity & Authority | Butler capacity, application outcome, Platform Eligibility, Assignment (assigner, scope, validity) |
| Destination Operations | Context vận hành được assign; không có workforce/HR concept |
| Booking / Inventory / Money | Không đổi |
| Stay | Không đổi khi onboarding; hành động vận hành sau đó theo [WF-04](04-stay-lifecycle.md) |

## Money Changes

**CONFIRMED:** không có. Approval không tạo quan hệ lao động với Stayora (ADR-P008). Butler không phải người thu nợ chính trong Oceanami Pilot ([ADR-P061](../00-start-here/DECISIONS.md#adr-p061)).

## Notifications

**TBD — future-policy question:** kết quả application, Assignment được đề xuất/có hiệu lực/kết thúc, và handoff khi đổi Butler. Nguồn không có recipient/channel/timing policy.

## Audit Events

**CONFIRMED về traceability; đây là mốc business, không phải event schema:** application kèm provenance; reviewer, basis và quyết định; các thay đổi eligibility; Assignment kèm assigner, capacity, authority source, resource, function, hiệu lực và lý do; action grant riêng; correction/reassignment giữ lịch sử assignment cũ và mới.

## Invariants

Butler capacity ≠ eligibility ≠ Assignment ≠ Authority; approval ≠ nhân viên Stayora; Assignment ≠ commercial/Booking/Inventory/financial authority; visibility ≠ permission; report ≠ Block/Finding/Completion; Owner status hoặc BQL visibility không đủ để assign; không có `BUTLER_ONBOARDED`/`BUTLER_ACTIVE`; destination policy không bị hard-code vào core.

## Open Questions

- Tiêu chí eligibility, evidence và người review Butler (C4-TBD-01, C1-T07).
- Grantor và acceptance của Assignment; vai trò của Host/delegated/Admin/BQL (C4-TBD-02, C4-TBD-11).
- Phân cấp scope: Property vs Stay vs Destination/Function (C4-TBD-03).
- Hiệu lực, expiry, revocation và handoff khi Stay đang diễn ra (C4-TBD-04, C1-T11).
- Grant cho Check-in/Checkout (C4-TBD-05).
- Trách nhiệm khi có nhiều Butler (C4-TBD-09).
- Scope trường dữ liệu Guest/privacy (C4-TBD-10).

Xem [C4 TBD register](../10-ux-foundation/c4-butler-onboarding/28-tbd-policy-register.md), [C4 gaps](../10-ux-foundation/c4-butler-onboarding/29-domain-workflow-authority-gaps.md) và [Workflow questions](08-open-workflow-questions.md).
