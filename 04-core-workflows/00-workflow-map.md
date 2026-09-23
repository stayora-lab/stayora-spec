# Bản đồ workflow và domain truth

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 18–26.

## Mục đích và phạm vi

Cho thấy commerce và external operations hội tụ vào Stay mà vẫn giữ authority riêng. Sơ đồ mô tả quan hệ business, không technical pipeline hoặc transaction ordering.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Commerce path — CONFIRMED conceptual architecture

```text
Identity & Authority
        ↓
Distribution
        ↓
Offer
        ↓
Booking ────────────► Money
        ↓
Inventory
        ↓
Stay ───────────────► Destination Operations
  ├─────────────────► Incident / Resolution
  └──► Completed
          ├──► Money
          ├──► Reputation
          └──► Verification
```

Sơ đồ không buộc Direct Guest phải có Sale/Affiliate; Distribution tham gia khi có relationship/attribution liên quan. Offer vẫn là conceptual object, không top-level domain mới. Inventory được kiểm tra ở commitment; mũi tên Booking → Inventory không cho Booking sở hữu Inventory Truth.

## External path — CONFIRMED

```text
External Commerce
      ├──► Inventory Truth
      └──► Stay
              ↓
       Destination Operations
              ↓
          Completed
              ↓
          Reputation (khi đủ eligibility/evidence)
```

Hai nhánh Inventory và Stay có thể được dùng và/hoặc tùy nhu cầu/điều kiện hợp lệ; không bắt buộc một Stayora Booking. External Booking là external commerce record, Inventory/Stay chỉ reference hoặc ghi tối thiểu. External path không bị ép qua Stayora Payment/Settlement.

## Các workflow

| Workflow | Điểm vào | Ranh giới kết quả |
|---|---|---|
| [WF-01](01-sale-assisted-request-booking.md) | Guest → Sale → Offer → Request | Authorized acceptance → Temporary Inventory Commitment + separate Payment Session/Attempt → Required Payment Condition + other conditions → Booking Confirmed → Stay |
| [WF-02](02-instant-book.md) | Eligible Direct Guest hoặc Sale → Offer | Host pre-authorization/policy + consent + Payment Session/Attempt + Required Payment Condition + inventory validation → Booking/Stay |
| [WF-03](03-external-booking-to-stay.md) | External Commerce | Authorized external commitment và/hoặc operational Stay; không commerce giả |
| [WF-04](04-stay-lifecycle.md) | Scheduled Stay từ các nguồn | Actual operations → Checkout → completion readiness → STAY COMPLETED hoặc policy-governed DID_NOT_OCCUR; Checkout ≠ Completed |
| [WF-05](05-incident-resolution.md) | Observation/Complaint | Evidence/response/resolution/responsibility; consequences do domain liên quan quyết định |
| [WF-06](06-completion-settlement-payout.md) | Actual Checkout → Operational Completion Readiness → STAY COMPLETED | Financial Reconciliation → Settlement → Payout; policy-driven exception eligibility remains separate |
| [WF-07](09-owner-onboarding.md) | Identity với Owner/Host intent, claim hoặc invitation | Owner và/hoặc Primary Host relationship + explicit capability grants; không publish, Verified, Inventory hay finance tự động |
| [WF-08](10-property-onboarding.md) | Property được represent (resource-first) | Destination + Bookable Unit + independent readiness outcomes; không Availability, Booking hay Stay |
| [WF-09](11-sale-onboarding.md) | Sale application, invitation hoặc Admin-assisted | Platform Eligibility + Distribution Relationship → bounded Sale Working Context; không Booking/Inventory Authority |
| [WF-10](12-butler-onboarding.md) | Butler application, invitation hoặc assignment | Platform Eligibility + scoped Butler Assignment → Butler Working Context; không commercial/Inventory/Money authority |

## Completed Stay là eligibility boundary — CONFIRMED

```text
STAY COMPLETED
  ├── Money may recognize eligible earned economics
  ├── Settlement may become eligible
  ├── Reputation may generate eligible Review Rights
  └── Verification may consume eligible signals
```

Không diễn đạt Stay completion như một thao tác tự chi tiền, tạo review và sửa Verified. Mỗi domain có rules/lifecycle riêng; “may” phụ thuộc eligibility. External completion không tự tạo commission hoặc đi vào Stayora Settlement.

`CHECKED OUT ≠ STAY COMPLETED ≠ FINANCIALLY RECONCILED ≠ SETTLED ≠ PAID`. Operational Completion Readiness thuộc Stay. Financial Reconciliation thuộc Money và thường theo sau STAY COMPLETED, nhưng policy-driven Economic Eligibility có thể mở exception path mà không tạo Completed giả.

## Truth ownership — CONFIRMED

Identity & Authority giữ Identity verification/eligibility/authority; Distribution giữ relationship/attribution basis; Booking giữ commercial snapshot; Inventory giữ availability; Stay giữ actual operational truth; Destination Operations consume Stay để vận hành; Money giữ financial ledger/execution. Incident thuộc Stay/Operations, Reputation giữ accumulated signals/Review Rights, Verification giữ Property-supply assurance.

**TBD:** Offer ownership chi tiết, Money bounded-context split và interface/implementation. Không dùng sơ đồ để tự giải. Nguồn: [Domain map](../02-domain/00-domain-map.md), [Ownership matrix](../02-domain/02-domain-ownership.md), [Foundation overview](../01-product-foundation/00-overview.md). Liên quan: [Authority model](../03-actor-authority/00-authority-model.md), [Cross-workflow invariants](07-cross-workflow-invariants.md), [Questions](08-open-workflow-questions.md).
