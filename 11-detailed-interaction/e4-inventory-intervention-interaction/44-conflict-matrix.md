> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Conflict Matrix

| Overlap | Detect | Preserve | Handoff | Resolution |
|---|---|---|---|---|
| Block vs confirmed | yes | both bases/provenance | responsible authority | TBD |
| External vs confirmed | yes | fact/commitment distinction | reconciliation | TBD |
| Temporary vs confirmed | yes | Request/Booking history | E2/E4 context | TBD |
| Overlapping blocks | yes | actors/reasons | authorized context | TBD |
| Correction vs commitment | revalidate | original + effective truth | manual if needed | TBD |

No row creates a priority, winner, cancellation or compensation rule.

Emergency Protective Hold may overlap an existing commitment; the overlap is preserved and does not create an override or automatic cancellation.
