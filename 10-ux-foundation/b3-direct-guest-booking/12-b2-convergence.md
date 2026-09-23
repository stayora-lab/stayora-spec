# B3 and B2 — Convergence Without Provenance Erasure

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Convergence point | B3 — Direct Guest Booking | B2 — External Booking → Stay | Preserved distinction |
|---|---|---|---|
| Inventory truth | Stayora-originated Request/confirmation can establish the relevant confirmed accommodation effect. | External report/fact may support Inventory Truth only after authority/provenance evaluation. | B3 has Stayora commerce; B2 has external commerce provenance. |
| Stay representation | Confirmed Booking may provide the Accommodation Basis for a Stay. | External Accommodation may provide the Accommodation Basis without a Stayora Booking. | Booking requirement differs; operational Stay semantics remain separate. |
| Guest access | Eligible Guest/Staying Party receives scoped confirmation/access. | Eligible external Guest/Staying Party may receive scoped access to represented Stay. | Access does not rewrite commercial origin or create authority. |
| Operations | Host/Butler/BQL consume need-to-know confirmed Stay truth. | Host/Butler/BQL consume need-to-know external Stay truth. | Operational convergence does not erase source, payment or attribution. |

## Guardrail

The existence of an operational Stay projection is not evidence that the source was a Stayora Booking. B3 must remain Stayora-originated commerce; B2 must remain External Commerce → Inventory Truth and/or Stay. Neither path is routed through the other for modeling convenience.
