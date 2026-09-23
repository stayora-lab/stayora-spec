# CP8-A — Actor, Working Context and Responsibility Model

> Status: **ACCEPTED AS CP8-B BASELINE** · **NOT FROZEN**

## Canonical model

```text
ONE IDENTITY
  → multiple relationships / capacities
  → multiple WORKING CONTEXTS
  → scoped resources and responsibilities
```

Working Context is a UX perspective, not a Role and not a permission grant. Role is not Permission. Relationship is not Authority. Ownership is not Hosting Authority. A critical action remains attributable as:

```text
Identity + Acting Capacity + Authority Basis + Resource + Action + Time
```

The rows below describe the minimum UX reasoning model for CP8-A. “Normally visible” means relevant data may be projected when relationship, authority, lifecycle and need-to-know conditions allow it. It never overrides effective permission or privacy policy.

## Guest context

| Dimension | UX model |
|---|---|
| Purpose | Discover eligible supply or use a valid Stay and complete the Guest's part of arrival, stay and review. |
| Responsibilities | Provide demand/party information when required; understand terms and request/Booking status; use scoped confirmation/access; report issues; provide an eligible review. |
| Resource scope | Relevant Property/Bookable Unit, Booking Request, Booking, Stay, Staying Party and scoped access credential. |
| Important objects | Listing, Destination, Availability, Public Price, Trust signals, Request, Booking, Stay, Access, Incident, Review Right. |
| Action families | Discover; submit Request where supported; provide required consent and, where identified as Payer/authorized payer, participate in payment; view own Booking/Stay; use access; report; review when eligible. |
| Normally visible | Decision-relevant listing, Availability/Price, relevant terms, own Request/Booking/Stay, arrival/access, destination information and help. |
| Normally not visible | Owner payout, Sale commission, internal ledger, unrelated Guest records, private evidence or authority grants. |
| Dependencies | Guest relationship and lifecycle; applicable Payment/Booking conditions; scoped credential; privacy and destination policy. Guest account is optional for valid Stay access where CP5/CP6 say so. |
| Open/TBD | QR fields/lifecycle, participant identity linkage, exact evidence and notification rules, cancellation/change/default details. |

## Owner / Legal Owner context

| Dimension | UX model |
|---|---|
| Purpose | Represent the ownership relationship and make valid supply/financial responsibilities actionable when authority and scope are established. |
| Responsibilities | Maintain or authorize Property information, understand commercial/operational records and provide valid authority evidence where required. |
| Resource scope | Related Party/Property and financial or operational resources only where separately granted. |
| Important objects | Property, Bookable Unit, Listing, Inventory Commitment, Booking Request, Booking, Stay, Quality and own eligible economics. |
| Action families | View/edit/publish, manage or delegate only when effective authority exists; review relevant exceptions and own economics where granted. |
| Normally visible | Property/supply facts, Requests, commitments, Stays, quality cases and scoped financial information. |
| Normally not visible | Unrelated properties, full Guest data, Sale economics or every financial ledger solely because of ownership. |
| Dependencies | Identity/Party relationship, Primary Host or delegated authority, platform eligibility, destination/property policy and financial capability. |
| Open/TBD | Evidence of legal/operating authority, transfer precedence, non-delegable actions, field-level finance/privacy scope. |

## Primary Host context

| Dimension | UX model |
|---|---|
| Purpose | Operate a Property's hosting/commercial responsibility as the authority anchor for the relevant scope. |
| Responsibilities | Decide or delegate valid Property, Inventory and Booking actions; maintain listing/price/availability; respond to Requests; coordinate operations and exceptions. |
| Resource scope | Property, Bookable Unit, Inventory, Requests, relevant Bookings/Stays and delegated people within effective scope. |
| Important objects | Property, Listing, Inventory Commitment, Availability, Request, Booking, Stay, Butler assignment, Incident, Quality, Money projections. |
| Action families | Edit/publish; block/manage Inventory; accept/reject Request; establish valid external commitments; assign/delegate; coordinate issue handling and review. |
| Normally visible | Supply and availability truth, Requests/Bookings/Stays, operational readiness, relevant quality/cases and own scoped economics. |
| Normally not visible | Unrelated properties or actors, full payment provider data, Sale earnings and destination data not needed for the Property task. |
| Dependencies | Primary Host authority source, delegation lifecycle, property/destination policy, Booking/Inventory policy and finance capability. |
| Open/TBD | Authority precedence, delegation propagation, dual-capacity/self-dealing rules, exact conflict resolution and financial grants. |

## Co-host context

| Dimension | UX model |
|---|---|
| Purpose | Execute specifically delegated Property, Inventory, Booking or operational work. |
| Responsibilities | Perform only the granted capability in the granted resource/lifecycle scope and preserve acting capacity in audit/handoff. |
| Resource scope | Property/Bookable Unit/Booking/Stay scope named by valid delegation. |
| Important objects | Delegation, Inventory, Request, Booking, Stay, Incident and relevant operational records. |
| Action families | Delegated edit, availability, block, accept/reject or operational actions as explicitly granted. |
| Normally visible | Objects needed for the delegated task and the authority scope that explains available actions. |
| Normally not visible | Every Primary Host action, unrelated Property finance, Sale economics or broader network data. |
| Dependencies | Valid delegating authority, capability, scope, lifecycle and revocation status. Co-host is not a fixed permission bundle. |
| Open/TBD | Non-delegable capability list, grant evidence, precedence and propagation on change/revocation. |

## Sale context

| Dimension | UX model |
|---|---|
| Purpose | Help a Guest find suitable available supply and progress attributable commerce within Sale authority. |
| Responsibilities | Discover supply; inspect relevant Availability and Public Price; prepare/share an offer where supported; create and monitor Booking Requests; monitor attributed Booking/Stay and own commercial outcomes where V0 supports them. |
| Resource scope | Eligible supply, relevant Property/Bookable Unit, Lead, Request, attributed Booking/Stay and Sale-owned economics. |
| Important objects | Destination, Listing, Availability, Public Price, Trust signals, Lead, Request, Booking, Stay, attribution/entitlement projection. |
| Action families | Search; compare; quote/share; create Request; monitor statuses; follow payment assurance; view own attribution/earnings where supported. |
| Normally visible | Fit, real Availability, Public Price, trust signals, Request/Booking status, operational information needed to fulfill demand and own economics. |
| Normally not visible | Owner net payout/tax/profitability, full Owner ledger, unrelated Guest data, Inventory controls or Host-only evidence. |
| Dependencies | Sale platform eligibility, Sale–Host Distribution Relationship, transaction context, applicable policy and any explicit additional capability. Whitelist is not Instant Book permission by itself. |
| Open/TBD | Affiliate split, Lead dispatch/timing, discount funding/limits, attribution and exact earnings visibility. Sale cannot accept a Request merely because of the Sale role. |

## Butler context

| Dimension | UX model |
|---|---|
| Purpose | Execute scoped Stay preparation and destination operations. |
| Responsibilities | Prepare arrival; understand expected Stay; assist Check-in; support current Guest; record operational evidence/Incident; assist Checkout and readiness. |
| Resource scope | Assigned Property/Stay/operational task and destination services within assignment. |
| Important objects | Stay, Staying Party, Arrival, Access, Readiness, Incident, operational issue and assignment. |
| Action families | View upcoming/current work; assert readiness; coordinate arrival/check-in/out; record evidence and issue response. |
| Normally visible | Need-to-know arrival, Guest operational data, villa/readiness, access and issue information. |
| Normally not visible | Public Price, Guest payment amount, Owner payout, Sale commission, Stayora fee or full settlement ledger. |
| Dependencies | Butler platform eligibility, valid assignment, Stay scope, destination policy and operational capability. Approval is not assignment. |
| Open/TBD | Assignment changes, access lifecycle, issue severity/escalation and exact Guest fields. Butler does not accept Booking by default. |

## Destination / BQL context

| Dimension | UX model |
|---|---|
| Purpose | Coordinate destination-scoped arrivals, in-house operations, access and services. |
| Responsibilities | See operational occupancy; validate access; coordinate required registration/vehicle/service data; handle destination issues and exceptions in scope. |
| Resource scope | Destination, participating Properties/Stays and operational functions assigned to the staff relationship. |
| Important objects | Destination, Stay, Arrival/Departure, Access, Guest/vehicle operational data, Services, Issues and Incident. |
| Action families | Monitor destination operations; validate scoped access; coordinate services; record/escalate issues. |
| Normally visible | Destination operational occupancy, arrivals/departures, in-house information and fields required for the assigned function. |
| Normally not visible | Owner payout/tax, Sale commission, full commercial ledger, unrelated destination/property data. |
| Dependencies | Destination Staff relationship, function/capability, destination policy/configuration and need-to-know. |
| Open/TBD | QR rules/fields, retention, local integration and destination-specific services. Oceanami rules do not become global Core invariants. |

## Stayora Admin context

| Dimension | UX model |
|---|---|
| Purpose | Govern eligibility, verification, incidents, conflicts, money exceptions, leads and audit through explicit scoped actions. |
| Responsibilities | Review/resolve cases; support manual-assisted paths; enforce platform policy where authorized; preserve provenance and history. |
| Resource scope | Assigned domain/resource/function, not all business authority by default. |
| Important objects | Applications, Platform Eligibility, Verification Assessment/Review Cases, Inventory Conflicts, Incidents, Money/Settlement cases, Leads, Destinations and Audit. |
| Action families | Assess; assign; record evidence; apply explicit policy action; reconcile; correct through new fact/adjustment; audit. |
| Normally visible | Case evidence and source needed for the assigned function, status/outcome, authority basis, reason and audit history. |
| Normally not visible | Unrelated private data or unrestricted business ledgers merely because the user is Admin. |
| Dependencies | Human function/domain/resource authority, policy ownership, privacy scope and auditable reason. Admin access is not silent impersonation. |
| Open/TBD | Staff grants, escalation/SLA, appeals, retention and detailed case policy. |

## Cross-context guardrails

- The same Identity may occupy more than one context; each critical action keeps its acting capacity.
- Contextual visibility does not create commercial, operational or financial authority.
- Owner, Primary Host, Co-host, Sale and Butler are not interchangeable labels.
- A surface may hand off a domain object to another context without creating a duplicate object or changing its domain owner.
