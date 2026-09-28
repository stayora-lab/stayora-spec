# WF-06 — Completion → Settlement → Payout

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 11, 23–27.

## Mục đích và phạm vi

Ghi ranh giới từ operational completion tới economic eligibility, phân bổ và chi trả. Chỉ business money boundaries đã duyệt; không tax/accounting implementation hoặc fee configuration.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Purpose

**CONFIRMED:** việc kết thúc Stay mở eligibility cho economics phù hợp; không tự hoàn tất Settlement/Payout và không biến Guest money thành Stayora revenue.

## Actors

Actor có authority xác nhận operational completion (exact assignment **TBD**); actor có Settlement authority; actor có Payout authority; economic beneficiaries; Distribution cung cấp attribution/entitlement basis. Primary Host không tự là beneficiary hoặc có mọi financial capability.

## Preconditions

Actual Checkout đã được ghi, completion readiness được xét. Chỉ eligible economics thuộc phạm vi Money/service liên quan đi vào settlement; external representation/completion không tự đủ điều kiện. Completion và finance authority tách biệt.

## Trigger

Stay được đánh giá completion readiness sau actual Checkout; khi thực sự Completed thì economics đủ điều kiện có thể trở thành earned/settlement-ready.

## Happy Path — CONFIRMED conceptual flow

```text
CHECKED OUT → Completion readiness → STAY COMPLETED
→ eligible economics become earned/settlement-ready
→ Reconciliation → Settlement → Payout
```

1. Stay xác định Operational Completion Readiness mà không đánh đồng Checkout với Completed; exact exceptions còn TBD. Bước này không tính final economic positions.
2. Stay ghi Completed theo authority/conditions hợp lệ. Đây là normal trigger cho eligible economics Earned/settlement-ready, không nhất thiết là path economic duy nhất.
3. Money reconciliation đối chiếu economic positions liên quan.
4. Settlement xác định final economic positions.
5. Payout thực thi một settled payable; chưa thể coi đã Paid chỉ vì Settlement đã xong.

Financial Reconciliation trong sơ đồ này thuộc Money và là normal step sau STAY COMPLETED; policy-driven exception eligibility có thể cho phép reconciliation/settlement khi commitment đã commercially fulfilled nhưng không có physical Stay. Nó xác định final economic positions từ eligible entitlements, discounts, refunds, adjustments, applicable costs/policies, funding attribution và beneficiary attribution. Đây không là Stay state.

## Alternative Paths

External Stay completion có thể tạo eligible Review Rights nhưng không tự đi vào Stayora Settlement. Economics của service sử dụng rõ ràng cần policy riêng; không tạo commission vì shared operations.

Security/Damage Deposit giữ lifecycle/economics riêng, không là commission base. Add-ons giữ economics riêng trừ khi có policy rõ; checkpoint này không tạo policy gộp mới.

## Failure Paths

**TBD:** qualifying completion blockers, unresolved disputes, partial settlement, cancellation/no-show/early departure, refund/chargeback, Payment Default, payout failure/retry và timelines. Fully paid/commercially fulfilled nhưng không có physical Stay có thể cần exception settlement eligibility; không bao giờ biến NO_SHOW thành STAY COMPLETED để unlock Settlement.

## Authority

Completion authority không tự cấp financial visibility, Settlement authority hay Payout authority. Primary Host không mặc nhiên là Owner entitlement beneficiary/settlement beneficiary/payout recipient. Finance staff cần function/domain/resource authority; Distribution không giữ Money ledger. [Financial capabilities](../03-actor-authority/02-authority-capabilities.md) và [Effective Permission](../03-actor-authority/05-effective-permission.md) áp dụng.

## Domain Truth Changes

**CONFIRMED:** Stay giữ operational completion; Distribution giữ attribution/entitlement basis; Money giữ financial ledger/execution, reconciliation, Settlement và Payout. Completed là normal economic eligibility boundary, không phải exclusive path nếu policy định nghĩa exception. Reputation có thể tạo eligible Review Rights; Verification có thể consume signals. Mỗi domain có downstream rule/lifecycle riêng.

## Money Changes — CONFIRMED boundaries

```text
Payment Received ≠ Booking Confirmed ≠ Stay Completed
≠ Financially Reconciled ≠ Settlement Completed ≠ Payout Completed

Earned ≠ Settled ≠ Paid
```

Booking Confirmed tạo expected/pending economics; Completed Stay là normal trigger cho eligible Earned/settlement-ready economics, nhưng policy-driven exception paths có thể tồn tại cho commercially fulfilled/fully paid commitment không dùng Stay. Guest money collected không tự là Stayora revenue. Sale base commission = 10% Commissionable Booking Value; định nghĩa base **TBD**.

Discount/refund/adjustment giữ **amount + beneficiary + funding source**. Sale không unilaterally giảm Owner entitlement. Exact Affiliate/Sale split, Stayora fee và performance incentive vẫn **WORKING MODEL/TBD**; không nhập ~3%/~5%/~2% thành final rates. Tax treatment, accounting recognition, invoice/withholding và quyền giữ/chi tiền **TBD · legal-validation-required**.

## Notifications

**TBD:** notification về completion/earned/settlement/payout, người nhận, timing/channel. Economic visibility chỉ đủ cho own entitlement/financial authority phù hợp; không cùng một statement finance cho mọi actor trong Stay.

## Audit Events

Trace completion evidence/actor/authority, eligibility basis, attribution, adjustments với amount/beneficiary/funding, reconciliation, Settlement determination và Payout outcome. Human actions giữ actual actor/capacity/source/reason/resource/time; policy actions auditable. Đây không là ledger schema hay event definition.

## Invariants

Checkout không tự Completed; Completed không tự Financially Reconciled; Financially Reconciled không tự Settled; Settlement không Payout; collected money không revenue; pending không Earned; Earned không Paid; financial authority khác hosting authority; Distribution basis khác Money execution; deposit/add-ons riêng; external completion không automatic settlement; No-show không tự Completed; Payment Default không tự No-show; physical absence không tự release Inventory.

## Resolution note

**CONFIRMED — WQ-15 resolved:** Operational Completion Readiness belongs to Stay. Financial Reconciliation belongs to Money. The normal path occurs after STAY COMPLETED; policy-driven Economic Eligibility may open an exception path without falsifying Stay as Completed. The unresolved questions remain Commissionable Booking Value, fees/splits, partial settlement, disputes and legal/accounting. Nguồn: [Foundation Money](../01-product-foundation/09-money-model.md), [ADR-P021](../00-start-here/DECISIONS.md#adr-p021), [Domain Invariants](../02-domain/03-domain-invariants.md), [WF-04](04-stay-lifecycle.md), [WF-05](05-incident-resolution.md).

## V0 Primary-transfer payout recipient

**Status: CONFIRMED per [ADR-P076](../00-start-here/DECISIONS.md#adr-p076).** This is a narrow recipient-handling rule, not a change to Financial Beneficiary, entitlement determination, Settlement eligibility or financial execution authority. Owner ≠ Primary Host ≠ Financial Beneficiary ≠ payout recipient.

Founder-confirmed: absent a valid retained-payout override, payout handling follows the Primary effective for the unit when the Stay actually checks in / commences, using canonical Stay/check-in event semantics. Booking-created-at, payment-received-at, earliest timestamp, midnight and calendar/timezone snapshots do not replace that event.

The transfer cohort contains only bookings CONFIRMED before the Primary transfer becomes EFFECTIVE with Stay/check-in after effectiveness; confirmations between designation and acceptance/effectiveness qualify when both conditions hold. Completed/already checked-in stays, cancelled bookings, future requests and unrelated Money records are excluded. Subject to the successive-transfer attribution limit below, ONE choice governs the WHOLE applicable cohort, not separate choices per booking. Record it while transfer is PENDING; it becomes binding at effectiveness and cannot be edited retrospectively through that transfer. RETAIN records an outgoing-actor/cohort payout override. FOLLOW INCOMING uses the default role-based actual-check-in/commencement rule, not a permanent lock to the named incoming person. The recorded choice governs manual handling, not Financial Beneficiary or general Financial Authority; no per-booking payout editor is created. No selection uses the default only where no valid retained override exists, without a new pending state.

Earlier valid actor/cohort-specific payout overrides are not silently overwritten by successive Primary changes; silence never cancels them. A later outgoing Primary may choose only for the applicable cohort whose current payout direction is attributable to that actor, and cannot redirect another actor's retained payout. For purposes of the next transfer, a booking with NO existing retained-payout override is attributable to the CURRENT Primary under the default policy, even if it was originally confirmed under an earlier Primary. Preserve decision provenance/audit. P0 retains B during P0→P1: later P1→P2 leaves B payable under P0's override; P1 cannot redirect B to P1 or P2. C with no override is attributable to P1 during P1→P2; P1 may choose RETAIN for the applicable C/cohort or leave the default. If C has no retained override at actual check-in/commencement, payout follows the then-effective Primary.

V0 payout remains MANUAL-ASSISTED. Stayora records the applicable payout recipient for that process; parties may arrange privately outside Stayora. Transfer does not automate fund movement, processor behavior, Settlement execution or deductions, or rewrite historical payments, executed payouts, Settlement facts or beneficiary records. Unrelated Money/Settlement TBDs remain open.
