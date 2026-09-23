# F2. Core primitive specifications

These specifications are prototype-ready guidance, not a production component library. Names are descriptive; exact React/Tailwind/Radix APIs remain implementation work.

| Primitive | Purpose / anatomy | Variants and states | Accessibility / token use / constraints |
|---|---|---|---|
| **Button / Action** | Label, optional leading/trailing icon, optional busy indicator | Primary, secondary, subtle, destructive; default, hover, active, focus, disabled, processing | Text label for consequential action; focus and disabled reason; action tokens; never hide authority in styling. |
| **Link** | Text or clearly labelled linked object | Inline, navigation, quiet; visited/focus | Semantic link, keyboard reachable, no link styled as mutation button. |
| **Field** | Label, control, help, error, optional scope/required note | Default, focused, invalid, disabled, read-only | Programmatic label/error association; never rely on placeholder or color. |
| **Input / Textarea** | Single/multiline value with stable label | Default, invalid, disabled, read-only, processing | Preserve input on recoverable errors; `aria-describedby`-style help/error mapping later. |
| **Form structure** | Field grouping, summary, action area | Single step, grouped, consequential summary | Logical heading/order; summary names scope and outcome; no invented wizard. |
| **Status / Badge** | Short text + optional icon for an interaction/presentation outcome or current-domain presentation | Neutral, current-domain, observed, protective, success, info, warning, danger, processing, pending, unknown, attention, conflict, corrected/superseded | Text is primary meaning; color/icon supplementary; current-domain and protective treatments are not generic SUCCESS/CONFLICT and never encode a domain object as a permanent color. |
| **Alert / Callout** | Persistent explanation with title/body/actions | Info, warning, danger, pending, unknown, conflict | Announced appropriately; persistent where unresolved truth matters; no toast-only consequential outcome. |
| **Card / Panel** | Surface grouping for one coherent responsibility | Default, elevated, interactive, selected | Heading and landmark structure; composition must not fragment one canonical object. |
| **Dialog** | Focus-trapped overlay for decision/support | Informational, confirmation, form, resolution | Focus return, labelled title, escape/cancel rules, scroll-safe; confirmation does not create authority. |
| **Sheet / Drawer** | Responsive contextual surface for detail or action | Side/bottom, read/detail/action | Accessible heading/focus, overlay scroll, clear dismiss; preserve scope/context. |
| **Loading** | Skeleton or progress indication for known work | Skeleton, inline progress, blocking only when necessary | Do not announce completion; retain known current truth where possible. |
| **Empty State** | Valid scope with no objects | Neutral, first-use, no-results | Explain scope and legitimate next action; not a failure or permission denial. |
| **Error State** | Known failure explanation and safe recovery | Inline, section, page-level | State known failure, preserve context, support keyboard and screen readers. |
| **List** | Repeated objects with summary and optional attention | Comfortable, compact, selectable | Stable headings/row labels; do not imply a row is editable or authoritative. |
| **Table foundation** | Comparable rows/columns with sticky context when useful | Compact, responsive, evidence-oriented | Header associations, reflow/scroll plan, no clipped scope or color-only status. |
| **Date / Calendar (limited core for G)** | Date/range selection and Unit × Time projection shell | Range selection, focused date, past date, conflict/unknown overlay | Text/icon + color; calendar cell is a projection, not an Inventory record; no direct “Available” edit. |

## LIKELY, not promoted without evidence

Select/Combobox, Checkbox/Radio/Switch, Popover, Tabs, Menu, Tooltip, Toast and Avatar/Identity marker remain LIKELY. Select/Combobox is likely for Working Context/resource filters; Toast is limited to low-consequence feedback; other promotions require CP8-G evidence.
