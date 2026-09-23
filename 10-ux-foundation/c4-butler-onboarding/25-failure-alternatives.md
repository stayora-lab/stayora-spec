# Failure and alternative paths

| Scenario | Classification / safe handling |
|---|---|
| Existing Identity or duplicate contact | **SUPPORTED:** resolve Identity/Party; matching details TBD |
| Butler claim not eligible / eligibility pending | **SUPPORTED:** no active Assignment; preserve application/provenance |
| Invitation declined | **SUPPORTED:** no Assignment/authority; expiry/retry policy TBD |
| Assignment missing or outside scope | **SUPPORTED:** no Butler context/action; route to assigner |
| Assignment expired/revoked | **SUPPORTED:** stop future actions; preserve valid history |
| Wrong Property or Stay | **SUPPORTED:** correct/supersede relationship; do not silently move history |
| Butler attempts Booking action | **SUPPORTED boundary:** deny unless separate explicit Booking Authority |
| Butler attempts Inventory mutation/Maintenance Block | **SUPPORTED boundary:** preserve report; authorized Inventory evaluation required |
| Butler reports Incident | **SUPPORTED:** record report/evidence and escalate; no automatic consequence |
| Butler attempts refund/financial consequence | **SUPPORTED boundary:** deny; Money authority required |
| Butler changes during Stay | **POLICY/WORKFLOW TBD:** preserve old/new assignment and handoff history |
| Multiple/conflicting Butlers or reports | **POLICY TBD:** preserve provenance; no invented hierarchy/winner |
| Host unavailable | **WORKFLOW/authority TBD:** do not invent reassignment or override |
| BQL escalation | **AUTHORITY TBD:** visibility alone does not grant assignment or Inventory authority |
| Guest privacy restriction | **POLICY/UX TBD:** limit projection; do not expose extra data |
| Authority changes mid-Stay | **SUPPORTED:** re-evaluate action at execution; prior valid action remains historical |
