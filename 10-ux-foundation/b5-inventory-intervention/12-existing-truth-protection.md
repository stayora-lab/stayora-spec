# B5 — Existing Booking, External Accommodation and Stay Protection

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Protection rules

- An Inventory problem is not a Booking cancellation.
- An Inventory problem is not a Stay cancellation.
- A Maintenance Block is not a refund, compensation or relocation decision.
- An Owner Block is not Guest relocation or automatic cancellation.
- An External Accommodation fact is not deleted because a Block overlaps it.
- A confirmed Booking remains Booking truth until its own authorized lifecycle/policy changes it.
- A Stay remains Stay truth until its own authorized lifecycle/policy changes it.
- Check-in, Checkout and Completion do not directly create/release Inventory.

## Exception boundary

When an intervention affects existing Booking, External Accommodation or Stay, B5 hands off:

```text
Inventory Conflict / affected Unit × Time
  → Booking / External Accommodation / Stay exception context
  → domain-specific authorized policy decision
```

The downstream context may decide a supported commercial or operational remedy only under its own authority and policy. B5 does not invent cancellation, refund, relocation, compensation, rescheduling, Guest messaging or legal treatment.

## Provenance

Preserve the intervening basis, original commitment/fact/Stay, source, actors, authority, evidence, timestamps, corrections and resolution history. An operational actor’s visibility of a Booking/Stay does not grant power to mutate it.
