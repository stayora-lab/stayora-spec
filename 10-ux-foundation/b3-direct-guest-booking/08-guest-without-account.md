# B3 — Direct Guest Without Mandatory Account

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Product outcome

B3 does not make a registered account or login a precondition for a valid Guest Request or later paid Stay. A Guest person/party, an account, a payer, a Booking creator, a lead guest and a Staying Party may be related without being the same concept.

## What must persist conceptually

Without selecting a technical mechanism, the product must preserve enough scoped relationship and audit truth for the Guest to:

1. identify and review their Booking Request;
2. receive a truthful pending, accepted, rejected or blocked outcome;
3. provide or correct required Guest/Staying Party information;
4. fulfil and reconcile an applicable Payment Condition as the relevant Payer;
5. receive a `CONFIRMED` Booking outcome when all conditions pass;
6. access the eligible Stay information and operational support; and
7. preserve consent, provenance, authority and correction history.

## Identity and account boundary

The canonical relationship may involve a Guest person/party and a separate account/login mechanism. No choice is made here among email link, OTP, password, social login, QR, token or another credential. Those are later interaction/security decisions.

Guest visibility or possession of a link does not itself prove Booking Authority, Staying Party identity, payer authority or operational access eligibility. Authentication, privacy, consent, recovery and credential lifecycle remain unresolved boundaries where CP6/CP8-A do not prescribe them.

## Confirmed minimum contact and access invariant

Per [ADR-P077](../../00-start-here/DECISIONS.md#adr-p077), commercial Request creation requires a name and at least email or phone, without requiring an Account or establishing verified Identity/contact/legal identity. “Khách” is only a presentation fallback and cannot satisfy this requirement. Guest without Account ≠ anonymous commerce actor.

Contact Identity ≠ Guest Credential ≠ Resource Identifier. A Request/Booking/Stay URL or resource identifier alone, even with matching/re-entered email or phone, does not authorize Guest data access. Accountless access requires the existing Guest Credential / recognized access eligibility tied to the relevant relationship/lifecycle and existing need-to-know/progressive disclosure. Security-sensitive identifiers/credentials require security-appropriate randomness; unpredictability does not replace access control. Concrete credential and recovery mechanisms remain TBD.

## Safe B3 behavior

- Keep Request, Payment and Booking truth independent of the original browser/session.
- Do not force account creation merely to make the domain model convenient.
- Do not expose another person’s commerce, payment, authority or operational data because a Guest lacks an account.
- Keep the Guest’s responsibility to provide truthful party information separate from the mechanism used to regain access.

## Open questions

Minimum Request contact identity and the access invariant are narrowed by ADR-P077. Exact credential mechanism, payer/Guest relationship proof, recovery, duplicate identity handling, consent evidence and remaining privacy/field-level disclosure are policy/UX/security TBD. B3 records these remaining questions; it does not resolve them.
