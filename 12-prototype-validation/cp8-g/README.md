# CP8-G — Prototype & Validation

> Status: **READY FOR FOUNDER / PRODUCT ARCHITECT VALIDATION**  
> CP8-H: **NOT STARTED**

CP8-G is a local, deterministic prototype for validating the accepted Stayora UX architecture. It is not production implementation, a backend, a database migration, an authentication system or a component library.

## Entry

Open [`index.html`](index.html) in a browser. The prototype starts in **Public Marketplace**. Use **Reset demo** at any time to restore the deterministic dataset. The **Validation map** button opens the review checklist.

Recommended spine:

1. Marketplace → Villa 03 → Start a request.
2. Create the direct Request, then switch to Host Workspace.
3. Accept the Request; observe that Booking remains UNCONFIRMED.
4. Use Admin to simulate Payment UNKNOWN, then Payment SUCCEEDED and confirmation evaluation.
5. Open Guest Stay Access, then Butler Ops to record READY, arrival observation, Check-in, Checkout and Completion.
6. Visit Destination / BQL for Incident, Emergency Protective Hold, Inventory Conflict and the calendar.
7. Visit Admin for the External Report → Fact → External-backed Commitment → Stay path.

All actions are local mock transitions. Labels marked `current`, `observed`, `processing`, `unknown`, `protective` and `conflict` follow CP8-F2 semantics.

## Files

- [`index.html`](index.html) — prototype shell and seven-surface entry.
- [`styles.css`](styles.css) — CP8-F2 visual language applied to the prototype.
- [`app.js`](app.js) — local deterministic state transitions and projections.
- [`dataset.json`](dataset.json) — illustrative Oceanami dataset.
- [`VALIDATION-PACKAGE.md`](VALIDATION-PACKAGE.md) — entry instructions, scenario map and review checklist.
- [`CP8-G-PROTOTYPE-COMPLETION-REPORT.md`](CP8-G-PROTOTYPE-COMPLETION-REPORT.md) — checkpoint completion report.

## Boundary

Prototype behavior is intentionally simulated. No payment provider, identity provider, messaging service, external channel, persistence layer or production API is connected. No Grok or legacy semantic assumptions are treated as canonical.
