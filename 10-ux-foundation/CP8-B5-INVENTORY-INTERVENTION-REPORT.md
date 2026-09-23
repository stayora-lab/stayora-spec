# CP8-B5 — Inventory Intervention Journey Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-B Critical Journeys**  
> Status: **ACCEPTED AS BASELINE FOR CP8-C2**  
> Freeze status: **NOT FROZEN**  
> Scope: **B5 only** · 2026-09-20

## 1. Executive Summary

B5 specifies how an authorized actor or legitimate operational fact may intervene in Oceanami V0 Inventory over a Bookable Unit × Time range. It covers Owner Blocks, Maintenance/Unusable Inventory, the Founder-approved Emergency Protective Hold, operational-to-Inventory handoff, overlap/conflict, derived Availability, Availability versus Bookability, correction/release and protection of existing Booking, External Accommodation and Stay truth.

The architecture passes the critical test when interventions target canonical Commitments or Blocks rather than a manual availability boolean. Availability remains derived truth. Reports and Incidents do not automatically become Maintenance Blocks. Owner action does not silently override existing commitments. Conflicts preserve legitimate truths and route to explicit exception/policy handling without inventing a winner.

**CP8-E closure assessment: ACCEPTED FOR CP8-E EXIT.** FD-08/09, FD-12, FD-13/14 and FD-15/16 close the B5 architecture, including no universal conflict precedence and the Emergency Protective Hold extension. Exact grants, evidence standards, release/expiry timing, Bookability policy and downstream remedies remain explicit TBDs. B5 does not start CP8-F.

## 2. Sources Reviewed

- [Start Here](../00-start-here/README.md), [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), [Glossary](../00-start-here/GLOSSARY.md), [Decision Register](../00-start-here/DECISIONS.md) and [Roadmap reconciliation](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- CP1 Product Foundation, CP2 Domain Map/Glossary/Invariants, CP3 Actor Authority/Core Workflows, CP4 State Machines/Policies, CP5 Oceanami V0 Scope, CP6 Information Architecture and CP7 Conceptual Data Model.
- Accepted [CP8-A UX Foundation](README.md), [CP8-B1 Sale-assisted Booking](CP8-B1-SALE-ASSISTED-BOOKING-REPORT.md), [CP8-B2 External Booking → Stay](CP8-B2-EXTERNAL-BOOKING-TO-STAY-REPORT.md), [CP8-B3 Direct Guest Booking](CP8-B3-DIRECT-GUEST-BOOKING-REPORT.md) and [CP8-B4 Stay Operations](CP8-B4-STAY-OPERATIONS-REPORT.md).

Source priority remains Founder decisions → canonical confirmed product decisions → CP1–CP6 → CP7 conceptual model → accepted CP8 work → supporting persistence → working models/hypotheses/references.

## 3. Files Created / Changed

### Created

Inside [B5 Inventory Intervention](b5-inventory-intervention/README.md):

- Journey overview.
- Detailed intervention journey for phases A–I.
- Inventory basis mapping.
- Owner Block journey.
- Maintenance Block journey.
- Operational → Inventory handoff.
- Overlap/conflict matrix.
- Derived Availability mapping.
- Availability versus Bookability.
- Cross-context projections.
- Responsibility handoffs.
- Existing Booking/Stay protection.
- Correction/release/history.
- Alternative/failure boundaries.
- B1–B4 impact check.
- TBD/policy register.
- Domain/workflow/authority gap findings.
- V0/source traceability.

This report is the required `CP8-B5-INVENTORY-INTERVENTION-REPORT.md`.

### Changed

- CP8 indexes now identify B5 and C1–C4 as accepted baselines and D1 as the current draft execution unit; CP8-A and B1–B4 remain accepted baselines.
- Start Here, Source of Truth and the outputs README now point to C1 as current.
- C2 consumes B5 as an accepted Inventory baseline; no B5 substantive decision changed.

No CP1–CP7 product, domain, authority, workflow, lifecycle, policy, V0 or data-model decision was changed.

## 4. Canonical Journey Summary

```text
Intent / operational fact
  → authority + Unit × Time + basis/evidence
  → existing Inventory truth evaluation
  → authorized Owner Block / Maintenance Block / Commitment / correction
  → conflict detection where incompatible
  → derived Availability
  → contextual Bookability/projections
  → correction/release/expiry with history
  → Booking / External Accommodation / Stay exception handoff where affected
```

No step targets a manual Availability flag.

## 5. Inventory Basis Findings

B5 preserves Owner Block, Maintenance Block, Temporary Exclusive Commitment, Confirmed Accommodation Commitment, External Accommodation-backed Commitment and External Accommodation Fact as distinct bases. `AVAILABLE`, `HELD`, `BOOKED` and `BLOCKED` remain projections/semantics, not a generic persisted lifecycle.

## 6. Owner Block Findings

Owner intent must be evaluated against resource relationship, Unit × Time, acting capacity, scope and authority. A valid Owner Block constrains derived Availability while effective. It does not automatically cancel Booking, delete External Accommodation, cancel Stay, refund, relocate or win a conflict.

## 7. Maintenance Block Findings

Operational report/Incident/evidence is distinct from the authorized decision to establish a Maintenance Block. Butler, BQL and Guest may report within scope; they do not gain Inventory Authority by discovering a problem. Maintenance Block creation, evidence, assessor and release remain policy/authority boundaries.

## 8. Authority Findings

Inventory mutation requires basis-specific authority over the relevant Unit × Time. Role, ownership, assignment, visibility, whitelist or operational evidence alone is insufficient. Every action preserves actual actor, acting capacity, authority source, resource, reason/policy and time.

## 9. Operational → Inventory Handoff

The required chain is operational report → evidence → authorized Inventory decision → Maintenance Block or another canonical basis → derived Availability. An Incident remains an Incident unless its own authority/policy establishes a Block. No automatic Butler/BQL authority is introduced.

## 10. Existing Inventory Truth Evaluation

Before intervention, evaluate Temporary Commitment, Confirmed Stayora Commitment, External Commitment, Owner Block, Maintenance Block and related Booking/External Accommodation/Stay over the Unit × Time. Existing truths remain recorded and effective until authoritative end/change.

## 11. Overlap / Conflict Findings

Meaningful Owner/Maintenance/Temporary/Confirmed/External/Stay overlaps are represented as preserved truths. Incompatible effective overlap may create Inventory Conflict. B5 selects no source/channel priority, winner, cancellation, release, refund, relocation or compensation remedy.

## 12. Derived Availability Findings

The canonical derivation is `effective Commitments + Blocks + Unit × Time → derived Availability`. Intervention changes a basis, not Availability directly. Stale, uncertain or conflicted truth remains explicit; no manual `UNAVAILABLE` state is created.

## 13. Availability vs Bookability Findings

An ended/corrected Block may make a range derived Available, but Bookability still depends on publication, actor/context eligibility, authority, verification/trust, commercial policy and current truth. Block removal never means universally Bookable.

## 14. Existing Booking / External Accommodation / Stay Protection

An Inventory problem is not a Booking cancellation or Stay cancellation. External Accommodation is not deleted. Existing Booking, External Commitment and Stay truth are handed to their own exception/policy owners. B5 does not invent commercial remedies.

## 15. Cross-Context Projection Findings

Owner/Host sees basis, scope and responsibility; Sale/Guest see relevant Availability/Bookability outcome; Butler/BQL see operational impact; Admin sees scoped evidence/conflict; Public Marketplace sees derived public projection only. Internal evidence, conflict details and economics remain need-to-know.

## 16. Responsibility Handoffs

The handoff chain is Owner/Reporter → authority evaluation → evidence → Inventory decision → derived Availability → contextual projection → conflict/Booking/Stay exception. A handoff transfers bounded responsibility, never all related domain authority.

## 17. Correction / Release / Historical Truth

Wrong Unit/range/reason, duplicate Block, resolved Maintenance, Owner change, late entry, expiry and correction use amendment, supersession, replacement or explicit release. Original source, actor, authority, time and prior truth remain auditable. Projection recalculation does not erase history.

## 18. Alternative / Failure Paths

The register covers unauthorized requests, Butler/BQL reports without Inventory Authority, insufficient evidence, wrong scope, duplicates, overlap with Booking/External/Stay/Blocks, late entry, early maintenance resolution, revoked authority, conflicting reports, stale projections and unknown/conflicted truth.

## 19. B1–B4 Impact Check

B5 does not change B1 Sale Request/Booking truth, B2 External provenance, B3 direct Request/Bookability semantics or B4 Stay lifecycle. It adds the Inventory handoff required when an operational fact may affect future Availability, without allowing Stay/Incident to control Inventory automatically.

## 20. TBD / Policy Boundaries

Open boundaries include effective interval/freshness, Owner grants, Maintenance assessment, Incident-to-Block threshold, conflict resolver/remediation, commitment coexistence/end, release evidence, Bookability after release, downstream Booking/Stay remedies, correction recalculation and destination-specific access. See [16-tbd-policy-register.md](b5-inventory-intervention/16-tbd-policy-register.md).

## 21. Domain / Workflow / Authority Gaps

Gaps are classified as authority, workflow, policy, data/history, Bookability, downstream exception and V0-scope gaps. B5 creates no aggregate, entity, state, permission, maintenance suite or priority hierarchy to fill them.

## 22. V0 Scope Check

B5 remains within CP5 manual-assisted Inventory intervention, Blocks/Commitments, conflict visibility, derived Availability, operational evidence and existing Booking/External/Stay boundaries. It does not expand into maintenance suite, workforce scheduling, PMS, Channel Manager, dynamic pricing/yield, CRM, Managed Operations, Affiliate Network, native apps, automated relocation/compensation or ERP.

## 23. Contradictions Found

No new contradiction was introduced. B5 explicitly prevents:

- manual Availability or generic `UNAVAILABLE` state;
- Owner Block overriding existing truth;
- Maintenance Block collapsing into Incident;
- Incident becoming Block automatically;
- Block collapsing into Commitment;
- External Fact collapsing into Commitment;
- conflict becoming an automatic winner;
- Check-in/Checkout/Completion controlling Availability;
- Block removal becoming universal Bookability.

## 24. Readiness Assessment

**ACCEPTED FOR CP8-E EXIT.** FD-08/09, FD-12, FD-13/14 and FD-15/16 close the B5 architecture, including no universal conflict precedence and Emergency Protective Hold. Exact evidence, grants, timing, Bookability and downstream remedies remain TBD and are preserved.

Conditions:

1. Preserve basis-specific authority and Unit × Time scope.
2. Decide or explicitly scope Owner/Maintenance grants, conflict/remediation, release/expiry, stale truth, Bookability and downstream exception policy before implementation-level work.
3. Keep operational evidence separate from Inventory mutation and defer Inventory UI/implementation decisions.
4. Do not interpret this report as screen design, implementation authorization or Founder Freeze.

## 25. Validation

- Availability remains derived truth; no manual Availability state: **PASS**.
- Owner Block remains distinct from Maintenance Block: **PASS**.
- Blocks remain distinct from Commitments: **PASS**.
- Temporary, Confirmed and External Commitments remain distinct: **PASS**.
- External Fact remains distinct from Commitment: **PASS**.
- Incident does not automatically become Block: **PASS**.
- Operational evidence does not imply Inventory Authority: **PASS**.
- Owner action does not silently override existing truth: **PASS**.
- Booking, External Accommodation and Stay are not silently cancelled/deleted: **PASS**.
- Conflict preserves truths; no winner/channel priority invented: **PASS**.
- Check-in/Checkout/Completion do not directly control Availability: **PASS**.
- Block removal does not imply universal Bookability: **PASS**.
- Corrections preserve historical truth: **PASS**.
- B1–B4 remain semantically intact: **PASS**.
- Authority claims trace to CP3; Inventory/lifecycle claims to CP4/CP7; V0 claims to CP5; context claims to CP6/CP8-A: **PASS**.
- No persistence assumption became product policy: **PASS**.
- No TBD silently closed: **PASS**.
- No new domain concept, lifecycle state, permission or maintenance domain introduced: **PASS**.
- No screen, wireframe, prototype, Figma, component, token, API, code, schema or migration created: **PASS**.
- No later CP8 work started: **PASS**.
- Markdown file/anchor links: **PASS — 202 Markdown files, 0 broken file/anchor links**.

Return this report to the Founder and Product Architect as the accepted B5 baseline. Do not mark CP8 complete or begin detailed actor onboarding/Workspace/Interaction/Design System work until explicitly directed.
