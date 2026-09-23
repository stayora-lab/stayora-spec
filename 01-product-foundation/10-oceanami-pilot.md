# Oceanami Pilot

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P015](../00-start-here/DECISIONS.md#adr-p015), [ADR-P016](../00-start-here/DECISIONS.md#adr-p016), [ADR-P026](../00-start-here/DECISIONS.md#adr-p026), [ADR-P029](../00-start-here/DECISIONS.md#adr-p029), [ADR-P030](../00-start-here/DECISIONS.md#adr-p030), [ADR-P045](../00-start-here/DECISIONS.md#adr-p045), [ADR-P046](../00-start-here/DECISIONS.md#adr-p046), [ADR-P049](../00-start-here/DECISIONS.md#adr-p049)

## Mục đích đã chốt

**CONFIRMED.** Oceanami là beachhead và môi trường validation đầu tiên. Founder chấp nhận pilot có thể thành công khi Stayora trở thành phần hạ tầng vận hành hữu ích, dù tỷ lệ booking do Stayora tạo còn thấp. Operational penetration → trusted inventory → network adoption → commerce growth là thứ tự chiến lược.

Đây không là cam kết commerce sẽ tự tăng, cũng không là quyết định triển khai mọi capability vision trong V0. Pilot phải chứng minh usage thật, chất lượng dữ liệu và vai trò của các bên trong destination.

## Điều kiện học từ pilot

**HYPOTHESIS — các câu hỏi validation đã hình thành trong discovery:**

| Câu hỏi | Tín hiệu cần quan sát | Không dùng thay thế |
|---|---|---|
| Host có sẵn lòng tham gia và duy trì inventory? | Active inventory, completeness/freshness, repeat usage | Số account đăng ký |
| Sale có dựa vào availability để làm việc? | Dùng inventory/booking trong nhu cầu thật, giảm hỏi lại | Chỉ xem demo hoặc đồng ý miệng |
| Butler/BQL có nhận giá trị vận hành? | Actual stays có records, arrival/IN/OUT và xử lý liên quan | Giả định BQL đã đồng ý triển khai |
| Guest có tin thông tin? | Giao dịch, incident outcomes, review đủ evidence | Gộp luxury với trust |
| Commerce có phát triển bền vững? | Booking nguồn Stayora, conversion, economics khi có base rõ | Chỉ nhìn GMV như doanh thu Stayora |

## External stays là phần của pilot

**CONFIRMED.** Stay từ Owner direct, Sale/Zalo hoặc OTA khác được represented để phục vụ inventory và operations. Không cần thu toàn bộ doanh thu ngoài. External confirmed có cùng inventory authority; completed external stay đủ evidence có thể đóng góp reputation.

**HYPOTHESIS.** Miễn phí external operations ban đầu có thể giảm rào cản adoption; monetization sau này chưa chốt. Không lấy access gate bắt buộc commerce qua Stayora làm giả định thành công.

## Oceanami Pilot Booking Payment Policy v0.1

**Status: CONFIRMED — Oceanami Pilot policy; NOT a global Stayora invariant.**

### Booking created more than 24 hours before scheduled Check-in

- Initial Payment = 50%.
- Satisfying the 50% Required Payment Condition may allow Booking Confirmation when all other Booking Confirmation Conditions are satisfied.
- Remaining Balance = 50%, due at T-24h before scheduled Check-in.

### Booking created at or within 24 hours before scheduled Check-in

- No partial/deposit confirmation path.
- 100% payment is required to satisfy the Required Payment Condition.

Before commercial commitment, clearly disclose Total Price, Initial Payment, Remaining Balance, exact payment deadline, applicable consequences, Change Policy, Cancellation Policy and No-show policy. Material terms require explicit auditable consent and a policy snapshot.

### T-48h and T-24h checkpoints

T-48h is Pre-arrival / Payment Assurance: system reminder plus Sale and/or Host follow-up as applicable. Butler is not the primary debt collector; Butler focuses on ETA, guest count, readiness and Destination/BQL operations. A reminder does not create the payment obligation.

T-24h is the Commercial Commitment Checkpoint, not primarily an anti-Sale enforcement mechanism. If the required balance remains unsatisfied after the deadline, do not automatically label it Payment Default when provider/payment result is UNKNOWN. Payment Default requires the applicable required balance unsatisfied, deadline passed, no valid approved change/cancellation/exception, and no unresolved provider/payment transaction requiring reconciliation. Exact legal wording/enforceability remains TBD · legal-validation-required.

**TBD — FOUNDER DECISION:** when a transaction begins before the 24-hour boundary but Booking Confirmation occurs at or inside 24 hours, the policy evaluation timestamp (for example, transaction start versus confirmation/commitment time) has not been selected. This pass does not choose it.

## Những gì chưa được xác nhận ngoài thực tế

**TBD.** Số villa/Owner/Sale tham gia, pilot cohort, người tài trợ vận hành, budget, kickoff/date range, BQL agreements, data-sharing permission, quy trình hỗ trợ và phương pháp thu baseline. Founder có kinh nghiệm và network Oceanami không đồng nghĩa mọi đối tác đã cam kết.

Horizon 12 tháng là khung target hypothesis đã được dùng để trao đổi, chưa là lịch launch được duyệt. Các con số 60/70/95… và ứng viên Destination Stay Coverage nằm ở [Success Metrics](11-success-metrics.md), giữ HYPOTHESIS.

## Từ Foundation tới thử nghiệm

**WORKING MODEL — hướng chuẩn bị, không tự thêm deliverable V0:** sau founder review, làm rõ domain/authority/workflows cần thiết; từ đó xác định scope đủ để đo supply, inventory trust, Sale adoption, operational coverage và Guest trust. Chưa quyết UI, database, integration vendor hoặc acceptance criteria trong Checkpoint 1.
