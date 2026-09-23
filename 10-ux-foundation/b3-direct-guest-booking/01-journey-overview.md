# B3 — Direct Guest Booking Journey Overview

> Status: **DRAFT — FOUNDER / PRODUCT ARCHITECT REVIEW** · **NOT FROZEN**

## Purpose

B3 asks one architecture question: can a Guest initiate Stayora-originated accommodation commerce directly while the canonical Request, Authority, Inventory, Payment, Booking and Stay boundaries remain intact?

## Canonical journey

```text
Guest demand
  → Public Marketplace discovery
  → dates / occupancy evaluation
  → Availability and actor-specific Bookability evaluation
  → Guest chooses to proceed
  → Guest (or an explicitly supported representative) creates Booking Request
  → Host / Primary Host / delegated Booking Authority accepts or rejects
  → Inventory revalidation and applicable finite commitment
  → Required Payment Condition and Payment Attempt
  → all Booking Confirmation Conditions pass
  → Booking `CONFIRMED`
  → Guest confirmation / eligible Stay Access
  → Host / Butler / Destination Operations
```

The sequence is a UX reasoning path. It does not add states or imply that every branch is V0-supported.

## What makes B3 direct

- The Guest is the demand initiator and public discovery actor.
- No Sale is required to discover supply, create a Request or confirm a Booking.
- No Sale attribution is fabricated when no Sale relationship or source exists.
- The same downstream Inventory, Payment, Booking and Stay truth used by B1 remains authoritative.
- A Guest can be represented as a person/party without making a registered account or login mandatory.

## What B3 does not mean

`Direct Guest Booking ≠ Instant Book`. The default B3 path preserves the Request and Host/authorized Booking Authority decision. Instant Book remains a separately controlled branch whose eligibility, scope, acceptance authority, payment timing and conflict behavior are not decided here.

`Guest intent ≠ Booking`. A Guest choosing a unit or starting a Request does not create a Booking, reserve Inventory, create Payment or create a Stay.

`Booking ≠ Stay`. A confirmed Booking may make a Stay representation operationally relevant, but Check-in and Completed remain separate Stay lifecycle outcomes.

## B3 success question

Can a Guest reach truthful Stayora-originated commerce and, after confirmation, receive scoped accommodation access without Sale dependency, false confirmation, automatic reservation or hidden resolution of authentication/privacy policy?
