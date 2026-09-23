# F1. Shape, border and elevation foundation

Use a deliberately small visual hierarchy:

```text
layout → spacing → typography → surface → border/elevation
```

## Shape

Keep a small radius set: one control radius, one panel/card radius and one larger emphasis radius where a public surface genuinely needs it. Avoid decorative rounding that changes the perceived meaning of a control or status.

## Border and separators

Use subtle separators for grouping and stronger borders for input/action boundaries or explicit emphasis. A border does not mean invalid, unavailable or committed without accompanying semantic text. Error and conflict treatments must include label/copy/icon or structure, not only a border color.

## Elevation

Use a small hierarchy such as base, raised and overlay. Prefer surface contrast, spacing and typography before shadow. Elevation indicates layering (for example a dialog or popover); it does not indicate authority, trust, verification or payment success.

Exact radius, border widths, shadow recipes, dark-theme behavior and motion of overlays remain open for later F work.
