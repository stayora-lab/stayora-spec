# Domain, workflow and authority gaps

| Class | Observed need | Existing concept | Impact / escalation |
|---|---|---|---|
| DOMAIN GAP | Distinguish candidate Property identity from duplicate representation | Property + provenance | Clarify canonical matching policy before implementation |
| AUTHORITY GAP | Owner relationship and grantor/basis beyond the V0 unit-hosting flow | Relationship + Authority Grant | ADR-P075 resolves real Destination-scoped Admin operational hosting approval and explicit grants in V0 only; legal ownership and other-flow rules remain open |
| POLICY GAP | Publication prerequisites and Verification display | Property readiness + Verification | Policy decision; keep separate |
| WORKFLOW GAP | Legal claim conflict and revocation paths beyond the decided V0 transfer slice | C1 correction/history | ADR-P075 resolves initial Primary, acceptance-based transfer, Co-host provenance and Admin exception; legal conflict and revocation timing remain open |
| PRIVACY GAP | Owner/Host/financial visibility by relationship | Scoped access principle | Need explicit data-access policy |
| V0-SCOPE GAP | V0 Admin-assisted operational hosting verification and exception boundary | CP5 manual assistance | Resolved for ADR-P075 hosting/Primary scope in CP5; legal ownership evidence and future Destination requirements remain separate/open |

The original C2 architecture added no aggregate, state, permission, actor or legal process to close these gaps. [ADR-P075](../../00-start-here/DECISIONS.md#adr-p075) now supplies only the scoped V0 disposition above; [ADR-P076](../../00-start-here/DECISIONS.md#adr-p076) governs the separate payout-recipient rule. No schema/API or legal process is introduced here.
