# C1 — Domain, Workflow and Authority Gap Findings

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Classification | Observed need | Existing canonical concept | Why insufficient | Affected onboarding/resources | Impact | Evidence | Recommended escalation |
|---|---|---|---|---|---|---|---|
| IDENTITY / DOMAIN GAP | One person may appear in several roles/Parties. | Identity, Party, capacity, relationship. | Matching/organization details are not fully specified. | All · Identity/Party | Duplication or wrong linkage. | CP7 identity model | Resolve identity/Party policy; no new account-per-role. |
| AUTHORITY GAP | Relationship must produce bounded resource action. | Relationship + Authority Grant + Effective Permission. | Exact grants/non-delegable/precedence remain open. | Owner/Host/Co-host/Sale | Unauthorized actions. | CP3 authority | Define capability policy later. |
| WORKFLOW GAP | Invitation/claim/assignment entry modes differ. | Relationship/assignment/eligibility concepts. | No shared acceptance/evidence workflow is canonical. | All · Grantor/recipient | False onboarding completion. | C1 entry/boundary docs | Define per-flow later; no universal lifecycle. |
| POLICY GAP | Context is visible before every action is authorized. | Working Context vs Permission. | Field-level projection/activation incomplete. | All contexts | Overexposure or blocked work. | CP6/CP8-A | Define privacy/context policy. |
| PROPERTY GAP | Property can exist before Host/publication/Verification. | Property, Destination, Listing, Verification. | Prerequisite ordering/status projections open. | Property/Unit | Fake publication or trust signal. | CP2/CP7 | Detail in later Property flow. |
| V0-SCOPE GAP | Manual-assisted onboarding needed without enterprise IAM. | CP5 actors and manual operations. | Exact manual boundary/approval work open. | Sale/Butler/Host/Property | Scope creep. | CP5 | Keep manual-assisted; defer tooling. |

These are escalation points, not new aggregates, entities, states, permissions or technical auth designs.
