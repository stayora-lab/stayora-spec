# Property versus Stay assignment

| Case | Architecture status | Boundary |
|---|---|---|
| Butler responsible for a Property | Supported by CP3/B4 at conceptual level | Does not grant all Property, Booking or Inventory authority |
| Butler assigned to a specific Stay | Supported where the Stay workflow has an explicit assignment/context | Does not imply property-wide or financial authority |
| Property Butler handles multiple Stays | Compatible with one Butler serving multiple Properties/Stays | No shift/work allocation engine is created |
| Butler changes during a Stay | Supported as assignment change/revocation with history | Exact handoff/propagation is workflow TBD |
| Temporary replacement Butler | Conceptually possible via a new scoped assignment | Precedence, acceptance and notice are TBD |

C4 does not invent a primary Butler hierarchy, scheduling, staffing or assignment precedence.
