# STAYORA PRODUCT FOUNDATION — REOPENED FOR RECONCILIATION — 2026-09-18

> Checkpoint 1 — Stayora Product Foundation v1  
> Document status: **REOPENED FOR RECONCILIATION — 2026-09-18**
> Biên soạn: 2026-09-18 · Decision owner: Founder  
> Decision status: theo từng mục; trạng thái tài liệu không thay thế trạng thái quyết định.  
> Review status: **REOPENED FOR RECONCILIATION — 2026-09-18**.

**CURRENT POSITION: CP8-G READY FOR FOUNDER / PRODUCT ARCHITECT VALIDATION — CP8-H NOT STARTED**  
CP1–CP4 remain documented/reconciled with checkpoint-specific review status; CP5–CP7 are documented at their evidence-backed architecture statuses below. CP8-A, CP8-B1 through B5 and CP8-C1 through C4 are accepted baselines; CP8-D1 through D3 are complete baselines; CP8-E1 through E4 are CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE. CP8-F1 Thin Design System Foundation accepted; CP8-F2 accepted; CP8-F is complete/accepted; CP8-G is ready for Founder/Product Architect validation; CP8-H and implementation have not started. No Founder Freeze is inferred from documentation completion.

**Bản bàn giao đang được reconciliation — 2026-09-18.** Canonical workspace hiện gồm CP1–CP7, trong đó CP7 có Conceptual Data Model và supporting Persistence Direction. Reconciliation/contradiction audit nằm trong DECISIONS; nguồn và giới hạn nằm trong SOURCE_OF_TRUTH. Các TBD/WORKING MODEL/HYPOTHESIS vẫn giữ nguyên status nội dung.

## Checkpoint status hiện hành

| Checkpoint | Evidence-backed status |
|---|---|
| CP1 — Product Foundation | Reopened for reconciliation; Founder review/freeze history is preserved at artifact scope, not re-declared globally here |
| CP2 — Domain Map + Glossary | Reopened for reconciliation; documentation complete, checkpoint-specific review remains required |
| CP3 — Actor Authority + Core Workflows | Reopened for reconciliation; documentation complete, checkpoint-specific review remains required |
| CP4 — State Machines + Policies | Reopened for reconciliation; draft awaiting Sol / Founder review |
| CP5 — Oceanami V0 Scope | Stable — documented; not Founder Freeze |
| CP6 — Information Architecture | Stable — architecture reviewed; not implementation freeze |
| CP7 — Data Model | Stable — architecture reviewed; includes Conceptual Data Model and supporting Persistence Architecture; not implementation freeze |
| CP8 — UX / Design System | CP8-A through D complete; CP8-E1 through E4 CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE; CP8-F1 accepted; CP8-F2 accepted; CP8-F COMPLETE / ACCEPTED; CP8-G ready for Founder/Product Architect validation; CP8-H not started |

This status table records documentation and review evidence. It does not grant Founder Freeze to any checkpoint.

Stayora là marketplace và operating network cho các destination lưu trú có nguồn cung phân mảnh. Oceanami là beachhead. Marketplace mở, Sale giữ vai trò trọng tâm, Destination là first-class domain; Managed nằm ngoài current core. Inventory/stay operations có thể phản ánh booking từ ngoài Stayora, không cần đợi chiếm commerce mới tạo giá trị vận hành.

## Đọc theo thứ tự

1. [Source of Truth](SOURCE_OF_TRUTH.md): authority, provenance, giới hạn nguồn và quy tắc thay đổi.
2. [Glossary](GLOSSARY.md): Owner/Primary Host, booking/stay, Inventory Commitment, payment session/deposit, Verified/reputation.
3. [Decisions](DECISIONS.md): 59 ADR và [20 mục contradiction audit](DECISIONS.md#contradiction-audit).
4. [Overview](../01-product-foundation/00-overview.md), rồi các chương theo nhu cầu.
5. [Open Questions](../01-product-foundation/13-open-questions.md): 24 câu hỏi còn mở, ưu tiên founder review.
6. [Checkpoint 4 — State Machines, Lifecycles & Policy Architecture](../05-state-machines-policies/README.md).
7. [Checkpoint 5 — Oceanami V0 Scope](../06-v0-scope/README.md).
8. [Checkpoint 6 — Information Architecture](../07-information-architecture/README.md).
9. [Checkpoint 7 — Conceptual Data Model](../08-conceptual-data-model/README.md).
10. [CP7 supporting persistence architecture](../09-database-design/README.md); CP8-D1 through D3 are accepted baselines; CP8-E1 through E4 are CLOSED / ACCEPTED; [CP8-F1](../10-ux-foundation/f1-thin-design-system-foundation/README.md) accepted; [CP8-F2](../10-ux-foundation/f2-prototype-ready-design-language/README.md) accepted; see the [CP8-F closure report](../10-ux-foundation/f2-prototype-ready-design-language/CP8-F2-FINAL-RECONCILIATION-CLOSURE-REPORT.md).
11. [CP8 UX Foundation and Critical Journeys](../10-ux-foundation/README.md); CP8-E is closed; [CP8-F1 Thin Design System Foundation](../10-ux-foundation/f1-thin-design-system-foundation/README.md) accepted; [CP8-F2](../10-ux-foundation/f2-prototype-ready-design-language/README.md) accepted; [CP8-F](../10-ux-foundation/f2-prototype-ready-design-language/CP8-F2-FINAL-RECONCILIATION-CLOSURE-REPORT.md) complete/accepted; CP8-G is ready for Founder/Product Architect validation; CP8-H remains not started.
12. [CP8-G Prototype & Validation](../12-prototype-validation/README.md) is ready for Founder/Product Architect validation.
13. [CP8-E1–E4 Detailed Interaction](../11-detailed-interaction/README.md) is CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE. See the [FD-01 → FD-19 reconciliation](../11-detailed-interaction/CP8-E-FOUNDER-DECISION-RECONCILIATION.md) and [batch report](../11-detailed-interaction/CP8-E-SOURCE-OF-TRUTH-BATCH-RECONCILIATION-REPORT.md). [CP8-F1](../10-ux-foundation/f1-thin-design-system-foundation/README.md) accepted; [CP8-F2](../10-ux-foundation/f2-prototype-ready-design-language/README.md) accepted; [CP8-F](../10-ux-foundation/f2-prototype-ready-design-language/CP8-F2-FINAL-RECONCILIATION-CLOSURE-REPORT.md) complete/accepted; CP8-G is ready for Founder/Product Architect validation; CP8-H remains not started.

## Product Foundation

| Tài liệu | Nội dung |
|---|---|
| [00-overview.md](../01-product-foundation/00-overview.md) | Overview — Stayora Product Foundation |
| [01-origin-and-problem.md](../01-product-foundation/01-origin-and-problem.md) | Origin and Problem — Oceanami |
| [02-vision.md](../01-product-foundation/02-vision.md) | Vision |
| [03-business-thesis.md](../01-product-foundation/03-business-thesis.md) | Business Thesis |
| [04-product-principles.md](../01-product-foundation/04-product-principles.md) | Product Principles |
| [05-marketplace-model.md](../01-product-foundation/05-marketplace-model.md) | Marketplace Model |
| [06-ecosystem-and-actors.md](../01-product-foundation/06-ecosystem-and-actors.md) | Ecosystem and Actors |
| [07-destination-model.md](../01-product-foundation/07-destination-model.md) | Destination Model |
| [08-trust-verified-reputation.md](../01-product-foundation/08-trust-verified-reputation.md) | Trust, Verified and Reputation |
| [09-money-model.md](../01-product-foundation/09-money-model.md) | Money Model |
| [10-oceanami-pilot.md](../01-product-foundation/10-oceanami-pilot.md) | Oceanami Pilot |
| [11-success-metrics.md](../01-product-foundation/11-success-metrics.md) | Success Metrics |
| [12-scope-boundaries.md](../01-product-foundation/12-scope-boundaries.md) | Scope Boundaries |
| [13-open-questions.md](../01-product-foundation/13-open-questions.md) | Open Questions và Founder Review |

## Những ranh giới đã giữ

- Một identity, nhiều role; Guest/Host self-onboard, Sale/Butler cần approval và relationship hợp lệ.
- Request không giữ inventory; authorized acceptance có thể tạo Temporary Inventory Commitment hữu hạn; Payment Session/Attempt thuộc Money; external confirmed có cùng inventory authority.
- Booking, Payment, Stay, Financial Reconciliation, Settlement và Payout khác nhau; Completed Stay là normal settlement eligibility boundary.
- Verified là trust/quality assurance, không luxury; external verified completed stays có thể tạo reputation.
- Financial/Guest data theo role, relationship và resource scope; BQL destination-scoped.
- 30/70 foundation, Managed-as-core và giả định từ Stayora 2.0 không được khôi phục ngầm.
- Các tỷ lệ economics, targets, policy details và legal/tax vẫn giữ đúng status; không được coi là yêu cầu đã duyệt.

## Điểm cần founder chú ý

One Public Price và Sale base commission 10% đã được founder xác nhận; discount policy, Commissionable Booking Value, lead timings, Affiliate approval và detailed Domain/Actor Authority vẫn mở. Các mục này được ghi cùng provenance và không tự chọn bên. Mô hình collection 100% là WORKING MODEL; legal/tax/invoice/accounting giữ `legal-validation-required / TBD`.

<a id="verification"></a>
## Kiểm tra artifact

Kiểm tra cấu trúc Checkpoints 1–3 trước đó đã hoàn tất; Checkpoint 4 được kiểm tra riêng trong [Checkpoint 4 README](../05-state-machines-policies/README.md). Relative links/explicit anchors, ADR IDs và question IDs được giữ không trùng; status hiện hành được ghi tại từng checkpoint.

Kết quả kiểm tra không có nghĩa các ambiguity/TBD đã giải hoặc các khẳng định pháp lý đã được xác minh. Bộ này là tài liệu Foundation, không là executable spec hoặc kết quả thử nghiệm sản phẩm.

## Bước tiếp theo

Checkpoint 5 defines the Oceanami V0 pilot boundary. It does not close unrelated TBDs or define the Information Architecture documented in Checkpoint 6.
