# B2 — External Truth, Provenance and Authority Mapping

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Report versus authoritative fact

| Concept | What it means | What it may do | What it may not do |
|---|---|---|---|
| External Report / source signal | Someone or a source tells Stayora that external accommodation may exist. | Preserve a provenance-bearing input for evaluation. | Automatically become Inventory Truth, a commitment, a Stayora Booking or payment fact. |
| External Accommodation Fact | Accepted external accommodation record with sufficient authority/evidence under policy. | Be referenced by Inventory and/or Stay; support operational representation. | Become a fake Stayora Booking or silently overwrite incompatible truth. |
| External Inventory Commitment | Authorized commitment effect established from an accepted external fact. | Contribute to effective Inventory Truth and derived Availability. | Erase the fact's external provenance or create Stayora commission. |
| Stay representation | Operational Stay linked to External Accommodation as Accommodation Basis. | Support Guest/Host/Butler/BQL operations and history. | Imply Stayora-originated commerce, payment, attribution or settlement. |

## Authority evaluation questions

The journey needs to evaluate, without inventing the answer:

- who the reporting Identity is and in which acting capacity;
- relationship to the Property/Bookable Unit and Destination;
- whether the actor has explicit `Record External Commitment` / Inventory Authority or only reporting capability;
- source/channel and external reference where available;
- evidence/confidence and time of report;
- whether the record is within resource/date scope and has an authoritative end;
- correction, amendment, duplicate and conflict history.

Property ownership, Primary Host status, Sale relationship, whitelist, Butler assignment and Admin visibility do not each automatically grant the same capability. An ordinary Sale may report/submit; a Sale with explicit external-commitment capability may establish a commitment in granted scope. Butler/BQL operational assignment does not establish commercial or Inventory Authority by default.

## One truth / multiple projections

### External accommodation reported

- **Reporter:** sees a submitted source/report and its pending or unresolved handling; no guarantee of canonical acceptance.
- **Host:** sees a report relevant to Property/Unit if scope allows and must not treat it as a Booking or reserved date until authority resolves.
- **Inventory:** receives a candidate signal, not an effective commitment.
- **Butler/BQL:** normally no operational responsibility yet.
- **Admin:** may see assigned source/evidence/conflict case; Admin is not automatically a business authority.

### External accommodation becomes authoritative

- **Host:** sees source/provenance and operational/inventory consequences in scope.
- **Inventory:** can use an authorized external commitment effect and derive Availability.
- **Guest:** may later receive Stay Access if a valid Stay/access relationship exists; origin remains external.
- **Butler/BQL:** receive need-to-know operational data when a Stay becomes relevant.
- **Admin:** can audit authority, evidence, history and downstream exceptions.

### Conflict exists

- **Host:** sees the external fact and overlapping commitment/exception; no automatic cancellation is implied.
- **Inventory:** preserves both truth sources and exposes conflict; no channel priority.
- **Butler/BQL:** receive only operational impact needed for a current/upcoming Stay, not commercial conflict details by default.
- **Admin:** receives conflict/evidence/authority context where assigned and may coordinate authorized resolution.

### Upcoming Stay becomes operationally relevant

- **Guest:** sees scoped operational preparation/access where eligible.
- **Host:** coordinates fulfillment and readiness.
- **Butler:** sees assigned arrivals, access, preparation and issues.
- **BQL:** sees destination-scoped occupancy, access and registration/service information.
- **Admin:** sees exceptions/audit only within function/resource scope.

### Stay completed

The external source, External Accommodation basis, Inventory history, Stay evidence, incidents and corrections remain distinct historical truth. A qualifying external completed Stay may support Review Eligibility/Review Right under policy. It does not create Stayora commission, Sale attribution, Payment, Settlement or Payout.
