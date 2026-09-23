# Generic Action Model

`CURRENT TRUTH → USER INTENT → ACTING CONTEXT → RESOURCE SCOPE → AUTHORITY CHECK → PRECONDITION CHECK → CURRENT-TRUTH REVALIDATION → ACTION INPUT → ACTION COMMITMENT → OUTCOME → UPDATED PROJECTION → AUDIT / PROVENANCE → HANDOFF / ATTENTION`.

| Action family | Required stages | Behavioral note |
|---|---|---|
| Read/inspect | truth → scope → visibility → projection | no mutation; stale may be safe to view |
| Navigate/context/resource change | context/scope → re-evaluate visibility | switch is not authority |
| Low-consequence record | intent → authority → preconditions → record → projection | canonical recording still retains provenance |
| Consequential mutation | all stages including revalidation and consequence awareness | no optimistic canonical success |
| Manual-assisted | truth/evidence → responsibility → human action → canonical result | manual boundary is visible |
| Exception/reconciliation | conflict/unknown → evidence → authorized evaluation → result | never silently choose a winner |

This is a behavioral model, not technical transaction or API design.
