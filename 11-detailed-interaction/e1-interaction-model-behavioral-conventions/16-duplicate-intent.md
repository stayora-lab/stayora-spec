# Duplicate Intent

When a user repeats Accept, Request submission, External Accommodation recording, Incident reporting, Check-in/Checkout or Payment retry after UNKNOWN, the interaction should show the existing known attempt/result, prevent unsafe duplicate commitment where outcome is unresolved, and route to recheck/reconciliation. No idempotency implementation is specified; duplicate safety is a behavioral requirement.
