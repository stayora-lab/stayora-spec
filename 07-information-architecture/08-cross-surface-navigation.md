# Cross-Surface and Contextual Navigation

> Status: **STABLE — CHECKPOINT 6 DOCUMENTED; NOT IMPLEMENTATION FREEZE**

Primary navigation locates responsibility; contextual navigation follows work. Users should not need to return through a generic sidebar for a legitimate lifecycle handoff, but every action remains authority-scoped.

Typical handoffs:

```text
Request → Booking *(contextual handoff between related objects; not a direct state transition. Request ≠ Booking and does not reserve Inventory. A Booking follows only through authorized acceptance, applicable temporary commitment/payment condition and Booking confirmation.)*
Booking → Stay
Booking → Payment
Booking → Guest Access
Stay → Incident
Stay → Review *(where the applicable Review Right / eligibility conditions are satisfied; not an unconditional right from Checkout or Completed alone)*
Incident → Verification Review
Incident → Adjustment
Issue → Availability Block
```

Notifications point to responsibility: new Request to Host/Request Detail; Lead assignment to Sale/Lead; Guest arrival to Butler/Stay; access exception to BQL/Access; payment exception to Admin/Payment case. They do not all land on a generic dashboard.

The same Stay can project as “my Stay” for Guest, “my property’s Stay” for Host, “customer transaction” for Sale, “my work” for Butler, destination arrival/in-house/departure for BQL and exception/governance context for Admin. Share truth, not necessarily screens. Do not create duplicate domain records or force one universal mega-detail page.

Acquisition surfaces (Stayora, Sale, OTA, Owner Direct) can converge into shared Stay truth and fulfillment by Host, Butler, BQL and Stayora. External fact reporting is not authoritative recording: a Sale may report; Host/authorized actor verifies or an explicit capability records authoritative external truth.
