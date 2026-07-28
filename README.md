# Axis Protocol

Axis Protocol is a **specification for structured, deterministic messaging** between devices, services and domains.  
It defines how to represent commands, events and queries in a way that is:

- **Implementation‑neutral** – not tied to any specific blockchain, database, runtime or smart‑contract framework.
- **Deterministic** – the same logical message yields the same serialized form and the same validation outcome.
- **Domain‑agnostic** – applicable to energy, IoT, supply‑chain, finance and other domains.
- **Extensible** – designed to evolve without breaking existing deployments.

This repository contains the **core specifications** of Axis Protocol (wire format, validation rules, lifecycles and related documents).

Concrete runtimes (such as **Axis Core** or others) can implement these specifications and add domain‑specific behavior.

---

## Repository structure

High‑level structure:

```text
Axis-protocol/
  spec/
    protocol/
      wire-format.md       # Wire-level message envelope and primitive types
      validation.md        # Validation model and protocol-level invariants
      lifecycle.md         # Entity and message lifecycle patterns
    adr/                   # Architecture Decision Records related to the protocol
  docs/
    README.md              # Documentation index and usage guidance
    ...                    # Additional explanatory documents
  LICENSE
  README.md                # This file
The spec/ directory is the normative source for the protocol definition.
Everything else (docs, examples, reference implementations) is informative or illustrative.

Axis Protocol vs implementations
Axis Protocol aims to clearly separate:

Protocol layer (this repo) – what a conforming message is and what invariants hold.
Implementation layer (separate repos) – how messages are produced, transported, stored and executed in specific environments.
Examples of implementation roles (non‑exclusive, non‑normative):

Axis Core – a reference implementation that:

provides serialization/deserialization libraries,
enforces validation rules from this repository,
integrates with specific transports or ledgers (configurable per deployment).
Other runtimes – independent implementations in different languages or platforms that:

consume and produce Axis‑conformant messages,
embed the protocol in existing infrastructures (databases, message buses, blockchains, etc).
Implementations SHOULD treat the specifications in spec/ as normative and document any additional constraints they introduce.

Getting started
There are two main ways to work with Axis Protocol:

As a protocol author / domain designer
You define domain‑specific schemas and rules on top of Axis.

As an implementer
You implement serialization, validation and execution for Axis messages in a particular runtime.

1. Read the core specifications
Start with the protocol documents:

spec/protocol/wire-format.md
Structure of the on‑wire message envelope, primitive types and framing guidelines.

spec/protocol/validation.md
Validation layers (structural, semantic, state‑dependent) and protocol‑level invariants.

spec/protocol/lifecycle.md
Recommended patterns for entity and message lifecycles across domains.

These documents are implementation‑neutral and form the core of Axis Protocol.

2. Explore architecture decisions
Axis Protocol uses Architecture Decision Records (ADRs) to capture key design choices and their rationale.

See:

spec/adr/ – a set of ADRs describing the evolution of the protocol.
ADRs are informative but strongly recommended reading if you intend to extend the protocol or build new implementations.

3. Check additional documentation
The docs/ directory provides additional guidance, such as:

conceptual overviews of Axis Protocol,
examples of domain modeling on top of Axis,
implementation notes and integration guides.
See docs/README.md for an index and entry points.

Using Axis Protocol in your project
Axis Protocol is designed to be embedded into a wide range of systems. Typical usage patterns:

Device / edge integration

Devices emit Axis‑formatted events and respond to Axis‑formatted commands.
Gateways or cloud services validate and process these messages.
Backend / service integration

Microservices communicate via a message bus using Axis messages as a shared contract.
Validation and lifecycle rules ensure consistent behavior across services.
Ledger / log integration

Systems append Axis messages to an append‑only log, event store or ledger.
Consumers rebuild state by replaying validated messages.
To adopt Axis Protocol, you typically:

Define your domains, entity types and message schemas on top of the core spec.
Choose or build an implementation (e.g. use Axis Core or another runtime).
Integrate Axis validation and serialization into your device, service or application code.
Conformance and compatibility
An implementation claims conformance to Axis Protocol if it:

Correctly implements the wire format as specified in spec/protocol/wire-format.md.
Enforces at least the structural validation rules in spec/protocol/validation.md.
Applies semantic and state‑dependent validation consistently according to its domain specifications.
Maintains deterministic behavior: given the same inputs and configuration, different implementations reach equivalent decisions and outcomes.
Profiles or deployments MAY introduce stricter rules (e.g. tighter validation, specific transports, particular authorization models) but MUST NOT contradict the core specifications.

Roadmap and evolution
Axis Protocol is expected to evolve over time. Changes are governed by:

Updates to the core specifications in spec/.
New or updated ADRs in spec/adr/.
Versioning of:
the envelope format (envelope_version),
individual message schemas (message_version),
and optionally domain‑specific profiles.
Backward‑compatible changes are preferred. Breaking changes are introduced only with clear versioning and migration guidance.

Contributing
Contributions to the Axis Protocol specifications are welcome.

Typical contribution types:

Clarifications or improvements to existing documents.
New ADRs proposing protocol‑level changes.
Corrections to inconsistencies or ambiguities.
Additional examples or explanatory docs in docs/.
To propose a change:

Open an issue describing the problem or proposal.
If the change is substantial, consider drafting an ADR under spec/adr/.
Submit a pull request with the proposed edits.
Maintainers use ADRs and review discussions to ensure that the protocol remains coherent and implementation‑neutral.

License
Unless otherwise noted, the contents of this repository are licensed under the terms specified in LICENSE.

Implementations and downstream projects built on Axis Protocol may use different licenses, as long as they respect the terms of this repository.
