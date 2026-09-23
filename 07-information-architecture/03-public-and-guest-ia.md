# Public Marketplace and Guest Stay Access

> Status: **STABLE — CHECKPOINT 6 DOCUMENTED; NOT IMPLEMENTATION FREEZE**

## Public Marketplace

```text
PUBLIC
├── Home
├── Destinations
│   └── Destination
│       ├── Overview
│       ├── Villas
│       ├── Experiences / Facilities
│       └── Destination Information
├── Search Results
└── Villa Detail
    ├── Listing
    ├── Availability
    ├── Price
    ├── Trust
    ├── Request to Book
    └── Need Consultation
```

Destination is first-class, not merely a geographic filter. Marketplace and Host/Sale use the same derived Inventory Truth. Non-Verified supply remains visible when otherwise eligible. Verified is an additional trust layer; there is no universal TrustScore.

Direct Guest paths are Request to Book → Host decision → applicable payment → Booking Confirmed, or Need Consultation → Lead → Sale-assisted flow. Request does not reserve Inventory. Guest account is optional/later; it is not required to access a valid paid Stay.

## Guest Stay Access

```text
GUEST STAY ACCESS
├── Stay Overview
├── Arrival
├── Access / QR
├── Guest / Vehicle Information
├── Villa
├── Butler
├── Destination
├── Help / Issue
└── Review
```

Before arrival, show required information and access preparation; during Stay, show operational information, Butler, Destination and help; after checkout, show eligible review actions. QR/link is a scoped credential, not underlying business Authority. External Guests may receive operational access without implying Stayora-originated commerce. Operational participation does not rewrite commercial provenance.
