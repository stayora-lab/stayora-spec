# Specification checker

Run from the repository root:

```sh
python3 tools/spec-check/check.py
python3 tools/spec-check/check.py --format=json
python3 tools/spec-check/check.py --only=E4
python3 -m unittest discover -s tools/spec-check/tests
```

The checker scans Markdown files throughout the repository. It uses only Python's standard library and reads no network resources. Findings are grouped by rule and include `file:line`, source text, and a short reason. ERROR findings produce exit code 1; WARN alone produces 0. JSON emits `findings`, severity totals and the W1/W2 suppression count. `--root` selects a fixture or another checkout.

| Rule | Check |
|---|---|
| E1 | ADR/FD references resolve to canonical DECISIONS headings / Founder Decision rows. |
| E2 | ADR headings, ADR anchors and FD register rows are unique. |
| E3 | Every ADR heading has the exact immediately preceding lowercase anchor and exactly one index row; stray anchors/index rows are reported. |
| E4 | Relative Markdown link files and fragments resolve to a file and explicit ID or GitHub-style heading slug. Non-Markdown files are checked for existence. |
| E5 | ADR decision status lines and ADR index cells use the permitted statuses. `CONFIRMED — REFINED` is the sole REFINED form. Document and checkpoint statuses are outside this rule. |
| E6 | Common token/key formats, private key headers, credentialed connection URLs, email, Vietnamese mobile numbers, Oceanami unit codes and high-entropy tokens. Reviewed exceptions belong in `allowlist.txt` as `file:line matched-text`; unused entries warn. |
| E7 | Explicit ADR and contradiction-audit item counts agree with the heading and audit-row registers. |
| W1 | Spec document has a level-one heading and status/checkpoint/scope metadata in the first 12 lines. |
| W2 | `Last reviewed: YYYY-MM-DD` appears in the first 30 lines and is no more than 180 days old. |
| W3 | A linked fragment is absent from its target, suggesting a renamed heading. E4 also reports the broken link. Unused E6 allowlist entries are reported here. |
| W4 | Best-effort CP status claims compare with the evidence-backed status table in `00-start-here/README.md`. It only recognizes simple `CPn is/status` claims and reports disagreements for human review. |

To add a rule, add its severity to `RULES`, implement a deterministic scan in `run`, document it here, and add passing and failing fixture cases in `tests/fixtures/cases.json`. Keep the tests independent of live spec content. Add the rule to `--only` automatically through `RULES`.

## W1/W2 document scope

`generated/**`, `tools/**` and `.github/**` contain tooling or generated evidence rather than specification documents. W1 (header metadata) and W2 (`Last reviewed`) do not report findings for Markdown files there. The summary shows `SUPPRESSED_W1_W2`, the number of W1/W2 candidates skipped by this scope. Every ERROR rule still scans these paths, including E6 secret and personal-data detection.
