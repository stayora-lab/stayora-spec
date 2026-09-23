# B1 — TBD and Policy Boundary Register

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

The method is: **Known truth → policy boundary → open question → downstream behavior that cannot yet be finalized.** The journey continues on independent branches; an unresolved policy does not erase the known domain truth.

| ID | Known truth | Policy boundary / open question | Downstream behavior not final | Classification / escalation |
|---|---|---|---|---|
| B1-T01 | Offer is a conceptual proposition used by Marketplace/Booking; ownership/lifecycle remain open. | Who owns/composes Offer, how long terms remain valid and how amendments are represented? | Exact option/quote persistence, expiry and change UX. | WORKFLOW / DOMAIN boundary; Founder/Product Architect before detailed interaction. |
| B1-T02 | Sale can discover, quote/share and create a Request with eligibility/relationship/context; Sale role does not accept. | Exact Sale–Host relationship/transaction eligibility and field-level visibility. | Why a particular option/action is unavailable and routing. | AUTHORITY / POLICY; CP3 and Founder. |
| B1-T03 | Request is `PENDING` and does not reserve Inventory. | Request expiry, withdrawal, unanswered handling and notification timing. | Pending/expired/unanswered branch and responsibility reminders. | POLICY; Founder/Distribution/Booking. |
| B1-T04 | Authorized acceptance may create a finite Temporary Inventory Commitment. | Exact commitment window, exclusivity, expiry/release and acceptance-to-commitment timing. | Countdown, expiry, release and late acceptance behavior. | POLICY; Founder/Inventory. |
| B1-T05 | Availability is derived and must be revalidated at commitment; conflicts preserve truth. | Stale/sync thresholds, conflict resolution, late discovery and actor-facing remediation. | Final availability outcome and conflict resolution journey. | POLICY; Founder/Inventory. |
| B1-T06 | Required Payment Condition gates a specific commercial action and is not all future obligations. | Amount/percentage, deadline, grace/reconciliation, default and policy evaluation timestamp. | Payment instruction, expiry, Default, cancellation and release behavior. | POLICY / legal-validation-required; Founder/Money/legal. |
| B1-T07 | Payment Attempt may be `SUCCEEDED`, `FAILED` or `UNKNOWN`; UNKNOWN is unresolved. | Provider reconciliation, retry, responsible actor and safe action while unresolved. | Exact next action and confirmation behavior under UNKNOWN. | POLICY / integration; Founder/Money. |
| B1-T08 | Booking starts at `CONFIRMED` when confirmation conditions pass. | Partial/late condition satisfaction, changed terms, explicit consent and compliance evidence. | What remains pre-confirmation and how a new attempt is made. | POLICY; Founder/Booking. |
| B1-T09 | Booking and Confirmed Accommodation Commitment create downstream operational relevance; Booking ≠ Stay. | Stay scheduling, minimum data, notification timing, and access handoff. | Exact preparation/access behavior. | WORKFLOW / privacy; Founder/Operations. |
| B1-T10 | Guest may use scoped confirmation/link/QR without mandatory account where allowed. | QR fields, lifecycle, privacy, participant linkage and destination data-sharing. | Exact Guest Stay Access interaction and access failure behavior. | LOCAL/JOURNEY blocker; Founder/privacy/destination. |
| B1-T11 | Sale attribution is separate from Money entitlement and Booking Authority. | Earnings visibility, discount funding, commissionable value and adjustments. | Exact Sale earnings/financial disclosures. | MONEY; Founder/legal/accounting. |
| B1-T12 | Manual assistance is valid for complex payment, conflict and exception paths if provenance remains. | Who may assist, which action they may execute and audit/appeal rules. | Admin/assisted handoff and visible provenance. | AUTHORITY/OPERATIONS; Founder. |

## Not silently resolved

No entry above is converted to a new state, permission, percentage, SLA, grace duration, refund rule, provider behavior, aggregate or V0 capability. Successful-payment happy path can proceed conceptually without selecting the unresolved branches.
