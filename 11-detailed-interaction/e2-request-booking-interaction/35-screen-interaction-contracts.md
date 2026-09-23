# Screen Interaction Contracts

| Concept | Purpose / entry | Truth | Actions | Authority/revalidation | Outcomes/attention/handoff |
|---|---|---|---|---|---|
| Public discovery/date/Request (`PUB-01/03/04/05`) | discover and create intent | Destination, Property/Unit, Public Price, derived Availability/Bookability | select dates, Request intent | public projection; revalidate on submit | validation, Request exists/PENDING, conflict |
| Sale supply/option/Request (`SAL-01/02/03`) | prepare Sale-assisted intent | scoped supply, price/terms permitted, attribution | prepare/share/create Request | Sale scope; no Booking authority | Request PENDING → Host |
| Sale activity/outcome (`SAL-04/05`) | monitor outcome | Request/Booking projection, attribution | inspect/follow up | permitted visibility | pending/confirmed/rejected/exception |
| Host responsibility/Requests (`HST-01/03`) | surface decision | Request, Inventory, authority posture | open Request | Host scope; attention projection | pending/conflict/manual |
| Host Request Detail (`HST-04`) | decide Request | Request + accommodation/Guest/Inventory/commercial/provenance | accept/reject | Host/Co-host authority + revalidation | accepted/rejected/conflict/conditions |
| Host Booking Detail (`HST-05`) | inspect confirmed outcome | Booking, conditions, commitment | coordinate/handoff | resource scope | confirmed/pending exception |
| Guest outcome/Stay (`GST-01`) | understand result/access | Request/Booking/Stay basis | access only when legitimate | scoped Guest | pending/rejected/confirmed/unknown |

No layout, component, modal, drawer or microcopy is specified.
