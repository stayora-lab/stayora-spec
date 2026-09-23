# F2. Interaction outcome patterns

Outcomes are presentation contracts, not domain states. The container and persistence should match consequence. Current domain/lifecycle truths such as CONFIRMED, CHECKED_IN, READY milestones and OBSERVED facts use a separate neutral/current presentation; they are not generic SUCCESS.

| Outcome | Visual treatment | Copy and persistence | Action behavior / provenance |
|---|---|---|---|
| **SUCCESS** | Positive semantic status with clear object/action label | Persistent inline/section confirmation when mutation matters; toast only for low consequence | Show updated projection and relevant provenance; do not imply related Booking/Payment/Stay completion. |
| **REJECTED / NOT PERMITTED** | Neutral/danger boundary without blame | Persistent at action boundary; reason category where safe | Keep safe visibility, explain legitimate next path; authority basis remains scoped. |
| **VALIDATION FAILURE** | Field/summary error, not domain-danger styling by default | Persists until corrected or dismissed with context | Associate error with field/condition; preserve entered data where safe. |
| **CONFLICT** | Explicit competing-basis treatment; no winner color | Persistent until acknowledged/resolved or superseded | Show Unit × Time, provenance, consequence and resolution entry; do not overwrite or pick a winner. |
| **PROCESSING** | Known work-underway treatment with progress cue and neutral/primary semantic | “Payment processing is still in progress.” Persist while work is underway. | Prevent unsafe duplicate mutation; show safe refresh/recheck if canonical. |
| **PENDING** | Neutral unresolved-condition treatment where a decision/condition is awaiting completion | Name what is pending and what can safely happen next; do not imply completion. | Preserve the pending object and authority boundary. |
| **FAILED** | Known failure treatment | Persistent enough to understand recovery | Offer known retry/manual path; do not use for UNKNOWN. |
| **UNKNOWN** | Distinct unresolved-authority treatment, not danger-only | “Processing may have completed, but the authoritative outcome is currently unknown.” Persist until reconciled or a new authoritative outcome exists. | Discourage duplicate payment/action; show attempt, known facts and manual/reconciliation follow-up. |
| **PARTIAL / MANUAL FOLLOW-UP** | Mixed/attention treatment showing completed and incomplete parts | Persistent while responsibility remains | Name next responsible context/person; do not call the workflow complete. |
| **CORRECTED / SUPERSEDED** | History/provenance treatment with current effective value | Retain history where relevant | Link/expand prior record; never erase evidence or imply a new domain state. |

A consequential mutation outcome belongs in the object detail, action region or attention projection when users need continued understanding. Toast is supplementary for low-risk feedback only. **PROCESSING ≠ UNKNOWN; UNKNOWN ≠ FAILED; UNKNOWN ≠ SUCCESS.** Current-domain presentation is neutral and does not announce interaction success.

## Current-domain and protective presentations

`presentation.current` is a neutral/current truth treatment for domain/lifecycle examples such as **CONFIRMED**, **CHECKED_IN**, a **READY** milestone or **OBSERVED** arrival evidence. It uses explicit text, object identity and a restrained border/background; it does not use the generic success color merely because the state is positive.

`presentation.protective` is the attention treatment for **Emergency Protective Hold**. It communicates protection, escalation and scope. It is distinct from `outcome.conflict`; if the Hold also participates in an actual Inventory conflict, the separate conflict presentation may be composed in addition.
