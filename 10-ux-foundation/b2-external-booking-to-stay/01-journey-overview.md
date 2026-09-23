# B2 — External Booking → Stay Journey Overview

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Canonical V0 journey

```text
External Commerce
  → external accommodation report/registration
  → authority + provenance/evidence evaluation
  → External Accommodation Fact where accepted
  → Confirmed Accommodation Commitment where an authorized commitment is established
  → Inventory Truth / derived Availability
  → operational Stay representation where supported
  → Guest Stay Access where eligible
  → Butler / Destination Operations
  → checkout/completion/history
```

The two branches are intentional:

- external information may be needed to establish Inventory Truth;
- external accommodation may be represented for operations and Stay even when Stayora does not own the commerce.

Neither branch requires a Stayora Booking. A reported fact may remain untrusted or unresolved until authority/evidence policy permits canonical use.

## External origins in scope of the architecture

Canonical sources mention Host Direct, Owner Direct, OTA-originated accommodation, Sale/Zalo/off-platform booking and other legitimate external sources. They are provenance categories, not a promise that every integration or input method is V0-supported. Manual Host entry and manual-assisted operations are permitted where CP5 allows them, provided authority, source, history and auditability remain intact. No Channel Manager, PMS or automatic OTA integration is designed here.

| Origin / input | B2 treatment |
|---|---|
| Host Direct / Owner Direct | Canonical external source category; may be manually represented when an authorized actor and required operational truth exist. Exact input workflow remains policy/workflow TBD. |
| OTA-originated accommodation | Canonical source category; external source/provenance may be recorded. No OTA integration or automatic synchronization is assumed in V0. |
| Sale / Zalo / off-platform accommodation | A Sale may report/submit; Sale role or relationship alone does not establish Inventory Commitment. Explicit capability is required for authoritative Inventory effect. |
| Manual Host/Admin entry | Manual-assisted path is compatible with CP5 where authority, provenance, evidence and auditability are preserved. It is not a new automated workflow. |
| Integration-supplied fact | Architecture can consume a source signal, but no integration, Channel Manager, PMS or sync SLA is created by B2. |
| Unidentified / unsupported source | Preserve as unresolved external information; do not promote to canonical fact, commitment or Stay without the required authority/evidence. |

## What Stayora legitimately knows

Before acceptance, Stayora may know only a report or source signal. A useful external accommodation fact may include, conceptually, source, external reference where available, Bookable Unit, accommodation dates, minimum Staying Party information, authoritative recorder, evidence/provenance and timestamps. External revenue, margin and payment data are not required merely to represent operational truth.

## Confirmation boundaries

- `External Report` is not automatically an `External Accommodation Fact`.
- `External Accommodation Fact` is not automatically an `Inventory Commitment`.
- An authorized external commitment may establish an Inventory Commitment; Availability is derived from effective commitments.
- An External Accommodation may provide the Accommodation Basis for a Stay, but it is not a Stayora Booking and does not imply Check-in or Completed.
- Conflict preserves both facts/commitments and requires authorized resolution; no source/channel priority is invented.

## B2 success question

Can Host, Guest, Butler and Destination/BQL rely on truthful operational and inventory information for an externally originated accommodation while still knowing that the original commerce, payment and attribution remain outside Stayora?
