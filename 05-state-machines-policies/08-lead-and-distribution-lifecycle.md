# Lead and Lead Assignment lifecycles

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

These are conceptual lifecycle states/outcomes, not a complete confirmed transition graph. Exact allowed transitions remain policy-level/TBD.

Lead lifecycle:

```text
OPEN → IN_PROGRESS → WON → CLOSED
                 ↘ LOST
```

Lead Assignment is separate:

```text
OFFERED / ACCEPTED / DECLINED / EXPIRED / RELEASED / REASSIGNED
```

`REASSIGNED` may remain history/action rather than a literal state. Sale ACCEPTED is Assignment truth, not Lead truth. Acceptance creates demand-handling accountability, not Property, Inventory, or Booking Authority. Declined/Expired/Released do not require a prior Accepted outcome. WON is a qualified attributable commercial outcome under Lead/Attribution Policy; it is not universally Booking Confirmed. CLOSED is administrative/non-commercial closure where appropriate and is not necessarily after WON or automatically Sale failure. Dispatch, 5–10 second timing, and 24h/+24h SLA remain WORKING MODEL/TBD.
