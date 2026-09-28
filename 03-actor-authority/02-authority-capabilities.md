# Nhóm năng lực quyền hạn — Authority Capabilities

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 8–10, 12–16.

## Mục đích và phạm vi

Ghi các capability family đã được duyệt ở mức business. Các ví dụ không phải technical permission enums hoặc fixed role bundles.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Capability families — CONFIRMED

| Family | Capability khái niệm | Giới hạn |
|---|---|---|
| Property Authority | View Property; edit information; publish/unpublish khi authorized | Ownership của thông tin thuộc Property; xem không tự có quyền sửa/publish |
| Inventory Authority | View availability; block/unblock; manage availability; establish authorized external commitments | Demand access không tạo quyền thay Inventory Truth |
| Booking Authority | View relevant Booking; accept/reject Request Booking; eligible booking actions | Co-host cần delegation rõ; Sale role không tự accept |
| Distribution Authority | Manage Sale relationships; whitelist/blacklist; relevant distribution delegation | Relationship Sale ↔ Commercial Authority holder trong scope của holder |
| Operations Authority | Assign/change Butler; manage stay preparation; coordinate operational information | Butler assignment không tự cho quyền đổi assignment của người khác |
| Financial Authority | Financial visibility; Settlement authority; Payout authority | Ba capability riêng; xem tiền không tự phân bổ hoặc chi tiền |
| Delegation Authority | Appoint Co-host; grant allowed capabilities; restrict/update; revoke | Không grant quyền mình không có; có thể có quyền non-delegable |

Mọi authority phải có capability, resource scope, lifecycle, source và auditability. Quyền kinh doanh (Commercial Authority) không đồng nghĩa legal ownership hoặc financial beneficiary.

## Record External Commitment — CONFIRMED

Đây là explicit authority capability thuộc Inventory Authority: ghi nhận external confirmed commitment hợp lệ trong granted scope. Sale role hoặc WHITELIST đơn lẻ đều không đủ. Sale được cấp rõ capability này có thể dùng đúng scope; audit giữ authority thực sự được dùng.

Sale thông thường có thể report/submit External Booking. Report đó chưa được tự đổi Inventory Truth thành BOOKED. Việc ghi nhận hợp lệ không được âm thầm overwrite inventory commitment không tương thích. External commerce vẫn nằm ngoài Booking domain Stayora.

**TBD — POLICY:** tiêu chí grant/revoke, evidence threshold và người xử lý report không đủ authority. Không đặt ra một approval workflow mới. Xem [WF-03](../04-core-workflows/03-external-booking-to-stay.md).

## Financial và operational boundaries — CONFIRMED

Primary Host không tự có financial visibility, Settlement authority hay Payout authority trên mọi khoản. Sale chỉ có economics thuộc Sale; Affiliate chỉ own economics cần thiết. Butler/Destination Staff ghi evidence không được tự áp financial/reputation consequences. Money sở hữu financial execution/ledger; actor cần authority tài chính phù hợp để thực hiện hành động liên quan.

## Phần còn mở và liên kết

**TBD:** danh mục non-delegable; exact finance grants; capability granularity và delegation policy. Xem [Delegation](04-delegation-and-scope.md), [Authority questions](07-open-authority-questions.md), [Domain Ownership](../02-domain/02-domain-ownership.md) và [Foundation financial boundaries](../01-product-foundation/06-ecosystem-and-actors.md).

<a id="v0-hosting-relationship-grants"></a>
## V0 hosting relationship grants

**Status: CONFIRMED per [ADR-P075](../00-start-here/DECISIONS.md#adr-p075).** Host capacity is self-service; unit hosting approval is a separate relationship decision. For approved onboarding establishing a Primary, the real Stayora Admin with appropriate Destination authority explicitly establishes the standard set defined below in the same audited action; additional grants require their own canonical basis. Approval is neither legal ownership adjudication nor an implicit permission bundle. Normal transfer and audited Admin replacement are distinct hosting relationship establishment paths, not onboarding requests. In normal transfer, recipient acceptance atomically establishes the incoming relationship/Primary and the standard V0 Primary Host capability set applicable to the unit under canonical policy, together with required provenance/audit. Source is the new Primary relationship plus canonical platform policy, not copied outgoing grants; personal/exception/actor-specific grants and HOST_DAMAGE do not transfer automatically. No effective-Primary/standard-authority gap or later Admin approval/recipient assessment is introduced. Every grant retains capability, scope, lifecycle, source and actual grantor or policy provenance.

### Standard V0 Primary Host capability set

**CONFIRMED per ADR-P075.** Approved onboarding that establishes a Primary and accepted normal Primary transfer establish the SAME standard set for the unit below. Authority does not depend on which valid path established the Primary relationship. This is explicit policy-based establishment, not permission inferred from the HOST label or relationship alone; capability, unit scope, lifecycle, source and audit remain required. The set uses existing business capability names, not new technical permission identifiers.

| Standard capability | Canonical extent and limits |
|---|---|
| Booking Authority | Canonical Host acceptance/rejection of Booking Requests, relevant Booking access and related eligible handling already established in the CP3 family above, [WF-01](../04-core-workflows/01-sale-assisted-request-booking.md) and [ADR-P010](../00-start-here/DECISIONS.md#adr-p010). No additional booking action is inferred. |
| Inventory Authority | Canonical Host availability management, ordinary block/unblock and authoritative external-accommodation recording where applicable, under the CP3 family above, [Owner Block journey](../10-ux-foundation/b5-inventory-intervention/04-owner-block-journey.md), [Inventory Policy](../05-state-machines-policies/13-inventory-policy.md), [FD-12/13](../11-detailed-interaction/CP8-E-FOUNDER-DECISION-RECONCILIATION.md) and [ADR-P074](../00-start-here/DECISIONS.md#adr-p074). Ordinary block/release still requires the applicable canonical authority basis and Unit × Time conditions; the Verified Ownership Relationship basis for Owner Block is not waived. Fact ≠ Commitment; no silent overwrite or general Inventory override. |
| Delegation Authority | Primary-only Co-host invitation/removal and delegation of permitted named capabilities within existing [delegation policy](04-delegation-and-scope.md) and ADR-P010. Only held/delegable capability and valid scope may be granted; no unrestricted onward delegation. |
| Villa Readiness operational authority | Existing Host-support authority under [ADR-P072](../00-start-here/DECISIONS.md#adr-p072): record readiness transitions when the assigned Butler cannot operate the system, including takeover mid-cleaning. No inspection, shortcut or broader operations capability. |

Explicitly EXCLUDED unless separately granted: Protective Hold; Maintenance Block; Butler assignment; Check-in / Checkout authority; financial visibility / general Financial Authority; HOST_DAMAGE; and any personal, exceptional or actor-specific grant. HOST_DAMAGE remains governed/granted under [ADR-P073](../00-start-here/DECISIONS.md#adr-p073). These authorities do not transfer merely because Primary changes. The standard set above is narrow; finer capability granularity, the non-delegable catalogue and unrelated grant/evidence/revocation policies remain open. Do not infer additional capabilities from prototype behavior. [ADR-P076](../00-start-here/DECISIONS.md#adr-p076) separately governs only the outgoing Primary's narrow transfer-time payout choice, not general Financial Authority.
