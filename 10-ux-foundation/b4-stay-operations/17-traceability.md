# B4 — V0 and Source Traceability

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

| B4 claim/capability | CP5 V0 dimension | Actor/context | CP6 surface | Canonical truth | Authority/lifecycle source | B4 source |
|---|---|---|---|---|---|---|
| Accommodation Basis → operational Stay | Destination Stay Coverage; Inventory Trust | Host/Operations/Admin | Host / Operations / Guest Access | Stay + Booking or External Accommodation basis | CP3 recording authority; CP4/CP7 Stay | [B4-A01](02-detailed-stay-operations-journey.md#phase-a--stay-becomes-operationally-relevant) |
| Pre-arrival preparation | Destination Stay Coverage | Host/Butler/BQL | Butler / Operations | Stay `SCHEDULED`, Arrival, Access | CP3 Butler/Destination scope; CP6 Operations | [B4-B01](02-detailed-stay-operations-journey.md#phase-b--pre-arrival) |
| Readiness milestone | Destination Stay Coverage | Butler/Host/BQL | Operations | Readiness projection, not `READY` state | CP4 Stay lifecycle | [B4-C01](02-detailed-stay-operations-journey.md#phase-c--readiness) |
| Arrival and Check-in | Destination Stay Coverage | Guest/Butler/Host/BQL | Guest Access / Operations | Arrival event; `SCHEDULED → CHECKED_IN` | CP3 capabilities; CP4 Stay | [B4-D01](02-detailed-stay-operations-journey.md#phase-d--arrival), [B4-E01](02-detailed-stay-operations-journey.md#phase-e--check-in) |
| In-stay support | Destination Stay Coverage; Guest Trust | Guest/Host/Butler/BQL | Guest Access / Operations | `CHECKED_IN`, Access, operational events | CP5/CP6; no `IN_STAY` state | [B4-F01](02-detailed-stay-operations-journey.md#phase-f--in-stay-operations) |
| Incident handling | Incident/exception V0 | Guest/Butler/Host/BQL/Admin | Issues / Operations | Incident + evidence, separate downstream cases | CP4 Incident; CP7 quality/cases | [B4-G01](02-detailed-stay-operations-journey.md#phase-g--incident--exception) |
| Checkout and completion | Destination Stay Coverage | Guest/Butler/Host/Operations | Departures / Operations | `CHECKED_OUT` → completion evaluation → `COMPLETED` | CP4/CP7 Stay | [B4-H01](02-detailed-stay-operations-journey.md#phase-hi--checkout-preparation-and-checkout), [B4-J01](02-detailed-stay-operations-journey.md#phase-jk--completion-and-post-stay-handoff) |
| Post-stay history | Guest Trust; destination history | Guest/Host/Quality/Admin | Guest / Operations / Admin | Stay history, Review Right/quality evidence where eligible | Each domain’s own authority/policy | [B4-J01](02-detailed-stay-operations-journey.md#phase-jk--completion-and-post-stay-handoff) |

## V0 boundary

B4 stays within CP5 manual-assisted Stay operations, scoped Guest access, Butler/Destination coordination, Incident recording and lifecycle evidence. It does not introduce a PMS, Channel Manager, housekeeping workforce management, maintenance suite, advanced concierge, CRM, native app, advanced task management, Managed Operations, Affiliate Network, advanced reputation, dynamic pricing or destination ERP.

## Source order

Founder decisions → canonical CP1–CP6 architecture → CP7 conceptual model → accepted CP8-A/B1/B2/B3 → supporting persistence constraints. No lower-priority source resolves a TBD.
