# Detailed conceptual Butler onboarding step matrix

This matrix is a reasoning aid, not a form, screen, API or persistence model.

| Step / context | Intent and entry | Identity / capacity / eligibility | Assignment / scope / basis | Authority and action | Domain/context effects | Failure / policy/TBD |
|---|---|---|---|---|---|---|
| BTL1 Identity resolution | Existing/new Identity enters self, invitation or Admin path | Identity; Party; Butler-intending capacity | Claim/application basis | Onboarding function only | Capacity proposal; no Assignment | Matching/organization policy |
| BTL2 Eligibility | Identity seeks operational eligibility | Capacity recognized; eligibility pending/approved/revoked | Platform status; no Assignment | Authorized eligibility function | Eligibility projection | Criteria/evidence/manual process |
| BTL3 Assignment proposal | Assigning actor selects operational subject | Eligible Butler where required | Property/Stay/Destination/function scope | Assignment authority required | Proposed assignment/provenance | Grantor, consent, scope, validity |
| BTL4 Assignment activation | Assignment accepted/established where policy requires | Eligibility valid; Assignment active | Resource/function/effective time | Separate action grants evaluated | Butler Context becomes useful | Propagation/revocation policy |
| BTL5 Pre-arrival/readiness | Prepare and report observations | Active Assignment | Stay/Property scope | Operational reporting/action capability | Readiness evidence; Stay state unchanged | Criteria and escalation TBD |
| BTL6 Arrival/Check-in | Coordinate arrival or record Check-in | Active Assignment + applicable action authority | Stay/access scope | Check-in authority if separately granted | Arrival observation or `CHECKED_IN` | Preconditions and access policy |
| BTL7 In-Stay/Incident | Support, observe, report, escalate | Active Assignment | Stay/function scope | Incident/evidence authority | Incident/report; no consequence automatically | Severity/escalation/privacy |
| BTL8 Inventory handoff | Route operational condition | Active Assignment; Inventory evaluator separate | Unit/time/evidence scope | Butler reports; Inventory authority decides | Possible Block only after canonical evaluation | Evidence threshold/evaluator |
| BTL9 Checkout/completion | Coordinate departure and hand off evidence | Active Assignment + Checkout authority if required | Stay/condition scope | Record Checkout; completion authority separate | Checkout/completion readiness projection | Release/completion/deposit policy |

Every step preserves actual Identity, acting capacity, Assignment, authority source, resource/function, time and result as required by CP7.
