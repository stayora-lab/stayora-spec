# F1. Interaction and outcome language

These are presentation outcomes derived from CP8-E. They are not domain state machines.

| Outcome | Visual/behavioral treatment | Must not imply |
|---|---|---|
| **SUCCESS** | Clear confirmation naming the object/action and updated projection. Preserve relevant provenance. | That every related domain object is complete, paid or settled. |
| **REJECTED / NOT PERMITTED** | Explain the reason category where safe, keep the object visible when allowed and show the legitimate next path. | That the actor, object or relationship is invalid in every context. |
| **VALIDATION FAILURE** | Associate the problem with the field or condition and preserve entered information where safe. | A domain rejection or technical failure. |
| **CONFLICT** | Show the conflicting basis/evidence and responsible resolution path without winner styling. | Which source wins or that the user may overwrite truth. |
| **PROCESSING / PENDING** | Show unresolved work and what can safely happen next; prevent unsafe duplicate commitment. | Success, failure or automatic release. |
| **FAILED** | State known failure and safe recovery/retry/manual path. | That an UNKNOWN outcome is failed. |
| **UNKNOWN** | Distinguish unresolved authoritative outcome, attempt/provenance and reconciliation responsibility. | Failed, cancelled, unpaid or safe duplicate retry. |
| **PARTIAL / MANUAL FOLLOW-UP** | Show what is known, what is incomplete and who/which context must continue. | Completed workflow or generic system breakage. |
| **CORRECTED / SUPERSEDED** | Retain history/provenance and show the currently effective representation. | Erasure of the earlier truth or a new domain state. |

## Consequential-action presentation

When relevant, expose the E1 grammar in a proportionate summary:

```text
current truth → user intent → acting context → resource scope
→ authority/preconditions → current-truth revalidation → action commitment
→ outcome → updated projection → audit/provenance → handoff/attention
```

Not every item is a visible step. The interface should surface the items that could change the decision: actor/context, Unit × Time or resource scope, reversibility, material consequence, conflict, UNKNOWN, external verification or correction/supersession. F1 adds no approval workflow and does not decide the underlying policy.
