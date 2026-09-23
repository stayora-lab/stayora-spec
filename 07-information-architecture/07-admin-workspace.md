# Admin Workspace

> Status: **STABLE — CHECKPOINT 6 DOCUMENTED; NOT IMPLEMENTATION FREEZE**

```text
ADMIN
├── Attention
├── Applications
├── Verification
├── Incidents
├── Inventory Conflicts
├── Money & Settlement
├── Leads
├── Platform Eligibility
├── Destinations
└── Audit
```

Admin is exception/governance-oriented, not a super-user version of every actor or an analytics-first home. Administrative intervention follows Case/Resource → explicit action → reason → auditable event. Platform administration does not imply impersonating Owner or Host.

Applications covers Sale/Butler approval. Verification preserves Assessment Case, Verification Status and Review Case; `REVIEW REQUIRED` is not a status and an open Review Case may coexist with VERIFIED. Incidents preserve Observation/Complaint ≠ Incident ≠ Finding ≠ Responsibility ≠ Consequence. Inventory Conflicts show source, commitments, evidence and authority without channel priority. Money keeps UNKNOWN unresolved, Settlement separate from Payout, and historical corrections as new adjustments/events. Leads may be assigned manually; assignment does not mean WON. Platform Eligibility remains separate from Host relationship and Reputation. Audit preserves provenance for authority, Inventory, Booking, Money, access and Verification actions. Destination configuration supports Oceanami needs without becoming a generic no-code policy platform.
