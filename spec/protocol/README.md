# Axis Protocol — Core Specification

This directory contains the **core, blockchain-agnostic specification** of the Axis protocol.

- It MUST stay independent from any particular chain, runtime or implementation.
- It defines the *conceptual model*, *wire format*, *validation rules* and *lifecycle semantics*.
- All chain‑ or product‑specific details (Solana, ENRG, etc.) belong in separate documents/repositories.

## Scope

Axis is a protocol for representing and exchanging **stateful claims** about real‑world or digital assets in a verifiable way.

The core spec covers:

- **Conceptual model**:
  - actors and identities;
  - assets and claims;
  - records, events and logs;
  - namespaces and versioning.
- **Wire format**:
  - canonical serialization of records;
  - hashing and content addressing;
  - references and linking.
- **Validation**:
  - structural validation;
  - semantic validation (policies, constraints);
  - versioning and compatibility rules.
- **Lifecycle**:
  - creation and evolution of claims;
  - revocation, supersession, expiration;
  - conflict resolution and merging.

Out of scope for this directory:

- smart‑contract layouts on any chain;
- gas/fees, transaction formats, RPC details;
- ENRG‑specific business logic, market rules or pricing.

## Structure

- [`model.md`](./model.md) — core conceptual model (actors, assets, claims, records).
- [`wire-format.md`](./wire-format.md) — canonical on‑wire representation.
- [`validation.md`](./validation.md) — validation rules and policy model.
- [`lifecycle.md`](./lifecycle.md) — lifecycle and state transitions.

Future additions (optional, not yet finalised):

- `security.md` — security, threat model and trust assumptions.
- `glossary.md` — glossary of core terms.
- `examples/` — cross‑chain examples and test vectors.

## Design principles

The Axis protocol is designed with the following principles:

1. **Chain‑agnostic**  
   The protocol must be implementable on multiple chains, off‑chain systems or hybrid setups.

2. **Deterministic & canonical**  
   The same logical record must have a unique canonical representation and hash across implementations.

3. **Minimal core, extensible edges**  
   The core spec should define a *small, stable* set of primitives that can be safely extended by domains (like ENRG).

4. **Separation of concerns**  
   - Protocol spec: what a valid Axis record is and how it behaves.
   - Implementations: how records are stored, executed or transacted.

5. **Human‑readable, machine‑checkable**  
   The spec should be readable by humans and strict enough to derive reference tests and validators.

## Versioning

This directory describes **Axis Protocol v0.x (draft)**.

- Breaking changes are tracked in a changelog and/or ADRs.
- Implementations MUST declare:
  - the **Axis protocol version** they support;
  - any **extensions** or **profiles** they rely on.

> Implementation‑specific ADRs and architecture documents MUST live outside this directory (e.g. in `docs/` or in implementation repos such as Axis‑core).
