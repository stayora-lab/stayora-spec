# F1. Accessibility baseline

F1 adopts a WCAG-informed baseline for later prototype work; it is not a certification exercise.

- **Contrast:** text, controls, focus indicators and status treatments remain readable against their surfaces at normal and zoomed text sizes.
- **Focus and keyboard:** every interactive element has a visible focus treatment, logical order and keyboard operation; focus is managed safely in dialogs, sheets and popovers.
- **Semantic labels:** controls, fields, links, headings, tables/lists and status regions have meaningful names and structure. Icons do not replace labels where the action is consequential.
- **Status beyond color:** success, warning, danger, pending, UNKNOWN, attention and conflict include text or an equivalent accessible announcement; color, position, hover and calendar shading are supplementary.
- **Touch and target safety:** controls have a comfortable touch target and spacing appropriate to the device; the exact minimum target and exceptions remain to be confirmed against the implementation baseline.
- **Errors:** validation and action errors are associated with the relevant control or outcome, preserve user input where safe and state the next legitimate action.
- **Motion:** respect reduced-motion preferences; no essential meaning depends on animation or timed disappearance.
- **Screen readers:** consequential outcomes name the object, action, scope, known result and unresolved condition. Live announcements are restrained so they do not create duplicate or confusing truth.
- **Zoom and reflow:** information remains usable at enlarged text and narrow widths; dense operational views may use an alternate projection rather than clipped text.

Credential/privacy copy, localization, contrast palette and exact touch-target values remain design dependencies, not silently chosen rules.
