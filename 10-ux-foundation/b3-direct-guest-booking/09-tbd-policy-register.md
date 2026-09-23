# B3 — TBD and Policy Register

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| ID | Known truth | Policy / open question | Downstream behavior not finalizable | Classification |
|---|---|---|---|---|
| B3-T01 | Request is separate from Booking and does not reserve. | What is the unanswered/expiry/withdrawal policy? | Timeout, notifications, closure and re-entry. | WORKFLOW / POLICY TBD |
| B3-T02 | Acceptance requires Host/authorized Booking Authority. | How is missing, revoked or multiple authority handled? | Routing, escalation and decision precedence. | AUTHORITY TBD |
| B3-T03 | Accepted Request requires final Inventory revalidation. | What is the finite commitment window and release rule? | Hold duration, expiry and Guest communication. | POLICY TBD |
| B3-T04 | Conflicting facts/commitments remain distinct. | Which actor resolves and what remediation applies? | Winner, release, compensation and channel behavior. | POLICY TBD |
| B3-T05 | Required Payment Condition is action-specific. | Amount, deadline, grace, refund/default/retry economics? | Payment orchestration and blocked confirmation behavior. | POLICY / LEGAL TBD |
| B3-T06 | Payment `UNKNOWN` is unresolved. | How and when is provider reconciliation completed? | Retry, release, default and Guest messaging. | INTEGRATION / POLICY TBD |
| B3-T07 | Direct B3 requires no Sale attribution. | When may a Sale be legitimately attributed if it later assists? | Attribution, commission and disclosure. | DISTRIBUTION TBD |
| B3-T08 | Instant Book is a separate controlled branch. | Eligibility, scope, authority, commitment and payment timing? | Optional direct path behavior. | FOUNDER / POLICY TBD |
| B3-T09 | Guest account is not required by current product truth. | Minimum identity/contact, recovery and privacy boundary? | Accountless continuity and access. | UX / SECURITY TBD |
| B3-T10 | Booking begins only at `CONFIRMED`. | Exact Guest-facing blocked/progressing projection? | Copy and contextual projections. | UX TBD |
| B3-T11 | Stay is separate from Booking. | Minimum basis/timing for Stay creation and access? | Schedule/access/operations handoff. | WORKFLOW / PRIVACY TBD |
| B3-T12 | Public truth excludes private economics and notes. | Which restrictions, evidence and trust signals are public? | Marketplace disclosure. | MARKETPLACE TBD |
| B3-T13 | External Commerce is a separate B2 concept. | How are referrals or external origins distinguished if they enter public discovery? | B2/B3 provenance projection. | DOMAIN / PROVENANCE TBD |

No row is promoted to a requirement by this document. An unresolved branch does not block independent journey analysis.
