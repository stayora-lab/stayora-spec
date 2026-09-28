# WF-07 — Owner / Host Onboarding

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW — 2026-09-23**  
> Checkpoint 3 — Onboarding workflow gap · 2026-09-23  
> Nguồn: derived từ [CP8-C1](../10-ux-foundation/c1-onboarding-architecture/README.md), [CP8-C2](../10-ux-foundation/c2-host-owner-property-onboarding/README.md), CP3 và ADR-P001, ADR-P006, ADR-P007, ADR-P009, ADR-P010. Không tạo quyết định mới.

## Mục đích và phạm vi

Ghi luồng một Identity trở thành Owner và/hoặc Host trong quan hệ với Property. Đây là hướng actor-first của C2; hướng resource-first nằm ở [WF-08](10-property-onboarding.md). Hai hướng hội tụ về cùng một canonical truth. Luồng không tự cấp publication, Verified hoặc authority từ relationship. V0 approved onboarding establishing a Primary explicitly establishes the standard unit-scoped capability set in the same audited action, identical to accepted normal transfer under [ADR-P075](../00-start-here/DECISIONS.md#adr-p075); financial execution remains separate.

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

**CONFIRMED boundary:** disputed legal-ownership claims remain pending and grant no inferred financial authority. Unresolved legal ownership does not prevent an independently Admin-approved operational hosting relationship under ADR-P075; it is not an ownership determination. Owner không có Booking Authority thì không được accept Request. Invitation bị từ chối hoặc thu hồi thì không có relationship/authority. Hai người claim cùng một Property thì giữ cả hai claim cùng provenance, không chọn winner ([C2 duplicate/conflict](../10-ux-foundation/c2-host-owner-property-onboarding/18-duplicate-claim-conflict.md)).

**TBD:** legal ownership evidence thresholds, disputed-claim disposition, multiple Owner precedence/legal transfer and wrong recipient/expiry. V0 operational hosting approval and Primary transfer are resolved only in the ADR-P075 section below.

## Authority

Dùng [Effective Permission](../03-actor-authority/05-effective-permission.md). Relationship và authority là hai quyết định riêng; V0 có thể ghi cả relationship approval và explicit grant trong cùng audited action ([C2 relationship/authority](../10-ux-foundation/c2-host-owner-property-onboarding/07-relationship-authority.md)). Property Authority, Booking Authority, Inventory Authority, Operations Authority, Delegation Authority và financial capability đều phải được grant tường minh. Stayora Staff hỗ trợ bằng actual identity; không silent impersonation. For V0 Admin-assisted onboarding approval, the grantor/approver is a real Stayora Admin acting within appropriate Destination authority under ADR-P075. Legal Owner relationship requirements and grantor rules for other flows remain **TBD**.

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
- Legal Owner/co-owner precedence and disputes remain open (C2-TBD-03, C2-TBD-05, C1-T09); normal V0 Primary transfer and the Admin exception are resolved only as below.
- Owner relationship requirements and grantor conditions beyond the V0 unit-hosting flow remain open (C2 AUTHORITY GAP).
- Invitation expiry, wrong recipient and other invitation policies remain open (C2-TBD-04, C1-T04); normal Primary transfer requires one recipient acceptance, not a second approval.
- Identity matching/merge (C2-TBD-01, C1-T01).
- Privacy projection giữa Owner và Host (C2-TBD-08).
- Hiệu lực và lan truyền khi revoke (C2-TBD-09).
- Legal identity/right-to-operate/compliance checklist remains open (ADR-P007: TBD, legal-validation-required); V0 operational relationship verification does not adjudicate ownership.
- Future-Destination evidence requirements remain open; V0 Admin-assisted hosting verification and exception handling are now listed in CP5 MANUAL-ASSISTED.

Xem [C2 TBD register](../10-ux-foundation/c2-host-owner-property-onboarding/21-tbd-policy-register.md) và [Workflow questions](08-open-workflow-questions.md).

## V0 hosting relationship and Primary lifecycle

**Status: CONFIRMED per [ADR-P075](../00-start-here/DECISIONS.md#adr-p075)** — this section narrows the general workflow; unrelated questions above remain open.

Host capacity is self-service. V0 hosting relationship establishment has three paths: Admin-assisted onboarding via an approved hosting relationship request on the unit (not a Host access request); normal Primary transfer by designation and recipient acceptance; audited Admin manual replacement when normal transfer cannot reasonably occur. Only onboarding requires the request. The other two paths establish/replace the relationship directly without adjudicating ownership. V0 supports in-Destination catalogue units only. Record applicant identity, destinationId, selected unit(s), contact name, email and phone as lightweight operational request information, not an implementation schema. PENDING / APPROVED / REJECTED applies per unit; partial approval is allowed.

For Admin-assisted onboarding only, a real, appropriately Destination-scoped Stayora Admin verifies the operational relationship outside Stayora; retain the actual approving/rejecting identity, timestamp, Admin-assisted verification basis/type, short reason and per-unit outcome. No ownership/identity document, chat transcript or sensitive evidence upload is required merely to establish this V0 relationship. Approval is not legal ownership adjudication. For approval establishing a Primary, the same audited action establishes the [standard V0 Primary Host capability set](../03-actor-authority/02-authority-capabilities.md#standard-v0-primary-host-capability-set), identical to that established on accepted normal transfer; authority does not depend on the valid establishment path. Other capabilities require separate explicit grants: Request ≠ Evidence ≠ Relationship ≠ Authority. Publication remains separate; HOST_DAMAGE is not a generic/default Host grant. See [capability boundaries](../03-actor-authority/02-authority-capabilities.md#v0-hosting-relationship-grants).

The first APPROVED relationship becomes initial Primary for the unit; first SUBMITTED is not precedence. Multiple requests retain their provenance until an authorized manual disposition; later participants are not automatically Primary. Legal-owner/co-owner precedence remains undecided.

The current Primary designates a specific proposed successor. The recipient ACCEPTS once; designation alone leaves transfer pending and the existing Primary/authority in place. Acceptance is not a second Stayora approval, and Stayora does not decide whether the recipient is a legally valid owner. Valid acceptance atomically ends outgoing Primary status, makes the incoming hosting relationship effective, establishes the recipient as Primary with the applicable standard V0 Primary Host capability set for the unit, and records required provenance/audit. No transfer-effective/standard-authority gap or later Admin grant step is allowed; Stayora does not assess the recipient or approve normal transfer. Authority source is the new Primary relationship plus canonical platform policy, not the old Primary's grants. Personal, exceptional and actor-specific one-off/scoped grants do not transfer mechanically; HOST_DAMAGE remains separately granted under ADR-P073. The defined standard set contains only existing canonical Booking, Inventory, Primary-only Delegation and Villa Readiness Host-support authority; excluded grants and unrelated granularity/TBDs remain separate/open. Revocation effective-time and propagation remain C2-TBD-09.

Existing Co-hosts are shown to the incoming Primary and retained by default unless removed during confirmation. Retained delegations must have the incoming Primary as valid source; they cannot continue solely under outgoing-Primary provenance. Primary can invite/remove Co-hosts within delegation scope. A removal warning may show accepted requests, upcoming stays, unsettled matters or Butler assignments but cannot block removal, create a lifecycle/Completion blocker or automatically transfer responsibility.

Admin/operations replacement is a manual exception when normal transfer cannot reasonably occur, requiring real Admin identity, appropriate Destination authority, reason, external operational verification and audit. It is neither arbitrary reassignment nor impersonation nor ownership proof. Confirmed bookings/upcoming stays remain attached to the unit without cancellation, recreation or rewriting historical truth; incoming Primary operates applicable future stays only under valid explicit authority. The narrow payout-recipient rule is separate in [ADR-P076](../00-start-here/DECISIONS.md#adr-p076) / [WF-06](06-completion-settlement-payout.md).
