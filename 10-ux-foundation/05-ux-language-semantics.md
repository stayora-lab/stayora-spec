# CP8-A — UX Language and Semantics

> Status: **ACCEPTED AS CP8-B BASELINE** · **NOT FROZEN**

This register tells later UX work which concepts may be shown directly and which need careful explanation. It does not rename canonical domain concepts or finalize marketing copy.

| Canonical term | User-facing treatment | Keep visibly distinct from | Internal detail that may remain behind progressive disclosure |
|---|---|---|---|
| Request / Booking Request | Use “Request” where a Guest/Sale/Host must understand that a decision is pending. | Booking, Reservation, Inventory Commitment. | Request lifecycle transitions and authority basis unless action depends on them. |
| Booking | Use “Booking” only after `CONFIRMED`; explain it as confirmed commercial accommodation. | Request, Stay, External Accommodation. | Orchestration details before confirmation. |
| Stay | Use “Stay” for actual operational accommodation experience. | Booking, payment, External Accommodation. | Completion-readiness evidence and downstream reconciliation mechanics. |
| External Accommodation | Use when provenance affects expectations; a simpler “external stay/booking record” may be used with provenance preserved. | Stayora Booking, fake channel reservation, automatic commission. | Source reference/evidence mechanics unless conflict or trust depends on them. |
| External Booking | Treat as a commerce/booking record created outside Stayora and referenced by Inventory and/or Stay. It is not owned by Stayora Booking by default. | Stayora Booking, external payment as Stayora payment. | Source-specific commercial fields not needed for operational truth. |
| Inventory Commitment | Use in Host/Admin/advanced exception contexts when explaining why dates are protected. | Availability, Request, Booking, Payment Session. | Commitment orchestration and storage/persistence details. |
| Availability | Use for derived date/resource truth. Qualify source/context when necessary. | Searchability, actor-specific Bookability, operational occupancy. | Effective-commitment calculation. |
| Bookable | Use when a resource can be considered for a specific action and context. | Merely searchable/listed/visible. | Exact eligibility/policy evaluation. |
| Held / Temporary Commitment | Prefer “temporary commitment” or “temporary hold” only where the finite, authority-scoped nature is clear. | Request, confirmed Booking, permanent reservation. | Expiry orchestration and Payment Session linkage. |
| Confirmed | Qualify the object: “Booking confirmed”, “payment succeeded”, “Stay completed”. Do not use as a universal badge. | Accepted Request, Paid, Completed Stay. | State transition details unless the action depends on them. |
| Payment Required | Explain the specific Required Payment Condition for the commercial action. | Fully Paid, Payment Received, Payment Obligation for all future amounts. | Obligation schedule and provider mechanics unless due/action relevant. |
| Payment Received / Paid | Use the object and scope: payment attempt succeeded, obligation satisfied, payout paid. | Booking confirmed, entitlement earned, Settlement. | Provider transaction IDs and reconciliation internals. |
| Payment `UNKNOWN` | Surface as unresolved payment outcome when user action depends on it; never show as failed by convenience. | Failed, Payment Default, cancellation. | Provider reconciliation steps. |
| Payment Obligation | Usually explain as “amount due” or “remaining balance” when audience needs it; preserve obligation semantics in Host/Admin/Money contexts. | Payment Attempt, Required Payment Condition. | Formula and adjustment history unless needed. |
| Payment Default | Use only after applicable due obligation, deadline and reconciliation/grace conditions satisfy policy. | Unpaid request, provider `UNKNOWN`, No-show. | Policy evaluation details unless consequence is actionable. |
| Completed Stay | Use when operational completion conditions are met. | Checkout click, paid, settled, no-show. | Completion-readiness evidence and exception path. |
| Verified / Stayora Verified | Always qualify the subject and meaning: property-supply quality assurance. | Identity Verification, Verified Stay, Reputation, luxury. | Assessment evidence and Review Case unless trust decision depends on it. |
| Verification Review / Review Case | Use in Admin/quality contexts as an open assessment/review case. | Verification Status, public Review, Reputation. | Evidence and policy basis can be progressive. |
| Review Right | Usually express as “eligible to review” or “review available” when relevant. | Review, Reputation, automatic right from checkout. | Eligibility evidence threshold unless challenged. |
| Review | Use for an authored/evidenced review interaction. | Review Right, Reputation signal, Incident. | Moderation and weighting unless applicable. |
| Reputation | Use as a signal family/projection with audience qualifier. | Universal TrustScore, Verification, one star score for everything. | Inputs/weighting/decay remain TBD. |
| Incident | Use for recorded problem/case. | Finding, Responsibility, Consequence, generic error. | Case taxonomy/severity/SLA while open. |
| Finding / Responsibility / Consequence | Keep separate in Admin/exception language; simplify for public users only when meaning cannot be confused. | Incident, fault, automatic refund or suspension. | Evidence and policy chain unless action depends on it. |

## Semantic writing rules

- Qualify “Owner” as Legal Owner or Primary Host/authorized actor when the authority distinction matters.
- Qualify “Verified” as Identity Verification, Stayora Verified, or Verified Stay.
- Qualify “Deposit” as Booking Deposit or Security/Damage Deposit.
- Say “Booking confirmed” rather than using “confirmed” alone when commercial truth matters.
- Do not use “reservation” as a convenience synonym if it could imply that a Request reserves Inventory.
- Keep external provenance visible where it affects Inventory, Stay, access, trust or expectations.
- Never use a successful payment, a QR credential or a visible object as shorthand for authority.

## Language still requiring Founder/policy review

Exact public copy for payment deadlines, cancellation/change/no-show, external source labels, Guest QR/privacy, Verification evidence, Review eligibility and Incident consequences remains open. This register does not choose it.
