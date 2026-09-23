# Open Domain Questions — Checkpoint 2

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**

Các câu hỏi dưới đây được giữ mở để không tự thiết kế domain. Câu hỏi nào đã có principle trong Foundation vẫn không được mở lại ở mức principle; chỉ phần boundary/detail chưa đủ rõ mới nằm ở đây.

## Money và Payment

1. `Money` nên giữ là một business area gồm Payment + Settlement hay sau này tách thành hai bounded contexts? Chưa tạo technical split.
2. `Commissionable Booking Value` gồm chính xác những khoản nào và xử lý discount, tax, add-on ra sao?
3. `Pending → Earned → Paid` của Sale commission và Affiliate entitlement liên kết với cancellation, refund, no-show, chargeback và completed Stay thế nào?
4. Facilitated collection 100% sẽ được biểu đạt qua provider, hợp đồng, invoice, revenue recognition và legal/tax treatment nào? Đây là `legal-validation-required / TBD`.

## Commercial Authority và Distribution

5. Khi Legal Owner, Primary Host, Authorized Host và delegated operator khác nhau, ai có thể tạo/sửa Distribution Relationship?
6. Commercial Authority scope thay đổi thế nào khi Primary Host đổi, Owner rút authority, Property offboard hoặc có tranh chấp?
7. Whitelist/Blacklist đã được xác định ở Owner/Authorized Host relationship scope; chi tiết propagation xuống từng Property/Bookable Unit và effective permission cần đặc tả ở Actor Authority checkpoint.
8. Affiliate approval, attribution window, fraud/self-referral và payout eligibility được định nghĩa thế nào? Không dùng self-apply → automated verification → ACTIVE làm mặc định.
9. Lead Management có tiếp tục là Distribution capability hay cần split sau khi workflow/volume rõ hơn?

## Property và Inventory

10. Một Property có thể có những cấu trúc Bookable Unit nào ngoài entire villa? Multi-unit, room, shared/partial unit và unit combination sẽ được mô hình hóa ở mức business nào?
11. “Time” của Inventory Truth là villa-night hay interval linh hoạt? Semantics của timezone, check-in/out, partial-day và overlapping interval chưa chốt.
12. Inventory xử lý hai confirmed sources, delayed iCal, manual block, maintenance block và conflict resolution thế nào? Không tự chọn winner rule.
13. Offer ownership và lifecycle thuộc Marketplace/Booking boundary ở mức nào? Không thiết kế aggregate hoặc price engine tại checkpoint này.

## Booking và Stay

14. Một Stay được tạo khi nào từ External Booking, và evidence tối thiểu nào cần trước khi coi là operational Stay?
15. Staying Party thay đổi so với Booking được ghi nhận ra sao mà không rewrite commercial truth?
16. Booking/Stay link cho split stay, move villa, extension, no-show, partial stay và duplicate external record thế nào?

## Destination và Destination Operations

17. Destination membership có một cấp hay nhiều cấp? Một Property có thể thuộc nhiều Destination/context không?
18. Ai sở hữu và thay đổi local configuration? Quyền ưu tiên giữa Core capability, Destination policy và integration constraint thế nào?
19. Oceanami BQL/security/QR/cart participation đã là partner commitment chưa? Quy trình offline, QR expiry/revocation và data scope chưa được quyết định trong Foundation.
20. Destination Operations có cần Incident capability riêng theo volume không, hay tiếp tục supporting capability gắn với Stay/Operations?

## Verification, Reputation và Incident

21. Verification Standard/version, inspection evidence, re-verification, suspension/removal và appeal được phân ranh giới thế nào?
22. Review Right cho Guest, Host, Butler và Sale cần evidence/relationship nào? External Stay review được chống duplicate/fraud ra sao?
23. Incident resolution authority thuộc ai trong từng loại issue? Incident signal đi vào Reputation/Verification theo policy nào mà vẫn giữ authority riêng?
24. Có cần một Incident & Resolution domain độc lập sau này không? Checkpoint 2 giữ nó là supporting capability.

## Domain shape và evolution

25. Distribution entitlement basis được Money tham chiếu thế nào mà không để Distribution sở hữu payment ledger?
26. Marketplace presentation cần cache/projection business nào ở mức conceptual, và làm sao bảo đảm không thành source of truth thứ hai?
27. Có cần top-level domain mới ngoài 12 domain đã duyệt không? Nếu có, phải ghi là proposal unresolved và được Founder/Product Architect review trước.

## Kết luận open questions

Không câu hỏi nào ở đây cho phép executor tự chọn schema, API, UI hoặc implementation. Các câu hỏi chỉ được đóng ở checkpoint sau khi có decision rõ; khi đó phải cập nhật Domain Map, Glossary, Ownership Matrix và Invariants đồng bộ.
