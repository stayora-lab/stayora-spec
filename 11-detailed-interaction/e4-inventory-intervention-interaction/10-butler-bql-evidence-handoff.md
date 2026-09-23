> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Butler / BQL Evidence Handoff

Butler or BQL may observe, report evidence and initiate a request for Inventory evaluation where their context permits. The path is `observation → evidence/report → responsible attention → authorized Inventory evaluation`.

`Report ≠ authoritative External Fact`; operational report does not mutate Inventory; assignment or destination visibility does not grant Inventory Authority. The handoff records reporter, resource, time, evidence, responsibility context and resulting attention.
