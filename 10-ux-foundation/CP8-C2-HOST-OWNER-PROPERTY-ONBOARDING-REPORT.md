# CP8-C2 — Host / Owner + Property Onboarding Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-C Onboarding**  
> Status: **ACCEPTED AS BASELINE FOR CP8-C3**  
> Freeze status: **NOT FROZEN**  
> Scope: **CP8-C2 only** · 2026-09-20

## 1. Executive Summary

C2 applies the accepted C1 onboarding reasoning model to Host/Owner and Property onboarding for Oceanami V0. Actor-first and resource-first entry modes converge on one canonical truth about Identity/Party, Property, Destination, Bookable Unit, Owner/Host relationships, explicit authority and readiness projections. The pass preserves all CP2–CP8-B5 boundaries and creates no new lifecycle, permission, evidence threshold, legal process, data model or UI. C2 is now the accepted baseline consumed by C3.

**Readiness: READY WITH CONDITIONS.** The architecture is coherent enough for Founder/Product Architect review and later detailed work. It is not frozen. Ownership evidence, conflict precedence, publication policy, per-action authority grants, privacy, transfer and manual operating procedures remain explicit TBDs.

## 2. Sources Reviewed

- CP1–CP7 canonical documentation and current source-of-truth registers.
- [CP3 actor catalog, capabilities and invariants](../03-actor-authority/01-actor-catalog.md).
- [CP7 Identity/Party/Authority](../08-conceptual-data-model/02-identity-party-relationship-authority.md) and [Property/Unit](../08-conceptual-data-model/03-destination-property-bookable-unit.md).
- Accepted [CP8-A UX Foundation](README.md), [B1](b1-sale-assisted-booking/README.md), [B2](b2-external-booking-to-stay/README.md), [B3](b3-direct-guest-booking/README.md), [B4](b4-stay-operations/README.md) and [B5](b5-inventory-intervention/README.md).
- [CP8-C1 Onboarding Architecture](c1-onboarding-architecture/README.md).

## 3. Files Created / Changed

Created the C2 folder with the README, overview, actor-first and resource-first journeys, convergence, identity/Party, Property/Destination/Unit, relationship/authority, entry modes, prerequisites, Owner/Host, publication/Verification/Managed, Inventory, Booking, Stay Operations, entry matrix, detailed conceptual step matrix, projections, change/history, conflict, C1/B1–B5 compatibility, TBD register, gaps and traceability documents. Updated the CP8 index, C1 status/report, Start Here, Source of Truth, outputs index and historical CP8 current-pass pointers to identify C2 as the current draft execution unit.

No CP1–CP8-B5 substantive product, domain, authority, workflow, lifecycle, policy, V0 or data-model decision was changed.

## 4. Canonical C2 Architecture

`Identity → Party/capacity → relationship → resource relationship → eligibility/assignment → explicit authority/scope → Working Context → bounded action`.

Actor-first and resource-first are different entry orientations to the same relationship/authority truth. Readiness outcomes are projections/eligibility conditions, not a universal onboarding state.

## 5. Actor-First Journey Findings

Actor-first can begin with an existing/new Identity, an Owner/Host intent or a claim. It resolves Party/capacity, identifies or represents Property, preserves basis/evidence, establishes a relationship only when authorized, then evaluates explicit authority and projects a bounded context. The actor may remain pending at any step.

## 6. Resource-First Journey Findings

Resource-first can represent a Property before Owner or Host joins. Destination and Unit relationships are recorded independently. Owner and Host are identified, invited, claimed or Admin-assisted through separate relationship decisions. The creator does not become Owner/Host/authority automatically.

## 7. Convergence Findings

Both journeys converge on the same Identity/Party, Property, Destination, Unit, relationship, basis/provenance, authority/scope and readiness truth. Entry mode does not alter semantics.

## 8. Property Representation Findings

Property representation includes the conceptual identity/physical-business representation, Destination membership, Unit relationship where known, Owner/Host relationship status, publication readiness, Inventory responsibility and applicable Verification relationship. It does not imply publication, Verification, Managed or Booking.

## 9. Property Existence / Readiness Findings

The pass distinguishes represented, relationship-complete context, publication-eligible, Inventory-ready, Booking-ready, Stay-operations-ready, Verified and Managed outcomes. These are not new Property states and there is no `PROPERTY_ONBOARDING_COMPLETE`.

## 10. Owner Relationship Findings

Self-claim, invitation, existing association and Admin-assisted representation are possible inputs. A claim is not authoritative ownership truth. Evidence thresholds, multiple-Owner precedence and legal transfer remain TBD/legal-validation-required.

## 11. Host Relationship Findings

Owner may designate a Host; an existing Host may be invited/accepted; an Owner may also be Primary Host. Co-host is separately delegated and scoped. Owner, Primary Host and Co-host do not collapse.

## 12. Owner = Host Findings

One Identity can hold both relationships. Actions remain attributable to the acting capacity and authority basis used. The dual relationship does not create financial, Booking or Inventory authority automatically.

## 13. Owner ≠ Host Findings

Owner and Primary Host can be different Identities. C2 preserves Owner scope, Host operating scope, delegation and downstream policy as separate questions and does not invent precedence where canon is silent.

## 14. Property Creator Findings

Owner, Host, Admin or another authorized actor may represent a Property depending on current scope. Creation/representation alone creates no ownership, hosting, Booking Authority, Inventory Authority or financial entitlement.

## 15. Destination Relationship Findings

Oceanami is the V0 pilot Destination. Membership is separate from BQL authority and does not grant Host, Owner, Booking, Inventory or commercial authority.

## 16. Bookable Unit Findings

Property remains distinct from Bookable Unit. Unit representation is required for Inventory truth and downstream Booking participation where applicable, but C2 introduces no unit types or persistence structure.

## 17. Publication Boundary Findings

Representation, publication/searchability, Availability and Bookability remain distinct. Publication conditions are referenced, not invented. Verification is not universal and Managed is outside current core.

## 18. Inventory Responsibility Findings

Inventory is Unit × Time. Inventory responsibility and explicit Inventory Authority must be established for interventions. Owner role, Host role, Sale eligibility or whitelist alone are insufficient. External commerce may be referenced by Inventory and/or create a Stay without a Stayora Booking.

## 19. Booking Participation Findings

Sale-assisted and Direct Guest participation require the relevant Property/Unit, discovery, Inventory, Booking Authority and commercial eligibility prerequisites. Onboarding does not create a Booking or change B1/B3 semantics.

## 20. Stay Operations Prerequisite Findings

Stay operations require Property/Unit and Destination context plus Host/operations responsibility or assignment as applicable. External and internal origins remain compatible; Booking is not the sole operational source of truth. Butler onboarding is not started.

## 21. Entry Mode Findings

The entry matrix covers self-entry, invitation, Admin-assisted setup, Property-first, actor-first, existing claims and Identity linkage. Invitation and claim remain non-authoritative inputs.

## 22. Cross-Context Projection Findings

Owner, Host, Admin, Sale, Butler, Destination/BQL and public marketplace views are projections of scoped truth. A Property can be represented but private; published but unavailable; available but not bookable; or have a changed Host while historical actions remain intact.

## 23. Relationship Change / Historical Truth

Corrections, transfer, replacement, revocation and duplicate consolidation preserve provenance and prior valid actions. Exact effective-time, notice, appeal and downstream policy remain TBD.

## 24. Duplicate / Claim Conflict Findings

Conflicting claims preserve claims, evidence, existing truth and decision responsibility. C2 does not select a winner or create a universal dispute system.

## 25. C1 Compatibility

C1 remains semantically intact: no role shortcut, creator shortcut, Owner shortcut or global onboarding state was introduced.

## 26. B1–B5 Compatibility

B1 receives explicit Host/Booking prerequisites without Sale authority; B2 supports External Accommodation and Stay without fabricated Booking; B3 preserves direct Request semantics; B4 preserves operational truth; B5 requires explicit Inventory authority. No accepted journey is silently changed.

## 27. TBD / Policy Boundaries

Identity matching, evidence/legal validation, ownership precedence, invitations, conflict handling, publication conditions, authority grantors, privacy, revocation timing, Destination correction and manual V0 procedures remain open. See [C2 TBD register](c2-host-owner-property-onboarding/21-tbd-policy-register.md).

## 28. Domain / Workflow / Authority Gaps

Gaps are classified as Property identity/duplicate domain gap, relationship/authority gap, publication policy gap, conflict/transfer workflow gap, privacy gap and V0 manual-operations gap. No new concept is invented to close them.

## 29. V0 Scope Check

C2 stays inside Oceanami V0, manual-assisted setup where CP5 allows it, Owner/Host/Property/Unit truth and downstream prerequisites. It does not expand into Managed Operations, legal verification platform, enterprise organizations, PMS, Channel Manager, ERP, CRM, Affiliate Network, native apps or advanced CMS.

## 30. Contradictions Found

No new contradiction was introduced. The principal protected distinctions are Owner/Host, creator/authority, Property/Unit, existence/publication, publication/Verification, Verified/Managed, relationship/authority and External Accommodation/Stayora Booking.

## 31. Readiness Assessment

**READY WITH CONDITIONS** for Founder/Product Architect review. C2 is not frozen and does not authorize CP8-C3 or later CP8 work.

## 32. Validation

- Actor-first and resource-first converge on identical conceptual truth: verified by cross-reference review.
- C1 and B1–B5 boundary checks: passed; no semantic edits to accepted journeys.
- TBD/product-decision check: passed; unresolved thresholds, precedence and policies remain registered.
- Markdown links: **passed** — `MARKDOWN_LINK_VALIDATION files=254 errors=0`.

## Current CP8-E closure overlay

The historical readiness assessment above is retained. C2 is covered for CP8-E exit by C1–C4 and E1–E4; Owner remains a perspective/context, and ownership evidence, publication, grants, privacy, transfer and manual procedure details remain TBD. No new Owner workspace or interaction family is introduced.
