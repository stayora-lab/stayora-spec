# F2. Grok reconciliation register

No Grok source/prototype file is present in the canonical workspace. This register uses the accepted F2 reference values and example semantics supplied in the F2 brief; it must be rechecked if the actual source is later attached. **CP8 and F1 remain authoritative.**

| Area | Decision | F2 treatment |
|---|---|---|
| Palette | ADAPT | Warm cream, warm dark, restrained purple, red danger and quiet borders become candidate reference tokens only; contrast review required. |
| Typography | ADAPT | Plus Jakarta Sans primary; Cormorant Garamond selective editorial/display accent; no extra family added. |
| Spacing | ADAPT | 8/12/16/20/24/32 rhythm; density varies by surface. |
| Radius | ADAPT | Purposeful 8/12/16/overlay/pill roles; do not use 24/32 everywhere. |
| Shadows | ADAPT | Restrained elevation only for layering; hierarchy comes earlier from layout/spacing/type/surface/border. |
| Cards | KEEP / ADAPT | Simple card/list composition for public and summaries; cards do not fragment canonical truth. |
| Panels | ADAPT | Workspace/evidence panels with explicit scope and hierarchy. |
| Buttons | ADAPT | Calm primary/secondary/subtle/destructive actions with authority and outcome language. |
| Forms | ADAPT | Field labels, help/error association and consequential summary; no implicit payment/authority. |
| Dialogs | ADAPT | Focus-safe confirmation/detail/resolution overlays; no new approval workflow. |
| Filter pills | ADAPT | Use as selected/filter UI only; never as Booking/Block truth. |
| Navigation | ADAPT | Responsibility/context navigation from D3; no actor-label or Owner workspace invention. |
| Mobile navigation | ADAPT | Progressive disclosure and safe touch targets; no native-app architecture decision. |
| Calendar | ADAPT / REJECT old semantics | Keep Property × date composition; reject binary booking/block, winner rendering and editable “Available”. |
| Checkout | REJECT old semantics | Preserve Checkout ≠ Completion and no automatic Inventory release. |
| Trips / Guest | ADAPT | Compose GuestStayHub/StaySummary; credential and association remain policy-bound. |
| Host Today | ADAPT | Attention projection and responsibility summary; no generic Task domain. |
| Reservations | REJECT / ADAPT | Do not use “reservation” as Request/Booking convenience; use canonical Request, Booking and Stay patterns. |
| Listing flow | ADAPT | Use onboarding/relationship/eligibility boundaries; listing visibility is not authority. |
| Inbox | ADAPT cautiously | May be a projection of attention/handoff; do not create a message-owned Task lifecycle. |
| Pricing / earnings | ADAPT | Scoped commercial/financial projection; no new economics, hidden spread or authority implied. |
| Duty | ADAPT cautiously | Use Butler Assignment/Today/Stay operations; do not create workforce/task architecture. |
| Status treatments | REJECT old semantics / ADAPT | Use F1/F2 outcomes; UNKNOWN ≠ FAILED, PENDING ≠ SUCCESS, CONFLICT has no winner. |
| New patterns required by CP8 | NEW NEEDED | RequestSummary, GuestStayHub, InventoryConflictPresentation, ExternalAccommodationEvidence, PaymentOutcome, AuthorityHint, WorkingContextBar and AttentionProjection. |

Rejected entries must not silently reappear in CP8-G under renamed labels.

## Explicitly rejected Grok semantic assumptions

These are **REJECTED**, even if a visual label or prototype interaction made them look convenient:

| Rejected assumption | Why it cannot survive |
|---|---|
| Request stored as Booking pending | Request and Booking are distinct canonical concepts. |
| Request accept → Booking confirmed automatically | Acceptance may lead to conditions/commitment; Booking begins only from canonical confirmation. |
| Request decline → Booking cancelled | A declined Request is not a cancelled Booking. |
| Payment method → proof of deposit/payment | A method or instrument is not payment evidence or a successful attempt. |
| Payment action that only records method → “paid” | Recording an input cannot assert Payment success, obligation satisfaction or Booking confirmation. |
| Universal 24-hour Request expiry | Expiry remains policy/TBD; no universal duration is a design assumption. |
| Expected calendar date → Stay state | Expected arrival/departure dates do not imply Check-in, Checkout or Completion. |
| iCal overlap ignored | External evidence and overlap must remain visible for Inventory evaluation and conflict handling. |
| Cancellation → automatic Inventory opening | Release consequences are policy/domain-dependent and cannot be inferred by a visual interaction. |
| Managed listing / Host / Owner relationship → mutation authority | Relationship, workspace or label does not grant authority; effective authority remains contextual and scoped. |
| Hard-coded 30% deposit | Historical/superseded economics cannot return through visual defaults. |
| Hard-coded 10–50% deposit limits | Unapproved payment limits remain TBD. |
| Hard-coded 50% refund | Refund policy is not a design-system assumption. |
| Hard-coded 8% platform fee | Economics are not a primitive or visual constant. |
