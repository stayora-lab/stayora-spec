# WF-09 — Sale Onboarding

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW — 2026-09-23**  
> Checkpoint 3 — Onboarding workflow gap · 2026-09-23  
> Nguồn: derived từ [CP8-C1](../10-ux-foundation/c1-onboarding-architecture/README.md), [CP8-C3](../10-ux-foundation/c3-sale-onboarding/README.md), CP4 và ADR-P006, ADR-P008, ADR-P011, ADR-P012. Không tạo quyết định mới.

## Mục đích và phạm vi

Ghi luồng một Identity trở thành Sale: capacity → platform eligibility → Distribution Relationship → Sale Working Context có giới hạn. Luồng không tạo Request, Booking, Inventory Commitment, Stay hay economics.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle có trong ADR, CP3 hoặc CP4. Trình tự bước lấy từ baseline CP8-C1/C3 đã được chấp nhận. Mọi điểm mà nguồn chưa quyết định được ghi TBD.

## Purpose

**CONFIRMED:** Sale đăng ký vai trò và phải được Stayora duyệt ([ADR-P008](../00-start-here/DECISIONS.md#adr-p008)). Sale là actor phân phối trọng tâm, không mặc định là Co-host và không bị loại khỏi marketplace ([ADR-P011](../00-start-here/DECISIONS.md#adr-p011)).

## Actors

Identity có ý định làm Sale; Commercial Authority holder (Owner/Authorized Host); Stayora Staff function cho review và Admin-assisted setup. Affiliate là actor khác Sale.

## Preconditions

**CONFIRMED:** một Identity có thể giữ nhiều role ([ADR-P006](../00-start-here/DECISIONS.md#adr-p006)). Owner/Host đăng ký Sale thì Sale là một capacity độc lập; ownership/hosting không kéo theo Sale eligibility ([C3 entry modes](../10-ux-foundation/c3-sale-onboarding/03-entry-modes.md)). Không cần Request hay Booking nào tồn tại trước.

## Trigger

Identity nộp Sale application; được invite; được Stayora Staff thiết lập với audit; hoặc một Sale đã eligible cần thêm Distribution Relationship/scope mới.

## Happy Path — CONFIRMED

```text
Resolve Identity + Party / Sale capacity
→ Sale application / invitation / Admin-assisted (provenance)
→ Application: SUBMITTED → UNDER_REVIEW → APPROVED
→ Platform Eligibility: ELIGIBLE
→ Distribution Relationship with Commercial Authority holder / scope
→ resolve supply / market scope
→ Sale Working Context: discovery, Offer preparation, Request creation
```

1. Resolve Identity và Sale-intending capacity (C3 S1). Đăng ký không phải là được phép bán.
2. Giữ application/invitation kèm provenance (S2). Tự mô tả không tạo Sale capacity được công nhận.
3. Review application theo `SUBMITTED → UNDER_REVIEW → APPROVED / REJECTED / WITHDRAWN`; eligibility hiệu lực là `ELIGIBLE ↔ SUSPENDED → REVOKED` ([CP4 eligibility](../05-state-machines-policies/09-role-application-and-eligibility.md)). APPROVED là kết quả lịch sử; ELIGIBLE là status hiệu lực (S3).
4. Thiết lập Distribution Relationship giữa Sale ↔ Commercial Authority holder ↔ Authority Scope (S4) ([C3 Distribution Relationship](../10-ux-foundation/c3-sale-onboarding/06-distribution-relationship.md)). Relationship ≠ Booking/Inventory Authority.
5. Resolve supply/market scope (S5). Không phải mọi supply đều tự động visible hoặc bookable.
6. Kích hoạt Sale Working Context (S6): discovery, Offer preparation, tạo Booking Request. Context không cấp permission.
7. Attribution chỉ được ghi khi thật sự attributable (S7) ([C3 journey](../10-ux-foundation/c3-sale-onboarding/02-sale-onboarding-journey.md)).

## Alternative Paths

**CONFIRMED:** Whitelist/Blacklist là trust relationship Sale ↔ Owner/Authorized Host trong scope commercial authority. Normallist là mặc định; Whitelist không tự cấp mọi capability; Blacklist có scope theo relationship ([ADR-P012](../00-start-here/DECISIONS.md#adr-p012)). Identity vừa là Sale vừa là Co-host chỉ accept trong capacity Co-host và scope của nó, với acting capacity được audit ([C1 Sale architecture](../10-ux-foundation/c1-onboarding-architecture/14-sale-architecture.md)).

**V0:** C3 ghi rằng việc đánh giá Sale theo kiểu manual-assisted phù hợp với CP5 nếu actor, basis, quyết định, scope và lịch sử được audit ([C3 eligibility](../10-ux-foundation/c3-sale-onboarding/05-sale-eligibility.md)). CP5 không liệt kê Sale approval trong MANUAL-ASSISTED một cách tường minh; xem Open Questions.

## Failure Paths

**CONFIRMED boundary:** application REJECTED/WITHDRAWN hoặc eligibility pending/SUSPENDED/REVOKED thì không có Sale Context và không có hành động phân phối về sau; lịch sử được giữ. Thiếu Distribution Relationship hoặc relationship đã kết thúc thì không có hành động trong scope đó. Sale thử accept Request, thay đổi Inventory hoặc ghi authoritative External Accommodation thì bị từ chối nếu không có authority riêng ([C3 failure](../10-ux-foundation/c3-sale-onboarding/21-failure-alternatives.md)). Sau khi revoke, muốn reinstatement phải có quy trình auditable hoặc application mới.

**TBD:** tiêu chí approval, người lập Distribution Relationship, xung đột attribution.

## Authority

Dùng [Effective Permission](../03-actor-authority/05-effective-permission.md): `Sale Platform Eligibility + Sale↔Commercial Authority Relationship + Property Distribution Policy + Transaction Context + Lead/Attribution Context`. Sale capacity không cấp Booking Authority, Host Authority, Inventory Authority, quyền sở hữu giá, payment/refund, settlement/payout hay authority vận hành Stay. Stayora Staff review bằng actual identity; không impersonate Sale hay Commercial Authority holder.

## Domain Truth Changes

| Domain | Truth liên quan — boundary |
|---|---|
| Identity & Authority | Sale capacity, application outcome, Platform Eligibility status |
| Distribution | Distribution Relationship (NORMAL / WHITELIST / BLACKLIST), scope, provenance |
| Booking / Inventory / Stay | Không đổi; onboarding không tạo Request, commitment hoặc Stay |

## Money Changes

**CONFIRMED:** không có. Attribution không phải commission, settlement hay payout. Sale economics chỉ phát sinh qua [WF-01](01-sale-assisted-request-booking.md)/[WF-06](06-completion-settlement-payout.md) theo policy. Commercial terms của relationship: **TBD** (C3-TBD-03, C3-TBD-08).

## Notifications

**TBD — future-policy question:** kết quả application, eligibility bị suspend/revoke, lời mời vào relationship và thay đổi relationship. Nguồn không có recipient/channel/timing policy.

## Audit Events

**CONFIRMED về traceability; đây là mốc business, không phải event schema:** application kèm provenance; reviewer, basis và quyết định; các thay đổi eligibility kèm thời điểm hiệu lực; Distribution Relationship được thiết lập/đổi trạng thái/kết thúc kèm grantor và scope; hành động của Staff kèm lý do; attribution kèm source ([C1 correction/history](../10-ux-foundation/c1-onboarding-architecture/19-correction-revocation-history.md)).

## Invariants

Identity ≠ Sale capacity ≠ Application ≠ Platform Eligibility ≠ Distribution Relationship ≠ Authority; APPROVED ≠ ELIGIBLE; Whitelist ≠ permission bundle; Sale ≠ Co-host; Affiliate ≠ Sale; suspension của một capability không tự suspend role khác; không có `SALE_ONBOARDED`; attribution ≠ earnings ([C3 outcomes](../10-ux-foundation/c3-sale-onboarding/17-completion-outcomes.md)).

## Open Questions

- Tiêu chí approval và evidence cho Sale (C3-TBD-01, C1-T07).
- Eligibility scope và quy trình V0 manual-assisted (C3-TBD-02).
- Grantor, scope và contracting của Distribution Relationship; chuyển trạng thái NORMAL/WHITELIST/BLACKLIST (C3-TBD-03, C1-T10).
- Invitation consent, expiry và cơ chế (C3-TBD-04).
- Visibility của Sale và thông tin riêng tư (C3-TBD-05).
- Qualification attribution và xung đột nhiều Sale (C3-TBD-07).
- Thời điểm hiệu lực, notice và appeal khi revoke; xử lý Request đang dở (C3-TBD-10).

Xem [C3 TBD register](../10-ux-foundation/c3-sale-onboarding/24-tbd-policy-register.md), [C3 gaps](../10-ux-foundation/c3-sale-onboarding/25-domain-workflow-authority-gaps.md) và [Workflow questions](08-open-workflow-questions.md).
