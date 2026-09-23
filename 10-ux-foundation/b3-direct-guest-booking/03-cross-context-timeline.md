# B3 — Cross-Context Timeline

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

This timeline is a conceptual responsibility map. It does not create a combined state machine.

| Journey point | Guest | Public Marketplace / Discovery Truth | Host / Booking Authority | Inventory Truth | Payment | Booking | Stay / Operations |
|---|---|---|---|---|---|---|---|
| Demand and discovery | Searches and evaluates | Projects Destination, Unit, content, Public Price, trust and discovery signals | No action responsibility | Read-only derived Availability | None | None | None |
| Range / occupancy evaluation | Supplies dates and party context | Shows Searchability, Availability and Bookability distinctions | No decision yet | Computes relevant derived truth | None | None | None |
| Guest intent | Chooses to proceed | Presents next action | Notified only after Request exists | Unchanged | None | None | None |
| Request created | Sees `PENDING` status and truthful next step | Stops being the sole context; public view does not become private authority | Receives decision responsibility | No reservation; existing commitments remain | No obligation/attempt unless a later condition is created | No Booking exists | No operational work |
| Request decision | Sees accepted/rejected result where visibility permits | May stop or hand off to private progress | Accepts/rejects only with Booking Authority | Revalidates after acceptance; no automatic winner | May become relevant after acceptance | Still no Booking at `ACCEPTED` | None |
| Inventory revalidation | Sees progressing/blocked outcome | Public availability may change from derived truth | Authority basis remains recorded | May establish finite Temporary Exclusive Commitment where policy supports | Specific condition may be presented | Still unconfirmed | None |
| Payment condition | Guest/Payer fulfils action-specific condition | No private payment detail | Sees scoped assurance only | Commitment has independent policy/expiry | Attempt has own lifecycle; `UNKNOWN` unresolved | Not confirmed by payment alone | None |
| Confirmation evaluation | Receives only truthful result | No false public availability promise | Authorized evaluation completes | Confirmed commitment effect only when conditions pass | Condition satisfaction is one input | Booking begins at `CONFIRMED` | Stay not automatically started |
| Confirmation / access | Sees confirmation and eligible scoped access | Public listing remains a projection | Host sees fulfilment responsibility | Confirmed accommodation affects future derived Availability | Future obligations remain separate | `CONFIRMED` | Stay may be `SCHEDULED` / not started |
| Operations relevance | Uses access/support where eligible | No private operations exposure | Fulfils accommodation responsibility | No change from access itself | Settlement/obligation rules remain separate | Remains separate from Stay | Butler/BQL receive need-to-know operational projection |

## Key boundary

The sequence is intentionally asynchronous: a Request can be accepted while a Booking is still absent; a Payment Attempt can succeed while another confirmation condition fails; a confirmed Booking can exist while a Stay is not checked in. No single lane absorbs another domain’s state.
