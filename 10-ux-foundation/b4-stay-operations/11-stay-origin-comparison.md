# B4 — Stay-Origin Comparison

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Operational concern | B1 Sale-assisted Booking | B3 Direct Guest Booking | B2 External Accommodation | Same vs origin-specific |
|---|---|---|---|---|
| Accommodation basis | Confirmed Stayora Booking. | Confirmed Stayora Booking. | Authoritative External Accommodation fact/commitment where supported. | Basis/provenance differs; Stay operations converge. |
| Stay creation | Represent Stay from confirmed accommodation. | Represent Stay from confirmed accommodation. | Represent Stay without fake Stayora Booking. | Same independent Stay concept. |
| Pre-arrival | Host/Butler/Guest preparation from Stay truth. | Same. | Same where operational data/evidence supports it. | Same need-to-know model. |
| Arrival / Check-in | Same canonical evidence and authority boundaries. | Same. | Same; external commerce does not change Stay lifecycle. | Same lifecycle; origin remains visible where needed. |
| In-stay operations | Guest support, Butler coordination, Destination/BQL. | Same. | Same. | Same operational semantics. |
| Commercial visibility | Sale provenance/economics only where legitimate and scoped. | Direct source; no fabricated Sale. | External source; no fake Booking/payment/commission. | Origin-specific projections only. |
| Incident / completion | Same Incident and completion boundaries. | Same. | Same. | Same operational truth. |
| Post-stay commerce | Separate Booking/Money/Settlement policies may consume truth. | Same. | External origin does not create Stayora settlement/payout. | Downstream commercial treatment differs. |

## Architectural conclusion

External Stay does not require a different Stay lifecycle. If a future branch requires a separate operational lifecycle solely because commerce was external, that is a domain contradiction requiring review. Differences belong to Accommodation Basis, provenance, available evidence, access/consent and downstream commercial policy.
