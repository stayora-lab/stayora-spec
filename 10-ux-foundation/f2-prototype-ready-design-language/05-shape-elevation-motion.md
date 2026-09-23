# F2. Shape, elevation and motion

**Status:** **ACCEPTED — F2 FOUNDER VISUAL DECISION**; F1 hierarchy remains accepted.

## Purposeful roles

| Role | Treatment |
|---|---|
| `radius.control` | 8px reference for buttons, inputs and compact controls. |
| `radius.card` | 12px reference for cards and list containers. |
| `radius.panel` | 16px reference for larger workspace panels. |
| `radius.overlay` | 16px reference for dialogs/sheets; 24px only when an overlay composition benefits from it. |
| `radius.pill` | Full radius only for compact filters/tags/status affordances; not for every card. |

Grok's 24/32 values are not default card radii. A large radius must have a clear public/editorial or overlay purpose.

## Borders and elevation

- `border.subtle`: quiet grouping and table separators.
- `border.default`: control/card boundary.
- `border.strong`: focused section or explicit evidence boundary.
- `border.interactive`: hover/active affordance, never authority proof.
- `border.focus`: always visible keyboard focus.
- `elevation.0`: canvas/card without shadow.
- `elevation.1`: raised card or sticky context.
- `elevation.2`: overlay/dialog/sheet separation.

Prefer layout, spacing, typography and surface contrast before shadow. Shadow cannot communicate trust, verification or payment.

## Motion

Calm, functional transitions may clarify navigation, overlay entry, selection or pending progress. Motion must not conceal state changes, delay a known outcome, imply success while pending or replace a text explanation. Respect reduced-motion preferences and avoid auto-dismissing consequential outcomes.
