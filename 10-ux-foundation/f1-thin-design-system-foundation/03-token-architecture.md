# F1. Semantic token architecture

## Layers

```text
Primitive / reference values
        ↓
Semantic tokens
        ↓
Component or application usage
```

**Primitive/reference values** are the eventual palette, type scale, spacing units, radii, borders and elevation references. They may be changed without changing product meaning. F1 does not choose final brand colors, font files or CSS variables.

**Semantic tokens** name meaning in the interface. They are the stable layer that maps a primitive value to a product role. A semantic token may be remapped for contrast, theme or surface profile without changing domain truth.

**Component/application usage** consumes semantic tokens for a specific primitive or pattern. It must not introduce a private meaning that conflicts with the semantic layer.

## Required semantic categories

| Category | Example semantic role | Boundary |
|---|---|---|
| Surface/background | `surface.canvas`, `surface.panel`, `surface.elevated`, `surface.inverse` | Describes presentation hierarchy, not object lifecycle. |
| Foreground/text | `fg.default`, `fg.muted`, `fg.subtle`, `fg.inverse` | Text priority must remain readable and explicit. |
| Border/separator | `border.default`, `border.subtle`, `border.strong` | A border does not itself mean blocked or invalid. |
| Interactive/action | `action.primary`, `action.secondary`, `action.destructive`, `action.disabled` | Visibility of an action is not authority. |
| Focus | `focus.ring`, `focus.inset` | Must remain visible independent of color-only state. |
| Selection | `selection.background`, `selection.foreground` | Selection is a UI condition, not confirmation. |
| Disabled | `disabled.surface`, `disabled.fg`, `disabled.border` | Explain unavailable authority or precondition where material. |
| Success | `state.success` | Interaction outcome only; never a universal domain state. |
| Warning | `state.warning` | Presentation emphasis; it does not decide policy. |
| Danger/destructive | `state.danger`, `action.destructive` | Communicates consequence or risk, not blame. |
| Informational | `state.info` | Contextual explanation, not evidence of authority. |
| Pending/processing | `state.pending` | Work is unresolved; never implies success. |
| Unknown | `state.unknown` | Authoritative outcome is unresolved; distinct from failure. |
| Attention | `state.attention` | Something requires responsible review; no lifecycle is implied. |
| Conflict | `state.conflict` | Truths cannot safely coexist; no winner is announced. |

## Rules

- A visual state is not a Booking, Payment, Inventory, Stay, Verification or Incident state.
- `UNKNOWN` must have a distinct text/icon/treatment from `FAILED`; `PENDING` must not look completed; `CONFLICT` must not use a winning/losing treatment.
- Color may reinforce a label but never carry the only meaning. Status text, accessible names and supporting provenance remain available.
- Do not assign permanent colors to domain objects such as “green = Booking” or “red = Block”. Semantic meaning belongs to the condition being communicated.
- Surface profiles may tune density and composition for the seven surfaces, but they reuse these semantic meanings.
