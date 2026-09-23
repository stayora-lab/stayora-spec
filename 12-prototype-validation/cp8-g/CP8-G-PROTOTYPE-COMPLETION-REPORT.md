# CP8-G Prototype Completion Report

> CP8-G status: **READY FOR FOUNDER / PRODUCT ARCHITECT VALIDATION**  
> CP8-H: **NOT STARTED**

CP8-G is a prototype/validation checkpoint. The artifact is a local deterministic simulation, not production implementation.

## A. Source-of-truth reviewed

Reviewed the current canonical Start Here, Source of Truth and Decisions layers; CP8-A through CP8-E accepted UX/domain/interaction baselines; CP8-F1 and CP8-F2 accepted design language; the CP8-F2 closure report and visual specimen; CP5–CP7 scope, IA and conceptual data-model boundaries where required by the journeys. CP8-F2 is authoritative for visual treatment, including domain-state vs SUCCESS, PROCESSING vs UNKNOWN, Protective Hold and External Fact vs External-backed Commitment.

No Grok source files were present in the current workspace. The accessible Grok Stayora browser prototype was inspected read-only: it provided a public marketplace shell, accommodation imagery treatment, category navigation, search composition, destination sections, cards and a Host entry point. Existing F2 specimen composition was used as the local starting point; no Grok semantic assumptions were imported.

## B. Prototype workspace / files changed

Created the dedicated prototype workspace [`12-prototype-validation/cp8-g/`](./README.md):

- [`index.html`](index.html) — seven-surface interactive shell.
- [`styles.css`](styles.css) — warm cream F2 language, responsive layout and semantic presentation families.
- [`app.js`](app.js) — deterministic local state, object transitions and contextual projections.
- [`dataset.json`](dataset.json) — small illustrative Oceanami dataset.
- [`VALIDATION-PACKAGE.md`](VALIDATION-PACKAGE.md) — entry instructions and scenario matrix.
- this report.

Updated only current status pointers and the canonical output archive to record CP8-G as ready for validation. No production application architecture was mutated.

## C. Grok reuse / adaptation summary

No Grok source files were available to copy from the workspace. Read-only inspection of the existing Grok browser prototype informed compatible composition only: public accommodation card hierarchy, imagery treatment, destination sections, search shell and Host entry point. The prototype also adapts CP8-F2 patterns: workspace cards, dense calendar composition, panels, list rows, responsive rail behavior and warm-surface token direction. Rejected Grok semantics are explicitly absent: Request is not Booking, acceptance is not confirmation, payment method is not proof of payment, there is no universal 24-hour expiry, dates do not create Stay state, and no cancellation silently reopens Inventory.

## D. Prototype architecture

The artifact is a single static HTML shell with CSS and a local JavaScript state model. A shared state object renders surface-specific projections. Buttons simulate authority checks, revalidation, payment outcomes, external validation, Inventory implications and Stay transitions. There is no network, backend, persistence or real authentication.

The model keeps Request, Booking, Payment, Stay, Inventory truth, Evidence, Attention and External Accommodation as separate concepts. Surface navigation changes projection/context; it does not change canonical truth.

## E. Prototype dataset

Oceanami is the pilot context. The dataset includes Villa 03 and Villa 04, Guest G-001, Host HOST-03, Sale SA-014, Butler BUTLER-07, BQL-OCEANAMI and ADMIN-01, with RQ-104, BK-084, ST-084, PA-084 and ER-019. Illustrative values are not product policy.

Representative Inventory truths include Owner Block, Maintenance Block, Emergency Protective Hold, Temporary Exclusive Commitment, Confirmed Accommodation Commitment, External-backed Commitment, Conflict, Derived Availability and Contextual Bookability.

## F. Primary vertical slice

The spine is rendered in the journey strip and can be stepped through: Marketplace discovery → Request → Host decision → confirmation conditions → Booking CONFIRMED → Guest Stay Access → SCHEDULED → READY → arrival OBSERVED → authorized CHECKED_IN → authorized CHECKED_OUT → separate completion evaluation → COMPLETED. The prototype also exposes the explicit DID_NOT_OCCUR branch.

## G. Direct Guest scenario

Marketplace creates RQ-104 with source Direct. Host Workspace shows the same Request truth. Host ACCEPTED remains distinct from Booking CONFIRMED. Confirmation evaluation requires applicable conditions; Payment SUCCEEDED is shown as an interaction outcome and does not automatically create Booking confirmation.

## H. Sale-assisted scenario

Sale Workspace creates the same canonical Request with source/attribution SA-014. The flow converges on Host decision, Inventory implication, confirmation conditions, Booking and Stay. Sale can initiate where allowed but cannot accept the Request or inherit Host authority. No DirectBooking/SaleBooking variants are created.

## I. Payment UNKNOWN scenario

Admin can simulate Payment UNKNOWN. The UI says processing may have completed but the authoritative outcome is currently unknown, blocks unsafe duplicate action and keeps Booking UNCONFIRMED. No retry timing, grace period, refund, deposit or cancellation economics are invented.

## J. Guest Stay Access scenario

Guest Stay Access offers a scoped credential projection and an authenticated Guest Identity projection. The credential path does not require an account. The UI explicitly states credential ≠ authority and access does not mutate Stay state. SCHEDULED, CHECKED_IN, CHECKED_OUT and COMPLETED remain distinct projections.

## K. Stay Operations scenario

Butler Ops demonstrates READY, arrival OBSERVED, authorized Check-in, operational support, authorized Checkout, separate Completion evaluation and explicit DID_NOT_OCCUR. Arrival observation does not auto-check in. Butler assignment does not grant authority. Checkout does not equal Completion, and Completion does not infer Inventory release.

## L. Incident / Evidence scenario

Destination / BQL can record an operational observation as Incident/evidence. Attention is projected from that underlying truth. The prototype does not create a generic Task entity or silently mutate Inventory from evidence.

## M. Emergency Protective Hold scenario

Destination / BQL can create and revalidate a scoped Emergency Protective Hold with protective/attention presentation. The calendar and card state distinguish it from Maintenance Block, Conflict, Finding, proof of uninhabitability and Booking cancellation. No universal duration is invented.

## N. Inventory Conflict scenario

The calendar shows a Unit × Time with Maintenance Block plus External-backed Commitment, source/basis and Attention. The conflict entry states NO WINNER and does not select universal precedence, preserving FD-09.

## O. External Accommodation scenario

Admin demonstrates External Report / Evidence → External Accommodation Fact → Inventory evaluation → External-backed Commitment → legitimate Stay. The path does not create a Stayora Request, Stayora Booking, Stayora Payment, commission, settlement or payout merely to reuse internal commerce UI.

## P. Inventory / Calendar

The adapted calendar includes Owner Block, Maintenance Block, Emergency Protective Hold, Temporary Exclusive Commitment, Confirmed Accommodation Commitment, External-backed Commitment, Conflict, Derived Availability and contextual bookability. It remains a projection of truth; no universal Available / Unavailable switch or PMS behavior is implemented.

## Q. Authority / Working Context

Material actions show Can See, Can Initiate, Can Act, Can Act if scoped, Cannot Act and Authority Unknown. The Working Context card identifies perspective/scope and states that it does not grant permission. Assignment, relationship, BQL visibility and Guest credentials are shown as distinct from authority. Consequential actions re-check local state before transition.

## R. Seven-surface coverage

| Surface | Depth | Evidence |
|---|---|---|
| Public Marketplace | HIGH | discovery, property, Request creation and contextual bookability |
| Guest Stay Access | HIGH | credential/identity paths and Stay projections |
| Host Workspace | HIGH | Request decision and confirmation conditions |
| Sale Workspace | MEDIUM | attribution and convergence |
| Operations — Butler | HIGH | operational lifecycle and exception |
| Operations — Destination/BQL | MEDIUM | Inventory, evidence, Hold and Conflict |
| Stayora Admin | exception/reconciliation | Payment UNKNOWN and External Accommodation |

Owner remains a perspective/context inside Host/Property architecture; no Owner top-level workspace was created.

## S. Responsive coverage

The CSS provides mobile navigation and narrow-screen layouts for Marketplace, Guest Stay Access and Butler Ops, while desktop layouts support Host Workspace and the dense Inventory calendar. The calendar preserves horizontal scrolling for dense truth. Responsive validation is demonstrated by the responsive rules and requires Founder/Product Architect review on actual target devices.

## T. Simulation / mock boundaries

All transitions are deterministic local mocks. There are no real payment, identity, credential, messaging, external-channel or persistence integrations. Simulated behavior is labeled in the shell and documented here. No production schema/API decision is introduced.

## U. Semantic regression validation

| Check | Result |
|---|---|
| Request ≠ Booking ≠ Stay | PASS |
| ACCEPTED ≠ CONFIRMED | PASS |
| Payment SUCCEEDED ≠ automatic Booking CONFIRMED | PASS |
| Payment UNKNOWN ≠ FAILED / SUCCESS | PASS |
| Arrival OBSERVED ≠ Check-in | PASS |
| Checkout ≠ Completion | PASS |
| Completion ≠ Inventory release | PASS |
| Incident/evidence does not auto-mutate Inventory | PASS |
| Protective Hold ≠ Maintenance Block ≠ Conflict | PASS |
| Inventory Conflict has no universal winner | PASS |
| External Fact ≠ External-backed Commitment | PASS |
| External path does not fabricate Stayora commerce | PASS |
| Working Context ≠ Authority | PASS |
| Attention remains a projection | PASS |
| CP8-F2 semantic presentation corrections preserved | PASS |
| Rejected Grok semantics absent | PASS |
| CP8-H remains not started | PASS |
| JavaScript syntax check | PASS |
| Dataset JSON parse | PASS |
| Canonical Markdown links | PASS — 674 files, 0 errors |

## V. Open TBDs / upstream issues

No upstream issue was silently resolved. Remaining TBDs include credential mechanism/expiry/revocation, payment/deposit/cancellation economics, confirmation policy details, evidence standards, Protective Hold duration/revalidation policy, conflict resolution procedure, Admin/BQL grants, Attention lifecycle, notifications, external-channel validation rules, Sale economics and release consequences. These remain outside the prototype decision layer.

## W. Validation package

The package consists of this report, [`README.md`](README.md), [`VALIDATION-PACKAGE.md`](VALIDATION-PACKAGE.md), the interactive [`index.html`](index.html) specimen and deterministic [`dataset.json`](dataset.json). It includes entry instructions, prototype/journey maps, surface/scenario coverage, representative rendered specimens, simulated behavior, limitations, unresolved TBDs, semantic regression checks and Founder validation questions.

## X. CP8-G exit assessment

The coherent vertical slice and required scenario demonstrations exist in the prototype. The artifact is ready for Founder/Product Architect validation. “Ready” means the review package is prepared; it does not mean any question has been accepted by Founder, and it does not mark CP8-G frozen or accepted.

## Y. Roadmap status

| Checkpoint | Status |
|---|---|
| CP8-F1 | ACCEPTED |
| CP8-F2 | ACCEPTED |
| CP8-F | COMPLETE / ACCEPTED |
| CP8-G | READY FOR FOUNDER / PRODUCT ARCHITECT VALIDATION |
| CP8-H | NOT STARTED |

CP8-G stops here. CP8-H is not started, and CP8 is not declared complete.

---

CP8-G:
READY FOR FOUNDER / PRODUCT ARCHITECT VALIDATION

CP8-H:
NOT STARTED

STOP.
