# Incident and Resolution lifecycle

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

```text
OPEN → ASSESSING → RESOLVED → CLOSED
```

This is a conceptual case lifecycle, not a complete confirmed transition graph. RESOLVED and CLOSED are distinct: resolution records substantive handling/outcome, while closure is the later administrative end of the case. Exact closure criteria, appeals and SLA remain TBD.

Remediation/action tracking may run in parallel; do not add `ACTION_REQUIRED` as a core Incident state. Complaint/Observation ≠ Incident ≠ Finding ≠ Responsibility ≠ Consequence.

Conceptually:

```text
Incident → Finding(s) → Responsibility Attribution(s)
```

Possible downstream consequences include Money adjustment/refund, Reputation signal, Verification Review, Distribution Relationship consequence, or Platform Eligibility action. Opening an Incident or recording evidence does not assign fault or grant authority to impose consequences. Multiple responsibility attributions may exist; operational remediation may precede final responsibility. RESOLVED ≠ CLOSED. Severity/priority ≠ fault. Exact SLA and taxonomy remain **TBD**.

## V0 checkout damage / compensation

[ADR-P073](../00-start-here/DECISIONS.md#adr-p073) resolves the checkout damage/compensation case within the existing lifecycle. An assessment of DAMAGE / COMPENSATION REQUIRING RESOLUTION enters/reuses Incident and the applicable Evidence / Finding / Response / Resolution / Responsibility / downstream-consequence model in [WF-05](../04-core-workflows/05-incident-resolution.md); it does not create a parallel damage-case lifecycle.

Open Incident ≠ Stay Completion Block. Only a qualifying unresolved checkout damage/compensation Incident under [Stay Completion Policy](16-stay-completion-policy.md) blocks V0 Completion. Stay remains CHECKED_OUT while that blocker remains unresolved and may be evaluated again when no applicable blocker remains. Evidence, a Finding or an Incident alone does not automatically create downstream blocking.

The appropriately assigned Butler normally observes/records Checkout Assessment. For Oceanami V0, a Host may ordinarily receive explicit villa-scoped authority for applicable damage-resolution actions that allow this blocker to clear, subject to existing Effective Permission. Ownership or the HOST label alone grants no such authority. This is not universal Host Checkout approval, a NORMAL-assessment approval requirement or a quality-inspection role.

Resolution/responsibility determination does not deduct a Security/Damage Deposit, charge a Guest, issue a refund, alter payout or execute another Money transaction. It may make a downstream financial consequence eligible under existing Money/Settlement policy; consequence execution remains separate. The blocker is the qualifying Incident, never Villa Readiness becoming READY.

This decision leaves unrelated taxonomy, severity, SLA, appeals, closure criteria and authority for other Incident cases open; it does not freeze the complete Incident transition graph.
