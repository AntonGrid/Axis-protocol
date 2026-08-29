# Axis Protocol – Documentation

This directory contains **documentation and guides** that complement the normative specifications in `spec/`.

> **Axis Protocol is an overlay trust standard.**  
> It defines how physical devices and digital systems establish, exchange, and verify trust without relying on any specific blockchain, platform, or vendor.

---

## 1. What is Axis Protocol?

Axis Protocol is the **language of trust** between the physical and digital worlds.

It defines:

- How a physical device obtains a **cryptographic identity**.
- How that identity is **registered** in a verifiable registry.
- How the device **proves** that an event occurred.
- How that proof is **verified** by independent parties.
- How trust is **transferred** from the physical world to the digital world — and back.

Axis Protocol does **not** define:

- How to store data (blockchain, database, or otherwise).
- How to execute transactions (smart contracts, off-chain services, or otherwise).
- How to tokenize assets (energy, carbon, or otherwise).

These are **implementation details** and **application logic** — they belong in implementations (like Axis Core) and applications, not in the protocol itself.

---

## 2. Documentation Map

Typical entry points:

1. **Core Protocol**
   - [`../spec/protocol/README.md`](../spec/protocol/README.md) — overview of the core specification.
   - [`../spec/protocol/model.md`](../spec/protocol/model.md) — trust model and entities.
   - [`../spec/protocol/wire-format.md`](../spec/protocol/wire-format.md) — wire format and serialization.
   - [`../spec/protocol/validation.md`](../spec/protocol/validation.md) — validation rules.
   - [`../spec/protocol/lifecycle.md`](../spec/protocol/lifecycle.md) — lifecycle of trust entities.

2. **Architecture Decisions**
   - [`../adr/`](../adr/) — Architecture Decision Records (ADRs).

3. **Concepts and Guides (this directory)**
   - [`ECOSYSTEM.md`](./ECOSYSTEM.md) — one map of the whole ecosystem (standard → core → domain → intelligence → interfaces).
   - [`CONSTITUTION.md`](./CONSTITUTION.md) — the canonical constitution: T-1..T-5, C-1..C-7, L-1..L-8.
   - [`GLOSSARY.md`](./GLOSSARY.md) — unified terminology across all repositories.
   - [`WHITEPAPER.md`](./WHITEPAPER.md) — "Sovereign Intelligence for the Physical World" (v1).
   - [`profiles/LOGISTICS.md`](./profiles/LOGISTICS.md) — second domain demo (cold-chain logistics), proving domain-agnosticism.
   - [`Axis-Protocol-One-Pager.md`](./Axis-Protocol-One-Pager.md) — high‑level overview.
   - [`Axis-Protocol-Overview.md`](./Axis-Protocol-Overview.md) — detailed overview.
   - [`Axis-Protocol-Specification.md`](./Axis-Protocol-Specification.md) — full specification.
   - [`Axis-Protocol-Terminology.md`](./Axis-Protocol-Terminology.md) — core terminology.
   - [`Axis-Governance-and-ADR.md`](./Axis-Governance-and-ADR.md) — governance and ADR process.
   - [`merkle-proof-verification.md`](./merkle-proof-verification.md) — Merkle proof verification.

---

## 3. Who This Documentation Is For

This documentation is organized for three main audiences:

1. **Protocol and Domain Designers**
   - Define domains (`domain`, `entity_type`) and message schemas.
   - Specify validation and lifecycle rules.
   - Extend the protocol with new concepts if necessary (via ADRs).

2. **Implementers**
   - Build or extend runtimes that support Axis Protocol.
   - Implement serialization, validation, and execution.
   - Integrate Axis Protocol with transports, storage, and authorization.

3. **Application Developers / Integrators**
   - Use existing implementations (e.g., Axis Core) to build products.
   - Model devices, services, and workflows using Axis messages.
   - Integrate Axis with existing infrastructures and protocols.

---

## 4. Core Concepts (Informal Overview)

The normative definitions are in `spec/`, but the following high‑level concepts help orient yourself:

- **Trust Envelope** — a consistent wrapper around all Axis messages.
- **Domains and Entities** — logical grouping of messages and state.
- **Message Types** — commands, events, queries, responses, notifications, errors.
- **Validation Layers** — structural, cryptographic, semantic, state‑dependent.
- **Lifecycles** — how trust entities are born, live, and die.

---

## 5. Domain Modeling with Axis Protocol

Axis Protocol is **domain‑agnostic**. Each domain provides its own models on top of the protocol.

A typical domain modeling process:

1. **Identify domains and entity types**
   - Example: domain `energy.metering` with entity types `Meter`, `ReadingSession`, `Tariff`.

2. **Define message schemas**
   - For each entity type and operation:
     - creation commands/events,
     - configuration changes,
     - operational events,
     - queries and responses.

3. **Specify validation rules**
   - Field constraints and formats.
   - Allowed ranges, enumerations, units.
   - Cross‑field constraints.

4. **Define lifecycles**
   - What phases an entity can be in.
   - Which messages are allowed in each phase.
   - How transitions occur.

5. **Document error and conflict behavior**
   - When messages are rejected.
   - How conflicts or duplicates are handled.

Domain documentation can live:

- inside this repository (if it is part of the generic Axis ecosystem), or
- in separate repositories that import this protocol as a dependency.

---

## 6. Relationship to Implementations

Axis Protocol does **not** prescribe a specific runtime, language, or infrastructure.

Common implementation patterns:

- **Library / SDK**
  - Provides data structures for envelopes and payloads.
  - Implements serialization/deserialization.
  - Enforces structural and semantic validation rules.

- **Runtime / Service**
  - Accepts Axis messages over one or more transports.
  - Applies state‑dependent validation and business logic.
  - Emits Axis messages as events, responses, or notifications.

- **Gateway / Adapter**
  - Translates between Axis Protocol and other protocols.
  - Acts as a bridge between devices and backends.

Reference implementations (such as Axis Core) are intended as **examples and starting points**, not as protocol definitions.

---

## 7. Extending Axis Protocol

Axis Protocol is designed to evolve:

- New **message types** may be added using reserved extension ranges.
- New **domains** and **entity types** can be defined without affecting existing ones.
- New documents and ADRs can refine or extend behavior.

When proposing protocol‑level changes:

1. Start by reading existing ADRs in `../adr/`.
2. Draft a new ADR describing:
   - the problem and context,
   - the proposed change,
   - compatibility considerations,
   - alternatives and trade‑offs.
3. Update or add specification documents in `spec/` as needed.

---

## 8. How to Contribute

Guidelines:

1. Documentation in `spec/` is **normative** – change carefully and with ADRs where appropriate.
2. Documentation in `docs/` is **informative** – can be more narrative, with examples and recommendations.
3. Avoid tying generic docs to a single specific implementation or technology stack.

Open an issue or submit a pull request for improvements.
