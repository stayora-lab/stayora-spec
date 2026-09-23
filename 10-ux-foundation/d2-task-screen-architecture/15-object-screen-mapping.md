# Object → Screen Mapping

| Canonical object/projection | Primary detail/home | Secondary projections | Surfaces | Dedicated detail? |
|---|---|---|---|---|
| Destination | PUB-02 | PUB-01, BQL-01/04, ADM-02 | Public/BQL/Admin | Yes for proposition/context |
| Property | HST-02 | PUB-03, GST-01/02, BQL-01, ADM-02 | Host/Public/Guest/BQL/Admin | Yes |
| Bookable Unit | HST-02 | PUB-03, GST-01/02, SAL-01/02 | Host/Public/Guest/Sale | Contextual with Property in V0 |
| Booking Request | HST-04 | HST-03, SAL-03/04, ADM attention | Host/Sale/Admin | Yes |
| Booking | HST-05 | GST-01, SAL-04, ADM exceptions | Host/Guest/Sale/Admin | Yes; separate from Request/Stay |
| External Accommodation | HST-08 | HST-10, ADM-03, GST-01/BQL-02 via Stay | Host/Admin/Operations/Guest | Entry plus exception detail; not Stayora Booking |
| Stay | GST-01 | HST-07, BUT-02/03/05, BQL-02, ADM-04 | Guest/Host/Butler/BQL/Admin | Yes |
| Inventory Commitment/Block projection | HST-09 | HST-01/03/10, PUB-04, SAL-01 | Host/Public/Sale/Admin | Intervention concept; Inventory remains derived |
| Incident/Finding | HST-10 | BUT-04, BQL-03, ADM-04 | Host/Butler/BQL/Admin | Yes where consequence/evidence needed |
| Payment truth | HST-12 | HST-04/05, SAL-05, ADM-05, GST limited | Host/Sale/Admin/Guest | No universal payment screen; contextual projections |
| Sale attribution | SAL-05 | SAL-04, ADM-06 | Sale/Admin | Summary only in V0 |
| Butler Assignment | BUT-01/02 | HST-11, C4 onboarding/Admin | Butler/Host/Admin | Contextual detail |

A projection cannot mutate the canonical object unless the actor has the corresponding authority.
