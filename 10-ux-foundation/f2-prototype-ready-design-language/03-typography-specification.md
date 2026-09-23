# F2. Prototype-ready typography

**Status:** **ACCEPTED — F2 FOUNDER VISUAL DECISION**, with semantic roles accepted from F1. Exact font loading/fallback remains implementation TBD.

## Accepted typeface pairing

- **Plus Jakarta Sans** is the accepted primary direction for product, marketplace, forms and workspaces. It supports clear labels, compact lists and numeric alignment.
- **Cormorant Garamond** is accepted as a selective editorial/display accent for destination or hospitality expression. It is not used for status, authority, payment, calendar, error or dense operational truth.

This is a two-family candidate, not a requirement to load both on every surface. Font availability, licensing, fallback and localization remain TBD.

## Role specification

| Role | Treatment | Guardrail |
|---|---|---|
| `display` | Cormorant accent or Jakarta display weight on selected public expression | Never required to understand a task or outcome. |
| `page-title` | Jakarta strong; one clear responsibility title | Do not use for decorative marketing in workspaces. |
| `section-heading` | Jakarta semibold; groups a decision-relevant region | Heading structure must remain semantic. |
| `object-title` | Jakarta semibold; Property, Unit, Request, Booking, Stay or case | Qualify the object; no universal “confirmed” title. |
| `body` | Jakarta regular; explanatory and decision-support text | Use for truth and consequence copy. |
| `compact-body` | Jakarta regular/medium for dense lists and tables | Preserve readable line-height and zoom. |
| `label` | Jakarta medium/semibold; explicit control label | Icon-only consequential actions are not sufficient. |
| `metadata` | Jakarta regular/medium; provenance, actor/context, source and time | Never make authority or error meaning depend on tiny text. |
| `numeric/tabular` | Jakarta tabular numerals for dates, money, counts and IDs | Numeric alignment does not imply payment or settlement authority. |

Avoid one-off sizes. Prototype mapping should use a small scale of role-specific steps and test text expansion, zoom and dense rows before selecting exact values.
