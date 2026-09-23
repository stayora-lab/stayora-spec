# CP8-A — UX Principles Derived from Stayora Architecture

> Status: **ACCEPTED AS CP8-B BASELINE** · **NOT FROZEN**

These are UX constraints derived from existing Stayora decisions. Each principle states what it changes in later UX work and what it does not authorize. None is a new product decision.

## 1. Make decision-relevant truth visible

**Rationale.** Stayora owns shared Inventory/Stay truth across direct, Sale, OTA and Owner Direct sources; CP5 makes Inventory Trust a V0 validation dimension. A user needs the state that supports a correct decision, including provenance and uncertainty where material.

**Affected actors/surfaces.** Guest and Sale in Public Marketplace/Sale; Host in Host Workspace; Butler/BQL in Operations; Admin in exception views.

**UX implication.** Show the relevant availability, commercial or operational state and its source at the point of decision. Surface conflicts, stale/unknown outcomes and action-required conditions explicitly.

**Does not authorize.** It does not require exposing Owner economics, external revenue, internal evidence or fields outside the actor's relationship and need-to-know scope; it does not turn a projection into canonical truth.

## 2. Make authority legible at the action boundary

**Rationale.** CP3 requires effective permission to be derived from Identity, eligibility, relationship, capability, scope, lifecycle, policy and transaction context. Role labels alone never grant a privileged action.

**Affected actors/surfaces.** Host/Co-host Requests and Inventory; Sale Requests; Butler/BQL Operations; Admin interventions.

**UX implication.** An action should communicate why it is available, unavailable or routed to another responsible actor when that reason affects user behavior. Acting capacity must remain attributable in contextual handoffs.

**Does not authorize.** It does not invent permission bundles, authority precedence, staff grants or technical RBAC/ABAC.

## 3. Organize around responsibility, not actor labels or database shape

**Rationale.** CP6 navigation follows responsibility and Working Context. One Identity may be Host for one Property, Co-host for another, Sale in a commercial relationship and Guest of a Stay.

**Affected actors/surfaces.** All CP6 surfaces, especially Host, Sale and Operations.

**UX implication.** A context should answer “what do I need to know or do here?” and show the resource scope that responsibility covers. Switching context changes perspective without creating a second business truth.

**Does not authorize.** It does not add roles, create separate accounts, or infer authority from a navigation location.

## 4. Show one shared truth through contextual projections

**Rationale.** CP6 and CP7 define contextual projections over shared Identity, Inventory, Booking, Stay, Money, Verification and Reputation truth.

**Affected actors/surfaces.** A Booking Request, Booking, Stay, Inventory Commitment and Incident may appear in multiple workspaces.

**UX implication.** Different contexts may emphasize different facts and actions while retaining the same object identity, provenance and lifecycle meaning.

**Does not authorize.** It does not duplicate records, create channel-specific availability truth, or rename one object into different business objects merely for a surface.

## 5. Keep commitment states visibly distinct

**Rationale.** CP4/CP7 separate Request, Temporary Inventory Commitment, Required Payment Condition, Booking CONFIRMED, Stay and Settlement. Request does not reserve Inventory; Booking begins at confirmation.

**Affected actors/surfaces.** Guest/Sale requests, Host decisions, Guest Stay Access, Host Calendar, Money and Operations.

**UX implication.** A request awaiting decision, a finite temporary commitment, a confirmed Booking, a Payment Attempt and an actual Stay must not look like interchangeable “booking” statuses.

**Does not authorize.** It does not add lifecycle states, invent timing, or decide when a request becomes a Booking.

## 6. Keep external accommodation operationally first-class without fabricating commerce

**Rationale.** CP2/CP5/CP7 allow external commerce to establish or reference Inventory Truth and/or a Stay. External Accommodation is not a fake Stayora Booking, and no automatic commission follows.

**Affected actors/surfaces.** Host Calendar, Butler/BQL Operations, Guest Stay Access where applicable, Admin conflict views and Reputation evidence.

**UX implication.** External origin and provenance remain visible wherever they affect expectations; operations can proceed on the represented Stay without routing the record through Stayora Booking.

**Does not authorize.** It does not require external price, revenue or payment details without an independently supported need, create a Stayora Booking, or grant commercial authority to a reporter.

## 7. Treat manual assistance as an integrity-preserving path

**Rationale.** CP5 explicitly uses MANUAL-ASSISTED handling for conflicts, complex refunds, Verification Review, reputation disputes, lead assignment and unusual settlement cases.

**Affected actors/surfaces.** Admin, Stayora functional staff, Host/Sale and Operations exception handoffs.

**UX implication.** A manual action should retain source, authority, reason, timestamp and resulting truth; users should see when a case needs a person rather than a silent automation.

**Does not authorize.** It does not permit fake commitments, overwritten financial history, silent impersonation, automatic commissions or ad hoc policy.

## 8. Use progressive complexity without hiding material risk

**Rationale.** CP1–CP7 contain necessary distinctions, but CP8 should expose them when they improve understanding or action. Complexity may be deferred only when the omitted detail cannot change the decision.

**Affected actors/surfaces.** Public/Guest, Sale, Host, Operations and Admin each need different detail levels.

**UX implication.** Start with the responsibility-relevant summary and make provenance, authority basis, uncertainty, exceptions and deeper evidence available when the decision depends on them.

**Does not authorize.** It does not collapse Payment UNKNOWN into failure, Verification Review into a status, or public trust into an invented TrustScore.

## 9. Make exceptions and uncertainty actionable

**Rationale.** CP4 treats Payment `UNKNOWN`, inventory conflicts, unresolved incidents, stale information and open Review Cases as distinct truths. They are not generic failure states.

**Affected actors/surfaces.** Money/Admin, Host/Sale booking handoffs, Operations issues, Verification and access.

**UX implication.** Affected users should know what is unresolved, which action is safe now, who owns the next decision and what must not be assumed.

**Does not authorize.** It does not choose conflict winners, grace duration, refund/default economics, escalation SLA or Review Case outcomes.

## 10. Keep V0 focused on pilot evidence

**Rationale.** CP5 validates Inventory Trust, Network Adoption, Destination Stay Coverage and Commerce Validation; it explicitly defers advanced distribution, universal TrustScore, full PMS, native apps and Managed Operations.

**Affected actors/surfaces.** Oceanami V0 public, Host, Sale, Guest Stay Access, Butler, BQL and Admin surfaces.

**UX implication.** Every later interaction should trace to a critical journey, a MUST BUILD integrity capability or a MANUAL-ASSISTED path that preserves the four theses.

**Does not authorize.** It does not add V0 capabilities, turn deferred areas into UI, or use target hypotheses as acceptance requirements.

## 11. Separate trust, verification and reputation signals

**Rationale.** Stayora Verified is quality assurance; Identity Verification belongs to Identity & Authority; Reputation is derived from attributable evidence; there is no universal TrustScore.

**Affected actors/surfaces.** Public Marketplace, Host Quality, Admin Verification, Guest Reviews and relationship-scoped Sale views.

**UX implication.** Label the signal's meaning and audience. Keep Verification Assessment/Review Case and Verification Status distinct; keep Review, Review Right and Reputation distinct.

**Does not authorize.** It does not expose private evidence, infer a score, or turn an incident/review into an automatic Verified or Reputation consequence.

## 12. Preserve privacy and information minimization by relationship

**Rationale.** CP1/CP3/CP6 require financial and guest information to be role-, relationship- and resource-scoped; BQL and Butler need operational fields, not unrelated economics.

**Affected actors/surfaces.** Guest Stay Access, Butler, Destination/BQL, Sale, Host, Admin and Finance functions.

**UX implication.** Treat each handoff as a data-purpose decision: show the minimum information needed for the task and make scope clear.

**Does not authorize.** It does not settle Guest QR fields, retention, consent, data sharing or legal/privacy policy; those remain open where documented.
