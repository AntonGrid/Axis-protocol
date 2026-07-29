# Axis Protocol — Core Specification

This directory contains the **core specification** of Axis Protocol — an **overlay trust standard** that defines how physical devices and digital systems establish, exchange, and verify trust without relying on any specific blockchain, platform, or vendor.

It is **not a blockchain protocol**.  
It is **not an application**.  
It is **not tied to energy, IoT, or any specific domain**.

Axis Protocol is the **language of trust** between the physical and digital worlds.

---

## Scope

The core specification defines:

- **Identity** — how devices obtain cryptographic identities.
- **Registry** — how identities and states are recorded and verified.
- **Proof** — how devices prove that events occurred.
- **Verification** — how proofs are validated by independent parties.
- **Trust Transfer** — how trust moves from the physical world to the digital world — and back.

All other concerns — storage, execution, tokenization, domain-specific logic — are outside the scope of this specification.

---

## What This Specification Does Not Define

- **Storage** — no blockchain, database, or persistence model is assumed.
- **Execution** — no smart contracts, off-chain services, or transaction models are assumed.
- **Domain Logic** — no energy, supply chain, identity, or other vertical logic is defined.
- **Implementation** — no reference code, SDKs, or deployment models are specified.

These belong in implementations (like Axis Core) and applications (like domain-specific profiles).

---

## Core Documents

| Document | Description |
| :--- | :--- |
| [`model.md`](./model.md) | Core data model: entities, relationships, and trust graph. |
| [`wire-format.md`](./wire-format.md) | Canonical message format and serialization rules. |
| [`validation.md`](./validation.md) | Validation pipeline, rules, and policy model. |
| [`lifecycle.md`](./lifecycle.md) | Lifecycle of entities, events, and trust relationships. |

---

## Design Principles

1. **Trust Over Technology**
   - Trust is the primary concern. Technology is a means to achieve it.

2. **Identity is Cryptographic**
   - Every device has its own identity. Private keys never leave the device.

3. **Proof is Verifiable**
   - Every event is cryptographically proven. Verification does not depend on a trusted third party.

4. **Registry is Canonical**
   - Device identity, state, and history are maintained in a verifiable registry.

5. **Protocol is Neutral**
   - No dependency on any blockchain, platform, vendor, or domain.

---

## Relationship to Other Repositories

- **Axis Protocol** (this repository) — the **normative specification** of the trust standard.
- **Axis Core** — a **platform-agnostic reference implementation** of the protocol.
- **Domain Applications** — specific applications built on the protocol (e.g., energy tokenization, supply chain tracking, etc.).

---

## Versioning

This directory describes **Axis Protocol v0.x (draft)**.

- Breaking changes are tracked in a changelog and/or ADRs.
- Implementations MUST declare:
  - the **Axis protocol version** they support;
  - any **extensions** or **profiles** they rely on.

> Implementation‑specific ADRs and architecture documents MUST live outside this directory (e.g., in `docs/` or in implementation repositories).
