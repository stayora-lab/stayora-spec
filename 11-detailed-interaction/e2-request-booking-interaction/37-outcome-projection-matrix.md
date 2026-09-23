# State / Outcome Projection Matrix

| Canonical stage/outcome | Guest | Sale | Host | Operations | Admin |
|---|---|---|---|---|---|
| intent only | selected intent | option/intent | none/preview | none | none |
| Request submitting | processing only | processing if creator | none | none | none |
| Request PENDING | received/pending | pending + attribution | actionable attention | none | only if exception |
| Request ACCEPTED | accepted/confirmation pending | outcome pending | accepted + conditions | possible relevance | exception if needed |
| Request REJECTED | rejected | rejected/outcome | resolved attention | none | audit if governed |
| Request CONFLICTED | impact only | permitted exception | conflict/authority | operational impact | reconciliation |
| Payment PROCESSING | condition processing | permitted outcome | condition processing | none | exception if required |
| Payment FAILED | failure/next canonical path | permitted outcome | not confirmed | none | reconciliation if required |
| Payment UNKNOWN | unresolved/no duplicate | permitted unresolved | reconciliation responsibility | no false confirmation | exception/reconciliation |
| Booking CONFIRMED | confirmed/outcome | outcome/attribution | Booking truth | operational handoff | audit/exception |
| Manual assistance | known truth + follow-up | permitted status | responsibility | as scoped | assigned case |
| Inventory conflict | availability impact | no false offer | conflict | operational impact | reconciliation |

These are projections, not new domain states.
