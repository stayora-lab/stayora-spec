# Ủy quyền và phạm vi — Delegation and Scope

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 7–8, 10, 12–17.

## Mục đích và phạm vi

Ghi nguyên tắc chuyển giao, giới hạn và thu hồi authority. Mô tả business lifecycle; không thiết kế state enums hay propagation algorithm.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Nguồn và vòng đời authority — CONFIRMED

Mỗi Property có đúng một Primary Host tại một thời điểm trong Stayora authority context. Nguồn authority của Primary Host phải chính đáng; Primary Host có thể khác Legal Owner. Co-host là delegated relationship, nhận đúng capability đã grant chứ không có permission bundle mặc định.

Delegation authority bao gồm appoint Co-host, grant allowed capabilities, restrict/update và revoke trong phạm vi hợp lệ. Không ai delegate quyền mình không sở hữu; một số quyền dù sở hữu vẫn có thể non-delegable. Danh mục và điều kiện cụ thể còn TBD.

| Thành phần cần ghi rõ | Ý nghĩa business |
|---|---|
| Capability | Có thể thực hiện loại hành động nào |
| Resource Scope | Property, Bookable Unit, Booking, Stay hoặc scope phù hợp được grant |
| Lifecycle | Authority còn hiệu lực trong context/thời gian nào |
| Source | Authority nguồn và relationship cho phép grant |
| Auditability | Ai grant/thay đổi/thu hồi, trong tư cách nào, dựa trên gì, với resource và thời điểm nào |

Scope financial phải tách khỏi hosting và operations. Grant quản lý Property không tự trao Owner entitlement hay quyền chọn người nhận Payout.

## Sale relationship và capability — CONFIRMED

NORMAL / WHITELIST / BLACKLIST là Distribution Relationship states. NORMAL là cách gọi trong Checkpoint 3 cho quan hệ mặc định được Foundation gọi Normallist; đây là canonical mapping trong văn bản, không migration enum.

Relationship thuộc Sale ↔ Actor holding Commercial Authority, trên inventory/resource thuộc authority của holder; không quay lại property-only whitelist. WHITELIST không phải capability bundle. Record External Commitment cần grant riêng. Grant/revoke criteria của capability này là **TBD — POLICY**.

## Assignment và quyền tham gia — CONFIRMED

Butler Role, Butler Assignment và Stay Access khác nhau. Destination Staff được scope theo Destination/function. Guest relationship có lifecycle; link/QR chỉ là credential/evidence để xét access, không authority tự thân. Đổi assignment, revoke và offboarding cần giữ audit; thời điểm propagation và xử lý work đang diễn ra vẫn TBD.

## Authority conflict — CONFIRMED principle, TBD precedence

Grant hoặc restriction chỉ có hiệu lực nếu được ban hành/thực hiện qua authority hợp lệ trên đúng action và resource scope. Không dùng “More restrictive authority always wins”. Blacklist trong Distribution scope hợp lệ vẫn có ý nghĩa đã freeze; điều đó không giải precedence giữa nhiều valid authorities hoặc xóa authority từ một acting capacity khác bằng suy luận tự động.

**TBD:** Primary transfer cases beyond the V0 scope of [ADR-P075](../00-start-here/DECISIONS.md#adr-p075), revoked-source effective-time/propagation, Property offboarding, legal dispute, multiple valid grants/restrictions and other effects on ongoing work. The decided V0 transfer preserves Booking/Stay truth as below. Không tự chọn “Host wins”, “latest wins” hoặc “deny always wins”.

## Liên kết nguồn và review

[Foundation ADR-P009–010](../00-start-here/DECISIONS.md#adr-p009), [Domain ownership](../02-domain/02-domain-ownership.md), [Effective Permission](05-effective-permission.md), [Authority questions](07-open-authority-questions.md).

## V0 Primary and delegation continuity

**Status: CONFIRMED per [ADR-P075](../00-start-here/DECISIONS.md#adr-p075).** Initial Primary is the first APPROVED unit-hosting relationship, not the first submitted request. Multiple requests preserve provenance until authorized manual disposition; legal Owner/co-owner precedence remains open.

Normal transfer requires designation by the current Primary and one explicit recipient acceptance. Before acceptance, existing Primary remains and authority does not silently move. On acceptance, outgoing Primary ceases to be Primary and incoming hosting relationship/Primary, applicable standard V0 Primary Host capabilities and required provenance/audit are established atomically. Source is the new Primary relationship plus canonical platform policy; personal/exception/actor-specific grants are not copied and HOST_DAMAGE remains separately granted. There is no standard-authority gap awaiting Admin grants or recipient assessment; acceptance is not a second Stayora approval or proof of ownership. Only Admin-assisted onboarding requires a hosting request; transfer and audited Admin replacement are separate relationship paths. Unresolved capability catalogue names remain open. Retained Co-hosts default to retain in the incoming Primary's confirmation, but delegations must acquire valid incoming-Primary source/provenance rather than surviving on outgoing-Primary authority. Invite/remove remains bounded by valid delegation; any outstanding-work warning is non-blocking and transfers no responsibility automatically.

Admin/operations replacement is an audited manual exception when normal transfer cannot reasonably occur, with real Admin identity, Destination-appropriate authority, reason and external operational verification; no impersonation or arbitrary reassignment. Confirmed bookings/upcoming stays stay with the unit, and applicable future operations require valid explicit authority. Historical actions remain intact; C2-TBD-09 revocation timing/propagation is not decided.

The financial separation above remains: only [ADR-P076](../00-start-here/DECISIONS.md#adr-p076) explicitly grants the outgoing Primary one whole-cohort payout-recipient choice, recorded while transfer is pending and binding/non-editable through that transfer at effectiveness, for bookings CONFIRMED before effectiveness with Stay/check-in afterward. Successive transfers preserve valid retained-payout overrides belonging to other actors; only currently attributable payout direction is within the later outgoing actor's choice. FOLLOW INCOMING/no selection uses the actual-check-in default without a permanent incoming-person lock or cancellation of earlier overrides. It creates neither Owner entitlement nor general Financial Authority and never rewrites Money history.
