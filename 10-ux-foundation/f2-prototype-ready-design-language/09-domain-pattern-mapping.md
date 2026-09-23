# F2. Domain pattern mapping

Patterns below compose F2 primitives. They are not one component per entity and do not create new domain states.

| Pattern | Minimum content | Required boundaries |
|---|---|---|
| **RequestSummary** | Request identity, staying party, dates/scope, source/attribution, current Request condition, decision authority, relevant Inventory implication, next legitimate action | Request ≠ Booking; accepted Request must not look like confirmed Booking. |
| **BookingSummary** | Canonical Booking identity, confirmed commercial basis, dates/property/unit, permitted payment/settlement projection, related Stay handoff | Begins only from canonical Booking truth; no Request-pending reuse. |
| **StaySummary** | Stay identity/basis, expected dates, arrival/departure observations, Check-in/Checkout/Completion evidence, responsible context, attention | Expected dates do not imply CHECKED_IN/CHECKED_OUT/COMPLETED. |
| **GuestStayHub** | Scoped Stay context, access/arrival/help information and legitimate operational actions | Same hub may be reached by scoped credential or authenticated Guest Identity with legitimate association; Credential ≠ Authority; QR/magic-link/OTP remains TBD. |
| **InventoryTruthView** | Unit × Time, facts/evidence, commitments/blocks/holds, provenance, derived Availability, contextual Bookability, stale/unknown posture | Owner Block, Maintenance Block, Emergency Protective Hold, Temporary Exclusive Commitment, Confirmed Accommodation Commitment and External-backed Commitment remain distinct. Emergency Protective Hold uses protective/attention presentation, not generic Conflict. |
| **InventoryConflictPresentation** | Competing truths, Unit × Time, provenance, consequence/attention, legitimate resolution entry | No universal precedence; no winner styling; FD-09 remains closed. |
| **ExternalAccommodationEvidence** | Report/evidence, reporter/source, authoritative Fact where established, Inventory evaluation, external-backed Commitment where applicable, legitimate Stay | External Accommodation does not fabricate Stayora Booking or commission; Fact is provenance/basis and remains distinct from an External-backed Commitment. |
| **PaymentOutcome** | Payment evidence/attempt, verification posture, outcome, required-condition/Booking-confirmation relationship, reconciliation path | Payment UNKNOWN ≠ FAILED; Payment SUCCEEDED ≠ Booking CONFIRMED; no economics. |
| **AuthorityHint** | Contextual label such as Can See, Can Initiate, Can Act, Can Act if Authorized, Cannot Act or Authority Unknown | Use at a material action boundary, not as a badge on every object; visibility is not permission. |
| **WorkingContextBar** | Acting perspective, resource/destination scope and change/switch affordance where applicable | Working Context ≠ Authority; a property selector alone cannot imply mutation authority. |
| **AttentionProjection** | Underlying object/condition, why attention exists, scope, responsible context and next legitimate action | Projection only; no Task entity, Task lifecycle or priority architecture. Emergency Protective Hold may use this protective attention pattern without becoming Conflict. |

| **CurrentDomainState** | Explicit domain label, object identity, supporting context and neutral/current presentation | CONFIRMED, CHECKED_IN, READY milestones and OBSERVED facts are not generic SUCCESS outcomes. |

## Composition rule

A pattern may be adapted by surface density, but object identity, provenance and canonical wording remain stable. Domain patterns must not hide external origin, turn a projection into an owner, or use color as the only semantic carrier.
