# Cross-policy reconciliation scenarios

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**

Each scenario preserves domain truth, policy outcome, tested invariants, and unresolved policy without inventing a rule. `PASS` means the architecture handles the boundary without inventing a missing policy; `TBD` means the boundary remains intentionally unresolved. The compact cases below should be read as facts/trigger → affected truth/invariant → expected result → unresolved policy.

1. **Request then external commitment — PASS:** Request becomes CONFLICTED. It never held Inventory. External is earlier only because it established a valid commitment first, not because a channel outranks another.
2. **Temporary commitment then discovered external booking — TBD:** classify whether external commitment was earlier but discovered late or created later during temporary exclusivity. Preserve both commitments, timestamps, evidence and authority basis; no silent overwrite. Resolution is **TBD**.
3. **Oceanami 10m, 5m unpaid at T-24 — TBD:** T-48 is assurance only. UNKNOWN blocks automatic Default. After reconciliation/grace, Default may be determined with policy consequences. Collected 5m is not automatically revenue or Earned commission. The >24h/≤24h policy evaluation timestamp remains a Founder Decision.
4. **Full-paid Guest never arrives — PASS:** do not release Inventory, cancel Booking, or mark Completed early. Accommodation right remains through its period; exception Economic Eligibility may apply under policy.
5. **Owner cancels Verified villa after full payment — PASS:** commitment ends authoritatively, Availability recomputes, Stay may be DID_NOT_OCCUR, Money handles refund/remediation, distribution attribution is protected, and Verification may review. Cancellation does not automatically remove Verified or delist.
6. **Serious service failure during Stay — PASS / TBD details:** Incident handles evidence/remediation/findings/responsibility. Complaint does not automatically suspend Verified; only a qualifying unresolved exception may delay completion. Taxonomy, authority and appeals remain TBD.
7. **Whitelisted Sale later platform-suspended — PASS:** Platform Eligibility overrides Whitelist for the affected effective capability; relationship history remains and unrelated roles are not silently suspended.
8. **External Airbnb Stay with evidence — PASS:** no fake Stayora Booking and no automatic commission; qualifying evidence may create Review Eligibility/Review Right.
9. **Co-host accepts then authority revoked — PASS:** valid historical acceptance remains valid; revocation affects future authority. Any fraud/error remediation is explicit and audited.
10. **Identity is Sale and Co-host — PASS / TBD details:** record acting capacity per action. Request as Sale does not use Co-host authority; acceptance as Co-host is audited as Co-host. Dual-capacity/self-dealing policy remains **TBD**.

Open conflict resolution, exact payment grace, exception economics, and dual-capacity rules remain open in [Open Policy Questions](22-open-policy-questions.md).
