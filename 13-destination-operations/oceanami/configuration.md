# Oceanami Pilot Configuration

> Destination: **Oceanami**
> Status: **CONFIRMED — Oceanami Pilot configuration; NOT a global Stayora invariant**
> Decision sources: named in each configuration section

This file is the single operative record of Oceanami pilot configuration values.

## Rule

Each configuration section names its own decision source. Values are transcribed from that source and may not be changed here. A change requires a new or amended ADR, and this file is updated in the same change-set. If this file and the named source disagree, the source governs and the discrepancy is a defect to be reported.

## Configuration

Decision source: [ADR-P061](../../00-start-here/DECISIONS.md#adr-p061) v0.1.

| Parameter | Applies when | Value |
|---|---|---|
| Initial Payment | Booking created more than 24 hours before scheduled Check-in | 50% |
| Remaining Balance | Booking created more than 24 hours before scheduled Check-in | 50%, due at T-24h before scheduled Check-in |
| Required Payment Condition | Booking created at or within 24 hours before scheduled Check-in | 100%; no partial/deposit confirmation path |
| T-48h | Before scheduled Check-in | Pre-arrival / Payment Assurance |
| T-24h | Before scheduled Check-in | Commercial Commitment Checkpoint |

## Request deadlines

Decision source: the Founder Decision Gate of 2026-09-23 recorded in [SRC-31](../../00-start-here/SOURCE_OF_TRUTH.md#src-31). The 24-hour value is not transcribed from an ADR: [ADR-P071](../../00-start-here/DECISIONS.md#adr-p071) governs the rule, not the number, and leaves deadline values to destination configuration.

| Parameter | Applies when | Value |
|---|---|---|
| Host-response window (normal) | Request is PENDING | 24 hours |
| Near-Check-in threshold and shortened Host-response window | Request is PENDING as Check-in approaches | TBD — configurable |
| Acceptance / confirmation-response window | After Commercial Acceptance, from acceptedAt | TBD — configurable; see [Open Policy Questions](../../05-state-machines-policies/22-open-policy-questions.md), item 13 (Temporary Exclusive Commitment duration) |

The 24-hour value is a pilot default informed by common marketplace practice, and it is configurable.

## Villa Readiness

Decision source: [ADR-P072](../../00-start-here/DECISIONS.md#adr-p072) (freshness decay rule); the duration has not been set by the Founder.

| Parameter | Applies when | Value |
|---|---|---|
| Freshness decay period | Villa is READY with no guest present | TBD — configurable |

## Open

Not configuration values; they remain open and are not restated here:

- Policy evaluation timestamp for the 24-hour boundary — see [Open Policy Questions](../../05-state-machines-policies/22-open-policy-questions.md), item 14, and the TBD — FOUNDER DECISION paragraph in [Oceanami Pilot](../../01-product-foundation/10-oceanami-pilot.md#oceanami-pilot-booking-payment-policy-v01).
- Temporary Exclusive Commitment duration — see [Open Policy Questions](../../05-state-machines-policies/22-open-policy-questions.md), item 13.

## Operational note

Butler is not the primary debt collector. Operational responsibility stays as recorded in [ADR-P061](../../00-start-here/DECISIONS.md#adr-p061) and in [Oceanami Pilot](../../01-product-foundation/10-oceanami-pilot.md#oceanami-pilot-booking-payment-policy-v01).
