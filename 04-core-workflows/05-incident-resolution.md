# WF-05 — Incident → Resolution

> Status: **REOPENED FOR RECONCILIATION — 2026-09-18**  
> Checkpoint 3 — Documentation Pass · 2026-09-18  
> Nguồn quyết định bổ sung: yêu cầu Founder “STAYORA — CHECKPOINT 3 DOCUMENTATION PASS”, mục 22, 24, 26–27.

## Mục đích và phạm vi

Giữ riêng việc ghi nhận vấn đề, phản hồi, giải quyết và attribution trách nhiệm. Incident/Resolution là supporting capability thuộc Stay/Operations, chưa là top-level domain.

**Cách đọc status:** CONFIRMED chỉ áp dụng cho principle được nêu rõ trong nguồn. TBD / WORKING MODEL được ghi riêng tại nơi sử dụng; checkpoint đang được reconciliation, nhưng các TBD/WORKING MODEL nội dung vẫn giữ nguyên.

## Purpose

**CONFIRMED:** Incident ghi nhận problem/event và evidence để xử lý có trách nhiệm. Incident tự nó chưa kết luận fault hoặc cho phép áp hậu quả tài chính/reputation.

## Actors

Guest/người quan sát, operational actor/Butler/Destination Staff có relationship liên quan; Host/authorized responder và Stayora functional staff trong scope. Money, Reputation, Verification là possible consumers. Exact response/resolution/responsibility decision authority theo loại case **TBD**.

## Preconditions

Có observation/complaint liên quan Stay/Operations; việc ghi evidence và xử lý phải theo authority/context hợp lệ. Chưa cần kết luận ai có lỗi để ghi Incident.

## Trigger

Observation hoặc complaint về sự cố, dịch vụ hoặc damage.

## Happy Path — CONFIRMED

```text
Observation / Complaint → Incident → Evidence → Response
→ Resolution → Responsibility → eligible downstream consequences
```

1. Ghi vấn đề và context/evidence; chưa quy lỗi mặc định cho một actor.
2. Response ghi việc phản hồi; Response ≠ Resolution.
3. Resolution và responsibility được xử lý theo authority/policy phù hợp còn cần chi tiết. Responsibility có thể theo dimension, không ép một universal guilty actor.
4. Eligible downstream consequences được domain sở hữu xem xét/thực hiện theo rule riêng. Money sở hữu financial recording/execution; Reputation sở hữu reputation; Verification có thể review theo signal.

## Alternative Paths

**CONFIRMED:** Guest remediation ≠ ultimate economic responsibility. Có thể cần phân biệt việc xử lý trải nghiệm Guest với bên cuối cùng chịu chi phí; nguồn không chốt ai ứng tiền hay cơ chế truy đòi. Guest Review ≠ Operational Performance Signal; không chuyển mọi operational report thành public review.

## Failure Paths

Chưa đủ evidence không tự quy lỗi hoặc tự trừ tiền/rating. Incident không trực tiếp sửa Verified status. Chỉ qualifying unresolved exceptions có thể block Stay completion; exact taxonomy/severity, blocker list, dispute handling, escalation và appeals **TBD**. Không dùng mọi Incident như lý do mặc định giữ payout/completion.

## Authority

Operational actor có thể record evidence trong scope nhưng không từ đó nhận authority impose financial/reputation consequence. Staff vẫn phải có function/domain/resource authority và giữ actual identity. Kết luận responsibility và financial action cần authority riêng; chi tiết phân công chưa được duyệt.

## Domain Truth Changes

Incident/Resolution thuộc Stay/Operations giữ case/evidence/response/resolution. Money consume eligible outcomes để ghi/thực thi adjustment; Reputation consume eligible signal theo policy riêng; Verification có thể mở review, không bị Incident rewrite status. Domain consume truth, không sở hữu thay truth đó.

## Money Changes

**CONFIRMED:** financial consequence do Money execution/recording, giữ amount, beneficiary và funding source. Remediation không tự xác định ultimate economic responsibility. Damage evidence không tự khấu trừ Security/Damage Deposit. Refund/claim rules, funding/approval và percentages **TBD**.

## Notifications

**TBD:** ai nhận complaint/response/resolution, severity escalation, timing/channel và visibility case. Không đặt response SLA hoặc publicize fault trước decision hợp lệ.

## Audit Events

Trace observation/source, reporter/capacity, evidence, response, resolution, responsibility theo dimension, authority/reason và downstream decision/financial funding attribution khi đủ điều kiện. Danh mục là business milestones; exact evidence retention/privacy là **TBD · legal-validation-required** khi liên quan.

## Invariants

Incident ≠ Fault; Response ≠ Resolution; responsibility có dimension; evidence không financial authority; Money sở hữu consequences execution/attribution; Guest Review ≠ Operational Performance Signal; Incident không trực tiếp đổi Verified/Reputation; remediation khác ultimate economics; chỉ qualifying exceptions block completion; không domain Incident mới.

## Open Questions

Taxonomy/severity, resolution authority, qualifying blockers, appeals, damages/compensation và partial settlement trong dispute: **TBD**. Nguồn: [Foundation Trust](../01-product-foundation/08-trust-verified-reputation.md), [Domain Ownership](../02-domain/02-domain-ownership.md), [Authority capabilities](../03-actor-authority/02-authority-capabilities.md), [WF-06](06-completion-settlement-payout.md), [Workflow questions](08-open-workflow-questions.md).
