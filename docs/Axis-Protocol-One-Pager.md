# Axis Protocol – One Pager

## What is Axis?

Axis Protocol is a domain-agnostic trust and attestation framework that connects physical devices and digital systems.

Axis defines:

- how devices and actors are identified,
- how claims about them are issued and verified on-chain,
- how registries of manifests, capabilities, events, and errors are maintained,
- how governance and policy are enforced across domains.

Any vertical — energy, mobility, IoT, supply chain, or others — can implement a **Domain Profile** on top of Axis Core.

---

## Core Building Blocks

- **Identity & Actors**
  - Model for devices, organizations, and services.
  - Links between off-chain identifiers and on-chain accounts.

- **On-chain Attestation**
  - Standard format for claims about devices and events.
  - Contracts/programs to issue, verify, and revoke attestations.

- **Registries**
  - **Manifest Registry** – what this device/actor is.
  - **Capability Registry** – what this device/actor can do.
  - **Event Registry** – what happened and when.
  - **Error Registry** – standardized failure and error codes.

- **Policy & Governance**
  - Rules for who can issue which attestations.
  - Upgrade and change management via ADR/RFC process.
  - Conformance requirements for implementations and domains.

---

## Axis Core vs Domain Profiles

- **Axis Core**
  - Domain-agnostic specifications and reference implementation.
  - Defines common terminology, schemas, and governance.
  - Owns the ADR/RFC process for protocol-level changes.

- **Domain Profiles**
  - Extend Axis with domain-specific registries and flows.
  - Reuse Axis Core primitives for identity and attestation.
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
