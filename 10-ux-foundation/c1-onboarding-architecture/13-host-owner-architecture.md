# C1 — Host / Owner Architecture

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Separate capacities

- **Owner:** Legal/economic relationship to a Property/Party, subject to evidence and policy.
- **Primary Host:** Hosting authority anchor for a Property in the Stayora context.
- **Host:** Hosting/commercial responsibility in a valid scope.
- **Co-host:** Delegated relationship for named capabilities/resources/lifecycle.
- **Financial Beneficiary:** Separate financial relationship/capability; not inferred from Owner or Host.

## Architecture cases

| Case | Resulting model | Not implied |
|---|---|---|
| Owner and Host are same Identity | One Identity, two capacities/relationships, possibly explicit authority. | Every finance/Inventory/Booking action. |
| Owner differs from Host | Owner relationship and hosting relationship both preserved. | Owner automatically overrides Host or Host becomes Owner. |
| Host operates without proven legal ownership | Hosting authority may be established separately where policy supports it. | Legal title or financial beneficiary. |
| Co-host joins Property | Delegated capability/resource/lifecycle scope. | Primary Host powers or unrestricted delegation. |
| Owner changes | New relationship/authority effective from a defined time; old actions remain historical. | Destructive rewrite or automatic cancellation. |

Exact evidence, precedence, delegation, transfer and finance grants remain TBD. C1 does not design the Host/Owner onboarding journey.
