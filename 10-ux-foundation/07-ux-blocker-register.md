# CP8-A — UX Blocker / TBD Register

> Status: **ACCEPTED AS CP8-B BASELINE** · **NOT FROZEN**

Classification is about whether the unresolved item prevents UX reasoning at this checkpoint. It does not resolve the item. CP8-A has no current **D — CP8 BLOCKER**: the canonical actor, surface, domain and lifecycle architecture is sufficient to create the UX foundation while preserving the open questions below.

## A — Not a UX blocker for CP8-A

| Question | Source | Affected actor / journey / surface | Why CP8-A can proceed | Recommended escalation |
|---|---|---|---|---|
| Exact Affiliate split, incentive and platform fee | [Foundation Money](../01-product-foundation/09-money-model.md), [ADR-P039](../00-start-here/DECISIONS.md#adr-p039) | Affiliate/Sale; later distribution and earnings | Affiliate is not a V0 proof target; CP8-A can preserve Sale/Affiliate boundaries without designing economics. | Founder / Money policy before Affiliate UX or detailed earnings. |
| Exact Commissionable Booking Value and tax/accounting treatment | [Foundation Money](../01-product-foundation/09-money-model.md) | Sale/Host/Admin; Commerce journey | Money/entitlement separation is known; amounts and legal treatment are not needed to define responsibility projections. | Founder + legal/accounting validation before financial UX freeze. |
| Verification evidence threshold, weighting and reassessment cadence | [CP4 Verification](../05-state-machines-policies/06-verification-and-reputation.md) | Host/Admin/Guest; trust surfaces | The UX foundation can distinguish Verified, Review Case and Identity Verification without designing the assessment. | Founder / Verification policy before Verification journey work. |
| Reputation weighting, decay, dispute and public projection | [CP4 Reputation](../05-state-machines-policies/06-verification-and-reputation.md) | Guest/Host/Sale/Admin; trust and quality surfaces | No universal score is canonical; signal boundaries are enough for CP8-A. | Founder / Reputation policy before public reputation UX. |
| Lead timing, dispatch, SLA and advanced distribution | [CP4 Lead](../05-state-machines-policies/08-lead-and-distribution-lifecycle.md) | Sale/Admin; Lead handoff | V0 allows manual assignment; CP8-A can model Lead as separate from Request/Booking. | Founder / Distribution policy before automation or critical lead journey. |
| Split stay, unit move and extension semantics | [CP7 persistence qualification](../09-database-design/04-booking-external-stay.md) | Host/Guest/Butler; non-happy-path Stay | CP8-A can treat the current one-unit/range direction as a qualified V0 simplification and keep future variants open. | Founder / Domain and Data Model before supporting journeys or persistence finalization. |
| Exact component, visual, responsive and implementation decisions | CP8 scope guardrail | All actors/surfaces | Explicitly outside CP8-A. | CP8-B and later Design System work. |

## B — Local UX blocker

| Question | Source | Affected actor / journey / surface | Why it matters locally | Recommended escalation |
|---|---|---|---|---|
| What exact Guest QR/link fields, expiry/revocation and privacy disclosure are required? | [CP6 Guest Access](../07-information-architecture/03-public-and-guest-ia.md), [CP3 open authority questions](../03-actor-authority/07-open-authority-questions.md) | Guest/BQL/Butler; access handoff | The surface and credential boundary are known, but field-level disclosure and lifecycle affect one access interaction. | Founder + privacy/destination policy before detailed Guest access work. |
| Which authority edge cases are actionable in a specific handoff (dual-capacity, delegation change, conflicting grants)? | [CP3 authority model](../03-actor-authority/00-authority-model.md) | Host/Co-host/Sale/Admin; Request/Inventory actions | The effective-permission model is sufficient for foundation, but a concrete action needs a safe route when authority is ambiguous. | Founder / Authority policy before action-level journey specification. |
| Which payment status copy and next action applies when provider outcome is `UNKNOWN`? | [CP4 Payment](../05-state-machines-policies/03-payment-lifecycle.md) | Guest/Sale/Host/Admin; confirmation/payment assurance | UX must not show failure or Default, but a journey needs an escalation/assistance path. | Founder / Payment and provider-reconciliation policy. |
| What minimum external operational information must be captured for a particular destination integration? | [CP5 external journey](../06-v0-scope/03-critical-journeys.md), [CP1 Oceanami pilot](../01-product-foundation/10-oceanami-pilot.md) | Host/Butler/BQL/Guest; External Booking → Stay | The principle is minimum operational truth, but field selection is destination- and privacy-sensitive. | Product Architect/Founder with destination operations. |

## C — Journey blocker, not CP8-A blocker

| Question | Source | Affected actor / journey / surface | Why the journey cannot be designed correctly without it | Recommended escalation |
|---|---|---|---|---|
| How should a true or late-discovered Inventory Conflict be resolved after preserving both commitments? | [CP4 cross-policy reconciliation](../05-state-machines-policies/21-cross-policy-reconciliation.md) | Host/Sale/Guest/Admin; request/external booking/conflict journey | The user needs a safe responsible decision and outcome; no channel priority is canonical. | Founder / Inventory and exception policy. |
| What grace/reconciliation path determines Payment Default after a due obligation misses its deadline? | [CP1 Oceanami policy](../01-product-foundation/10-oceanami-pilot.md), [CP4 Payment](../05-state-machines-policies/03-payment-lifecycle.md) | Guest/Sale/Host/Admin; payment assurance/confirmation | Required Payment Condition cannot stand in for future obligations; unresolved `UNKNOWN` cannot be shown as Default. | Founder + legal/payment validation. |
| What exact conditions permit cancellation, no-show, early departure, refund, remedy or exception Settlement? | [CP4 Settlement](../05-state-machines-policies/05-settlement-and-payout.md), [CP5 manual-assisted scope](../06-v0-scope/04-capability-matrix.md) | Guest/Host/Sale/Admin; exception/completion/settlement journey | The UX must show responsibility and next steps without promising an unselected economic outcome. | Founder / Booking, Money and legal policy. |
| What operational exception blocks Completion Readiness, and who decides it? | [CP4 Stay](../05-state-machines-policies/04-stay-lifecycle.md), [CP3 Incident](../04-core-workflows/05-incident-resolution.md) | Guest/Host/Butler/Admin; incident → completion journey | An Incident is not automatically a blocker; a qualifying list and authority are needed for a real journey. | Founder / Stay and Incident policy. |

## D — CP8 blocker

**None identified for CP8-A.** The checkpoint can establish principles, contexts, surfaces, object projections, semantics, traceability and prerequisites without selecting the unresolved policies above. A future CP8-B journey pass must re-evaluate the C-level items before specifying interactions.
