# Screen Consolidation Review

The initial task inventory was reduced where responsibility and object semantics allow, then kept separate where they do not.

| Candidate merge | Decision | Reason |
|---|---|---|
| PUB-01 + PUB-02 | Keep separate conceptually | Destination discovery and Destination truth/detail have different jobs; implementation may compose them later. |
| PUB-03 + PUB-04 | Keep separate | Accommodation proposition vs date/availability intent; derived Availability/Bookability needs a distinct decision step. |
| GST-01 + GST-02 | Keep distinct but adjacent | Stay truth and scoped credential/arrival task differ; can share a contextual access surface later. |
| HST-03 + HST-04 | Keep distinct | Collection triage vs consequential Request decision. |
| HST-05 + HST-07 | Keep distinct | Booking and Stay are different canonical objects/lifecycles. |
| HST-10 + ADM-03 | Keep distinct | Host consequence responsibility vs Admin reconciliation/governance. |
| SAL-04 + SAL-06 | Consolidate attention into activity projection | Both concern Sale outcome; a separate exception view is only a structural projection when exception context requires it. |
| BUT-01 + BUT-02 | Keep distinct conceptually | Today triage vs assigned Stay operation; later mobile composition is open. |
| BQL-01 + BQL-02 | Keep distinct conceptually | Today awareness vs collection of active Stays. |

No screen remains without a justified primary/supporting task. No merge collapses Request/Booking/Stay, Property/Unit, Incident/Maintenance Block or Payment/Entitlement/Settlement/Payout.
