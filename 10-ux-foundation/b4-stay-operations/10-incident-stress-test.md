# B4 — Incident Stress Test

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Scenario: Guest reports an operational problem during Stay

```text
Guest / Butler / Host / Destination observation
  → Incident record / report
  → scoped evidence and operational response
  → escalation where severity/scope requires
  → resolution or follow-up evidence
  → optional downstream Finding / Responsibility / Consequence review
```

| Step | Known operational truth | Actor/context | Safe projection | Boundary |
|---|---|---|---|---|
| Report | A Guest or operator reports an observation/problem. | Guest, Butler, Host, BQL or authorized Staff. | Reporter sees acknowledgement/status where allowed. | Complaint/Observation is not automatically Incident until the Incident context accepts it. |
| Incident | A scoped case may be opened with facts and provenance. | Incident handling context. | Relevant handlers see facts/urgency. | Incident is not Finding, Responsibility or Consequence. |
| Response | Operations coordinates immediate support or escalation. | Butler/Host/BQL within scope. | Guest receives appropriate support/status. | No blame or compensation is inferred from response. |
| Evidence | Reports, observations, corrections and response evidence are retained. | Actual actors and assigned handlers. | Need-to-know evidence only. | Evidence does not grant authority or prove liability automatically. |
| Follow-up | Qualifying facts may be referred to Quality/Verification/Reputation/Money. | Owning downstream domain. | Only eligible outcome is projected. | No automatic refund, deduction, Reputation change, Verification change or Settlement consequence. |

## Incident boundaries

- An Incident does not itself change Stay state, Availability, Inventory, Booking or Payment.
- An unusable-villa report may support a separate authorized Maintenance/Operational Block workflow; Butler reporting alone does not create the Block.
- Open Incident does not automatically block `COMPLETED`; only policy-defined qualifying unresolved exceptions may do so.
- A post-Completed complaint does not reopen Stay; it is a later case/history path.
- Any Finding, Responsibility or Consequence requires its own evidence, authority, policy and audit trail.
