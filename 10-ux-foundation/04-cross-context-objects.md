# CP8-A — Cross-Context Domain Truth

> Status: **ACCEPTED AS CP8-B BASELINE** · **NOT FROZEN**

The same canonical object can support different responsibilities. The following projections are conceptual; they do not add fields, screens or alternate records.

## Booking Request

| Context | Why the same Request matters | Authority boundary |
|---|---|---|
| Guest | Know whether the request is pending, accepted, rejected, expired or conflicted and what is required next. | Guest does not accept the Request or treat it as a reserved Booking. |
| Host / authorized Co-host | Decide whether to accept/reject within valid Booking Authority and understand Inventory/terms context. | Sale role or ownership alone does not accept; acceptance is attributable. |
| Sale | Progress demand, share relevant status and support the Guest through the commercial path. | Sale creates/monitors demand but does not accept for Host by default. |
| Butler | Normally no responsibility before a confirmed accommodation basis creates an operational Stay. | No commercial acceptance or finance from operational visibility. |
| BQL / Destination | Normally no Request decision; may later need destination-operational data after confirmed Stay. | Destination scope does not create Booking Authority. |
| Admin | See exceptions, evidence or manual-assist cases when assigned. | Admin action requires domain/function/resource authority and audit. |

**Canonical guardrail.** Request is commercial intent awaiting authorized decision. It does not reserve Inventory and is not a pending Booking. An accepted Request still requires the applicable commitment, payment and confirmation conditions before a Booking exists.

## Booking

| Context | Why the same Booking matters | Authority boundary |
|---|---|---|
| Guest | Understand confirmed commercial accommodation terms and the path to Stay/access. | Visibility is scoped to the Guest relationship; it does not expose internal economics. |
| Host / authorized Co-host | Fulfill the confirmed accommodation commitment and coordinate the related Stay. | Booking actions require valid hosting/delegated authority. |
| Sale | Monitor attributed commerce, Guest support and own commercial outcome. | Attribution does not grant Inventory, Booking acceptance or Owner finance. |
| Butler | Use the Booking only as relevant basis/context for the operational Stay. | Operational need-to-know does not expose terms or grant commercial change. |
| BQL / Destination | Derive relevant arrival/occupancy/access preparation. | Destination operational visibility is not commercial authority. |
| Admin | Reconcile exceptions, cases and audit across domains. | Admin cannot rewrite Booking truth or impersonate another actor. |

**Canonical guardrail.** Booking begins at `CONFIRMED`; it is commercial truth and is not Stay. A Booking can provide an Accommodation Basis for a Stay, but completion is an independent operational fact.

## Stay

| Context | Why the same Stay matters | Authority boundary |
|---|---|---|
| Guest | Use the actual Stay for arrival, access, help, participation and eligible review. | Scoped Stay access does not create general business authority. |
| Host / authorized Co-host | Coordinate fulfillment, readiness, check-in/out, completion and incidents. | Hosting responsibility does not automatically grant financial authority. |
| Sale | Support the attributed Guest/commerce relationship and observe completion where relevant. | Sale does not own operational or financial consequences. |
| Butler | Execute assigned arrival, in-stay and departure work; record evidence. | Assignment permits scoped operations, not Booking acceptance or finance. |
| BQL / Destination | Coordinate destination occupancy, access, services and issues. | Destination staff see only function/need-to-know data. |
| Admin | Handle qualifying exceptions, incidents, verification/reputation or money cases. | Downstream domain decisions remain owned by their domains. |

**Canonical guardrail.** Stay can arise from a Stayora Booking or External Accommodation. `CHECKED_OUT` is not automatically `COMPLETED`; operational completion belongs to Stay and does not itself settle money.

## Inventory and Availability

| Context | Why the same truth matters | Authority boundary |
|---|---|---|
| Guest | Decide whether a listing appears suitable for requested dates. | Searchability/visibility does not guarantee actor-specific bookability or create a hold. |
| Host / authorized Co-host | Maintain Blocks/Commitments and respond to conflicts within scope. | Only authorized actions establish or release commitments. |
| Sale | Sell from actual derived Availability and avoid promising incompatible dates. | Demand access is not Inventory Authority. |
| Butler | Report an operational issue; understand operational consequences where shared. | Observation alone does not create an Availability Block. |
| BQL / Destination | Understand operational occupancy/access needs. | Operational occupancy is not commercial Availability. |
| Admin | Inspect conflict source, evidence, effective commitments and authority. | No channel priority or arbitrary overwrite. |

**Canonical guardrail.** Inventory Truth belongs to Bookable Unit × Time and is derived from effective Inventory Commitments. `AVAILABLE`, `HELD`, `BOOKED` and `BLOCKED` are contextual semantics/projections; Request is not a commitment.

## Property and Bookable Unit

| Context | Why the same truth matters | Authority boundary |
|---|---|---|
| Guest | Understand the destination, property/listing and bookable accommodation being considered. | Public information does not expose private ownership or full authority records. |
| Host / authorized Co-host | Maintain supply facts, listing, price, availability and relationships. | Property scope does not automatically authorize every Unit/action. |
| Sale | Match Guest demand to a suitable unit and trust signal. | Sale cannot edit Host supply without separate authority. |
| Butler | Prepare the assigned physical accommodation and record operations. | Operational assignment does not create commercial control. |
| BQL / Destination | Coordinate destination-level operation of participating supply. | Destination relationship does not imply ownership or Host authority. |
| Admin | Assess eligibility, quality, conflict and audit. | Admin action remains scoped and attributable. |

**Canonical guardrail.** Destination → Property → Bookable Unit is conceptual. For Oceanami V0 a Villa is one Property plus one Entire-Villa Bookable Unit; nested inventory is out of V0. Property, ownership, publication, Verification and Availability remain distinct.

## Incident

| Context | Why the same Incident matters | Authority boundary |
|---|---|---|
| Guest | Report a problem and understand response/remediation without being asked to prove fault. | Complaint/report does not itself assign responsibility or consequence. |
| Host / authorized Co-host | Respond, provide evidence and coordinate operational resolution. | Response is not a financial/reputation decision. |
| Sale | Support a Guest/transaction relationship when relevant. | Sale does not impose refund, payout or reputation consequences. |
| Butler | Record operational observation/evidence and respond within assignment. | Evidence does not equal Finding or commercial authority. |
| BQL / Destination | Record destination operational issue and coordinate local response. | Local operational scope does not determine ultimate economics. |
| Admin | Assess case, finding, responsibility and downstream policy handoff. | Incident, Finding, Responsibility and Consequence remain separate. |

**Canonical guardrail.** `OPEN → ASSESSING → RESOLVED → CLOSED` is a conceptual case lifecycle. A qualifying policy-defined unresolved exception may affect completion, but opening an Incident does not automatically change Verification, Reputation, Money or Stay.

## Projection rule

```text
ONE CANONICAL OBJECT / TRUTH
        ↓
CONTEXT-SPECIFIC RESPONSIBILITY + NEED-TO-KNOW PROJECTION
        ↓
AUTHORITY-SCOPED INTERACTION
```

Different context emphasis is expected. Duplicate business records, silent state renaming and cross-domain authority inference are not.
