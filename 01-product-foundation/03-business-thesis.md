# Business Thesis

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P011](../00-start-here/DECISIONS.md#adr-p011), [ADR-P016](../00-start-here/DECISIONS.md#adr-p016), [ADR-P029](../00-start-here/DECISIONS.md#adr-p029), [ADR-P031](../00-start-here/DECISIONS.md#adr-p031), [ADR-P032](../00-start-here/DECISIONS.md#adr-p032), [ADR-P039](../00-start-here/DECISIONS.md#adr-p039), [ADR-P045](../00-start-here/DECISIONS.md#adr-p045), [ADR-P046](../00-start-here/DECISIONS.md#adr-p046)

## Thesis đang kiểm chứng

**CONFIRMED — lựa chọn hướng đi.** Stayora bắt đầu bằng marketplace kết hợp operating network tại Oceanami; Sale là trung tâm distribution, không là trung gian phải loại bỏ. External stays vẫn có giá trị dù không tạo commerce cho Stayora.

**HYPOTHESIS — lý do hướng đi có thể thành công.** Khi shared inventory và stay operations đáng tin hơn cách truyền tin thủ công, các actor sẽ tự nguyện dùng thường xuyên. Usage làm operational coverage tốt hơn; coverage giúp inventory/trust hữu ích hơn; từ đó network và commerce có thể phát triển. Đây là giả thuyết nhân quả, không phải kết quả đã chứng minh.

## Giá trị và điều cần chứng minh

| Actor | Giá trị mong muốn từ model hiện tại | Evidence pilot cần quan sát — HYPOTHESIS |
|---|---|---|
| Host | Inventory tập trung, thêm phân phối, visibility và reputation đúng trách nhiệm | Chủ động cập nhật/duy trì inventory và quay lại dùng |
| Sale | Tìm villa nhanh, giá thật, hình ảnh, availability, request/confirmation rõ | Dùng Stayora cho nhu cầu thực thay vì chỉ đăng ký |
| Butler | Biết villa/stay được giao, IN/OUT và yêu cầu liên quan | Thực hiện và cập nhật công việc nhất quán |
| BQL | Arrival/departure, cổng và điều phối ít miss tin, có lịch sử | Dùng dữ liệu trong quy trình thực tế; cần đồng thuận triển khai |
| Guest | Chọn đúng nhu cầu, thấy giá và trách nhiệm, hiểu Verified/reputation | Tin thông tin, hoàn tất giao dịch, review có evidence |
| Affiliate | Attribution acquisition được ghi nhận khi Guest tự đặt hoặc cần Sale | Referral có chất lượng và economics bền vững |

## Distribution và demand

**CONFIRMED.** Demand có thể đến từ Stayora marketing/direct, khách riêng của Sale hoặc Affiliate referral. Guest direct đủ tin tưởng có thể tự đặt; khi cần tư vấn, để lại thông tin để phân lead cho Sale. Affiliate và Sale có thể cùng đóng góp một booking.

**WORKING MODEL.** Sale tiếp tục dùng Zalo cho quan hệ khách hàng, còn Stayora hỗ trợ inventory, booking và operations. Không có requirement xây chat thay Zalo hoặc tích hợp Zalo. “Utility before enforcement” diễn đạt chiến lược adoption; không là sự miễn trừ các booking/access rules.

## Monetization

**CONFIRMED — ý định.** Stayora cần tạo demand và thu nhập từ giao dịch, không chỉ trợ giúp Owner. Sale base distribution commission là 10% của Commissionable Booking Value; ban đầu vẫn ưu tiên phát triển thị trường hơn lợi nhuận ngắn hạn.

**WORKING MODEL.** Platform fee, commission và incentive phải được nhìn tách biệt; mức ~5%/~3%/~2% là baseline mô phỏng. **HYPOTHESIS:** external operations miễn phí ban đầu rồi có thể thu phí. **TBD:** unit economics, chi phí payment/support/verification, CAC, retention, willingness-to-pay và thời điểm monetization. Xem [Money Model](09-money-model.md).

## Điều có thể bác bỏ thesis

**HYPOTHESIS — rủi ro cần thử:** inventory thường xuyên sai khiến Sale quay lại hỏi thủ công; cập nhật external stay quá tốn công; BQL không tham gia; công cụ không tạo repeat voluntary usage; chi phí vận hành/support lớn hơn economics có thể giữ lại. Không chỉ lấy số account hoặc GBV làm bằng chứng thesis đúng.

Không nhập TAM, thị phần OTA hoặc scenario “100 destinations” từ chat thành dự báo của Stayora. Foundation này không cung cấp market sizing đã xác minh.
