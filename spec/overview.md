# Axis Protocol – Specification Overview

Axis Protocol defines common rules for trust, verification and interaction
between participants in any domain (energy, logistics, finance, etc.),
independent of any particular blockchain or infrastructure.

This repository contains the **canonical specification** of the Axis protocol.
It is organized into several sections:

- **`spec/protocol/` – Core protocol**  
  The normative definition of the protocol: object model, message formats,
  validation rules and lifecycle of protocol objects.

- **`spec/registry/` – Registries and identifiers**  
  Global registries of types, identifiers and capabilities used by the
  protocol and its extensions.

- **`spec/api/` – Public APIs**  
  HTTP / RPC / other APIs that expose Axis functionality to applications
  and integrations.

- **`spec/architecture/` – Architectural constraints**  
  High‑level architectural invariants that all compliant implementations
  must respect.

- **`spec/platform/` – Platform-specific notes**  
  Platform bindings (e.g. EVM, other ledgers) and the way they map the
  generic protocol to concrete execution environments.

- **`spec/rfc/` – Extensions and proposals**  
  RFC‑style documents that introduce new features or changes to the core
  protocol before they become part of a stable release.

For a detailed introduction to the ideas behind Axis, see `docs/overview.md`
and `docs/Axis-One-Pager.md`.

For implementers, the best starting point is `spec/protocol/README.md`.
