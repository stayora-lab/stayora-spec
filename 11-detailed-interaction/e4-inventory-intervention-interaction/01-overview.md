> CP8-E4 — Inventory Intervention Interaction
> Status: **ACCEPTED — CP8-E CLOSED** · Freeze status: **CP8-E CLOSED — ACCEPTED V0 UX ARCHITECTURE BASELINE** · 2026-09-21
> This document defines interaction behavior only. It does not create a new domain, policy, lifecycle, permission, persistence model, visual design or implementation.

# Overview

CP8-E4 details V0 interaction for B5 Inventory Intervention. It connects commercial accommodation intents and commitments, Owner/Host inventory intent, operational evidence, External Accommodation truth, authorized interventions, derived Availability and contextual Bookability. Inventory UX is a projection and intervention interface over canonical Inventory truth; it is not an editable availability calendar.

The accepted chain is `intent or operational fact → authority + Unit × Time + basis/evidence → Inventory truth evaluation → authorized intervention → conflict detection → derived Availability → contextual Bookability/projection → correction, release or expiry where canonical → downstream handoff`. All unresolved policy remains visible as TBD.

**Founder-approved extension:** Emergency Protective Hold is part of the reconciled V0 vocabulary. It is a scoped protective intervention after serious operational evidence, prevents new conflicting commitments, escalates immediately and remains distinct from Maintenance Block, Finding, uninhabitable proof and existing-commitment override. Review/expiry follows policy; no universal timeout is defined.

E4 stops here. It does not start E5, CP8-F, prototype or implementation.
