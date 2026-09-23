> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Authority × Action Matrix

| Action | Guest | Host | Owner | Sale | Butler/BQL | Admin |
|---|---|---|---|---|---|---|
| Inspect | scoped | relationship | relationship | permitted supply | evidence scope | governance |
| Report evidence | scoped operational | where allowed | where allowed | no default | yes in context | yes |
| Request intervention | no default | where grant | where grant | no default | handoff only | scoped |
| Perform Block/Commitment | no | explicit grant | explicit grant | no | no default | no universal grant |
| Correct/Release | no | explicit grant | explicit grant | no | no default | scoped authorized action |

“Explicit grant” is a placeholder for upstream authority policy, not a grant created by E4.
