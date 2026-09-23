# Request ↔ Booking Stress Test

Pending Requests live in Host Requests (`HST-03`) and Sale activity projections. Request Detail (`HST-04`) is the authorized decision context. Accepted Request hands off to Booking Detail (`HST-05`) only when the canonical workflow creates a Booking; it is not a status mutation of the same object. Confirmed Bookings are contextual in Host Bookings & Stays and Sale outcomes. No fake Request → Booking lifecycle is introduced.
