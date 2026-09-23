# Converged Product Structure Map

```text
PUBLIC MARKETPLACE
└─ PRIMARY: PUB-01 Destination Discovery
   ├─ contextual destination/detail: PUB-02 Destination Detail
   ├─ object detail: PUB-03 Accommodation Detail (Property + Unit)
   ├─ contextual selection: PUB-04 Date & Availability Intent
   └─ action entry: PUB-05 Request Entry

GUEST STAY ACCESS
└─ PRIMARY SCOPED: GST-01 Stay Hub
   ├─ scoped access: GST-02 Arrival & Access
   ├─ contextual help: GST-03 Help & Operational Contact
   └─ conditional action: GST-04 Review Entry

HOST WORKSPACE
├─ PRIMARY: HST-01 Current Responsibility
├─ PRIMARY: HST-03 Requests
│  └─ detail/action: HST-04 Request Detail
├─ PRIMARY: HST-06 Bookings & Stays
│  ├─ detail: HST-05 Booking Detail
│  └─ detail: HST-07 Stay Detail & Operations
├─ PRIMARY: HST-02 Properties & Units
├─ PRIMARY/CONTEXTUAL: HST-09 Inventory Intervention
├─ CONTEXTUAL: HST-10 Incident & Inventory Exception
│  └─ coordination projection: HST-11 Operations Coordination
└─ embedded Money projection: HST-12 Money & Reconciliation

SALE WORKSPACE
├─ PRIMARY: SAL-01 Supply Discovery
├─ PRIMARY: SAL-04 Sale Activity & Outcome
│  └─ attention: SAL-06 Sale Exception
├─ contextual option: SAL-02 Option & Offer Context
├─ action entry: SAL-03 Request Entry
└─ contextual attribution: SAL-05 Attribution & Earnings Summary

BUTLER CONTEXT
└─ PRIMARY: BUT-01 Today & Assignments
   ├─ assigned Stay detail: BUT-02
   ├─ action flow: BUT-03 Check-in
   ├─ incident detail/action: BUT-04
   └─ action flow: BUT-05 Checkout

BQL CONTEXT
└─ PRIMARY: BQL-01 Operations Today
   ├─ collection: BQL-02 Stay Operations
   ├─ attention: BQL-03 Incident & Exception
   └─ contextual services: BQL-04 Access & Services

STAYORA ADMIN
├─ PRIMARY: ADM-01 Governance & Attention
│  ├─ contextual: ADM-02 Property & Verification
│  ├─ exception: ADM-03 Inventory & External
│  ├─ exception: ADM-04 Incident Governance
│  └─ exception: ADM-05 Money Exceptions
└─ PRIMARY/SECONDARY: ADM-06 Audit & Provenance
```

This is a structural map, not a final sitemap or route list.
