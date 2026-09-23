# Marketplace Model

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P001](../00-start-here/DECISIONS.md#adr-p001), [ADR-P011](../00-start-here/DECISIONS.md#adr-p011), [ADR-P012](../00-start-here/DECISIONS.md#adr-p012), [ADR-P013](../00-start-here/DECISIONS.md#adr-p013), [ADR-P014](../00-start-here/DECISIONS.md#adr-p014), [ADR-P015](../00-start-here/DECISIONS.md#adr-p015), [ADR-P016](../00-start-here/DECISIONS.md#adr-p016), [ADR-P017](../00-start-here/DECISIONS.md#adr-p017), [ADR-P018](../00-start-here/DECISIONS.md#adr-p018), [ADR-P023](../00-start-here/DECISIONS.md#adr-p023), [ADR-P024](../00-start-here/DECISIONS.md#adr-p024), [ADR-P031](../00-start-here/DECISIONS.md#adr-p031), [ADR-P032](../00-start-here/DECISIONS.md#adr-p032), [ADR-P033](../00-start-here/DECISIONS.md#adr-p033), [ADR-P034](../00-start-here/DECISIONS.md#adr-p034), [ADR-P041](../00-start-here/DECISIONS.md#adr-p041), [ADR-P042](../00-start-here/DECISIONS.md#adr-p042), [ADR-P047](../00-start-here/DECISIONS.md#adr-p047)

## Supply và chất lượng

**CONFIRMED.** Marketplace mở cho Owner Listed; Verified là lớp assurance riêng. Owner/Host tự vận hành property và chịu trách nhiệm của mình. Self-onboarding không tự publish; legal right/compliance cần được kiểm tra theo policy còn phải xác minh. Managed không là nhánh core hiện hành.

Marketplace tạo điều kiện để Guest so sánh thông tin, giá, reputation và Verified. Không có rule loại mọi villa bình dân hoặc ép cùng mức giá. Guest tự chọn nhu cầu; transparency không có nghĩa công bố Owner net và toàn bộ ledger.

## Demand và distribution

**CONFIRMED.** Direct Guest có đường self-service và đường tư vấn qua Sale. Sale có thể dùng inventory để phục vụ khách riêng. Affiliate là acquisition/referral, có thể cùng attribution với Sale conversion. Sự hiện diện của Affiliate không tự biến lead thành “khách riêng của Sale”, cũng không tự xóa attribution acquisition.

Lead được phân ưu tiên dựa trên chất lượng Sale; Sale nhận phải xử lý/cập nhật. Sales Coordinator thuộc Stayora xử lý exception. **WORKING MODEL:** offer 5–10s, xử lý 24h, xin tối đa +24h; **TBD:** policy timings và thuật toán cuối, cách duyệt gia hạn, chống gaming. Không đưa các con số này vào SLA hiện hành.

## Quan hệ Host–Sale

| Quan hệ — CONFIRMED | Ý nghĩa | Giới hạn |
|---|---|---|
| Normallist | Mặc định được tiếp cận/request inventory hợp lệ | Không có quyền giữ phòng bằng request |
| Whitelist | Trust relationship giữa Sale và Owner/Authorized Host trên inventory trong commercial authority; là điều kiện cần cho Sale Instant Book | Còn cần eligibility nền tảng, property enabled và booking rules |
| Blacklist | Chặn Sale tương tác/book trong inventory scope của Owner/Authorized Host | Exact Domain/Authority refinement vẫn để phase sau |

Sale role không có booking acceptance authority. Nếu người đó đồng thời là Co-host có quyền thì hành động dựa trên relationship Co-host, được audit theo authority đó.

## Booking và inventory

| Bước/nguồn — CONFIRMED principle | Tác động inventory |
|---|---|
| Request pending | Không reserve, không hold |
| Primary Host/authorized Co-host accept | Có thể tạo Temporary Inventory Commitment có hạn; Money mở Payment Session/Attempt riêng |
| Không thỏa applicable confirmation/payment obligation đúng hạn | Temporary authorization/commitment hết hiệu lực theo policy; Availability được recompute. Required Payment Condition áp dụng cho commercial confirmation; các Payment Obligation về sau được xét theo Payment Policy. |
| Payment Session/Attempt đạt điều kiện áp dụng | Đi đến confirmation theo Booking Confirmation Conditions |
| Instant Book đủ điều kiện | Không cần accept riêng; vẫn kiểm tra inventory/payment |
| External confirmed booking | Cùng authority đóng inventory như Stayora confirmed |
| External confirmed trong lúc request pending | Request không được thắng confirmed inventory |

**TBD:** commitment window, concurrent accept, late payment, provider UNKNOWN/reconciliation, hai confirmed từ nhiều nguồn, manual override, cancellation/reopen, no-show/Payment Default và sync failure. Không tự chọn “first timestamp wins” hoặc “Stayora wins”.

**CONFIRMED — hướng integration.** Host ghi nhận direct/Zalo/external booking để truth phản ánh thực tế; iCal hỗ trợ OTA. **WORKING MODEL:** polling 15 phút từ nguồn cũ. Độ trễ vẫn tạo rủi ro; không hứa zero overbooking hoặc realtime khi nguồn ngoài không có real-time integration.

## Giá và commercial transparency

**CONFIRMED.** Giá booking là giá thực bán cho Guest; Sale nhận commission, không hidden spread. Sale có thể tự giảm phần commission mà không giảm entitlement của Owner/Stayora.

**CONFIRMED — ADR-P041.** One Public Price: Direct Guest và Sale bắt đầu từ cùng public booking price. Sale có thể giảm giá bằng cách hy sinh economics thuộc Sale; không giảm Owner entitlement. Discount funding/limits/stacking vẫn TBD. Concept public/direct cao hơn Sale 5–10% là SUPERSEDED trong [ADR-P059](../00-start-here/DECISIONS.md#adr-p059).

## External operations không là commerce bắt buộc

External stay được ghi với dữ liệu đủ vận hành; không ép khai giá và toàn bộ dòng tiền. External confirmed khóa inventory; external verified completed stay có thể tạo reputation. Điều này không tự tạo Sale/platform commission, entitlement refund, hay cam kết Stayora xử lý mọi tranh chấp commerce ngoài hệ thống.

Confirmation/QR xem được không account đã chốt ở principle. Access token, dữ liệu public/private và việc dùng cùng QR cho cổng còn TBD; xem [actors](06-ecosystem-and-actors.md).
