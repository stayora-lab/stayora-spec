# F1. Open questions and design dependencies

F1 records these items without resolving them.

## Design TBDs

- final brand palette and contrast-tested mappings;
- font family, weight availability, locale and numeric/tabular treatment;
- exact spacing, breakpoint, radius, border, elevation and motion values;
- dark mode or other theme requirements;
- primitive API/naming conventions and implementation mapping;
- exact table/calendar/date-range compositions;
- localization, text expansion and content-length assumptions;
- final touch-target minimum and any device-specific exceptions;
- visual treatment for credential/access states once credential policy is decided.

## Product/domain dependencies

These remain upstream decisions or policy boundaries: Booking/payment economics; Required Payment Condition and Payment Obligation timing; Inventory precedence; role/relationship authority and grants; Guest credential mechanism, expiry, sharing and privacy; Request expiry; cancellation/refund/no-show; Emergency Protective Hold duration; Temporary Inventory Commitment duration; Admin/BQL grants; Attention lifecycle; domain state definitions; Verification evidence/review policy; Reputation inputs; external source labels; and any new workspace or actor.

When a prototype needs one of these to render a branch, it must use an explicit placeholder and preserve the TBD label. F1 does not convert a visual need into a product requirement.
