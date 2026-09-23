# CP8-C3 — Sale Onboarding Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-C Onboarding**  
> Status: **ACCEPTED AS BASELINE FOR CP8-C4**  
> Freeze status: **NOT FROZEN**  
> Scope: **CP8-C3 only** · 2026-09-20

## 1. Executive Summary

C3 documents the minimum Oceanami V0 Sale onboarding architecture. It separates Identity, Sale capacity, platform eligibility, Distribution Relationship, resource/market scope, Sale Working Context, bounded distribution actions and attribution. It supports the B1 path through discovery, option preparation, Guest intent and Booking Request creation while preserving Host/Co-host Booking Authority, Inventory Authority, Money and Stay boundaries. C3 is now the accepted baseline consumed by C4.

**Readiness: READY WITH CONDITIONS.** The conceptual architecture is coherent for Founder/Product Architect review. Approval criteria, relationship grantor/scope, privacy/commercial visibility, attribution conflict, economics, revocation timing and external-report handling remain explicit TBDs. C3 is not frozen.

## 2. Sources Reviewed

- CP1–CP7 canonical Product Foundation, Domain, Actor Authority, Workflows, State/Policy, V0, IA and Conceptual Data Model.
- [Roadmap & Source-of-Truth Reconciliation Report](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- [CP3 actor catalog](../03-actor-authority/01-actor-catalog.md), [capabilities](../03-actor-authority/02-authority-capabilities.md), [invariants](../03-actor-authority/06-authority-invariants.md).
- [CP4 eligibility](../05-state-machines-policies/09-role-application-and-eligibility.md), [Distribution lifecycle](../05-state-machines-policies/08-lead-and-distribution-lifecycle.md), [Distribution policy](../05-state-machines-policies/19-distribution-policy.md), Request/Booking and Money policies.
- [CP5 critical journeys and boundaries](../06-v0-scope/03-critical-journeys.md).
- [CP6 Sale Workspace](../07-information-architecture/05-sale-workspace.md).
- [CP7 Identity, provenance and Money](../08-conceptual-data-model/02-identity-party-relationship-authority.md), [provenance](../08-conceptual-data-model/08-provenance-temporal-history.md), [Money](../08-conceptual-data-model/06-money-payment-settlement-payout.md).
- Accepted [CP8-A](README.md), [B1](b1-sale-assisted-booking/README.md), [B2](b2-external-booking-to-stay/README.md), [B3](b3-direct-guest-booking/README.md), [B4](b4-stay-operations/README.md), [B5](b5-inventory-intervention/README.md), [C1](c1-onboarding-architecture/README.md) and [C2](c2-host-owner-property-onboarding/README.md).

## 3. Files Created / Changed

Created the C3 folder with overview, journey, entry modes, Sale capacity/relationship, eligibility, Distribution Relationship, supply visibility, commercial information, Request capability, attribution, multi-capacity stress tests, External Accommodation, Inventory, Stay Operations, context activation, completion outcomes, projections, history, conflict, alternatives, C1/C2 and B1–B5 compatibility, TBD register, gaps, detailed step matrix and traceability. Updated CP8 indexes, C2 status/report, Start Here, Source of Truth, outputs README and historical current-pass pointers to identify C3 as the current draft execution unit.

No CP1–CP8-C2 substantive product, domain, authority, workflow, lifecycle, policy, V0 or data-model decision was changed.

## 4. Canonical Sale Onboarding Architecture

`Identity → Sale capacity/relationship → platform eligibility → Distribution Relationship → resource/market scope → Sale Working Context → bounded distribution action → attribution where canonical`.

This is a reasoning chain, not `choose Sale → dashboard → sell everything`, and not a universal Sale lifecycle.

## 5. Sale Entry Mode Findings

Self-entry/application, invitation, Admin-assisted setup, existing Identity, Owner/Host plus Sale and additional relationship scope are legitimate conceptual modes. Technical mechanisms and approval criteria remain open.

## 6. Sale Capacity / Relationship Findings

Sale capacity is distinct from self-description and eligibility. Distribution Relationship is a separate scoped commercial relationship to a Commercial Authority holder/authority scope. It does not create Host, Booking or Inventory authority.

## 7. Eligibility Findings

CP4's Application and Platform Eligibility concepts are preserved. Manual-assisted V0 evaluation is allowed where CP5 permits it and remains auditable. No score, KYC, tier, training or performance threshold is invented.

## 8. Distribution Relationship Findings

NORMAL, WHITELIST and BLACKLIST remain relationship states with scope, lifecycle and provenance. Whitelist is not unrestricted permission; blacklist is relationship-scoped and does not erase history. Grantor, exact scope, terms and appeal remain TBD where canonical sources are silent.

## 9. Supply Visibility Findings

Sale consumes public and Sale-context supply projections only within valid eligibility, relationship, scope, policy and privacy. Searchability, Availability and Bookability remain distinct; not all supply becomes visible or bookable.

## 10. Commercial Information Findings

Sale may need Public Price, real Availability, fit and trust information for B1. Owner economics, tax, profitability, full ledger and payout data are not exposed automatically. No pricing/commission/payout formula is invented; CP7's confirmed 10% base commission and TBD CBV remain unchanged.

## 11. Request Capability Findings

Sale can create a Booking Request after the relevant onboarding and supply prerequisites. Sale cannot accept its own Request. Request remains separate from Booking and does not reserve Inventory.

## 12. Attribution Findings

Attribution remains separate from authority, commission entitlement, Settlement and Payout. Acquisition and Sales Handling attribution can coexist. C3 preserves claims/provenance and does not select a winner.

## 13. Sale + Co-host Findings

One Identity may act as Sale to create a Request and later act as Co-host under explicit delegated Booking Authority to accept. The audit records actual capacity, authority basis and resource scope. Sale creation does not authorize acceptance.

## 14. Sale + Owner / Host Findings

Owner/Host and Sale relationships can coexist or change independently. No duplicate Identity or precedence rule is introduced.

## 15. External Accommodation Boundary

Sale may report external information; only explicit Inventory Authority can authoritatively record External Accommodation or establish an Inventory Commitment. External commerce may create Inventory truth and/or Stay without a Stayora Booking.

## 16. Inventory Boundary

Sale consumes derived Availability/Bookability and does not create Blocks, commitments, releases or conflict overrides without separate Inventory Authority.

## 17. Stay Operations Boundary

Sale is not automatically an operational actor. B4 handoff to Host, Butler, Destination/BQL and Guest remains intact; Sale receives only limited need-to-know information under policy.

## 18. Sale Context Activation

Context usability is a projection after Identity, capacity, eligibility, active relationship and scope are sufficient. No `SALE_ACTIVE` state is introduced.

## 19. Onboarding Completion Findings

Identity, capacity, eligibility, relationship, scope, context usability, Request creation and attribution are independent outcomes. There is no `SALE_ONBOARDED` universal flag.

## 20. Cross-Context Projection Findings

Sale, Admin, Host/Owner, Guest, Public Marketplace and Money projections change only as their independent truth and scope permit. Revocation restricts future actions while preserving valid history.

## 21. Revocation / Change / Historical Truth

Eligibility and relationship changes preserve actual actor, capacity, basis, scope, time and result. Valid prior Requests, Bookings, attribution and completed Stays are not destructively rewritten.

## 22. Multiple Sale / Attribution Conflict

Conflicts preserve claims, evidence, timestamps and downstream object truth. Winner, split, replacement, fraud and appeal policies remain TBD.

## 23. Alternative / Failure Paths

Existing Identity, pending/denied/revoked eligibility, missing relationship, out-of-scope supply, visible-but-not-bookable supply, unauthorized acceptance, Inventory mutation, External Accommodation reporting and attribution conflict are covered. Unsupported policy outcomes remain explicit TBD/gaps.

## 24. C1 / C2 Compatibility

C3 preserves C1's identity/capacity/relationship/eligibility/scope/authority/context chain and does not alter C2 Owner/Host/Property semantics. Sale relationship is not ownership or hosting.

## 25. B1–B5 Compatibility

B1 Request creation is enabled without Booking Authority; B2 reporting is separated from authoritative external truth; B3 remains independent; B4 operations remain separate; B5 Inventory authority remains explicit. No accepted journey is silently changed.

## 26. TBD / Policy Boundaries

Approval criteria, evidence, relationship grantor/scope, visibility, Offer/Request details, attribution qualification/conflict, economics, revocation and manual operations remain registered in [C3 TBD register](c3-sale-onboarding/24-tbd-policy-register.md).

## 27. Domain / Workflow / Authority Gaps

Gaps include eligibility policy, relationship authority, attribution/Offer ownership, privacy/commercial presentation, revocation during Request and external-report authorization. C3 adds no new domain concepts to close them.

## 28. V0 Scope Check

C3 stays inside Oceanami V0 Sale network and minimal Lead/Distribution scope. It excludes Affiliate Network, advanced lead distribution, CRM, commission engine, reseller platform, partner contracting, PMS, Channel Manager, Managed Operations, native apps and workforce tooling.

## 29. Contradictions Found

No new contradiction was introduced. The protected distinctions are capacity/eligibility/relationship, relationship/authority, visibility/bookability, attribution/money and Sale/Host/Inventory/Stay responsibilities.

## 30. Readiness Assessment

**READY WITH CONDITIONS** for Founder/Product Architect review. C3 is not frozen and does not authorize CP8-C4 or later CP8 work.

## 31. Validation

- Sale capacity, eligibility, Distribution Relationship, scope, attribution and authority remain distinct: passed by cross-document review.
- C1/C2 and B1–B5 compatibility: passed; no accepted journey semantics changed.
- TBD/product-decision check: passed; unresolved criteria, grantors, attribution rules and economics remain registered.
- Markdown links: **passed** — `MARKDOWN_LINK_VALIDATION files=283 errors=0`.

## Current CP8-E closure overlay

The historical readiness assessment above is retained. C3 is covered for CP8-E exit by C1–C4 and E1–E4; Sale approval/capacity/relationship reasoning remains bounded, while economics, privacy, attribution conflict, revocation and external-report procedure details remain TBD.
