# Destination Operations

> Status: **PARTIAL — only the Oceanami pilot configuration is written**
> Decision basis: [ADR-P005](../00-start-here/DECISIONS.md#adr-p005)

This directory holds Destination Operations: destination-local policies, configuration and integration. Stayora Core defines reusable capabilities; a Destination defines local policies and configuration ([ADR-P005](../00-start-here/DECISIONS.md#adr-p005)).

## Contents

| Destination | File | Status |
|---|---|---|
| Oceanami | [Oceanami pilot configuration](oceanami/configuration.md) | CONFIRMED — Oceanami Pilot configuration |

## Not yet written

The remaining Destination Operations material from the original plan is **NOT YET WRITTEN**: destination model, stay operations, BQL, security/access, QR, butler operations, arrival, checkout and local services. Absence means not written, not out of scope.

## Boundary

Nothing in this directory may contradict a CONFIRMED decision in [DECISIONS](../00-start-here/DECISIONS.md).
