> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Error / Recovery Matrix

| Condition | User-facing posture | Safe next step |
|---|---|---|
| Missing scope/basis | blocked | correct or provide evidence |
| No authority | not permitted | route to responsible capacity |
| Stale truth | stale | refresh/revalidate |
| Overlap/conflict | conflict | inspect/reconcile |
| Unknown outcome | unknown | manual reconciliation |
| Technical failure | unconfirmed | retry only after current truth check |
| Partial external data | incomplete | request/evaluate evidence |

No recovery path silently mutates Inventory or invents business consequences.
