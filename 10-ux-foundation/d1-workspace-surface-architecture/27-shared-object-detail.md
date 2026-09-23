# Shared Object Detail principle

Each domain object has one canonical detail concept with contextual projections:

| Object | Guest | Host | Sale | Butler | BQL | Admin |
|---|---|---|---|---|---|---|
| Stay | own access/arrival | commercial + responsibility | limited attributable outcome | operational need-to-know | destination operational | exception/audit |
| Booking | confirmation | decision/commercial | Request/outcome/attribution | relevant operational basis | need-to-know | reconciliation |
| Incident | own report/status | response/responsibility | normally none | evidence/action | operations | case/audit |
| Property | public listing | supply authority | discovery/terms | assigned operations | destination operations | representation/compliance |

Different projections do not create separate Booking, Stay, Incident or Property objects. Domain ownership remains CP2/CP7; surfaces own responsibility for a task only.
