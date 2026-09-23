# B5 — Maintenance / Unusable Inventory Journey

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Boundary

```text
Operational report / Incident / evidence
        ≠
Maintenance Block decision
        ≠
Maintenance management software
```

## Canonical path

```text
Guest / Butler / BQL / Host reports condition
  → evidence and scope assessment
  → authorized Inventory decision
  → Maintenance Block where supported
  → derived Availability / conflict projection
  → authoritative release or correction
```

Butler/BQL/Guest may report an unusable condition within their operational scope. Reporting or assignment does not grant Inventory Authority. A Host or other explicitly authorized Inventory actor/Staff context may assess/establish the Maintenance Block where canonical authority/policy supports it. Exact assessor, evidence threshold, range and grant remain TBD.

## Existing truth

A Maintenance Block does not silently cancel Booking, delete External Accommodation, cancel Stay, refund, compensate, assign blame or rewrite Incident history. Existing commitments and Stays remain recorded; overlap becomes Inventory Conflict/exception and follows separate policy.

## V0 limit

B5 documents the intervention boundary only. It does not create repair workflow, work orders, workforce scheduling, maintenance management, automatic relocation or compensation.
