# B3 — State and Domain Truth Mapping

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Object boundaries

| Concept | B3 meaning | Explicit non-equivalence |
|---|---|---|
| Guest intent | A decision to continue toward a Request. | Not Request, Commitment, Payment, Booking or Stay. |
| Booking Request | A request awaiting an authorized commercial decision. | Not Booking and does not reserve Inventory. |
| Inventory Commitment | An effective protection/block over Unit × Time, including a finite Temporary Exclusive Commitment where supported. | Not Availability, Request or Payment. |
| Required Payment Condition | Condition required for a specific commercial action such as Booking Confirmation. | Not all future Payment Obligations and not Booking. |
| Payment Obligation | Financial obligation due under applicable commercial terms/schedule. | Not Required Payment Condition and not Payment Attempt. |
| Payment Attempt | Attempt and provider outcome for a payment action. | Not Booking; `UNKNOWN` is unresolved. |
| Booking | Stayora-originated commercial accommodation record beginning only at `CONFIRMED`. | Not Request and not Stay. |
| Stay | Operational representation of accommodation on its own lifecycle. | Not proof that Booking was confirmed or payment settled. |
| Guest account | Optional interaction/authentication mechanism if later chosen. | Not Guest identity or Staying Party. |
| Sale attribution | Source/relationship only when genuinely present. | Not required for direct B3 and not inferred from public discovery. |

## Existing lifecycle use

- Request uses canonical outcomes such as `PENDING`, `ACCEPTED`, `REJECTED`, `EXPIRED` and `CONFLICTED` where applicable; B3 adds none.
- Payment Attempt uses the existing `INITIATED`, `PROCESSING`, `SUCCEEDED`, `FAILED` and `UNKNOWN` reasoning; B3 adds none.
- Booking begins only when all canonical confirmation conditions pass and is `CONFIRMED` at that point.
- Stay remains independent (`SCHEDULED`, arrival/check-in, checkout/completion according to CP4); B3 does not infer operational state from payment or confirmation alone.

## Confirmation invariant

Conceptually:

```text
Booking CONFIRMED only if
  valid Offer / applicable terms
  AND valid Booking Authority
  AND exclusive Inventory truth for the relevant scope
  AND applicable Required Payment Condition satisfied where required
  AND required consent / compliance conditions pass
```

This is a cross-domain invariant already grounded in CP4/CP7, not a new B3 rule. A successful Payment Attempt is one possible condition result; it does not bypass the others.

## Inventory invariant

```text
Guest intent → no commitment
Request created → no commitment
Request accepted → revalidation / possible finite commitment according to policy
Booking confirmed → confirmed accommodation effect
```

No B3 statement chooses commitment duration, conflict priority, release behavior or Payment Default economics.
