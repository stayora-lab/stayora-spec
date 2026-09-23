> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Authority

The interaction distinguishes **CAN SEE**, **CAN REPORT EVIDENCE**, **CAN INITIATE REQUEST FOR INTERVENTION**, **CAN PERFORM INTERVENTION**, **CAN CORRECT**, **CAN RELEASE** and **AUTHORITY UNKNOWN**. The effective grant is evaluated at action time against identity, role, relationship, resource and time scope.

Ownership, Host relationship, Butler assignment, BQL visibility and Admin access each remain insufficient by themselves for unrestricted Inventory mutation.
