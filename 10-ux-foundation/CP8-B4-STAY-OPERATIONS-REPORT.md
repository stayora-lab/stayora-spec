# CP8-B4 — Stay Operations Journey Report

> Parent checkpoint: **CP8 — UX / Design System**  
> Workstream: **CP8-B Critical Journeys**  
> Status: **ACCEPTED AS BASELINE FOR CP8-B5**  
> Freeze status: **NOT FROZEN**  
> Scope: **B4 only** · 2026-09-20

## 1. Executive Summary

B4 specifies how a legitimate accommodation becomes an operational Stay and moves through Oceanami V0 preparation, readiness, arrival, Check-in, in-stay support, Incident handling, Checkout, completion and post-stay history.

The architecture remains coherent when Stay is treated as an independent operational truth. B1 Sale-assisted Booking, B3 Direct Guest Booking and B2 External Accommodation can converge on the same Stay lifecycle and operational projections without fabricating a Booking, erasing commercial provenance or giving Butler/BQL commercial authority.

**CP8-E closure assessment: ACCEPTED FOR CP8-E EXIT.** FD-01 → FD-07 close the B4 interaction architecture: Check-in/Checkout authority, automatic completion conditions, DID_NOT_OCCUR authority and hybrid Guest access. Readiness criteria, Incident consequences, field-level privacy, no-show effects and operating detail remain explicit TBDs. B4 does not start CP8-F.

## 2. Sources Reviewed

- [Start Here](../00-start-here/README.md), [Source of Truth](../00-start-here/SOURCE_OF_TRUTH.md), [Glossary](../00-start-here/GLOSSARY.md), [Decision Register](../00-start-here/DECISIONS.md) and [Roadmap reconciliation](../ROADMAP-SOURCE-OF-TRUTH-RECONCILIATION-REPORT.md).
- CP1 Product Foundation, CP2 Domain Map/Glossary/Invariants, CP3 Actor Authority/Core Workflows, CP4 State Machines/Policies, CP5 Oceanami V0 Scope, CP6 Information Architecture and CP7 Conceptual Data Model.
- Accepted [CP8-A UX Foundation](README.md), [CP8-B1 Sale-assisted Booking](CP8-B1-SALE-ASSISTED-BOOKING-REPORT.md), [CP8-B2 External Booking → Stay](CP8-B2-EXTERNAL-BOOKING-TO-STAY-REPORT.md) and [CP8-B3 Direct Guest Booking](CP8-B3-DIRECT-GUEST-BOOKING-REPORT.md).

Source priority remains Founder decisions → canonical confirmed product decisions → CP1–CP6 → CP7 conceptual model → accepted CP8 work → supporting persistence → working models/hypotheses/references.

## 3. Files Created / Changed

### Created

Inside [B4 Stay Operations](b4-stay-operations/README.md):

- Journey overview.
- Detailed Stay Operations journey for phases A–K.
- Cross-context timeline.
- Operational responsibility matrix.
- Butler boundary.
- Destination/BQL boundary.
- Guest operational outcomes.
- Stay lifecycle/domain mapping.
- Responsibility handoffs.
- Incident stress test.
- Stay-origin comparison.
- Inventory relationship.
- Alternative/failure boundaries.
- Correction/historical truth mapping.
- TBD/policy register.
- Domain/workflow/authority gap findings.
- V0/source traceability.

This report is the required `CP8-B4-STAY-OPERATIONS-REPORT.md`.

### Changed

- CP8 indexes now identify B4 and C1–C4 as accepted baselines and D1 as the current draft execution unit; CP8-A and B1–B5 remain accepted baselines.
- Start Here, Source of Truth and the outputs README now point to C1 as current.
- B4 report/index wording now records C1 as the next execution unit; no B4 substantive decision changed.

No CP1–CP7 product, domain, authority, workflow, lifecycle, policy, V0 or data-model decision was changed.

## 4. Canonical Journey Summary

```text
Accommodation Basis
  (B1 Booking | B3 Booking | B2 External Accommodation)
  → Stay `SCHEDULED`
  → pre-arrival preparation
  → readiness milestone (not a Stay state)
  → expected/physical arrival observation
  → authorized Check-in → `CHECKED_IN`
  → in-stay operations and Incident handling
  → departure / authorized Checkout → `CHECKED_OUT`
  → completion evaluation → `COMPLETED` where conditions pass
  → post-stay history and eligible domain processes
```

`SCHEDULED → DID_NOT_OCCUR` remains the separate pre-Check-in/final-policy outcome.

## 5. Stay Entry / Origin Findings

Stay may arise from a confirmed Stayora Booking or an accepted External Accommodation basis. External Accommodation does not require a fake Stayora Booking. Every Stay retains source/provenance, but operational actors primarily consume Stay, party, access, arrival and issue truth.

## 6. Stay Lifecycle Findings

Only the canonical CP4/CP7 lifecycle is used: `SCHEDULED → CHECKED_IN → CHECKED_OUT → COMPLETED`, with `SCHEDULED → DID_NOT_OCCUR`. `PREPARATION` and `READY` are operational milestones; `ARRIVAL` is an observation; `IN_STAY` is not added. B4 creates no lifecycle state.

## 7. Operational Responsibility Findings

Action owner, information consumer, evidence recorder, exception owner, commercial authority and operational authority are distinct capacities. A Butler or BQL context may record/consume operational information without becoming Booking, pricing, payment, Inventory, settlement or reputation-consequence authority.

## 8. Pre-arrival Findings

Host retains operational responsibility; assigned Butler prepares and coordinates; Destination/BQL consumes destination-scoped upcoming occupancy/access/service information. Guest provides allowed party/arrival information and receives relevant preparation/help information. No PMS, concierge suite or workforce-management model is introduced.

## 9. Readiness Findings

Operational readiness is a projection/milestone. It does not create `READY` in the Stay lifecycle, guarantee Check-in or change Availability. Readiness blockers remain visible to the responsible context; exact criteria and escalation owner are TBD.

## 10. Arrival / Check-in Findings

Expected arrival, physical arrival, access and formal Check-in are separate. Arrival is not automatically Check-in. Check-in requires canonical preconditions, authorized context and evidence; `SCHEDULED → CHECKED_IN` is the only lifecycle transition. Payment is not converted into a Stay state. Whether an applicable payment/compliance condition may block Check-in remains policy/legal TBD.

## 11. In-stay Operations Findings

During `CHECKED_IN`, Guest, Host, Butler and Destination/BQL coordinate support, access, destination services and operational evidence. No `IN_STAY` state is added. Guest Access remains scoped; operational visibility does not expose full commerce or grant authority.

## 12. Incident / Exception Findings

The stress test preserves `Incident ≠ Finding ≠ Responsibility ≠ Consequence`. Reports and evidence may be recorded, routed and escalated. No blame, compensation, refund, financial deduction, Reputation change, Verification change, Settlement effect or Inventory Block is automatic. An unusable-villa report may enter a separate authorized Inventory/Block workflow, which belongs to later policy/B5 work.

## 13. Checkout / Completion Findings

Scheduled departure, physical departure, Checkout and completion remain separate. Authorized Checkout transitions `CHECKED_IN → CHECKED_OUT`; it does not release Inventory or make the Stay Completed automatically. `COMPLETED` requires canonical completion conditions; open Incidents only block completion when a policy-defined qualifying exception applies. A post-Completed complaint does not reopen Stay automatically.

## 14. Butler Boundary Findings

Butler may prepare, coordinate arrival/Check-in/Checkout where granted, support Guests, report readiness and Incidents and preserve evidence. Butler does not automatically accept Booking, set price, manage Inventory, handle payment/refund/Settlement/Payout, assign blame or impose Reputation/Verification/financial consequences.

## 15. Destination/BQL Boundary Findings

BQL consumes destination-scoped operational occupancy, arrival/departure, access, registration, vehicle, service and issue data where allowed. Operational Occupancy is not Commercial Availability. BQL does not gain Booking Authority, pricing, payment, Owner economics, Sale commission or full ledger access.

## 16. Guest Operational Findings

The Guest can know relevant Stay details, access/help path, instructions and issue status; participate in arrival/Check-in/Checkout; report problems; and receive truthful completion/follow-up outcomes. B4 does not choose an app, chat, QR, notification provider or authentication mechanism.

## 17. Cross-Context Projection Findings

One Stay truth projects differently to Guest, Host, Butler, BQL, Admin and Quality. Projections are need-to-know and context-scoped. They do not create duplicate Stay lifecycles or allow a projection to become commercial source of truth.

## 18. Responsibility Handoffs

The handoff sequence is Accommodation Basis → Stay preparation → Butler/Destination readiness → arrival observation → authorized Check-in → in-stay operations → Incident handling where needed → authorized Checkout → completion evaluation → eligible post-stay domains. Each handoff transfers bounded operational responsibility, not all related authority.

## 19. Stay Origin Comparison

B1 and B3 share Stayora Booking provenance; B2 retains External Accommodation provenance. All three use the same Stay lifecycle and operational semantics. Origin-specific differences concern basis, evidence, access/consent and downstream commercial treatment—not a separate Stay state machine.

## 20. Inventory Relationship Findings

Inventory remains derived from effective Commitments and Blocks. Check-in does not create a Commitment. Checkout does not release Inventory. Completion does not make a Unit Available. Operational events may feed a separate authorized Inventory/Block workflow, but B4 does not define that workflow.

## 21. Correction / Historical Truth

Incorrect arrival, Check-in, party, Checkout, late entry, Incident or assignment changes use amendment, supersession, replacement or explicit correction while preserving original source, actor, authority and time. Completed Stay is not silently rewritten or reopened by a later complaint.

## 22. Alternative / Failure Paths

The register covers insufficient basis, incomplete data, missing assignment, unready Villa, early/late arrival, access failure, arrival without Check-in, payment/compliance blocker, conflicting Incident reports, unusable accommodation, departure without Checkout, Checkout with open Incident, incomplete completion and `DID_NOT_OCCUR`.

## 23. TBD / Policy Boundaries

Open boundaries include external Stay acceptance, readiness criteria, Check-in authority/preconditions, payment/compliance blocking, Butler assignment, BQL fields/retention, Incident severity/consequences, completion blockers, `DID_NOT_OCCUR` evidence, operational-to-Inventory Blocks, corrections and post-stay domain timing. See [15-tbd-policy-register.md](b4-stay-operations/15-tbd-policy-register.md).

## 24. Domain / Workflow / Authority Gaps

Gaps are classified as workflow, policy, authority, privacy, state-machine, Inventory policy or V0-scope gaps. B4 adds no aggregate, entity, state, permission or task-management domain to resolve them.

## 25. V0 Scope Check

B4 remains within CP5 manual-assisted Stay operations, scoped Guest access, Butler/Destination coordination, Incident recording and lifecycle evidence. It does not expand into PMS, Channel Manager, housekeeping workforce management, maintenance suite, advanced concierge, CRM, native app, advanced task management, Managed Operations, Affiliate Network, advanced Reputation, dynamic pricing or destination ERP.

## 26. Contradictions Found

No new contradiction was introduced. B4 explicitly prevents:

- Booking being treated as Stay;
- External Accommodation being converted into fake Booking;
- commerce origin creating separate Stay lifecycles;
- arrival being treated as Check-in;
- Checkout being treated as Completion;
- Butler/BQL visibility being treated as commercial authority;
- Incident being treated as blame, compensation or Reputation consequence;
- Stay events silently controlling Inventory Availability.

## 27. Readiness Assessment

**ACCEPTED FOR CP8-E EXIT.** FD-01 → FD-07 close the B4 architecture. Readiness criteria, Incident procedure/consequence, privacy, no-show effects and connectivity remain TBD and are preserved.

Conditions:

1. Preserve the canonical Stay lifecycle and keep operational milestones/events separate from states.
2. Resolve or explicitly scope Check-in authority/preconditions, readiness criteria, completion blockers, Incident policy, privacy fields and operational-to-Inventory rules before implementation-level specification.
3. Keep Butler and BQL operationally scoped; do not infer commercial authority from visibility or assignment.
4. Do not treat this report as screen design, implementation authorization or Founder Freeze.

## 28. Validation

- Stay remains independent from Booking: **PASS**.
- External Stay does not require fake Stayora Booking: **PASS**.
- B1/B2/B3 origins converge operationally while preserving provenance: **PASS**.
- No separate Stay lifecycle by origin: **PASS**.
- Only canonical Stay states used: **PASS**.
- Readiness/arrival treated as milestone/event, not new state: **PASS**.
- Booking confirmation not treated as Check-in: **PASS**.
- Arrival not automatically treated as Check-in: **PASS**.
- Checkout not automatically treated as Completion: **PASS**.
- Butler/BQL retain operational scope without commercial authority: **PASS**.
- Guest Access does not imply operational authority: **PASS**.
- Incident remains separate from Finding/Responsibility/Consequence: **PASS**.
- No automatic financial, Reputation or Verification consequence: **PASS**.
- Inventory remains commitment-derived; Stay does not silently control Availability: **PASS**.
- Corrections preserve historical truth: **PASS**.
- Authority claims trace to CP3; lifecycle claims to CP4/CP7; V0 claims to CP5; context claims to CP6/CP8-A: **PASS**.
- No persistence assumption became product policy: **PASS**.
- No TBD silently closed: **PASS**.
- No new domain concept, lifecycle state, permission or task-management domain introduced: **PASS**.
- No screen, wireframe, prototype, Figma, component, token, API, code, schema or migration created: **PASS**.
- No B5 or later work started: **PASS**.
- Markdown file/anchor links: **PASS — 182 Markdown files, 0 broken file/anchor links**.

Return this report to the Founder and Product Architect as the accepted B4 journey baseline. Do not mark CP8 complete or begin Onboarding/Workspace/Interaction/Design System work until explicitly directed.
