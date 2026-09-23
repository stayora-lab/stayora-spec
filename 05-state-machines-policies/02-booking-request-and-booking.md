# Booking Request and Booking

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

## Booking Request lifecycle

```text
PENDING → ACCEPTED
       ↘ REJECTED
       ↘ EXPIRED
       ↘ CONFLICTED
```

`ACCEPTED` authorizes proceeding; it is not Booking Confirmed. Request does not reserve Inventory. Request expiry, Temporary Inventory Commitment expiry, and Payment Session expiry are separate. Multiple Requests may coexist while no exclusive commitment exists.

## Commercial commitment boundary

```text
Valid Offer/Terms + Valid Authority + Inventory Exclusivity Available
+ Required Payment Condition + Explicit Consent + other compliance
→ Commercial Accommodation Commitment → Booking CONFIRMED
```

Booking begins when the commercial accommodation commitment is successfully established. Its small lifecycle is `CONFIRMED → CANCELLED`; `TERMINATED` remains a future modeling hypothesis. Do not mirror Payment, Stay, Settlement, or Payout states into Booking. A failed pre-confirmation attempt is not a cancelled Booking because no Booking existed.

Request Booking and Instant Book converge after authorization at this same commitment boundary.
