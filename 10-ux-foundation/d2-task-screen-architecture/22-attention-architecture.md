# Attention Architecture

Attention is a projection of canonical facts into a responsibility context. No generic Task domain or universal priority algorithm is introduced.

| Attention fact | Structural home(s) | Responsible decision |
|---|---|---|
| Pending Booking Request | HST-01/HST-03/HST-04; SAL-04 projection | Host decision; Sale monitors outcome |
| Inventory conflict | HST-10; ADM-03; relevant PUB/SAL availability explanation | Authorized Inventory authority / Admin exception |
| Payment `UNKNOWN` | HST-04/05; HST-12; ADM-05; limited Guest projection | Money reconciliation authority |
| Incident | BUT-04; HST-10; BQL-03; ADM-04 | Operational/responsible authority |
| External conflict | HST-10; ADM-03; BQL-03 as need-to-know | Inventory/operations reconciliation |
| Onboarding pending | ADM-01; partial context | Eligibility/relationship authority |
| Stay operational exception | GST-01; HST-07; BUT-01/02; BQL-01/03 | Scoped operational authority |

Surfaces may embed attention into an Overview or collection. A separate attention screen is justified only where exception triage is the primary job.
