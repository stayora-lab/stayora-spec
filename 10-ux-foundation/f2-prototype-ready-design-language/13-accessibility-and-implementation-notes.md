# F2. Accessibility and implementation notes

## Accessibility carry-forward

F1's baseline remains mandatory: AA-oriented contrast review, visible keyboard focus, semantic labels/headings, status beyond color, including current-domain and protective presentations, associated field errors, safe touch targets, reduced motion, reflow/zoom, overlay scrolling and screen-reader-understandable outcomes. Grok contrast calculations are evidence, not certification.

F2-specific checks:

- test warm light borders and muted metadata at normal and zoomed text sizes;
- provide text/icon labels for calendar cells, current-domain state, protective attention and conflict, not color alone;
- avoid image overlays that reduce heading/action contrast;
- keep dialogs/sheets keyboard-contained with focus return and an accessible title;
- ensure dense tables have header associations, horizontal/alternate reflow and no clipped Unit × Time scope;
- preserve outcome copy for screen readers and do not auto-dismiss UNKNOWN, conflict or manual follow-up;
- preserve comfortable touch targets for Butler and Guest Stay Access;
- test text expansion/localization before selecting final widths.

## Implementation mapping boundary

The intended implementation context remains Next.js/React/TypeScript/Tailwind with shadcn/ui/Radix-style primitives where useful. F2 specifies behavior, anatomy and semantic token use; it does not write components, CSS, routes or a token file. Primitive APIs, package choices and theming remain later implementation work.
