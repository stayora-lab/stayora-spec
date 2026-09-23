# B1 — Domain / Workflow / Authority Gap Findings

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

The review looked for concepts needed by the Sale-assisted journey that are absent upstream. No new aggregate, entity, role, permission or state is proposed.

## Finding B1-G01 — Offer ownership and lifecycle boundary

**Classification:** DOMAIN / WORKFLOW GAP (already recorded upstream as TBD; not newly created by B1).

**Observed need.** Sale must present a coherent option/terms package before creating a Request.

**Why current concepts are insufficient for later detailed UX.** `Offer` exists as a conceptual proposition, but its ownership, lifecycle, validity/amendment behavior and persistence boundary are explicitly open. B1 can refer to an Offer presentation, but cannot specify its exact object behavior.

**Affected phase/actors.** Discovery and Guest Choice; Sale, Guest, Host.

**Potential impact.** Later detailed journey work cannot finalize quote validity, change/expiry or exact audit behavior.

**Source evidence.** [CP2 Offer glossary](../../02-domain/01-domain-glossary.md), [CP2 domain map](../../02-domain/00-domain-map.md), [CP4 Booking policy](../../05-state-machines-policies/12-booking-and-commitment-policy.md).

**Recommended escalation.** Founder/Product Architect decision before detailed Offer/quote interaction. Do not create a new Offer aggregate in B1.

## Finding B1-G02 — Request unanswered / missing authority outcome

**Classification:** POLICY / WORKFLOW GAP.

**Observed need.** A Request must reach a valid Host/Booking Authority, but no complete timeout, reassignment or no-authority behavior is confirmed.

**Why current concepts are insufficient.** Request lifecycle is known, but notification, expiry, escalation and authority-precedence rules remain open.

**Affected phase/actors.** Host Decision; Sale, Guest, Host/Co-host, Admin.

**Potential impact.** A detailed journey could not safely promise a response time or automatic outcome.

**Source evidence.** [CP4 Request lifecycle](../../05-state-machines-policies/02-booking-request-and-booking.md), [CP3 authority questions](../../03-actor-authority/07-open-authority-questions.md).

**Recommended escalation.** Founder/Booking/Authority policy. B1 keeps the branch visible without inventing an SLA.

## Finding B1-G03 — Payment/inventory policy boundary

**Classification:** POLICY GAP, not a domain gap.

**Observed need.** After acceptance, the journey needs a safe result for temporary commitment, Required Payment Condition, Payment `UNKNOWN` and conflict.

**Why current concepts are insufficient.** The domain objects and distinctions exist; exact windows, grace, reconciliation, conflict resolution and economic consequences do not.

**Affected phase/actors.** Inventory and Payment; Guest, Sale, Host, Admin.

**Potential impact.** Expiry, retry, Default, release, refund and confirmation branches cannot be finalized.

**Source evidence.** [CP4 cross-policy reconciliation](../../05-state-machines-policies/21-cross-policy-reconciliation.md), [CP1 Oceanami payment policy](../../01-product-foundation/10-oceanami-pilot.md).

**Recommended escalation.** Founder + Money/Inventory/legal validation. Do not add a state or policy in B1.

## Finding B1-G04 — Guest access data boundary

**Classification:** UX INTERACTION / PRIVACY GAP, not a new domain gap.

**Observed need.** A confirmed Booking must hand off to scoped Guest Stay Access.

**Why current concepts are sufficient but incomplete for detail.** Booking, Stay, Staying Party and scoped QR/link exist; exact fields, lifecycle, consent and retention remain open.

**Affected phase/actors.** Booking → Stay Access; Guest, Butler, BQL, Host.

**Potential impact.** Exact confirmation/access behavior cannot be designed without privacy decisions.

**Source evidence.** [CP6 Guest Access](../../07-information-architecture/03-public-and-guest-ia.md), [CP8-A blocker register](../07-ux-blocker-register.md).

**Recommended escalation.** Founder/privacy/destination policy before a detailed access journey. B1 stops at the conceptual handoff.

## No silent additions

Guest need, quote/discussion, Sale attribution, Host decision, Payment Obligation/Attempt and Guest access are all represented by existing concepts or documented contextual projections. No new Lead, Quote, Offer, Reservation, state, actor, permission or aggregate was silently introduced.
