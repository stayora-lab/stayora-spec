# Stay Completion Policy

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

Stay COMPLETED means primary operational obligations ended and no qualifying operational issue remains that must block normal financial progression. It does not mean Guest satisfaction, completed reviews, completed payout, every Incident CLOSED, or all post-stay work finished.

```text
CHECKED_OUT → Operational Completion Readiness → COMPLETED
```

Readiness may consider departure, handback evidence, operational records, and qualifying unresolved exceptions. Open Incident ≠ Completion Block; only qualifying unresolved exceptions may delay completion. Do not create `COMPLETION_BLOCKED`. Stay remains CHECKED_OUT while readiness is NOT_READY with a reason. Sufficient authoritative evidence plus Policy may permit completion. Exact automation/timing remains **TBD**. After Completed, later complaint/refund does not reopen Stay. DID_NOT_OCCUR never becomes Completed to unlock Settlement.

## Checkout Assessment — V0

**Status: CONFIRMED per ADR-P073**

Per [ADR-P073](../00-start-here/DECISIONS.md#adr-p073), authorized Checkout requires Checkout Assessment before Completion evaluation. Checkout ≠ Completion. The normal observer/recorder is the appropriately assigned Butler.

| Assessment outcome | Completion effect | Operational handling |
|---|---|---|
| NORMAL | No Completion blocker; Completion may proceed. | No Host approval is required. |
| DAMAGE / COMPENSATION REQUIRING RESOLUTION | A qualifying unresolved checkout damage/compensation Incident blocks Completion. Stay remains CHECKED_OUT while the blocker remains unresolved; re-evaluate once no applicable Completion blocker remains. | Enter/reuse the existing [Incident lifecycle](07-incident-lifecycle.md) and its applicable Evidence / Finding / Response / Resolution / Responsibility model. |
| ENHANCED CLEANING REQUIRED | No Completion blocker. | Create a structured operational indication associated with the [Villa Readiness workflow](23-villa-readiness-lifecycle.md); no additional readiness state. |

This is the minimum complete V0 catalogue, not a universal catalogue for future versions. V0 must not invent additional Completion blockers; future blocker types require a future governed decision. Lost property is not a V0 Completion blocker under this decision.

Open Incident ≠ Completion Block. Evidence, a Finding or an Incident alone does not automatically create a blocker or downstream consequence; only an unresolved case explicitly qualifying under this policy blocks Completion. Incident resolution is substantive handling, distinct from administrative CLOSED; completion evaluation depends on whether an applicable blocker remains, not on every Incident being CLOSED.

## Authority and domain boundaries

For Oceanami V0, a Host may ordinarily be granted explicit, villa-scoped authority for applicable damage-resolution actions that allow the qualifying blocker to clear. Ownership ≠ Authority and the HOST label alone grants no permission. Apply the existing [Effective Permission](../03-actor-authority/05-effective-permission.md) model. This does not make Host a universal Checkout approver or introduce a quality-inspection role.

Incident resolution or responsibility determination does not deduct a Security/Damage Deposit, charge a Guest, issue a refund, alter payout or execute another Money transaction. It may make a downstream financial consequence eligible under existing [WF-05](../04-core-workflows/05-incident-resolution.md) / [WF-06](../04-core-workflows/06-completion-settlement-payout.md) policy; the financial execution boundary remains unchanged.

Stay Completion never waits for Villa Readiness to become READY. DIRTY or CLEANING is not a Completion blocker; damage waits only for the qualifying Incident blocker. Villa Readiness remains DIRTY → CLEANING → READY, independent of Stay Completion, Inventory and Availability. Enhanced cleaning does not add a fourth state.
