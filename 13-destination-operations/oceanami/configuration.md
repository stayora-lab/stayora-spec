# Oceanami Pilot Configuration

> Destination: **Oceanami**
> Status: **CONFIRMED — Oceanami Pilot configuration; NOT a global Stayora invariant**
> Decision source: [ADR-P061](../../00-start-here/DECISIONS.md#adr-p061)

This file is the single operative record of Oceanami pilot configuration values.

## Rule

These values are transcribed from [ADR-P061](../../00-start-here/DECISIONS.md#adr-p061) v0.1. They may not be changed here. A change requires a new or amended ADR, and this file is updated in the same change-set. If this file and ADR-P061 ever disagree, ADR-P061 governs and the discrepancy is a defect to be reported.

## Configuration

| Parameter | Applies when | Value |
|---|---|---|
| Initial Payment | Booking created more than 24 hours before scheduled Check-in | 50% |
| Remaining Balance | Booking created more than 24 hours before scheduled Check-in | 50%, due at T-24h before scheduled Check-in |
| Required Payment Condition | Booking created at or within 24 hours before scheduled Check-in | 100%; no partial/deposit confirmation path |
| T-48h | Before scheduled Check-in | Pre-arrival / Payment Assurance |
| T-24h | Before scheduled Check-in | Commercial Commitment Checkpoint |

## Open

Not configuration values; they remain open and are not restated here:

- Policy evaluation timestamp for the 24-hour boundary — see [Open Policy Questions](../../05-state-machines-policies/22-open-policy-questions.md), item 14, and the TBD — FOUNDER DECISION paragraph in [Oceanami Pilot](../../01-product-foundation/10-oceanami-pilot.md#oceanami-pilot-booking-payment-policy-v01).
- Temporary Exclusive Commitment duration — see [Open Policy Questions](../../05-state-machines-policies/22-open-policy-questions.md), item 13.

## Operational note

Butler is not the primary debt collector. Operational responsibility stays as recorded in [ADR-P061](../../00-start-here/DECISIONS.md#adr-p061) and in [Oceanami Pilot](../../01-product-foundation/10-oceanami-pilot.md#oceanami-pilot-booking-payment-policy-v01).
