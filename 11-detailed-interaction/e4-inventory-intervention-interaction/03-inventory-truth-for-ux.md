> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Inventory Truth for UX

The minimum useful truth view distinguishes the relevant canonical categories. The canonical invariant is `Inventory Fact/Evidence ≠ Inventory Decision`. It must distinguish: Unit/resource, time range, current commitments and blocks, supporting facts/evidence, provenance, effective status, conflicts, stale/incomplete posture and any responsible attention. A visual “unavailable” result is a projection, not an Inventory record.

Canonical concepts remain separate: Owner Block, Maintenance Block, Emergency Protective Hold, Temporary Exclusive Commitment, Confirmed Accommodation Commitment and External-backed Commitment. Emergency Protective Hold is canonical intervention truth when the Founder-approved scoped capability and policy conditions apply. It is not a Maintenance Block and does not prove maintenance status or uninhabitability. No `AVAILABLE / UNAVAILABLE / BOOKED / BLOCKED` replacement state is introduced.
