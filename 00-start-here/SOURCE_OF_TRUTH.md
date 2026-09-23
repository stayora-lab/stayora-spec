# Source of Truth và provenance

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

## Thứ tự authority

1. Yêu cầu/correction mới nhất của founder trong task hiện tại.
2. Quyết định rõ của founder trong discovery, đọc cùng câu hỏi và correction về sau.
3. Reconciliation và nội dung Product Architect/Editor đã tổng hợp, trong phạm vi được founder chấp nhận. Câu “tôi chốt” của assistant không tự tạo một quyết định của founder.
4. Checkpoint và bộ Foundation này là tài liệu dẫn xuất. Nếu tóm tắt sai, lời founder nguồn thắng; ghi discrepancy thay vì tự chọn cách hiểu.
5. Business/operations/Flexible Payment, Grok demo, Stayora 2.0 và các ví dụ từ nền tảng khác chỉ là reference. Một ý tưởng chỉ trở thành current decision khi được adopt rõ.

Quyết định mới chỉ thay quyết định cũ khi có đủ bằng chứng về cùng vấn đề. Assistant đề xuất khác hoặc founder nói “ok” với một hướng rộng không tự duyệt mọi tham số nằm trong phần trả lời kế tiếp. Trường hợp không chắc giữ hai vế trong [contradiction audit](DECISIONS.md#contradiction-audit), đặt câu hỏi TBD.

## Tình trạng gói tài liệu

**REOPENED FOR RECONCILIATION — 2026-09-18.** Founder đã xác nhận các principle trong artifact/phạm vi Foundation. Các mục có trạng thái WORKING MODEL, HYPOTHESIS, TBD, OUT OF SCOPE — V0 hoặc SUPERSEDED vẫn giữ nguyên trạng thái nội dung tương ứng; reconciliation không biến chúng thành requirement mới.

GPT-5.6 Sol giữ vai trò Product Architect/Editor theo phân công. Executor chuyển nội dung nguồn thành file, nối cross-links và kiểm tra artifact. Audit biên tập không có quyền thay quyết định founder. Không bắt đầu Domain/UX/implementation chỉ vì gói file đã được tạo.

Checkpoint 4 hiện được ghi tại [State Machines, Lifecycles & Policy Architecture](../05-state-machines-policies/README.md). Checkpoint 5 hiện được ghi tại [Oceanami V0 Scope](../06-v0-scope/README.md). Checkpoint 6 hiện được ghi tại [Information Architecture](../07-information-architecture/README.md). Checkpoint 7 gồm [Conceptual Data Model](../08-conceptual-data-model/README.md) và [supporting Persistence Architecture](../09-database-design/README.md). [CP8-A — UX Foundation](../10-ux-foundation/README.md), [CP8-B1 — Sale-assisted Booking](../10-ux-foundation/b1-sale-assisted-booking/README.md), [CP8-B2 — External Booking → Stay](../10-ux-foundation/b2-external-booking-to-stay/README.md), [CP8-B3 — Direct Guest Booking](../10-ux-foundation/b3-direct-guest-booking/README.md), [CP8-B4 — Stay Operations](../10-ux-foundation/b4-stay-operations/README.md), [CP8-B5 — Inventory Intervention](../10-ux-foundation/b5-inventory-intervention/README.md), [CP8-C1 — Onboarding Architecture](../10-ux-foundation/c1-onboarding-architecture/README.md), [CP8-C2 — Host/Owner + Property Onboarding](../10-ux-foundation/c2-host-owner-property-onboarding/README.md), [CP8-C3 — Sale Onboarding](../10-ux-foundation/c3-sale-onboarding/README.md) and [CP8-C4 — Butler Onboarding](../10-ux-foundation/c4-butler-onboarding/README.md) are accepted baselines; [CP8-D1](../10-ux-foundation/d1-workspace-surface-architecture/README.md), [CP8-D2](../10-ux-foundation/d2-task-screen-architecture/README.md), [CP8-D3](../10-ux-foundation/d3-screen-navigation-convergence/README.md), [CP8-E1](../11-detailed-interaction/e1-interaction-model-behavioral-conventions/README.md) and [CP8-E2](../11-detailed-interaction/e2-request-booking-interaction/README.md) are accepted baselines; CP8-E1 through E4 [Detailed Interaction](../11-detailed-interaction/README.md) are CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE; the [FD-01 → FD-19 reconciliation](../11-detailed-interaction/CP8-E-FOUNDER-DECISION-RECONCILIATION.md) and [batch report](../11-detailed-interaction/CP8-E-SOURCE-OF-TRUTH-BATCH-RECONCILIATION-REPORT.md) record the closure. [CP8-F1 Thin Design System Foundation](../10-ux-foundation/f1-thin-design-system-foundation/README.md) accepted; [CP8-F2 Prototype-Ready Design Language](../10-ux-foundation/f2-prototype-ready-design-language/README.md) accepted with four semantic presentation corrections; [CP8-F closure report](../10-ux-foundation/f2-prototype-ready-design-language/CP8-F2-FINAL-RECONCILIATION-CLOSURE-REPORT.md) records completion; CP8-G is in progress; v2 validation disposition is FAILED — ITERATION REQUIRED; CP8-H and implementation have not started. [CP8-G — Prototype & Validation](../12-prototype-validation/README.md) is the current validation artifact; Persistence direction thuộc CP7 Data Model; nó không phải checkpoint CP8 và không đóng unrelated policy TBDs.

## Nguồn đã truy xuất và giới hạn

- Cuộc trò chuyện **Phân tích website Stayora**, ID `6aabf341-8984-83ec-b4c1-2ba30b97cf5f`: lịch sử mới đã đọc qua các trang, gồm Câu 38 trở đi, Money Model, Foundations 1–7 và chỉ đạo handoff.
- Checkpoint `STAYORA_PRODUCT_DISCOVERY_CHECKPOINT_2026-09-18.md`: phần tổng hợp 1–29 và phụ lục 45 lượt trao đổi ban đầu. Câu 29–37 còn được founder dán lại trong SRC-10; các quyết định 30/70 trong checkpoint là lịch sử đã bị correction mới thay thế.
- Bản lưu business “Mô hình vận hành villa theo cụm”, Flexible Payment và HTML Lark “Bản đồ trực quan mô hình vận hành villa ký gửi” đã có trong source archive trước đó. HTML là bản render một phần có placeholder, không chứng minh đã đọc đủ tài liệu Lark gốc. Tài liệu vận hành theo cụm có các số giả định riêng; không nhập hub, fee, scorecard hoặc SOP vào current core.
- Bốn ảnh Oceanami được checkpoint cũ phân tích; gói này dùng lời founder và mô tả đã lưu làm bối cảnh, không kiểm chứng lại số liệu ảnh. “76 đánh giá” và các nhóm nguyên nhân không là KPI baseline.
- Không có toàn bộ Stayora 2.0 trong gói nguồn. Không fetch lại Grok để suy ra yêu cầu. Nội dung demo, trạng thái website hiện tại và khả năng triển khai không được xác nhận ở checkpoint này.
- Các khẳng định nghiên cứu luật/thuế/thị trường trong chat là phát biểu lịch sử, **chưa được xác minh cho gói này**. Không tái dùng citation nội bộ của chat làm bằng chứng legal. Mọi vấn đề pháp lý liên quan giữ `legal-validation-required / TBD`.

Định danh turn bên dưới cho phép tìm đúng lượt trong cuộc trò chuyện nguồn. Không coi thứ tự SRC là timeline tuyệt đối; trong mỗi mục đã ghi những turn liên quan và chiều correction.

## Sổ nguồn

<a id="src-00"></a>
### SRC-00 — Yêu cầu Checkpoint 1 hiện tại

Turn ID: `Yêu cầu trực tiếp trong task này`

Ràng buộc hiện hành, cấu trúc 18 file, statuses, không freeze, không tự quyết TBD.

<a id="src-01"></a>
### SRC-01 — Nguồn gốc Oceanami

Turn ID: `c8e5ad4e-bb8e-409f-ad02-df09102cbdb6; 8b5b7437-b3a1-4143-b525-c111f6e0cf3c; f16204a2-dac2-41b3-bdb5-2f82feb3a098`

Founder sở hữu hai villa; mô tả chi phí cố định, nguồn cung/vận hành phân mảnh và hiện trạng Zalo.

<a id="src-02"></a>
### SRC-02 — Marketplace mở và trách nhiệm

Turn ID: `215aa44b-0e6c-4746-ba48-751ade9d2191; 461db5cb-d432-414e-9121-feb0b7867201`

Không cấm Owner tự đăng/tự vận hành; review minh bạch và phân biệt trách nhiệm.

<a id="src-03"></a>
### SRC-03 — Sale là trọng tâm; discount từ commission

Turn ID: `011e96e2-1434-4581-be56-e609cc30a0e1; 065efc74-b4a3-4151-af09-be53e0ea2fd0`

Không loại Sale. Sale có thể tự giảm hoa hồng; không làm giảm phần Owner/Stayora.

<a id="src-04"></a>
### SRC-04 — Guest history, Butler và Verified ban đầu

Turn ID: `19bf4645-f200-4329-ae15-8933a3e34743; afe38beb-1c47-44a8-a6e3-b5131dbdfa0d; f339c9c8-5173-43f2-8a32-9f465b7c9e49; 246246d3-e66b-40bf-bba6-3515b01e8bc7`

Butler do Owner chọn; nhiều villa/nhiều Butler; Butler chịu trách nhiệm kết quả; đánh giá Guest nội bộ.

<a id="src-05"></a>
### SRC-05 — Inventory và operations Oceanami

Turn ID: `0ae2bc72-d238-4e7d-a3cf-0e10f6691fb2; 30f1686a-5430-42de-a479-7df2822f428d`

iCal dự kiến 15 phút; rủi ro độ trễ; QR, cổng, xe điện và lịch sử điều phối.

<a id="src-06"></a>
### SRC-06 — External stays và demand

Turn ID: `e62992f4-d142-406f-9766-bff9e194653c; 117036ed-7424-44fd-9bb7-0eebc98a8ff9; eb1037cb-8355-4377-851b-b058eb7c3809`

Dữ liệu external tối thiểu; không ép khai thương mại; miễn phí ban đầu/thu phí sau là ý định; marketing và affiliate.

<a id="src-07"></a>
### SRC-07 — Tạm bỏ giá sàn

Turn ID: `145d829d-5585-4a5c-9158-06288cdde910; 74751038-765b-4b0a-b3e8-0d82b835ca9a; 6efc400b-1458-45af-976c-bedfde58d9cb`

Chuỗi correction: floor bắt buộc → đề nghị do BDD/cư dân, không BQL → tạm bỏ giá sàn.

<a id="src-08"></a>
### SRC-08 — Managed lịch sử

Turn ID: `aa5f9c35-32fd-42e1-91dd-ae69cb1a756c; 8f888b1c-ec16-4f51-9e1f-6acc92424882; 76494a3c-52e5-4d63-ab8f-05a7e3316a5a`

10% per booking Managed; Owner duyệt tài sản; chỉ lưu lịch sử, không đưa sang marketplace core.

<a id="src-09"></a>
### SRC-09 — Grok và Stayora 2.0

Turn ID: `1994d5e8-89b4-4991-a277-48f235e8eec9; 7070b14b-c1b1-45fa-8c2b-20fc1030bc43; b356038d-ac7d-418d-a452-465cdc2151e3`

Demo và spec cũ để tham khảo, không mặc định tái sử dụng.

<a id="src-10"></a>
### SRC-10 — Checkpoint Câu 29–37

Turn ID: `4b0d9285-dbf6-4368-9198-4917df84b27b`

Founder đưa nguyên checkpoint đã correction: value Sale; whitelist + eligibility; Owner accept; operator xác nhận cọc; 30/70 lịch sử; Guest xem bằng QR không tài khoản.

<a id="src-11"></a>
### SRC-11 — Giá thật và hidden spread

Turn ID: `676eac66-a212-4112-9e1c-7cb32b0d0838`

Giá trên hệ thống phải là giá thực bán cho Guest; Sale nhận commission, không thu chênh ẩn.

<a id="src-12"></a>
### SRC-12 — Sale commission và incentive cũ

Turn ID: `c35a6949-4039-429f-a1ee-3b286cc7a98f`

Founder nêu 10% trực tiếp, dự tính tổng 15% gồm quỹ 5%; lịch sử này được cập nhật bởi Founder Review: Sale base 10% của Commissionable Booking Value là CONFIRMED, còn quỹ/incentive và các economics khác không tự được xác nhận.

<a id="src-13"></a>
### SRC-13 — Direct/Sale pricing

Turn ID: `c7c98750-7370-406b-b130-8d4e39873bb6; 026b8b7d-b7a8-4c57-82dd-f8e215aa088f; 4f91cd70-c8b0-4e05-a67c-7d3311603c3c`

Lịch sử gồm public cao hơn Sale 5–10% và ý tưởng direct instant giảm 10%; Founder Review đã SUPERSEDE public premium bằng One Public Price. Direct instant discount 10% không được khôi phục ngầm; policy discount còn TBD.

<a id="src-14"></a>
### SRC-14 — Ba trạng thái quan hệ Sale

Turn ID: `02f54e24-1405-4630-846b-670c74dd0ca0`

Normallist mặc định; whitelist tin tưởng; blacklist không tương tác với chủ nhà đó.

<a id="src-15"></a>
### SRC-15 — Direct demand và lead

Turn ID: `d208797a-9913-4f9e-a951-afb5bed1086d; e9083492-4a16-43da-815f-9276256c0b11; 9a33ee8a-7376-4d80-aa1f-76f97d651cac; ebfb4c6a-b3fa-4d99-8734-31a56ce26d20`

Self-service hoặc tư vấn qua Sale; tier/rating ưu tiên; cửa sổ dự tính 5–10s; xử lý 24h, xin thêm tối đa 24h; Coordinator là nhân sự Stayora.

<a id="src-16"></a>
### SRC-16 — Affiliate khác Sale

Turn ID: `206c6f50-269c-411a-b071-88b51f20eb0b; 42ec6220-0236-4810-a119-4ac3adce8e08; dbe90c33-1dbc-415f-9a48-161a6dae4134; 31fc8f85-2cde-4f55-bab1-b47d37e98a5b`

Acquisition khác conversion; cùng attribution; founder đề xuất A% Affiliate và Sale 10%−A%, không chốt A.

<a id="src-17"></a>
### SRC-17 — Commissionable value

Turn ID: `7e99eaa5-c3b0-452c-863b-c9cdbb3e998f`

Founder đồng ý tách commissionable value khỏi toàn bộ Guest payment; deposit/add-on có economics riêng.

<a id="src-18"></a>
### SRC-18 — Bỏ Managed khỏi core

Turn ID: `1018596e-8306-4c44-a3b7-9372227eaff9; 37563e4b-4cf9-462b-a877-24c90b1012df; cecde8b3-a642-48e8-b525-c3fcc8413ad1`

Founder: “tạm thời có thể bỏ managed ra khỏi stayora… chỉ tập trung vào marketplace”.

<a id="src-19"></a>
### SRC-19 — Money research và lần chốt foundation cũ

Turn ID: `df61d348-5a55-48a3-9caa-dd2d1f8e07e1; dfe1737f-d083-4111-89d4-3307e17cd703`

100% facilitated collection; company/intermediary direction; ~3%/~2%/~5% working. Lời assistant về pháp luật không được coi là xác minh. Có xung đột nhãn 10% Sale.

<a id="src-20"></a>
### SRC-20 — Thesis và định nghĩa pilot

Turn ID: `6b020308-441d-4157-b884-ed58df10ad12; a78d2743-0ded-4495-a352-b91653d06749; 88ff28c6-c0db-40d0-a8e5-163920c9816f; 42210456-c224-49fc-8488-c6b51387bfae`

Founder chấp nhận operational penetration là thành công dù commerce thấp. KPI số là target hypotheses.

<a id="src-21"></a>
### SRC-21 — Primary Host và delegation

Turn ID: `1f54aa4f-7e84-4fa1-a0b9-feef708eda2a; e1e02ba8-a6aa-41b1-a877-cb18483ff623`

Một Primary Host, nhiều Co-host; quyền accept/reject được delegate; ownership khác authority.

<a id="src-22"></a>
### SRC-22 — Request và inventory authority

Turn ID: `9082b487-d1db-48e5-8a5d-ca700a3f50e4; 43fc1e18-732a-4936-90f1-8abde5409f0e`

Request không reserve; authorized acceptance có thể tạo Temporary Inventory Commitment hữu hạn; Payment Session/Attempt tách riêng; external confirmed có cùng authority; một villa-night một truth.

<a id="src-23"></a>
### SRC-23 — Instant Book

Turn ID: `252496b0-5fde-4a3b-ba91-c9db7cc9ebd7`

Commitment; villa enabled, điều kiện hợp lệ, thanh toán; founder muốn không hủy/đổi và phải show rõ; wording/remediation chưa chốt.

<a id="src-24"></a>
### SRC-24 — Settlement sau completed stay

Turn ID: `b6e61bb1-2371-4ee6-85a7-554b3f1ec895`

Founder: “chuyển sau khi checkout, khi booking thật sự kết thúc”. Không suy ra payout ngay khi checkout.

<a id="src-25"></a>
### SRC-25 — Identity và onboarding

Turn ID: `fe82cf89-bb14-4940-bdb4-a83789bd0304`

Guest/Owner tự đăng ký; Sale/Butler apply approval. Affiliate chưa có quyết định rõ về exemption hay approval.

<a id="src-26"></a>
### SRC-26 — Financial/data boundaries

Turn ID: `640b95e2-5344-44fc-807a-113d6ca4fc25`

Sale thấy giá bán và commission của mình, không Owner net/payout/tax/settlement; access theo relationship.

<a id="src-27"></a>
### SRC-27 — Verified và reputation

Turn ID: `4f311b4f-741f-4b00-9e5d-09eff5032d79; 311ba980-6700-4378-9020-d2fa3ae07aac`

Verified không luxury; maintained; external verified completed stay có thể tạo reputation; checklist 6 nhóm là đề xuất.

<a id="src-28"></a>
### SRC-28 — Destination

Turn ID: `311ba980-6700-4378-9020-d2fa3ae07aac; 61581189-3ef3-47ac-8dc1-d923570f3984`

Destination first-class; core/configuration/integration; BQL scoped. Mô hình independent property chưa đặc tả.

<a id="src-29"></a>
### SRC-29 — Phương pháp và baseline Checkpoint 1

Turn ID: `9d226a42-f3c9-471f-9af3-af5bb6a16537; 38f06ef4-a79c-43d6-8315-1ef441044115; 7ca27d39-6a36-4cc3-a608-c44357e043e6; 5852f568-4904-46b6-bc58-6ca67d9bd612; 8c0f906f-a7f2-424a-86aa-3ad836a15efb`

Reconcile trước; Sol architect/editor, executor tạo file; 18 docs; không tự nâng status, founder review rồi mới freeze.

<a id="src-30"></a>
### SRC-30 — Founder operating case: parallel acceptance

Turn ID: `Founder operating case, relayed in the Product Architect disposition of 2026-09-23`

Founder operating case, 2026-09-23 — two overlapping Requests on one Host's open dates; the Host accepts without rejecting the other so as not to lose both if the deposit does not arrive; deposit race; waiting time set by the Host; extension on request; confirmation blocks the remaining Requests. Recorded as the source of ADR-P070.

## Quy tắc cập nhật

Đề xuất thay đổi phải ghi decision ID, câu hiện hành, câu mới, status, nguồn founder và file bị ảnh hưởng. Không xóa lịch sử: đánh dấu SUPERSEDED và nối decision thay thế. Khi chỉ thay tỷ lệ hoặc cách triển khai, không tự thay principle nền. Founder đã xác nhận freeze: ghi rõ phiên bản, ngày, phạm vi và các TBD được giữ mở.

## Protected Baseline

All CONFIRMED decisions in CP1–CP8 form the Protected Baseline. Downstream work must comply with them. No agent may change a CONFIRMED decision because implementation is difficult. There is no global Founder Freeze; this is a compliance rule, not immutability.

Change path: conflict discovered → affected decision identified → Founder / Product Architect review → explicit amendment → DECISIONS / ADR update → downstream reconciliation.

TBD remains open. WORKING MODEL may be refined. HYPOTHESIS must be validated. OUT OF SCOPE — V0 is not pulled into V0 without an explicit decision.

## Founder Decisions (FD) and ADR-P

ADR-P is the canonical durable product/domain decision record. FD entries are the historical record of the Founder Decision Gate. A domain-effective FD is marked CANONICALIZED → ADR-P0xx; it is not renumbered and not marked SUPERSEDED. The canonicalization index is in DECISIONS.md.

## Public Exposure Review

This repository is PUBLIC during the specification phase. Before Implementation Planning begins — after CP8-H — a Public Exposure Review is performed: remove anything that should not remain public, confirm no credentials or real personal, commercial or contractual data were ever committed, then switch the repository to PRIVATE. Switching visibility does not change the source of truth; commit SHAs, ADR history, branches and decision history are preserved.
