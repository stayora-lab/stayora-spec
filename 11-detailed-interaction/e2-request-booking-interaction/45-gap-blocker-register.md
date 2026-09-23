# E2 Gap / Blocker Register

| Class | Need | Affected branch | Level | Independent work |
|---|---|---|---|---|
| POLICY GAP | payment/confirmation economics | accept → Booking | C journey | Request/revalidation work continues |
| POLICY GAP | Request expiry/withdrawal/amendment | pending/correction | B local | common outcomes continue |
| WORKFLOW GAP | Inventory conflict remediation | decision | B/C | conflict preservation continues |
| MONEY GAP | Payment UNKNOWN/retry/default | payment | B/C | unknown behavior continues |
| PRIVACY GAP | Guest credential/contact | Stay handoff | B/C | handoff structure continues |
| MONEY GAP | Sale economics | Sale outcome | B local | attribution continues |
| AUTHORITY GAP | Admin/override/self-dealing | decisions | B/C | effective-authority behavior continues |
| INTERACTION GAP | field Check-in/Checkout | operations handoff | B | E2 stops before B4 detail |

No D-level CP8 blocker is introduced.

## Current closure overlay

The historical E2 blocker rows are retained. Current architecture status is CLOSED for the FD-08/09, FD-10/11, FD-12 and FD-17/18/19 items; only their policy/configuration detail remains open. No D-level CP8 blocker remains.
