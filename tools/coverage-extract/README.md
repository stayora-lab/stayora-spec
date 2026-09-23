# Coverage evidence extractor

Run from the repository root with an explicit prototype commit:

```sh
python3 tools/coverage-extract/extract.py 5c39748168a939eea66e6df68c8ceea98ec0f094
python3 -m unittest discover -s tools/coverage-extract/tests
```

The command fetches only the requested full 40-character commit from the public `stayora-lab/stayora-new` repository into a temporary shallow checkout. It runs no prototype build and makes no change to that repository. For an existing local checkout at the requested commit, `--prototype-dir /path/to/checkout` avoids the network and accepts a short SHA; the tool verifies the checkout's `HEAD` matches the argument. It never selects a branch or defaults to a current prototype revision.

Output is `generated/coverage/<first-seven-SHA-characters>.md`; the report header contains the full resolved prototype SHA, extraction time and spec commit holding the mapping. The extractor writes no canonical spec file. It reports matching tests and exported engine functions for each guardrail, constants from the config module, lifecycle state unions from domain types, and unmatched tests/functions. Missing expected source files are explicit in the report.

`guardrails.yml` is a human-maintained YAML 1.2 file written in JSON syntax, so Python's standard library can parse it. It has the 19 exact canonical row names, expected prototype source files and lists of case-insensitive substring patterns. Prefix a pattern with `re:` for a case-insensitive regular expression. A pattern changes which evidence is surfaced; it does not determine coverage. Review the unmapped section on every run because it exposes prototype behavior outside the current mapping.

This tool does not assign coverage states, judge whether a test proves an invariant, reconcile the canonical table or alter the prototype. A matched name is a pointer for human inspection, not a validation result. Its lexical parser recognizes single-line `it`/`test` names, exported `function` declarations, config `const` declarations and string-literal type unions; computed names or dynamically generated tests need manual review.
