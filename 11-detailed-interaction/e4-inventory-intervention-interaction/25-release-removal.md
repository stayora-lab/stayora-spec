> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Release / Removal

There is no generic Delete. Depending on canonical upstream semantics, a record may be released, expired, corrected, superseded or revoked. The action preserves original provenance and establishes the effective result.

Release of a block or commitment is authorized and scoped; it does not imply Availability, Bookability, completion, checkout, settlement or cancellation unless a separate canonical rule says so. Timing remains TBD where not defined.
