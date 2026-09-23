# B4 — Stay Lifecycle and Domain Mapping

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Canonical lifecycle

```text
SCHEDULED → CHECKED_IN → CHECKED_OUT → COMPLETED
SCHEDULED → DID_NOT_OCCUR
```

| Concept | Canonical treatment | B4 use |
|---|---|---|
| Accommodation Basis | Conceptual relationship: Stayora Booking or External Accommodation. | Explains why the Stay legitimately exists; does not become a new lifecycle. |
| Stay | Independent operational aggregate candidate and state machine. | Source of operational truth. |
| PREPARATION | Operational readiness phase/milestone. | May be projected without adding a Stay state. |
| READY | Operational readiness milestone, not a core Stay state. | Report readiness without adding `READY`. |
| ARRIVAL | Event/observation. | Physical arrival can be recorded without asserting Check-in. |
| CHECKED_IN | Canonical Stay state. | Requires the supported preconditions, authority and evidence. |
| IN_STAY | Not a canonical core state. | Use `CHECKED_IN` plus operational projections/events. |
| CHECKED_OUT | Canonical Stay state. | Requires authorized Checkout recording/evidence. |
| Operational Completion Readiness | Stay-owned completion evaluation. | May precede `COMPLETED`; unresolved policy remains visible. |
| COMPLETED | Canonical terminal/history state when completion conditions pass. | Does not automatically mean settlement, payout or reputation change. |
| DID_NOT_OCCUR | Pre-Check-in/final-policy outcome. | Applies only where the accommodation commitment legitimately ends without a Stay occurring. |

## Transition responsibility

The actor who reports an observation is not automatically the actor authorized to transition the Stay. Butler may coordinate/report; Host or an explicitly authorized operational context may record/confirm within scope; exact grants remain CP3/TBD. Guest arrival evidence does not self-transition a Stay.

## Domain separation

Inventory remains derived from effective Commitments and Blocks. Stay events do not create, release or rewrite Inventory unless a separate canonical Inventory action occurs. Payment state does not become a Stay state. Incident, Finding, Responsibility and Consequence remain separate models/cases.
