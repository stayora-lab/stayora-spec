# TBD and policy register

| ID | Boundary | Why C2 does not decide it |
|---|---|---|
| C2-TBD-01 | Identity matching/merge | Requires product and privacy policy |
| C2-TBD-02 | Ownership evidence/threshold/legal validation | Remains open; ADR-P075 resolves V0 Admin-assisted operational hosting verification only, without adjudicating ownership |
| C2-TBD-03 | Multiple Owner precedence/legal transfer | Legal/co-owner precedence remains open; V0 initial Primary, normal Primary transfer and Admin exception are resolved only under ADR-P075 |
| C2-TBD-04 | Invitation acceptance and expiry | ADR-P075 requires one recipient acceptance for normal Primary transfer; invitation expiry, wrong recipient and other invitation policy remain open |
| C2-TBD-05 | Claim conflict/dispute handling | Do not invent a dispute system |
| C2-TBD-06 | Property publication conditions | Exact moderation/commercial policy remains open |
| C2-TBD-07 | Inventory responsibility grantor/scope | ADR-P075 identifies real Destination-scoped Admin explicit unit grants for V0 onboarding, and normal transfer establishes standard authority atomically from the new Primary relationship + canonical platform policy at acceptance; the standard V0 set is defined in Authority Capabilities, while other-flow grantor rules and finer granularity remain open |
| C2-TBD-08 | Owner/Host privacy projections | Relationship/resource policy required |
| C2-TBD-09 | Effective-time and revocation propagation | CP4/authority policy dependency |
| C2-TBD-10 | Destination correction/membership workflow | Destination policy not defined here |
| C2-TBD-11 | Booking/payment/commercial readiness details | Downstream policy remains separate |

Each TBD is an explicit blocker or policy dependency, not a hidden requirement.

## CP8-E closure reconciliation overlay

C1–C4 onboarding architecture, together with E1 generic interaction grammar, is sufficient for CP8-E exit. The canonical reasoning remains Identity → Party/capacity/acting capacity → relationship → eligibility/assignment where applicable → explicit authority + resource scope → Working Context → bounded action. Invitation, Claim, Relationship, Assignment and Working Context remain distinct from Authority; Property creation does not imply Ownership, Hosting, Publication, Verification, Inventory or Payout; no universal ONBOARDED state is introduced. Remaining policy, privacy, eligibility and grant details remain TBD.

## V0 hosting / Primary-transfer disposition — 2026-09-28

[ADR-P075](../../00-start-here/DECISIONS.md#adr-p075) narrows C2-TBD-02/03/04/07 only as stated above; none is closed wholesale. Admin-approved hosting relationship is not legal ownership or implicit authority. [ADR-P076](../../00-start-here/DECISIONS.md#adr-p076) separately resolves the narrow transfer payout-recipient rule, not Financial Beneficiary or general financial grants. C2-TBD-09 (revocation effective-time/propagation) remains unchanged. Legal disputes/checklists/evidence thresholds, Owner/co-owner precedence, future independent-property onboarding, future-Destination evidence, privacy and unrelated capability/policy questions remain open.
