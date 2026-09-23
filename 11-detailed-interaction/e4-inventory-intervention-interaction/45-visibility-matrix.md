> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Information Visibility Matrix

| Data | Public/Guest | Sale | Host/Owner | Butler/BQL | Admin |
|---|---|---|---|---|---|
| Derived availability/bookability | permitted | permitted supply | scoped | operational impact | governed |
| Private block reason/Owner intent | no | no | scoped | no default | scoped need-to-know |
| Guest identity | only relevant guest context | no default | relationship-scoped | assignment-scoped | governed |
| Incident evidence | impact only | no default | scoped | evidence scope | governed |
| Conflict/authority history | no | no | scoped | no default | reconciliation scope |

Financial and personal data remain role/relationship/resource scoped.
