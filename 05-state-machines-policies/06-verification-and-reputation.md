# Verification and Reputation models

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

## Verification

Status set: `NOT_VERIFIED`, `VERIFIED`, `SUSPENDED`, `REMOVED`; this is a status model, not a mandatory single linear transition graph. Assessment Case: `OPEN → ASSESSING → DECIDED` with PASS/FAIL examples. Review Case: `OPEN → ASSESSING → RESOLVED`, with KEEP VERIFIED, SUSPEND, REMOVE, or REQUIRE REMEDIATION outcomes.

An open Review Case does not automatically change Verification status. Serious qualifying evidence may permit precautionary suspension under explicit Policy. Removal and reinstatement preserve history; `REMOVED → VERIFIED` is never a silent/direct rewrite and requires a new qualifying assessment/grant. Stayora Verified ≠ Identity Verification, Property Compliance, or Reputation. Verification is a scoped assurance grant, not a score, and does not own Inventory, Booking, or Commercial Authority.

## Reputation

Reputation is a derived model:

```text
Verified Events / Evidence → Reputation Signals → Reputation Projections
```

There is no universal TrustScore and no Good/Average/Bad state machine. Independent dimensions may include Guest Reviews, Verified Transaction History, Commercial Reliability, Lead Performance, Host Relationship History, and Platform Policy History. Visibility may be PUBLIC, RELATIONSHIP-SCOPED, or INTERNAL. Whitelist/Normal/Blacklist is Distribution Relationship, not Reputation. Weighting, decay, samples, disputes, algorithms, and public score design remain **TBD**.
