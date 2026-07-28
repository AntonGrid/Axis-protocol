# Axis Protocol – Documentation

This directory contains **documentation and guides** that complement the normative specifications in `spec/`.

- `spec/` – defines what Axis Protocol *is* (normative).
- `docs/` – explains how to **understand, use and extend** Axis Protocol in real systems (informative).

If you are new to Axis Protocol, this document is your starting point.

---

## 1. Documentation map

Typical entry points:

1. **Core protocol**
   - [`../spec/protocol/wire-format.md`](../spec/protocol/wire-format.md)  
     Wire format, envelope structure, primitive types.
   - [`../spec/protocol/validation.md`](../spec/protocol/validation.md)  
     Validation layers and protocol‑level invariants.
   - [`../spec/protocol/lifecycle.md`](../spec/protocol/lifecycle.md)  
     Entity and message lifecycle patterns.

2. **Architecture decisions**
   - [`../spec/adr/`](../spec/adr/)  
     Architecture Decision Records (ADRs) documenting key protocol design choices.

3. **Concepts and guides (this directory)**
   - Conceptual overviews.
   - Domain modeling guides.
   - Implementation and integration notes.
   - Examples and patterns.

The exact set of documents in `docs/` may evolve over time; check this README for links and structure.

---

## 2. Who this documentation is for

This documentation is organized for three main audiences:

1. **Protocol and domain designers**
   - Define domains (`domain`, `entity_type`) and message schemas.
   - Specify validation and lifecycle rules.
   - Extend the protocol with new concepts if necessary (via ADRs).

2. **Implementers**
   - Build or extend runtimes that support Axis Protocol.
   - Implement serialization, validation and execution.
   - Integrate Axis Protocol with transports, storage and authorization.

3. **Application developers / integrators**
   - Use existing implementations (e.g. Axis Core or others) to build products.
   - Model devices, services and workflows using Axis messages.
   - Integrate Axis with existing infrastructures and protocols.

---

## 3. Core concepts (informal overview)

The normative definitions are in `spec/`, but the following high‑level concepts help orient yourself:

- **Message envelope**  
  A consistent wrapper around all Axis messages: contains type, versioning, entity references, correlation information and payload.

- **Domains and entities**
  - A **domain** groups related entity types and message schemas (e.g. “energy.metering”).
  - An **entity** is a logical object identified by `domain`, `entity_type`, `entity_id`.

- **Message types**
  - Commands, events, queries, responses, notifications, errors, and possible extensions.
  - Each combination of domain, entity_type, message_type and message_version defines a concrete schema.

- **Validation layers**
  - Structural (wire‑level correctness).
  - Semantic (message makes sense according to its schema).
  - State‑dependent (message is valid in current system state, authorized, etc.).

- **Lifecycles**
  - Typical entity phases: Non‑existent → Initializing → Active → Suspended → Terminated.
  - Domains refine these phases and define allowed transitions.

For details, always refer back to the protocol specifications in `spec/protocol/`.

---

## 4. Domain modeling with Axis Protocol

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
   - How transitions occur (e.g. which command/event causes which transition).

5. **Document error and conflict behavior**
   - When messages are rejected.
   - How conflicts or duplicates are handled.

Domain documentation can live:

- inside this repository (if it is part of the generic Axis ecosystem), or
- in separate repositories that import this protocol as a dependency.

---

## 5. Implementations and runtimes

Axis Protocol does **not** prescribe a specific runtime, language or infrastructure.

Common implementation patterns:

- **Library / SDK**
  - Provides data structures for envelopes and payloads.
  - Implements serialization/deserialization to/from Axis wire format.
  - Enforces structural and semantic validation rules.

- **Runtime / service**
  - Accepts Axis messages over one or more transports (HTTP, message bus, ledger, etc.).
  - Applies state‑dependent validation and business logic.
  - Emits Axis messages as events, responses or notifications.

- **Gateway / adapter**
  - Translates between Axis Protocol and other protocols (fieldbuses, legacy systems, proprietary APIs).
  - Acts as a bridge between devices and backends.

Reference implementations (such as Axis Core) are intended as **examples and starting points**, not as protocol definitions.  
They MUST remain compatible with the normative specs in `spec/`.

---

## 6. Transport and storage

Axis Protocol is **transport‑agnostic**:

- Messages can be carried over:
  - TCP/UDP connections,
  - message queues or pub/sub systems,
  - event logs or ledgers,
  - request/response APIs,
  - or any other reliable or best‑effort channels.

- Messages can be stored as:
  - append‑only logs,
  - event streams per entity,
  - snapshots + change logs,
  - or other representations.

Each deployment SHOULD document:

- How Axis messages are framed on the chosen transport.
- How ordering (if any) is guaranteed or approximated.
- How long messages are retained and how state is reconstructed if needed.

The wire‑format spec (`spec/protocol/wire-format.md`) provides guidelines for framing and length‑prefixing.

---

## 7. Extending Axis Protocol

Axis Protocol is designed to evolve:

- New **message types** may be added using reserved extension ranges.
- New **domains** and **entity types** can be defined without affecting existing ones.
- New documents and ADRs can refine or extend behavior.

When proposing protocol‑level changes:

1. Start by reading existing ADRs in `spec/adr/`.
2. Draft a new ADR describing:
   - the problem and context,
   - the proposed change,
   - compatibility considerations,
   - alternatives and trade‑offs.
3. Update or add specification documents in `spec/` as needed.

The goal is to keep Axis Protocol coherent, minimal and implementation‑neutral while still being practical for real‑world use.

---

## 8. How to navigate and contribute to docs/

If you want to improve or extend the documentation:

- **Clarify** existing documents:
  - Fix ambiguities, improve explanations, add diagrams or examples.
- **Add guides**:
  - Domain modeling recipes,
  - implementation checklists,
  - migration or integration guides.
- **Keep specs and docs aligned**:
  - When specs change, ensure `docs/` is updated to reflect the new behavior.

Guidelines:

1. Documentation in `spec/` is **normative** – change carefully and with ADRs where appropriate.
2. Documentation in `docs/` is **informative** – can be more narrative, with examples and recommendations.
3. Avoid tying generic docs to a single specific implementation or technology stack; keep implementation‑specific details in separate, clearly labeled sections or repos.

---

## 9. Feedback and questions

If you have questions or suggestions about Axis Protocol documentation:

- Open an issue in the repository.
- Propose changes via pull requests.
- Reference specific sections of `spec/` or `docs/` when discussing behavior or ambiguities.

Clear documentation is part of the protocol’s contract; improvements here benefit all implementations and domains built on Axis.
