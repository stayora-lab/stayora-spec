# Open Questions và Founder Review

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

Phụ thuộc: [ADR-P038](../00-start-here/DECISIONS.md#adr-p038), [ADR-P041](../00-start-here/DECISIONS.md#adr-p041), [ADR-P042](../00-start-here/DECISIONS.md#adr-p042), [ADR-P043](../00-start-here/DECISIONS.md#adr-p043), [ADR-P048](../00-start-here/DECISIONS.md#adr-p048), [ADR-P049](../00-start-here/DECISIONS.md#adr-p049)

## Cách sử dụng

Các câu hỏi này ghi nhận điểm chưa chốt; executor không trả lời thay founder. Cột “bên cần tham gia” là đề nghị routing review, không khẳng định các cá nhân/đối tác đã nhận việc. Deadline sản phẩm chưa được đặt.

Các policy TBD không ngăn bàn giao Foundation draft. Những ambiguity về status/hướng sản phẩm cần được thấy rõ khi founder review; legal/TBD phải được giải trước hành động triển khai phụ thuộc, không phải bằng cách gắn nhãn CONFIRMED trong docs.

## Ưu tiên founder review bản này

1. Q-01: One Public Price đã chốt; còn discount funding/limits/stacking.
2. Q-02: Commissionable Booking Value và exception treatment của 10% Sale.
3. Q-10: timing lead từng có số cụ thể nhưng chưa phải policy freeze.
4. Q-11: Affiliate approval model chưa được chốt; không tự miễn duyệt.
5. Q-09: Domain/Actor Authority chi tiết dưới Owner/Authorized Host scope.

Các con số fees/KPI, checklist Verified và legal claims còn giữ nguyên trạng thái chưa final. Founder có thể review fidelity trước, rồi lựa chọn câu nào chốt và câu nào tiếp tục mở.

## Question register

<a id="q-01"></a>
### Q-01 — One Public Price discount policy

**Status:** TBD  
**Liên quan:** C-03 / ADR-P041  
**Bên cần tham gia:** Founder

One Public Price đã chốt. Cần quyết định discount limits, stacking, attribution và cách phân biệt Sale-funded với Owner/Stayora/Affiliate/campaign-funded discounts. Direct Instant Book discount 10% không được tự khôi phục nếu chưa có quyết định mới.

**Dependency:** Trước Pricing Policy và quote engine.

<a id="q-02"></a>
### Q-02 — Commissionable Booking Value và Sale exceptions

**Status:** PARTIALLY REFINED — TBD remainder  
**Liên quan:** C-04 / ADR-P038  
**Bên cần tham gia:** Founder + financial modelling

10% đã CONFIRMED là base distribution commission trên Commissionable Booking Value. Checkpoint 4 now confirms the abstraction and preserves Pending → Earned / NOT_EARNED → Paid semantics, but the definition's exact calculation, cancellation/refund/no-show treatment and exception economics remain TBD.

**Dependency:** Trước commission policy; không cần hard-code để review Foundation.

<a id="q-03"></a>
### Q-03 — Affiliate/incentive/platform economics

**Status:** TBD  
**Liên quan:** C-05/C-06 / ADR-P039–040  
**Bên cần tham gia:** Founder + financial modelling

A%, shared split, ~2%/~5%, ai chịu phí, self-service economics, incentive qualification và campaign allocation?

**Dependency:** Trước financial model final và settlement rules.

<a id="q-04"></a>
### Q-04 — Legal entity và supplier/intermediary

**Status:** TBD · legal-validation-required  
**Liên quan:** C-17 / ADR-P036/048  
**Bên cần tham gia:** Founder cùng chuyên gia phù hợp, chưa được chỉ định

Pháp nhân/hợp đồng và substance của mỗi bên; điều kiện marketplace/compliance?

**Dependency:** Trước đăng ký và hợp đồng/launch phụ thuộc.

<a id="q-05"></a>
### Q-05 — Collection/payment confirmation

**Status:** TBD · legal-validation-required  
**Liên quan:** C-02 / ADR-P037/048  
**Bên cần tham gia:** Product + payment partner + legal, chưa được chỉ định

Provider/rails, người nhận và quyền giữ/chi tiền; thủ công hay tự động xác minh; late/partial/overpayment, refund rail?

**Dependency:** Trước payment policy/implementation.

<a id="q-06"></a>
### Q-06 — Accounting/tax/invoice

**Status:** TBD · legal-validation-required  
**Liên quan:** C-17 / ADR-P048  
**Bên cần tham gia:** Chuyên gia kế toán/thuế cùng founder

Gross/net revenue, từng loại Owner, withholding, tax base, invoices/chứng từ Sale/Affiliate; không áp 7% mặc định?

**Dependency:** Trước định nghĩa ledger/tax rules cuối.

<a id="q-07"></a>
### Q-07 — Host và property onboarding

**Status:** TBD  
**Liên quan:** ADR-P007/009  
**Bên cần tham gia:** Founder/Product; legal validation phần compliance

Chứng cứ quyền khai thác, điều kiện publish, đồng sở hữu, transfer Primary Host và tranh chấp?

**Dependency:** Trước Domain/Authority chi tiết.

<a id="q-08"></a>
### Q-08 — Co-host và sensitive authority

**Status:** TBD  
**Liên quan:** C-07 / ADR-P009/010/027  
**Bên cần tham gia:** Founder/Product

Granular permissions, finance access, payout/tax identity, revoke và chuyển quyền thế nào?

**Dependency:** Trước permission matrix.

<a id="q-09"></a>
### Q-09 — Sale relationship scope

**Status:** TBD  
**Liên quan:** C-19 / ADR-P012/018  
**Bên cần tham gia:** Founder/Product

Relationship đã CONFIRMED giữa Sale ↔ Owner / Authorized Host trên commercial authority scope. Cần đặc tả Domain/Actor Authority về delegation, thay đổi Host, offboarding và effective permission; không thiết kế database/RBAC trong Foundation.

**Dependency:** Trước Sale authority/Instant Book policy.

<a id="q-10"></a>
### Q-10 — Lead timings/algorithm

**Status:** TBD  
**Liên quan:** C-09 / ADR-P033/042  
**Bên cần tham gia:** Founder/Product

Giữ 24h/+24h như rule hay working? Chọn offer window; tier/rating weights; extension và exception authority?

**Dependency:** Trước Lead Policy/SLA.

<a id="q-11"></a>
### Q-11 — Affiliate onboarding/attribution

**Status:** TBD  
**Liên quan:** C-12 / ADR-P032/043  
**Bên cần tham gia:** Founder/Product

Approval hay automated activation; attribution window, self-referral, duplicate/repeat guest, fraud và tranh chấp?

**Dependency:** Trước Affiliate workflows.

<a id="q-12"></a>
### Q-12 — Hold và inventory concurrency

**Status:** TBD  
**Liên quan:** C-08 / ADR-P014/015  
**Bên cần tham gia:** Product; founder quyết các business trade-offs

Temporary Inventory Commitment window, concurrent accept, late successful payment, provider UNKNOWN/reconciliation, hai external/platform confirmed, override và reopen?

**Dependency:** Trước booking/inventory state machines.

<a id="q-13"></a>
### Q-13 — iCal/sync và confidence

**Status:** TBD  
**Liên quan:** ADR-P015/047  
**Bên cần tham gia:** Product/integration

Cadence 15 phút có giữ không; staleness, failure, timezone, manual blocks, API capabilities và confidence V0?

**Dependency:** Trước integration/SLA.

<a id="q-14"></a>
### Q-14 — Instant Book cancellation/remedy

**Status:** TBD · legal-validation-required  
**Liên quan:** C-14 / ADR-P019  
**Bên cần tham gia:** Founder/Product + legal

Exact wording, consent, change/cancel/refund, supplier failure và quyền remediation?

**Dependency:** Trước Terms và payment consent.

<a id="q-15"></a>
### Q-15 — Completion/settlement exceptions

**Status:** PARTIALLY REFINED — TBD remainder  
**Liên quan:** C-20 / ADR-P020/021  
**Bên cần tham gia:** Founder/Product + finance

Checkpoint 4 confirms Operational Completion Readiness belongs to Stay, normal Financial Reconciliation follows STAY COMPLETED, and policy-driven exception Economic Eligibility may proceed without falsifying Completed. Who confirms completion, reconciliation/SLA, incident hold, cancellation/no-show/partial-stay entitlement and chargeback remains TBD.

**Dependency:** Trước money/state policies.

<a id="q-16"></a>
### Q-16 — Security deposit và add-ons

**Status:** TBD  
**Liên quan:** ADR-P022  
**Bên cần tham gia:** Founder/Product + legal phần hợp đồng

Amount, collection/refund/claim/evidence; add-on supplier, commission, invoice và settlement riêng?

**Dependency:** Trước các policy tiền phụ thuộc.

<a id="q-17"></a>
### Q-17 — Verified standard/lifecycle

**Status:** TBD  
**Liên quan:** ADR-P002/044  
**Bên cần tham gia:** Founder/Product + operations

Duyệt sáu nhóm checklist? Ai kiểm, evidence, interval, fee, suspend/remove/appeal và phạm vi support?

**Dependency:** Trước Verified spec.

<a id="q-18"></a>
### Q-18 — Reputation/evidence

**Status:** TBD  
**Liên quan:** ADR-P025/026/044  
**Bên cần tham gia:** Founder/Product

Review rights từng actor; external stay evidence; public/internal; weights, abuse, appeal, Guest linkage và retention?

**Dependency:** Trước Reputation Policy.

<a id="q-19"></a>
### Q-19 — Guest QR và privacy

**Status:** TBD · legal-validation-required  
**Liên quan:** C-11 / ADR-P027/034  
**Bên cần tham gia:** Product + privacy/legal

Field-level access, accountless token, expiry/revoke, gate QR riêng/chung, share/forward, access sau stay?

**Dependency:** Trước access/QR specification.

<a id="q-20"></a>
### Q-20 — Destination membership/policy

**Status:** TBD  
**Liên quan:** C-18 / ADR-P004/005/028  
**Bên cần tham gia:** Founder/Product

Geographic vs operational scope, independent property, staff onboarding, policy owner, precedence, nhiều destination?

**Dependency:** Trước Destination Domain.

<a id="q-21"></a>
### Q-21 — Oceanami partner/operations

**Status:** TBD  
**Liên quan:** C-18 / ADR-P028/029  
**Bên cần tham gia:** Founder và đối tác thực tế, chưa có cam kết trong nguồn

BQL agreement, guest registration, security/QR/offline, xe điện, access data và trách nhiệm support?

**Dependency:** Trước pilot vận hành thực tế.

<a id="q-22"></a>
### Q-22 — Pilot measurement/baseline

**Status:** TBD  
**Liên quan:** ADR-P030/045  
**Bên cần tham gia:** Founder/Product cùng data source owners

Định nghĩa actual/represented, denominator độc lập, dedupe/window, target và pilot cohort/date/budget?

**Dependency:** Trước báo KPI và chốt pass/fail.

<a id="q-23"></a>
### Q-23 — External fee/support

**Status:** TBD  
**Liên quan:** ADR-P016/046  
**Bên cần tham gia:** Founder

Miễn phí ban đầu bao lâu, tính phí thế nào, support boundary/threshold và economics external?

**Dependency:** Trước cam kết giá/support với users.

<a id="q-24"></a>
### Q-24 — V0 scope và founder review

**Status:** TBD  
**Liên quan:** ADR-P049 / SRC-00  
**Bên cần tham gia:** Founder

Phạm vi triển khai tối thiểu sau Foundation; chấp thuận/sửa ambiguity; khi nào và phiên bản nào được freeze?

**Dependency:** Review hiện tại; chưa tự bắt đầu checkpoint sau.

## Review outcome

**Artifact đã được Founder freeze ngày 2026-09-18; các câu hỏi nội dung vẫn mở.** Không có câu hỏi nào ở trên được đánh dấu đã giải chỉ vì bộ file đã hoàn thành. Mỗi câu trả lời tương lai phải cập nhật Decision register, contradiction audit và các chương liên quan; giữ decision cũ dưới SUPERSEDED nếu thật sự bị thay.

Xem [Decision register](../00-start-here/DECISIONS.md) và [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md).
