# CP8-A — V0 UX Traceability Map

> Status: **ACCEPTED AS CP8-B BASELINE** · **NOT FROZEN**

The four validation dimensions below use the canonical CP5 wording. This map connects evidence sought in the Oceanami pilot to actor, responsibility, critical journey, surface, domain truth, authority and open policy. It does not add V0 capabilities or turn hypotheses into acceptance requirements.

| CP5 V0 validation dimension | Actor / Working Context | Responsibility / task family | Critical journey | Surface | Domain truth | Authority source | Relevant state / policy | Open question carried forward |
|---|---|---|---|---|---|---|---|---|
| **Inventory Trust** | Host / Primary Host / Co-host; Sale; Guest; Admin | Maintain and consume real Availability without repeated manual recheck; surface conflict and uncertainty. | Sale-assisted Booking; Direct Guest Booking; Availability Control; External Booking → Stay. | Host Workspace; Sale Workspace; Public Marketplace; Admin Inventory Conflicts. | Effective Inventory Commitments → derived Availability; Request does not reserve; External Accommodation may establish/reference a valid commitment. | Host/Co-host Inventory Authority; Sale demand access; Admin scoped conflict authority. | Inventory Commitment model; Request/Booking boundary; external commitment and conflict policy. | Conflict winner/resolution, sync health, late discovery and exact commitment timing remain TBD. |
| **Network Adoption** | Host; Sale; Butler; BQL/Destination Staff; supporting Admin | Return voluntarily to shared truth and complete role-appropriate work. | Sale-assisted Booking; External Booking → Stay; Incident/Exception; Availability Control. | Host; Sale; Butler; Destination/BQL; Admin. | Shared Identity/Inventory/Booking/Stay truth; contextual projections; operational participation ≠ commercial provenance. | CP3 effective permission; assignments, relationships, destination scope and platform eligibility. | Lead/Assignment, Stay Operations, Incident and manual-assisted V0 policies. | Lead timing/dispatch, Butler assignment changes, notifications and local operational configuration remain open. |
| **Destination Stay Coverage** | Host; Butler; BQL/Destination Staff; Guest; Admin | Represent actual stays from Stayora and external sources; coordinate arrival, access, Stay and checkout. | External Booking → Stay; Sale-assisted Booking; Direct Guest Booking; Incident/Exception. | Host; Guest Stay Access; Butler; Destination/BQL; Admin. | External Accommodation → Stay; Stay lifecycle; Staying Party; Access; Operational Completion Readiness; evidence/provenance. | Host/authorized recorder; Butler assignment; destination function/capability; Guest scoped relationship; Admin case authority. | Stay lifecycle; access/destination policy; Review Right eligibility; completion/readiness. | Guest QR/privacy fields, external data minimum, split stay/unit move/extension and completion exceptions remain open. |
| **Commerce Validation** | Guest; Sale; Host/authorized Co-host; supporting Admin/Butler/BQL | Discover, request, authorize, satisfy applicable payment condition, confirm Booking and complete a real Stay. | Sale-assisted Booking; Direct Guest Booking; optional controlled Instant Book. | Public Marketplace; Sale; Host; Guest Stay Access; Admin Money/Settlement. | Request → authorized acceptance → applicable commitment/payment condition → Booking `CONFIRMED` → Stay; Payment, Settlement and Payout remain separate. | Host/Co-host Booking Authority; Sale eligibility/relationship for distribution; Guest consent/payment relationship; Admin manual assistance. | Booking Request/Booking lifecycle; Required Payment Condition; Payment Attempt `UNKNOWN`; settlement after Completed Stay normal path. | Exact payment timing, discount/cancellation/default/refund economics, Instant Book policy and authority edge cases remain open. |

## Traceability use

Later journey work should be able to start from a row above and follow:

```text
V0 thesis → context responsibility → critical journey → surface
→ canonical object/lifecycle → authority → unresolved policy
```

If a proposed interaction cannot map to one of the four dimensions, a CP5 MUST BUILD/MANUAL-ASSISTED integrity capability, or a documented prerequisite, it should not be added to V0 UX by assumption.

## Source trail

- [CP5 V0 success thesis](../06-v0-scope/01-v0-success-thesis.md)
- [CP5 critical journeys](../06-v0-scope/03-critical-journeys.md)
- [CP5 capability matrix](../06-v0-scope/04-capability-matrix.md)
- [CP5 pilot metrics](../06-v0-scope/06-pilot-metrics.md)
- [CP6 surface architecture](../07-information-architecture/01-surface-architecture.md)
- [CP6 journey validation](../07-information-architecture/10-journey-validation.md)
