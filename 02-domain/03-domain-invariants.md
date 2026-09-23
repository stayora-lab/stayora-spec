# Domain Invariants — Stayora

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**

Các invariant dưới đây là business rules ở mức conceptual. Chúng chưa phải technical enum, state machine, API validation hay database constraint.

## 1. Truth và boundary

1. **Property ≠ Inventory.** Property định nghĩa accommodation; Inventory định nghĩa availability theo thời gian.
2. **Bookable Unit ≠ necessarily Property.** Một villa có thể là một Bookable Unit; hotel có thể có nhiều Bookable Unit.
3. **One Bookable-Unit-time interval has one Inventory Truth** bất kể source là Stayora, OTA, Owner Direct, Sale/Zalo, block hay maintenance.
4. **Marketplace Projection ≠ Source of Truth.** Marketplace hiển thị/composes; domain authoritative giữ dữ liệu gốc.
5. **Destination ≠ Location/filter.** Destination là first-class business domain có context và operational boundary.

## 2. Commercial và operational truth

6. **Booking ≠ Stay.** Booking là commercial commitment; Stay là operational lifecycle. A Stay may exist without a Stayora Booking.
7. **Commercial Truth ≠ Operational Truth.** Booking có thể ghi 8 guests trong khi Staying Party thực tế có 7; không rewrite Booking history vì Stay data thay đổi.
8. **Booking ≠ Payment.** Booking giữ commitment/snapshot; Money giữ payment movement và allocation.
9. **Stay ≠ Settlement.** Stay completion là điều kiện/nguồn tham chiếu; Settlement là reconciliation và phân bổ money.
10. **Payment Received ≠ Settlement/Payout.** Tiền nhận, entitlement earned, settlement hoàn tất và Paid là các khái niệm riêng.
11. **Request không tạo exclusive Inventory Commitment.** Authorized acceptance có thể tạo Temporary Exclusive Inventory Commitment trong finite commitment/payment window; Payment Session / Attempt vẫn là Money truth. Duration và expiry policy chưa được định nghĩa.
12. **External confirmed booking có inventory authority ngang booking Stayora.** Không ưu tiên một source chỉ vì nó đi qua Stayora.

## 3. Identity, authority và distribution

13. **Identity Role ≠ Resource Authority.** Một người có nhiều role nhưng chỉ hành động trong authority/relationship/scope hợp lệ.
14. **Owner ≠ necessarily Primary Host ≠ necessarily Commercial Authority holder.** Không collapse ba khái niệm thành một owner field.
15. **Sale Platform Eligibility ≠ Host Trust.** Approved Sale chưa chắc được Owner whitelist; blacklist relationship không xóa Sale role globally.
16. **Whitelist không tự cấp mọi capability.** Effective Permission = Identity/Platform Eligibility + Distribution Relationship + Property Policy + Resource Authority.
17. **Blacklist overrides commercial access** trong authority scope của Owner / Authorized Host; chi tiết delegation và scope change thuộc checkpoint sau.
18. **Affiliate ≠ Sale.** Affiliate acquisition/referral và Sale conversion/relationship có thể cùng attribution một Booking nhưng vẫn là actor/capability riêng.

## 4. Trust, reputation và incident

19. **Identity Verification ≠ Stayora Verified.** Identity verification và platform eligibility thuộc Identity & Authority; Stayora Verified thuộc Verification và tập trung vào Property-supply quality.
20. **Verification ≠ Reputation.** Verification nói Stayora đã kiểm tra gì; Reputation nói lịch sử interaction/stay tích lũy gì.
21. **Incident không trực tiếp rewrite Verified hoặc Reputation.** Incident cung cấp evidence/signal; Verification và Reputation quyết định truth của mình theo policy sau này.
22. **Reputation attaches to responsible actor/component.** Lỗi villa, Butler, Sale hoặc destination service không tự đổ lên mọi thành phần.
23. **External Stay có thể tham gia reputation eligibility** khi có evidence đủ rằng stay diễn ra và completed; không cần tạo Stayora Booking giả.
24. **Stayora Verified ≠ Luxury.** Verified là Trust & Quality Assurance; không phải admission requirement cho marketplace mở và không đồng nghĩa Managed.

## 5. Money và pricing

25. **One Public Price** là giá khởi điểm chung của Direct Guest và Sale trong cùng Offer context.
26. **Sale-funded discount không được âm thầm giảm Owner entitlement.** Owner/Stayora/Affiliate/campaign-funded discount phải có attribution riêng.
27. **Sale base distribution commission = 10% Commissionable Booking Value.** Exact base definition và exception policy vẫn để Money/Commission Policy.
28. **Commission states are separate:** Pending sau confirmation có thể được ghi nhận; Completed Stay là normal Earned/settlement eligibility boundary; policy-driven exception economics có thể tồn tại cho commercially fulfilled nhưng physically unused commitment; Paid là settlement/payment state sau đó. Exact exception economics vẫn TBD.
29. **Guest Total Payment ≠ Commissionable Booking Value ≠ Stayora Revenue ≠ Owner Payout.** Không dùng một giá trị thay cho giá trị khác.

## 6. Destination và operations

30. **Core defines capabilities; Destination defines local policies/configuration; Integration connects local operations.**
31. **Destination Operations không sở hữu commercial economics.** QR/gate/cart/checkout workflows không tạo quyền xem Sale commission hoặc Owner payout.
32. **Need-to-know access.** Financial và Guest data được scope theo role + relationship + resource + lifecycle; accountless QR không mặc định mở full booking/PII.

## 7. Inventory và payment refinements — confirmed current decision

33. **Inventory Availability** là derived truth từ effective Inventory Commitments trên Bookable Unit + time range; không là persisted lifecycle enum đã đóng.
34. **Inventory Commitment** gồm Temporary Exclusive Commitment, Confirmed Accommodation Commitment và Availability Block. Request, Lead, Offer và Stay không phải Inventory Commitments.
35. **Inventory Release requires authoritative end** của applicable Inventory Commitment. Physical absence, late arrival, lack of Check-in hoặc No-show observation không tự release Inventory khi accommodation right còn hiệu lực.
36. **Physical absence ≠ Inventory Release.**
37. **Payment Session / Attempt ≠ Temporary Inventory Commitment.** Hai domain truth có thể coordinated trong commitment window nhưng không hợp nhất.
38. **Required Payment Condition ≠ necessarily Fully Paid.** Booking Confirmation cần điều kiện áp dụng; không có universal payment percentage trong Stayora Core.
39. **Payment Default là một policy determination riêng.** Required Payment Condition là điều kiện payment cho một commercial action cụ thể, như Booking Confirmation. Payment Obligation là nghĩa vụ tài chính đến hạn theo commercial terms/schedule. Payment Default được xác định khi một Payment Obligation đến hạn vẫn chưa được thỏa mãn sau deadline và các điều kiện reconciliation/grace áp dụng; thời lượng grace và economics vẫn TBD. No-show là operational non-use/non-arrival và không tự terminate accommodation right, release Inventory, tạo Default hoặc tạo Stay COMPLETED.
40. **No-arrival observation ≠ Booking Cancellation.** Change, Cancellation, Payment Default và No-show/non-arrival là các concepts khác nhau.

## 7. Conceptual lead lifecycle

Lead và Lead Assignment là hai lifecycle khác nhau. Lead là demand opportunity; Lead Assignment là quan hệ xử lý giữa Lead và Sale. Sale ACCEPTED là Assignment truth, không phải Lead truth; accountability của Sale bắt đầu khi Assignment được accepted. Acceptance không cấp Property, Inventory hoặc Booking Authority. Lead lifecycle hiện chỉ là conceptual outcomes `OPEN`, `IN_PROGRESS`, `WON`, `LOST`, `CLOSED`; Assignment có thể có `OFFERED`, `ACCEPTED`, `DECLINED`, `EXPIRED`, `RELEASED`, `REASSIGNED`. Đây không phải một linear transition graph đã đóng; transition/dispatch policy còn TBD. Offer 5–10 seconds, 24-hour handling và optional +24-hour extension là WORKING MODEL / future Lead Policy, chưa phải committed SLA hoặc technical state machine.

## 8. Verification models — three separate concepts

Checkpoint 4 là canonical lifecycle definition. Không dùng một giant Verification state machine để gộp các model sau:

1. **Application / Assessment Case:** workflow của application, inspection, evidence, assessment, decision và remediation.
2. **Verification Status:** status set gồm `NOT_VERIFIED`, `VERIFIED`, `SUSPENDED`, `REMOVED`.
3. **Review Case:** case review có thể `OPEN` trong khi Verification Status vẫn `VERIFIED`; `REVIEW REQUIRED` là review signal/case condition, không phải Verification Status.

Application, inspection, evidence và remediation không mặc nhiên là Verification states. `SUSPENDED ≠ REMOVED`; `REMOVED` không trực tiếp trở lại `VERIFIED` mà cần qualifying reassessment/new grant, có lưu lịch sử. Xem [Verification and Reputation models](../05-state-machines-policies/06-verification-and-reputation.md).
