# WF-08 — Property and Bookable Unit Onboarding

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW — 2026-09-23**  
> Checkpoint 3 — Onboarding workflow gap · 2026-09-23  
> Nguồn: derived từ [CP8-C1](../10-ux-foundation/c1-onboarding-architecture/README.md), [CP8-C2](../10-ux-foundation/c2-host-owner-property-onboarding/README.md), CP5, CP7 và ADR-P001, ADR-P002, ADR-P003, ADR-P004, ADR-P007. Không tạo quyết định mới.

## Mục đích và phạm vi

Ghi luồng represent Property, gắn Destination và represent Bookable Unit trước hoặc song song với Owner/Host relationship. Đây là hướng resource-first của C2; hướng actor-first nằm ở [WF-07](09-owner-onboarding.md). Luồng dừng ở các readiness outcome độc lập. Nó không tạo Availability, Booking hoặc Stay.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle có trong ADR, CP5 hoặc CP7. Trình tự bước lấy từ baseline CP8-C1/C2 đã được chấp nhận. Mọi điểm mà nguồn chưa quyết định được ghi TBD.

## Purpose

**CONFIRMED:** Property và Bookable Unit là MUST BUILD trong V0 ([CP5 capability matrix](../06-v0-scope/04-capability-matrix.md)). Marketplace mở: Owner Listed supply tham gia khi đáp ứng listing/compliance, và không cần Stayora Verified chỉ để được tham gia ([ADR-P001](../00-start-here/DECISIONS.md#adr-p001)). Marketplace mở không đồng nghĩa miễn listing, identity, right-to-operate hoặc compliance requirements.

## Actors

Actor có Property Authority cho resource scope đó; Owner, Primary Host hoặc Co-host được grant; Stayora Staff function khi Admin-assisted. Property creator có thể khác Owner/Host. Verification là một program riêng, do domain Verification sở hữu.

## Preconditions

**CONFIRMED:** Destination là first-class, là lớp discovery và operational boundary ([ADR-P004](../00-start-here/DECISIONS.md#adr-p004)). Quan hệ khái niệm là `Destination → Property → Bookable Unit`, và Inventory thuộc Unit × Time ([C2 Property/Destination/Unit](../10-ux-foundation/c2-host-owner-property-onboarding/06-property-destination-unit.md)). Actor thực hiện phải có Property Authority cho scope hiện tại; creator chỉ có scope đang được grant.

## Trigger

Property đã được biết đến, vừa được represent, hoặc được tạo với Admin assistance. Hoặc WF-07 cần một Property cho relationship Owner/Host.

## Happy Path — CONFIRMED

```text
Identify or represent Property
→ associate Destination (candidate / accepted)
→ represent Bookable Unit(s)
→ identify / invite / claim Owner   (WF-07)
→ identify / invite / assign Host   (WF-07)
→ evaluate eligibility + explicit authority
→ project independent readiness outcomes
```

1. Xác định hoặc represent Property (C2 R1). Ownership và hosting còn chưa rõ.
2. Gắn Destination (R2). Membership không phải BQL authority hay commercial authority.
3. Represent một hoặc nhiều Bookable Unit (R3). Ví dụ CP7 "một Villa = một Property + một Entire-Villa Unit" chỉ là ví dụ, không phải yêu cầu chung.
4. Owner và Host relationship được thiết lập theo WF-07 (R4–R5). Owner không tự thành Host.
5. Chỉ gắn capability và scope tường minh (R6); không có shortcut qua creator hoặc role.
6. Project từng readiness outcome riêng (R7): Property represented, publication-eligible, Inventory-ready, Booking-ready, Stay-operations-ready ([C2 prerequisites](../10-ux-foundation/c2-host-owner-property-onboarding/09-property-prerequisites.md)). Không có `PROPERTY_ONBOARDING_COMPLETE`.

## Alternative Paths

**CONFIRMED:** Property có thể tồn tại và hữu ích ở dạng private/administrative trước khi Owner/Host truth đầy đủ ([C2 resource-first](../10-ux-foundation/c2-host-owner-property-onboarding/03-resource-first-journey.md)). Property chưa có Host thì vẫn được represent nhưng chưa publish hoặc bị giới hạn theo policy. Verified là program riêng; Stayora Verified assessment là MANUAL-ASSISTED trong V0 (CP5), và onboarding không cấp Verified ([ADR-P002](../00-start-here/DECISIONS.md#adr-p002)). Managed nằm ngoài current core và không bao giờ là đường onboarding mặc định ([ADR-P003](../00-start-here/DECISIONS.md#adr-p003)).

## Failure Paths

**CONFIRMED boundary:** Property bị represent hai lần, hoặc có hai claim trên cùng Property, thì giữ cả hai record kèm provenance, và discovery/publication/Booking/Inventory bị chặn hoặc theo policy cho đến khi truth đủ ([C2 duplicate/conflict](../10-ux-foundation/c2-host-owner-property-onboarding/18-duplicate-claim-conflict.md)). Gắn sai Unit hoặc Destination thì sửa/supersede dưới authority hợp lệ và giữ lịch sử.

**TBD:** matching Property trùng, precedence, và quy trình sửa Destination membership.

## Authority

Dùng [Effective Permission](../03-actor-authority/05-effective-permission.md). Muốn represent/sửa Property và điều khiển publication cần Property Authority cùng các publication conditions. Muốn quản lý Inventory cần Inventory Authority tường minh. Ownership, role Host, Sale eligibility hoặc whitelist đều không đủ ([C2 relationship/authority](../10-ux-foundation/c2-host-owner-property-onboarding/07-relationship-authority.md)). Verified Ownership Relationship là authority basis cho Owner Block có scope, không phải override chung ([FD-13](../11-detailed-interaction/CP8-E-FOUNDER-DECISION-RECONCILIATION.md)). Grantor/scope của Inventory responsibility: **TBD** (C2-TBD-07).

## Domain Truth Changes

| Domain | Truth liên quan — boundary |
|---|---|
| Destination / Property | Property representation, Destination membership, Unit relationship, provenance |
| Identity & Authority | Owner/Host relationship và capability grant (qua WF-07) |
| Inventory | Không có commitment. Chỉ xác định Inventory responsibility; Availability không được tạo bởi onboarding |
| Verification | Không đổi; Verified là program/status riêng |
| Booking / Stay | Không đổi |

## Money Changes

**CONFIRMED:** không có. Represent hoặc publish Property không tạo economics, Settlement hay Payout. Public Price và commercial information thuộc các domain liên quan, không được quyết ở đây.

## Notifications

**TBD — future-policy question:** thông báo về duplicate/claim conflict, publication-eligible và các điều kiện còn thiếu. Nguồn không có recipient/channel/timing policy.

## Audit Events

**CONFIRMED về traceability; đây là mốc business, không phải event schema:** Property represented kèm actor/basis; Destination association; Unit represented/corrected; publication decision kèm authority; Inventory responsibility được xác định; duplicate/conflict được giữ; correction/supersession kèm thời điểm hiệu lực.

## Invariants

`Property exists ≠ published`; `published ≠ Available ≠ Bookable`; `published ≠ Verified`; `Verified ≠ Managed`; `Owner Listed ≠ Verified ≠ Managed`; Property ≠ Bookable Unit; Inventory thuộc Unit × Time; Destination membership ≠ authority; creator ≠ Owner/Host; onboarding không tạo Booking, Stay hoặc Inventory Commitment ([C2 publication/Verification](../10-ux-foundation/c2-host-owner-property-onboarding/11-publication-verification-managed.md), [C1 Property prerequisites](../10-ux-foundation/c1-onboarding-architecture/12-property-prerequisites.md)).

## Open Questions

- Điều kiện publication và moderation (C2-TBD-06, C1-T08).
- Grantor/scope cho Inventory responsibility (C2-TBD-07).
- Matching/precedence khi Property bị represent trùng (C2 DOMAIN GAP; C2-TBD-05).
- Quy trình sửa Destination membership (C2-TBD-10).
- Chi tiết Booking/payment/commercial readiness (C2-TBD-11).
- Cách hiển thị Verification trên Property (C2 POLICY GAP).
- Cấu trúc phân cấp Destination/operational membership (ADR-P004: TBD).
- Checklist listing/compliance/right-to-operate (ADR-P001 boundary; ADR-P007: TBD, legal-validation-required).

Xem [C2 TBD register](../10-ux-foundation/c2-host-owner-property-onboarding/21-tbd-policy-register.md), [C2 gaps](../10-ux-foundation/c2-host-owner-property-onboarding/22-domain-workflow-authority-gaps.md) và [Workflow questions](08-open-workflow-questions.md).
