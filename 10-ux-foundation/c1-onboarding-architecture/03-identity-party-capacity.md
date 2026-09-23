# C1 — Identity, Party and Capacity

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Canonical model

- **Identity:** person/account capable of acting; one Identity may hold multiple capacities and relationships.
- **Party:** business, legal or economic subject; Individual Party or Organization Party. Organization is not an Identity.
- **Account:** interaction/authentication mechanism; it is not the whole Party or proof of authority.
- **Capacity / Role:** context in which an Identity acts, such as Owner, Host, Sale, Butler or Guest. Capacity does not by itself grant authority.
- **Acting capacity:** the capacity actually used for a privileged action; audit must preserve it.

## Multi-capacity rule

One Identity may be Owner, Host, Sale, Co-host, Butler and Guest in different relationships/contexts. Do not create separate accounts merely to simplify onboarding. The effective action remains:

```text
Identity + acting capacity + authority basis + resource scope + action + time
```

## Party representation

An Identity may represent or act for a Party through a valid relationship/authority basis. Legal Owner, Primary Host, Financial Beneficiary, Booking Creator, Payer, Lead Guest and Staying Party remain distinct where canonical sources distinguish them. Organization management remains OUT OF SCOPE — V0.

## Unresolved

Identity resolution, duplicate contact handling, organization representation, account recovery, evidence thresholds and field-level privacy remain policy/authority/UX TBD. C1 does not choose technical authentication or KYC.
