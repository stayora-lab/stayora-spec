# Trust, Verified and Reputation

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P002](../00-start-here/DECISIONS.md#adr-p002), [ADR-P025](../00-start-here/DECISIONS.md#adr-p025), [ADR-P026](../00-start-here/DECISIONS.md#adr-p026), [ADR-P027](../00-start-here/DECISIONS.md#adr-p027), [ADR-P044](../00-start-here/DECISIONS.md#adr-p044), [ADR-P048](../00-start-here/DECISIONS.md#adr-p048)

## Bốn khái niệm khác nhau

**CONFIRMED — distinction từ foundation.** Identity verification hỏi người đó có đúng danh tính; property compliance hỏi quyền hợp lệ đưa villa lên và điều kiện tham gia; Stayora Verified hỏi quality/accuracy đã cam kết; reputation phản ánh lịch sử tương tác có evidence. Một loại xác minh không thay ba loại còn lại.

## Stayora Verified

**CONFIRMED.** Verified là trust/quality assurance, không luxury. Villa ở phân khúc bình dân vẫn có thể đạt nếu thực tế đúng thông tin và chất lượng cam kết. Owner vẫn tự vận hành. Badge cần duy trì; chất lượng/listing không phù hợp có thể làm mất Verified. Không có quyết định “trả tiền là được badge”.

**WORKING MODEL — checklist đề xuất trong nguồn:**

1. Listing accuracy: ảnh, vị trí, phòng, tiện nghi đúng thực tế.
2. Cleanliness and condition: sạch, điều kiện sử dụng phù hợp.
3. Safety and essentials: những yếu tố an toàn/thiết yếu đáp ứng chuẩn cần xác định.
4. Stay readiness: sẵn sàng cung cấp những gì đã hứa.
5. Service accountability: có Host/đầu mối chịu trách nhiệm và phản hồi.
6. Consistency: tiếp tục duy trì chất lượng tương ứng với trạng thái Verified.

Sáu nhóm là đề xuất tổ chức, **chưa phải checklist V0 approved**. Application/inspection/evidence/remediation là assessment workflow; Verification Status và Review Case là các model riêng theo [Checkpoint 4](../05-state-machines-policies/06-verification-and-reputation.md). `REVIEW REQUIRED` không phải Verification Status; Review Case có thể OPEN khi status vẫn VERIFIED. **TBD:** ai kiểm, evidence, tần suất, phí, trigger, appeal/reinstatement, lời hứa support và chuẩn safety cần legal/operational validation.

## Reputation theo trách nhiệm

**CONFIRMED.** Phải phân biệt villa/Host, Butler, Sale và destination services; một review xấu về xe hoặc thái độ không tự quy lỗi cho mọi property Oceanami. Butler chịu trách nhiệm phần việc ngay cả khi thuê người làm. Guest có thể được Host đánh giá; Butler có nguồn đánh giá Guest nội bộ theo discovery.

**WORKING MODEL.** Reputation có nhiều dimensions (accuracy, cleanliness, responsiveness, transaction conduct...), không nhất thiết mọi actor đều hiển thị cùng một điểm sao. Ma trận “ai review ai”, public/private và quyền xem chưa hoàn thiện. BQL operational history hỗ trợ attribution, không tự thành public BQL score đã duyệt.

## External verified stays

**CONFIRMED.** Nguồn booking không quyết định quyền tạo reputation. External stay được ghi trong operations, có bằng chứng thực sự diễn ra và completed, có thể đủ điều kiện. “Verified stay” không đòi villa phải có badge Stayora Verified.

**TBD:** evidence threshold, ai attest, chống self-review/fake stay, quyền Guest không account, guest identity linkage, thời gian review, duplicate reviews từ nhiều nguồn và appeal. QR gate/Butler/BQL có thể là evidence candidates trong working model, không một dấu quét đơn lẻ tự chứng minh completed stay.

## Support và remediation

**CONFIRMED — hướng nguồn.** Stayora có vai trò hỗ trợ các vấn đề thuộc phạm vi booking/Verified liên quan; scope theo trường hợp cần được đặc tả. Không suy ra bảo hiểm, hoàn tiền vô điều kiện hoặc trách nhiệm thương mại cho mọi external stay. Không diễn giải “hạn chế ảnh hưởng rating” thành xóa/che review xấu thật.

**TBD:** incident ownership, compensation, sanctions, reputation impact, dispute evidence và safety/privacy. Xem [Money Model](09-money-model.md) cho refund/settlement; [Open Questions](13-open-questions.md) cho toàn bộ gap.
