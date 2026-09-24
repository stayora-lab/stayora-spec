Repository role: CANONICAL PRODUCT SPECIFICATION
Write owner: Codex — Spec Editor. Responsible for drafting and changing the
canonical specification.

Roles:
- Codex — Write Owner / Spec Editor: default executor for stayora-spec. Creates the
  branch, edits the canonical spec per the task contract, runs basic self-checks,
  commits, pushes and reports the diff.
- Product Architect (ChatGPT) — Review & Governance: architecture review,
  reconciliation, diff review, disposition decisions. Performs a GitHub write only
  when the Founder assigns one specific operation.
- Auditor (Claude Chat) — Independent review: challenges task contracts before work
  starts, reviews changes that touch the Protected Baseline, an ADR, a canonical
  lifecycle or the CP8-G coverage contract, and drafts and reviews prototype task
  contracts under the CP8-G Exit Contract. Read-only: never edits the canonical spec
  and never writes to any repository.
- Claude Code — Verifier / Toolsmith: read-only on the canonical spec by default.
  Verifies the task contract against the diff against the canonical baseline; runs
  CI, checkers and the extractor; reports scope and semantic regressions. Writes
  spec only when the Founder reassigns a specific task.
- Founder — Final Authority: governance and source-of-truth changes, merge approval.
- Grok — Prototype Write Owner, in stayora-lab/stayora-new only.

Authority chain: Founder decision → Product Architect disposition and task contract →
Codex implementation → required review → Founder merge. The Spec Editor writes the
specification; it does not decide it.

Role assignment is a Founder decision recorded in this file; an agent cannot change
its own role.
The party that drafted a change does not verify that change.

Review:

| Change category | Task contract | Required review |
| --- | --- | --- |
| Protected Baseline, ADR, canonical lifecycle, CP8-G coverage contract | Product Architect, with Auditor challenge while the disposition forms | Auditor + Claude Code |
| Hygiene, tooling, destination configuration that does not change canonical product semantics | Product Architect | Claude Code |
| Prototype work | Auditor, per the CP8-G Exit Contract | Auditor |

Category is decided by what the change actually alters, not by which directory the
file sits in. A change under a configuration path that in substance creates policy or
alters a lifecycle, authority or the Protected Baseline belongs in the first category.

Any change that modifies, reinterprets, extends or reconciles the Protected Baseline,
an ADR, a canonical lifecycle or the CP8-G coverage contract requires Auditor review
before merge. The Founder may override this for a specific case; an agent may not
downgrade a category to save quota.

A task contract states objective, canonical base, scope and files, invariants and
constraints, and verification and stop conditions. The executing agent reads the
canonical sources itself and finds its own evidence. Unverified conclusions must not
be put into a contract as though they were evidence.

Mechanical verification: `spec-check` scans repository Markdown for ADR/FD reference,
uniqueness, anchor, index and status rules; relative link targets; selected credential
and personal-data patterns; explicit register counts; and metadata, review-date and
simple CP-status warnings. ERROR findings fail the check; warnings alone do not.
`coverage-extract` reads a specified prototype commit and uses name patterns and a
limited lexical parser to report matching tests, exported functions, config constants,
lifecycle state unions and unmatched evidence by guardrail. It does not assign coverage
states, prove invariants, reconcile the canonical table or run a prototype build.

Holding credentials that can push to GitHub does not make an agent the write owner.

Prototype behavior, tests, deployed UI, conversations and agent memory are evidence —
they do not override this specification.

CONFIRMED decisions form the Protected Baseline.
TBD / WORKING MODEL / HYPOTHESIS must not be silently promoted.

Never change product semantics merely to match implementation.

Prototype concreteness does not create product policy.

Do not create, rename or remove roadmap checkpoints without an explicit
Founder / Product Architect decision.

No cross-repository write in the same task. A task changes the canonical spec or the
prototype, never both. Flow: spec decision/merge → SHA → prototype task →
prototype SHA → validation evidence → separate spec reconciliation task.

The prototype repository (stayora-lab/stayora-new) is owned by Grok. Agents working
here are read-only there.

This repository is public during the specification phase. Never commit credentials,
API keys, real owner names, real unit codes, real guest data, real prices, phone
numbers, emails, financial records or internal contract documents. If a decision
needs evidence from an internal document, record the conclusion and a reference —
never paste the document.

Before editing:
SOURCE_OF_TRUTH.md
→ 00-start-here/README.md
→ relevant checkpoint docs
→ DECISIONS.md / relevant ADRs
→ plan
→ edit
→ cross-reference verification
→ report.

Every PR states: which decision, gate, coverage row or task it implements; which files
changed; and which cross-references were verified.

One task, one branch, one PR. Do not bundle unrelated changes; do not mix a migration
or refactor with content decisions. Do not merge without Founder approval.
