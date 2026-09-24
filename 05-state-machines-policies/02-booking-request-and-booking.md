# Booking Request and Booking

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

## Booking Request lifecycle

```text
PENDING → ACCEPTED → CONFLICTED
                  ↘ EXPIRED
       ↘ REJECTED
       ↘ EXPIRED
       ↘ CONFLICTED
```

`ACCEPTED` authorizes proceeding; it is not Booking Confirmed. Request does not reserve Inventory. Request expiry, Temporary Inventory Commitment expiry, and Payment Session expiry are separate. Multiple Requests may coexist while no exclusive commitment exists.

Non-accepted outcomes are distinct. `REJECTED` is the Host declining the Request. `EXPIRED` is the Request lapsing under its applicable lifecycle or expiry. `CONFLICTED` is a Request that could still have progressed but can no longer be fulfilled because a new authoritative inventory truth exists — including when another competing Request becomes Booking CONFIRMED ([ADR-P070](../00-start-here/DECISIONS.md#adr-p070)).

Acceptance may be handled exclusively or competitively per [ADR-P070](../00-start-here/DECISIONS.md#adr-p070). Only the exclusive form creates a Temporary Exclusive Commitment.

Two independent clocks apply. The Host-response deadline runs while a Request is `PENDING` and measures how long the Host has to respond. The acceptance / confirmation-response deadline runs after Commercial Acceptance, from `acceptedAt`. Expiry of either transitions the Request to `EXPIRED`, which is terminal. A Host-response deadline never extends beyond the applicable Check-in boundary ([ADR-P071](../00-start-here/DECISIONS.md#adr-p071)).

## Commercial commitment boundary

```text
Valid Offer/Terms + Valid Authority + Inventory Exclusivity Available
+ Required Payment Condition + Explicit Consent + other compliance
→ Commercial Accommodation Commitment → Booking CONFIRMED
```

`Inventory Exclusivity Available` means that, at authoritative confirmation time, no applicable Inventory truth or valid exclusive commitment prevents this Request from establishing the Commercial Accommodation Commitment. The confirming Request need not already hold a Temporary Exclusive Commitment: competitive handling can reach confirmation without one, while a valid Temporary Exclusive Commitment held by another Request cannot be bypassed. Revalidate current Inventory truth at confirmation ([ADR-P014](../00-start-here/DECISIONS.md#adr-p014), [ADR-P070](../00-start-here/DECISIONS.md#adr-p070)).

Booking begins when the commercial accommodation commitment is successfully established. Its small lifecycle is `CONFIRMED → CANCELLED`; `TERMINATED` remains a future modeling hypothesis. Do not mirror Payment, Stay, Settlement, or Payout states into Booking. A failed pre-confirmation attempt is not a cancelled Booking because no Booking existed.

Request Booking and Instant Book converge after authorization at this same commitment boundary.
