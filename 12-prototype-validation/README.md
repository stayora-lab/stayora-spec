# CP8-G — Prototype & Validation

> Status: **IN PROGRESS**
> Current v2 validation disposition: **FAILED — ITERATION REQUIRED** (baseline assessed at `5c39748`)
> CP8-H — V0 Acceptance Package: **NOT STARTED**
> Last reviewed: 2026-09-22 · Owner: Product Architect
> Depends on: Protected Baseline (CP1–CP8 CONFIRMED decisions), ADR-P066 (draft, pending entry review), FD-01 → FD-19

---

## Purpose

CP8-G does not prove that a prototype is ready for production. It proves that the V0 UX is clear, natural and consistent with the domain enough to move to **CP8-H — V0 Acceptance Package**.

Prototype versions:

| Version | Artifact | Disposition |
|---|---|---|
| v1 | Static HTML prototype — [`cp8-g/`](cp8-g/README.md) | **FAILED VALIDATION** (Product Architect disposition). Findings: *not yet filed in repo — SOURCE RECONCILIATION REQUIRED.* |
| v2 | `dev.stayora.vn`, repo `stayora-lab/stayora-new` | **IN PROGRESS** — baseline coverage below |

## Exit Principle

> **Prototype concreteness does not create product policy.**

A prototype may instantiate a TBD value in order to run. It may not resolve that TBD on behalf of the Founder. Every concrete value that stands in for an open decision is recorded under [Prototype Assumptions](#prototype-assumptions).

---

## Exit Gates

CP8-G closes only when all six gates PASS. Resolving every TBD is **not** a condition of PASS.

| Gate | PASS condition |
|---|---|
| **G1 — Experience** | Mandatory journeys can be completed end to end and feel like a real hospitality product, not a specification or state machine rendered as UI. |
| **G2 — Semantic Integrity** | No P0/P1 deviation from a CONFIRMED invariant remains. Every guardrail row is TESTED — PASS or VALIDATED ELSEWHERE. |
| **G3 — Cross-surface Continuity** | The same Request / Booking / Stay / Inventory truth is reflected consistently across every surface that shows it. |
| **G4 — Operational Usability** | Host, Sale, Butler and BQL understand "what do I need to do next" without understanding the domain architecture. |
| **G5 — Responsive & Field Reality** | Mandatory journeys are usable on their real form factor (see [Responsive requirements](#responsive-requirements)). |
| **G6 — Spec Reconciliation** | Every prototype learning is classified as *confirmed behavior / deviation / assumption / TBD* and reconciled into the spec before G closes. |

Severity: one open **P0** in G2 → G does not close. A **P1** must be fixed or carry an explicit Product Architect disposition before G closes.

---

## Guardrail Coverage States

| State | Meaning |
|---|---|
| **TESTED — PASS** | The prototype represents the guardrail and validation shows it holds. |
| **TESTED — FAIL** | The prototype represents the guardrail and violates the Protected Baseline. |
| **PARTIAL** | Represented, but not enough to verify the whole boundary. |
| **NOT REPRESENTED** | The prototype does not represent the boundary. |
| **VALIDATED ELSEWHERE** | The Product Architect determines the boundary need not be prototyped to close G, and names the canonical evidence. |

Exit rules:

- **NOT REPRESENTED ≠ PASS.** Before G closes, every NOT REPRESENTED row becomes TESTED — PASS or VALIDATED ELSEWHERE — `<canonical evidence>`.
- **VALIDATED ELSEWHERE** may be used only when the prototype does not need that representation to validate a mandatory V0 journey. If a mandatory journey depends on the boundary (for example, the Butler journey depends on Arrival Observation to show Arrival ≠ Check-in), it must be represented behaviorally. Pointing to CP8-E documentation does not satisfy it.

### Protected Baseline guardrails (minimum regression set)

Request ≠ Booking · Acceptance ≠ Confirmation · Payment SUCCEEDED ≠ automatic Booking CONFIRMED · Payment UNKNOWN ≠ FAILED · Booking cancellation ≠ automatic Stay state mirroring · Arrival observation ≠ Check-in · Departure observation ≠ Checkout · Checkout ≠ Completion · Completion ≠ Inventory release · Incident ≠ Maintenance Block · Emergency Protective Hold ≠ Maintenance Block · Emergency Protective Hold ≠ Commitment · External Report ≠ External Fact · External Fact ≠ External-backed Commitment · External Accommodation ≠ Stayora Booking · Assignment ≠ Authority · BQL visibility ≠ Authority · Working Context ≠ Authority · Conflict ≠ automatic winner.

## Representation Requirement

> Not every Protected Baseline rule must appear visibly in the prototype. Every rule necessary to validate a mandatory prototype journey must be represented behaviorally.

Behavioral representation means the product acts correctly, not that it explains itself. *BQL visibility ≠ authority* is represented by BQL having no action it is not allowed to take — not by a screen describing the authority model. *Request ≠ Booking* is represented when a Guest naturally understands "my request was sent but my stay is not confirmed yet."

> **Architecture protects the experience; it does not become the experience.**

## Known Deviation Test Rule

The test suite is an executable representation of the source of truth, not the source of truth itself.

> **A passing test does not legitimize a known deviation from the Protected Baseline.**

- A test that asserts a known deviation is marked **KNOWN DEVIATION TEST** and links to the decision it conflicts with.
- When the deviation is reconciled, code, test and coverage record change **in the same change-set**. Fixing code while leaving the old test failing is not allowed; making a test green without fixing behavior is not allowed.
- Passing test counts are recorded as implementation evidence only. They are not evidence that any gate PASSES.

## Representative Actor Validation

Two different kinds of review are required and neither substitutes for the other.

**Product Architect / Founder review** assesses conceptual correctness, product direction, information architecture, hospitality character, Protected Baseline, scope, and whether product intent is represented correctly.

**Representative actor validation** assesses whether real people understand and can use it. For each mandatory actor journey that is prototyped, at least **one representative user who did not take part in designing the spec**. This is minimum evidence, not a statistical usability claim; no pass-rate threshold is set.

PASS (qualitative, observable): *the person understands the goal, identifies the information they need and completes the core journey without the facilitator explaining the domain model or pointing to which button to press.*

If a tester has to ask how a Request differs from a Booking, the UI has failed. If a Butler has to be told that READY is only a milestone while CHECKED_IN is the Stay state, the UX has failed even though the domain model is correct.

Role questions used in validation:

| Actor | Question the UI must answer |
|---|---|
| Guest | Do I know what I am booking, what happens next, and whether it is confirmed yet? |
| Sale | Do I know which requests need follow-up and what is happening with my guest? |
| Host | Do I know what I need to decide today? |
| Butler | Opening my phone in the morning, do I know which villa to prepare, who arrives and who leaves today? |
| BQL | Can I see what is happening across the destination today and which issues need attention? |

If the UI can only answer "this is the current state of the aggregate", the gate FAILS even when semantics are 100% correct.

Validation uses the dev test dataset only. No real guests, prices or bookings.

---

## Mandatory V0 Prototype Journeys

Only these journeys are required. CP8-G does not require prototyping the whole of Stayora.

| Journey | Flow | Must be evident |
|---|---|---|
| **Guest** | Discover → Villa → Dates/Guests → Request → Waiting → Confirmation → Upcoming Stay | A Request is not a confirmed Booking — understood through the experience, without explaining the state machine. |
| **Sale / Host** | Demand → Request → Host Decision → Confirmation conditions → Booking | Sale brings demand in; Sale has no Host authority; Host decision is not Booking CONFIRMED; confirmation conditions are handled correctly. |
| **Butler** | Today → Prepare → Arrival → Check-in → In-stay → Departure → Checkout | Mobile-first operational experience. No domain-debugger presentation. |
| **Exception / Inventory** | Incident → Attention → authorized inventory intervention · Inventory Conflict → preserve conflicting truths → reconciliation | Does not need a large workspace. Both paths must be validated. |
| **External Stay** | External accommodation information → authoritative fact → applicable inventory representation → Stay | No fake Stayora Booking is created. |
| **BQL** | Today → Arrivals / In-house / Departures → Stay detail → operational attention | Feels like destination operational visibility, not a Host or Admin dashboard. |

### Responsive requirements

| Surface | Required |
|---|---|
| Guest | Mobile + desktop |
| Marketplace | Mobile + desktop |
| Host / Sale | Desktop primary; mobile sanity check |
| Butler | Mobile mandatory |
| BQL / Admin operational views | Desktop/tablet-oriented; on mobile must not break unless V0 defines mobile as primary |

No clipping, no inaccessible primary action, no unusable modal, no table that hides a core workflow.

---

## v2 Baseline Coverage — commit `5c39748`

> This snapshot is validation evidence at one specific commit. It is **not** canonical product semantics. Later iterations add new columns/tables; this snapshot is never overwritten.

Summary: **9 TESTED — PASS · 2 PARTIAL · 1 TESTED — FAIL · 7 NOT REPRESENTED**

| # | Guardrail | State at `5c39748` | Evidence | Disposition |
|---|---|---|---|---|
| 1 | Request ≠ Booking | TESTED — PASS | `domain.test.ts` #442 (distinct RQ/BK/ST ids); #778 (only payment recording creates a Booking) | |
| 2 | Acceptance ≠ Confirmation | TESTED — PASS | #390 (acceptance creates a temporary hold only); #442 | |
| 3 | Payment SUCCEEDED ≠ automatic Booking CONFIRMED | TESTED — PASS | #501 (late success → refund, no Booking); #665; #881 | |
| 4 | Payment UNKNOWN ≠ FAILED | TESTED — PASS | #472; #529 | |
| 5 | Booking cancellation ≠ automatic Stay state mirroring | **TESTED — FAIL** | `resolveConflict` sets Stay `CANCELLED`; protected by #991 and #1027 — see [KD-01](#known-deviations) | |
| 6 | Arrival observation ≠ Check-in | NOT REPRESENTED | No arrival-observation concept in the engine | MUST REPRESENT |
| 7 | Departure observation ≠ Checkout | NOT REPRESENTED | No departure-observation concept | MUST REPRESENT |
| 8 | Checkout ≠ Completion | PARTIAL | `checkOutStay` completes in the same action when nothing blocks (consistent with FD-02) but the difference is not observable | |
| 9 | Completion ≠ Inventory release | TESTED — PASS | #274 | |
| 10 | Incident ≠ Maintenance Block | TESTED — PASS | #305 (incident changes no Booking, Stay or commitment) | |
| 11 | Emergency Protective Hold ≠ Maintenance Block | NOT REPRESENTED | No Protective Hold | MUST REPRESENT |
| 12 | Emergency Protective Hold ≠ Commitment | NOT REPRESENTED | No Protective Hold | MUST REPRESENT |
| 13 | External Report ≠ External Fact | NOT REPRESENTED | Only the Host records directly; no report path from Sale/Butler | MUST REPRESENT |
| 14 | External Fact ≠ External-backed Commitment | NOT REPRESENTED | One action creates both | TBD — PRODUCT ARCHITECT |
| 15 | External Accommodation ≠ Stayora Booking | TESTED — PASS | #763; #835 | |
| 16 | Assignment ≠ Authority | PARTIAL | Engine restricts Butler to assigned villas; no dedicated test for an unassigned Butler | |
| 17 | BQL visibility ≠ Authority | TESTED — PASS | #248; #1336 | |
| 18 | Working Context ≠ Authority | NOT REPRESENTED | Roles come from links; no Working Context | VALIDATED ELSEWHERE (conditional) |
| 19 | Conflict ≠ automatic winner | TESTED — PASS | #859; #1124 | |

Correction, 2026-09-23: the baseline summary originally read 10 · 2 · 1 · 6. That was a miscount in the artifact; the per-row states are unchanged.

#### Disposition — Product Architect, 2026-09-23

Mandatory journey list: UNCHANGED. The Exit Contract is not narrowed to reduce iteration scope.

Rows 6, 7, 11, 12 and 13 MUST REPRESENT behaviorally: each is required to validate a mandatory journey — Butler for 6 and 7, Exception / Inventory for 11 and 12, External Stay for 13. Citing CP8-E documentation does not satisfy them. Row 14 has no disposition yet; it is referred to the Product Architect. The auditor's recommendation is MUST REPRESENT within G-v2.3, because the mandatory External Stay journey runs external information → authoritative Fact → applicable inventory representation → Stay, and row 14 is that third step.

Row 18 is VALIDATED ELSEWHERE: canonical evidence is CP8-D1 Workspace Surface Architecture and CP8-E1. This holds only while Working Context is not materially represented in prototype UX. If the prototype later lets one identity switch between capacities or workspaces, or Working Context becomes a real interaction, VALIDATED ELSEWHERE lapses for that scope and the boundary must be tested behaviorally.

CP8-G remains IN PROGRESS — ITERATION REQUIRED. CP8-H is not opened.

#### CP8-G v2 iteration slices

These are implementation slices inside CP8-G v2. They are not new gates, not new guardrails and not new checkpoints. Each slice delivers a real experience, not a checklist of boundaries rendered as UI. A whole-of-G validation pass across G1–G6 and cross-surface continuity follows the three slices; no slice closes G on its own.

**G-v2.1 — Butler Field Journey.** Today → Prepare → Arrival observation → authorized Check-in → In-stay → Departure observation → authorized Checkout. Demonstrates rows 6 and 7, and is expected to move row 8 (Checkout ≠ Completion) beyond PARTIAL.

**G-v2.2 — Exception and Inventory Journey.** Incident → Attention → Emergency Protective Hold → evaluation → Maintenance Block or release, together with Inventory Conflict and reconciliation. Demonstrates rows 11 and 12, and must keep Hold, conflict, Maintenance Block and Commitment visibly distinct.

**G-v2.3 — External Stay and lifecycle reconciliation.** External information / report → authoritative Fact → applicable External-backed Commitment → Stay, creating no fake Stayora Booking. Demonstrates row 13. KD-01 is reconciled in this slice, not as a separate earlier fix: the deviation sits at the Booking → Stay lifecycle boundary, so code, the two Known Deviation Tests and the coverage record change in the same change-set, as the Known Deviation Test Rule requires. Regression coverage is re-run after the change.

Implementation evidence at `5c39748`: 44 domain tests passing. Recorded for traceability only — not evidence that any gate PASSES.

### Journey coverage at `5c39748`

| Journey | Gap |
|---|---|
| Butler | Prepare, Arrival (observation), In-stay and Departure steps missing |
| Exception / Inventory | Incident → Attention → authorized intervention missing; Conflict path present |
| BQL | Operational attention missing; lists present |
| G1 / G4 | No representative-actor evidence yet |

### Iteration log

| Iteration | Commit | PASS | PARTIAL | FAIL | NOT REP. | VAL. ELSEWHERE |
|---|---|---|---|---|---|---|
| Baseline | `5c39748` | 9 | 2 | 1 | 7 | 0 |
| G-v2.1 | — | | | | | |
| G-v2.2 | — | | | | | |
| G-v2.3 | — | | | | | |
| Final validation | — | | | | | |

Every prototype change in an iteration states which **journey, gate or coverage row** it addresses.

---

## Prototype Assumptions

Concrete values in v2 that stand in for open decisions. Each is a **PROTOTYPE ASSUMPTION — NOT DOMAIN POLICY**.

| Assumption in v2 | Location | Open decision |
|---|---|---|
| Temporary Exclusive Commitment = 30 minutes | `src/lib/domain/config.ts` `HOLD_MS` | D3 — TBD, configurable (FD-10) |
| ">24h before Check-in" evaluated at Request creation | `engine.ts` `paymentPlan(…, request.createdAt)` | D5 — TBD; first define which policy the threshold governs |
| Hold keeps running while payment is UNKNOWN | engine behavior | ADR-P068 draft — bounded extension; parameters TBD |
| Check-in 14:00, time zone Asia/Ho_Chi_Minh | `config.ts` | Destination configuration — not yet specified |
| Sale commission shown as 10% of accommodation total | `config.ts` `COMMISSION_RATE` | Commission Base Value — TBD |
| Payment outcome recorded manually by Stayora operations | engine + Admin UI | Payment infrastructure — WORKING MODEL, legal validation required |
| Example villas, prices, guest data, amenity hours | seed and content files | Test data only |
| Roles assigned by link | `role.ts` | Identity / Working Context — not represented |

## Known Deviations

| ID | Deviation | Conflicts with | Tests protecting it | Status |
|---|---|---|---|---|
| **KD-01** | Ending a commitment through conflict resolution sets Stay to `CANCELLED` (Stayora and external stays). Stay has no `CANCELLED` state, and Booking cancellation must not automatically drive Stay state. | CP4 Stay lifecycle (`05-state-machines-policies/04-stay-lifecycle.md`); ADR-P066 (draft) | **KNOWN DEVIATION TEST**: `domain.test.ts` #991, #1027 | OPEN — reconcile code, tests and this table in one change-set |

---

## Exit Artifact

CP8-G ends with a **CP8-G Validation Report**, never with "the prototype looks good". It contains:

- **A. Validated journeys** — PASS / PARTIAL / FAIL per mandatory journey.
- **B. Protected Baseline regression** — final coverage table; no P0/P1 without disposition.
- **C. Founder validation findings.**
- **D. Prototype deviations** — including KD-01 until reconciled.
- **E. Prototype assumptions.**
- **F. Product learnings** — what the prototype taught about UX.
- **G. Remaining TBDs** — not force-closed.
- **H. Final disposition** — exactly one of:
  - `CP8-G FAILED — ITERATION REQUIRED`
  - `CP8-G CONDITIONALLY ACCEPTED — LISTED CORRECTIONS REQUIRED`
  - `CP8-G ACCEPTED — READY FOR CP8-H`

## Current Disposition

**CP8-G v2 — IN PROGRESS · baseline `5c39748` · FAILED — ITERATION REQUIRED**

This does not mean v2 failed the way v1 did. It means v2 has not met the exit contract.

Blocking evidence:

- **Semantic blocker** — KD-01: Booking cancellation → Stay `CANCELLED`, conflicting with the CP4 Stay lifecycle and ADR-P066, and preserved by tests #991 and #1027.
- **Coverage gaps** — 6 guardrails NOT REPRESENTED; each must be classified as required-to-prototype or VALIDATED ELSEWHERE under the constraint above.
- **Journey gaps** — Butler Prepare → Arrival → In-stay → Departure; Exception Incident → Attention → authorized intervention; BQL operational attention.
- **Actor validation** — no representative-user evidence for G1 / G4.

CP8-H is not opened.

---

## Boundary

CP8-G validates the prototype and the V0 experience. It does not resolve open product policy merely because the prototype requires a concrete value.

Only **CP8-G ACCEPTED — READY FOR CP8-H** opens CP8-H.

CP8-H — V0 Acceptance Package does not design more UX. It packages what CP8 has learned into a baseline clean enough for Implementation Planning: V0 UX baseline, validated V0 journeys, V0 user stories, acceptance criteria, remaining TBD/Hypothesis register, known deferred scope, Protected Baseline verification and implementation handoff package. Then: **CP8 COMPLETE → Implementation Planning.**
