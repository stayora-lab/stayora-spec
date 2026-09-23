# Screen Disposition Matrix

All 42 D2 references are explicitly retained and classified.

| D2 ID | Name | Surface | D3 disposition | Parent responsibility | Anchor | Why / distinctions / authority | V0 trace |
|---|---|---|---|---|---|---|---|
| PUB-01 | Destination Discovery | Public | PRIMARY DESTINATION | Public discovery | Destination | repeated discovery; public scope | CP5/B3 |
| PUB-02 | Destination Detail | Public | CONTEXTUAL DESTINATION / DETAIL | Public discovery | Destination | detail reached from discovery; Destination distinct | CP5/B3 |
| PUB-03 | Accommodation Detail | Public | OBJECT DETAIL | Public discovery | Property + Unit | truth before intent; Property ≠ Unit; public projection | CP5/B3 |
| PUB-04 | Date & Availability Intent | Public | EMBEDDED / CONTEXTUAL VIEW | accommodation intent | Availability/Bookability | date selection is not a destination; derived truth | CP5/B3 |
| PUB-05 | Request Entry | Public | ACTION ENTRY / FLOW | guest intent | Request intent | action, not place; Guest intent → Host authority | CP5/B3 |
| GST-01 | Stay Hub | Guest | PRIMARY SCOPED ACCESS | Stay access | Stay | central Guest job; Stay ≠ Booking | B1–B4 |
| GST-02 | Arrival & Access | Guest | SCOPED ACCESS VIEW | Stay access | Stay/credential | scoped arrival action; credential ≠ authority | B1–B4 |
| GST-03 | Help & Operational Contact | Guest | EMBEDDED / ACTION ENTRY | Stay access | Stay/contact | contextual help; need-to-know | B4 |
| GST-04 | Review Entry | Guest | ACTION ENTRY | Stay access | Review Right | conditional action; Review ≠ Reputation | B4/CP5 |
| HST-01 | Responsibility Overview | Host | PRIMARY DESTINATION | Host attention | Property/attention | repeated responsibility and exceptions | B1–B5/C2 |
| HST-02 | Property & Unit | Host | PRIMARY DESTINATION / DETAIL | Properties | Property + Unit | durable representation; Unit stays contextual | C2/B5 |
| HST-03 | Request Collection | Host | PRIMARY DESTINATION / COLLECTION | Requests | Booking Request | repeated triage; Request ≠ Booking | B1/B3 |
| HST-04 | Request Detail | Host | OBJECT DETAIL / ACTION ENTRY | Requests | Booking Request | consequential decision; Host authority | B1/B3 |
| HST-05 | Booking Detail | Host | OBJECT DETAIL | Bookings & Stays | Booking | outcome truth; Booking ≠ Stay | B1/B3 |
| HST-06 | Stay Collection | Host | PRIMARY DESTINATION / COLLECTION | Bookings & Stays | Stay | operational collection; Stay independent | B4 |
| HST-07 | Stay Detail & Operations | Host | OBJECT DETAIL / EMBEDDED | Bookings & Stays | Stay | operations context; not Booking merge | B4 |
| HST-08 | External Accommodation Entry | Host | ACTION ENTRY / FLOW | External operations | External Accommodation | record/reconcile; no Stayora Booking | B2 |
| HST-09 | Inventory Intervention | Host | CONTEXTUAL DESTINATION / ACTION FLOW | Properties & Inventory | Commitment/Block | authorized mutation; Availability derived | B5 |
| HST-10 | Incident & Inventory Exception | Host | ATTENTION / EXCEPTION | Operations | Incident + Inventory projection | evidence → decision; Incident ≠ Block | B4/B5 |
| HST-11 | Operations Coordination | Host | EMBEDDED / CONTEXTUAL VIEW | Operations | Assignment/Stay | coordination from Stay/Property | B4/C4 |
| HST-12 | Money & Reconciliation | Host | EMBEDDED / CONTEXTUAL VIEW | relevant responsibility | Payment/Money projections | no Finance nav; need-to-know | CP5/B1 |
| SAL-01 | Supply Discovery | Sale | PRIMARY DESTINATION | Sale supply | Unit/Availability | durable distribution task; no Booking authority | B1/C3 |
| SAL-02 | Option & Offer Context | Sale | OBJECT DETAIL / CONTEXTUAL | Sale supply | Unit/Price | option preparation; policy scoped | B1/C3 |
| SAL-03 | Request Entry | Sale | ACTION ENTRY / FLOW | Sale activity | Request intent | Sale initiates; Host decides | B1 |
| SAL-04 | Sale Activity & Outcome | Sale | PRIMARY DESTINATION / COLLECTION | Sale activity | Request/Booking outcome | repeated monitoring; no CRM | B1/C3 |
| SAL-05 | Attribution & Earnings Summary | Sale | EMBEDDED / CONTEXTUAL VIEW | Sale activity | Attribution | attribution ≠ commission; economics TBD | B1/C3 |
| SAL-06 | Sale Exception | Sale | ATTENTION / EXCEPTION | Sale activity | Request/Booking exception | embedded attention where possible | B1 |
| BUT-01 | Today & Assignments | Butler | PRIMARY DESTINATION | Butler field operations | Assignment/Stay | current assigned work; field-critical | B4/C4 |
| BUT-02 | Stay / Assignment Detail | Butler | OBJECT DETAIL / CONTEXTUAL | Butler field operations | Stay + Assignment | assigned Stay truth; no commercial authority | B4/C4 |
| BUT-03 | Arrival / Check-in Entry | Butler | ACTION FLOW PLACEHOLDER | assigned Stay | Stay milestone | action, not navigation | B4/C4 |
| BUT-04 | Incident Entry & Detail | Butler | ATTENTION / ACTION ENTRY | assigned Stay | Incident | evidence/escalation; no Inventory control | B4/C4 |
| BUT-05 | Checkout Entry | Butler | ACTION FLOW PLACEHOLDER | assigned Stay | Stay completion | action, not navigation | B4/C4 |
| BQL-01 | Operations Today | BQL | PRIMARY DESTINATION | destination operations | arrivals/Stays | field-critical destination awareness | B2/B4 |
| BQL-02 | Stay Operations Collection | BQL | CONTEXTUAL COLLECTION | destination operations | Stay | active operation; no Booking ownership | B2/B4 |
| BQL-03 | Incident & Exception | BQL | ATTENTION / EXCEPTION | destination operations | Incident | destination scope; no super-admin | B4/B5 |
| BQL-04 | Access & Services Context | BQL | EMBEDDED / CONTEXTUAL VIEW | destination operations | service/access projection | local services only where canonical | B4 |
| ADM-01 | Applications & Eligibility | Admin | PRIMARY DESTINATION / GOVERNANCE | governance/attention | application/eligibility | manual assist; staff function | C1–C4 |
| ADM-02 | Property & Verification | Admin | OBJECT DETAIL / CONTEXTUAL | governance | Property/Verification case | Verification boundary preserved | C1/C2 |
| ADM-03 | Inventory & External Exceptions | Admin | ATTENTION / EXCEPTION | governance | conflict/External Accommodation | reconciliation; no universal control | B2/B5 |
| ADM-04 | Incident Governance | Admin | ATTENTION / EXCEPTION | governance | Incident/Finding | evidence/responsibility/consequence distinct | B4 |
| ADM-05 | Money Exceptions | Admin | ATTENTION / EXCEPTION | governance | Payment/Settlement exception | Money categories distinct | B1/B2 |
| ADM-06 | Audit & Provenance | Admin | SECONDARY DESTINATION / COLLECTION | governance | audit/provenance | durable governance inspection | C1–C4 |
