# Success Metrics

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P020](../00-start-here/DECISIONS.md#adr-p020), [ADR-P022](../00-start-here/DECISIONS.md#adr-p022), [ADR-P029](../00-start-here/DECISIONS.md#adr-p029), [ADR-P030](../00-start-here/DECISIONS.md#adr-p030), [ADR-P045](../00-start-here/DECISIONS.md#adr-p045), [ADR-P048](../00-start-here/DECISIONS.md#adr-p048)

## North Star direction

**CONFIRMED — direction.** Destination Stay Coverage là North Star direction giai đoạn Oceanami. Nó nhìn phần actual stays được represented trong Stayora, bất kể booking source. GMV và Stayora-originated bookings là commerce measures riêng.

**HYPOTHESIS/TBD — measurement.** Exact metric definition, denominator, measurement mechanics và numerical target chưa được chốt.

**WORKING MODEL — biểu thức khái niệm:**

`Destination Stay Coverage = actual stays represented trong Stayora / tổng actual stays của destination trong cùng kỳ`

Đây chưa là measurement specification. Không thể tự suy denominator từ số stay hệ thống đã biết; sẽ tạo vòng tròn và coverage giả. Một external stay không tự tạo GBV commerce của Stayora. Không dùng villa-nights, booking count và stay count thay nhau mà không định nghĩa.

## Measurement questions — TBD

| Vấn đề | Điều cần xác định trước khi báo KPI |
|---|---|
| Actual stay | Một lượt ở tính theo villa hay đoàn, split/multi-villa/extend tính thế nào |
| Represented | Chỉ tạo record đã đủ hay cần dữ liệu tối thiểu/verified completion |
| Denominator | Nguồn tổng actual stays, quyền lấy từ BQL/Host, kiểm tra độ phủ/thiếu |
| Deduplication | Gộp external import/manual/platform records để không đếm đôi |
| Time window | Kỳ tính theo arrival, departure hay occupied nights; timezone |
| Exceptions | Hủy, no-show, move villa, partial stay, stay chưa hoàn tất |
| Evidence quality | Confidence, sampling đối soát và coverage không biết |

## Các chiều thành công

**WORKING MODEL — bộ đo cần phát triển:** supply coverage; operational coverage; Sale adoption; inventory trust; commerce; repeat voluntary usage. Retention Sale 30/60/90 ngày, Owner active inventory rate và Butler usage được đề xuất để hiểu usage thật; chưa có metric definitions/targets chính thức.

## Target hypotheses từ discovery

Toàn bộ bảng là **HYPOTHESIS**, nguồn [SRC-20](../00-start-here/SOURCE_OF_TRUTH.md#src-20); không phải requirement, forecast, SLA hoặc điều kiện pass/fail đã duyệt. Horizon được thảo luận: 12 tháng, chưa chốt lịch pilot.

| Metric candidate | Target hypothesis lịch sử | Cần xác định |
|---|---|---|
| Villa kinh doanh represented | ≥60% | Universe villa kinh doanh và mức active |
| Actual stays represented | ≥70% | Denominator và represented definition |
| Active Sale trong target network | ≥60% | Target network, active event/window |
| Inventory accuracy | ≥95% | Sample, so sánh với truth nào, weighting |
| Stayora-originated bookings / represented stays | ≥25% | Booking khác stay; cần thống nhất đơn vị trước khi dùng tỷ lệ |
| Booking không cần hỏi availability thủ công | ≥80% | Event đo và phạm vi nguồn booking |
| Verified trong participating supply | ≥20–30% | Nguồn ghi khoảng chưa chuẩn hóa; chưa chọn 20 hay 30 |
| Completed Stayora bookings có review | ≥40% | Eligible denominator, thời gian để review |

Ví dụ “70% operational coverage nhưng 15% commerce vẫn thành công” dùng để chốt ưu tiên chiến lược, không xác nhận hai ngưỡng đó là acceptance criteria. Không yêu cầu đạt đồng thời mọi số trong bảng để pilot được xem xét thành công.

## Economics và quality

**TBD.** Take rate thực tế, contribution margin, acquisition/support/verification cost, incident/refund rate và repeat Guest cần định nghĩa phù hợp Money Model. GBV, collected cash và Stayora revenue phải báo riêng. Chưa có final target cho các chỉ số này; không mượn số mô phỏng business reference làm baseline.
