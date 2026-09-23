> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Checkout / Completion Boundary

Checkout and Completion do not release Inventory. Completion and Stay lifecycle events may be relevant evidence or downstream inputs, but a Unit becomes available only through canonical Inventory truth and policy.

This preserves E3: departure observation ≠ Checkout; Checkout ≠ Completion; Completion ≠ release/Availability/Bookability.
