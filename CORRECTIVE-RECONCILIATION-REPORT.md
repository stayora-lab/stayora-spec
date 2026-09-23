# Stayora Checkpoint 4 Corrective Reconciliation Report

> Status: **CORRECTIVE RECONCILIATION COMPLETE — AWAITING SOL / ASTRA / FOUNDER FREEZE REVIEW**

## Files changed

- `00-start-here/DECISIONS.md`
- `00-start-here/GLOSSARY.md`
- `01-product-foundation/10-oceanami-pilot.md`
- `01-product-foundation/13-open-questions.md`
- `02-domain/01-domain-glossary.md`
- `02-domain/03-domain-invariants.md`
- `03-actor-authority/05-effective-permission.md`
- `04-core-workflows/00-workflow-map.md`
- `04-core-workflows/02-instant-book.md`
- `04-core-workflows/06-completion-settlement-payout.md`
- `04-core-workflows/08-open-workflow-questions.md`
- `04-core-workflows/README.md`
- `05-state-machines-policies/03-payment-lifecycle.md`
- `05-state-machines-policies/05-settlement-and-payout.md`
- `05-state-machines-policies/06-verification-and-reputation.md`
- `05-state-machines-policies/07-incident-lifecycle.md`
- `05-state-machines-policies/08-lead-and-distribution-lifecycle.md`
- `05-state-machines-policies/09-role-application-and-eligibility.md`
- `05-state-machines-policies/10-review-rights.md`
- `05-state-machines-policies/11-policy-architecture.md`
- `05-state-machines-policies/15-commercial-exception-policy.md`
- `05-state-machines-policies/17-settlement-and-commission-policy.md`
- `05-state-machines-policies/19-distribution-policy.md`
- `05-state-machines-policies/21-cross-policy-reconciliation.md`

## Contradictions fixed

- Reconciled settlement wording so Completed Stay is the normal economic boundary, while policy-driven exception Economic Eligibility may proceed without falsifying Stay as Completed.
- Removed the stale CP2 Lead graph that mixed Lead and Lead Assignment; clarified that Sale acceptance is Assignment truth.
- Removed the misleading linear Assignment diagram and preserved transition uncertainty as policy/TBD.
- Restored Offer ownership as a conceptual composition boundary with aggregate/domain ownership still TBD.
- Reconciled Required Payment Condition, Payment Obligation and Payment Default terminology.
- Added the unresolved Founder Decision for the Oceanami >24h/≤24h policy evaluation timestamp.
- Restored safe replacement/supersession semantics for an existing accommodation commitment.
- Restored economic funding, forfeiture, refund, responsibility and commission-history invariants.

## Invariants restored or clarified

- Sale, Affiliate, Commercial Authority, Property and Operations may retain separate attribution.
- UNKNOWN provider outcomes are unresolved truth, not FAILED or automatic Default.
- Verification status, Review Case and Reputation remain separate models.
- Review Rights require evidence/eligibility; Completed is a normal basis, not an unconditional grant.
- Lifecycle diagrams are conceptual unless explicitly identified as complete transition graphs.
- Platform Suspension is scoped to affected capability and does not silently suspend unrelated roles.
- Policy scopes do not create a new global authority-precedence algorithm.
- Authority is evaluated at action time; later revocation does not retroactively invalidate a legitimate action.

## Terminology reconciled

`ACTIVE` in the older CP3 Sale wording is mapped to the current `Platform Eligibility / ELIGIBLE` capability terminology. Required Payment Condition is a condition for a specific commercial action; Payment Obligation is a due financial obligation; Payment Default is determined from the latter after applicable reconciliation. Settlement follows Economic Eligibility, with normal and exception paths explicitly separated.

## Decision and open-question status changes

Q-02 and Q-15 are marked **PARTIALLY REFINED — TBD remainder**. ADR-P020 and ADR-P021 now explicitly preserve the distinction between confirmed conceptual boundaries and unresolved transition/economic details. Offer ownership remains TBD. No new ADR identifier was created.

## Unresolved TBDs preserved

The pass did not decide inventory conflict resolution, commitment duration, concurrency/locking, cancellation/refund/default/no-show percentages, grace or UNKNOWN duration, supplier-failure economics, partial settlement, deposit/add-on economics, reputation algorithms, Lead dispatch/SLA, Affiliate rates/windows/qualification, platform fee/incentive, legal/tax/accounting, privacy fields/retention, dual-capacity/self-dealing, authority precedence, Offer aggregate ownership, completion blockers/timing, or the Oceanami policy evaluation timestamp.

## Founder Decisions still required

- Which timestamp evaluates Oceanami's >24h versus ≤24h payment policy when transaction start and confirmation cross the boundary.
- Offer aggregate/domain ownership.
- Exact exception economics, policy precedence and all parameters listed in the open-policy registers.

## Regression checks performed

- Read all 67 canonical Markdown files before editing.
- Relative Markdown links: **PASS**; 0 missing links.
- ADR definitions: 65 unique definitions; no new duplicate definition introduced.
- Open-question definitions and references reviewed; no new identifier introduced.
- Searched CP1–4 for stale settlement-only-after-Completed, mixed Lead graph, unconditional Review Right, unqualified Offer ownership and Sale `ACTIVE` terminology.
- Confirmed no new schema, API, UI, implementation, V0 or Checkpoint 5 material was added.
- Confirmed Managed remains outside current core, External Commerce remains first-class, and Booking/Stay, Authority/Access and Verification/Reputation remain separate.

## Intentionally not changed

No product model was redesigned. No TBD was closed by inference. No percentage, deadline, algorithm, legal conclusion, implementation contract or Founder Freeze status was added.

CHECKPOINT 4 CORRECTIVE RECONCILIATION COMPLETE
AWAITING SOL / ASTRA / FOUNDER FREEZE REVIEW
