# Bất biến xuyên workflow — Cross-workflow Invariants

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 18–27, 29.

## Mục đích và phạm vi

Tập hợp các business boundaries phải tồn tại xuyên suốt sáu workflow. Giữ domain ownership và eligibility; không đóng policy/implementation gaps.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Authority — CONFIRMED

Role ≠ Permission; mọi privileged action cần valid authority context. Owner ≠ Primary Host; Primary Host ≠ automatic Financial Beneficiary. Booking Creator ≠ Payer ≠ Lead Guest ≠ Staying Party. Administrative Access không cấp quyền silent impersonation. Whitelist không là Instant Book permission bundle và không là Record External Commitment authority. [Authority invariants](../03-actor-authority/06-authority-invariants.md) là bảng đầy đủ.

## Inventory và commerce — CONFIRMED

- Property ≠ Bookable Unit; Inventory Truth thuộc Bookable Unit × Time, không thuộc từng channel riêng.
- Request ≠ Inventory Commitment. Request không reserve Inventory; authorized acceptance có thể tạo Temporary Inventory Commitment hữu hạn, còn Payment Session/Attempt thuộc Money.
- Inventory Availability là derived truth từ các Inventory Commitment có hiệu lực theo Bookable Unit × Time; không coi AVAILABLE/HELD/BOOKED/BLOCKED là requirement về persistence.
- Mọi release/recompute cần authoritative end/expiry/cancellation/override; physical absence tự nó không release Inventory.
- Inventory được revalidate tại commitment; Instant Book kiểm tra ngay trước commitment.
- Confirmed competing commitments làm incompatible pending Requests mất availability; không chọn thắng giữa hai conflicting confirmed sources khi policy chưa có.
- Demand access không tạo Inventory Authority; Sale không block để giữ cơ hội hoặc giữ long hold tùy ý.
- Instant Book là Host pre-authorization qua policy, cần transaction-time eligibility, explicit consent, Required Payment Condition và các Booking Confirmation Conditions khác; điều đó không mặc định là 100% payment.
- External confirmed commitment hợp lệ có availability authority ngang Stayora confirmed; không overwrite incompatible truth.
- External Booking là external concept được Inventory/Stay reference; External Stay không cần Stayora Booking/Payment/Settlement.

## Stay và consequences — CONFIRMED

- Booking ≠ Stay; expected commerce truth không overwrite actual Stay truth hoặc ngược lại.
- Stay lifecycle độc lập commerce source; shared operations không đồng nghĩa shared commercial liability.
- Ready là operational assertion, không zero-defect guarantee. Arrival/Access/Check-in khác nhau nơi destination cần.
- Expected checkout time không actual Checkout; Checkout ≠ Completed; Operational Completion Readiness thuộc Stay và không phải Financial Reconciliation.
- Incident ≠ Fault; Response ≠ Resolution; evidence không tạo financial/reputation authority.
- Guest Review ≠ Operational Performance Signal; attribution responsibility có thể theo dimension.
- Incident không trực tiếp sửa Reputation/Verified; Money thực thi financial consequences, giữ amount/beneficiary/funding.
- Chỉ qualifying unresolved exceptions block completion; danh sách còn TBD. No-arrival không tự là cancellation, Payment Default hoặc Completed; Payment Default không đồng nghĩa No-show.
- Completed là normal eligibility boundary, không tự hoàn tất downstream lifecycle. Policy-driven exception economics có thể tồn tại cho commitment đã commercially fulfilled/đủ điều kiện nhưng không có physical Stay; không giả tạo STAY COMPLETED để mở Settlement. External evidence đủ có thể tạo Review Rights; không automatic commission.

## Money — CONFIRMED

One Public Price cho Direct Guest/Sale cùng context. Sale-funded discount không tự giảm Owner entitlement. Sale base = 10% Commissionable Booking Value; base vẫn TBD. Payment Received ≠ Booking Confirmed ≠ Stay Completed ≠ Financially Reconciled ≠ Settlement Completed ≠ Payout Completed. Required Payment Condition ≠ Fully Paid. CHECKED OUT ≠ STAY COMPLETED ≠ FINANCIALLY RECONCILED ≠ SETTLED ≠ PAID. Earned ≠ Settled ≠ Paid. Guest collection không tự Stayora revenue. Security/Damage Deposit và Booking Deposit có lifecycle/economics riêng. External Stay completion không tự vào Stayora Settlement.

## Một domain không trở thành nguồn truth thứ hai — CONFIRMED

| Domain consume | Không được sở hữu thay |
|---|---|
| Booking | Actual Stay truth |
| Stay | Payment ledger |
| Incident | Financial adjustments execution/ledger |
| Reputation | Incident truth |
| Verification | Identity verification |
| Marketplace | Inventory Truth |
| Distribution | Money ledger |

Identity Verification ≠ Stayora Verified. Core capability, Destination policy/configuration và Integration nối local operations là các lớp khác nhau; không global hóa Oceanami rules.

## Status guard

**TBD:** authority precedence, Temporary Inventory Commitment window, Record External Commitment grants, blockers, Incident taxonomy, Commissionable Booking Value, refund/deposit mechanics, Payment Default/no-show economics và implementation. **WORKING MODEL:** Lead timings, Affiliate split/fee/incentive baselines. **TBD · legal-validation-required:** legal/tax/accounting/rails/privacy. Không đưa các mục đó vào invariants như final values.

Nguồn: [Foundation principles](../01-product-foundation/04-product-principles.md), [Domain invariants](../02-domain/03-domain-invariants.md). Liên quan: [Workflow map](00-workflow-map.md), [Open workflow questions](08-open-workflow-questions.md).
