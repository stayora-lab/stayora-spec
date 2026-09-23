# B1–B5 Journey → Screen Trace

| Journey | Structural trace |
|---|---|
| **B1 Sale-assisted Booking** | SAL-01 supply discovery → SAL-02 option context → SAL-03 Request Entry → HST-03/04 Request decision → HST-05 Booking Detail / SAL-04 outcome → GST-01/02 Stay Access → HST-07 / BUT-01/02 / BQL-01 operations. |
| **B2 External Booking → Stay** | HST-08 authorized External Accommodation Entry → HST-09/10 Inventory/external exception projection → GST-01 Stay Hub and HST-07/BUT-02/BQL-02 operations → ADM-03 reconciliation where required. No Stayora Booking is required. |
| **B3 Direct Guest Booking** | PUB-01/02 discovery → PUB-03/04 accommodation/date intent → PUB-05 Request Entry → HST-03/04 decision → HST-05 Booking → GST-01/02 and operations. |
| **B4 Stay Operations** | HST-06 / BUT-01 upcoming Stay → HST-07 or BUT-02 preparation → BUT-03 / GST-02 arrival/check-in → BUT-02 / GST-01 in-Stay → BUT-04/HST-10/BQL-03 Incident → BUT-05 checkout → HST-07 completion handoff. |
| **B5 Inventory Intervention** | HST-10 operational evidence / HST-01 Host intent → HST-09 authorized Inventory evaluation/action → PUB-04/SAL-01 derived Availability/Bookability → ADM-03 conflict exception where needed. |

The trace preserves Request ≠ Booking, Booking ≠ Stay, External Accommodation ≠ Stayora Booking and Inventory ≠ Availability.
