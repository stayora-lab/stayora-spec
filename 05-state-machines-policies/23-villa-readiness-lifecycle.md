# Villa Readiness lifecycle

> Status: **CONFIRMED — ADR-P072**
> Last reviewed: 2026-09-26

Villa Readiness is a physical state of the villa that persists across Stays. It is independent of the [Stay lifecycle](04-stay-lifecycle.md), Booking lifecycle and Payment lifecycle. The canonical decision is [ADR-P072](../00-start-here/DECISIONS.md#adr-p072).

```text
DIRTY → CLEANING → READY
                    ├─ recorded guest departure (observation or Checkout) → DIRTY
                    └─ freshness decay with no guest present → DIRTY
```

| Transition | Trigger | Acting authority |
|---|---|---|
| `DIRTY → CLEANING` | Cleaning begins | Assigned Butler, or the villa's Host recording the action when the Butler cannot operate the system |
| `CLEANING → READY` | Cleaning completes | Assigned Butler, or the villa's Host when the Butler cannot operate the system; self-attested, with no V0 inspection or approval |
| `READY → DIRTY` | Guest departure is recorded by observation or Checkout | Automatic lifecycle effect; record the departure event's actual provenance |
| `READY → DIRTY` | Configurable freshness period passes with no guest present | Automatic lifecycle effect; [Oceanami duration](../13-destination-operations/oceanami/configuration.md#villa-readiness) is TBD |

The Host may take over a CLEANING transition begun by the Butler when the Butler cannot operate the system. The Host's supporting action records the Host as the actor, never the Butler. It grants no `DIRTY → READY` shortcut. `DID_NOT_OCCUR` does not transition Villa Readiness; no physical-use departure occurred, and freshness decay continues independently.

Villa Readiness does not block Stay Completion. DIRTY and CLEANING are not blockers under [FD-02](../11-detailed-interaction/CP8-E-FOUNDER-DECISION-RECONCILIATION.md#cp8-e-founder-decision-reconciliation--fd-01--fd-19) or [ADR-P066](../00-start-here/DECISIONS.md#adr-p066); the unresolved Completion blocker catalogue is separate. Villa Readiness is not an [Availability Block (ADR-P067)](../00-start-here/DECISIONS.md#adr-p067) or an [Inventory Commitment (ADR-P063)](../00-start-here/DECISIONS.md#adr-p063), including the temporary exclusivity described in [ADR-P070](../00-start-here/DECISIONS.md#adr-p070). DIRTY or CLEANING remains an internal Host/Butler operational signal and does not remove future commercial bookability absent a later decision.

`reportPrepared` / `Stay.preparedAt` is superseded as the canonical readiness representation because it belongs to one Stay and cannot persist a villa's state or show cleaning in progress. Prototype migration is a separate task.
