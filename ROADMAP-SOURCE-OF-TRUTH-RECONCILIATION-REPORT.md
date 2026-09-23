# Stayora Roadmap & Source-of-Truth Reconciliation Report

## 1. Executive Summary

Stayora has not materially lost its product direction. The CP1–CP7 architecture remains coherent and preserves the core separations between identity, authority, inventory, booking, stay, money, trust and reputation. The material drift was in roadmap labeling: the supporting physical database work was presented as “CP8”, which shifted UX / Design System to an implied CP9.

The database work is useful and should be retained. It is being reclassified as **Supporting Persistence Architecture belonging to CP7 — Data Model**, with status **NOT IMPLEMENTATION FREEZE** and **SUBJECT TO UX / IMPLEMENTATION VALIDATION**. No physical implementation is authorized by this correction.

The current position is **RECONCILIATION GATE BEFORE CP8**. The next canonical checkpoint is **CP8 — UX / Design System**, which has not started. No checkpoint is being retroactively marked Founder Frozen.

## 2. Files Reviewed

The review covered the original documentation plan supplied in the source conversation, the canonical [Start Here](00-start-here/README.md), [Source of Truth](00-start-here/SOURCE_OF_TRUTH.md), [Decision Register](00-start-here/DECISIONS.md), CP1 Product Foundation, CP2 Domain, CP3 Actor Authority and Core Workflows, CP4 State Machines and Policies, CP5 V0 Scope, CP6 Information Architecture, CP7 Conceptual Data Model, the existing [supporting persistence directory](09-database-design/README.md), and the available corrective/completion reports.

The supplied original plan explicitly placed Data Model after Information Architecture and described a progression through persistence and PostgreSQL / Drizzle. It did not establish a separate canonical “CP8 Physical Database Design” checkpoint.

## 3. Files Changed

- [00-start-here/README.md](00-start-here/README.md)
- [00-start-here/SOURCE_OF_TRUTH.md](00-start-here/SOURCE_OF_TRUTH.md)
- [00-start-here/DECISIONS.md](00-start-here/DECISIONS.md)
- outputs README (file not part of this repository)
- [07-information-architecture/CHECKPOINT-6-COMPLETION-REPORT.md](07-information-architecture/CHECKPOINT-6-COMPLETION-REPORT.md)
- [06-v0-scope/CHECKPOINT-5-COMPLETION-REPORT.md](06-v0-scope/CHECKPOINT-5-COMPLETION-REPORT.md)
- [08-conceptual-data-model/README.md](08-conceptual-data-model/README.md)
- [08-conceptual-data-model/CHECKPOINT-7-COMPLETION-REPORT.md](08-conceptual-data-model/CHECKPOINT-7-COMPLETION-REPORT.md)
- [09-database-design/README.md](09-database-design/README.md)
- [09-database-design/01-architecture-principles.md](09-database-design/01-architecture-principles.md)
- [09-database-design/02-identity-party-authority.md](09-database-design/02-identity-party-authority.md)
- [09-database-design/03-property-inventory-concurrency.md](09-database-design/03-property-inventory-concurrency.md)
- [09-database-design/04-booking-external-stay.md](09-database-design/04-booking-external-stay.md)
- [09-database-design/05-money-financial-history.md](09-database-design/05-money-financial-history.md)
- [09-database-design/06-trust-quality-reputation.md](09-database-design/06-trust-quality-reputation.md)
- [09-database-design/07-constraints-temporal-provenance.md](09-database-design/07-constraints-temporal-provenance.md)
- [09-database-design/08-projections-read-models.md](09-database-design/08-projections-read-models.md)
- [09-database-design/09-postgresql-drizzle-mapping.md](09-database-design/09-postgresql-drizzle-mapping.md)
- [09-database-design/10-open-decisions.md](09-database-design/10-open-decisions.md)
- [09-database-design/CP7-PERSISTENCE-COMPLETION-REPORT.md](09-database-design/CP7-PERSISTENCE-COMPLETION-REPORT.md)
- Renamed the legacy `CHECKPOINT-8-COMPLETION-REPORT.md` to the CP7 persistence completion report above.

No source-domain, workflow, policy, UX or application-code files were created.

## 4. Canonical Roadmap Restored

| Sequence | Canonical scope |
|---|---|
| CP1 | Product Foundation |
| CP2 | Domain Map + Glossary |
| CP3 | Actor Authority + Core Workflows |
| CP4 | State Machines + Policies |
| CP5 | V0 Scope |
| CP6 | Information Architecture |
| CP7 | Data Model — Conceptual Data Model + Persistence / Physical Database Direction |
| CP8 | UX / Design System |
| Next | Implementation Plan |
| Later | Implementation — Oceanami V0; Oceanami Pilot |

The persistence material remains in `09-database-design/` for continuity, but its canonical meaning is now **supporting persistence architecture for CP7**, not a numbered checkpoint of its own.

## 5. Physical Database Reclassification

The correction changes labels, roadmap position and status language only. PostgreSQL, Drizzle mapping directions, invariant layers, temporal history, provenance, projections, transaction-boundary directions and table-family directions are retained as supporting architecture.

The retained status is:

> **SUPPORTING PERSISTENCE ARCHITECTURE — CP7 DATA MODEL**  
> **NOT IMPLEMENTATION FREEZE**  
> **SUBJECT TO UX / IMPLEMENTATION VALIDATION**

No SQL, migration, Drizzle schema, repository, API, service, job or infrastructure artifact was added.

## 6. Database-Driven Product Assumptions

### One Booking / one Unit / one Range

The previous persistence wording treated “one Booking = one Bookable Unit + one continuous accommodation range” as a V0 direction. It is now explicitly qualified as a **current V0 persistence simplification**, normally producing one Stay. It does not close the upstream TBDs for split stays, unit moves, extensions or related accommodation behavior. Those product decisions remain open and must be validated before persistence is finalized.

### Fail-closed conflict handling

The previous wording preferred temporary false-unavailability when reconciliation was delayed. It is now described as a **safety-oriented persistence direction** intended to avoid silently permitting double booking. It is not a universal product policy and does not resolve the still-open inventory conflict, concurrency, late-discovery or grace behavior questions.

## 7. Status / Freeze Reconciliation

| Checkpoint | Evidence-backed status |
|---|---|
| CP1 | Reopened for reconciliation in the current canonical tree; Founder review/freeze history is preserved at the Foundation artifact scope and is not re-declared as a global freeze here. |
| CP2 | Reopened for reconciliation; documentation exists and checkpoint-specific review remains required. |
| CP3 | Reopened for reconciliation; documentation exists and checkpoint-specific review remains required. |
| CP4 | Reopened for reconciliation; draft awaiting Sol / Founder review. |
| CP5 | Stable — checkpoint documented; not Founder Freeze. |
| CP6 | Stable — architecture reviewed; not implementation freeze. |
| CP7 conceptual | Stable — architecture reviewed; not implementation freeze. |
| CP7 persistence | Supporting persistence architecture documented; not implementation freeze; subject to UX / implementation validation. |

No Founder Freeze was granted or inferred for CP1–CP7 by this pass.

## 8. Missing-vs-Represented Original Plan Inventory

| Original-plan area | Current evidence | Classification | Timing assessment |
|---|---|---|---|
| Marketplace specification / source-of-truth layer | Foundation Marketplace Model, CP5 marketplace capabilities, CP6 Public Marketplace and shared Inventory/Property truth | PARTIALLY REPRESENTED | Can be completed inside CP8 as UX surface behavior; a deeper Marketplace policy specification can be deferred to Implementation Plan if needed. |
| Destination Operations specification / source-of-truth layer | Foundation Destination Model, CP5 operational journeys/metrics, CP6 Butler and Destination/BQL workspaces | PARTIALLY REPRESENTED | Core operational surfaces can be completed inside CP8; destination-specific policy/integration detail can be deferred. |
| Owner / Host onboarding | Actor and authority boundaries exist; no dedicated end-to-end onboarding workflow document | MISSING as a dedicated spec | Minimum V0 onboarding flow is needed inside CP8 UX; legal/compliance and automation detail can be deferred. |
| Property onboarding | Property, listing, authority and publish boundaries exist; no dedicated end-to-end onboarding workflow document | MISSING as a dedicated spec | Minimum V0 flow can be completed inside CP8; detailed policy can be deferred. |
| Sale onboarding | Sale approval/eligibility and Sale workspace are represented; no dedicated onboarding workflow document | PARTIALLY REPRESENTED | Minimum V0 interaction can be completed inside CP8; advanced approval/dispatch policy can be deferred. |
| Butler onboarding | Butler approval, assignment and operational scope are represented; no dedicated onboarding workflow document | PARTIALLY REPRESENTED | Minimum V0 flow can be completed inside CP8; staffing/assignment policy detail can be deferred. |
| V0 user stories | CP5 theses, actors, critical journeys and capability matrix provide outcome-level coverage | MISSING as the original-plan artifact | Needed before Implementation Plan; can be produced as a CP8 UX deliverable if the Founder accepts that scope. |
| V0 acceptance criteria | CP5 metrics, guardrails and journey boundaries exist, but no acceptance-criteria document | MISSING as the original-plan artifact | Needed before Implementation Plan; can be deferred until the transition into Implementation Plan, provided CP8 records testable UX outcomes. |

This inventory diagnoses coverage; it does not create the missing specifications or add folders.

## 9. Remaining Founder Decisions

Only a small set materially affects entering CP8:

- Confirm whether the minimum Owner/Property/Sale/Butler onboarding journeys are CP8 UX deliverables or must be specified as a short prerequisite before UX.
- Confirm the CP8 V0 surface boundary and review depth for Guest Stay Access, Host, Sale, Butler, Destination/BQL and Admin, using the existing CP5–CP6 architecture.
- Preserve the unresolved Guest QR/privacy field and lifecycle decisions as explicit UX constraints; do not let prototypes decide them silently.
- Keep split-stay, unit-move and extension behavior open while UX explores the V0 happy path; resolve before persistence implementation is finalized.

The remaining payment, legal, reputation, authority and conflict-policy registers are not prerequisites to start UX unless a screen or interaction would depend on a specific unresolved rule.

## 10. CP8 Readiness

**READY WITH CONDITIONS.** The conceptual architecture, V0 boundary, information architecture and supporting persistence direction are available as inputs. Entry into CP8 requires treating the persistence material as CP7 support, keeping the listed product TBDs visible, and defining the minimum V0 onboarding and acceptance-outcome coverage inside the UX checkpoint or as an explicitly approved prerequisite. This pass does not start CP8.

## 11. Recommended Immediate Next Step

Product Architect and Founder should review this reconciliation report and accept the restored roadmap labels. After that gate, start CP8 — UX / Design System against CP1–CP7, with CP5 critical journeys and CP6 surfaces as inputs, while preserving all current TBD/WORKING MODEL/HYPOTHESIS statuses.

## 12. Validation

- Internal Markdown links: **PASS** for the full canonical tree and this report; no broken relative links found.
- Stale CP8/CP9 references: database-as-CP8 and CP9-as-next labels removed; remaining CP8 references explicitly mean the next UX checkpoint.
- Status contradictions: root and Start Here summaries now state the reconciliation gate and checkpoint-specific statuses; no checkpoint is marked Founder Frozen.
- Accidental TBD promotion: none identified; the two persistence assumptions are explicitly qualified and upstream TBDs remain open.
- Accidental Founder Freeze: none introduced. Existing historical freeze wording is retained only where it describes prior artifact history.
- Schema/API/code creation: none.
- CP8 UX: not started.

## Conclusion

The canonical roadmap is restored to **CP7 — Data Model (Conceptual + Supporting Persistence Direction) → CP8 — UX / Design System**. The project remains at the **RECONCILIATION GATE BEFORE CP8** and is **READY WITH CONDITIONS** for the next checkpoint after Product Architect / Founder review.

## Current CP8 closure overlay

This roadmap reconciliation report records the pre-CP8 entry gate as it stood when authored. The subsequent CP8 work is now complete through CP8-E: A UX Foundation, B Critical Journeys, C Onboarding and D Workspace & Surface UX are complete; E Detailed Interaction is **CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE**. CP8-F Thin Design System is **NEXT — NOT STARTED**. Founder Decision Gate and Closure Coverage Pass are review activities inside CP8-E, not new roadmap units. The historical “before CP8” statements above are retained for provenance.
