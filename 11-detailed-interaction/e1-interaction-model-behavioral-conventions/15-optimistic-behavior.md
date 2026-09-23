# Optimistic Behavior

Optimistic canonical success is unsafe for Booking confirmation, Inventory mutation, Payment outcome, authoritative Check-in/Checkout, authority/relationship changes and other consequential actions. UX may acknowledge intent submission, but current truth must remain pending/unknown until authoritative outcome exists. Read-only or low-consequence local presentation may remain responsive without claiming domain mutation.
