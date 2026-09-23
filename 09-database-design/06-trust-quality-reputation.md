# Incident, Finding, Verification, Review and Reputation

> Status: **SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL; NOT IMPLEMENTATION FREEZE**

Canonical chain:

```text
Observation / Complaint / Signal
→ Incident / Review Case
→ Evidence + Assessment
→ Finding
→ Policy Evaluation
→ Possible Consequence
```

Observation/Complaint/Signal ≠ Incident ≠ Finding ≠ Responsibility ≠ Consequence. Incident is a Case root; evidence preserves provenance but does not automatically create Finding. Finding is first-class historical determination and need not lead to punishment.

Verification separates Assessment Case, Review Case, Verification Decision and current Status. Do not use `property.verified BOOLEAN`. Open Review Case may coexist with VERIFIED; precautionary suspension requires an explicit authorized Verification Decision. Decision history preserves subject, originating Case, prior/resulting status, reason, policy basis, authority and effective time.

Review follows `Verified Interaction → Review Eligibility → Review Right → Review`. Persist granted Review Right; external represented Stay may qualify. Review components correspond to eligible interaction context and may concern Property/Villa, Host, Butler, Sale or Destination. Reputation is derived, audience-specific, versionable and rebuildable; there is no universal TrustScore/ReputationScore. Binary evidence media may live outside the relational database while stable identity/metadata/provenance remain represented.
