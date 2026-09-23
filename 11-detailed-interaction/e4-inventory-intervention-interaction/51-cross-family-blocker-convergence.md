> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Cross-Family Blocker Convergence

The table below is the historical E4 blocker snapshot from draft authoring. Current status is reconciled by FD-01 → FD-19: the listed architecture blockers are closed; remaining policy/configuration detail is tracked in the Founder reconciliation register.

| Blocker | First appeared | E units | Severity | Recurrence | What continues | What cannot finalize |
|---|---|---|---|---|---|---|
| Payment/confirmation conditions | E1/E2 | E2/E4 | C | CROSS-JOURNEY | Inventory handoff | exact confirmation consequence |
| Guest credentials/privacy | E1/E2 | E2/E3 | C | CROSS-JOURNEY | scoped projections | credential lifecycle/fields |
| Inventory conflict resolution | E1/E2 | E2/E3/E4 | C | CROSS-JOURNEY | detection/representation | winner/remediation |
| Inventory authority grants | E1/E3 | E2/E3/E4 | C | CROSS-JOURNEY | context checks | actor action grants |
| Check-in/Checkout grants | E3 | E3/E4 | B | LOCAL | handoff | exact grants |
| Completion/DID_NOT_OCCUR | E3 | E3/E4 | B | LOCAL | evaluation boundary | no-show effects |
| Sale economics | E1/E2 | E2/E4 | C | CROSS-JOURNEY | supply projection | economics detail |
| Admin/BQL grants | E1/E3 | E3/E4 | C | CROSS-JOURNEY | scoped views | universal/admin authority |
| Attention semantics | E1 | E1–E4 | C | MULTI-FAMILY | projection | acknowledgement/priority policy |
| Request expiry/withdrawal | E2 | E2/E4 | B | LOCAL | pending path | timing/effect |
| External reconciliation | E1/E2/E3 | E3/E4 | C | CROSS-JOURNEY | facts/handoff | automatic reconciliation |
| Correction/retention | E1 | E1–E4 | C | MULTI-FAMILY | provenance | retention duration |
| Connectivity/offline | E1/E3 | E3/E4 | B | LOCAL | online confirmation | offline contract |

Severity remains evidence-based: A = not an E blocker, B = local/journey blocker, C = cross-family blocker, D = potential CP8 exit blocker. Recurrence is recorded as LOCAL, MULTI-FAMILY or CROSS-JOURNEY; recurrence alone does not upgrade severity. No current E4 item is declared D.
