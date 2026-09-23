# Owner Perspective Stress Test

| Scenario | Structural result | Authority boundary |
|---|---|---|
| Owner Identity only | No private Host destination; onboarding/eligibility context only | Identity ≠ relationship/authority |
| Owner + valid Property relationship, no Host authority | Property-scoped contextual view from `HST-02`; read scope only where canonical | Owner ≠ Host; no Request acceptance or Inventory mutation |
| Owner + Host authority | Host responsibility groups may appear only for effective Host capacity | Authority is relationship/resource scoped |
| Owner with legitimate economic visibility | `HST-12` projection reached from authorized Property/Booking context | Payment/Entitlement/Settlement/Payout remain separate; exact fields TBD |
| Owner Block authorized | `HST-09` action entry from Property/Inventory context | Requires explicit Owner/Inventory authority |
| Publication/representation responsibility | `HST-02`/`ADM-02` contextual path | Verification/publication authority remains policy-bound |
| Owner and Host are same Identity | Context label/capacity distinguishes acting role | Context switch does not grant permission |

**Remaining IA gap:** no separate Owner Workspace is created. The current composition is coherent for V0 if relationship-scoped projections are sufficient; a distinct Owner responsibility set would require Founder/Product Architect decision.
