# Domain Glossary — Vietnamese-first + English canonical mapping

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**

Mỗi thuật ngữ có một English canonical term ổn định để Domain → Engineering về sau không đổi tên tùy tiện. Các định nghĩa là business concepts, không phải schema hoặc enum.

| Thuật ngữ ưu tiên | English canonical term | Định nghĩa ngắn | Không phải / dễ nhầm với | Domain sở hữu |
|---|---|---|---|---|
| Danh tính | Identity | Danh tính nền tảng của một người/tổ chức. Một Identity có thể có nhiều role. | Account type tách biệt theo nghề | Identity & Authority |
| Tác nhân | Actor | Người/tổ chức tham gia một interaction hoặc relationship. | Role hoặc permission | Identity & Authority |
| Vai trò | Role | Vai trò được kích hoạt trên Identity, như Guest, Sale, Butler, Host. | Authority trên mọi resource | Identity & Authority |
| Quyền hạn | Authority | Khả năng hợp lệ để hành động trong một resource/scope. | Role name đơn thuần | Identity & Authority |
| Chủ nhà chính | Primary Host | Actor chịu trách nhiệm chính và có commercial/hosting authority chính trên Property trong một thời điểm. | Legal Owner bắt buộc | Identity & Authority / Property |
| Đồng quản lý | Co-host | Actor được Primary Host delegate quyền trong phạm vi cụ thể. | Sale mặc định hoặc Owner | Identity & Authority / Property |
| Quyền kinh doanh | Commercial Authority | Quyền hợp lệ quyết định/đại diện commercial operation trên một inventory scope. | Legal ownership hoặc payout recipient | Identity & Authority |
| Chủ sở hữu | Owner / Legal Owner | Người sở hữu tài sản hoặc quyền pháp lý liên quan. | Primary Host, Commercial Authority holder | Property |
| Cơ sở lưu trú | Property | Cơ sở/accommodation identity và cấu trúc được đưa vào marketplace. | Bookable Unit hoặc Inventory | Property |
| Đơn vị có thể đặt | Bookable Unit | Đơn vị nhỏ nhất có thể độc lập được commit trong Booking. | Property luôn luôn là một Bookable Unit | Property |
| Nguồn phòng | Inventory | Truth về khả năng commit của Bookable Unit theo thời gian. | Listing, Property content hoặc Booking | Inventory |
| Sự thật nguồn phòng | Inventory Truth | Trạng thái authoritative của Bookable Unit × Time, bất kể booking source. | Calendar riêng của một channel | Inventory |
| Khả năng có thể đặt | Inventory Availability | Derived truth được tính từ effective Inventory Commitments trên Bookable Unit + time range. AVAILABLE/HELD/BOOKED/BLOCKED chỉ là availability semantics/projections, không phải một persisted lifecycle enum đóng tại đây. | Inventory Commitment hoặc technical availability state | Inventory |
| Cam kết nguồn phòng | Inventory Commitment | Umbrella concept gồm Temporary Exclusive Commitment, Confirmed Accommodation Commitment và Availability Block. | Request, Lead, Offer hoặc Stay | Inventory |
| Cam kết độc quyền tạm thời | Temporary Exclusive Inventory Commitment | Cam kết Inventory độc quyền có hạn trong commitment/payment window. | Payment Session / Attempt | Inventory |
| Chặn lịch | Block / Availability Block | Tín hiệu làm Bookable Unit không thể commit, như Owner Block hoặc Maintenance Block. | Booking hoặc Payment Session / Attempt | Inventory |
| Cam kết Inventory tạm thời | Temporary Exclusive Inventory Commitment | Cam kết hữu hạn do authorized acceptance tạo ra; thuộc Inventory, có authoritative end theo policy. | Request pending; Payment Session / Attempt | Inventory |
| Session / Attempt thanh toán | Payment Session / Attempt | Nỗ lực hoặc phiên xử lý payment thuộc Money; không phải Inventory Commitment. | Temporary Inventory Commitment; Booking Confirmation Conditions | Money |
| Đề nghị đặt chỗ | Offer | Commercial proposition theo Bookable Unit, dates, context, Public Price và conditions. Marketplace có thể compose/present Offer; aggregate/domain ownership vẫn TBD. | Booking committed hoặc Price catalog | Conceptual composition boundary; ownership TBD |
| Giá công khai | Public Price | Giá chung làm điểm xuất phát cho Direct Guest và Sale trong cùng Offer context. | Owner Payout hoặc Sale commission | Marketplace & Discovery / Money reference |
| Booking | Booking | Commercial commitment với parties, dates, conditions và snapshot. | Stay, Payment hoặc Settlement | Booking |
| Đề nghị đặt | Request Booking | Yêu cầu booking đang chờ Host/authorized Co-host quyết định; không tự reserve Inventory. | Temporary Inventory Commitment hoặc Confirmed Booking | Booking |
| Đặt ngay | Instant Book | Booking commitment không cần accept từng request khi đủ eligibility, policy và payment conditions. | Bỏ qua kiểm tra Inventory/payment | Booking |
| Booking ngoài | External Booking | Commerce/booking record được tạo bên ngoài Stayora, từ Airbnb, Booking.com, Owner Direct, Sale/Zalo hoặc nguồn khác. Stayora chỉ reference hoặc ghi nhận tối thiểu để thiết lập Inventory Truth và/hoặc tạo External Stay; không cần Stayora Booking. | Stay đã thực sự diễn ra; không phải một Stayora Booking bắt buộc | External commerce concept; được Inventory và Stay tham chiếu |
| Kỳ lưu trú | Stay | Operational lifecycle của một lần lưu trú thực tế hoặc dự kiến. | Booking commerce commitment | Stay |
| Kỳ lưu trú ngoài | External Stay | Stay không nhất thiết bắt nguồn từ Stayora Booking nhưng tham gia operational network khi đủ evidence. | External Booking record duy nhất | Stay |
| Nhóm khách lưu trú | Staying Party | Người thực sự dự kiến/đã lưu trú; có thể khác số liệu commercial trong Booking. | Guest Identity duy nhất hoặc Booking party | Stay |
| Điểm đến | Destination | First-class context có identity, membership, local capabilities và operating relationships. | Location/filter string | Destination |
| Vận hành điểm đến | Destination Operations | Workflows arrival, access, QR, gate, security, cart, checkout và coordination. | Destination identity hoặc commercial pricing | Destination Operations |
| Sale | Sale | Actor tạo conversion, tư vấn, relationship và phân phối inventory. | Affiliate hoặc Co-host mặc định | Distribution |
| Affiliate | Affiliate | Actor/kênh tạo acquisition/referral. | Sale chỉ đổi tên | Distribution |
| Quan hệ phân phối | Distribution Relationship | Quan hệ Sale ↔ Owner / Authorized Host trong commercial authority scope, gồm whitelist/blacklist. | Platform Sale approval | Distribution |
| Lead | Lead | Demand cần được phân phối/xử lý, thường từ Guest yêu cầu tư vấn. | Booking hoặc Attribution | Distribution |
| Quy nguồn đóng góp | Attribution | Ghi nhận ai/kênh nào tạo acquisition, conversion hoặc đóng góp vào Booking. | Payment entitlement tự động | Distribution |
| Xác minh | Verification | Quy trình kiểm tra evidence, standards, inspection và verification programs — trọng tâm là Property-supply quality như Stayora Verified. Identity verification và platform eligibility thuộc Identity & Authority. | Reputation history; không phải toàn bộ Identity verification | Verification |
| Đã xác minh bởi Stayora | Stayora Verified | Lớp Trust & Quality Assurance về accuracy, condition, safety/readiness và accountability đã cam kết. | Luxury badge, Managed, Identity verification | Verification |
| Uy tín | Reputation | Tín hiệu lịch sử tích lũy từ interaction/stay có evidence. | Verification certification hoặc TrustScore duy nhất | Reputation |
| Quyền đánh giá | Review Right | Quyền review phát sinh từ interaction/stay đủ điều kiện. | Có account là review mọi nơi | Reputation |
| Sự cố và xử lý | Incident & Resolution | Ghi nhận điều xảy ra trong Stay/Operations, người xử lý và resolution/accountability. | Tự động rewrite Reputation/Verified | Stay / Destination Operations supporting capability |
| Thanh toán | Payment | Tiền được yêu cầu, thực hiện, nhận, refund hoặc điều chỉnh. | Booking confirmation hoặc Settlement | Money |
| Điều kiện thanh toán bắt buộc | Required Payment Condition | Một Booking Confirmation Condition áp dụng; không nhất thiết là 100% payment. | Fully Paid hoặc Payment Received ở mọi thời điểm | Money / Booking reference |
| Trạng thái không đáp ứng thanh toán | Payment Default | Policy determination khi một Payment Obligation đã đến hạn nhưng chưa được thỏa mãn sau deadline, extension/cancellation hợp lệ và reconciliation/grace áp dụng; không chỉ là thiếu điều kiện xác nhận ban đầu. UNKNOWN provider result chưa tự là Default. | No-show hoặc Cancellation | Money / Booking reference |
| Quyền được hưởng | Entitlement | Phần kinh tế mà actor/resource được phân bổ theo rule và attribution. | Tiền đã Paid | Money |
| Hoa hồng | Commission | Khoản distribution entitlement; Sale base là 10% Commissionable Booking Value. | Affiliate rate ~3% đã chốt | Money / Distribution reference |
| Đối soát / phân bổ | Settlement | Reconciliation và phân bổ nghĩa vụ/entitlement sau Economic Eligibility; Completed Stay là normal boundary, exception path có thể tồn tại theo policy. | Payment Received hoặc Booking Confirmed | Money |
| Chi trả | Payout | Tiền được chuyển/chi trả sau khi entitlement đủ điều kiện. | Earned hoặc Settlement record chưa Paid | Money |

## Các phân biệt bắt buộc

`Owner ≠ Primary Host`; `Property ≠ Bookable Unit`; `Booking ≠ Stay`; `Request ≠ Inventory Commitment`; `Payment Session / Attempt ≠ Temporary Inventory Commitment`; `External Booking ≠ Stayora Booking`; `Payment Received ≠ Booking Confirmed`; `Payment Received ≠ Fully Paid`; `Payment Default ≠ No-show`; `Physical absence ≠ Inventory Release`; `Role ≠ Authority`; `Identity Verification ≠ Stayora Verified`; `Verification ≠ Reputation`; `Public Price ≠ Owner Payout`.
