# Failure and alternative paths

| Scenario | Classification / C3 handling |
|---|---|
| Existing Identity or duplicate contact | **SUPPORTED:** resolve Identity/Party; matching/merge details TBD |
| Sale claim not eligible | **SUPPORTED:** keep claim/application pending or rejected; no Sale Context |
| Eligibility pending/denied/revoked | **SUPPORTED:** block future distribution actions; preserve history; policy details TBD |
| Invitation declined | **SUPPORTED:** no relationship/authority; expiry/renewal TBD |
| Distribution Relationship missing/ended | **SUPPORTED:** no scoped distribution action; do not infer relationship |
| Resource outside Sale scope | **SUPPORTED:** hide/block action; scope policy TBD |
| Supply visible but not Bookable | **SUPPORTED:** preserve Searchable/Available/Bookable distinction |
| Sale creates Request then attempts acceptance | **SUPPORTED boundary:** route to independent Booking Authority; reject unauthorized action |
| Sale + Co-host with valid delegated authority | **SUPPORTED:** accept only in Co-host capacity and scope |
| Sale attempts Inventory mutation | **SUPPORTED boundary:** deny unless separate explicit Inventory Authority |
| Sale reports External Accommodation | **SUPPORTED:** preserve report; authoritative recording requires Inventory Authority |
| Attribution conflict | **POLICY TBD:** preserve claims/provenance; no winner chosen |
| Commercial terms unavailable | **POLICY/WORKFLOW TBD:** do not expose invented economics or create misleading Request |
| Authority changes mid-journey | **SUPPORTED:** re-evaluate action at execution; preserve prior valid action |

