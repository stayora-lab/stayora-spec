# Danh mục tác nhân — Actor Catalog

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 6–16.

## Mục đích và phạm vi

Mô tả vai trò, relationship và giới hạn của từng actor. Danh mục không tự cấp capability; một Identity có thể xuất hiện ở nhiều hàng.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Actors và authority — CONFIRMED trừ phần ghi TBD

| Actor | Nguồn / relationship | Capability và visibility theo context | Không mặc nhiên có |
|---|---|---|---|
| Legal Owner | Quyền sở hữu tài sản; chứng cứ/quyền khai thác chi tiết TBD | Quyền trên Stayora phải được xác lập qua authority hợp lệ | Primary Host authority, mọi dữ liệu Guest, toàn bộ quyền finance |
| Primary Host | Một authority anchor/Property tại một thời điểm; nguồn chính đáng | Hosting/commercial responsibility và delegation trong authority có thật | Financial Beneficiary, người nhận Payout hoặc mọi quyền Settlement |
| Co-host | Delegated relationship từ authority hợp lệ | Chỉ capability/resource/lifecycle được ủy quyền rõ | Fixed permission bundle, mọi finance, delegation không giới hạn |
| Sale | Platform approval/eligibility và Distribution Relationship | Search, availability liên quan, Offer, Request Booking, Lead; Instant Book khi đủ điều kiện; economics của mình; accountable commercial context được ghi nhận theo policy | Chặn Inventory, accept thay Host, Owner payout/ledger, economics Sale khác |
| Butler | Platform approval và assignment | Arrival/departure liên quan, chuẩn bị villa, assert Ready, Check-in/out coordination, operational events, Incident/damage reports | Booking acceptance, sửa Public Price, quản lý Sale, finance/Settlement |
| Guest | Booking relationship và/hoặc Stay relationship | Booking/Stay capabilities có scope/lifecycle; participant được nhận diện có thể dùng confirmation/link/QR không full account | Authority chỉ từ việc cầm QR; mọi người trong nhóm có quyền của Payer/Creator |
| Affiliate | Attributable demand; onboarding approval TBD | Attribution và own economics cần thiết | Inventory/Booking/negotiation authority, Guest operations hoặc Host finance |
| Destination Staff | Identity → Destination Staff Relationship → Destination → function/capability | Security, Guest Services, Operations, Coordinator, Destination Admin trong scope được giao | Global BQL authority, Booking economics chỉ vì cần dữ liệu cổng |
| Stayora Staff / Platform | Human function/domain/resource authority hoặc Platform Policy Enforcement có căn cứ | Support, Trust & Safety, Verification Operations, Finance Operations, Destination Operations, Sale Operations, Platform Administration theo scope | “STAYORA_ADMIN = all business authority”, silent impersonation hoặc Property Commercial Authority do platform restriction |

## Onboarding và assignment — CONFIRMED

Guest/Host self-onboard; publish/compliance vẫn có điều kiện riêng. Sale/Butler apply và được duyệt. Butler approval không phải tuyển dụng vào Stayora; Butler không tự là staff. Một Butler có thể phục vụ nhiều Property, một Property có nhiều Butler. Oceanami max-two-Butlers là Destination-specific, không là global invariant.

Không có Butler không xóa operational responsibility của Host. Assignment và Stay Access cần được phân biệt, nhất là khi thay người hoặc thay ca; propagation chi tiết còn TBD.

## Staff và platform — CONFIRMED

Human Authority được phân theo chức năng, domain và resource. Staff làm privileged action phải bảo toàn actual actor, acting capacity, authority source, reason/policy, resource và time. Agency/delegation để hành động thay Host chỉ có thể dựa trên relationship chính đáng; cơ chế tương lai chưa được quyết định.

Platform Policy Enforcement gồm các ví dụ đã duyệt: Sale suspension, Property compliance restriction, Verified lifecycle enforcement, Temporary Inventory Commitment expiry và Review Right generation. Policy actions phải auditable và do domain tương ứng sở hữu. Platform hạn chế eligibility/capability không đồng nghĩa platform nhận Commercial Authority của Property.

## Sale accountability and reputation boundaries

Stayora may record verified Sale behavior/history as downstream evidence: speculative booking behavior, repeated Payment Default attributable to the Sale context, lead handling, completed transactions, and Host relationship history. Consequences belong to the relevant Reputation, Distribution Relationship, or Platform Eligibility policy; a failed transaction alone is not universal misconduct, and no universal Sale score is created by this amendment. Guest Reviews, Verified Transaction History, Commercial Reliability, Lead Performance, Host Relationship History, and Platform Policy History remain distinct signals; visibility, weighting, retention, and appeal are TBD. The T-24h Commercial Commitment Checkpoint is a commitment/payment policy boundary, not by itself an anti-Sale control.

## TBD và nguồn

Exact staff grants, Affiliate approval, Guest identity linkage/QR lifecycle và Butler assignment change nằm tại [Open Authority Questions](07-open-authority-questions.md). Tham chiếu [Foundation Actors](../01-product-foundation/06-ecosystem-and-actors.md), [Destination](../01-product-foundation/07-destination-model.md), [Domain Ownership](../02-domain/02-domain-ownership.md), [Actor–Resource Matrix](03-actor-resource-matrix.md) và [Stay Lifecycle](../04-core-workflows/04-stay-lifecycle.md).
