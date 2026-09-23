# WF-01 — Sale-assisted Request Booking

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 10–11, 18, 26–27.

## Mục đích và phạm vi

Ghi luồng Guest được Sale tư vấn tới Booking Confirmed và Stay chuẩn bị vận hành. Phân biệt Request, Temporary Inventory Commitment, Payment Session / Attempt và Required Payment Condition.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Purpose

**CONFIRMED:** hỗ trợ Sale chuyển demand thành booking hợp lệ mà không cho Sale giữ nguồn phòng chỉ để bảo toàn cơ hội bán.

## Actors

Guest, Sale, Primary Host / authorized Co-host; Butler và Destination Staff tham gia preparation theo assignment/scope. Booking Creator, Payer, Lead Guest và Staying Party có thể khác nhau. Staff hỗ trợ phải dùng legitimate authority và actual identity.

## Preconditions

**CONFIRMED:** Sale có platform eligibility, Distribution Relationship và transaction context phù hợp; Offer nêu Bookable Unit, dates/context, Public Price và conditions. Host/Co-host quyết định phải có Booking Authority. Availability trước đó không đảm bảo availability tại commitment.

## Trigger

Guest cần tư vấn hoặc Sale xử lý Lead/khách của mình, rồi tạo Request Booking theo Offer đã trao đổi. Lead attribution không tự tạo Inventory Authority.

## Happy Path — CONFIRMED

```text
Guest → Sale → Search / Compare → Offer → Request Booking
→ Host / Authorized Co-host Decision → Authorized Commitment Window
   ├─ Temporary Inventory Commitment — Inventory
   └─ Payment Session / Attempt — Money
→ Required Payment Condition satisfied
→ other applicable Booking Confirmation Conditions satisfied
→ BOOKING CONFIRMED → Stay Created / Scheduled
→ Butler / Destination preparation
```

1. Sale tìm/so sánh inventory và compose/present Offer. Direct Guest và Sale bắt đầu cùng One Public Price cho cùng villa-night/context.
2. Sale tạo Request; Inventory chưa reserve. Request là yêu cầu chờ quyết định, không là commitment giữ đêm.
3. Primary Host hoặc Co-host có authority accept/reject. Authorized acceptance có thể tạo Temporary Exclusive Inventory Commitment trong finite commitment/payment window; inventory được revalidate tại commitment.
4. Money thực hiện Payment Session / Attempt. Required Payment Condition và các Booking Confirmation Conditions áp dụng phải được thỏa mãn; Host acceptance đơn lẻ chưa tạo Booking Confirmed. Điều kiện này không mặc định 100% payment.
5. Booking Confirmed giữ commercial snapshot; tạo/schedule operational Stay truth riêng.
6. Butler/Destination preparation dùng dữ liệu theo assignment, relationship và operational need. Privileged decisions giữ actual actor và authority dùng.

## Alternative Paths

**CONFIRMED:** Sale có thể fund Guest discount từ economics của mình. Ví dụ minh họa đã duyệt: Public Price 10 triệu; Sale base entitlement 1 triệu; Sale-funded discount 0,3 triệu; Guest transaction price 9,7 triệu; expected Sale entitlement 0,7 triệu. Ví dụ không định nghĩa Commissionable Booking Value, không là universal pricing configuration và không quyết định Affiliate split.

**CONFIRMED:** actor đồng thời là Sale/Co-host có thể quyết định bằng delegated Booking Authority hợp lệ, audit acting capacity Co-host. Nhánh Instant Book đủ eligibility chuyển sang [WF-02](02-instant-book.md), không dùng whitelist để giả lập acceptance.

## Failure Paths

**CONFIRMED:** reject không tạo Temporary Inventory Commitment. Khi commitment window kết thúc, Inventory Availability được recompute từ effective commitments; không gọi đây là transition về AVAILABLE. Confirmed competing inventory commitment làm các pending Requests không tương thích mất hiệu lực về availability; Request không được thắng confirmed inventory.

**TBD:** exact cancellation/status notification, simultaneous accept, late/partial/overpayment, Payment Session/Attempt UNKNOWN hoặc conflict và remediation. Không tự chọn winner hoặc refund percentage. Sale không được block Inventory hay tạo long hold để giữ cơ hội.

## Authority

Dùng [Effective Permission](../03-actor-authority/05-effective-permission.md). Sale tạo Request trong context phù hợp; acceptance cần Host/Co-host authority; authority xác minh tiền tách biệt với authority accept. Ai/nguồn nào xác nhận payment cụ thể vẫn TBD. Không silent impersonation.

## Domain Truth Changes

| Domain | Truth liên quan — CONFIRMED boundary |
|---|---|
| Distribution | Lead/relationship/attribution, không giữ Inventory Truth hoặc payment ledger |
| Booking | Request, quyết định hợp lệ, commercial commitment/snapshot khi confirm |
| Inventory | Request không đổi thành exclusive commitment; authorized acceptance có thể tạo Temporary Exclusive Inventory Commitment; Availability được derive từ commitments |
| Money | Payment Session / Attempt và expected/pending economics, không tự xem là Earned/Paid |
| Stay | Operational Stay được tạo/schedule sau confirmation, không bản sao commercial lifecycle |
| Destination Operations | Preparation/coordination consume Stay truth |

## Money Changes

**CONFIRMED:** Sale base distribution commission = 10% của Commissionable Booking Value; base definition **TBD**. Booking Confirmed tạo expected/pending economics, chưa Earned/Settled/Paid. Sale-funded discount không giảm Owner entitlement nếu không có authority/funding mechanism riêng. Affiliate split, platform fee và incentive vẫn **WORKING MODEL**, exact values **TBD**; cancellation/refund percentages là **TBD — POLICY** theo [Money Model](../01-product-foundation/09-money-model.md).

## Notifications

**TBD — future-policy question:** người nhận/kênh/thời điểm cho Request decision, commitment window, payment/confirmation và preparation. Không có approved notification SLA trong nguồn. Bất kỳ disclosure nào phải theo relationship, lifecycle, operational need và authority/scope; exact fields, actors, timing, retention và masking vẫn TBD/policy. Không suy ra gửi toàn bộ Guest/financial data cho mọi actor.

## Audit Events

**CONFIRMED về traceability; danh mục dưới là mốc business, không event schema:** Request creator/acting capacity; acceptance/rejection và authority source; hold/payment evidence liên quan; material Offer/discount funding và commercial snapshot; Booking confirmation/Stay creation; privileged preparation actions. Audit privileged action giữ actor, acting capacity, source, reason/policy, resource, time. Exact evidence/retention policy vẫn TBD.

## Invariants

Request ≠ Inventory Commitment; Payment Session / Attempt ≠ Temporary Inventory Commitment; acceptance ≠ Booking Confirmation; Required Payment Condition không mặc định Fully Paid; Inventory được revalidate tại commitment; competing confirmed commitments invalidates incompatible pending Requests; Sale không trực tiếp block; Booking ≠ Stay; discount không âm thầm giảm Owner entitlement; Guest disclosure theo relationship/need; actual actor và authority luôn được giữ.

## Open Questions

Commitment window duration, payment evidence/late payment và competing commitments: **TBD**. Lead dispatch/SLA timings: **WORKING MODEL / future-policy question**, không dùng 5–10s/24h/+24h như SLA. Xem [Workflow questions](08-open-workflow-questions.md), [Foundation Marketplace](../01-product-foundation/05-marketplace-model.md), [Domain Invariants](../02-domain/03-domain-invariants.md), [WF-04](04-stay-lifecycle.md).
