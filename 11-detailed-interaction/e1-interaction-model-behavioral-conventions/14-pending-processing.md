# Pending and Processing

Business pending and technical processing remain distinct:

- Booking Request PENDING is business truth.
- Payment PROCESSING can be payment/domain truth.
- UI submitting/working is transient interaction behavior.

The interaction may show processing while awaiting authoritative result, but must not convert transient UI processing into domain completion or failure.
