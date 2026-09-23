> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Intervention Action Model

Every consequential intervention follows: `current truth → user intent/evidence → acting context → Unit × Time → authority → basis → preconditions → revalidation → intervention → canonical outcome → derived projection → provenance → handoff/attention`.

Actions are classified as inspect, report evidence, request intervention, perform intervention, correct or release. Generic Edit/Delete is not used. An action may end in blocked, conflict, unknown or manual reconciliation without fabricating success.

Emergency Protective Hold uses the same action grammar plus explicit scoped Hold capability, Unit×Time revalidation, immediate Attention/escalation and policy-defined review/expiry.
