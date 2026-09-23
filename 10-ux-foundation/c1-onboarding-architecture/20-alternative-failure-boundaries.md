# C1 — Alternative and Failure Boundaries

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Situation | Known truth | Classification | Safe behavior | Not decided |
|---|---|---|---|---|
| Identity already exists | One Identity may hold multiple capacities. | SUPPORTED | Resolve to existing Identity; do not duplicate for role convenience. | Matching/recovery/privacy. |
| Duplicate contact | Contact is not guaranteed unique person truth. | POLICY / IDENTITY TBD | Preserve ambiguity and require supported resolution. | Match threshold. |
| Invited person already has Identity | Invitation targets existing Identity/relationship. | SUPPORTED | Resolve recipient; acceptance does not grant authority alone. | Notification/merge behavior. |
| Wrong recipient | Invitation/claim does not match intended subject. | WORKFLOW TBD | Reject/revoke/escalate; preserve audit. | Recovery/expiry. |
| Invitation declined/revoked | Proposal is not relationship/authority. | SUPPORTED + policy | Keep no active assignment/authority. | Messaging/reenrollment. |
| Relationship claim disputed | Claim is not truth. | AUTHORITY / POLICY TBD | Preserve claim/evidence/dispute; no automatic authority. | Resolver/appeal. |
| Ownership unclear | Owner relationship/evidence is incomplete. | LEGAL / AUTHORITY TBD | Keep pending; do not infer Host/finance. | Evidence threshold. |
| Host differs from Owner | Distinct relationships are canonical. | SUPPORTED | Represent separately; use explicit Host authority. | Precedence/transfer. |
| Authority not granted | Context/relationship may exist without action. | SUPPORTED | Show pending/limited context; no privileged action. | Escalation. |
| Authority revoked | Revocation affects future actions. | SUPPORTED | Restrict future action; preserve history. | In-flight action handling. |
| Property already exists/duplicate | Property identity is separate from claim. | WORKFLOW TBD | Preserve existing and claimed records; reconcile. | Merge/precedence. |
| Property has no Host | Property can exist before hosting relationship. | SUPPORTED | Keep represented/unpublished or limited per policy. | Discovery/assignment. |
| Owner but no Booking Authority | Ownership and hosting/Booking are separate. | SUPPORTED | Do not accept Request or alter Booking without authority. | Grant path. |
| Sale known but not eligible | Known Identity ≠ platform eligibility. | SUPPORTED | No Sale capabilities until eligible. | Approval/appeal. |
| Butler has no assignment | Butler capacity/eligibility ≠ assignment. | SUPPORTED | No scoped operational context. | Assignment path. |
| Assignment ends | Assignment is temporal. | SUPPORTED | Remove future operational scope; preserve evidence. | Handoff/replacement. |
| Multiple contexts | One Identity may have several capacities. | SUPPORTED | Select context; evaluate action authority separately. | Context navigation. |
| Resource relationship changes | Scope/time changes. | SUPPORTED + policy | Apply future effective scope; preserve history. | Propagation. |

Boundary method: **known truth → policy boundary → open question → downstream behavior not finalizable**.
