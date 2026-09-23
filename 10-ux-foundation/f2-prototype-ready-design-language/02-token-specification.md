# F2. Prototype-ready token specification

**Status:** reference values and visual direction are **ACCEPTED — F2 FOUNDER VISUAL DECISION**, with the semantic presentation corrections recorded below. Exact implementation mapping and the full accessibility matrix remain open.

## Accepted F2 reference palette

| Reference token | Accepted F2 value | Intended use | Status |
|---|---|---|---|
| `ref.color.cream-050` | `#f6f1ea` | warm canvas | ACCEPTED — F2 FOUNDER VISUAL DECISION |
| `ref.color.cream-000` | `#fffcf8` | primary light surface/card | ACCEPTED — F2 FOUNDER VISUAL DECISION |
| `ref.color.cream-100` | `#efe8de` | subtle surface/muted control | ACCEPTED — F2 FOUNDER VISUAL DECISION |
| `ref.color.ink-900` | `#1a1614` | primary foreground | ACCEPTED — F2 FOUNDER VISUAL DECISION |
| `ref.color.stone-600` | `#6f675e` | secondary/muted foreground | ACCEPTED — F2 FOUNDER VISUAL DECISION |
| `ref.color.plum-600` | `#9d3291` | primary action/brand direction | ACCEPTED — F2 FOUNDER VISUAL DECISION |
| `ref.color.plum-800` | `#7a246f` | accent foreground on light accent | ACCEPTED — F2 FOUNDER VISUAL DECISION |
| `ref.color.plum-050` | `#f6e8f3` | accent/subtle action surface | ACCEPTED — F2 FOUNDER VISUAL DECISION |
| `ref.color.red-700` | `#9b2c2c` | destructive/danger direction | ACCEPTED — F2 FOUNDER VISUAL DECISION |
| `ref.color.cream-border` | `#e4dcd0` | subtle/default border direction | ACCEPTED — F2 FOUNDER VISUAL DECISION |

The preliminary contrast ratios of the accepted F2 dark foregrounds are promising for normal text in the listed light pairs, but this is not certification. Focus, disabled, status, image-overlay and small-metadata combinations require a full audit.

## Semantic layer

| Semantic token family | Prototype mapping rule |
|---|---|
| `surface.canvas`, `surface.default`, `surface.elevated`, `surface.subtle`, `surface.inverse` | Use for layer hierarchy; never imply object lifecycle or authority. |
| `fg.primary`, `fg.secondary`, `fg.muted`, `fg.inverse`, `fg.disabled` | Use explicit text hierarchy; metadata remains readable at zoom. |
| `border.subtle`, `border.default`, `border.strong`, `border.interactive`, `border.focus` | Use for grouping/focus; do not make border alone mean invalid, blocked or committed. |
| `action.primary`, `action.secondary`, `action.subtle`, `action.destructive` | Availability remains authority-dependent; action styling does not grant permission. |
| `interaction.hover`, `interaction.active`, `interaction.selected`, `interaction.focus`, `interaction.disabled` | UI interaction conditions only; selected is not confirmed. |
| `outcome.success`, `outcome.info`, `outcome.warning`, `outcome.danger` | Presentation outcomes with label/icon and copy. |
| `outcome.pending`, `outcome.unknown`, `outcome.attention`, `outcome.conflict`, `outcome.corrected`, `outcome.superseded` | Separate unresolved, attention, conflict and history treatments; none is a domain state. |
| `presentation.current`, `presentation.observed`, `presentation.protective` | Neutral current-domain truth, observed milestone and protective attention treatments; never generic SUCCESS or CONFLICT. |

## Usage rule

```text
reference value → semantic token → primitive/pattern usage
```

A primitive consumes semantic tokens. A domain pattern composes primitives and adds canonical object labels, scope, provenance and next legitimate action. No token maps directly to “Booking”, “Block”, “Stay” or another domain object. `presentation.current` is a neutral/current-domain-state treatment for CONFIRMED, CHECKED_IN, READY milestones and OBSERVED facts; it is not `outcome.success`. `presentation.protective` is for Emergency Protective Hold attention and is not `outcome.conflict`. `PROCESSING` and `UNKNOWN` remain distinct: processing is known work underway, while UNKNOWN means the authoritative outcome cannot currently be established. `UNKNOWN` is visibly distinct from `FAILED`; `PENDING` cannot resemble completion; `CONFLICT` shows competing basis without winner styling.
