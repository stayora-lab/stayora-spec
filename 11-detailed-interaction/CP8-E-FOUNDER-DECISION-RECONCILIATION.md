# CP8-E Founder Decision Reconciliation — FD-01 → FD-19

> Status: **COMPLETE** · Review activity inside CP8-E, not a new checkpoint
> Scope: reconciliation of Founder decisions against E1–E4 and affected B2/B4/B5/C/D references · 2026-09-21

This register records the current canonical effect of FD-01 through FD-19. It does not erase what earlier E1–E4 artifacts correctly recorded as open at the time they were written. Residual policy, configuration, legal, privacy and implementation questions remain TBD where stated.

| ID | Current canonical decision | Reconciliation status | Residual boundary deliberately open |
|---|---|---|---|
| FD-01 | Check-in/Checkout requires explicit operational capability/grant + valid Assignment/resource scope + current Stay preconditions. Assignment, Host relationship or BQL visibility alone is insufficient. | CLOSED — architecture | Exact role/capacity grants and field policy where not separately decided |
| FD-02 | After authoritative CHECKED_OUT, completion evaluation automatically establishes COMPLETED when canonical conditions pass; a lifecycle blocker keeps completion pending for authorized resolution/re-evaluation. | CLOSED — lifecycle | Exact exception handling remains policy-bound |
| FD-03 | COMPLETED means the accommodation/Stay lifecycle is complete; it does not close Incident, Payment, compensation, Settlement or release Inventory. | CLOSED — semantics | Separate financial/Incident policies |
| FD-04 | V0 minimal completion is authoritative Checkout → CHECKED_OUT → evaluation → COMPLETED when no canonical Stay-lifecycle blocker exists. | CLOSED — conditions | No workforce/housekeeping workflow implied |
| FD-05 | DID_NOT_OCCUR is never clock-automatic: expected arrival → Attention → authorized operational evaluation → explicit action with capability + Assignment/scope + current preconditions. | CLOSED — architecture | Penalty, refund, default, cancellation and release effects remain open |
| FD-06 | Guest access is hybrid: scoped Stay Access credential or authenticated Guest Identity with legitimate Stay association/claim; both reach the same Guest Stay Hub/truth. | CLOSED — architecture | QR/link/OTP, expiry, revocation, sharing/security mechanics |
| FD-07 | Guest projection follows legitimate Guest↔Stay association, access mechanism and current Stay truth across SCHEDULED, CHECKED_IN, CHECKED_OUT and COMPLETED. | CLOSED — projection | Field-level privacy and credential security lifecycle |
| FD-08 | Inventory conflict preserves competing canonical truths, provenance and Unit×Time, identifies responsible actors/actual authority, and resolves within legitimate authority or scoped Admin reconciliation. | CLOSED — responsibility | Specific operating procedure and remedy |
| FD-09 | V0 has no universal conflict precedence or automatic winner. Confirmed/Owner/Maintenance/External truths are not globally ranked. | CLOSED — policy boundary | Case-specific legitimate resolution |
| FD-10 | Temporary Exclusive Commitment is a real truth after applicable ACCEPTED policy; duration is policy/configuration, not a hard-coded universal value; expiry/release/replacement follows policy and re-derives Inventory truth. | CLOSED — lifecycle architecture | Concrete duration, extension and policy details |
| FD-11 | Temporary release is either canonical policy/lifecycle execution or explicit scoped Inventory Release Authority + Unit×Time + current-truth revalidation; creator does not automatically retain release authority. | CLOSED — authority | Exact release conditions and timing |
| FD-12 | Only explicit scoped External Accommodation Recording Authority can establish an authoritative External Accommodation Fact. Otherwise information remains Report/Evidence awaiting review. | CLOSED — authority | Evidence standards and operating procedure |
| FD-13 | Verified Ownership Relationship provides an authority basis for a scoped Owner Block capability over Property/Unit×Time after revalidation. Ownership is not unrestricted authority, Booking Authority, Check-in/Checkout Authority or universal override. | CLOSED — authority | Exact grant administration and case remedies |
| FD-14 | Maintenance Block requires explicit scoped Maintenance Inventory Authority. Incident/Finding/evidence routes to evaluation and does not itself create a block. | CLOSED — authority | Evidence standard and operating procedure |
| FD-15 | Emergency Protective Hold is a Founder-approved protective intervention distinct from Maintenance Block, Finding and proof of uninhabitability. It prevents new conflicting commitments, escalates immediately and does not override existing commitments. | CLOSED — extension | Eligible actor grants and review/expiry policy |
| FD-16 | Emergency Protective Hold has a policy-defined review/expiry boundary. Before it, authorized Maintenance Block may supersede or an authorized determination may release; unresolved expiry leaves Attention. | CLOSED — lifecycle | Concrete duration/boundary and operating procedure |
| FD-17 | Request ACCEPTED + applicable Inventory conditions + applicable Booking Confirmation Policy may produce Booking CONFIRMED. Payment may be an input but is not universally the trigger. Payment success/failure/unknown do not map one-to-one to Booking state. | CLOSED — architecture | Payment amount/deadline/grace/retry/cancellation/default details |
| FD-18 | Payment evidence requires explicit scoped Payment Verification Authority before authoritative verification; verification is distinct from Booking Authority and Inventory Authority. | CLOSED — authority | Exact evidence/verification procedure and legal controls |
| FD-19 | Payment UNKNOWN is neither success nor failure; it prevents unsafe duplicate payment, routes reconciliation and can later resolve to SUCCEEDED, FAILED or remain UNKNOWN. | CLOSED — behavior | Retry windows, refund/cancellation/deposit/deadline and settlement details |

## Preserved invariants

- Request ≠ Booking ≠ Stay.
- External Accommodation ≠ Stayora Booking; External Report ≠ authoritative Fact; Fact ≠ Inventory Commitment ≠ Availability ≠ Bookability.
- Incident/Finding ≠ Maintenance Block; Emergency Protective Hold ≠ Maintenance Block.
- Role, Working Context, Ownership, Assignment, BQL visibility and Guest credential do not by themselves grant authority.
- Checkout ≠ Completion; Completion ≠ Inventory release/Availability.
- Payment evidence ≠ verified Payment; Payment verified ≠ Booking CONFIRMED; Payment UNKNOWN remains UNKNOWN until reconciled.
- Manual assistance preserves truth, authority, provenance and audit.

## Historical handling

E1–E4 reports and their original TBD/blocker rows retain their historical meaning. Current closure overlays are added to the affected registers and reports; old prose is not treated as a current blocker when a Founder decision now closes the architecture. No policy detail is inferred from the closure.

## Canonicalization index

| FD | Canonical ADR | Note |
|---|---|---|
| FD-05 | ADR-P066 | Clarified and generalized: DID_NOT_OCCUR is not a synonym for no-show; reason mandatory |
| FD-15 | ADR-P067 | Emergency Protective Hold is an Availability Block, not an Inventory Commitment |
| FD-16 | ADR-P067 | Review/expiry boundary remains policy-defined and TBD |
| FD-19 | ADR-P068 | Policy direction: one bounded reconciliation extension; parameters TBD |

FD entries remain the historical record and are not renumbered or superseded.
