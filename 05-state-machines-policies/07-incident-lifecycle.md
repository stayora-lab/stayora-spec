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
