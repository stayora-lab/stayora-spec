# Overview — Stayora Product Foundation

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P001](../00-start-here/DECISIONS.md#adr-p001), [ADR-P003](../00-start-here/DECISIONS.md#adr-p003), [ADR-P004](../00-start-here/DECISIONS.md#adr-p004), [ADR-P013](../00-start-here/DECISIONS.md#adr-p013), [ADR-P015](../00-start-here/DECISIONS.md#adr-p015), [ADR-P020](../00-start-here/DECISIONS.md#adr-p020), [ADR-P021](../00-start-here/DECISIONS.md#adr-p021), [ADR-P029](../00-start-here/DECISIONS.md#adr-p029)

## Stayora là gì

**CONFIRMED — định hướng sản phẩm.** Stayora kết nối nguồn cung villa, mạng lưới Sale/Affiliate, trust, booking và vận hành lưu trú trong những destination có nhiều bên độc lập. Oceanami là nơi đầu tiên kiểm chứng. Owner Listed và Stayora Verified thuộc foundation hiện tại; Managed nằm ngoài current core.

**WORKING MODEL — cách diễn đạt tổng hợp:** “Stayora là marketplace và operating network cho các destination lưu trú có nguồn cung phân mảnh.” Câu định vị không tự mở thêm scope kỹ thuật.

| Lớp giá trị | Foundation đã có | Chưa được suy ra |
|---|---|---|
| Marketplace | Supply mở, giá thật minh bạch, direct và Sale-assisted booking | Mọi villa tự động publish hoặc final pricing engine |
| Distribution | Sale trung tâm; Affiliate riêng; lead từ Guest cần tư vấn | Tỷ lệ phí và dispatch algorithm đã chốt |
| Inventory | Một villa-night một truth, external confirmed có cùng authority | Zero overbooking mọi OTA |
| Operations | Stay từ mọi nguồn có thể phục vụ Butler/BQL | Mọi external booking được Stayora bảo đảm tiền/hỗ trợ thương mại |
| Trust | Verified assurance; reputation theo trách nhiệm/evidence | Luxury gating hoặc tất cả actor đều có public star score |
| Money | Booking/payment/stay/settlement tách biệt; Payment Session / Attempt thuộc Money; payout sau completed stay hoặc policy-driven exception eligibility | Pháp lý collection/thuế đã được xác nhận |

## Luồng khái niệm

Guest có thể tự tìm và đặt, hoặc nhờ Sale tư vấn. Request chờ Primary Host/Co-host có quyền; chưa tạo exclusive Inventory Commitment. Authorized acceptance có thể tạo Temporary Exclusive Inventory Commitment trong commitment window, trong khi Money thực hiện Payment Session / Attempt riêng. Booking Confirmation cần các điều kiện áp dụng, gồm Required Payment Condition; không mặc định 100%. Instant Book bỏ bước accept từng request khi đủ điều kiện, nhưng vẫn cần kiểm tra inventory và Required Payment Condition. Booking confirmed cung cấp đầu vào cho stay operations; Completed Stay là normal settlement eligibility boundary, không phải duy nhất. Reputation phát sinh khi interaction/stay có evidence đủ điều kiện.

External confirmed booking đi vào inventory và operations với authority tương đương về villa-night. Việc nguồn commerce nằm ngoài Stayora không tự tạo payment/commission của Stayora và không loại stay khỏi reputation nếu đủ evidence.

Đây là mô tả concept, không phải state machine kỹ thuật hoàn chỉnh. Exception, timeout, concurrency, no-show và dispute policy còn mở.

## Mục đích Checkpoint 1

Gói này tạo ngôn ngữ và ranh giới nhất quán để founder review. Nó ghi cả quyết định và điều chưa quyết định, giữ history superseded. Các checkpoint Domain, Authority, Workflows, State Machines, Policies, V0, IA, Data, UX và Implementation chưa được thực hiện trong gói này. Thứ tự chi tiết V0/IA trong các plan cũ có khác nhau; không cần giải thành scope build ở Foundation.

Đọc [nguyên tắc](04-product-principles.md), [marketplace](05-marketplace-model.md), [actors](06-ecosystem-and-actors.md), [money](09-money-model.md), rồi [open questions](13-open-questions.md).
