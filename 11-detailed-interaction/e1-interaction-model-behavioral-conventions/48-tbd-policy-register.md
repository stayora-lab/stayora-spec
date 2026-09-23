# E1 TBD / Policy Register

| ID | Boundary | Interaction consequence | Blocker |
|---|---|---|---|
| E1-TBD-01 | payment/confirmation conditions | cannot finalize consequential Booking flow | B local/journey |
| E1-TBD-02 | Payment UNKNOWN/retry/reconciliation policy | no safe detailed retry branch | B local |
| E1-TBD-03 | Inventory conflict resolution | no winner/automatic block behavior | B local |
| E1-TBD-04 | Guest QR/credential/privacy | access/recovery branch incomplete | B local/journey |
| E1-TBD-05 | Sale economics/commission | SAL-05 partial only | B local |
| E1-TBD-06 | Admin/BQL grants | action availability remains conditional | B local |
| E1-TBD-07 | attention acknowledgement/ordering | no universal acknowledgment workflow | A/B |
| E1-TBD-08 | correction/retention semantics | exact history UI cannot finalize | A/B |
| E1-TBD-09 | Check-in/Checkout grants and Completion | field action details bounded | B journey |

At original E1 authoring, no item was resolved by E1; current FD closure is recorded in the overlay below.

## Current FD reconciliation overlay

FD-01, FD-05, FD-06/07, FD-08/09, FD-12, FD-17/18/19 close the corresponding interaction architecture boundaries. The rows above preserve their historical E1 state. Remaining policy/configuration details (credentials/security, Payment amounts/retry/refund, external evidence procedure, Attention mechanics, privacy/retention and exact grants) remain TBD.
