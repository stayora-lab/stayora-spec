# B5 — Availability versus Bookability

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| Concept | Meaning | B5 implication |
|---|---|---|
| Available | Derived Inventory truth indicates no effective blocking constraint for the relevant Unit × Time, subject to canonical semantics. | A block ending may make dates Available. |
| Searchable | Supply can participate in discovery. | Searchability can persist while dates are unavailable. |
| Bookable | This actor/context/action may proceed under authority, eligibility, terms and policy. | Availability alone does not make the Unit Bookable. |

When a Block ends or is corrected, derived Inventory may become Available, but Bookability can still depend on publication, eligibility, authority, verification/trust, commercial policy, stale/unknown truth and other canonical conditions. B5 does not choose a universal re-publish or actor eligibility policy.

`Block removed → universally Bookable` is expressly false.
