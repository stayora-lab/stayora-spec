# Navigation Architecture

D3 defines four conceptual layers:

1. **Context layer:** select Working Context (Public, Guest Stay, Host, Sale, Butler, BQL, Admin) only when the Identity has a legitimate context basis.
2. **Primary responsibility destinations:** durable groups listed in [Primary Destination Matrix](31-primary-destination-matrix.md).
3. **Contextual object entries:** detail/collection projections reached from a responsibility destination, attention or handoff.
4. **Action/attention entries:** consequential action flows and exception projections reached from an object or responsibility context.

There is no sidebar, bottom navigation, icon set, route naming, tab styling or visual hierarchy here. Context selection and resource selection are separate from permission evaluation.
