# B2 — Domain / Workflow / Authority Gap Findings

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

No new aggregate, actor, permission or state is proposed. Findings identify where existing concepts are present but policy/workflow detail is insufficient for later interaction design.

## B2-G01 — External Report to authoritative fact boundary

**Classification:** POLICY / AUTHORITY GAP (not a missing domain concept).

**Observed need.** Stayora needs to distinguish a report from a trusted External Accommodation Fact before changing Inventory or creating a Stay representation.

**Existing concepts.** External Accommodation, Record External Commitment capability, provenance/evidence, Inventory Conflict and Stay.

**Why insufficient for detail.** Grant/revoke, evidence threshold, confidence, reviewer and exact acceptance timing remain TBD.

**Affected phase/actors.** Report/evaluation; Host, Owner, Co-host, Sale, Admin, Inventory.

**Impact.** UX cannot finalize “accepted/authoritative” action or guarantee dates from a report.

**Sources.** [CP3 external commitment capability](../../03-actor-authority/02-authority-capabilities.md), [WF-03](../../04-core-workflows/03-external-booking-to-stay.md), [CP7 provenance](../../08-conceptual-data-model/08-provenance-temporal-history.md).

**Escalation.** Founder/Product Architect + Authority/Inventory policy. Do not invent a verification workflow.

## B2-G02 — External Fact to Inventory Commitment timing

**Classification:** WORKFLOW / POLICY GAP.

**Observed need.** A fact may be sufficient for operations but not yet establish a protected Inventory Commitment, or vice versa.

**Existing concepts.** External Accommodation Fact, Confirmed Accommodation Commitment, Availability derived model.

**Why insufficient for detail.** The architecture permits Inventory and/or Stay branches but does not select when every accepted fact must create a commitment.

**Affected phase/actors.** Inventory; Host, Sale, Admin, Guest.

**Impact.** Availability/Bookability and conflict UX cannot promise a universal timing.

**Sources.** [CP3 WF-03](../../04-core-workflows/03-external-booking-to-stay.md), [CP4 Inventory](../../05-state-machines-policies/01-inventory-commitment-model.md).

**Escalation.** Founder/Inventory policy. Keep fact, commitment and Availability visibly distinct.

## B2-G03 — Conflict resolution

**Classification:** POLICY / WORKFLOW GAP.

**Observed need.** External facts can overlap Stayora Booking, Temporary Commitment, Owner/Maintenance Block or another external source.

**Existing concepts.** Inventory Conflict/Exception, effective commitments, provenance/history.

**Why insufficient for detail.** No source priority or winner/remediation rule is confirmed.

**Affected phase/actors.** Host, Guest, Butler, BQL, Admin, Inventory.

**Impact.** UX can surface the conflict and owner of next action, but not finalize resolution, cancellation or compensation.

**Sources.** [CP4 cross-policy reconciliation](../../05-state-machines-policies/21-cross-policy-reconciliation.md), [CP7 inventory](../../08-conceptual-data-model/04-inventory-booking-external-accommodation.md).

**Escalation.** Founder/Inventory and exception policy.

## B2-G04 — Late/corrected external truth

**Classification:** WORKFLOW / HISTORY POLICY GAP.

**Observed need.** External information may arrive late, be corrected, withdrawn or be completed before registration.

**Existing concepts.** Amendment, supersession, replacement fact, correction action, temporal validity and immutable history.

**Why insufficient for detail.** Exact effective-time and downstream release/recompute rules are not selected.

**Affected phase/actors.** Reporter, Host, Inventory, Stay, Admin, Reputation.

**Impact.** Later journey work cannot specify the exact correction interaction.

**Sources.** [CP7 provenance/history](../../08-conceptual-data-model/08-provenance-temporal-history.md), [CP3 WF-03](../../04-core-workflows/03-external-booking-to-stay.md).

**Escalation.** Founder/Domain Architect before detailed correction UX or persistence implementation.

## B2-G05 — Guest access/privacy boundary

**Classification:** UX INTERACTION / PRIVACY GAP.

**Observed need.** External Guests may receive scoped Stay Access without Stayora-originated commerce.

**Existing concepts.** Stay, Staying Party, Guest relationship, QR/link concept, destination-scoped access.

**Why insufficient for detail.** Exact fields, lifecycle, consent, authentication and retention are intentionally open.

**Affected phase/actors.** Guest, Butler, BQL, Host.

**Impact.** B2 can specify prerequisites and boundaries but not QR/privacy interaction.

**Sources.** [CP6 Guest Access](../../07-information-architecture/03-public-and-guest-ia.md), [CP8-A blocker register](../07-ux-blocker-register.md).

**Escalation.** Founder/privacy/destination policy before detailed access work.

## No V0-scope or domain expansion

No Channel Manager, PMS, OTA integration platform, external accounting, CRM, Affiliate, Managed Operations or new domain aggregate is required to state B2. Manual-assisted source entry remains a V0 integrity path only where CP5 supports it.
