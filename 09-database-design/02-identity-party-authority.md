# Identity, Party and Authority Mapping

> Status: **SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL; NOT IMPLEMENTATION FREEZE**

```text
IDENTITY
├── Party Representation
├── Actor Relationships
├── Authority Grants
└── Platform Eligibility
```

Identity is a human/account principal; Party is a legal/economic subject. Identity ≠ Party. Individual and Organization Parties are both supported conceptually; enterprise organization management remains OUT OF SCOPE — V0.

Do not use a mutable `property.owner_id` as ownership truth. Ownership is a temporal Party ↔ Property relationship. Legal Ownership ≠ Primary Host ≠ Commercial Authority ≠ Operational Assignment. Actor Relationship ≠ Authority Grant. Use typed relationship families for Primary Host, Co-host, Sale ↔ Commercial Authority and Butler assignment. Exactly one effective Primary Host per Property applies at a time; the relationship is temporal.

Authority Grant is first-class temporal truth with controlled capabilities and typed resource-scope associations. Platform Eligibility is separate from relationships. Butler assignment does not imply unrestricted authority. Sale relationship states NORMAL, WHITELIST and BLACKLIST belong to Sale ↔ Commercial Authority Principal within scope, not hard-coded Sale ↔ Legal Owner.

Critical actions preserve Identity, Acting Capacity, Authority Basis, Resource and Timestamp. Historical relationships and grants are not destructively overwritten.
