# Action Classes

| Class | Examples | Expected behavior |
|---|---|---|
| READ / INSPECT | view Property, Stay, Request | show current known truth and scope |
| NAVIGATE / CHANGE CONTEXT | Host → Sale, Property A → B | re-evaluate projection; no permission grant |
| CREATE INTENT / REQUEST | Guest/Sale Request | preserve intent; downstream authority decides |
| DECISION | accept/reject Request | show decision context, revalidate and record outcome |
| OPERATIONAL RECORDING | readiness evidence, Incident observation | record actor/time/scope; do not infer consequence |
| AUTHORITATIVE RECORDING | External Accommodation, authoritative correction | verify authority and provenance |
| CONSEQUENTIAL MUTATION | Owner Block, Inventory intervention | consequence preview and revalidation |
| CORRECTION / SUPERSESSION | correct fact, supersede representation | preserve history; no destructive rewrite |
| EXCEPTION / RECONCILIATION | conflict, Payment UNKNOWN | preserve evidence and responsibility |
| MANUAL-ASSISTED HANDOFF | Admin/Host support | identify requester, actor, authority, resource, reason |

Classes are behavioral categories, not technical commands or new domain objects.
