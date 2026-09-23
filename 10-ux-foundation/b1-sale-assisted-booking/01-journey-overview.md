# B1 — Sale-Assisted Booking Journey Overview

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Canonical V0 journey

The CP5 journey is:

```text
Guest contacts Sale externally
  → Sale searches actual Availability and Public Price
  → quote / discussion
  → Sale creates Booking Request
  → Host / authorized Co-host accepts or rejects
  → finite authorization and Temporary Exclusive Commitment where applicable
  → Required Payment Condition and evidence
  → Booking CONFIRMED
  → Confirmed Accommodation Commitment
  → need-to-know Butler / BQL data
  → Guest confirmation and scoped QR/link
  → arrival / check-in
  → Stay
```

The later Stay, checkout, Completion Readiness and Settlement portions are acknowledged as downstream context, but B1 stops at the Booking → Guest Stay Access handoff. They are not redesigned here.

## What the journey proves

This journey is a CP5 MUST BUILD path for **Commerce Validation**, while also protecting **Inventory Trust**, **Network Adoption** and **Destination Stay Coverage**. The journey must show that Sale can make a real attributable request against shared truth without receiving Host authority, and that a confirmed commercial path can hand off to operations without creating duplicate Booking/Stay truth.

## Canonical object chain

```text
Guest need / communication context
  → Property / Bookable Unit
  → derived Availability + Public Price
  → conceptual Offer / quote presentation
  → Booking Request (PENDING)
  → authorized decision (ACCEPTED or REJECTED)
  → Temporary Exclusive Inventory Commitment where applicable
  → Payment Obligation / Attempt + Required Payment Condition
  → Booking (CONFIRMED)
  → Confirmed Accommodation Commitment
  → Guest confirmation / scoped Stay Access
```

Lead/Lead Assignment may be present when Sale handles assigned demand, but Lead is not Request or Booking. Offer is a conceptual proposition; its ownership/lifecycle remains open. No new quote, reservation or CRM object is introduced by this journey.

## Canonical confirmation boundary

The journey reaches `Booking CONFIRMED` only when the canonical Booking Confirmation Conditions are satisfied: valid Offer/Terms, valid authority, available inventory exclusivity, applicable Required Payment Condition, explicit commercial consent and other required compliance. This statement does not select payment percentage, grace period, provider behavior, refund, cancellation or default economics.

## Explicit exclusions

This B1 document does not define Instant Book as a separate journey, direct Guest self-service, external commerce, the operational Stay lifecycle, QR field design, onboarding forms, notifications, a CRM, a quote/offer aggregate, a payment provider integration or any technical permission model.

## Upstream questions carried into B1

- Exact Offer ownership and lifecycle remain TBD.
- Lead timing/dispatch and notification timing remain WORKING MODEL/TBD.
- Inventory conflict resolution, stale/unknown availability behavior and final revalidation outcome remain policy boundaries.
- Payment `UNKNOWN`, Required Payment Condition timing, Payment Default, grace/reconciliation, refund and cancellation behavior remain open.
- Guest account/QR/privacy details remain open at the Booking → Stay Access handoff.
