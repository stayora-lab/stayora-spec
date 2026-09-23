# Decision register và contradiction audit

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

## Cách đọc

Đây là reconciliation register của Checkpoint 1. Mỗi ADR ghi kết luận hẹp nhất có thể bảo vệ bằng nguồn. Chi tiết đề xuất trong cùng một lượt chat không tự kế thừa status của principle được xác nhận. Những quyết định có nhãn TBD/WORKING MODEL không được dùng như requirement triển khai.

| Status | Ý nghĩa |
|---|---|
| CONFIRMED | Quyết định/ranh giới được founder xác nhận; sự kiện nguồn gốc là founder-reported, không kiểm chứng độc lập. |
| WORKING MODEL | Model/baseline dùng để reasoning, chưa là policy cuối. |
| HYPOTHESIS | Niềm tin, mục tiêu hoặc cơ chế cần validation. |
| TBD | Quyết định còn mở hoặc source/status conflict chưa reconcile được. |
| OUT OF SCOPE — V0 | Capability bị loại rõ khỏi V0/current core; không tự áp cho thứ chưa được bàn. |
| SUPERSEDED | Model/giả định cũ không còn hiệu lực; giữ lịch sử và chỉ ra replacement nếu có. |

`legal-validation-required` là cờ validation, không phải status thứ bảy. `OPEN/RESOLVED` dưới đây là trạng thái audit, không phải quyết định sản phẩm.

## Checkpoint 4 decision provenance

Checkpoint 4 lifecycle and policy decisions are documented in [05-state-machines-policies](../05-state-machines-policies/README.md). They preserve the existing ADR vocabulary and refine only the explicitly resolved boundaries: lifecycle classification, Booking/Payment/Stay/Settlement separation, Inventory Commitment semantics, Verification/Reputation/Incident/Lead models, policy layers, and the ten reconciliation scenarios. The refinement is partial where noted in Q-02, Q-15 and ADR-P020/P021; Offer ownership, policy precedence, exact transitions and economic parameters remain open. Open policy questions remain in [Checkpoint 4 open questions](../05-state-machines-policies/22-open-policy-questions.md); no new ADR numbering is introduced by the documentation pass.

## Checkpoint 5 decision provenance

Checkpoint 5 V0 scope is documented in [06-v0-scope](../06-v0-scope/README.md). It operationalizes the approved Oceanami pilot thesis and capability boundary without redesigning CP1–4. V0 MUST BUILD preserves Inventory, Booking, Stay, Destination Operations and Money/domain integrity; complex policy execution may be MANUAL-ASSISTED; Affiliate network, advanced automation, full PMS/Channel Manager and Managed Operations remain OUT OF V0. Existing hypotheses (including coverage, accuracy and trust targets) remain HYPOTHESIS. No new ADR numbering is introduced here.

## Checkpoint 6 decision provenance

Checkpoint 6 Information Architecture is documented in [07-information-architecture](../07-information-architecture/README.md). It refines the presentation and navigation layer only: one Identity may use multiple Working Contexts; context changes perspective but not authority; surfaces are contextual projections over shared truth; navigation follows responsibility; Public Marketplace, Guest Stay Access, Host, Sale, Butler, Destination/BQL and Admin have distinct responsibilities; acquisition and fulfillment remain separable. It does not create routes, schemas, UI components or a CP7 Data Model. Guest Account/My Trips and Instant Book remain optional/later or controlled pilot as stated in CP5. No new ADR numbering is introduced.

## Checkpoint 7 decision provenance

Checkpoint 7 Conceptual Data Model is documented in [08-conceptual-data-model](../08-conceptual-data-model/README.md). It records business objects, aggregate candidates, domain ownership, derived projections, temporal relationships, provenance and immutable historical truth. Candidate aggregates are conceptual only; no physical persistence, API or implementation decision is introduced. R1 late external fact/conflict, R2 amendment/supersession and R3 temporal validity are recorded as refinements. Existing TBD/HYPOTHESIS/WORKING MODEL statuses remain open. No new ADR numbering is introduced.

## CP7 persistence-direction provenance

Supporting Persistence Architecture is documented in [09-database-design](../09-database-design/README.md) as the persistence portion of CP7 Data Model. The artifact preserves PostgreSQL as canonical transactional store, database/domain/application invariant boundaries, temporal/provenance/history requirements, projection direction, V0 modular-monolith topology and table-family mapping directions. It is not an implementation freeze and remains subject to UX/implementation validation; no final columns, SQL, Drizzle schema, migration, API or service decision is introduced. Open decisions remain in [CP7 Persistence Open Decisions](../09-database-design/10-open-decisions.md). No new ADR numbering is introduced.

## CP8-E Founder Decision Gate FD-01 → FD-19

**Status: COMPLETE.** These are Founder decisions reconciled after E1–E4. They are review decisions inside CP8-E, not a new checkpoint. The full matrix and residual boundaries are in [CP8-E Founder Decision Reconciliation](../11-detailed-interaction/CP8-E-FOUNDER-DECISION-RECONCILIATION.md).

| ID | Canonical outcome | Status | Residual boundary |
|---|---|---|---|
| FD-01 | Check-in/Checkout = explicit capability/grant + Assignment/resource scope + current Stay preconditions. | CLOSED | Exact grant administration |
| FD-02 | CHECKED_OUT is evaluated; COMPLETED is automatic when canonical conditions pass; blockers remain pending for re-evaluation. | CLOSED | Exception policy |
| FD-03 | COMPLETED ends the Stay lifecycle; it does not close Incident, Payment, compensation, Settlement or release Inventory. | CLOSED | Separate downstream policies |
| FD-04 | V0 completion conditions are authoritative Checkout → CHECKED_OUT → evaluation → COMPLETED when no Stay-lifecycle blocker exists. | CLOSED | No workforce workflow |
| FD-05 | DID_NOT_OCCUR is explicit, authorized and evaluated; never clock-automatic. | CLOSED | Penalty/refund/default/cancellation/release effects |
| FD-06 | Credential or authenticated Guest Identity + legitimate Stay association reach the same Guest Stay Hub/truth. | CLOSED | Credential mechanism/security lifecycle |
| FD-07 | Guest projection follows legitimate association, access mechanism and Stay truth across lifecycle states. | CLOSED | Field-level privacy |
| FD-08 | Conflict preserves truths, provenance and Unit×Time, identifies responsibility and uses legitimate authority or scoped Admin reconciliation. | CLOSED | Operating remedy |
| FD-09 | No universal V0 conflict precedence or automatic winner exists. | CLOSED | Case-specific resolution |
| FD-10 | Temporary Exclusive Commitment is canonical where applicable; duration/expiry/release/replacement follow policy, not a hard-coded universal timeout. | CLOSED | Concrete duration/extension |
| FD-11 | Temporary release is canonical lifecycle execution or explicit scoped Release Authority + Unit×Time + revalidation. | CLOSED | Exact timing/conditions |
| FD-12 | Only explicit scoped External Accommodation Recording Authority creates an authoritative External Fact. | CLOSED | Evidence standards/procedure |
| FD-13 | Verified Ownership Relationship is an authority basis for scoped Owner Block capability, not unrestricted or universal override authority. | CLOSED | Grant administration/remedy |
| FD-14 | Maintenance Block requires explicit scoped Maintenance Inventory Authority; Incident/Finding/evidence only routes to evaluation. | CLOSED | Evidence standard/procedure |
| FD-15 | Emergency Protective Hold is Founder-approved, protective and distinct from Maintenance Block; it prevents new conflicts, escalates and does not override existing commitments. | CLOSED — EXTENSION | Eligible actor and policy boundary |
| FD-16 | Emergency Protective Hold has policy-defined review/expiry; unresolved expiry leaves Attention. | CLOSED — EXTENSION | Concrete duration |
| FD-17 | Booking Confirmation Policy, not Payment alone, determines confirmation after Request ACCEPTED and applicable Inventory conditions. | CLOSED | Payment/deadline/grace/default details |
| FD-18 | Payment Verification requires explicit scoped Payment Verification Authority and is distinct from Booking/Inventory Authority. | CLOSED | Evidence/verification procedure |
| FD-19 | Payment UNKNOWN is neither success nor failure; reconcile before SUCCEEDED/FAILED or continued UNKNOWN. | CLOSED | Retry/refund/cancellation/deposit/deadline details |

## CP8-F Founder Visual Decision — F2 Closure

**Status: ACCEPTED.** The Founder/Product Architect accepted the CP8-F2 visual direction as the CP8-G baseline with four semantic presentation corrections. This is a design-language acceptance, not a production UI freeze, component API freeze or global prohibition on future visual evolution. CP8-G remains not started.

| Decision | Outcome | Canonical consequence |
|---|---|---|
| COLOR | ACCEPTED | Warm cream canvas, warm surfaces/ink, restrained purple action and restrained semantic colors are accepted as the F2 direction. |
| TYPOGRAPHY | ACCEPTED | Plus Jakarta Sans is primary; Cormorant Garamond is selective editorial/display. |
| SHAPE | ACCEPTED | 8 / 12 / 16 / full radius roles are accepted. |
| SURFACE / ELEVATION | ACCEPTED | Warm surfaces and restrained borders/elevation are accepted. |
| DENSITY | ACCEPTED | Surface-specific density is accepted across Marketplace, Guest, Workspace and Operations. |
| MARKETPLACE CHARACTER | ACCEPTED | Warm hospitality character is accepted. |
| WORKSPACE CHARACTER | ACCEPTED WITH CORRECTIONS | Domain truth must not be represented as generic SUCCESS. |
| OPERATIONAL CHARACTER | ACCEPTED WITH CORRECTIONS | Processing/Unknown, protective attention and current-domain presentation are distinct. |
| OVERALL F2 VISUAL DIRECTION | ACCEPTED WITH CORRECTIONS | F2 is the CP8-G prototype baseline; no product/domain/policy semantics changed. |

### F2 semantic presentation corrections

1. **Domain state ≠ SUCCESS.** CONFIRMED, CHECKED_IN, READY milestones and OBSERVED facts use neutral/current-domain presentation, not generic interaction-success treatment.
2. **PROCESSING ≠ UNKNOWN.** PROCESSING means known work is still underway. UNKNOWN means the authoritative outcome cannot currently be established; both protect against unsafe duplicate action, but their copy and visual treatment remain distinct. UNKNOWN ≠ FAILED and UNKNOWN ≠ SUCCESS.
3. **Emergency Protective Hold ≠ CONFLICT.** It uses protective/attention presentation. It remains distinct from Maintenance Block, Conflict, Finding and Booking cancellation; an actual conflict may be composed separately.
4. **External Accommodation Fact ≠ External-backed Commitment.** The chain remains Report/Evidence → authorized recording/validation → External Accommodation Fact → Inventory evaluation → External-backed Commitment where applicable → legitimate Stay where applicable. Inventory truth uses External-backed Commitment when that is canonical and retains the Fact as basis/provenance.

No new role, workspace, domain state, policy, Inventory precedence or payment rule is created by these visual decisions.

**Protected consequences:** Completion does not release Inventory; Payment does not by itself confirm Booking; Guest credential does not grant authority; Butler Assignment/Host relationship/BQL visibility do not grant operational mutation authority; Emergency Protective Hold is not Maintenance Block. Remaining TBDs are not silently resolved.

## Decision index

| ID | Quyết định | Status |
|---|---|---|
| [ADR-P001](#adr-p001) | Marketplace mở | CONFIRMED |
| [ADR-P002](#adr-p002) | Stayora Verified là assurance | CONFIRMED |
| [ADR-P003](#adr-p003) | Managed nằm ngoài current core | OUT OF SCOPE — V0 |
| [ADR-P004](#adr-p004) | Destination first-class | CONFIRMED |
| [ADR-P005](#adr-p005) | Core khác destination policy | CONFIRMED |
| [ADR-P006](#adr-p006) | Một identity, nhiều role | CONFIRMED |
| [ADR-P007](#adr-p007) | Onboarding Guest và Host | CONFIRMED |
| [ADR-P008](#adr-p008) | Sale và Butler cần approval | CONFIRMED |
| [ADR-P009](#adr-p009) | Primary Host và Co-host | CONFIRMED |
| [ADR-P010](#adr-p010) | Delegated booking authority | CONFIRMED |
| [ADR-P011](#adr-p011) | Sale là actor phân phối trọng tâm | CONFIRMED |
| [ADR-P012](#adr-p012) | Normallist / whitelist / blacklist | CONFIRMED |
| [ADR-P013](#adr-p013) | Request không giữ inventory | CONFIRMED |
| [ADR-P014](#adr-p014) | Authorized acceptance tạo Temporary Inventory Commitment; Money attempt tách riêng | CONFIRMED — REFINED |
| [ADR-P015](#adr-p015) | Một villa-night một inventory truth | CONFIRMED |
| [ADR-P016](#adr-p016) | External stay tham gia operations | CONFIRMED |
| [ADR-P017](#adr-p017) | Instant Book là commitment | CONFIRMED |
| [ADR-P018](#adr-p018) | Điều kiện Sale Instant Book | CONFIRMED |
| [ADR-P019](#adr-p019) | Chính sách Instant Book | CONFIRMED |
| [ADR-P020](#adr-p020) | Booking / Payment / Stay / Settlement tách biệt | CONFIRMED |
| [ADR-P021](#adr-p021) | Settlement sau completed stay | CONFIRMED |
| [ADR-P022](#adr-p022) | Commissionable value riêng | CONFIRMED |
| [ADR-P023](#adr-p023) | Giá giao dịch minh bạch | CONFIRMED |
| [ADR-P024](#adr-p024) | Sale tự giảm commission | CONFIRMED |
| [ADR-P025](#adr-p025) | Reputation theo trách nhiệm | CONFIRMED |
| [ADR-P026](#adr-p026) | External verified stays tạo reputation | CONFIRMED |
| [ADR-P027](#adr-p027) | Financial/data access có scope | CONFIRMED |
| [ADR-P028](#adr-p028) | BQL destination-scoped | CONFIRMED |
| [ADR-P029](#adr-p029) | Oceanami là beachhead | CONFIRMED |
| [ADR-P030](#adr-p030) | North Star direction | CONFIRMED |
| [ADR-P031](#adr-p031) | Direct demand có hai đường | CONFIRMED |
| [ADR-P032](#adr-p032) | Affiliate khác Sale | CONFIRMED |
| [ADR-P033](#adr-p033) | Lead responsibility và coordinator | CONFIRMED |
| [ADR-P034](#adr-p034) | Guest xem confirmation không account | CONFIRMED |
| [ADR-P035](#adr-p035) | Minh bạch thay giá sàn | CONFIRMED |
| [ADR-P036](#adr-p036) | Hướng commercial/legal entity | WORKING MODEL |
| [ADR-P037](#adr-p037) | Facilitated collection 100% | WORKING MODEL |
| [ADR-P038](#adr-p038) | Sale base commission 10% | CONFIRMED |
| [ADR-P039](#adr-p039) | Affiliate / incentive / platform fee | WORKING MODEL |
| [ADR-P040](#adr-p040) | Shared distribution economics | WORKING MODEL |
| [ADR-P041](#adr-p041) | One Public Price | CONFIRMED |
| [ADR-P042](#adr-p042) | Lead timings và Sale scoring | WORKING MODEL |
| [ADR-P043](#adr-p043) | Affiliate onboarding | TBD |
| [ADR-P044](#adr-p044) | Verified standard và reputation mechanics | WORKING MODEL |
| [ADR-P045](#adr-p045) | Pilot targets và flywheel | HYPOTHESIS |
| [ADR-P046](#adr-p046) | Miễn phí external operations giai đoạn đầu | HYPOTHESIS |
| [ADR-P047](#adr-p047) | Inventory sync cadence | WORKING MODEL |
| [ADR-P048](#adr-p048) | Legal/tax treatment | TBD |
| [ADR-P049](#adr-p049) | V0 implementation boundary | TBD |
| [ADR-P050](#adr-p050) | Old Managed-as-core | SUPERSEDED |
| [ADR-P051](#adr-p051) | 30/70 là payment foundation | SUPERSEDED |
| [ADR-P052](#adr-p052) | Request giữ đêm theo Airbnb reference | SUPERSEDED |
| [ADR-P053](#adr-p053) | BQL/floor bắt buộc điều khiển giá | SUPERSEDED |
| [ADR-P054](#adr-p054) | Tách account cố định theo actor | SUPERSEDED |
| [ADR-P055](#adr-p055) | 5% incentive cố định | SUPERSEDED |
| [ADR-P056](#adr-p056) | Affiliate cộng thêm pool độc lập mặc định | SUPERSEDED |
| [ADR-P057](#adr-p057) | Stayora 2.0 là source of truth | SUPERSEDED |
| [ADR-P058](#adr-p058) | Payout ở confirmation/check-in | SUPERSEDED |
| [ADR-P059](#adr-p059) | Direct price premium over Sale | SUPERSEDED |
| [ADR-P060](#adr-p060) | Required Payment Condition | CONFIRMED |
| [ADR-P061](#adr-p061) | Oceanami Pilot Booking Payment Policy v0.1 | CONFIRMED |
| [ADR-P062](#adr-p062) | Inventory Availability derived truth | CONFIRMED |
| [ADR-P063](#adr-p063) | Inventory Commitment umbrella | CONFIRMED |
| [ADR-P064](#adr-p064) | Physical absence ≠ Inventory Release | CONFIRMED |
| [ADR-P065](#adr-p065) | Payment Default ≠ No-show | CONFIRMED |

<a id="adr-p001"></a>
### ADR-P001 — Marketplace mở

**Status: CONFIRMED**

Marketplace mở. Owner Listed supply có thể tham gia khi đáp ứng listing/compliance; property không cần Stayora Verified chỉ để được tham gia. Stayora Verified là lớp Trust & Quality Assurance bổ sung, không phải marketplace admission mặc định.

**Ranh giới:** Marketplace mở không đồng nghĩa miễn listing, identity, right-to-operate hoặc compliance requirements.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-02](SOURCE_OF_TRUTH.md#src-02)

<a id="adr-p002"></a>
### ADR-P002 — Stayora Verified là assurance

**Status: CONFIRMED**

Verified là trust/quality assurance, không phải luxury, không đồng nghĩa Managed; phải được duy trì.

**Ranh giới:** Checklist, tần suất, phí, người kiểm: TBD.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-27](SOURCE_OF_TRUTH.md#src-27)

<a id="adr-p003"></a>
### ADR-P003 — Managed nằm ngoài current core

**Status: OUT OF SCOPE — V0**

Loại Stayora Managed khỏi marketplace foundation hiện tại; có thể là business bên ngoài hoặc lớp tương lai.

**Ranh giới:** Không kế thừa management fee 10%, P&L và quyền operator vào core.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-18](SOURCE_OF_TRUTH.md#src-18)

<a id="adr-p004"></a>
### ADR-P004 — Destination first-class

**Status: CONFIRMED**

Destination là lớp discovery và operational boundary, không chỉ một location/filter.

**Ranh giới:** Cấu trúc phân cấp địa lý/operational membership chi tiết: TBD.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-28](SOURCE_OF_TRUTH.md#src-28)

<a id="adr-p005"></a>
### ADR-P005 — Core khác destination policy

**Status: CONFIRMED**

Core định nghĩa capabilities; destination định nghĩa local policies; integration nối vận hành địa phương.

**Ranh giới:** Không hard-code QR/xe điện/tối đa hai Butler cho mọi nơi.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-28](SOURCE_OF_TRUTH.md#src-28), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p006"></a>
### ADR-P006 — Một identity, nhiều role

**Status: CONFIRMED**

Guest/Host/Sale/Butler là role và relationship trên một identity, không phải bốn account type độc lập.

**Ranh giới:** Một role không tự cấp quyền trên mọi tài nguyên.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-25](SOURCE_OF_TRUTH.md#src-25)

<a id="adr-p007"></a>
### ADR-P007 — Onboarding Guest và Host

**Status: CONFIRMED**

Guest và Host được self-onboard; Host tự đăng ký không đồng nghĩa villa tự động publish.

**Ranh giới:** Checklist identity/quyền khai thác/compliance: TBD; legal-validation-required.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-25](SOURCE_OF_TRUTH.md#src-25)

<a id="adr-p008"></a>
### ADR-P008 — Sale và Butler cần approval

**Status: CONFIRMED**

Sale/Butler đăng ký vai trò và phải được Stayora duyệt; Butler approved còn cần quan hệ assignment với villa.

**Ranh giới:** Approval không tự biến Butler thành nhân viên Stayora.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-25](SOURCE_OF_TRUTH.md#src-25), [SRC-04](SOURCE_OF_TRUTH.md#src-04)

<a id="adr-p009"></a>
### ADR-P009 — Primary Host và Co-host

**Status: CONFIRMED**

Mỗi villa tại một thời điểm có một Primary Host chịu trách nhiệm chính; nhiều Co-host có quyền được delegate.

**Ranh giới:** Primary Host không nhất thiết legal owner; chuyển quyền/tranh chấp: TBD.

**Nguồn:** [SRC-21](SOURCE_OF_TRUTH.md#src-21)

<a id="adr-p010"></a>
### ADR-P010 — Delegated booking authority

**Status: CONFIRMED**

Co-host được cấp quyền có thể accept/reject như Primary Host; phải ghi actor, authority và thời điểm.

**Ranh giới:** Cuộc gọi không thay thế hành động chấp nhận trong hệ thống.

**Nguồn:** [SRC-21](SOURCE_OF_TRUTH.md#src-21)

<a id="adr-p011"></a>
### ADR-P011 — Sale là actor phân phối trọng tâm

**Status: CONFIRMED**

Sale tư vấn, conversion và relationship; không mặc định là Co-host và không bị loại khỏi marketplace.

**Ranh giới:** Sale có thể đồng thời mang role khác; quyền mỗi relationship tách riêng.

**Nguồn:** [SRC-03](SOURCE_OF_TRUTH.md#src-03), [SRC-10](SOURCE_OF_TRUTH.md#src-10), [SRC-16](SOURCE_OF_TRUTH.md#src-16)

<a id="adr-p012"></a>
### ADR-P012 — Normallist / whitelist / blacklist

**Status: CONFIRMED**

Whitelist/Blacklist là trust relationship giữa Sale ↔ Owner / Authorized Host, áp dụng trên inventory nằm trong commercial authority của Owner/Authorized Host; đây không phải property-scoped-only relation. Normallist là mặc định được request. Blacklist chặn tương tác trong scope commercial authority đó.

**Ranh giới:** Whitelist không tự cấp mọi capability. Effective permission = Sale–Owner/Authorized Host relationship + property policy + platform eligibility. Legal ownership và commercial/hosting authority có thể khác nhau.

**Nguồn:** [SRC-14](SOURCE_OF_TRUTH.md#src-14), [SRC-22](SOURCE_OF_TRUTH.md#src-22), [SRC-23](SOURCE_OF_TRUTH.md#src-23)

<a id="adr-p013"></a>
### ADR-P013 — Request không giữ inventory

**Status: CONFIRMED**

Request chỉ là ý định; không reserve villa-night và không dùng để ôm hàng.

**Ranh giới:** External confirmed đến khi request pending làm request mất availability.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-22](SOURCE_OF_TRUTH.md#src-22)

<a id="adr-p014"></a>
### ADR-P014 — Authorized Acceptance tạo Temporary Inventory Commitment

**Status: CONFIRMED — REFINED**

Request không reserve Inventory. Host hoặc Co-host có authority accept có thể tạo một Temporary Exclusive Inventory Commitment có hạn; Money độc lập thực hiện Payment Session / Attempt áp dụng. Hết window theo policy thì commitment kết thúc và Inventory Availability được tính lại. Lịch sử “Payment Hold” là tên cũ của một khái niệm kết hợp; đã REFINED thành Temporary Inventory Commitment thuộc Inventory và Payment Session / Attempt thuộc Money.

**Ranh giới:** Duration, payment pending/late success và race: TBD.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-22](SOURCE_OF_TRUTH.md#src-22)

<a id="adr-p015"></a>
### ADR-P015 — Một villa-night một inventory truth

**Status: CONFIRMED**

Confirmed external booking có cùng inventory authority với Stayora booking; không ưu tiên nguồn commerce Stayora.

**Ranh giới:** Không hứa real-time đa kênh hay tự chọn bên thắng khi hai confirmation xung đột.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-22](SOURCE_OF_TRUTH.md#src-22)

<a id="adr-p016"></a>
### ADR-P016 — External stay tham gia operations

**Status: CONFIRMED**

Ghi villa, IN/OUT, số khách, dữ liệu cần cho BQL, nguồn booking; không ép khai toàn bộ giá/doanh thu ngoài.

**Ranh giới:** Không tự có commission hoặc commercial support tương đương Stayora booking.

**Nguồn:** [SRC-06](SOURCE_OF_TRUTH.md#src-06), [SRC-22](SOURCE_OF_TRUTH.md#src-22)

<a id="adr-p017"></a>
### ADR-P017 — Instant Book là commitment

**Status: CONFIRMED**

Khi villa bật và đủ eligibility/rules, không chờ accept từng booking; đi vào thanh toán/confirmation.

**Ranh giới:** Không có nghĩa confirmed chỉ vì bấm nút; inventory/payment validation vẫn cần.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-23](SOURCE_OF_TRUTH.md#src-23)

<a id="adr-p018"></a>
### ADR-P018 — Điều kiện Sale Instant Book

**Status: CONFIRMED**

Cần đồng thời platform eligibility, Host whitelist, villa bật Instant Book và các booking rules hợp lệ.

**Ranh giới:** Tiêu chí eligibility và tier algorithm: TBD.

**Nguồn:** [SRC-10](SOURCE_OF_TRUTH.md#src-10), [SRC-14](SOURCE_OF_TRUTH.md#src-14), [SRC-23](SOURCE_OF_TRUTH.md#src-23)

<a id="adr-p019"></a>
### ADR-P019 — Chính sách Instant Book

**Status: CONFIRMED**

Ý định thương mại không hủy/không đổi phải được nói rõ trước khi Guest cam kết.

**Ranh giới:** Wording, ngoại lệ supplier failure, refund/remediation: TBD, legal-validation-required; không phải miễn trách nhiệm tuyệt đối.

**Nguồn:** [SRC-23](SOURCE_OF_TRUTH.md#src-23)

<a id="adr-p020"></a>
### ADR-P020 — Booking / Payment / Stay / Settlement tách biệt

**Status: CONFIRMED**

Chấp nhận booking, Payment Session / Attempt, thực hiện lưu trú và phân bổ/payout là các khái niệm khác nhau. Booking Confirmation cần các Booking Confirmation Conditions áp dụng, trong đó Required Payment Condition là một điều kiện; điều kiện này không mặc định là Fully Paid.

**Ranh giới:** Checkpoint 4 now documents conceptual lifecycle/state sets and selected confirmed boundaries, but diagrams are not automatically complete transition graphs. Unspecified transitions, guards and terminal/disposition details remain policy/data-model TBD.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-17](SOURCE_OF_TRUTH.md#src-17), [SRC-22](SOURCE_OF_TRUTH.md#src-22), [SRC-24](SOURCE_OF_TRUTH.md#src-24), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p021"></a>
### ADR-P021 — Settlement sau completed stay

**Status: CONFIRMED**

Completed Stay là normal settlement/economic eligibility boundary, không phải universal prerequisite. Một fully paid hoặc otherwise commercially entitled accommodation commitment mà Guest không sử dụng có thể đi theo exception settlement path theo policy, nhưng không được đánh dấu Stay COMPLETED giả. Exact no-show economics vẫn TBD.

**Ranh giới:** SLA, reconciliation, dispute/no-show/cancellation entitlement: TBD.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-24](SOURCE_OF_TRUTH.md#src-24)

<a id="adr-p022"></a>
### ADR-P022 — Commissionable value riêng

**Status: CONFIRMED**

Commission không tính mặc định trên toàn bộ Guest payment; security deposit không là booking revenue/commissionable; add-ons có economics riêng.

**Ranh giới:** Cơ sở tính chính xác, discount/tax inclusion: TBD.

**Nguồn:** [SRC-17](SOURCE_OF_TRUTH.md#src-17), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p023"></a>
### ADR-P023 — Giá giao dịch minh bạch

**Status: CONFIRMED**

Giá booking trên hệ thống phải phản ánh giá thật bán cho Guest; Sale không được tạo hidden spread.

**Ranh giới:** Enforcement, dispute và chế tài cụ thể: TBD.

**Nguồn:** [SRC-11](SOURCE_OF_TRUTH.md#src-11)

<a id="adr-p024"></a>
### ADR-P024 — Sale tự giảm commission

**Status: CONFIRMED**

Sale được giảm phần hoa hồng của mình để cạnh tranh; không tự làm giảm phần Owner và Stayora.

**Ranh giới:** Quan hệ với Affiliate split/incentive và mức discount tối đa: TBD.

**Nguồn:** [SRC-03](SOURCE_OF_TRUTH.md#src-03)

<a id="adr-p025"></a>
### ADR-P025 — Reputation theo trách nhiệm

**Status: CONFIRMED**

Phân biệt trách nhiệm villa/Host, Sale, Butler và dịch vụ destination; review dựa trên tương tác có bằng chứng.

**Ranh giới:** Không suy ra mọi actor đều có sao công khai hoặc tự động chịu lỗi.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-02](SOURCE_OF_TRUTH.md#src-02), [SRC-04](SOURCE_OF_TRUTH.md#src-04), [SRC-27](SOURCE_OF_TRUTH.md#src-27)

<a id="adr-p026"></a>
### ADR-P026 — External verified stays tạo reputation

**Status: CONFIRMED**

External stay có đủ evidence thực sự diễn ra và completed có thể tạo reputation; commerce source không quyết định eligibility.

**Ranh giới:** Evidence threshold, review rights, chống giả và appeal: TBD.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-27](SOURCE_OF_TRUTH.md#src-27)

<a id="adr-p027"></a>
### ADR-P027 — Financial/data access có scope

**Status: CONFIRMED**

Role + relationship + resource scope quyết định access. Sale xem giá bán và commission của mình, không Owner net/payout/tax/settlement.

**Ranh giới:** Butler/BQL không mặc định xem commercial ledger; internal staff theo chức năng.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-26](SOURCE_OF_TRUTH.md#src-26)

<a id="adr-p028"></a>
### ADR-P028 — BQL destination-scoped

**Status: CONFIRMED**

BQL/destination staff chỉ có quyền trong destination và phạm vi chức năng được giao.

**Ranh giới:** BQL không quyết định giá thị trường và không là global super-role.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-28](SOURCE_OF_TRUTH.md#src-28), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p029"></a>
### ADR-P029 — Oceanami là beachhead

**Status: CONFIRMED**

Ưu tiên operational penetration → trusted inventory → network adoption → commerce growth; pilot có thể thành công khi commerce còn thấp.

**Ranh giới:** Không đồng nghĩa PMF đã chứng minh hoặc vô thời hạn không cần economics.

**Nguồn:** [SRC-20](SOURCE_OF_TRUTH.md#src-20), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p030"></a>
### ADR-P030 — North Star direction

**Status: CONFIRMED**

Destination Stay Coverage là North Star direction cho Oceanami pilot; operational penetration → trusted inventory → network adoption → commerce growth. Exact metric definition, denominator, measurement mechanics và numerical target vẫn HYPOTHESIS/TBD.

**Ranh giới:** Cách đo denominator/baseline và target số: chưa chốt.

**Nguồn:** [SRC-20](SOURCE_OF_TRUTH.md#src-20), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p031"></a>
### ADR-P031 — Direct demand có hai đường

**Status: CONFIRMED**

Guest tự booking hoặc yêu cầu tư vấn để hệ thống phân lead cho Sale.

**Ranh giới:** Không mặc định xây chat thay Zalo.

**Nguồn:** [SRC-15](SOURCE_OF_TRUTH.md#src-15)

<a id="adr-p032"></a>
### ADR-P032 — Affiliate khác Sale

**Status: CONFIRMED**

Affiliate tạo acquisition/referral; Sale tạo conversion/relationship; một booking có thể attribution cho cả hai.

**Ranh giới:** Không gộp profile, tiền hoặc approval của hai actor.

**Nguồn:** [SRC-16](SOURCE_OF_TRUTH.md#src-16)

<a id="adr-p033"></a>
### ADR-P033 — Lead responsibility và coordinator

**Status: CONFIRMED**

Sale nhận lead phải liên hệ, xử lý, cập nhật; Sale tốt được ưu tiên; Coordinator là nhân sự nội bộ Stayora xử lý exception.

**Ranh giới:** Thuật toán và timings nằm ở ADR-P042.

**Nguồn:** [SRC-15](SOURCE_OF_TRUTH.md#src-15)

<a id="adr-p034"></a>
### ADR-P034 — Guest xem confirmation không account

**Status: CONFIRMED**

Sau confirmation, Sale chuyển xác nhận/QR để Guest xem thông tin booking không cần account.

**Ranh giới:** Không có nghĩa QR công khai toàn bộ PII/ledger; token, expiry, revoke và gate QR: TBD.

**Nguồn:** [SRC-10](SOURCE_OF_TRUTH.md#src-10), [SRC-11](SOURCE_OF_TRUTH.md#src-11)

<a id="adr-p035"></a>
### ADR-P035 — Minh bạch thay giá sàn

**Status: CONFIRMED**

Tạm bỏ cơ chế floor bắt buộc; Owner chọn chiến lược giá/hiệu quả, trust và chất lượng giúp Guest lựa chọn.

**Ranh giới:** Giá thấp không tự là vi phạm; không khôi phục floor/AI floor.

**Nguồn:** [SRC-07](SOURCE_OF_TRUTH.md#src-07)

<a id="adr-p036"></a>
### ADR-P036 — Hướng commercial/legal entity

**Status: WORKING MODEL**

Baseline Công ty TNHH, Owner là accommodation supplier, Stayora là marketplace/intermediary ở mức product intent. Đây là hướng product intent để tiếp tục validation, không phải kết luận pháp lý đã xác nhận.

**Ranh giới:** legal-validation-required; không xác nhận tư cách pháp lý thực tế, hợp đồng hay gross/net accounting.

**Nguồn:** [SRC-18](SOURCE_OF_TRUTH.md#src-18), [SRC-19](SOURCE_OF_TRUTH.md#src-19)

<a id="adr-p037"></a>
### ADR-P037 — Facilitated collection 100%

**Status: WORKING MODEL**

Ưu tiên collection toàn bộ booking money qua licensed payment infrastructure, Stayora điều phối booking/settlement. “100% facilitated collection” nói về payment/collection rail, không nói Guest phải trả 100% tại Booking Confirmation; Oceanami có thể dùng policy 50% + 50%.

**Ranh giới:** legal-validation-required; provider, quyền giữ/chi tiền, xác minh payment và reconciliation: TBD.

**Nguồn:** [SRC-19](SOURCE_OF_TRUTH.md#src-19), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p038"></a>
### ADR-P038 — Sale base commission 10%

**Status: CONFIRMED**

Sale base distribution commission = 10% của Commissionable Booking Value.

Commission có thể ở trạng thái Pending sau confirmation; Completed Stay là normal Earned/settlement eligibility boundary. Policy-driven exception economics có thể tồn tại cho commercially fulfilled nhưng physically unused accommodation commitments, không rewrite Stay truth. Paid là settlement/payment state về sau. Cancellation/refund/no-show treatment vẫn là policy/TBD. Affiliate compensation có thể lấy từ distribution pool này; exact Affiliate/Sale split vẫn WORKING MODEL/TBD.

**Ranh giới:** Exact Commissionable Booking Value và exception treatment chưa chốt. Không biến tỷ lệ Affiliate ~3% thành CONFIRMED.

**Nguồn:** [SRC-12](SOURCE_OF_TRUTH.md#src-12), [SRC-19](SOURCE_OF_TRUTH.md#src-19)

<a id="adr-p039"></a>
### ADR-P039 — Affiliate / incentive / platform fee

**Status: WORKING MODEL**

~3% Affiliate, ~2% performance incentive, ~5% Stayora fee là số để financial modelling.

**Ranh giới:** Không là requirement/bảng giá. Cơ sở tính, người chịu phí và allocation: TBD.

**Nguồn:** [SRC-16](SOURCE_OF_TRUTH.md#src-16), [SRC-19](SOURCE_OF_TRUTH.md#src-19), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p040"></a>
### ADR-P040 — Shared distribution economics

**Status: WORKING MODEL**

Founder đề xuất Affiliate A%, Sale 10%−A% khi cần tư vấn; self-service không tự phát sinh Sale commission.

**Ranh giới:** Giữ ý định và provenance; exact split, A, attribution/refund: TBD.

**Nguồn:** [SRC-16](SOURCE_OF_TRUTH.md#src-16), [SRC-19](SOURCE_OF_TRUTH.md#src-19), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p041"></a>
### ADR-P041 — Direct/Sale price architecture

**Status: CONFIRMED**

Stayora dùng One Public Price: Direct Guest và Sale bắt đầu từ cùng public booking price trong cùng offer context. Sale có thể giảm giá cho Guest bằng cách hy sinh phần commission/incentive kinh tế thuộc Sale, subject to future policy. Sale không được tự ý giảm Owner entitlement. Owner-funded, Stayora-funded, Affiliate/campaign-funded discounts là mechanisms riêng và phải có attribution rõ.

**Ranh giới:** Không tự quyết discount limits, stacking, funding implementation hoặc accounting mechanics.

**Nguồn:** [SRC-13](SOURCE_OF_TRUTH.md#src-13), [SRC-19](SOURCE_OF_TRUTH.md#src-19), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p042"></a>
### ADR-P042 — Lead timings và Sale scoring

**Status: WORKING MODEL**

Giữ đề xuất nguồn: offer 5–10s; xử lý 24h; xin gia hạn tối đa +24h; latest baseline để timing/details mở.

**Ranh giới:** TBD policy reconciliation C-09, không đóng hard SLA; algorithm/tier weights: TBD.

**Nguồn:** [SRC-15](SOURCE_OF_TRUTH.md#src-15), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p043"></a>
### ADR-P043 — Affiliate onboarding

**Status: TBD**

Có đề xuất self-apply/basic verification; founder chưa chốt một approval model riêng cho Affiliate.

**Ranh giới:** Không tự miễn approval dựa trên lời assistant.

**Nguồn:** [SRC-25](SOURCE_OF_TRUTH.md#src-25), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p044"></a>
### ADR-P044 — Verified standard và reputation mechanics

**Status: WORKING MODEL**

Sáu nhóm checklist và lifecycle inspection/review/suspend/remove là đề xuất tổ chức.

**Ranh giới:** Inspection frequency, evidence, người kiểm, fee, review visibility/weights: TBD.

**Nguồn:** [SRC-27](SOURCE_OF_TRUTH.md#src-27)

<a id="adr-p045"></a>
### ADR-P045 — Pilot targets và flywheel

**Status: HYPOTHESIS**

Adoption tự nguyện, network effects, khả năng nhân rộng, target 12 tháng cần kiểm chứng bằng pilot.

**Ranh giới:** Không coi số ví dụ hay dự báo thị trường là baseline đã audit.

**Nguồn:** [SRC-06](SOURCE_OF_TRUTH.md#src-06), [SRC-20](SOURCE_OF_TRUTH.md#src-20)

<a id="adr-p046"></a>
### ADR-P046 — Miễn phí external operations giai đoạn đầu

**Status: HYPOTHESIS**

Founder dự tính miễn phí để adoption, có thể thu phí sau.

**Ranh giới:** Không cam kết free forever; chưa chốt fee/threshold/date.

**Nguồn:** [SRC-06](SOURCE_OF_TRUTH.md#src-06)

<a id="adr-p047"></a>
### ADR-P047 — Inventory sync cadence

**Status: WORKING MODEL**

Nguồn cũ dự kiến iCal 15 phút; hướng iCal và thừa nhận độ trễ giữ nguyên.

**Ranh giới:** Không là SLA realtime; cadence, provider capability, sync health V0: TBD.

**Nguồn:** [SRC-05](SOURCE_OF_TRUTH.md#src-05), [SRC-22](SOURCE_OF_TRUTH.md#src-22)

<a id="adr-p048"></a>
### ADR-P048 — Legal/tax treatment

**Status: TBD**

Pháp nhân, hợp đồng, payment regulation, invoice, thuế/khấu trừ, privacy và gross/net cần xác minh độc lập.

**Ranh giới:** legal-validation-required. Không đưa 7%, các ngưỡng thuế hoặc luật trong chat thành rule.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-19](SOURCE_OF_TRUTH.md#src-19)

<a id="adr-p049"></a>
### ADR-P049 — V0 implementation boundary

**Status: TBD**

Foundation ghi conceptual scope; chưa phải danh sách tính năng V0/acceptance criteria đã freeze.

**Ranh giới:** Không tự coi toàn bộ actor/capability vision là must-build V0.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p050"></a>
### ADR-P050 — Old Managed-as-core

**Status: SUPERSEDED**

Mô hình Listed/Verified/Managed như ba nhánh core không còn hiệu lực cho foundation hiện tại.

**Ranh giới:** Thay bởi ADR-P003; lịch sử Managed không bị xóa.

**Nguồn:** [SRC-08](SOURCE_OF_TRUTH.md#src-08), [SRC-18](SOURCE_OF_TRUTH.md#src-18)

<a id="adr-p051"></a>
### ADR-P051 — 30/70 là payment foundation

**Status: SUPERSEDED**

30% về Stayora, 70% Owner nhận trực tiếp không còn là payment foundation mặc định.

**Ranh giới:** Thay bằng ADR-P037 WORKING MODEL, không biến model mới thành legally confirmed.

**Nguồn:** [SRC-10](SOURCE_OF_TRUTH.md#src-10), [SRC-19](SOURCE_OF_TRUTH.md#src-19), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p052"></a>
### ADR-P052 — Request giữ đêm theo Airbnb reference

**Status: SUPERSEDED**

Không áp giữ inventory ngay khi request từ baseline tham khảo Airbnb.

**Ranh giới:** Thay bởi ADR-P013 và ADR-P014.

**Nguồn:** [SRC-10](SOURCE_OF_TRUTH.md#src-10), [SRC-22](SOURCE_OF_TRUTH.md#src-22)

<a id="adr-p053"></a>
### ADR-P053 — BQL/floor bắt buộc điều khiển giá

**Status: SUPERSEDED**

Giả định BQL định giá và floor là cơ chế core bị loại khỏi baseline hiện hành.

**Ranh giới:** Thay bởi ADR-P035; BDD proposal cũng đã parked, chưa có quyền giá tập thể được duyệt.

**Nguồn:** [SRC-07](SOURCE_OF_TRUTH.md#src-07)

<a id="adr-p054"></a>
### ADR-P054 — Tách account cố định theo actor

**Status: SUPERSEDED**

Không sử dụng Guest/Sale/Owner/Butler như các account type loại trừ nhau.

**Ranh giới:** Thay bởi ADR-P006; đây là model bị loại, không khẳng định từng được founder duyệt.

**Nguồn:** [SRC-25](SOURCE_OF_TRUTH.md#src-25), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p055"></a>
### ADR-P055 — 5% incentive cố định

**Status: SUPERSEDED**

Không dùng 5% quỹ incentive cũ như requirement mặc định trong foundation hiện hành.

**Ranh giới:** Reopened thành ADR-P039 working ~2%; không tuyên bố 2% là chính sách final.

**Nguồn:** [SRC-12](SOURCE_OF_TRUTH.md#src-12), [SRC-19](SOURCE_OF_TRUTH.md#src-19), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p056"></a>
### ADR-P056 — Affiliate cộng thêm pool độc lập mặc định

**Status: SUPERSEDED**

Đề xuất assistant trả Affiliate như pool cộng thêm không là baseline hiện hành.

**Ranh giới:** Thay bởi ADR-P040 WORKING MODEL; không coi shared pool đã chốt tỷ lệ.

**Nguồn:** [SRC-16](SOURCE_OF_TRUTH.md#src-16)

<a id="adr-p057"></a>
### ADR-P057 — Stayora 2.0 là source of truth

**Status: SUPERSEDED**

Không dùng architecture/spec/implementation cũ để quyết định sản phẩm mới.

**Ranh giới:** Grok cũng reference only; adopt lại cần quyết định rõ.

**Nguồn:** [SRC-00](SOURCE_OF_TRUTH.md#src-00), [SRC-09](SOURCE_OF_TRUTH.md#src-09), [SRC-29](SOURCE_OF_TRUTH.md#src-29)

<a id="adr-p058"></a>
### ADR-P058 — Payout ở confirmation/check-in

**Status: SUPERSEDED**

Các lựa chọn payout trước hoặc khi check-in đã nhường chỗ cho quyết định sau completed stay.

**Ranh giới:** Thay bởi ADR-P021; exception finance treatment vẫn TBD.

**Nguồn:** [SRC-24](SOURCE_OF_TRUTH.md#src-24)

<a id="adr-p059"></a>
### ADR-P059 — Direct price premium over Sale

**Status: SUPERSEDED**

The previous concept that Direct Guest/public price is 5–10% higher than Sale price is superseded by ADR-P041 One Public Price. It remains historical context only.

**Ranh giới:** This does not decide discount limits, funded promotions, stacking or attribution mechanics.

**Nguồn:** [SRC-13](SOURCE_OF_TRUTH.md#src-13), [SRC-00](SOURCE_OF_TRUTH.md#src-00)

<a id="adr-p060"></a>
### ADR-P060 — Required Payment Condition

**Status: CONFIRMED**

Booking Confirmation requires satisfaction of applicable Booking Confirmation Conditions. Required Payment Condition is one such condition and does not necessarily mean 100% payment. Payment Received ≠ Booking Confirmed and Payment Received ≠ Fully Paid. No universal payment percentage is defined in Stayora Core.

**Ranh giới:** Payment Session / Attempt thuộc Money; Temporary Inventory Commitment thuộc Inventory. Exact conditions and policy remain scoped below.

<a id="adr-p061"></a>
### ADR-P061 — Oceanami Pilot Booking Payment Policy v0.1

**Status: CONFIRMED** — Oceanami Pilot policy; not a global Stayora invariant.

For bookings created more than 24 hours before scheduled Check-in: Initial Payment = 50%; satisfying that Required Payment Condition may allow Booking Confirmation when other conditions are met; Remaining Balance = 50%, due at T-24h. At or within 24 hours: no partial/deposit confirmation path; 100% payment is required for the Required Payment Condition. Material Total Price, payments, deadline, consequences and Change/Cancellation/No-show Policy require explicit auditable consent/policy snapshot. T-48h is Payment Assurance; T-24h is a Commercial Commitment Checkpoint. Butler is not primary debt collector. Payment Default excludes unresolved provider/payment UNKNOWN and remains legal-validation-required/TBD in exact wording.

<a id="adr-p062"></a>
### ADR-P062 — Inventory Availability derived truth

**Status: CONFIRMED**

Inventory Availability is derived truth computed from effective Inventory Commitments over a Bookable Unit + time range. AVAILABLE/HELD/BOOKED/BLOCKED are availability semantics/projections, not a frozen persisted lifecycle enum.

<a id="adr-p063"></a>
### ADR-P063 — Inventory Commitment umbrella

**Status: CONFIRMED**

Inventory Commitment is the umbrella for Temporary Exclusive Commitment, Confirmed Accommodation Commitment and Availability Block. Request, Lead, Offer and Stay are not Inventory Commitments. Conceptual exclusivity semantics may be NON_EXCLUSIVE, TEMPORARY_EXCLUSIVE or EXCLUSIVE; these are not technical enums.

<a id="adr-p064"></a>
### ADR-P064 — Physical absence ≠ Inventory Release

**Status: CONFIRMED**

Inventory Release requires an authoritative end of the applicable Inventory Commitment. Late arrival, no arrival yet, lack of Check-in or a No-show observation does not by itself release Inventory while a valid accommodation right remains.

<a id="adr-p065"></a>
### ADR-P065 — Payment Default ≠ No-show

**Status: CONFIRMED**

Payment Default concerns a policy determination that an applicable due Payment Obligation remains unsatisfied after its deadline and applicable reconciliation/grace conditions. Required Payment Condition is only a condition for a specific commercial action such as Booking Confirmation; it does not represent all future Payment Obligations. No-show/no-arrival concerns operational non-use. No-show does not automatically terminate a valid accommodation right, create Payment Default or mark Stay COMPLETED.

<a id="contradiction-audit"></a>
## Contradiction audit

| ID | Hai vế cần đối chiếu | Kết quả và cách giữ trong docs | Trạng thái |
|---|---|---|---|
| C-01 | Managed là lớp core vs founder bỏ Managed | ADR-P050 → ADR-P003. Giữ lịch sử 10% Managed, không đem sang marketplace fee. | RESOLVED |
| C-02 | 30/70 về tài khoản Stayora/Owner vs 100% facilitated collection | ADR-P051 superseded; ADR-P037 là working model mới. Ai xác nhận tiền và tài khoản nhận thực tế chưa chốt lại. | RESOLVED về loại baseline cũ; OPEN về implementation/legal |
| C-03 | Direct cao hơn Sale 5–10%; direct instant giảm 10%; assistant đề xuất public base | ADR-P041 One Public Price CONFIRMED; ADR-P059 đánh dấu public premium cũ SUPERSEDED. Discount limits, funding, stacking và implementation vẫn TBD. | RESOLVED principle; OPEN policy |
| C-04 | Founder nêu Sale 10% là rule vs summary sau gọi cả 10/3/2/5 working | ADR-P038 xác nhận 10% của Commissionable Booking Value; ~3% Affiliate, ~2% incentive, ~5% platform fee không được nâng status. | RESOLVED base; OPEN economics/policy |
| C-05 | Quỹ incentive 5% cũ vs ~2% mới | 5% không còn default requirement; ~2% chỉ working, không final. Không cộng cả hai vào economics. | RESOLVED về baseline; OPEN về mức chính thức |
| C-06 | Affiliate pool cộng độc lập vs A% và Sale 10%−A% | Đề xuất pool độc lập bị founder sửa hướng. Shared model giữ WORKING MODEL theo baseline mới; exact rate/attribution còn TBD. | RESOLVED về hướng reference; OPEN về policy |
| C-07 | Owner phải bấm accept vs Co-host có quyền | “Owner” cũ được làm rõ thành Primary Host/authorized Co-host. Sale role đơn thuần không có quyền accept. | RESOLVED |
| C-08 | Airbnb request reserve vs Stayora request không reserve | Request không reserve Inventory. Authorized acceptance có thể tạo Temporary Exclusive Inventory Commitment hữu hạn; Money độc lập xử lý Payment Session / Attempt. Hai confirmed/late payment race chưa có rule. | RESOLVED principle; OPEN concurrency policy |
| C-09 | Founder nêu 24h/+24h, offer 5–10s vs baseline cuối để timing TBD | Giữ các timing dưới WORKING MODEL; principle Sale accountable khi nhận lead là CONFIRMED. Không khóa SLA/algorithm/policy chi tiết. | RESOLVED status; OPEN policy |
| C-10 | “Money Model đã frozen” trong chat vs trạng thái artifact Foundation | Lời chốt workstream cũ không xác minh luật. Founder-confirmed history from 2026-09-18 ở cấp artifact; các status nội dung và legal/TBD vẫn giữ nguyên. | RESOLVED |
| C-11 | Identity một người/multiple roles vs Guest QR không account | Xem confirmation không yêu cầu registered account; không tự cấp mọi action cho anonymous visitor. Identity linkage/token/privacy còn TBD. | RESOLVED ở principle; OPEN access design |
| C-12 | “Các actor còn lại phải duyệt” vs assistant gợi ý Affiliate tự kích hoạt | Sale/Butler approval rõ. Không có founder decision riêng về Affiliate exception; giữ TBD, không auto-activate. | OPEN |
| C-13 | Booking = Stay và chỉ booking Stayora tạo review vs external verified stay | Tách commerce khỏi operations; external completed có evidence được reputation. Không cần dựng booking payment giả. | RESOLVED |
| C-14 | Non-refundable/non-changeable vs supplier failure/legal remedy | Ý định thương mại đã chốt; exact exception/wording chưa được quyết định/pháp lý xác minh. Không viết tuyệt đối không hoàn tiền. | OPEN policy/legal |
| C-15 | BQL có quyền giá; floor là giải pháp core | BQL ≠ BDD. Floor đã parked, không còn core mechanism. | RESOLVED |
| C-16 | Verified là luxury/managed/paid badge | Trust/quality assurance đã chốt; Owner vẫn vận hành. Không có quyết định mua badge là đạt chuẩn. | RESOLVED |
| C-17 | Thuế 7%, ngưỡng/pháp nhân trong chat vs chưa xác minh | Không dùng bất kỳ tỷ lệ hay kết luận legal cũ như current rule; đưa legal-validation-required/TBD. | OPEN external validation |
| C-18 | Oceanami rules = core; BQL đã đồng ý; mọi booking phải qua Stayora | Core/config tách; chưa có bằng chứng BQL cam kết hoặc bắt buộc commerce. External stays vẫn first-class trong operations. | RESOLVED ranh giới; OPEN partner validation |
| C-19 | Whitelist/blacklist thuộc Owner vs authority theo villa/Primary Host | ADR-P012 CONFIRMED relationship-level across Owner/Authorized Host commercial authority; exact Domain/Authority refinement remains later. | RESOLVED principle; OPEN detailed authority |
| C-20 | Settlement sau completed stay vs no-show/cancel/incident | Rule happy path rõ; không tự coi no-show là completed stay hoặc kết luận không ai có entitlement. | OPEN exception finance policy |

## Kết quả consistency review

Các nội dung triển khai chưa chốt được đưa vào [Open Questions](../01-product-foundation/13-open-questions.md), không giải trong prose. Các phần pricing/money, actor authority, inventory và reputation dùng chung decision ID để tránh mỗi chương có một rule riêng. Checklist kiểm tra cấu trúc và trạng thái được ghi tại [README](README.md#verification).

**Founder review còn cần:** C-09 và C-12 vẫn mở ở mức policy/approval; C-02/C-14/C-17/C-20 còn mở về legal/payment/exception trước khi policy hoặc implementation phụ thuộc được chốt. C-03, C-04 và C-19 đã được founder correction pass giải ở mức principle; chi tiết vẫn nằm trong các TBD tương ứng. Không yêu cầu giải hết mọi TBD để review Foundation, nhưng không được coi chúng đã biến mất.
