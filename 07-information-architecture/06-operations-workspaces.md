# Operations Workspaces

> Status: **STABLE — CHECKPOINT 6 DOCUMENTED; NOT IMPLEMENTATION FREEZE**

## Butler context

```text
BUTLER
├── Today
├── Upcoming
├── Stays
└── Issues
```

Primary object is Stay: arrivals, in-house stays, departures, readiness, check-in, checkout, incident reporting and operational updates. Butler is operational, not commercial; operational observation does not imply commercial authority. Butler does not need Public Price, Guest payment amount, Owner payout, Sale commission, Stayora fee or Owner settlement ledger. Reporting an unusable villa may support an Incident or block review under policy, but does not itself authorize commercial consequences.

## Destination / BQL context

```text
OCEANAMI OPERATIONS
├── Today
├── Arrivals
├── In House
├── Departures
├── Access
├── Villas
├── Services
└── Issues
```

BQL needs destination-operational occupancy, arrivals/departures, guest counts, required registration, access validation, vehicle information where policy requires, service requests and relevant issues. Operational Occupancy is distinct from Commercial Availability. BQL does not receive unnecessary booking economics, Sale commission, Owner payout/tax or full commercial ledger.

QR/access answers whether access is valid for the current Stay/context; invalid or unverified access supports escalation and is not an automatic universal denial rule. Vehicle, gate, cart and other Oceanami capabilities remain Destination configuration, not universal Core invariants. Full housekeeping workforce management and maintenance/work-order suites are deferred.
