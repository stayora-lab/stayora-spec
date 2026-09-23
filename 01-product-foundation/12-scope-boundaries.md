# Scope Boundaries

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P003](../00-start-here/DECISIONS.md#adr-p003), [ADR-P035](../00-start-here/DECISIONS.md#adr-p035), [ADR-P048](../00-start-here/DECISIONS.md#adr-p048), [ADR-P049](../00-start-here/DECISIONS.md#adr-p049), [ADR-P050](../00-start-here/DECISIONS.md#adr-p050), [ADR-P051](../00-start-here/DECISIONS.md#adr-p051), [ADR-P052](../00-start-here/DECISIONS.md#adr-p052), [ADR-P053](../00-start-here/DECISIONS.md#adr-p053), [ADR-P054](../00-start-here/DECISIONS.md#adr-p054), [ADR-P055](../00-start-here/DECISIONS.md#adr-p055), [ADR-P056](../00-start-here/DECISIONS.md#adr-p056), [ADR-P057](../00-start-here/DECISIONS.md#adr-p057), [ADR-P058](../00-start-here/DECISIONS.md#adr-p058)

## Scope của Checkpoint 1

**CONFIRMED — nhiệm vụ tài liệu.** Reconcile discovery, decision register và contradiction audit; tạo 18 Markdown files Start Here + Product Foundation, cross-link và consistency check; artifact đã được Founder freeze ngày 2026-09-18. Freeze không chuyển Foundation thành thiết kế Domain/Authority/Workflow/State/Policy/IA/Data/UX hoặc code.

## Conceptual core hiện tại

**CONFIRMED — foundation concepts, không phải must-build list V0:** marketplace mở; Owner Listed/Stayora Verified; One Public Price; Sale base distribution commission 10% trên Commissionable Booking Value; Guest, Primary Host/Co-host, Sale, Butler, Affiliate như actor độc lập; destination/BQL integration; inventory, booking, payment/settlement; external stays; trust/reputation; scoped authority/data. Checkpoint 5 now defines the Oceanami V0 capability boundary; xem [V0 Scope](../06-v0-scope/README.md). Chi tiết ngoài phạm vi CP5 vẫn TBD.

## Đã bị loại rõ

| Nội dung | Status | Ranh giới |
|---|---|---|
| Stayora Managed trong current core/V0 | OUT OF SCOPE — V0 | Founder có thể làm business này bên ngoài; không nhập management P&L/fee/asset authority vào core |
| Managed-as-core cũ | SUPERSEDED | Giữ lịch sử, không đọc như nhánh marketplace hiện hành |
| 30/70 payment foundation | SUPERSEDED | Model mới facilitated collection còn WORKING MODEL/legal TBD |
| Floor bắt buộc/BQL điều khiển giá | SUPERSEDED | Price-floor idea đã parked; transparency và Owner choice hiện hành |
| Account types tách biệt cố định | SUPERSEDED | Một identity có nhiều role/relationship |
| Stayora 2.0 làm source of truth | SUPERSEDED | Có thể tham khảo nhưng adopt lại cần quyết định rõ |

**CONFIRMED — ranh giới trách nhiệm:** không quản việc Butler tự dọn hay thuê ai; không bắt Owner tự vận hành khai toàn bộ chi phí nội bộ; không bắt external stay khai toàn bộ giá và tiền chỉ để vận hành. Đây là product boundaries, không phải danh sách feature chưa làm vì thiếu thời gian.

## Chưa quyết định V0, không tự loại

**TBD.** Granularity của Affiliate, lead automation, Verified inspection, reputation dimensions, QR/BQL integration, sync-health, add-ons, disputes và finance automation trong V0. Khái niệm có trong Foundation không bảo đảm full implementation ở V0; thiếu chi tiết cũng không tự là OUT OF SCOPE — V0.

AI pricing, loyalty, experiences, maintenance marketplace, owner analytics nâng cao, financing, insurance, các mô hình hub/lease/franchise xuất hiện như đề xuất/reference/future possibility. **Không được adopt làm current requirements.** Cần quyết định riêng nếu muốn đưa vào roadmap; không tự đóng tất cả là bị founder loại vĩnh viễn.

## Reference không được nhập ngầm

- Airbnb request hold, cancellation windows và payment details không thay decision Stayora.
- Flexible Payment P1–P5, 20/30/50% deposits, escrow/smart-lock rules không phải current policy.
- Cluster/hub radius, 100-point scorecard, fee 18–22%, ngưỡng tự duyệt sửa chữa và forecast trong operations reference không thuộc core.
- Grok layout và Stayora 2.0 schema không quyết định Destination hierarchy, roles hoặc money flow.
- Số thuế/luật trong chat chưa kiểm chứng không là implementation constants.

## Review boundary

Founder đã xác nhận fidelity và phạm vi artifact ngày 2026-09-18. Những policy TBD tiếp tục giữ mở và không bị nâng thành requirement. Xem [Open Questions](13-open-questions.md) và [audit](../00-start-here/DECISIONS.md#contradiction-audit).
