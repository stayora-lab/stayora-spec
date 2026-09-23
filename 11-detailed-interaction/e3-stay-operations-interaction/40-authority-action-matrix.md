# Authority × Action Matrix

| Action | Context/capacity | Required authority | Scope/revalidation | Unauthorized behavior |
|---|---|---|---|---|
| report preparation/readiness | Butler/Host/ops | canonical observer/reporting authority | Assignment/Property/Stay | evidence not recorded |
| record arrival observation | Butler/BQL/Host as canonical | observation authority | Stay/resource | no Check-in |
| Check-in | Butler/Host/authorized ops | explicit Check-in grant | Stay/Unit/state | not permitted/unknown |
| report Incident | Guest/Butler/Host/BQL | operational reporting scope | Stay/resource | no downstream consequence |
| escalate Incident | responsible context | escalation grant | Incident/Stay | manual assistance |
| Checkout | Butler/Host/authorized ops | explicit Checkout grant | CHECKED_IN Stay | not permitted/unknown |
| completion evaluation | canonical responsible authority | explicit condition/authority | CHECKED_OUT Stay | remains pending |
| DID_NOT_OCCUR | canonical authority if defined | explicit trigger/grant | SCHEDULED Stay | unresolved blocker |
| manual reconciliation | Admin/function | staff function/resource grant | evidence | no Admin override |
