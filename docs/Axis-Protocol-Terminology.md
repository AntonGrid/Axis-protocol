# Axis Protocol — Terminology

This document defines core terminology used in the Axis Protocol.  
It is **normative** for Axis Core and **referential** for Domain Profiles.

---

## 1. Axis Core

**Axis Core** is the domain-agnostic part of the Axis Protocol. It defines:

- common concepts, terminology, and schemas,
- on-chain and off-chain components for identity and attestation,
- registries (manifest, capability, event, error),
- governance (ADR/RFC process) and conformance requirements.

All Domain Profiles MUST be compatible with Axis Core.

---

## 2. Domain Profile

A **Domain Profile** is a specialization of Axis Core for a specific vertical (e.g. energy, mobility, IoT, supply chain).

Characteristics:

- Defines domain-specific registries, events, and flows.
- Reuses Axis Core primitives for identity, attestation, and governance.
- MUST NOT redefine or conflict with Axis Core terminology.
- MUST document its own conformance rules on top of Axis Core.

Examples:
- **Energy Domain Profile** – for energy generation and metering.
- **Mobility Domain Profile** – for vehicle tracking and fleet management.
- **Supply Chain Profile** – for product traceability and provenance.

---

## 3. Actor

An **Actor** is any identifiable participant interacting with Axis:

- physical devices (sensors, meters, controllers),
- organizations (manufacturers, operators, auditors),
- services (oracles, applications, contracts).

Each Actor has:

- one or more **off-chain identifiers** (e.g. serial number, certificate subject, legal entity ID),
- one or more **on-chain accounts** (e.g. public keys, program IDs),
- a **Manifest** describing its identity and properties.

---

## 4. Attestation

An **Attestation** is a signed statement by an Actor about a claim, asset, or event.

It includes:

- **Claim** — a structured statement about the world (e.g., "device X produced 1 kWh").
- **Evidence** — data that supports the claim.
- **Signature** — cryptographic proof of the Actor's identity.

Attestations are verified on-chain or off-chain using Axis Core primitives.

---

## 5. Registry

A **Registry** is a structured repository of protocol information.

Types of registries:

- **Manifest Registry** — stores Actor manifests and their properties.
- **Capability Registry** — defines what Actors can do (e.g., "can produce energy").
- **Event Registry** — logs events and their timestamps.
- **Error Registry** — standardizes error codes and failure conditions.

All registries MUST follow Axis Core schemas and governance rules.

---

## 6. Policy & Governance

**Policy** defines rules for:

- who can issue which attestations,
- how claims are validated,
- how conflicts are resolved.

**Governance** defines:

- how the protocol evolves (ADR/RFC process),
- who decides on changes (community, token holders, guardians),
- how registries are updated and maintained.

---

## 7. Reference Implementation

A **Reference Implementation** is a concrete implementation of Axis Core (e.g., Axis-core repository). It:

- demonstrates how the protocol works,
- provides libraries, SDKs, and tools,
- serves as a baseline for Domain Profiles.

Domain Profiles MAY build on or extend the Reference Implementation.

---

## Normative vs. Informative

- **Normative** — must be followed for conformance.
- **Informative** — explanatory, non-binding.

Axis Core is normative for all Domain Profiles. Domain Profiles MAY define additional normative rules, but they MUST NOT conflict with Axis Core.
