# Payment Interaction Boundary

Preserve Required Payment Condition, Payment Obligation, Payment Attempt and Payment Default distinctions. Interaction may represent Payment Attempt PROCESSING, SUCCEEDED, FAILED or UNKNOWN, and Booking confirmation only when canonical conditions are met. No deposit percentage, grace period, retry count, refund, cancellation, default timing or release timing is invented. Branches needing those decisions are local interaction blockers.
