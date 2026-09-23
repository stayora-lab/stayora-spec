# CP6 Journey Validation

> Status: **STABLE — CHECKPOINT 6 DOCUMENTED; NOT IMPLEMENTATION FREEZE**

CP6 was checked against the five CP5 critical journeys.

1. **Sale-assisted Booking — PASS.** Sale uses Find a Villa → Request; Host accepts; commitment/payment/Booking/Stay/Guest Access/operations converge without a duplicate Booking entry.
2. **External Booking → Stay Operations — PASS.** Host/authorized actor records external truth → Confirmed Accommodation Commitment → derived Availability → Stay → Butler/BQL → scoped Guest access. Commerce remains externally originated.
3. **Direct Guest Booking — PASS.** Marketplace → Villa → Request → Host → applicable payment → Booking → Stay Access → Operations; it converges with Sale-assisted truth.
4. **Owner/Maintenance Block — PASS.** Host Calendar → Owner/Maintenance Block → Availability Block → derived Availability. No Booking, Stay or fake Guest is created; Issue → Availability Block is authority-scoped.
5. **Incident/Exception — PASS.** Observation → Incident → assessment → finding → responsibility → consequence. Operational resolution does not automatically mean closure, responsibility, refund or Verification consequence; later complaints do not reopen a Completed Stay.

These results validate information architecture against CP5. They do not close policy TBDs or make CP6 an implementation specification.
