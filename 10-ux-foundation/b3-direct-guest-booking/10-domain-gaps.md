# B3 — Domain, Workflow and Authority Gap Findings

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Classification | Observed need | Existing canonical concept | Why insufficient for B3 | Affected phase/actors | Impact | Recommended escalation |
|---|---|---|---|---|---|---|
| WORKFLOW GAP | Guest must continue without an account/session continuity. | Guest person/party, Account boundary, Request/Booking/Stay. | Recovery and continuity outcomes are not fully specified. | F/K · Guest/Payer | Guest may lose access or expose wrong data. | Decide interaction/security policy later; do not add an account aggregate here. |
| AUTHORITY GAP | Direct Guest can create a Request, while Host must decide. | Request-creation capability and Booking Authority. | Exact actor/context basis for accountless creation and delegated representation is open. | F/G · Guest/Host/Co-host | Unauthorized or untraceable requests are possible. | Reconcile capability and representation policy in CP3/CP4 policy maintenance. |
| POLICY GAP | Searchable, Available and Bookable produce different outcomes. | CP8-A language and Inventory truth. | Actor-specific eligibility and disclosure are not fully operationalized. | B/D/E · Guest/Marketplace | UX may promise an action that policy blocks. | Define policy/projection rules later; keep terms separate. |
| POLICY GAP | Payment can be successful while confirmation remains blocked. | Payment Attempt and Confirmation Conditions. | Amount/deadline/grace/reconciliation/default remain open. | I/J · Guest/Payer/Money | Incorrect confirmation or refund behavior. | Founder/legal/payment policy decision; no B3 economics. |
| DOMAIN GAP | No single object represents “Guest intent before Request.” | Intent is an interaction condition, not a new domain object. | Product analysis needs the distinction, but architecture should not invent an entity. | E · Guest | Risk of treating intent as Booking/hold. | Preserve as journey concept only. |
| AUTHORITY GAP | Operations need confirmed accommodation truth without commercial power. | Stay, assignments, function/destination scope. | Exact projections/access fields remain incomplete. | K/L · Butler/BQL/Host | Overexposure or accidental authority. | Resolve in later Stay Operations/access policy; no B4 work here. |
| WORKFLOW GAP | Direct path converges with B1 at confirmation. | Shared Request/Inventory/Payment/Booking/Stay truth. | Exact source/provenance projection is not fully standardized. | All · Guest/Sale/Host | Attribution or disclosure drift. | Use B1/B3 comparison and maintain explicit source provenance. |
| V0-SCOPE GAP | Optional Instant Book could be mistaken for direct default. | CP4 optional controlled branch. | B3 does not define eligibility or implementation. | G–J · Guest/Host | Scope expansion and authority bypass. | Keep as later policy branch; no V0 MUST claim. |

These are escalation points, not newly proposed domain concepts, states, screens or permissions.
