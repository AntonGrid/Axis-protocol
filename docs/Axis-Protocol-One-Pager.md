# Axis Protocol – One Pager

## What is Axis?

Axis Protocol is an **overlay trust standard** — a domain-agnostic language of trust between physical devices and digital systems.

It defines:

- how physical devices obtain cryptographic identity,
- how that identity is registered and verified,
- how devices prove that real-world events occurred,
- how those proofs are verified by independent parties,
- how trust is transferred from the physical world to the digital world — and back.

Axis Protocol does **not** define:

- how to store data (blockchain, database, or otherwise),
- how to execute transactions (smart contracts, off-chain services, or otherwise),
- how to tokenize assets (energy, carbon, or otherwise).

These are **implementation details** and **application logic**.

---

## Core Building Blocks

- **Identity & Actors**
  - Cryptographic identity for devices, organizations, and services.
  - Links between physical devices and digital identifiers.

- **Proof & Attestation**
  - **Proof** — cryptographic evidence that a physical event occurred.
  - **Attestation** — signed verification of a Proof by a trusted entity.

- **Registries**
  - **Device Registry** — source of truth for device identity and state.
  - **Manifest Registry** — what a device is and what it can do.
  - **Capability Registry** — what a device or actor is capable of.
  - **Event Registry** — what happened and when.
  - **Error Registry** — standardized error codes.

- **Policy & Governance**
  - Rules for who can issue which attestations.
  - ADR/RFC process for protocol evolution.
  - Conformance requirements for implementations.

---

## Trust Pipeline

Axis Protocol defines a standardized pipeline for trust:
Physical Device → Event → Proof → Attestation → Digital Trust

text

Each link in the chain is cryptographically verifiable.  
No trusted third party is required.

---

## Axis Core vs Domain Profiles

- **Axis Core**
  - Domain-agnostic reference implementation of the protocol.
  - Provides common terminology, schemas, and governance.
  - Owns the ADR/RFC process for protocol-level changes.

- **Domain Profiles**
  - Domain-specific extensions (energy, supply chain, identity, etc.).
  - Reuse Axis Core primitives for identity, proof, and attestation.
  - Must comply with Axis Core conformance and governance.

---

## Getting Started

1. Read the [Core Specification](../spec/protocol/README.md)
2. Review the [Architecture Decision Records](../adr/)
3. Explore the [Reference Implementation](https://github.com/AntonGrid/Axis-core)
4. Build your own Domain Profile

---

## Governance

The protocol is governed by the community through a hybrid governance model documented in [ADR-0009](../adr/ADR-0009-Governance-Protocol.md).
