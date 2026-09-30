# WF-03 — External Booking → Stay

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 10, 20, 25–27.

## Mục đích và phạm vi

Ghi nhận Inventory/operational truth khi commerce được tạo ngoài Stayora. Không tạo Stayora Booking giả hoặc bắt buộc khai external economics.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Purpose

**CONFIRMED:** Stayora không cần sở hữu Booking để có Inventory/operational truth. External Booking là commerce record được tạo ngoài Stayora; Inventory/Stay có thể reference hoặc ghi tối thiểu cho mục đích được dùng.

## Actors

Host có Record External Commitment authority trong scope ghi nhận external accommodation trực tiếp; actor vận hành có authority tạo/phục vụ Stay; Staying Party, assigned Butler và Destination Staff theo relationship. Ordinary Sale và Butler không submit External Report trong V0 theo [ADR-P074](../00-start-here/DECISIONS.md#adr-p074). Nguồn commerce có thể là Airbnb, Booking.com, Agoda, Owner Direct, Sale/Zalo hoặc nguồn ngoài khác.

## Preconditions

**CONFIRMED:** establish external confirmed commitment cần explicit authority và commitment hợp lệ, không chỉ role/WHITELIST. Stay cần lightweight operational data/evidence phù hợp. Exact evidence threshold và điều kiện tạo Stay vẫn **TBD**; V0 không có bước External Report trước khi Host ghi nhận authoritative theo ADR-P074.

## Trigger

Có external commerce/confirmed commitment cần phản ánh availability và/hoặc có kỳ lưu trú ngoài cần tham gia operating network.

## Happy Path — CONFIRMED

```text
External Commerce
├──→ Inventory Truth
└──→ Stay
       ↓
Destination Operations
```

1. Host được cấp Record External Commitment trong scope ghi nhận external accommodation trực tiếp; một V0 workflow thiết lập External Accommodation Fact và applicable External-backed Commitment như hai truth riêng biệt theo [ADR-P074](../00-start-here/DECISIONS.md#adr-p074), không route qua Stayora Booking.
2. Inventory xét sự tương thích của applicable confirmed commitment với truth hiện có; Fact ≠ Commitment dù cùng một action thiết lập cả hai.
3. Stay được biểu đạt bằng dữ liệu phục vụ vận hành; Foundation nêu villa, IN/OUT, số khách, booking source và thông tin cần cho BQL. Đây không là final required-field schema.
4. Stay tham gia [WF-04](04-stay-lifecycle.md)/Destination Operations theo authority tương ứng.
5. Khi Stay có đủ evidence diễn ra/completed, Reputation có thể tạo eligible Review Rights theo rule riêng.

## Alternative Paths

**CONFIRMED:** dùng nhánh Inventory Truth và/hoặc Stay; không buộc cả hai qua một commerce pipeline. V0 không có ordinary Sale/Butler External Report stage; quyền ghi nhận Host vẫn cần explicit capability trong scope theo ADR-P074. Future untrusted-source reporting remains outside this V0 workflow.

External cancellation/no-show cập nhật operational truth đúng thực tế; không invent external refund, penalty, commission hoặc automatic completion. Shared operations không suy identical commercial responsibility.

## Failure Paths

**CONFIRMED:** external commitment không được silently overwrite incompatible Inventory Truth. Valid external confirmed commitments có availability authority ngang Stayora confirmed commitments; không ưu tiên Stayora source.

**TBD:** conflicting confirmed sources, delayed/duplicate records, manual corrections, validation evidence và escalation. Giữ khái niệm **sync health** (tình trạng cập nhật nguồn) và **inventory confidence** (mức độ tin cậy availability) để không hứa realtime/zero overbooking; algorithms, thresholds và cadence chưa chốt. iCal 15 phút chỉ **WORKING MODEL**, không SLA.

## Authority

[Record External Commitment](../03-actor-authority/02-authority-capabilities.md) là capability explicit. Sale role/whitelist không đủ. Quyền ghi inventory không tự cấp mọi quyền Stay/Guest data hoặc finance. Operational actors chỉ dùng scope được giao; actual actor và authority source được audit.

## Domain Truth Changes

External Commerce giữ commercial lifecycle bên ngoài. Inventory giữ availability truth; Stay giữ actual/expected operational data; Destination Operations consume Stay truth; Reputation dùng qualifying evidence. Stayora Booking không mặc định sở hữu External Booking.

## Money Changes

**CONFIRMED:** External Stay representation hoặc completion tự nó không tạo Stayora/Sale/Affiliate commission và không tự vào Stayora Payment/Settlement. Chỉ thu external commercial economics khi cần cho một service được sử dụng rõ ràng; service/fee policy còn TBD. Không suy ra service đó đã triển khai hoặc free forever.

## Notifications

**TBD:** báo external record chưa đủ authority, conflict/sync issues, changes/cancellations và operational coordination cho ai, lúc nào, kênh nào. Operational need không mở toàn bộ external commerce data.

## Audit Events

Trace business source, actual Host actor/capability establishing the Fact and applicable commitment, resource/scope, evidence, conflict/changes, Stay participation và actual operations. Các policy actions giữ provenance. Data schema và evidence threshold **TBD**.

## Invariants

External commerce có thể tạo inventory/stay truth không cần Stayora Booking; confirmed sources có authority ngang nhau; record commitment cần explicit capability; không overwrite conflict; không unnecessary commercial disclosure; common operations không identical commercial liability; eligible external evidence có thể tạo Review Rights; không automatic commission; cancellation/no-show không invent financial consequences.

## Open Questions

Grant/revoke policy, minimum evidence, creation timing, conflict resolution, sync health/confidence và external service economics: **TBD**. Nguồn: [Foundation Marketplace](../01-product-foundation/05-marketplace-model.md), [Domain Glossary](../02-domain/01-domain-glossary.md), [Authority questions](../03-actor-authority/07-open-authority-questions.md), [Workflow questions](08-open-workflow-questions.md).
