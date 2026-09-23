# WF-07 — Owner / Host Onboarding

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW — 2026-09-23**  
> Checkpoint 3 — Onboarding workflow gap · 2026-09-23  
> Nguồn: derived từ [CP8-C1](../10-ux-foundation/c1-onboarding-architecture/README.md), [CP8-C2](../10-ux-foundation/c2-host-owner-property-onboarding/README.md), CP3 và ADR-P001, ADR-P006, ADR-P007, ADR-P009, ADR-P010. Không tạo quyết định mới.

## Mục đích và phạm vi

Ghi luồng một Identity trở thành Owner và/hoặc Host trong quan hệ với Property. Đây là hướng actor-first của C2; hướng resource-first nằm ở [WF-08](10-property-onboarding.md). Hai hướng hội tụ về cùng một canonical truth. Luồng không cấp publication, Verified, Booking Authority, Inventory Authority hoặc quyền tài chính.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle có trong ADR hoặc CP3. Trình tự bước lấy từ baseline CP8-C1/C2 đã được chấp nhận. Mọi điểm mà nguồn chưa quyết định được ghi TBD; workflow này không giải chúng.

## Purpose

**CONFIRMED:** Host được self-onboard, nhưng Host tự đăng ký không đồng nghĩa villa tự động publish ([ADR-P007](../00-start-here/DECISIONS.md#adr-p007)). Ownership và hosting authority là hai relationship riêng: Primary Host không nhất thiết là legal owner ([ADR-P009](../00-start-here/DECISIONS.md#adr-p009)).

## Actors

Identity có ý định làm Owner/Host; Owner; Primary Host; Co-host (được delegate sau); Stayora Staff function khi hỗ trợ (Admin-assisted). Property creator có thể là người khác Owner/Host ([C2 Identity, Party, Owner và Host](../10-ux-foundation/c2-host-owner-property-onboarding/05-identity-party-owner-host.md)). Financial Beneficiary là relationship riêng, không suy ra từ Owner hoặc Host.

## Preconditions

**CONFIRMED:** một Identity có thể giữ nhiều role ([ADR-P006](../00-start-here/DECISIONS.md#adr-p006)); không tạo account mới chỉ để đơn giản hóa onboarding. Identity đã tồn tại thì được resolve tới Identity đó ([C1 alternative/failure](../10-ux-foundation/c1-onboarding-architecture/20-alternative-failure-boundaries.md)). Không cần Property đã tồn tại. Nếu Property chưa có, nó được represent theo WF-08.

## Trigger

Identity nêu intent hoặc claim Owner/Host; được invite bởi actor có authority; hoặc Stayora Staff thiết lập với audit. Các entry mode theo [C1 Entry Modes](../10-ux-foundation/c1-onboarding-architecture/06-entry-modes.md). Không có entry mode hay trình tự onboarding bắt buộc chung.

## Happy Path — CONFIRMED

```text
Resolve Identity + Party / capacity
→ Owner / Host intent or claim
→ identify or represent Property (WF-08)
→ relationship basis: invitation / existing association / evidence / Admin-assisted
→ relationship established if authorized (Owner, Primary Host)
→ evaluate eligibility + explicit capability grants
→ bounded Host / Owner Working Context
```

1. Resolve Identity và Party/capacity (C2 A1). Tạo account không phải là Owner/Host truth.
2. Ghi intent hoặc claim thành input của relationship đề xuất (A2). Claim ≠ Evidence ≠ Relationship ≠ Authority ([C1 claim/evidence](../10-ux-foundation/c1-onboarding-architecture/08-claim-evidence-boundary.md)).
3. Xác định hoặc represent Property (A3; xem WF-08). Người tạo Property không vì thế mà thành Owner hoặc Host.
4. Thu relationship basis (A4): invitation, association hiện có, evidence hoặc Admin-assisted. Không tự đặt threshold và không kết luận pháp lý.
5. Nếu được phép, thiết lập Owner và/hoặc Primary Host relationship có scope và hiệu lực (A5). Một Identity có thể vừa là Owner vừa là Primary Host, nhưng hai relationship vẫn tách riêng.
6. Đánh giá eligibility và các capability grant tường minh (A6). Role hoặc Working Context không cấp permission.
7. Project một Working Context có giới hạn (A7). Publication, Inventory readiness, Booking readiness và Stay readiness được xét riêng ([C2 actor-first](../10-ux-foundation/c2-host-owner-property-onboarding/02-actor-first-journey.md)).

## Alternative Paths

**CONFIRMED:** Owner khác Host, nên cả hai relationship được giữ và Owner không tự override Host ([C1 Host/Owner](../10-ux-foundation/c1-onboarding-architecture/13-host-owner-architecture.md)). Host có thể vận hành unit không sở hữu. Relationship được ghi nhận nhưng không tự mở rộng authority. Primary Host có thể delegate Co-host cho capability/resource/lifecycle được đặt tên; Co-host được cấp quyền có thể accept/reject, và mỗi lần phải ghi actor, authority và thời điểm ([ADR-P010](../00-start-here/DECISIONS.md#adr-p010)).

Kết quả pending là hợp lệ: Property đã represent nhưng Owner chưa rõ; Owner đã có nhưng chưa có Host; Host đã có nhưng Property chưa publish. Owner/Host cũng có thể đăng ký Sale theo [WF-09](11-sale-onboarding.md) như một capacity độc lập.

## Failure Paths

**CONFIRMED boundary:** claim bị tranh chấp hoặc ownership chưa rõ thì giữ pending, không suy ra Host hoặc quyền tài chính. Owner không có Booking Authority thì không được accept Request. Invitation bị từ chối hoặc thu hồi thì không có relationship/authority. Hai người claim cùng một Property thì giữ cả hai claim cùng provenance, không chọn winner ([C2 duplicate/conflict](../10-ux-foundation/c2-host-owner-property-onboarding/18-duplicate-claim-conflict.md)).

**TBD:** evidence threshold, người quyết claim tranh chấp, precedence khi nhiều Owner, chuyển nhượng và cách xử lý wrong recipient/expiry.

## Authority

Dùng [Effective Permission](../03-actor-authority/05-effective-permission.md). Relationship và authority được thiết lập ở hai bước riêng ([C2 relationship/authority](../10-ux-foundation/c2-host-owner-property-onboarding/07-relationship-authority.md)). Property Authority, Booking Authority, Inventory Authority, Operations Authority, Delegation Authority và financial capability đều phải được grant tường minh. Stayora Staff hỗ trợ bằng actual identity; không silent impersonation. Grantor và điều kiện chấp nhận relationship Owner/Host: **AUTHORITY GAP / TBD**.

## Domain Truth Changes

| Domain | Truth liên quan — boundary |
|---|---|
| Identity & Authority | Identity, Party/capacity, Owner/Host relationship, basis/evidence, capability grants, scope và hiệu lực |
| Property | Chỉ qua WF-08; WF-07 không tạo publication, Verified hoặc Managed |
| Inventory | Không đổi; Owner/Host role không tạo Inventory Authority |
| Booking / Stay | Không đổi; onboarding không tạo Booking hay Stay |

## Money Changes

**CONFIRMED:** không có. Owner hoặc Host không tự là Financial Beneficiary. Financial relationship/capability là việc riêng, không nằm trong onboarding. Payout không được mở bởi workflow này.

## Notifications

**TBD — future-policy question:** kênh, người nhận và thời điểm cho invitation, kết quả claim và relationship established. C1 không chọn email, OTP, magic link hoặc token ([C1 invitation](../10-ux-foundation/c1-onboarding-architecture/07-invitation-boundary.md)).

## Audit Events

**CONFIRMED về traceability; đây là mốc business, không phải event schema:** claim/intent kèm provenance; invitation và chấp nhận; relationship established/pending/disputed kèm basis và evidence; capability grant kèm grantor, scope, thời điểm; hành động của Staff kèm lý do; correction/revocation giữ lịch sử ([C1 correction/history](../10-ux-foundation/c1-onboarding-architecture/19-correction-revocation-history.md)).

## Invariants

Identity ≠ Role ≠ Party; capacity được grant, không tự gán; Claim ≠ Evidence ≠ Relationship ≠ Authority; Owner ≠ Primary Host ≠ Financial Beneficiary; Property creator ≠ Owner/Host; Host self-onboard ≠ publish; relationship không tự mở rộng authority; không có trạng thái ONBOARDED chung; correction giữ lịch sử.

## Open Questions

- Evidence threshold và legal validation cho ownership (C2-TBD-02, C1-T05).
- Precedence khi nhiều Owner, transfer và dispute (C2-TBD-03, C2-TBD-05, C1-T09).
- Grantor và điều kiện chấp nhận relationship Owner/Host (C2 AUTHORITY GAP).
- Invitation acceptance, expiry và wrong recipient (C2-TBD-04, C1-T04).
- Identity matching/merge (C2-TBD-01, C1-T01).
- Privacy projection giữa Owner và Host (C2-TBD-08).
- Hiệu lực và lan truyền khi revoke (C2-TBD-09).
- Checklist identity/right-to-operate/compliance cho Host self-onboarding (ADR-P007: TBD, legal-validation-required).
- Quy trình V0 cho việc xem xét evidence thủ công: CP5 không liệt kê bước này trong MANUAL-ASSISTED (C2 V0-SCOPE GAP).

Xem [C2 TBD register](../10-ux-foundation/c2-host-owner-property-onboarding/21-tbd-policy-register.md) và [Workflow questions](08-open-workflow-questions.md).
