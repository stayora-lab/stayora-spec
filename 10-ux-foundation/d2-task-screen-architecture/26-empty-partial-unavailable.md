# Empty / Partial / Unavailable Conditions

| Condition | Meaning | Example structural response |
|---|---|---|
| NO DATA | Scope exists but collection is empty | No Requests, no upcoming Stays |
| NO RELATIONSHIP | Actor has not established required relationship | Sale relationship pending; Butler unassigned |
| NO SCOPE | Object exists outside current resource scope | Property/Destination not in working context |
| NO AUTHORITY | Object visible for context but action cannot be taken | Owner sees Request but cannot accept without Host authority |
| PENDING | Canonical outcome not complete | onboarding/eligibility/verification pending; unpublished Property |
| CONFLICT / EXCEPTION | Canonical truth needs reconciliation | Inventory conflict, Payment `UNKNOWN`, Stay exception |
| OUT OF SCOPE | Capability intentionally excluded from V0 | CRM, workforce suite, dynamic pricing |

These conditions do not create fake objects or invented lifecycle/UI statuses. Exact copy and action affordances remain later interaction work.
