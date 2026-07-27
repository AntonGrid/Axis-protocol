# Axis Protocol – Validation Rules

> Status: DRAFT

## 1. Scope

This document defines **normative validation rules** for the Axis protocol:

- invariants over state,
- preconditions for operations,
- consistency rules.

These rules MUST hold in any conforming implementation, regardless of blockchain or runtime.

## 2. Invariants

Examples (adapt/replace):

- **I-001**: Total issued supply of an Asset MUST NOT be negative.
- **I-002**: An Asset in state `Retired` MUST NOT accept new operations modifying its state.

For each invariant:

- unique identifier (e.g. `I-XXX`),
- description,
- affected entities.

## 3. Operation Preconditions

For each protocol operation (see `wire-format.md` and `lifecycle.md`):

- input validity conditions,
- required authorizations,
- constraints on current state.

## 4. Error Model

Define:

- error categories (e.g. `ValidationError`, `AuthError`, `StateConflict`),
- how they are surfaced to clients (codes, messages),
- which errors are **normative** (must exist in any impl).
