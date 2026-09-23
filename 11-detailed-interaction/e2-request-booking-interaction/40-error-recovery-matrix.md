# Error / Recovery Matrix

| Condition | Example | Safe recovery |
|---|---|---|
| validation failure | missing canonical date/Unit | correct input; no Request |
| no authority | Sale tries accept | explain safe category; route context |
| wrong scope | Host opens another Property | switch only to legitimate scope |
| stale truth | Request changed while open | refresh/revalidate; no commit |
| conflict | Inventory incompatible | preserve evidence; authorized reconciliation |
| technical failure | submission transport failure | recheck whether canonical Request exists; no blind repeat |
| unknown outcome | Payment Attempt UNKNOWN | no duplicate; recheck/reconcile |
| manual assistance | policy edge | record evidence/responsibility; await result |

No row invents timeout, retry, cancellation, refund or release policy.
