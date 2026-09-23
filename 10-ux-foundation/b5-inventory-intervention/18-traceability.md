# B5 — V0 and Source Traceability

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| B5 claim/capability | CP5 V0 dimension | Actor/context | CP6 surface | Canonical truth | Authority/lifecycle source | B5 source |
|---|---|---|---|---|---|---|
| Inventory is commitment/block derived | Inventory Trust; Commerce | Inventory/Host/Admin | Host/Admin projections | Commitments + Blocks → derived Availability | CP4 Inventory; CP7 model | [B5-C01](02-detailed-inventory-intervention-journey.md#phase-c--existing-inventory-truth-evaluation) |
| Owner Block | Inventory Trust; Supply protection | Owner/Host/Inventory | Host/Admin | Owner Block, Unit × Time | CP3 authority; CP4 Inventory policy | [Owner Block](04-owner-block-journey.md) |
| Maintenance handoff | Inventory Trust; Destination Coverage | Butler/BQL/Guest → Inventory authority | Operations/Host/Admin | Report/Incident ≠ Maintenance Block | CP3 capability; B4 Incident | [Operational handoff](06-operational-inventory-handoff.md) |
| Maintenance Block | Inventory Trust; operational protection | Authorized Inventory/Host/Staff | Host/Admin/Operations | Maintenance Block → derived Availability | CP4/CP7 Inventory | [Maintenance Block](05-maintenance-block-journey.md) |
| Conflict preservation | Inventory Trust | Inventory/Booking/Stay exception | Host/Admin/operations projections | Conflict preserves all bases | CP4 Inventory policy | [Conflict matrix](07-overlap-conflict-matrix.md) |
| Contextual Availability | Guest Trust; Supply Adoption | Public/Sale/Guest/Host/Butler/BQL | Public, Sale, Guest, Host, Operations | Derived Availability; Bookability separate | CP8-A/B3 semantics | [Availability/Bookability](09-availability-bookability.md) |
| Existing truth protection | Commerce; Destination Coverage | Booking/External/Stay owners | Host/Guest/Operations/Admin | Booking/External/Stay remain separate | CP4/CP7/B4 | [Protection](12-existing-truth-protection.md) |
| Correction/release | Inventory Trust; auditability | Authorized basis owner/Admin | Host/Admin | Amendment/supersession/replacement/release | CP7 provenance; CP4 Inventory | [History](13-correction-release-history.md) |

## V0 boundary

B5 uses CP5 Inventory Blocks/Commitments, manual-assisted conflict/exception handling, operational evidence, Availability projections and existing Booking/External/Stay boundaries. It does not introduce a maintenance suite, PMS, Channel Manager, yield/pricing engine, CRM, automated relocation/compensation, ERP or workforce scheduling.

## Source order

Founder decisions → CP1–CP6 canonical architecture → CP7 conceptual model → accepted CP8-A/B1–B4 → supporting persistence constraints. No lower-priority source resolves a TBD.
