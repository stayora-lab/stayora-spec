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

**TBD:** chuyển Primary Host, source bị thu hồi, Property offboarding, dispute, nhiều grants/restrictions hợp lệ cùng lúc, và ảnh hưởng tới Booking/Stay đang chạy. Không tự chọn “Host wins”, “latest wins” hoặc “deny always wins”.

## Liên kết nguồn và review

[Foundation ADR-P009–010](../00-start-here/DECISIONS.md#adr-p009), [Domain ownership](../02-domain/02-domain-ownership.md), [Effective Permission](05-effective-permission.md), [Authority questions](07-open-authority-questions.md).
