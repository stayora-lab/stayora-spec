> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Revalidation

Before an action that can affect Inventory truth, revalidate acting authority, Unit × Time, current commitments/blocks, accommodation facts, evidence/basis and conflict posture. A stale screen, changed relationship, overlapping commitment or changed external fact produces a safe blocked/conflict/unknown outcome.

E4 does not prescribe locks, idempotency keys or retry implementation. It requires that the second action cannot silently overwrite the first canonical result.
