# B5 — Inventory Intervention Journey Overview

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Purpose

B5 tests whether Stayora can protect, restrict, restore or correct Unit × Time inventory without collapsing Blocks, Commitments, External Accommodation, Booking or Stay into one mutable availability flag.

## Canonical journey

```text
Intervention need / operational fact
  → identify actor, capacity, Unit × Time and basis
  → evaluate existing effective Inventory truth
  → authorized decision
  → Owner Block / Maintenance Block / Emergency Protective Hold / Commitment / correction
  → preserve overlap and surface Inventory Conflict where incompatible
  → derive Availability from effective truth
  → project scoped result to Host, Sale, Guest, Butler, BQL, Admin
  → correct, release or expire through authoritative history
  → hand off affected Booking / External Accommodation / Stay to exception policy
```

## Protected boundaries

`Inventory Commitment ≠ Availability`, `Emergency Protective Hold ≠ Maintenance Block`, `Availability Block ≠ Availability`, `Owner Block ≠ Maintenance Block`, `Block ≠ Commitment`, `External Accommodation Fact ≠ Inventory Commitment`, `Incident ≠ Block`, `Stay ≠ Inventory Commitment`, `Conflict ≠ automatic winner`, and `Block removal ≠ universal Bookability`.

An Owner or operational report does not override existing commitments by default. A legitimate intervention preserves existing Booking, External Accommodation and Stay truth and routes the conflict to the owning exception/policy context.
