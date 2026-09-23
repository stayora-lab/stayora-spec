# Destination Model

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P004](../00-start-here/DECISIONS.md#adr-p004), [ADR-P005](../00-start-here/DECISIONS.md#adr-p005), [ADR-P016](../00-start-here/DECISIONS.md#adr-p016), [ADR-P027](../00-start-here/DECISIONS.md#adr-p027), [ADR-P028](../00-start-here/DECISIONS.md#adr-p028), [ADR-P035](../00-start-here/DECISIONS.md#adr-p035), [ADR-P049](../00-start-here/DECISIONS.md#adr-p049)

## First-class domain

**CONFIRMED.** Destination vừa có vai trò discovery phía Guest, vừa tạo operational boundary cho property, BQL/security, local services, policies và integrations. Oceanami không chỉ là text trong địa chỉ villa.

| Lớp — CONFIRMED principle | Trách nhiệm | Ví dụ để hiểu, chưa là schema |
|---|---|---|
| Stayora Core | Khái niệm chung và capabilities | Identity, Host/Co-host, inventory, booking, stay, payment/settlement, trust |
| Destination | Phạm vi tổ chức supply và operations | Oceanami, properties, destination staff/relationships |
| Configuration / integration | Cách vận hành địa phương | Gate QR, đăng ký arrival, xe điện, quy tắc Butler |

Core không hard-code Oceanami; destination policy cũng không mặc định được override các principle chung như scoped data hoặc inventory truth. Thứ tự ưu tiên policy và quyền cấu hình chi tiết là **TBD**.

## Discovery

**CONFIRMED — direction.** Guest có thể khám phá destination như một đối tượng có thông tin và supply. **WORKING MODEL:** story, facilities, experiences, villas và dịch vụ là cách trình bày có thể dùng; không phải danh sách page, feature hoặc content model V0 đã chốt.

## Operations và BQL

**CONFIRMED.** Nhân sự BQL được scoped theo destination và chức năng. BQL Oceanami không có quyền xem destination khác. Nhu cầu vận hành gồm biết villa/ngày/số khách, arrival/departure và phối hợp Butler/security/services. Không cần biết Owner net hoặc Sale commission để làm những việc đó.

**CONFIRMED — hướng Oceanami đã mô tả.** QR giúp xác nhận thông tin tại cổng; Butler báo checkout/yêu cầu xe; BQL điều phối và lưu lịch sử. **TBD:** evidence xác nhận, offline fallback, QR validity/revocation, nhiều xe/vào lại, thời điểm guest registration, ai chịu trách nhiệm xử lý exception. Gate entry không tự là check-in hoặc bằng chứng completed stay.

## Local policy không phải global rule

Tối đa hai Butler đăng ký/villa là quy tắc Oceanami founder thuật lại. Xe điện, security gate và yêu cầu arrival cũng thuộc local operations. Chưa có bằng chứng BQL đã ký cam kết triển khai hoặc đồng ý chỉ nhận booking commerce qua Stayora. External stays từ các kênh khác vẫn có thể tham gia operations.

**WORKING MODEL.** Independent property có thể không có BQL integration; geographic destination và operational cluster cần tách rõ khi đặc tả. **TBD:** membership nhiều cấp, ranh giới địa lý, một property thuộc nhiều nhóm, onboarding/offboarding destination và owner của configuration.

## Giá và dữ liệu

**CONFIRMED.** BQL không là cơ quan quyết định giá bán villa. BDD/cư dân không đồng nhất với BQL; ý tưởng floor cộng đồng đã parked. Destination-first không cấp quyền thu toàn bộ dữ liệu commerce của external stays.

Xem [Oceanami pilot](10-oceanami-pilot.md), [metrics](11-success-metrics.md) và [actors](06-ecosystem-and-actors.md).
