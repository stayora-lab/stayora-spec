# B5 — Derived Availability Mapping

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Canonical derivation

```text
Effective Inventory Commitments + Availability Blocks
        + Bookable Unit + Time Range
                    ↓
         Derived Availability projection
                    ↓
       contextual Searchability / Bookability
```

Availability is a derived result, not an independent command target. Actors act on a canonical Commitment, Block, External Accommodation fact/commitment or correction—not `available = false`.

## Intervention effects

| Intervention | Truth changed | Availability effect | What is not implied |
|---|---|---|---|
| Owner Block established | Owner Block becomes effective if authorized. | Relevant Unit × Time becomes constrained in derived projection. | Booking cancellation, conflict winner or universal unbookability. |
| Maintenance Block established | Maintenance Block becomes effective. | Relevant Unit × Time becomes constrained. | Incident blame, refund, Stay cancellation or repair workflow. |
| Temporary Commitment | Finite exclusive commitment becomes effective. | Incompatible range is constrained while valid. | Confirmed Booking or permanent block. |
| Confirmed Accommodation Commitment | Confirmed accommodation right is effective. | Relevant dates are constrained. | Stay Check-in/Completion or settlement. |
| External Commitment | External confirmed commitment effect is accepted with provenance. | Same effective Inventory effect as valid confirmed source. | Stayora Booking, commission or channel priority. |
| Block released/corrected | Effective constraint changes through authoritative history. | Projection may become Available for that range. | Universal Bookability or automatic public publication. |

Stale, conflicted or uncertain Inventory truth remains explicitly uncertain; B5 does not invent a manual override or freshness threshold.
