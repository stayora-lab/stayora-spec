# B2 — Inventory Effect Mapping

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Inventory truth chain

```text
External Accommodation Fact
  + explicit Inventory Authority
  + compatible Bookable Unit × Time
  + accepted external commitment basis
        ↓
Inventory Commitment (external provenance retained)
        ↓
effective Inventory Commitments
        ↓
derived Availability
```

The external fact and the Inventory Commitment remain separate concepts. The fact is the source/provenance-bearing accommodation record; the commitment is the Inventory domain's effective protection of a resource/time scope.

## Distinctions

| Concept | Inventory meaning | B2 boundary |
|---|---|---|
| External Accommodation Fact | External source says an accommodation exists/was arranged. | May be pending or authoritative; not itself a commitment. |
| Owner Block | Authorized owner/hosting block prevents a Unit from being committed. | No Guest/commercial accommodation basis; not an external booking. |
| Maintenance Block | Authorized maintenance/operational block prevents commitment. | Operational restriction; not Guest accommodation or external commerce. |
| Temporary Exclusive Commitment | Finite protection after authorized Request acceptance. | Stayora commerce progression; not an external fact and not a Booking until confirmed. |
| Confirmed Stayora Accommodation Commitment | Confirmed commercial accommodation basis from Stayora Booking. | Stayora-originated commerce; distinct from external provenance. |
| External confirmed commitment | Authorized Inventory effect based on an external accommodation fact. | Equivalent inventory effect where valid; no source priority, Booking or commission. |
| Availability | Derived projection over effective commitments for Bookable Unit × Time. | Not a stored channel state and not actor-specific Bookability. |

## Conflict behavior

If an external fact/commitment overlaps a Stayora Booking, Temporary Commitment, Owner Block, Maintenance Block or another external commitment:

1. Preserve the external fact and the existing commitment/block/history.
2. Record/display an Inventory Conflict/Exception with source, time, authority and evidence where available.
3. Do not discard the external fact because it is external.
4. Do not select a channel/source winner, cancel, release or rewrite anything automatically.
5. Require authorized resolution under future policy; keep Availability/Bookability conservative while unresolved only as supported by the eventual policy, not as a new universal rule.

Late, duplicate, withdrawn or corrected information follows the same truth-preservation rule. Physical absence or no arrival does not by itself release a valid commitment.

## What B2 does not specify

No calendar UI, sync cadence, integration, conflict winner, false-unavailability rule, release grace, interval algorithm, Channel Manager or PMS behavior is defined here.
