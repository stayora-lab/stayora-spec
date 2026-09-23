# E2 TBD / Policy Register

| ID | Unresolved boundary | Interaction stops/continues |
|---|---|---|
| E2-TBD-01 | Request expiry/withdrawal | creation/pending continues; terminal behavior blocked |
| E2-TBD-02 | Request correction/amendment | provenance model continues; exact flow blocked |
| E2-TBD-03 | Offer validity/terms | option path continues; validity rules blocked |
| E2-TBD-04 | Temporary Commitment duration/release | acceptance boundary continues; timing blocked |
| E2-TBD-05 | Inventory conflict remediation | conflict behavior continues; resolution blocked |
| E2-TBD-06 | Required Payment Condition economics/deadline/grace | boundary reached; detailed payment blocked |
| E2-TBD-07 | Payment UNKNOWN reconciliation/retry | safe unknown behavior defined; retry blocked |
| E2-TBD-08 | confirmation exception/cancellation/default/release | confirmation boundary blocked |
| E2-TBD-09 | Guest credential/privacy | handoff defined; credential detail blocked |
| E2-TBD-10 | Sale economics/commission | attribution projection only |
| E2-TBD-11 | dual-capacity/self-dealing | capacity behavior defined; policy not solved |
| E2-TBD-12 | manual override authority | assist path defined; grant not invented |

At original E2 authoring, no TBD was closed by E2; current FD closure is recorded in the overlay below.

## Current FD reconciliation overlay

FD-08/09 close conflict responsibility and the no-universal-precedence boundary; FD-10/11 close Temporary Commitment lifecycle/release architecture; FD-12 closes External recording authority; FD-17/18/19 close Booking Confirmation architecture, Payment Verification Authority and Payment UNKNOWN behavior. Request expiry/withdrawal/amendment, Offer validity, concrete duration/deadlines/grace/retry/refund/cancellation/default, Guest credentials, Sale economics, self-dealing and specific grants remain TBD.
