# Guest Credential Boundary

A QR/credential is a scoped access mechanism where canonical; it is not authority. Generation timing, expiry, sharing, revocation, offline behavior, contact exposure and retention remain unresolved. Guest access branches depending on those decisions are locally blocked, while Stay truth remains available where safe.

Per [ADR-P077](../../00-start-here/DECISIONS.md#adr-p077), the existing Guest Credential also applies to accountless Guest access beginning at Request-level where protected access is required, tied to the relevant relationship/lifecycle. Contact Identity ≠ Guest Credential ≠ Resource Identifier: a Request/Booking/Stay URL or identifier alone, or matching/re-entered email or phone, is not access authority. Guest Credential is not a Host/Admin role grant or delegation; existing need-to-know/progressive disclosure applies. Exact credential and recovery mechanisms remain TBD.
