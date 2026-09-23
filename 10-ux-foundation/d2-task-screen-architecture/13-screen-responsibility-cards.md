# Screen Responsibility Cards

Cards use the same semantic contract for every concept: responsibility, user job, scope, anchor, information, attention, actions, entry/exit, partial condition, policy dependencies, device context, V0 and source trace. The inventory is the compact index; this file records the card-level invariants and representative cards.

## Card contract

- **Surface / working context:** one of seven D1 surfaces; Owner is contextual.
- **Primary responsibility / job:** the user goal that justifies the concept.
- **Scope / anchor:** canonical object or derived projection; no duplicate truth.
- **Information:** primary, supporting, action-decision and provenance needs.
- **Actions:** categories only; authority checked at execution.
- **Entry / exit:** accepted journey or onboarding handoff, not route design.
- **Empty / partial:** NO DATA, NO RELATIONSHIP, NO SCOPE, NO AUTHORITY, PENDING or CONFLICT/EXCEPTION.
- **Policy/device/V0/source:** unresolved policy is surfaced; device constraint is semantic.

## Representative cards

### PUB-03 — Accommodation Detail

Surface Public Marketplace · Type DETAIL · Job understand a Property/Unit proposition and trust before intent. Anchor Property/Bookable Unit with public Price, derived Availability and public Verification/Reputation projection. Primary information is accommodation truth; supporting information is Destination context; exception input is a permitted unavailable/bookability explanation. Action category is select date/intent; entry from PUB-01/PUB-02, exit to PUB-04/PUB-05. Empty/partial: no public Unit, unpublished Property, no eligible dates. Privacy PUBLIC. Device-neutral. Source CP5, CP6, B3, D1.

### GST-01 — Stay Hub

Surface Guest Stay Access · Type SCOPED ACCESS/OVERVIEW · Job access the represented Stay truth. Anchor Stay plus accommodation basis and milestone. Primary information is dates, Property/Unit and current canonical Stay state; supporting is scoped operational contact; attention is Stay exception. Actions are access arrival/help/review entry only. Entry from confirmed Booking/External Stay → Stay handoff; exit GST-02/GST-03/GST-04. Empty/partial: no valid scope, pending/unknown access, unresolved exception. Privacy relationship/resource scoped. Mobile-important. Source B1–B4, D1.

### HST-04 — Request Detail

Surface Host Workspace · Type DETAIL/ACTION ENTRY · Job decide an authorized Booking Request. Anchor Booking Request with inventory and payment-condition projections, without turning them into Request state. Primary information is Request context and dates; action-decision information is accepted/rejected consequences; attention includes external conflict or Payment UNKNOWN. Actions accept/reject categories only. Entry HST-03; exit Booking outcome or exception handoff. No-authority and conflict conditions are explicit. Desktop-important, mobile-important where field work requires. Source B1/B3/B5, CP3/CP4/CP7.

### SAL-02 — Option & Offer Context

Surface Sale Workspace · Type DETAIL/ACTION ENTRY · Job prepare/share an eligible option. Anchor Property/Unit, public Price, Availability/Bookability and active Distribution Relationship. Actions prepare/share/request only; no Booking or Inventory mutation. Entry SAL-01; exit SAL-03 or SAL-04. Privacy commercial need-to-know. Mobile-important. Source B1/C3/D1.

### BUT-02 — Stay / Assignment Detail

Surface Butler Context · Type DETAIL · Job prepare and operate an assigned Stay. Anchor Stay + Butler Assignment + Property/Unit. Primary information is readiness/arrival/operation; attention is Incident/evidence. Actions readiness evidence, check-in/out entry and incident entry according to authority. Entry BUT-01; exit BUT-03/04/05. No commercial/Inventory action. Field-critical. Source B4/C4/D1.

### BQL-01 — Operations Today

Surface Destination/BQL · Type OVERVIEW · Job understand scoped destination operations today. Anchor arrivals/departures, active Stays, incidents and local service/access projections. Actions coordinate/escalate only where destination authority exists. Entry from BQL context activation; exit BQL-02/03/04. No Host/Booking/Inventory authority. Field-critical. Source B2/B4/D1.

### ADM-03 — Inventory & External Exceptions

Surface Admin · Type ATTENTION/EXCEPTION · Job inspect provenance and support reconciliation. Anchor Inventory conflicts and External Accommodation facts. Primary information is evidence/provenance; action categories manual-assisted reconciliation/escalation. Entry ADM-01 or attention; exit responsible Host/Operations/authority. Admin function/resource-scoped, audit required. Desktop-important. Source B2/B5/C1/D1.

## Complete card index

The following compact cards cover every inventory identifier. Detailed interaction is intentionally omitted.

| ID | Responsibility / primary job | Scope / anchor | Action categories | Entry → handoff | Empty/partial · device · V0 |
|---|---|---|---|---|---|
| PUB-01 | Discover Destinations | Public Destination | select destination | public entry → PUB-02 | no public Destinations · neutral · MUST BUILD |
| PUB-02 | Understand Destination proposition | Destination/public trust | inspect/select supply | PUB-01 → PUB-03 | unpublished/no supply · neutral · MUST BUILD |
| PUB-03 | Understand Property/Unit truth | Property + Unit/public trust | date/intent | PUB-01/02 → PUB-04/05 | unpublished/no Unit · neutral · MUST BUILD |
| PUB-04 | Select date/availability intent | derived Availability/Bookability | select intent | PUB-03 → PUB-05 | no dates/conflict · neutral · MUST BUILD |
| PUB-05 | Initiate Direct Guest Request | Request intent | submit Request intent | PUB-04 → Host Request | no valid intent · mobile-important · MUST BUILD |
| GST-01 | Access Stay truth | Stay + accommodation basis | arrival/help/review entry | Booking/External Stay → GST-02/03/04 | no scope/exception · mobile-important · MUST BUILD |
| GST-02 | Understand arrival/access and use credential | Stay + scoped credential | access/check-in guidance | GST-01 → Butler/BQL/Host | credential pending/invalid scope · mobile-important · MUST BUILD |
| GST-03 | Contact correct operational actor | Stay + need-to-know contact | contact/escalate | GST-01/02 → operations | no contact/need-to-know limit · mobile-important · MUST BUILD |
| GST-04 | Enter eligible review | Review Right + Stay | review entry | GST-01 → Review | not eligible/pending completion · neutral · MUST BUILD |
| HST-01 | Understand current Property responsibility | Property/Unit + attention projections | open scoped task | context entry → collections | no scope/no attention · desktop-important · MUST BUILD |
| HST-02 | Maintain Property/Unit representation | Property + Unit | authorized representation/publication | HST-01 → Public/Admin | unpublished/pending verification · desktop-important · MUST BUILD |
| HST-03 | Triage Booking Requests | Request collection | open Request | HST-01/Sale → HST-04 | no Requests · desktop-important · MUST BUILD |
| HST-04 | Decide Request | Booking Request | accept/reject | HST-03 → Booking/exception | no authority/conflict/Payment UNKNOWN · desktop-important · MUST BUILD |
| HST-05 | Understand Booking truth | Booking + commitments/payment projection | inspect/coordinate | HST-04 → Guest/operations | no Booking/out of scope · desktop-important · MUST BUILD |
| HST-06 | Triage upcoming/current Stays | Stay collection | open Stay | HST-01 → HST-07 | no Stays · desktop-important · MUST BUILD |
| HST-07 | Coordinate Stay operations | Stay + operations milestones | coordinate/handoff | HST-06/Booking → Butler/BQL | Stay exception · desktop/mobile · MUST BUILD |
| HST-08 | Record External Accommodation | External Accommodation | authorized record | B2/reporting → Inventory/Stay | no authority/conflict · desktop/mobile · MUST BUILD/manual |
| HST-09 | Evaluate Inventory intervention | Inventory Commitment/Block | create/correct authorized block | HST-01/HST-10 → Availability | policy/authority conflict · desktop-important · MUST BUILD/manual |
| HST-10 | Respond to Incident/inventory exception | Incident/Finding + Inventory | evidence/escalate/consequence request | attention → authority | unresolved conflict · desktop/mobile · MANUAL-ASSISTED |
| HST-11 | Coordinate Butler/operations | Butler Assignment + Stay | assign/coordinate if authorized | HST-07 → Butler | unassigned/no authority · desktop/mobile · MUST BUILD |
| HST-12 | View authorized Money truth | Payment/Entitlement/Settlement/Payout projections | inspect/reconcile | HST-04/05 → Admin/finance | Payment UNKNOWN/no scope · desktop-important · MUST BUILD/manual |
| SAL-01 | Find truthful supply | Property/Unit + Availability/Bookability | discover/select | Sale context → SAL-02 | no relationship/supply · mobile-important · MUST BUILD |
| SAL-02 | Prepare/share option | Unit + Public Price + relationship | prepare/share | SAL-01 → SAL-03 | no permitted commercial data · mobile-important · MUST BUILD |
| SAL-03 | Create Sale Booking Request | Request intent | initiate Request | SAL-02 → Host HST-03/04 | missing Guest intent · mobile-important · MUST BUILD |
| SAL-04 | Track Sale outcome | Request/Booking projection | monitor/escalate | SAL-03 → Guest/Host | no relationship/outcome pending · mobile-important · MUST BUILD |
| SAL-05 | Understand permitted attribution | Sale attribution | inspect permitted outcome | SAL-04 → reconciliation | no entitlement/policy TBD · desktop/mobile · MUST BUILD/manual |
| SAL-06 | Resolve Sale exception | Request/Booking exception | escalate/manual assist | SAL-04 → Host/Admin | conflict/unknown · mobile-important · MANUAL-ASSISTED |
| BUT-01 | Understand today's assignments | Butler Assignment + Stay collection | open assigned Stay | context entry → BUT-02 | unassigned/no upcoming · field-critical · MUST BUILD |
| BUT-02 | Prepare/operate assigned Stay | Stay + Property/Unit + Assignment | readiness/evidence/support | BUT-01 → BUT-03/04/05 | no Assignment/out of scope · field-critical · MUST BUILD |
| BUT-03 | Perform authorized Check-in | Stay milestone | check-in entry | BUT-02 → Stay/Guest | authority/readiness missing · field-critical · MUST BUILD |
| BUT-04 | Record Incident/evidence | Incident/Finding | report/escalate | BUT-02 → HST/BQL/Admin | no scope/evidence pending · field-critical · MUST BUILD/manual |
| BUT-05 | Support Checkout | Stay completion evidence | checkout entry | BUT-02 → completion handoff | not eligible/exception · field-critical · MUST BUILD |
| BQL-01 | Understand destination operations today | destination arrivals/departures/Stays | coordinate/escalate | BQL context → BQL-02/03/04 | no scope/no activity · field-critical · MUST BUILD |
| BQL-02 | Inspect active Stay operations | Stay collection + external coverage | open Stay | BQL-01 → operations | no active Stays · field-critical · MUST BUILD |
| BQL-03 | Inspect destination Incident | Incident/Finding | escalate/coordinate | BQL-01/02 → responsible authority | no authority/exception · field-critical · MUST BUILD/manual |
| BQL-04 | Support access/services | Destination service/access projection | authorized service action | BQL-01 → Guest/Butler | service unavailable/no scope · mobile-important · MUST BUILD/manual |
| ADM-01 | Review eligibility/relationships | applications/eligibility | review/assist | partial context → applicant/relationship | pending/no case · desktop-important · MUST BUILD/manual |
| ADM-02 | Govern Property/Verification case | Property + Verification case/status | inspect/assist | ADM-01 → Property/Public | pending evidence/no scope · desktop-important · MUST BUILD/manual |
| ADM-03 | Reconcile Inventory/external exception | Inventory conflict + External Accommodation | inspect/evidence/escalate | attention → Host/Operations | unresolved conflict · desktop-important · MUST BUILD/manual |
| ADM-04 | Govern Incident exception | Incident/Finding/Responsibility | inspect/escalate | attention → responsible authority | no case/unknown consequence · desktop-important · MUST BUILD/manual |
| ADM-05 | Inspect Money exception | Payment/Settlement/Payout exception | reconcile/escalate | attention → finance authority | Payment UNKNOWN/no scope · desktop-important · MUST BUILD/manual |
| ADM-06 | Inspect audit/provenance | Audit/event/provenance projection | inspect/export where canonical | any governed context → source authority | no scope/private · desktop-important · MUST BUILD/manual |
