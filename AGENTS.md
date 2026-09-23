Repository role: CANONICAL PRODUCT SPECIFICATION
Write owner: Claude Code — Spec Editor. Responsible for drafting and changing the
canonical specification.

Roles:
- Claude Code — Write Owner / Spec Editor.
- Product Architect (ChatGPT) — Review & Governance: architecture review,
  reconciliation, diff review, disposition decisions. Performs a GitHub write only
  when the Founder assigns one specific operation.
- Codex — Verifier / Toolsmith: checks, CI, extraction. Does not edit the canonical
  spec by default.
- Founder — Final Authority: governance and source-of-truth changes, merge approval.
- Grok — Prototype Write Owner, in stayora-lab/stayora-new only.

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
