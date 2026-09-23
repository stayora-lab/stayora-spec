# Glossary — ngôn ngữ dùng chung

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

## Khái niệm và ranh giới

Các định nghĩa dưới đây chuẩn hóa ngôn ngữ tài liệu, không tự quyết schema, enum hay state machine. Status của rule đi theo [Decision register](DECISIONS.md).

| Thuật ngữ | Nghĩa trong Foundation | Không được đánh đồng |
|---|---|---|
| Stayora | Marketplace và operating network cho destination có nguồn cung lưu trú phân mảnh. | Công ty trực tiếp vận hành mọi villa hoặc OTA chỉ bán booking. |
| Marketplace | Nơi supply, demand, distribution và giao dịch gặp nhau. | Toàn bộ destination operations. |
| Destination | First-class domain cho discovery và operational boundary. | Chuỗi địa chỉ hoặc BQL global. |
| Destination configuration | Policies, services và integrations địa phương. | Rule cố định của mọi Stayora property. |
| Property / Villa | Đơn vị tài sản/lưu trú; villa là dạng tài sản pilot. | Listing, legal ownership hoặc một booking. |
| Listing / Owner Listed | Thông tin chào bán do Host cung cấp theo điều kiện marketplace. | Lời đảm bảo Stayora Verified. |
| Owner / Legal Owner | Người sở hữu tài sản; từ “Owner” trong nguồn cũ đôi khi chỉ người vận hành. | Primary Host, người được payout hoặc tax subject trong mọi trường hợp. |
| Primary Host | Một đầu mối chịu trách nhiệm và có authority chính cho villa tại một thời điểm. | Bắt buộc legal owner. |
| Co-host | Relationship quản lý được Primary Host delegate quyền. | Mọi Sale bán villa. |
| Identity | Danh tính chung; một người có thể có nhiều role/relationship. | Một account type riêng cho mỗi nghề. |
| Role | Năng lực/vai trò ở mức hệ sinh thái. | Permission trên mọi resource. |
| Relationship | Quan hệ với villa, booking, stay hoặc destination làm căn cứ access. | Quyền vô hạn/vĩnh viễn. |
| Sale | Actor tư vấn, conversion, chăm sóc và phân phối inventory. | Affiliate hoặc Co-host mặc định. |
| Affiliate | Actor/kênh acquisition và referral. | Sale chỉ đổi tên; cũng không tự có cùng approval/rate. |
| Sales Coordinator | Nhân sự Stayora giám sát và xử lý lead exception. | Sale tier cao. |
| Butler / Quản gia | Người được Host lựa chọn/assign để thực hiện vận hành và chịu trách nhiệm phần việc. | Nhân viên Stayora chỉ vì platform approved. |
| Guest | Người sử dụng dịch vụ lưu trú; một số quyền xem confirmation có thể không cần account. | Bắt buộc người chuyển tiền hoặc người đứng tên booking. |
| BQL / Destination Staff | Nhân sự ban quản lý/phục vụ destination, access theo scope. | BDD hoặc quyền điều khiển giá. |
| BDD | Ban đại diện cư dân theo cách founder gọi trong discovery. | BQL; chưa có authority sản phẩm cụ thể được chốt. |
| Normallist | Quan hệ Sale mặc định, có thể request khi hợp lệ. | Quyền Instant Book. |
| Whitelist | Trust relationship Sale ↔ Owner / Authorized Host trên inventory thuộc commercial authority của bên Host. | Không tự cấp mọi capability; vẫn cần property policy và platform eligibility. |
| Blacklist | Owner / Authorized Host chặn Sale tương tác/book trên inventory scope thuộc commercial authority. | Không mặc định là ban toàn platform hoặc chỉ một property. |
| Inventory / villa-night | Tình trạng authoritative của một villa trong một đêm. | Calendar riêng của từng kênh có thể bán chồng. |
| Request | Ý định đặt, chờ Host/authorized Co-host quyết định. | Reservation hoặc hold. |
| Payment Session / Attempt | Phiên/lần thực hiện payment thuộc Money; kết quả có thể SUCCEEDED, FAILED hoặc UNKNOWN ở mức conceptual reasoning. | Temporary Inventory Commitment hoặc security/damage deposit. |
| Temporary Inventory Commitment | Cam kết inventory độc quyền có hạn do authorized acceptance tạo trong commitment/payment window; thuộc Inventory. | Payment Session / Attempt hoặc Request. |
| Confirmed Accommodation Commitment | Cam kết accommodation đã xác nhận, tạo protected accommodation right và có hiệu lực trên Inventory. | Booking Request hoặc Payment Attempt. |
| Availability Block | Cam kết/chặn Inventory được authorized để ngăn commit trong scope/lifetime xác định. | Request, Lead hoặc Stay. |
| Required Payment Condition | Điều kiện payment áp dụng mà Booking Confirmation cần thỏa mãn; không mặc định là 100% payment. | Fully Paid hoặc Payment Received ở mọi thời điểm. |
| Booking Deposit | Khoản booking payment hướng vào accommodation commitment theo policy. | Security / Damage Deposit. |
| Payment Default | Policy determination khi Payment Obligation đã đến hạn nhưng chưa được thỏa mãn sau deadline và các extension/cancellation/reconciliation/grace hợp lệ. Required Payment Condition chỉ là điều kiện cho một commercial action, không phải toàn bộ future obligations. | No-show, cancellation hoặc payment provider UNKNOWN. |
| Payment Obligation | Nghĩa vụ tài chính và Amount Due/Collections/Refunds/Adjustments; không chỉ là transaction state. | Payment Attempt. |
| Payment Attempt | Lần xử lý payment có lifecycle INITIATED/PROCESSING/SUCCEEDED/FAILED/UNKNOWN. | Payment Obligation hoặc Inventory Commitment. |
| Instant Book | Booking commitment không cần duyệt từng request nếu đủ điều kiện. | Confirmation chỉ từ thao tác bấm nút, hoặc quyền bỏ qua payment. |
| Booking | Cam kết/giao dịch đặt dịch vụ; có nguồn/channel. | Stay đã xảy ra hoặc doanh thu đã earned. |
| External Booking | Booking từ OTA/direct/Zalo/nguồn khác được ghi để phản ánh inventory/operations. | Booking commerce do Stayora tạo. |
| Stay | Việc lưu trú thực tế và hoạt động phục vụ, IN/OUT/incident/completion. | Một payment record; mỗi booking luôn có stay hoàn tất. |
| Completed Stay | Lưu trú đã thực sự kết thúc theo điều kiện sẽ đặc tả. | Check-out click luôn đủ, hoặc no-show tự động. |
| Booking Payment | Tiền thanh toán dịch vụ booking. | Doanh thu Stayora hoặc damage deposit. |
| Security / Damage Deposit | Khoản bảo đảm thiệt hại có lifecycle riêng. | Booking Deposit hoặc cọc đặt phòng; không commissionable. |
| One Public Price | Giá public chung làm điểm xuất phát cho Direct Guest và Sale trong cùng offer context. | Không tự quyết discount limits, funding hoặc stacking. |
| GBV / Booking Value | Giá trị booking ở cấp giao dịch; base chính xác sẽ định nghĩa trong policy. | Tiền thực thu, doanh thu kế toán hoặc Owner net. |
| Commissionable Booking Value | Phần giá trị đủ điều kiện làm cơ sở commission; Sale base distribution commission hiện là 10% của phần này. | Tổng mọi khoản Guest trả. |
| Owner entitlement | Phần kinh tế Owner được hưởng sau phân bổ hợp lệ. | 70% cố định hay tiền đã payout. |
| Owner net / payout | Net là khái niệm economics cần định nghĩa; payout là tiền chi thực tế. | Hai thuật ngữ thay thế tùy ý. |
| Settlement | Đối soát/phân bổ nghĩa vụ tài chính sau Economic Eligibility. Completed Stay là normal boundary; exception eligibility có thể cho phép settlement mà không tạo Completed giả. | Booking confirmed, payment received hoặc bank transfer hoàn tất. |
| Payout | Thực hiện nghĩa vụ đã Settled; lifecycle riêng và failure không revert Settlement. | Settlement entitlement itself. |
| Facilitated collection | Working model payment partner xử lý thu tiền, Stayora điều phối. | Kết luận Stayora có quyền pháp lý giữ tiền/escrow. |
| Stayora revenue | Phần doanh thu của Stayora theo treatment phải xác minh. | Mọi tiền chạy qua payment rail. |
| Stayora Verified | Assurance về thông tin/chất lượng đã cam kết của property, cần duy trì. | Luxury, identity verification, compliance hoặc Managed. |
| Verified stay | Stay có bằng chứng xảy ra và hoàn thành đủ tin cậy để xét reputation. | Villa mang badge Verified. |
| Reputation | Tín hiệu tích lũy từ hoạt động có bằng chứng, gắn trách nhiệm actor/property. | Một điểm sao chung cho cả destination. |
| Review right | Quyền đánh giá phát sinh từ interaction/stay đủ điều kiện. | Có account là được review mọi property. |
| Review Case | Case đánh giá evidence/assessment của Verification; OPEN không tự thành Suspended. | Identity Verification hoặc Reputation state. |
| Lead | Cơ hội phân phối có lifecycle OPEN/IN_PROGRESS/WON/LOST/CLOSED. | Booking hoặc Inventory Authority. |
| Lead Assignment | Quan hệ assignment OFFERED/ACCEPTED/DECLINED/EXPIRED/RELEASED riêng với Lead. | Sale acceptance hoặc supply authority. |
| Platform Eligibility | Trạng thái capability ELIGIBLE/SUSPENDED/REVOKED theo role/capability. | Reputation hoặc Sale–Host relationship. |
| Destination Stay Coverage | Hướng đo phần actual stays được represented trong Stayora. | Commerce share, occupancy, số villa listed hay GMV. |
| Stayora Managed | Business quản lý vận hành riêng đã bị loại khỏi current core/V0. | Tên khác của Verified hoặc Host trên marketplace. |

## Từ cần dùng có điều kiện

- “Confirmed” phải chỉ rõ đang nói **decision status** hay **booking status**.
- “Verified” phải chỉ rõ **property badge**, **identity verification** hay **verified stay**.
- “Deposit” phải ghi Booking Deposit hay Security / Damage Deposit; không dùng một từ cho cả hai.
- Historical note: “Payment Hold” was the former combined label. Current truth uses Payment Session / Attempt (Money) and Temporary Inventory Commitment (Inventory).
- “Owner” trong rule quyền phải đọc lại thành legal ownership hay Primary Host/authorized Co-host. Không đổi mọi chữ Owner thành Primary Host trong các đoạn thuế/tài chính.
- “Invoice” chưa chốt: booking confirmation không tự là hóa đơn thuế hợp lệ. `legal-validation-required / TBD`.
- “Frozen” áp dụng cho đúng artifact/phạm vi đã được founder xác nhận; current reconciliation pass không re-freeze checkpoint gốc.
