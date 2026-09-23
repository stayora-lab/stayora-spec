# F2. Inventory and calendar composition

## Accepted composition to keep/adapt

A prototype may use a Property × date overview with sticky resource context, range selection, focused editor/detail region, past-date differentiation and text/icon plus color. The calendar is a visual Unit × Time projection and an entry point to scoped detail, not the Inventory domain itself.

## Required layers in a calendar projection

1. Resource/property/unit identity and scope.
2. Date/range and past/future context.
3. Evidence/facts with provenance.
4. Inventory Commitments and intervention types, each labelled.
5. Derived Availability.
6. Contextual Bookability for the actor/action.
7. Conflict, stale/unknown and attention overlays.
8. Authorized action entry with revalidation.

A cell can show multiple stacked or listed bases through a focused detail region. The visual must not silently compress them into a binary booking/block state.

## Explicitly rejected calendar assumptions

- booking vs block as the only truth;
- direct editable “Available” as a canonical record;
- `Trống` / `Khoá` as the Inventory model;
- dropping overlaps;
- first-reservation-wins rendering;
- cancellation automatically reopening Inventory;
- iCal as a generic block without provenance.

External-backed commitments, Maintenance Blocks, Owner Blocks, Emergency Protective Holds and Temporary Exclusive Commitments must remain distinguishable. Emergency Protective Hold uses a protective/attention treatment with scope, escalation and review posture; it is not Conflict, Maintenance Block, Finding, proof of uninhabitability or Booking cancellation. If a Hold participates in an actual conflict, compose a separate conflict presentation. No universal conflict precedence is introduced. The prototype may show an unresolved conflict and a legitimate resolution/manual-assistance entry without deciding the winner.

When the calendar shows an Inventory truth, label **External-backed Commitment** where that is the canonical truth. Its provenance may reference the **External Accommodation Fact**; Fact and Commitment must not be collapsed.
