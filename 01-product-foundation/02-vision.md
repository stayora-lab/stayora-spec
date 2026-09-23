# Vision

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P003](../00-start-here/DECISIONS.md#adr-p003), [ADR-P004](../00-start-here/DECISIONS.md#adr-p004), [ADR-P005](../00-start-here/DECISIONS.md#adr-p005), [ADR-P029](../00-start-here/DECISIONS.md#adr-p029), [ADR-P030](../00-start-here/DECISIONS.md#adr-p030), [ADR-P045](../00-start-here/DECISIONS.md#adr-p045), [ADR-P049](../00-start-here/DECISIONS.md#adr-p049)

## Định hướng đã chốt

**CONFIRMED.** Stayora phục vụ nhiều bên cùng tham gia lưu trú, thay vì chỉ gom listing và tạo booking. Owner có nguồn thông tin và thêm kênh phân phối; Sale có inventory và công cụ giao dịch; Butler có lịch và công việc liên quan; BQL có dữ liệu destination cần cho vận hành; Guest có thông tin và trust để chọn nơi ở phù hợp.

Destination là first-class domain. Oceanami là beachhead để chứng minh shared operational truth có giá trị ngay cả trước khi Stayora tạo phần lớn booking. Ưu tiên chiến lược là operational penetration → trusted inventory → network adoption → commerce growth.

## Lời hứa ở mức Foundation

**WORKING MODEL — diễn đạt từ các quyết định đã chốt:**

“Booking platforms aggregate properties. Stayora organizes fragmented destinations.”

Ý nghĩa của câu này là kết nối commerce, distribution, operations và accountability. Nó không khẳng định đối thủ không có những năng lực tương tự, và không trao cho Stayora quyền quản lý tập trung mọi bên.

## Tương lai cần kiểm chứng

**HYPOTHESIS.** Nếu Oceanami tạo được adoption tự nguyện, inventory đáng tin và operational history hữu ích, mô hình có thể nhân rộng sang resort/cluster khác. Network density, trust history và quan hệ giữa các actor có thể tạo lợi thế cạnh tranh. Pilot phải kiểm chứng các quan hệ này; chưa có bằng chứng PMF hoặc dự báo tăng trưởng đáng tin.

**WORKING MODEL.** Core không nên phụ thuộc việc mọi property đều thuộc một resort có BQL. Mô hình independent property, geographic destination và operational destination cần được làm rõ ở Domain; chưa khóa hierarchy `Destination → Resort → Property` từ prototype.

## Ranh giới

Managed nằm ngoài core hiện tại. Tầm nhìn không tự mở scope sang property services, financing, insurance, AI, loyalty, experiences hoặc toàn quốc. Những ý này trong nguồn là khả năng tương lai, chưa được adopt thành V0. Thiết kế UI từ Airbnb/Six Senses là reference về trải nghiệm, không phải authority cho domain/rule.

Xem [business thesis](03-business-thesis.md), [destination model](07-destination-model.md), [scope boundaries](12-scope-boundaries.md).
