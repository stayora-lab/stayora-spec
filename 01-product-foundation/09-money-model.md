# Money Model

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P019](../00-start-here/DECISIONS.md#adr-p019), [ADR-P020](../00-start-here/DECISIONS.md#adr-p020), [ADR-P021](../00-start-here/DECISIONS.md#adr-p021), [ADR-P022](../00-start-here/DECISIONS.md#adr-p022), [ADR-P023](../00-start-here/DECISIONS.md#adr-p023), [ADR-P024](../00-start-here/DECISIONS.md#adr-p024), [ADR-P027](../00-start-here/DECISIONS.md#adr-p027), [ADR-P036](../00-start-here/DECISIONS.md#adr-p036), [ADR-P037](../00-start-here/DECISIONS.md#adr-p037), [ADR-P038](../00-start-here/DECISIONS.md#adr-p038), [ADR-P039](../00-start-here/DECISIONS.md#adr-p039), [ADR-P040](../00-start-here/DECISIONS.md#adr-p040), [ADR-P041](../00-start-here/DECISIONS.md#adr-p041), [ADR-P048](../00-start-here/DECISIONS.md#adr-p048), [ADR-P051](../00-start-here/DECISIONS.md#adr-p051), [ADR-P055](../00-start-here/DECISIONS.md#adr-p055), [ADR-P056](../00-start-here/DECISIONS.md#adr-p056), [ADR-P058](../00-start-here/DECISIONS.md#adr-p058)

## Những điều đã chốt

**CONFIRMED.** Booking acceptance, Payment Session / Attempt, stay completion và settlement là các việc khác nhau. Booking Confirmation requires applicable Booking Confirmation Conditions, including a Required Payment Condition; Required Payment Condition does not necessarily mean Fully Paid. Payment Received ≠ Booking Confirmed and Payment Received ≠ Fully Paid. Completed Stay là normal settlement/economic eligibility boundary; exception policy có thể tạo eligibility cho commercially fulfilled nhưng physically unused accommodation commitment mà không falsify Stay. Security/damage deposit tách khỏi Booking Deposit, không là booking revenue và không commissionable. Add-ons có economics riêng. Commission chỉ dựa trên commissionable value, không tự trên tổng mọi khoản Guest trả.

**CONFIRMED.** Stayora dùng One Public Price: Direct Guest và Sale bắt đầu từ cùng public booking price trong cùng offer context. Sale kiếm commission minh bạch; hidden spread không được phép. Sale có thể cung cấp discount bằng cách hy sinh phần commission/incentive kinh tế thuộc Sale, subject to future policy; không được giảm Owner entitlement. Owner-funded, Stayora-funded, Affiliate/campaign-funded discounts là mechanisms riêng và phải có attribution rõ. Sale không được xem Owner net/payout/tax/settlement chỉ vì tham gia booking.

## Payment direction hiện hành

**WORKING MODEL · legal-validation-required.** Baseline ưu tiên booking money đi qua facilitated collection rail bằng hạ tầng payment partner được cấp phép; Stayora điều phối booking, đối soát, phân bổ và settlement. “Facilitated collection 100%” nói về rail/collection responsibility, không nói Guest phải thanh toán 100% tại Booking Confirmation. Cấu hình thanh toán của Oceanami Pilot được ghi tại [13-destination-operations/oceanami/configuration.md](../13-destination-operations/oceanami/configuration.md) (quyết định: ADR-P061). Đây là hướng product để nghiên cứu, không kết luận mô hình đã được phép triển khai tại Việt Nam, provider nào hỗ trợ hoặc Stayora có quyền giữ tiền.

**SUPERSEDED.** 30% chuyển về tài khoản Stayora và 70% Owner nhận trực tiếp không còn là foundation mặc định. Không áp lại cơ chế này từ checkpoint Câu 34–35. Cũng không dùng lý luận “nhận 30% thì doanh thu chịu thuế là 30%”.

**TBD.** Ai là bên nhận tiền về mặt pháp lý, nguồn xác nhận payment, operator thủ công hay provider notification, matched/partial/overpaid/late transfers, provider UNKNOWN/reconciliation, refund rail và Temporary Inventory Commitment window. Authority Host accept vẫn khác authority xác minh tiền; không tự cho Sale/Host xác nhận payment chỉ bằng lời nói.

## Các lớp giá trị phải phân biệt

| Khái niệm | Điều Foundation bảo vệ | Phần còn TBD |
|---|---|---|
| Guest total payment | Tổng số tiền khách trả không tự là commission base | Bao gồm thuế/add-on/deposit thế nào |
| Booking/room value | Giá trị dịch vụ lưu trú cần nhận diện | Trước/sau giảm giá, thuế/phụ thu |
| Payment Session / Attempt | Phiên/lần payment thực hiện trong Money; UNKNOWN khác FAILED | Provider/result lifecycle, retries và reconciliation |
| Required Payment Condition | Điều kiện payment áp dụng để Booking Confirmation; không mặc định 100% | Exact policy, deadlines, exceptions |
| Booking Deposit | Booking payment hướng vào accommodation commitment | Không phải Security / Damage Deposit |
| Commissionable value | Chỉ phần đủ điều kiện để tính commission | Định nghĩa base chính xác |
| Money collected | Tiền đã nhận qua rail | Thu hộ, người nhận pháp lý, đối soát |
| Owner entitlement | Phần kinh tế Owner được hưởng | Công thức, adjustment, tax incidence |
| Sale/Affiliate payable | Phần quyền lợi của distribution theo attribution | Pending/earned/payable/paid và refund/no-show |
| Stayora revenue | Không suy ra bằng tiền collected | Gross/net recognition và invoice/tax treatment cần xác minh |
| Settlement/payout | Sau Completed Stay trong normal path; policy-driven exception eligibility có thể đi theo path riêng; tiền chi thực tế khác booking confirm | Reconciliation, SLA, dispute, kỳ payout |

Không sử dụng công thức `selling price = Owner net / 70%`. Không coi management fee 10% Managed là platform fee hoặc Sale commission.

## Economics baseline — không phải bảng phí

| Khoản | Status hiện hành | Ghi chú |
|---|---|---|
| Sale base 10% | CONFIRMED | 10% của Commissionable Booking Value. Pending sau confirmation; Completed Stay là normal Earned/settlement eligibility boundary; policy-driven exception economics có thể tồn tại cho commercially fulfilled nhưng physically unused commitment; Paid là state settlement/payment sau đó. Cancellation/refund/no-show vẫn TBD/policy. |
| Affiliate ~3% | WORKING MODEL/TBD | Không được xác nhận con số ~3%; Affiliate có thể lấy từ distribution pool, exact split chưa chốt |
| Affiliate A% + Sale 10%−A% | WORKING MODEL | Giữ founder intent shared distribution; exact split/attribution vẫn TBD |
| Performance incentive ~2% | WORKING MODEL | Chưa final; không hard-code quỹ 5% cũ |
| Stayora platform fee ~5% | WORKING MODEL | Người chịu, base và tax treatment chưa chốt |
| Payment processing | TBD | Actual cost và pricing policy chưa xác định |
| Taxes/withholding | TBD · legal-validation-required | Không hard-code 7% hoặc ngưỡng/thuế suất trong chat |
| Security/damage deposit | CONFIRMED về tách biệt; amount/rules TBD | Không commissionable; claim/refund lifecycle riêng |
| Add-ons | CONFIRMED về economics riêng; rates TBD | Không tự thêm vào room commission |

Không cộng bảng này thành một fee stack đã duyệt hoặc tự suy ra Owner luôn nhận phần còn lại của 17%. No-Sale booking không tự tạo Sale commission; phần distribution không phát sinh sẽ thuộc ai hoặc giảm giá thế nào vẫn **TBD**.

## Pricing còn mở

**CONFIRMED — ADR-P041.** One Public Price thay thế concept cũ public/direct cao hơn Sale 5–10% (ADR-P059 SUPERSEDED). Direct Guest và Sale bắt đầu cùng public booking price; Sale-funded discount chỉ hy sinh economics của Sale. **TBD:** discount limits, stacking, owner/platform/campaign funding và accounting mechanics. Direct Instant Book discount 10% không được tự khôi phục.

## Settlement và ngoại lệ

**CONFIRMED.** Khi booking confirmed, expected economics có thể được ghi nhận nhưng không đồng nghĩa tiền đã earned/paid. Completed Stay là normal trigger, không nhất thiết là economic eligibility path duy nhất. Fully paid/commercially entitled nhưng Guest không sử dụng có thể cần exception settlement path theo later policy; không đánh dấu Stay COMPLETED giả. Payout không đi trước applicable economic eligibility.

**CONFIRMED boundary.** Sau CHECK-OUT, Stay dùng Operational Completion Readiness để xác định liệu Stay đã đủ operational closure để trở thành STAY COMPLETED; bước này không tính payout, commission, revenue, refund allocation hoặc settlement positions. Normal path: sau STAY COMPLETED, Money thực hiện Financial Reconciliation để xác định final economic positions trước Settlement và Payout. Policy-driven Economic Eligibility có thể mở exception reconciliation/settlement path cho commercially fulfilled hoặc qualifying no-use/cancellation/default/supplier-failure economics mà không falsify Stay thành COMPLETED. **TBD:** qualifying exceptions, dispute window, hold phần nào, điều kiện release, refund percentages/deadlines, cancellation/no-show entitlement, chargeback và unfulfilled stay. “Non-refundable/non-changeable” là ý định thương mại Instant Book đã chốt, không miễn mọi remedy khi supplier failure hoặc pháp luật yêu cầu.

## Legal validation cần có trước policy phụ thuộc

Tất cả các mục dưới là **TBD · legal-validation-required**, không phải kết luận luật:

- Pháp nhân phù hợp; tư cách marketplace/intermediary và accommodation supplier theo hợp đồng/thực tế.
- Licensed provider structure; quyền thu hộ, giữ, chi, refund và tách tiền các bên.
- Gross/net revenue recognition của Stayora; entitlement và chứng từ cho Owner/Sale/Affiliate.
- VAT/TNDN/TNCN và withholding/remittance theo từng loại chủ thể/giao dịch; không dùng một mức cho mọi villa.
- Ai xuất invoice/hóa đơn; booking confirmation khác chứng từ thuế thế nào.
- Điều khoản cancellation, supplier failure, deposit claim, complaint và dữ liệu cá nhân.

Nguồn chat có các khẳng định và correction pháp lý khác nhau; gói này không kiểm chứng hoặc tái xác nhận chúng. Hướng Công ty TNHH + intermediary là working product intent, không là lời tư vấn lựa chọn pháp nhân cuối cùng.

Xem [contradiction audit](../00-start-here/DECISIONS.md#contradiction-audit) và [Open Questions](13-open-questions.md).
