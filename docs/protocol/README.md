# Axis Protocol

## Status

Informational (index of normative documents)

---

## Overview

Axis Protocol is an open, implementation-independent standard for establishing cryptographically verifiable trust between physical infrastructure and distributed digital systems.

This directory provides a human-oriented entry point into the normative Axis Protocol specification located under `spec/` and related supporting documents.

The authoritative, normative definition of Axis Protocol behavior is given by the specification documents in `spec/`.

---

## Core Specification Documents

The core, implementation- and blockchain-agnostic protocol specification is structured as follows:

- `../../spec/overview.md` — high-level overview of Axis Protocol.
- `../../spec/protocol/README.md` — index of protocol-level documents.
- `../../spec/protocol/model.md` — core data and event model.
- `../../spec/protocol/wire-format.md` — serialization and wire format.
- `../../spec/protocol/validation.md` — validation rules and constraints.
- `../../spec/protocol/lifecycle.md` — lifecycle and state transitions.

These documents are **normative** unless explicitly marked otherwise.

---

## Supporting Documentation

Additional, primarily non-normative documentation is organized as follows:

- `../architecture/` — architecture overviews, diagrams, and explanatory material.
- `../adr/` (if present) — Architecture Decision Records documenting key design choices.
- `../registry/` (if present) — registries of identifiers, types, and constants used by the protocol.
- `../rfc/` (if present) — protocol proposals, experiments, and extensions.
- `../legacy/` (if present) — historical documents kept for reference only.

Implementations **MUST NOT** derive normative behavior from these documents unless they are explicitly marked as normative or are referenced as such from the core specification under `spec/`.

---

## Domain-Agnostic Design

Axis Protocol is designed to be:

- **Domain-agnostic** — it does not assume any specific application domain (such as energy, supply chains, finance, etc.).
- **Infrastructure-agnostic** — it does not depend on any specific blockchain, distributed ledger, or runtime environment.
- **Implementation-independent** — implementations may vary in technology, but MUST conform to the normative specification under `spec/`.

Domain- or implementation-specific materials (for example, concrete deployments, application profiles, or integrations with particular blockchains or systems) MUST live outside the core specification and MUST NOT redefine Axis Protocol behavior.

---

## Authority

Axis Protocol behavior is normatively defined only by:

1. The specification documents located under `spec/`, and
2. Any explicitly normative registries that those specification documents reference.

Supporting documents in `docs/` exist to complement and explain the specification. They **MUST NOT** override or contradict the normative specification.

In case of any conflict between documentation under `docs/` and the specification under `spec/`, the specification under `spec/` SHALL prevail.
