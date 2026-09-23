# Authority × Action Matrix

| Action | Context/capacity | Required authority | Scope/revalidation | Unauthorized behavior |
|---|---|---|---|---|
| Create Direct Request | Guest/public intent | Guest intent capability | Unit/date; revalidate | no Request if invalid |
| Create Sale Request | Sale | active Sale relationship/scope | supply/date; revalidate | Sale cannot accept |
| Accept Request | Host/Primary Host/delegated Co-host | valid Booking Authority | Request/Property/Unit/date/Inventory | NOT PERMITTED/UNKNOWN |
| Reject Request | Host/Primary Host/delegated Co-host | valid Booking Authority | same | no rejection commit |
| Establish Inventory commitment | authorized Host/Inventory actor | explicit basis/authority | current commitments | conflict/manual |
| Initiate/record Payment | payer/authorized flow | applicable condition | Attempt/condition | no unsafe duplicate |
| Confirm Booking | canonical confirmation path | all conditions | Request/payment/Inventory | no confirmation |
| Correct Request | authorized recorder | correction/amendment policy | provenance/current truth | policy boundary |
| Manual reconciliation | Admin/authorized function | function/resource grant | evidence | no super-admin |
