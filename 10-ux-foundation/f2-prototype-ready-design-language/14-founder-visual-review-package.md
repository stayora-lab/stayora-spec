# F2. Founder Visual Review Package

**Status: ACCEPTED — F2 FOUNDER VISUAL DECISION WITH FOUR SEMANTIC PRESENTATION CORRECTIONS.** This package combines semantic guidance with the [static visual review specimen](specimen/CP8-F2-visual-review-specimen.html). It is not a production implementation or a global future-design freeze.

## Visual specimen artifact

Open [CP8-F2 Visual Review Specimen](specimen/CP8-F2-visual-review-specimen.html) to compare the accepted palette, typography, shape/surface hierarchy, primitive states, nine interaction outcomes, Request/Booking/Stay distinctions, Inventory conflict treatment, three character proofs, density profiles and accessibility notes. The accessibility section explicitly shows ACCEPTED F2 REFERENCE versus ACCESSIBLE IMPLEMENTATION ADJUSTMENT; no token is silently changed in this pass. The artifact is static review material only; it creates no product route or component implementation.

## Review legend

- **ACCEPTED FROM F1:** semantic foundation and CP8 boundaries.
- **ADAPTED FROM GROK:** useful visual/composition reference made CP8-compatible.
- **ACCEPTED — F2 FOUNDER DECISION:** visual direction accepted for the CP8-G baseline.
- **CORRECTED:** semantic presentation adjustment required by the Founder decision.
- **TBD:** implementation-level or policy dependency intentionally open.

## A. Color direction

**ACCEPTED — ADAPTED FROM GROK:** warm cream canvas, light card, warm ink, restrained purple action, plum accent, red danger and quiet warm borders. Full contrast matrix for normal/small text, focus, disabled, overlays and images remains implementation review.

## B. Typography direction

**ACCEPTED — ADAPTED FROM GROK:** Plus Jakarta Sans for product/workspace; Cormorant Garamond only for selective editorial/display expression. Fallback, licensing and localization remain implementation TBD.

## C. Shape/radius direction

**ACCEPTED:** 8 control, 12 card, 16 panel/overlay, full pill; larger radii only by explicit composition reason.

## D. Surface/elevation direction

**ACCEPTED — ADAPTED FROM GROK:** warm canvas, light surface, subtle surface, restrained raised/overlay levels. Shadow and theme details remain implementation review.

## E. Density direction

**ACCEPTED — F1 CARRIED FORWARD:** comfortable public/Guest, medium-to-dense Host/Sale, mobile/action Butler, dense Destination/BQL/Admin. Legibility and reflow remain implementation review.

## F. Primitive examples

Review Button/Action, Status/Badge, Alert/Callout, Card/Panel, Dialog/Sheet, Field/Input, Table/List and Date/Calendar against the anatomy/state/accessibility rules in [06-core-primitives](06-core-primitives.md).

## G. Interaction outcomes

Review visual specimens for SUCCESS, REJECTED, VALIDATION FAILURE, CONFLICT, PROCESSING/PENDING, FAILED, UNKNOWN, PARTIAL/MANUAL FOLLOW-UP and CORRECTED/SUPERSEDED. The test is that UNKNOWN never looks failed or successful, pending never looks complete and conflict never picks a winner.

## H. Marketplace character

Warm hospitality, strong property imagery and calm hierarchy, with public price/dates/bookability truth visible. No hidden spread, invented verification or Booking implication from a Request.

## I. Workspace character

Structured object titles, scope/context, lists/tables, attention and action boundaries. Host, Sale and Admin may be dense but remain one system.

## J. Operational character

Field-ready, legible and action-focused Butler/Destination/BQL composition. Evidence, responsibility and attention are visible; operational UX is not commercial Booking UX.

## Founder decision record

| Visual decision | Result | Reconciliation note |
|---|---|---|
| COLOR | ACCEPTED | Candidate warm cream/purple direction retained. |
| TYPOGRAPHY | ACCEPTED | Plus Jakarta Sans primary; Cormorant Garamond selective editorial/display. |
| SHAPE | ACCEPTED | 8 / 12 / 16 / full radius roles retained. |
| SURFACE / ELEVATION | ACCEPTED | Warm surfaces and restrained elevation retained. |
| DENSITY | ACCEPTED | Surface-specific density retained. |
| MARKETPLACE CHARACTER | ACCEPTED | Warm hospitality character retained. |
| WORKSPACE CHARACTER | ACCEPTED WITH SEMANTIC PRESENTATION CORRECTIONS | Current-domain states must not use generic SUCCESS. |
| OPERATIONAL CHARACTER | ACCEPTED WITH SEMANTIC PRESENTATION CORRECTIONS | Processing/Unknown, protective attention and current-domain states clarified. |
| OVERALL STAYORA VISUAL DIRECTION | ACCEPTED WITH FOUR SEMANTIC PRESENTATION CORRECTIONS | F2 is the CP8-G baseline; no product/domain/policy change. |

## Four recorded semantic corrections

1. Domain/lifecycle truth such as CONFIRMED, CHECKED_IN, READY and OBSERVED uses neutral/current presentation, not generic SUCCESS.
2. PROCESSING is known work underway; UNKNOWN means the authoritative outcome cannot currently be established.
3. Emergency Protective Hold uses protective/attention presentation and remains distinct from Conflict and Maintenance Block.
4. External Accommodation Fact remains distinct from External-backed Commitment; Inventory truth uses the latter where applicable and keeps the Fact as basis/provenance.

## Review questions

1. Does the palette feel recognizably Stayora while keeping semantic status readable?
2. Does the typography pairing support both hospitality and operational truth?
3. Are radius/elevation choices calm rather than ornamental?
4. Does density vary correctly without creating seven unrelated products?
5. Can a reviewer distinguish Request, Booking, Stay, Inventory basis, Payment UNKNOWN and authority without relying on color?
6. Are any proposed values too close to a product decision or policy assumption?

The visual decisions above are recorded. Exact component APIs, responsive breakpoints, full accessibility audit and other implementation details remain open; this record does not create a global freeze.
