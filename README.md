# Axis Protocol

**Axis Protocol** is an open, implementation-independent standard for establishing cryptographically verifiable trust between physical infrastructure and distributed digital systems.

It defines a **unified trust layer** that can be implemented on top of different persistence and settlement systems (blockchains, ledgers, or conventional databases), while keeping:

- A consistent **data model** for claims, assets, and attestations
- A canonical **wire format** for signed envelopes
- A shared **validation pipeline** and semantics
- A standard **lifecycle** for key protocol entities

The protocol is **domain-agnostic** — it does not assume any specific application domain (energy, supply chains, finance, etc.) and is **infrastructure-agnostic** — it does not depend on any specific blockchain or runtime environment.

---

## Repository Structure

This repository contains the **specification** of the Axis Protocol:

- `spec/` — core, normative protocol specification
  - `spec/overview.md` — high-level overview
  - `spec/protocol/` — detailed protocol specification (model, wire format, validation, lifecycle)
- `docs/` — supporting documentation, architecture overviews, ADRs, and explanatory materials
- `adr/` — Architecture Decision Records documenting key design choices

The reference implementation of the Axis protocol lives in a separate repository:

👉 [Axis-core](https://github.com/AntonGrid/Axis-core)

Domain-specific applications built on top of Axis Protocol (such as energy tokenization) live in their own repositories:

👉 [ENRG](https://github.com/AntonGrid/ENRG)

---

## Getting Started

To understand the protocol, start with:

1. [`spec/overview.md`](spec/overview.md) — high-level introduction
2. [`spec/protocol/README.md`](spec/protocol/README.md) — core specification index
3. [`adr/`](adr/) — architecture decision records explaining key choices

For implementation details, see the [Axis-core](https://github.com/AntonGrid/Axis-core) repository.

---

## Governance

The Axis Protocol is governed by the community through a hybrid governance model documented in [ADR-0009](adr/ADR-0009-Governance-Protocol.md).

---

## Contributing

Contributions are welcome! Please see:
- [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- [SECURITY.md](SECURITY.md) for security reporting

---

## License

[MIT](LICENSE)
