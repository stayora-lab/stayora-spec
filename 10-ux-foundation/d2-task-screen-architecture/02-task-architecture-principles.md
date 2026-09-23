# Task Architecture Principles

## Status

**CONFIRMED derivation rules** from CP5, CP6 and D1; unresolved policy remains TBD.

1. Express tasks as user goals and decisions, not CRUD operations.
2. Derive every task from a V0 requirement, journey or onboarding outcome.
3. Keep Request, Booking, Stay, External Accommodation and Inventory distinct.
4. A screen projects one canonical object or derived projection; it does not duplicate truth.
5. Visibility, context switching and screen entry do not grant authority.
6. Consequential actions originate from an object/context with explicit CP3 authority checks.
7. Attention is a projection of pending domain facts, never a generic Task domain or invented priority algorithm.
8. Empty, partial, out-of-scope and no-authority states are meaningful architecture conditions, not fake data.
9. Use manual-assisted views where CP5 permits people to execute policy; do not turn manual assistance into automation requirements.
10. Prefer the minimum coherent set of views; merge compatible projections only when object semantics and responsibility remain clear.

## Screen justification test

For each concept, identify V0 requirement, actor/context, responsibility, unsolved user job, anchor object, authority-dependent action, journey/onboarding entry and whether merging would lose clarity. If any essential answer is absent, the concept stays a gap or is removed.
