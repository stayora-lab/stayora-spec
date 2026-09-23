# CP8-G Validation Package

## Entry instructions

Open [`index.html`](index.html) locally. Start from Marketplace and use the Reset demo control before each independent scenario. The top bar identifies the surface as a local deterministic simulation.

For responsive review, resize the browser to a narrow mobile width and inspect Marketplace, Guest Stay Access and Butler Ops; use a wide desktop width for Host Workspace and Destination / BQL.

## Prototype map

| Surface | Entry | What to inspect |
|---|---|---|
| Public Marketplace | Marketplace | accommodation detail, contextual bookability, Request creation |
| Guest Stay Access | Guest stay | credential vs authenticated identity projection; Stay lifecycle |
| Host Workspace | Host workspace | Request truth, Host decision, confirmation conditions |
| Sale Workspace | Sale workspace | attribution, initiation, authority boundary |
| Operations — Butler | Butler ops | READY, arrival observation, Check-in, Checkout, Completion, DID_NOT_OCCUR |
| Operations — Destination/BQL | Destination / BQL | calendar, evidence, Protective Hold, Conflict, Attention |
| Stayora Admin | Stayora Admin | Payment UNKNOWN reconciliation, external accommodation convergence |

## Primary vertical slice

`Marketplace → Property → Request → Host decision → confirmation conditions → Booking CONFIRMED → Guest Stay Access → SCHEDULED → READY → arrival OBSERVED → CHECKED_IN → CHECKED_OUT → COMPLETED`.

The prototype intentionally keeps Request, Booking, Payment and Stay as separate visible objects.

## Scenario matrix

| Scenario | Entry/actions | Evidence | Status |
|---|---|---|---|
| A — Direct Guest Request | Marketplace → Villa 03 → Start a request → Create Request → Host | RQ-104 exists; no reservation; Host decision is separate | DEMONSTRATED |
| B — Sale-assisted Request | Sale workspace → Create Sale-assisted Request → Host | same Request/Booking/Stay spine; Sale attribution does not accept | DEMONSTRATED |
| C — Payment UNKNOWN | Host accept → Admin → Simulate payment UNKNOWN | UNKNOWN copy, duplicate-action protection, Booking stays unconfirmed | DEMONSTRATED |
| D — Guest Stay Access | Guest Stay → switch Credential / Identity | credential path does not require account; credential ≠ authority | DEMONSTRATED |
| E — Stay Operations | Butler → READY → arrival → Check-in → Checkout → Completion | observation ≠ Check-in; Checkout ≠ Completion; explicit DID_NOT_OCCUR | DEMONSTRATED |
| F — Incident / Evidence | Destination / BQL → Record observation | Incident/evidence creates Attention; Inventory does not auto-mutate | DEMONSTRATED |
| G — Emergency Protective Hold | Destination / BQL → Create protective hold → Revalidate | protective attention distinct from Conflict and Maintenance Block | DEMONSTRATED |
| H — Inventory Conflict | Destination / BQL calendar | Maintenance Block + External-backed Commitment; no universal winner | DEMONSTRATED |
| I — External Accommodation | Admin → report → Fact → Commitment → Stay | External convergence without Stayora Request/Booking/Payment | DEMONSTRATED |

## Validation instrumentation

Each critical action can be reviewed with this lens:

| Field | Prototype evidence
|---|---|
| User intent | Guest need, Sale assistance, operational intervention or reconciliation |
| Current truth | Request / Payment / Booking / Stay / Inventory / Evidence record shown in cards |
| Acting context | top-right Working context and surface label |
| Authority | contextual `Can See`, `Can Initiate`, `Can Act`, `Cannot Act`, `Authority Unknown` markers |
| Action | button label and local mock transition |
| Expected canonical change | toast plus updated object/state projection |
| Visible result | updated card, journey spine, calendar or Attention item |
| Exception | UNKNOWN, DID_NOT_OCCUR, conflict, Protective Hold or external path |
| Question | checklist in the completion report and Validation map |

## Review questions

1. Can users distinguish Request, Booking and Stay?
2. Is ACCEPTED visibly different from Booking CONFIRMED?
3. Does Working Context remain separate from authority?
4. Is Payment UNKNOWN safe and understandable?
5. Can Guest access Stay without a mandatory account?
6. Is Butler assignment distinct from authority?
7. Is arrival observation distinct from Check-in?
8. Is Checkout distinct from Completion?
9. Is Inventory Conflict understandable without a winner?
10. Is Emergency Protective Hold distinct from Maintenance Block and Conflict?
11. Does External Accommodation avoid fake Stayora commerce?
12. Does Attention remain tied to underlying truth?
13. Do all seven surfaces feel like one product without sharing inappropriate actions?
14. Does CP8-F2 survive operational density and narrow screens?

## Evidence categories

- **IMPLEMENTED IN PROTOTYPE:** deterministic local rendering and transitions in `app.js`.
- **DEMONSTRATED:** the scenario can be stepped through in the local prototype.
- **VALIDATED:** not claimed before Founder/Product Architect review of the actual prototype.
- **FAILED VALIDATION:** none recorded yet; review may add findings.
- **NOT TESTED:** production integrations, real credentials, network failures and device-specific behavior.
- **TBD:** policy/economics, credential mechanism, expiry/revocation, evidence standards, conflict resolution and other items listed in the completion report.
