# CP8-A — Surface Responsibility Model

> Status: **ACCEPTED AS CP8-B BASELINE** · **NOT FROZEN**

This is a responsibility model derived from CP6. It is not a sitemap, route map, screen specification or component inventory. Surfaces are contextual projections over shared domain truth; each action still passes the CP3 effective-permission model.

## Public Marketplace

**Who enters and why.** Guest, prospective Guest and Sale enter to discover eligible supply, compare options and progress demand.

**Responsibilities supported.** Destination discovery; listing/property understanding; Availability and Public Price inspection; trust-signal interpretation; Request or consultation entry.

**Canonical objects.** Destination, Property/Listing, Bookable Unit, derived Availability, Public Price, Stayora Verified signals, relevant Offer/Request entry.

**Actions that belong.** Discover, search, inspect, compare, request and enter a Sale-assisted path where supported.

**Actions that do not belong.** Host acceptance, Inventory commitment administration, Owner Blocks, Butler assignment, payout administration, Verification decisions or private evidence.

**Handoffs and boundaries.** Request hands to Host/authorized Booking Authority; consultation hands to Lead/Sale. The same Inventory Truth is used by Host and Sale. Non-Verified supply may remain visible when otherwise eligible; Verified is not a marketplace admission or luxury label.

**V0.** Public discovery, listing detail, Availability, Public Price, trust signals and Request/consultation entry support Commerce Validation and Inventory Trust.

## Guest Stay Access

**Who enters and why.** A Guest or Staying Party member with a valid scoped confirmation/link/QR enters to prepare for, access and use a Stay.

**Responsibilities supported.** View relevant Stay, arrival, villa, Butler, Destination, access and help information; provide operational information when required; report issues; review when eligible.

**Canonical objects.** Booking or External Accommodation basis, Stay, Staying Party, Access credential, Destination operations, Incident and Review Right.

**Actions that belong.** Scoped access and operational participation; issue reporting; eligible review.

**Actions that do not belong.** Request acceptance, Inventory edits, public price changes, owner finance, Sale commission, or universal access from merely holding a QR.

**Handoffs and boundaries.** Booking/External Accommodation may establish a Stay; external origin remains visible where it affects expectations. Access is scoped and does not rewrite commercial provenance. Exact Guest data, QR lifecycle, consent and privacy remain open.

**V0.** Confirmation, scoped QR/link, arrival/check-in support, Stay operations, checkout and eligible review support Destination Stay Coverage and Commerce Validation.

## Host Workspace

**Who enters and why.** Legal Owner, Primary Host, Co-host or another actor with valid scoped Property/Inventory/Booking authority enters to operate supply and respond to demand.

**Responsibilities supported.** Maintain Property/Listing; manage Availability/Blocks; review Requests; confirm eligible Booking; register external accommodation facts/commitments when authorized; coordinate Stays, people, quality and own scoped Money views.

**Canonical objects.** Party/Identity relationships, Destination, Property, Bookable Unit, Inventory Commitments, derived Availability, Request, Booking, Stay, Butler relationship, Incident, Verification and financial projections.

**Actions that belong.** Authority-scoped edit/publish, inventory action, accept/reject, external record, delegate/assign and exception response.

**Actions that do not belong.** Treating Request as a Booking, overwriting another commitment, using ownership as automatic authority, changing Sale economics unilaterally, or treating Calendar as a second availability calculator.

**Handoffs and boundaries.** Request → authorized Host decision; Booking → Stay/Guest Access/Operations; Issue → Incident or Availability Block where authority and policy support it. External Booking is referenced by Inventory/Stay and does not need a Stayora Booking.

**V0.** Host supply, Inventory, Requests, Bookings/Stays, external registration, conflict surfacing, operations and basic audit support all four CP5 dimensions and integrity.

## Sale Workspace

**Who enters and why.** An approved and eligible Sale enters to find supply, manage demand and monitor attributable commerce.

**Responsibilities supported.** Search actual Availability; inspect fit, Public Price and trust signals; prepare/share offer; create and monitor Request; monitor attributed Booking/Stay; view own economics where supported.

**Canonical objects.** Destination, Property/Listing, Bookable Unit, Availability, Public Price, Lead, Request, Booking, Stay and Sale attribution/entitlement projection.

**Actions that belong.** Search, compare, quote/share, create Request, track status, support payment assurance and view own attribution/earnings when V0 supports it.

**Actions that do not belong.** Accept Request by Sale role alone, block Inventory, modify Host-controlled price, see Owner payout/tax/full ledger, or treat whitelist as an Instant Book permission bundle.

**Handoffs and boundaries.** Lead can progress to Request; Host/authorized Co-host decides; confirmed commerce converges on shared Booking/Stay truth; operational handoff goes to Butler/BQL. Sale reporting an external booking does not itself establish authoritative Inventory Truth.

**V0.** Find a Villa, Leads, Requests, Bookings, Earnings and scoped network relationships support Network Adoption and Commerce Validation. Full CRM, ranking and advanced dispatch are deferred.

## Butler Context

**Who enters and why.** An approved Butler with a valid Property/Stay assignment enters to execute operational work.

**Responsibilities supported.** Prepare arrivals; see expected/current Stays; assist Check-in/out; assert operational readiness; record incidents and evidence; support Guest operations.

**Canonical objects.** Stay, Arrival/Departure, Access, Staying Party operational data, Readiness, Incident, assignment and destination service.

**Actions that belong.** View assigned work, coordinate operations, record evidence and escalate issues.

**Actions that do not belong.** Accept Booking Request, set Public Price, change Inventory without authority, see unrelated financial information or impose financial/reputation consequences.

**Handoffs and boundaries.** Booking/External Accommodation → Stay; Host/BQL may provide scoped operational context; Incident can be consumed by Money, Reputation or Verification under their own policies.

**V0.** Today, Upcoming, Stays and Issues validate Destination Stay Coverage and Network Adoption; full housekeeping/work-order tooling is deferred.

## Destination / BQL Context

**Who enters and why.** Destination Staff/BQL with a destination-scoped relationship enters to coordinate access, arrivals, in-house operations, services and issues.

**Responsibilities supported.** Monitor destination operational occupancy; validate current Stay access; coordinate registration, vehicles/services and destination issues within assigned function.

**Canonical objects.** Destination, Stay, Arrival/Departure, Access, operational Guest/vehicle data, Services, Incident and Issue.

**Actions that belong.** Destination-scoped operational monitoring, access validation, service coordination and issue escalation.

**Actions that do not belong.** Owner payout/tax, Sale commission, full commercial ledger, Host Inventory authority or universal BQL control over pricing.

**Handoffs and boundaries.** Access exceptions go to BQL/Admin or responsible operator; operational issues can hand to Host/Butler/Incident. Destination policy/configuration remains local and does not become a Core invariant.

**V0.** Today, Arrivals, In House, Departures, Access, Villas, Services and Issues validate Destination Stay Coverage and Network Adoption.

## Stayora Admin

**Who enters and why.** Stayora staff with explicit domain/function/resource authority enters to resolve exceptions, assess applications/cases, enforce policy and preserve auditability.

**Responsibilities supported.** Application/eligibility review; Verification assessment/review; Incident and Inventory Conflict handling; Money/Settlement exception support; Lead assignment; destination configuration; audit.

**Canonical objects.** Application, Platform Eligibility, Verification Assessment/Review Case and Status, Incident/Finding, Inventory Conflict, Payment/Settlement, Lead/Assignment, Destination and Audit.

**Actions that belong.** Assess, assign, record evidence, apply explicit policy action, reconcile, correct through new fact/adjustment and audit.

**Actions that do not belong.** Act as a universal super-user, impersonate Owner/Host/Sale/Guest, select conflict winners without policy, overwrite historical financial truth or make every open Review Case a status change.

**Handoffs and boundaries.** Admin action must preserve actual staff identity, capacity, authority source, reason, resource and time. Manual assistance is an auditable path, not a new source of domain truth.

**V0.** Exception/governance capability is MANUAL-ASSISTED where CP5 says so; no analytics-first or unrestricted admin surface is implied.

## Surface handoff rule

Cross-surface navigation follows responsibility and contextual lifecycle handoff. A handoff changes the actor's perspective or action owner; it does not create a duplicate Booking, Stay, Incident or Inventory record. The domain truth remains shared and the CP3 authority test remains in force.
