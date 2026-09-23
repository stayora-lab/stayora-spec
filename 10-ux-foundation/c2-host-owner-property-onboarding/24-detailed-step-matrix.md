# Detailed conceptual step matrix

This matrix is a documentation aid, not a form or data model. `TBD` means the downstream decision is not established by the canonical sources.

| ID / context | Intent and entry | Identity / Party / resource | Relationship / basis | Authority and action | Effects and handoff | Failure / policy dependency |
|---|---|---|---|---|---|---|
| A1 actor-first | Actor starts with Owner/Host intent | Identity; Party/capacity; Property candidate | Claim, invitation or existing association | Only current context capability | Candidate relationship input; resolve Property | Claim/evidence/matching TBD |
| A2 actor-first | Represent or identify Property | Identity; Property; candidate Unit/Destination | Resource representation | Property Authority if granted | Property may exist privately; no publication/Inventory | Creator authority scope TBD |
| A3 actor-first | Establish Owner/Host relationship | Identity; relevant Party; Property | Relationship basis and provenance | Explicit grantor/capability | Relationship projection; no automatic authority | Threshold, conflict and acceptance TBD |
| A4 actor-first | Make bounded context useful | Identity/capacity; Property/Unit | Established relationship + scope | Explicit Property/Booking/Inventory/Operations capability | Working Context and readiness projections | Publication/Booking/Inventory policies TBD |
| R1 resource-first | Represent known Property | Initiator; Property; candidate Unit/Destination | Resource provenance | Current Property Authority only | Resource-first context | Duplicate identity/conflict TBD |
| R2 resource-first | Add Owner/Host relationships | Invited/claiming Identities; Property | Relationship proposal and basis | Relationship-specific grantor | Owner/Host contexts if established | No creator/Owner/Host shortcut |
| R3 resource-first | Evaluate downstream readiness | Property/Unit/Destination; actors | Authority/eligibility/assignment | Explicit scoped capabilities | Publication/Inventory/Booking/Stay projections | Each outcome policy-dependent |

For each step, the acting capacity, resource scope, evidence/basis, provenance, effective time and audit need remain attributable. No step creates a screen, technical invite or persistence field.
