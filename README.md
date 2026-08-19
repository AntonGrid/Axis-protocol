# Axis Protocol

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Spec](https://img.shields.io/badge/spec-v1.0-blue.svg)

Axis Protocol is an **overlay trust standard** — a domain-agnostic language of trust between physical devices and digital systems.

It defines how devices and digital systems establish, exchange, and verify trust without relying on any specific blockchain, platform, or vendor.

This repository contains the **core specifications** of Axis Protocol (trust model, wire format, validation rules, lifecycles, and related documents).

---

## Philosophy

The foundational philosophy of the Axis Protocol is captured in the **Architecture Book**:

- [Prologue](docs/philosophy/architecture/00_Prologue.md) — Introduction to the vision
- [Chapter 1](docs/philosophy/architecture/01_The_Birth_of_an_Idea.md) — How it all began
- [Chapter 2](docs/philosophy/architecture/02_When_a_Token_Was_No_Longer_Enough.md) — Moving beyond tokens
- [Chapter 3](docs/philosophy/architecture/03_When_the_Protocol_Became_More_Important_than_the_Project.md) — Protocol over project
- [Chapter 4](docs/philosophy/architecture/04_Architecture_Is_Born_Before_the_Code.md) — Architecture first
- [Chapter 5](docs/philosophy/architecture/05_The_First_Law_of_Trust.md) — The first law of trust
- [Epilogue](docs/philosophy/architecture/06_Epilogue.md) — Where the journey leads

---

## Repository structure

```text
Axis-protocol/
  spec/
    overview.md            # High-level overview of the protocol
    protocol/
      README.md            # Core specification index
      model.md             # Trust model and entities
      wire-format.md       # Wire format and serialization
      validation.md        # Validation rules
      lifecycle.md         # Lifecycle of trust entities
  docs/
    README.md              # Documentation index
    Axis-Protocol-*.md     # One-Pager, Overview, Specification, Terminology
    philosophy/            # Architecture Book (6 chapters + Epilogue)
    platform/              # Device lifecycle, provisioning
  adr/                     # Architecture Decision Records (9 ADRs)
  LICENSE                  # Apache 2.0
  NOTICE                   # Attribution
  README.md                # This file
```

The `spec/` directory is the **normative** source for the protocol definition.
Everything else (`docs/`, `adr/`, examples) is informative or illustrative.

---

## Axis Protocol vs Implementations

Axis Protocol clearly separates:

- **Protocol layer** (this repository) — what a conforming message is and what invariants hold.
- **Implementation layer** (separate repositories) — how messages are produced, transported, stored, and executed in specific environments.

Examples of implementation roles (non-exclusive, non-normative):

- **Axis Core** — a reference implementation that provides serialization/deserialization libraries, enforces validation rules, and integrates with specific transports or ledgers.
- **Other runtimes** — independent implementations in different languages or platforms that consume and produce Axis-conformant messages.

Implementations SHOULD treat the specifications in `spec/` as normative and document any additional constraints they introduce.

---

## Reference Implementations

- [**Axis Core**](https://github.com/AntonGrid/Axis-core) — the universal reference implementation of the protocol (schemas, validation, oracle with Ed25519 verification).
- [**ENRG**](https://github.com/AntonGrid/ENRG) — an example of a domain profile (energy) built on top of the protocol.

---

## Getting Started

There are two main ways to work with Axis Protocol:

- **As a protocol author / domain designer** — define domain-specific schemas and rules on top of Axis.
- **As an implementer** — implement serialization, validation, and execution for Axis messages in a particular runtime.

### 1. Read the core specifications

Start with the protocol documents:

- [spec/protocol/README.md](spec/protocol/README.md) — overview of the core specification.
- [spec/protocol/model.md](spec/protocol/model.md) — trust model and entities.
- [spec/protocol/wire-format.md](spec/protocol/wire-format.md) — wire format and serialization.
- [spec/protocol/validation.md](spec/protocol/validation.md) — validation rules.
- [spec/protocol/lifecycle.md](spec/protocol/lifecycle.md) — lifecycle of trust entities.

### 2. Explore architecture decisions

Axis Protocol uses Architecture Decision Records (ADRs) to capture key design choices and their rationale.

- See [adr/](adr/) — a set of ADRs describing the evolution of the protocol.

### 3. Check additional documentation

- See [docs/README.md](docs/README.md) for an index and entry points.

---

## Using Axis Protocol in Your Project

Axis Protocol is designed to be embedded into a wide range of systems. Typical usage patterns:

- **Device / edge integration** — devices emit Axis-formatted events and respond to Axis-formatted commands. Gateways or cloud services validate and process these messages.
- **Backend / service integration** — microservices communicate via a message bus using Axis messages as a shared contract. Validation and lifecycle rules ensure consistent behavior across services.
- **Ledger / log integration** — systems append Axis messages to an append-only log, event store, or ledger. Consumers rebuild state by replaying validated messages.

To adopt Axis Protocol, you typically:

1. Define your domains, entity types, and message schemas on top of the core spec.
2. Choose or build an implementation (e.g., use Axis Core or another runtime).
3. Integrate Axis validation and serialization into your device, service, or application code.

---

## Conformance and Compatibility

An implementation claims conformance to Axis Protocol if it:

- correctly implements the wire format as specified in [spec/protocol/wire-format.md](spec/protocol/wire-format.md);
- enforces at least the structural and cryptographic validation rules in [spec/protocol/validation.md](spec/protocol/validation.md);
- applies semantic and state-dependent validation consistently according to its domain specifications;
- maintains deterministic behavior: given the same inputs and configuration, different implementations reach equivalent decisions and outcomes.

Profiles or deployments MAY introduce stricter rules but MUST NOT contradict the core specifications.

---

## Roadmap and Evolution

Axis Protocol is expected to evolve over time. Changes are governed by:

- updates to the core specifications in `spec/`;
- new or updated ADRs in `adr/`;
- versioning of:
  - the envelope format (`envelope_version`),
  - individual message schemas (`message_version`),
  - and optionally domain-specific profiles.

Backward-compatible changes are preferred. Breaking changes are introduced only with clear versioning and migration guidance.

---

## Contributing

Contributions to the Axis Protocol specifications are welcome.

Typical contribution types:

- Clarifications or improvements to existing documents.
- New ADRs proposing protocol-level changes.
- Corrections to inconsistencies or ambiguities.
- Additional examples or explanatory docs in `docs/`.

Please read:

- [CONTRIBUTING.md](CONTRIBUTING.md) — guidelines for PRs and the ADR process.
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — community standards.

---

## Security

Security issues should be reported privately — see [SECURITY.md](SECURITY.md).

---

## License

Unless otherwise noted, the contents of this repository are licensed under the terms specified in [LICENSE](LICENSE).

Implementations and downstream projects built on Axis Protocol may use different licenses, as long as they respect the terms of this repository.
