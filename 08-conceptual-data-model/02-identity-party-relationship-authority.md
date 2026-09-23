# Identity, Party, Relationship and Authority

> Status: **STABLE — CP7 ARCHITECTURE REVIEWED; NOT IMPLEMENTATION FREEZE**

## Party and Identity

`Party` represents a business, legal or economic subject:

```text
Party
├ Individual Party
└ Organization Party
```

`Identity` represents a person/account capable of acting. Organization is not an Identity. An Identity may represent or act for a Party through valid relationship/authority. Party exists so the model is not locked to one individual Owner per villa. Enterprise organization management remains OUT OF SCOPE — V0.

## Relationships and grants

Actor Relationship and Authority Grant are separate. `Sale ↔ Host = WHITELISTED` is a commercial relationship; `Co-host may ACCEPT_BOOKING_REQUEST for Villa A` is authority. Relationship may influence permission but is not itself necessarily authority.

Effective Permission remains the CP3 model:

```text
Identity + Platform Eligibility + Actor Relationship + Authority Capability
+ Resource Scope + Authority Lifecycle + Resource/Destination Policy
+ Transaction Context → Effective Permission
```

Resource Scope is a conceptual scope/value-object candidate, not an aggregate decision. Relationships and grants have temporal validity. Revocation affects future actions and access; it does not retroactively invalidate a legitimate historical action.
