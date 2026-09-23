# Invariants and Stress Tests

> Status: **STABLE — CP7 ARCHITECTURE REVIEWED; NOT IMPLEMENTATION FREEZE**

## Cross-cutting invariants

- One Identity may hold multiple capacities; acting capacity and authority basis are recorded per critical action.
- Request does not reserve Inventory; Booking starts at CONFIRMED; Booking ≠ Stay.
- Availability is derived from effective Inventory Commitments; no channel priority; physical absence does not release a valid commitment.
- External Accommodation is not a fake Stayora Booking; authoritative external commitments have equal inventory effect; facts and conflicts are both preserved.
- Ownership, relationship, authority and assignment remain distinct and temporally valid.
- Payment UNKNOWN is unresolved; Payment ≠ Entitlement; Settlement ≠ Payout.
- Public Price and funding attribution remain historical Commercial Snapshot; Sale-funded discount does not silently reduce Owner entitlement.
- Earned history, successful transactions and payouts are corrected by later adjustments/reversals, not destructive rewriting.
- Incident, Finding, Responsibility and Consequence remain separate.
- Verification Assessment/Review Cases are separate from Status; Review Case may coexist with VERIFIED; Review Right is evidence/eligibility based; no universal TrustScore.
- Operational participation does not rewrite commercial provenance.

## Stress-test results

**PASS:** concurrent Requests/inventory race; authority revocation; Payment UNKNOWN; Sale-funded discount; pre-arrival property failure; no-show; post-settlement refund; post-payout correction; late complaint; Verification Review while VERIFIED; Admin correction; dual-capacity Sale + Co-host.

**REFINEMENTS:** R1 — late External Accommodation fact versus Inventory Conflict; R2 — Booking/commercial changes require amendment/supersession semantics; R3 — important relationships/authority require temporal validity. No foundation-level reopen was required.

These results validate the conceptual model; they do not close policy, legal, measurement or physical implementation TBDs.
