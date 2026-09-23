# Aggregate and Projection Map

> Status: **STABLE — CP7 ARCHITECTURE REVIEWED; NOT IMPLEMENTATION FREEZE**

The following are conceptual aggregate candidates, not ORM/table decisions.

| Area | Candidate business object | Conceptual form |
|---|---|---|
| Identity & Authority | Identity, Party, Authority Grant | Candidate Aggregate Roots |
| Relationships | Actor Relationship, Platform Eligibility | Lifecycle / candidate root |
| Supply | Destination, Property | Candidate Aggregate Roots |
| Supply detail | Bookable Unit | Entity within Property for V0 |
| Commerce & Inventory | Booking Request, Inventory Commitment, Booking, External Accommodation | Candidate Aggregate Roots |
| Operations | Stay, Incident | Candidate Aggregate Roots |
| Money | Payment Obligation, Payment Transaction, Settlement, Payout | Candidate Aggregate Roots |
| Quality | Verification Assessment Case, Verification Review Case | Candidate Aggregate Roots |
| Quality decisions | Verification Decision | Immutable decision/history record |
| Trust | Review Right, Review | Eligibility record / candidate root |

Derived/projection concepts include Availability, Reputation, Search Index, Calendar View, Host Dashboard, Sale Earnings View, Destination Today and Verification Summary. They are not canonical business truth and must not become alternate domain ownership.

Cross-aggregate workflows are not one giant transaction. Host acceptance may orchestrate Request acceptance, Temporary Commitment and payment requirements without creating Booking. Satisfied conditions may orchestrate Booking confirmation, Confirmed Accommodation Commitment, temporary supersession and Stay scheduling. Physical transaction mechanisms remain later design.
