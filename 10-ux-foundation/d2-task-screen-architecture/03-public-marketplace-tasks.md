# Public Marketplace — Task Architecture

**Surface:** Public Marketplace · **V0:** MUST BUILD discovery, public listing truth and Direct Guest intent.

| ID | Task (user goal) | Type | Information needed | Structural home | Authority / handoff |
|---|---|---|---|---|---|
| PUB-T1 | Discover a Destination relevant to the trip intent | Primary | Destination proposition, public trust, public supply signal | `PUB-01 Destination Discovery` | Public; into `PUB-02` |
| PUB-T2 | Understand a Property/Unit accommodation proposition | Primary | Property, Unit, public facts, trust/Verified projection | `PUB-03 Accommodation Detail` | Public; into date/intent |
| PUB-T3 | Understand public price and relevant date availability/bookability | Primary | Public Price, derived Availability, contextual Bookability | `PUB-04 Date & Availability Intent` | Public; into request |
| PUB-T4 | Initiate a Direct Guest Request or consultation | Primary | selected Unit, dates, party intent, known conditions | `PUB-05 Request Entry` | Guest intent → Host Request |
| PUB-T5 | Understand why an option is unavailable or not requestable | Supporting/attention | derived conflict/bookability explanation at permitted level | `PUB-03` or `PUB-04` | No mutation; no invented status |

The inventory does not assume a checkout. Payment/confirmation remains downstream of the canonical Request → authorized decision path in B3. Public screens expose no private economics, authority, incident details or operational notes.
