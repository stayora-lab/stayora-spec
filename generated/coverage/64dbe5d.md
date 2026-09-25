# Coverage evidence — 64dbe5dd17f1ec3d4e0b3d513f235e50e12eeb65

Prototype repository: `stayora-lab/stayora-new`

Prototype SHA: `64dbe5dd17f1ec3d4e0b3d513f235e50e12eeb65`

Extraction timestamp (UTC): `2026-09-25T12:08:50Z`

Spec commit containing mapping: `577fc4685d36c5ea35ef8941e1d04fd6a5cae4f7`

Generated evidence. Not canonical. Coverage states are assigned by the Product Architect.

## 1. Guardrail evidence

### 1. Request ≠ Booking

- Test: `exclusive handling: INITIAL SUCCEEDED → 1 Booking, HOLD ENDED/SUPERSEDED, ids all different` — `src/lib/domain/domain.test.ts:705`
- Test: `no exported function creates a Booking except recordPayment/resolveUnknown` — `src/lib/domain/domain.test.ts:1041`
- Function: `createRequest` — `src/lib/domain/engine.ts:303`

### 2. Acceptance ≠ Confirmation

- Test: `exclusive handling: INITIAL SUCCEEDED → 1 Booking, HOLD ENDED/SUPERSEDED, ids all different` — `src/lib/domain/domain.test.ts:705`
- Function: `acceptRequest` — `src/lib/domain/engine.ts:357`

### 3. Payment SUCCEEDED ≠ automatic Booking CONFIRMED

- Test: `late SUCCEEDED after expiry → attempt stored as SUCCEEDED, 1 OPEN RefundCase, 0 Bookings` — `src/lib/domain/domain.test.ts:764`
- Test: `SUCCEEDED on INITIAL after hold ended by conflict → RefundCase INVENTORY_CONFLICT, 0 Bookings` — `src/lib/domain/domain.test.ts:928`
- Test: `external overlapping an ACTIVE HOLD → INITIAL SUCCEEDED → no Booking, RefundCase INVENTORY_CONFLICT` — `src/lib/domain/domain.test.ts:1144`
- Function: `recordPayment` — `src/lib/domain/engine.ts:677`

### 4. Payment UNKNOWN ≠ FAILED

- Test: `UNKNOWN → no Booking; second attempt refused; resolveUnknown SUCCEEDED while hold active → Booking created` — `src/lib/domain/domain.test.ts:735`
- Test: `UNKNOWN → expiry → another guest books → resolveUnknown(SUCCEEDED) → attempt stored SUCCEEDED, RefundCase OPEN, still exactly 1 Booking and no overlap` — `src/lib/domain/domain.test.ts:792`
- Test: `UNKNOWN does not win, does not block the other request, and reconciles into a refund only if money arrived` — `src/lib/domain/domain.test.ts:2058`
- Function: `resolveUnknown` — `src/lib/domain/engine.ts:728`

### 5. Booking cancellation ≠ automatic Stay state mirroring

- Function: `resolveConflict` — `src/lib/domain/engine.ts:1434`

### 6. Arrival observation ≠ Check-in

- Test: `check-in does not record an arrival observation` — `src/lib/domain/domain.test.ts:361`
- Function: `observeArrival` — `src/lib/domain/engine.ts:808`

### 7. Departure observation ≠ Checkout

- Test: `checkout does not record a departure observation` — `src/lib/domain/domain.test.ts:396`
- Function: `observeDeparture` — `src/lib/domain/engine.ts:826`

### 8. Checkout ≠ Completion

- Test: `checkout records CHECKED_OUT and leaves completion for a later evaluation` — `src/lib/domain/domain.test.ts:418`
- Function: `checkOutStay` — `src/lib/domain/engine.ts:849`
- Function: `evaluateStayCompletion` — `src/lib/domain/engine.ts:874`

### 9. Completion ≠ Inventory release

- Test: `completing a Stay does not end its CONFIRMED_ACCOMMODATION commitment` — `src/lib/domain/domain.test.ts:291`

### 10. Incident ≠ Maintenance Block

- Test: `an incident does not change Booking, Stay, or commitments` — `src/lib/domain/domain.test.ts:324`
- Function: `reportIncident` — `src/lib/domain/engine.ts:946`

### 11. Emergency Protective Hold ≠ Maintenance Block

- Function: `placeProtectiveHold` — `src/lib/domain/engine.ts:984`
- Function: `releaseProtectiveHold` — `src/lib/domain/engine.ts:1025`

### 12. Emergency Protective Hold ≠ Commitment

- Function: `placeProtectiveHold` — `src/lib/domain/engine.ts:984`
- Function: `releaseProtectiveHold` — `src/lib/domain/engine.ts:1025`

### 13. External Report ≠ External Fact

- Test: `a Sale or Butler report is not a Fact and does not hold the calendar` — `src/lib/domain/domain.test.ts:1847`
- Function: `submitExternalReport` — `src/lib/domain/engine.ts:1122`

### 14. External Fact ≠ External-backed Commitment

- Test: `a Host can record a Fact while no External-backed Commitment exists` — `src/lib/domain/domain.test.ts:1890`
- Function: `recordExternalBooking` — `src/lib/domain/engine.ts:1330`

### 15. External Accommodation ≠ Stayora Booking

- Test: `seedWorld(): no Booking exists for any Stay with origin EXTERNAL` — `src/lib/domain/domain.test.ts:1026`
- Test: `external booking on free dates → commitment + Stay, 0 Bookings, 0 obligations` — `src/lib/domain/domain.test.ts:1098`

### 16. Assignment ≠ Authority

- Test: `a Butler cannot prepare, observe, check in, or check out a villa they are not assigned to` — `src/lib/domain/domain.test.ts:461`
- Function: `checkInStay` — `src/lib/domain/engine.ts:770`

### 17. BQL visibility ≠ Authority

- Test: `BQL cannot call any Stay transition` — `src/lib/domain/domain.test.ts:265`
- Test: `BQL/Butler/Sale calling any Phase 2 function → FORBIDDEN` — `src/lib/domain/domain.test.ts:1634`

### 18. Working Context ≠ Authority

- Test: `sign-up with no grants is a guest, even if the client sends admin` — `src/lib/access.test.ts:23`
- Test: `an active grant is the role; a client-sent role is ignored` — `src/lib/access.test.ts:33`
- Test: `unsigned callers stay guests unless demo mode is on` — `src/lib/access.test.ts:101`
- Function: `resolveWorkingRole` — `src/lib/access.ts:20`

### 19. Conflict ≠ automatic winner

- Test: `external overlapping a Stayora booking → both ACTIVE, 1 OPEN conflict` — `src/lib/domain/domain.test.ts:1122`
- Test: `3-way conflict: ending one while two still overlap → STILL_OVERLAPPING, conflict OPEN` — `src/lib/domain/domain.test.ts:1415`
- Function: `resolveConflict` — `src/lib/domain/engine.ts:1434`

### 20. Commercial Acceptance ≠ Temporary Exclusive Commitment

- Test: `end HOLD → Request CONFLICTED` — `src/lib/domain/domain.test.ts:1347`
- Function: `expireHolds` — `src/lib/domain/engine.ts:219`
- Function: `acceptRequest` — `src/lib/domain/engine.ts:357`
- Function: `placeProtectiveHold` — `src/lib/domain/engine.ts:984`
- Function: `releaseProtectiveHold` — `src/lib/domain/engine.ts:1025`
- Function: `recordMaintenanceFromHold` — `src/lib/domain/engine.ts:1062`

### 21. Payment UNKNOWN ≠ Competitive Priority / Inventory Exclusivity

- Test: `competitive accept of two overlapping requests → both ACCEPTED, no hold` — `src/lib/domain/domain.test.ts:619`

## 2. Prototype assumptions found

| Name | Value | File:line |
|---|---|---|
| `HOLD_MS` | `30 * 60 * 1000` | `src/lib/domain/config.ts:6` |
| `HOST_RESPONSE_MS` | `24 * 60 * 60 * 1000` | `src/lib/domain/config.ts:13` |
| `NEAR_CHECK_IN_MS` | `48 * 60 * 60 * 1000` | `src/lib/domain/config.ts:24` |
| `NEAR_CHECK_IN_RESPONSE_MS` | `2 * 60 * 60 * 1000` | `src/lib/domain/config.ts:25` |
| `ACCEPTANCE_RESPONSE_MS` | `HOLD_MS` | `src/lib/domain/config.ts:33` |
| `COMMISSION_RATE` | `0.1` | `src/lib/domain/config.ts:35` |
| `PILOT_NOW` | `"2026-09-22T03:00:00.000Z"` | `src/lib/domain/config.ts:36` |
| `PILOT_TODAY` | `"2026-09-22"` | `src/lib/domain/config.ts:37` |
| `CHECK_IN_TIME` | `"14:00"` | `src/lib/domain/config.ts:40` |
| `TIMEZONE` | `"Asia/Ho_Chi_Minh"` | `src/lib/domain/config.ts:43` |
| `COMPLETION_BLOCKERS_DECIDED` | `false` | `src/lib/domain/config.ts:55` |
| `PREPARE_WINDOW` | `"arrival-day-only"` | `src/lib/domain/config.ts:63` |
| `PROTECTIVE_HOLD_REVIEW_MS` | `24 * 60 * 60 * 1000` | `src/lib/domain/config.ts:72` |
| `PROTECTIVE_HOLD_ACTORS` | `"bql-and-host-of-villa"` | `src/lib/domain/config.ts:82` |
| `EXTERNAL_RECORDING_ACTOR` | `"host"` | `src/lib/domain/config.ts:101` |
| `EXTERNAL_COMMITMENT_TIMING` | `"host-may-wait"` | `src/lib/domain/config.ts:110` |
| `NON_OCCURRENCE_ACTOR` | `"assigned-butler"` | `src/lib/domain/config.ts:119` |

## 3. Lifecycle states found

### RequestStatus

`src/lib/domain/types.ts:17` — `PENDING`, `ACCEPTED`, `DECLINED`, `EXPIRED`, `CONFLICTED`

### StayStatus

`src/lib/domain/types.ts:27` — `SCHEDULED`, `CHECKED_IN`, `CHECKED_OUT`, `COMPLETED`, `DID_NOT_OCCUR`, `CANCELLED`

### StayOrigin

`src/lib/domain/types.ts:35` — `STAYORA`, `EXTERNAL`

### CommitmentKind

`src/lib/domain/types.ts:37` — `HOLD`, `CONFIRMED_ACCOMMODATION`, `AVAILABILITY_BLOCK`

### CommitmentStatus

`src/lib/domain/types.ts:39` — `ACTIVE`, `ENDED`

### EndedReason

`src/lib/domain/types.ts:41` — `EXPIRED`, `SUPERSEDED`, `RELEASED`

### CommitmentBasis

`src/lib/domain/types.ts:43` — `STAYORA_BOOKING`, `EXTERNAL`, `BLOCK`

### BlockKind

`src/lib/domain/types.ts:45` — `OWNER`, `MAINTENANCE`

### CommissionStatus

`src/lib/domain/types.ts:47` — `PENDING`, `EARNED`, `VOID`

### PaymentOutcome

`src/lib/domain/types.ts:49` — `SUCCEEDED`, `FAILED`, `UNKNOWN`

### RefundReason

`src/lib/domain/types.ts:53` — `HOLD_EXPIRED`, `DUPLICATE_PAYMENT`, `INVENTORY_CONFLICT`, `CONFLICT_RESOLUTION`, `BOOKING_CANCELLED`

### Booking.status

`src/lib/domain/types.ts:101` — `CONFIRMED`, `CANCELLED`

### RefundCase.status

`src/lib/domain/types.ts:172` — `OPEN`, `DONE`

### InventoryConflict.status

`src/lib/domain/types.ts:213` — `OPEN`, `RESOLVED`

### ProtectiveHold.status

`src/lib/domain/types.ts:248` — `ACTIVE`, `ENDED`

## 4. Unmapped material

Tests and exported engine functions that matched no guardrail pattern:

- Test: `produces the same Booking and Stay shape after Host accept + payment` — `src/lib/domain/domain.test.ts:156`
- Test: `is 10% of accommodation total, only on bookings with that saleId, and stays Chờ until COMPLETED` — `src/lib/domain/domain.test.ts:202`
- Test: `refuses DID_NOT_OCCUR from CHECKED_IN` — `src/lib/domain/domain.test.ts:255`
- Test: `DID_NOT_OCCUR does not release inventory` — `src/lib/domain/domain.test.ts:307`
- Test: `observing arrival leaves the stay scheduled and does not check in` — `src/lib/domain/domain.test.ts:348`
- Test: `arrival can be noted after check-in without changing the stay` — `src/lib/domain/domain.test.ts:370`
- Test: `observing departure leaves the guest checked in and does not check out` — `src/lib/domain/domain.test.ts:382`
- Test: `departure can be noted without ever checking in` — `src/lib/domain/domain.test.ts:407`
- Test: `an open incident does not block completion and does not change checkout` — `src/lib/domain/domain.test.ts:442`
- Test: `a butler granted one villa per grant can act on each of those villas` — `src/lib/domain/domain.test.ts:488`
- Test: `Sale cannot accept a request` — `src/lib/domain/domain.test.ts:556`
- Test: `groups seed stays for 22/9 without treating external as second-class` — `src/lib/domain/domain.test.ts:574`
- Test: `two PENDING requests on the same dates → villa still available` — `src/lib/domain/domain.test.ts:594`
- Test: `exclusive handling still reserves the dates and blocks a second exclusive accept` — `src/lib/domain/domain.test.ts:652`
- Test: `reject is refused from ACCEPTED` — `src/lib/domain/domain.test.ts:685`
- Test: `BALANCE before Booking → NO_BOOKING_YET, nothing stored` — `src/lib/domain/domain.test.ts:838`
- Test: `BALANCE after Booking → stored; Booking unchanged` — `src/lib/domain/domain.test.ts:864`
- Test: `BALANCE after Booking CANCELLED → attempt stored, RefundCase BOOKING_CANCELLED` — `src/lib/domain/domain.test.ts:883`
- Test: `check-in 2026-11-02 → BALANCE dueAt = 2026-11-01T07:00:00.000Z` — `src/lib/domain/domain.test.ts:969`
- Test: `check-in 10 days ahead → 50/50; check-in 12h ahead → 100%, same villa` — `src/lib/domain/domain.test.ts:977`
- Test: `duplicate INITIAL SUCCEEDED → 2 attempts, RefundCase DUPLICATE_PAYMENT, 1 Booking` — `src/lib/domain/domain.test.ts:1057`
- Test: `Host cannot recordPayment; ADMIN can` — `src/lib/domain/domain.test.ts:1069`
- Test: `block on an occupied range → NOT_AVAILABLE` — `src/lib/domain/domain.test.ts:1178`
- Test: `releaseBlock on CONFIRMED_ACCOMMODATION → refused` — `src/lib/domain/domain.test.ts:1194`
- Test: `resolveConflict ending the Stayora commitment → Booking CANCELLED, RefundCase CONFLICT_RESOLUTION, conflict RESOLVED, no overlap remaining` — `src/lib/domain/domain.test.ts:1207`
- Test: `end Stayora commitment → Booking CANCELLED, Stay still SCHEDULED, then DID_NOT_OCCUR is a separate step` — `src/lib/domain/domain.test.ts:1254`
- Test: `end EXTERNAL commitment → its Stay stays SCHEDULED until a separate non-occurrence` — `src/lib/domain/domain.test.ts:1306`
- Test: `ending a commitment whose Stay is CHECKED_IN → STAY_IN_PROGRESS, nothing changed` — `src/lib/domain/domain.test.ts:1382`
- Test: `Commission VOID never becomes EARNED` — `src/lib/domain/domain.test.ts:1452`
- Test: `every mutating function appends exactly one audit entry` — `src/lib/domain/domain.test.ts:1492`
- Test: `placing a protective hold does not create a maintenance block` — `src/lib/domain/domain.test.ts:1698`
- Test: `recording maintenance is a separate host action and is not the hold` — `src/lib/domain/domain.test.ts:1719`
- Test: `a protective hold over a stay does not end the booking or open a conflict` — `src/lib/domain/domain.test.ts:1748`
- Test: `a protective hold blocks a new stayora commitment without choosing a winner` — `src/lib/domain/domain.test.ts:1794`
- Test: `establishing a commitment is a different truth from the Fact, and one action can write both without a Booking` — `src/lib/domain/domain.test.ts:1943`
- Test: `refuses a prose reason and accepts only a non-occurrence reason` — `src/lib/domain/domain.test.ts:1985`
- Test: `the first verified payment confirms; the other accepted request is CONFLICTED, not DECLINED` — `src/lib/domain/domain.test.ts:2023`
- Test: `competition is disclosed only from real overlapping acceptances, and the count is the same for both` — `src/lib/domain/domain.test.ts:2105`
- Test: `a PENDING request expires on its own clock; an accepted request expires on a new clock` — `src/lib/domain/domain.test.ts:2124`
- Test: `the Host-response deadline shortens near Check-in and never passes Check-in` — `src/lib/domain/domain.test.ts:2189`
- Test: `the Host may extend an acceptance deadline and may not shorten it` — `src/lib/domain/domain.test.ts:2203`
- Test: `host and butler villa grants authorize every selected villa` — `src/lib/access.test.ts:44`
- Test: `a revoke takes effect on the next resolution` — `src/lib/access.test.ts:81`
- Test: `a guest can still create a request while signed out` — `src/lib/access.test.ts:112`
- Function: `hostResponseDueAt` — `src/lib/domain/engine.ts:157`
- Function: `competingAccepted` — `src/lib/domain/engine.ts:167`
- Function: `advanceTime` — `src/lib/domain/engine.ts:274`
- Function: `createEmptyWorld` — `src/lib/domain/engine.ts:279`
- Function: `extendAcceptanceDeadline` — `src/lib/domain/engine.ts:430`
- Function: `rejectRequest` — `src/lib/domain/engine.ts:467`
- Function: `reportPrepared` — `src/lib/domain/engine.ts:790`
- Function: `markDidNotOccur` — `src/lib/domain/engine.ts:905`
- Function: `recordExternalFact` — `src/lib/domain/engine.ts:1209`
- Function: `establishExternalCommitment` — `src/lib/domain/engine.ts:1312`
- Function: `createBlock` — `src/lib/domain/engine.ts:1356`
- Function: `releaseBlock` — `src/lib/domain/engine.ts:1400`
- Function: `markRefundDone` — `src/lib/domain/engine.ts:1592`
- Function: `stayGuestLabel` — `src/lib/domain/engine.ts:1625`
- Function: `opsLists` — `src/lib/domain/engine.ts:1642`
- Function: `butlerFieldBoard` — `src/lib/domain/engine.ts:1657`
- Function: `publicStayTotal` — `src/lib/domain/engine.ts:1670`
- Function: `obligationSucceeded` — `src/lib/domain/engine.ts:1675`
- Function: `hostToday` — `src/lib/domain/engine.ts:1681`
