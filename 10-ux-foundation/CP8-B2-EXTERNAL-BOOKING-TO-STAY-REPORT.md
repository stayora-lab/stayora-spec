# CP8-B2 — External Booking → Stay Journey Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-B Critical Journeys → B2 External Booking → Stay**  
> Status: **ACCEPTED AS BASELINE FOR CP8-B3**  
> Freeze status: **NOT FROZEN**  
> Date: 2026-09-19

## 1. Executive Summary

CP8-B2 specifies how accommodation created outside Stayora commerce can become truthful Inventory and operational Stay information for Oceanami V0. It preserves the thesis:

```text
External Commerce
  → External Accommodation Fact
  → Inventory Truth and/or Stay Representation
  → Guest / Host / Butler / Destination Operations
```

The journey supports Destination Stay Coverage without requiring a Stayora Booking, Stayora Payment, Sale attribution or commission. The key control is a staged trust boundary: an External Report is not automatically an authoritative External Accommodation Fact; the fact is not automatically an Inventory Commitment; and an Inventory Commitment is not Availability.

**CP8-E closure assessment: ACCEPTED FOR CP8-E EXIT.** B2 is sufficiently covered by B2 + E3 + E4 + FD-08/09 + FD-12 + FD-15/16. Authority/evidence thresholds, conflict procedure, late correction, external data minimums and Guest access/privacy remain policy boundaries; they do not block the architecture or justify fabricating Stayora commerce. No prototype or implementation work has started.

## 2. Sources Reviewed

- [Start Here](../00-start-here/README.md), [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), [Glossary](../00-start-here/GLOSSARY.md), [Decision Register](../00-start-here/DECISIONS.md) and [Roadmap Reconciliation Report](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- CP1 Product Foundation, especially Marketplace, Destination, Trust, Money, Oceanami Pilot, Success Metrics and Scope Boundaries.
- CP2 [Domain Map / Glossary / Invariants](../02-domain/README.md).
- CP3 [Actor Authority](../03-actor-authority/README.md) and [Core Workflows](../04-core-workflows/README.md), especially WF-03 External Booking → Stay.
- CP4 [State Machines and Policies](../05-state-machines-policies/README.md), especially Inventory, Stay, Incident, Verification, access and cross-policy reconciliation.
- CP5 [Oceanami V0 Scope](../06-v0-scope/README.md), critical journeys, capability matrix, boundaries and metrics.
- CP6 [Information Architecture](../07-information-architecture/README.md), especially Guest Stay Access, Host, Operations, Admin and cross-surface navigation.
- CP7 [Conceptual Data Model](../08-conceptual-data-model/README.md), especially External Accommodation, Inventory, Stay, provenance/history and quality/cases.
- CP8-A accepted UX Foundation and CP8-B1 accepted Sale-assisted Booking, used for contextual and contrast boundaries.
- CP7 [Supporting Persistence Architecture](../09-database-design/README.md) only as constraint/reference material.

Source priority remains Founder decisions → canonical confirmed product decisions → CP1–CP6 → CP7 conceptual model → accepted CP8 work → supporting persistence → working models/hypotheses/references.

## 3. Files Created / Changed

### Created

Inside [B2 External Booking → Stay](b2-external-booking-to-stay/README.md):

- B2 journey overview.
- Detailed journey specification.
- Cross-context timeline.
- Provenance and authority mapping.
- Inventory effect mapping.
- Operations handoff mapping.
- Alternative/failure/TBD boundaries.
- Domain/workflow/authority gap findings.
- B1 vs B2 comparison.
- V0/source traceability matrix.

This report is the required `CP8-B2-EXTERNAL-BOOKING-TO-STAY-REPORT.md`.

### Changed

- [CP8 UX README](README.md) now records B2 as an accepted baseline and D1 as the current draft execution unit.
- [Start Here README](../00-start-here/README.md), [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md) and [outputs README](../../README.md) now point to C1 as current; later work remains not started.

These are index/status corrections only. No CP1–CP7 product, domain, authority, workflow, lifecycle, policy, V0 or data-model decision was changed.

## 4. Canonical Journey Summary

```text
External Commerce
  → report / registration with source and provenance
  → authority/evidence evaluation
  → External Accommodation Fact where accepted
  → authorized Inventory Commitment where compatible
  → derived Availability
  → operational Stay representation where sufficient
  → scoped Guest Stay Access
  → Butler / Destination Operations
  → checkout/completion and preserved history
```

Inventory and Stay are two supported branches. External commerce does not need to pass through Stayora Booking.

## 5. External Origin Findings

Canonical architecture supports external origins such as Host Direct, Owner Direct, OTA-originated accommodation, Sale/Zalo/off-platform booking and other legitimate sources. These are provenance categories, not a commitment to integrations or universal input methods.

Manual Host entry and manual-assisted recording are acceptable where CP5 permits, provided identity, acting capacity, authority, source, evidence, resource scope and audit history remain intact. No Channel Manager, PMS, OTA integration platform or synchronization design was added.

## 6. Authority / Provenance Findings

External reporting and authoritative recording are separate capabilities. A Host/Owner/authorized Co-host relationship may support a report, but Property relationship alone is not a universal Record External Commitment grant. Ordinary Sale may report/submit; only an explicitly granted Inventory capability can establish an external commitment in scope. Butler/BQL assignment supports operations, not commercial or Inventory Authority.

Every critical action must preserve Identity, acting capacity, authority basis, resource, source, evidence/reason and time. An unresolved report is retained as provenance-bearing input rather than silently promoted or discarded.

## 7. External Accommodation Fact Findings

The canonical External Accommodation candidate may reference source, external reference where available, Property/Bookable Unit, accommodation dates, minimum Staying Party information, authoritative recorder, provenance and timestamps. External revenue, margin and payment are not required merely to represent operational truth.

An accepted fact can be referenced by Inventory and/or Stay. It is not a Stayora Booking and does not require a Request, Payment, commission or settlement.

## 8. Inventory Findings

The safe chain is:

```text
External Accommodation Fact
  + explicit Inventory Authority
  + compatible Unit × Time commitment
  → Inventory Commitment
  → derived Availability
```

The fact, commitment and Availability remain separate. External confirmed commitments have equivalent inventory effect where valid; no channel/source priority exists. Owner Block and Maintenance Block are distinct Availability Blocks. Temporary Commitment is a finite Stayora commerce progression. Confirmed Stayora Accommodation Commitment comes from confirmed Stayora Booking. None is silently substituted for another.

## 9. Conflict Findings

An external fact may overlap a Confirmed Stayora Booking, Temporary Commitment, Owner Block, Maintenance Block or another external accommodation. B2 preserves every fact/commitment, source, evidence and timestamp and surfaces an Inventory Conflict/Exception. It does not invent a winner, channel priority, automatic cancellation, release, compensation or overwrite.

The unresolved conflict policy remains a journey-level blocker for later detailed interaction work, not a reason to falsify external truth.

## 10. Stay Representation Findings

An External Accommodation may provide the Accommodation Basis for a Stay. The Stay remains an independent operational truth and can be represented with sufficient operational data/evidence without a Stayora Booking. A represented Stay may be `SCHEDULED` and later progress through its existing lifecycle; external registration does not imply `CHECKED_IN` or `COMPLETED`.

The Stay does not create or release Inventory by convenience. Physical absence, late registration or no arrival does not rewrite a valid commitment. Completion uses Stay policy and preserves the external basis/history.

## 11. Guest Access Findings

An external Guest may receive scoped Guest Stay Access when a valid Stay relationship and applicable destination/access conditions exist. Access is need-to-know and does not imply Stayora-originated commerce, Booking Authority or payment authority.

QR/link format, authentication, fields, expiry/revocation, participant linkage, consent, privacy and retention remain unresolved. B2 records prerequisites only and does not resolve them.

## 12. Operations Handoff Findings

- Host/authorized operational actors establish or maintain the external fact/Stay within scope.
- Butler consumes assigned Stay, arrival, readiness, access and issue information.
- Destination/BQL consumes destination-scoped occupancy, access, registration, vehicle/service and issue information where policy requires.
- Admin/Quality/Money consume evidence or cases only under their own authority/policy.

Operational visibility does not expose external commercial economics, Sale commission, Owner payout or full ledger. Butler/BQL may record evidence but cannot impose financial/reputation consequences by default.

## 13. Cross-Context Projection Findings

- **Reported:** Reporter sees pending input; Host sees a report; Inventory sees a candidate signal; Butler/BQL normally see nothing; Admin sees assigned evidence/case.
- **Authoritative:** Host/Admin sees provenance and scope; Inventory may establish a commitment; Guest/Butler/BQL see only later operational projections.
- **Conflict:** Host/Admin see both truths and next decision responsibility; Inventory surfaces conflict; Butler/BQL see only operational impact; no winner is implied.
- **Upcoming Stay:** Guest sees scoped preparation/access; Host fulfills; Butler/BQL operate; Admin handles exceptions/audit.
- **Completed Stay:** external source, fact, commitment history, Stay, incidents and corrections remain distinct; qualifying evidence may support Review Right, not commission.

## 14. Commercial Non-Fabrication Check

An external accommodation does **not** automatically create:

- Stayora Booking;
- Stayora Booking Request;
- Stayora Payment or Payment Obligation;
- Stayora commission or Sale attribution;
- Stayora Settlement entitlement or Payout;
- internal Stayora commerce provenance.

No canonical exception was found that reverses this boundary. External commercial lifecycle remains external. A separately authorized Stayora service/economic policy would require a future explicit decision; B2 does not infer one.

## 15. Responsibility Handoffs

The handoff mapping covers External Source → Reporter, Reporter → authority evaluation, evaluator → Inventory, evaluator/Host → Stay, Stay → Guest Access, Stay → Butler, Stay → Destination/BQL and Operations → Admin/Quality/Money consumers. Each handoff identifies trigger, object, authority, information, responsibility, failure and TBD dependency.

## 16. Alternative / Failure Paths

B2 covers late, unauthorized, insufficient, wrong-unit, wrong-date, duplicate, corrected, conflicting, incomplete, delayed, uncertain, withdrawn, already-started and already-completed external information. Existing architecture supports truth preservation, provenance, no fake Booking, no automatic commitment from a report and scoped operational representation. Exact conflict, timing, evidence, correction and access outcomes remain policy/workflow boundaries.

## 17. Correction / Historical Truth

CP7's correction principle is preserved: use amendment, supersession, replacement facts or explicit correction actions rather than destructive rewriting. A corrected external report/fact may change future projections only through authorized truth handling; original source, recorder, time and prior operational/inventory history remain auditable. No SQL, versioning scheme or event infrastructure is selected.

## 18. TBD / Policy Boundaries

Open boundaries include reporter/grant policy, evidence/confidence, fact acceptance timing, fact-to-commitment timing, conflict winner/remediation, stale/sync health, wrong-unit/date correction, duplicate handling, late registration, minimum operational Guest data, access/privacy, assignment changes, completion blockers and review eligibility. The complete register is [07-alternatives-tbd.md](b2-external-booking-to-stay/07-alternatives-tbd.md).

Known truth continues independently where possible; no TBD was silently closed.

## 19. Domain / Workflow / Authority Gaps

The findings are:

- report → authoritative fact: authority/policy gap;
- fact → Inventory Commitment timing: workflow/policy gap;
- conflict resolution: policy/workflow gap;
- late/corrected source truth: history/workflow policy gap;
- Guest access fields/lifecycle: UX/privacy gap.

Existing domain concepts are sufficient to express B2. No new aggregate, actor, permission, state or V0 capability was introduced.

## 20. B1 vs B2 Findings

B1 starts from Sale-assisted Stayora commerce: Sale creates Request, Host accepts, payment conditions are evaluated, Booking begins at `CONFIRMED`, then Stay can follow. B2 starts from external commerce: a report/fact is evaluated, an authorized external commitment and/or Stay may be represented, and no Stayora Booking/Payment/attribution is fabricated.

Both paths converge on shared Inventory/Stay operations while preserving origin, authority and financial provenance. Operational convergence does not mean commercial convergence.

## 21. V0 Scope Check

B2 uses CP5 external Booking/Stay registration, external commitment representation, conflict detection, Stay lifecycle, scoped Guest access, Butler/BQL operations and audit/provenance. It does not add Channel Manager, PMS, OTA integration, external accounting, automatic reconciliation, CRM, Affiliate, Managed Operations, dynamic pricing or workforce management.

## 22. Contradictions Found

No new contradiction was introduced. B2 explicitly prevents:

- External Booking being routed through Stayora Booking;
- a report being treated as authoritative fact;
- an external fact being treated as commitment or Availability;
- external commerce being treated as Stayora Payment, commission or Sale attribution;
- external conflict being resolved by source priority;
- external Stay being treated as automatic Check-in/Completed;
- Butler/BQL operational access becoming commercial authority.

## 23. Readiness Assessment

**ACCEPTED FOR CP8-E EXIT.** FD-08/09, FD-12 and FD-15/16 close the architecture. Evidence thresholds, reconciliation procedure, late correction, privacy and commercial details remain TBD and are preserved.

Conditions:

1. Preserve the report/fact/commitment/Availability distinctions.
2. Resolve or explicitly scope authority/evidence, conflict, correction and access/privacy policy before detailed interaction work.
3. Keep external source provenance visible through Stay and completion.
4. Do not interpret B2 as a Channel Manager, PMS, integration or implementation specification.

CP8-B3 Direct Guest Booking, CP8-B4 Stay Operations, CP8-B5 Inventory Intervention and CP8-C1 through C4 Onboarding are accepted preceding baselines. D1 Workspace & Surface Architecture is documented in its own current execution unit; later CP8 work has not started.

## 24. Validation

- External Accommodation was not converted into Stayora Booking: **PASS**.
- No fake Request, Payment, commission or unsupported Sale attribution: **PASS**.
- External provenance remains visible: **PASS**.
- Report is not silently equated with authoritative fact: **PASS**.
- External Fact is not collapsed into Inventory Commitment: **PASS**.
- Inventory Commitment is not collapsed into Availability: **PASS**.
- Conflict preserves truth and does not invent a winner: **PASS**.
- Booking remains separate from Stay: **PASS**.
- Butler/BQL retain operational scope without commercial authority: **PASS**.
- Guest access/QR/privacy remains unresolved: **PASS**.
- Correction preserves historical truth without destructive rewrite: **PASS**.
- Authority/lifecycle/V0/domain claims trace upstream: **PASS**.
- Supporting persistence not promoted to product policy: **PASS**.
- No TBD silently closed or new domain concept introduced: **PASS**.
- No screen/wireframe/prototype/code/schema/migration created: **PASS**.
- No later journey started: **PASS**.
- Markdown links after B2 expansion: **PASS — 148 Markdown files, 0 broken file/anchor links**.

Return this report to Founder and Product Architect as the accepted B2 baseline. Do not mark CP8 complete or begin B5 until explicitly directed.
