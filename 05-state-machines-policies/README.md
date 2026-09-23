# Checkpoint 4 — State Machines, Lifecycles & Policy Architecture

> Status: **REOPENED FOR RECONCILIATION — 2026-09-19**  
> **DRAFT — AWAITING SOL / FOUNDER REVIEW**

Checkpoint 4 documents lifecycle boundaries and policy architecture on top of [Foundation](../00-start-here/README.md), [Domain](../02-domain/README.md), [Actor Authority](../03-actor-authority/README.md), and [Core Workflows](../04-core-workflows/README.md). It is conceptual product/domain documentation, not an implementation specification.

## Reading order

[Lifecycle map](00-lifecycle-map.md) → lifecycle models → policy architecture → policy families → [cross-policy reconciliation](21-cross-policy-reconciliation.md) → [open policy questions](22-open-policy-questions.md).

State Machine describes what happened to domain truth. Policy determines when a transition is allowed and what consequences follow. Not every concept is a state machine.

## Scope guard

No database, API, UI, provider integration, RBAC implementation, technical locking, V0 scope, or Checkpoint 5 work is defined here. `CONFIRMED`, `WORKING MODEL`, and `TBD` retain their source meaning. Oceanami-specific rules are configuration, not global Stayora invariants.
