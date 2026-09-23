# Revalidation

Revalidation is conceptually required immediately before consequential actions whose truth may change: Inventory/Blocks, Booking Request, Booking confirmation conditions, Property publication, Butler Assignment, authority/relationship, Payment Condition/Attempt, Stay Check-in/Checkout and Inventory interventions.

Revalidation checks current state, scope, authority, relevant conflicts and policy preconditions. If changed, do not commit against stale truth; show the new known truth and route to conflict, retry or manual assistance. No API, polling or freshness threshold is specified.
