# Guest Stay Access — Task Architecture

**Surface:** Guest Stay Access · **V0:** MUST BUILD scoped Stay access for B1/B2/B3/B4.

| ID | Task | Type | Information needed | Structural home | Authority / handoff |
|---|---|---|---|---|---|
| GST-T1 | Access the truth of a confirmed/represented Stay | Primary | Stay, accommodation basis, dates, party-scoped information | `GST-01 Stay Hub` | Scoped Guest relationship |
| GST-T2 | Understand where and how arrival/check-in happens | Primary | Property/Unit, arrival guidance, authorized Butler/Destination contact | `GST-02 Arrival & Access` | Guest → Butler/BQL/Host operations |
| GST-T3 | Use a scoped credential or QR where canonical | Primary | credential projection, scope, validity | `GST-02` | Credential is not authority |
| GST-T4 | Contact the correct operational actor for help | Supporting | need-to-know contact/operational context | `GST-03 Help & Operational Contact` | Scoped handoff |
| GST-T5 | Understand current Stay milestone and relevant exception | Supporting/attention | canonical Stay state, operational exception | `GST-01` | Does not invent UI status |
| GST-T6 | Enter an eligible review flow | Supporting | Review Right and relevant completed Stay context | `GST-04 Review Entry` | Eligibility-based; Review ≠ Reputation |

A full Guest account is not required where B3 canonical access permits a scoped link/credential. No Guest screen grants Booking, Inventory, Payment or operational authority.
