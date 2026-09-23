# F1. Primitive versus domain pattern rules

## Definitions

- **UI primitive:** a reusable visual/interaction building block with generic semantics, such as `Badge`, `Dialog`, `Button`, `Table` or `Field`.
- **Domain pattern:** a composed presentation or interaction arrangement whose meaning comes from an accepted Stayora responsibility, such as `BookingStatusBadge`, `OwnerBlockConfirmation` or `StaySummary`.

## Rules

1. Domain patterns compose primitives and preserve canonical terminology; they do not redefine the underlying domain.
2. A primitive must not encode Booking, Payment, Inventory, Stay, Verification or authority semantics merely through a color or generic label.
3. Create a domain pattern only when the same responsibility, scope and outcome semantics recur across a journey or surface family. Do not create one component for every entity.
4. Domain patterns must keep actor/context, provenance and uncertainty visible where the decision depends on them.
5. A pattern may project one canonical object differently by surface, but it must not create competing truth or imply that a projection owns the object.
6. Consequential patterns must expose the relevant E1 grammar and revalidation boundary; a `Dialog` alone does not make an action safe.

| Primitive | Domain pattern example | Boundary to preserve |
|---|---|---|
| Badge / Status | `BookingStatusBadge` or `PaymentOutcomeBadge` | Qualify the object/outcome; do not use a universal “confirmed” badge. |
| Dialog | `OwnerBlockConfirmation` | Show scope, acting context, authority and consequence; no new approval workflow. |
| Card / Panel | `StaySummary` | Stay remains distinct from Booking and external accommodation. |
| Table / List | `InventoryTruthTable` | Fact, commitment, Availability and Bookability remain distinct projections. |
| Alert / Callout | `PaymentUnknownNotice` | UNKNOWN is unresolved, not FAILED or default. |

## Protected semantic distinctions

Visual patterns must keep these CP8-A–E distinctions explicit wherever they are relevant:

- Request ≠ Booking ≠ Stay.
- External Accommodation ≠ Stayora Booking.
- External Report ≠ authoritative Fact.
- Fact ≠ Inventory Commitment ≠ Availability ≠ Bookability.
- Incident ≠ Maintenance Block.
- Emergency Protective Hold ≠ Maintenance Block.
- Arrival observation ≠ Check-in.
- Departure observation ≠ Checkout.
- Checkout ≠ Completion.
- Completion ≠ Inventory release.
- Payment UNKNOWN ≠ FAILED.
- Payment SUCCEEDED ≠ Booking CONFIRMED.
- Assignment ≠ Authority.
- Credential ≠ Authority.

A label, color, badge, icon, table row or dialog must not silently collapse one of these concepts into another.
