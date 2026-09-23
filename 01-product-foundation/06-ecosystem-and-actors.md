# Ecosystem and Actors

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P006](../00-start-here/DECISIONS.md#adr-p006), [ADR-P007](../00-start-here/DECISIONS.md#adr-p007), [ADR-P008](../00-start-here/DECISIONS.md#adr-p008), [ADR-P009](../00-start-here/DECISIONS.md#adr-p009), [ADR-P010](../00-start-here/DECISIONS.md#adr-p010), [ADR-P011](../00-start-here/DECISIONS.md#adr-p011), [ADR-P012](../00-start-here/DECISIONS.md#adr-p012), [ADR-P027](../00-start-here/DECISIONS.md#adr-p027), [ADR-P028](../00-start-here/DECISIONS.md#adr-p028), [ADR-P032](../00-start-here/DECISIONS.md#adr-p032), [ADR-P033](../00-start-here/DECISIONS.md#adr-p033), [ADR-P034](../00-start-here/DECISIONS.md#adr-p034), [ADR-P043](../00-start-here/DECISIONS.md#adr-p043)

## Identity và authority

**CONFIRMED.** Một identity có thể mang nhiều vai trò. Authority xuất phát từ role + relationship + resource scope; không từ một nhãn account duy nhất. Legal ownership, quyền khai thác, Primary Host authority và người nhận payout không được mặc định là cùng một người.

Mỗi villa có một Primary Host tại một thời điểm, nhiều Co-host. Primary Host có thể delegate accept/reject; Co-host được cấp quyền hành động với authority tương ứng. Quyền tài chính, chuyển Primary Host, payout identity và quyền nhạy cảm chi tiết vẫn **TBD**. Bảng dưới là Foundation responsibility map, không phải permission matrix hoàn chỉnh.

| Actor | Vai trò hiện hành | Onboarding/relationship | Data boundary đã rõ |
|---|---|---|---|
| Guest | Tìm/chọn, booking, sử dụng stay, phản hồi | Self-onboard; xem confirmation có nhánh không account | Dữ liệu booking liên quan; exact access/action TBD |
| Legal Owner | Sở hữu tài sản/quyền liên quan | Chứng cứ quyền sở hữu/khai thác theo compliance TBD | Không tự có mọi quyền khi chưa thiết lập Host relationship |
| Primary Host | Đầu mối chịu trách nhiệm chính của villa | Host self-onboard; property compliance; một Primary Host | Quản lý villa và quyền delegate; finance theo entitlement/authority |
| Co-host | Hỗ trợ quản lý villa | Primary Host cấp quyền trong phạm vi cụ thể | Không all-or-nothing; không mặc định xem mọi finance |
| Sale | Tư vấn, conversion, relationship, booking request | Apply/Stayora approval; trust relationship với Owner/Authorized Host | Availability, One Public Price, commission của mình, booking liên quan; không Owner net/payout/tax/settlement |
| Affiliate | Acquisition/referral | Approval model TBD | Attribution/economics liên quan; fields và privacy TBD |
| Butler | Phục vụ stay, IN/OUT/clean theo quan hệ được giao | Apply/approval rồi Host assign | Chỉ villa/stay được giao và dữ liệu cần vận hành; không full commercial ledger |
| BQL / Destination Staff | Operations, security, guest services của destination | Cấp quyền theo destination/chức năng; quy trình onboarding TBD | Dữ liệu phục vụ arrival/access/operations; không global data hoặc Sale commission |
| Sales Coordinator | Nhân sự Stayora giám sát lead, xử lý exception | Internal role theo chức năng | Lead history và quyền điều phối được cấp; không tự full finance admin |
| Stayora internal finance/support/admin | Nhiệm vụ platform theo chức năng | Quyền nội bộ cần đặc tả | Không mặc định mọi admin xem/sửa tất cả |
| BDD | Context cộng đồng/đại diện cư dân | Chưa có role sản phẩm được chốt | Không tự có dashboard Guest/finance hoặc quyền giá |

## Butler và trách nhiệm thực tế

**CONFIRMED.** Butler do Owner/Host chọn và thiết lập quan hệ dịch vụ; một Butler có thể làm nhiều villa, một villa có nhiều Butler. Platform approval không phải tuyển dụng. Butler chịu trách nhiệm kết quả phần việc dù tự dọn hay thuê người dọn; Stayora không quản việc họ tuyển ai để thực hiện cleaning.

Giới hạn hai Butler/villa là bối cảnh Oceanami được founder thuật lại, không rule global. Assignment theo stay, thay ca và phạm vi delegation cần đặc tả; không tự cho approved Butler thấy mọi villa.

## Financial và Guest data

**CONFIRMED.** Tham gia booking không đồng nghĩa được thấy toàn bộ booking. Sale xem One Public Price và phần economics của mình; Butler/BQL không mặc định xem ledger; staff nội bộ phân quyền theo chức năng. Relationship-scoped access cũng áp dụng cho Guest contact và stay data.

**CONFIRMED PRINCIPLE.** Guest operational data is progressively disclosed according to relationship, lifecycle, operational need và authority/scope. **TBD / POLICY:** exact fields, actors, lifecycle timing, retention periods, masking rules, consent, audit/export, quyền xem Guest history và xử lý tranh chấp. Privacy/retention obligations vẫn legal-validation-required. Đây không phải field-level permission matrix đã freeze.

## Những phân biệt không được mất

- Guest xem QR không account không đồng nghĩa được truy cập công khai PII/finance hoặc có review right tự động.
- Whitelist là quan hệ tin tưởng; không thay platform approval/eligibility.
- Approval Sale không cho quyền accept thay Host; dual-role cần authority rõ cho hành động.
- Quyết định Managed cũ về sửa chữa và chi phí không tạo quyền Stayora vận hành mọi Owner Listed/Verified.

Xem [Destination](07-destination-model.md), [Trust](08-trust-verified-reputation.md) và [Open Questions](13-open-questions.md).
