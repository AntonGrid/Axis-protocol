# Axis Protocol — Trust Model

This document defines the **trust model** of Axis Protocol. It describes how trust is established, represented, verified, and transferred between physical devices and digital systems.

The model is **implementation-agnostic** and **domain-neutral**. It does not assume any specific blockchain, storage layer, or runtime.

---

## Core Principles

1. **Trust is Cryptographic**  
   Every identity, event, and proof is rooted in cryptographic keys and signatures.

2. **Trust is Verifiable**  
   No third party is required to validate a proof. Verification is deterministic and self-contained.

3. **Trust is Transferable**  
   Trust moves from the physical world (device, event) to the digital world (attestation, registry) through a standardized pipeline.

4. **Trust is Neutral**  
   The model does not depend on any specific domain, platform, or implementation.

---

## The Trust Pipeline

Axis Protocol models trust as a pipeline from physical reality to digital verification:
Physical Device → Event → Proof → Attestation → Verification → Trust

text

Each stage is represented by specific entities.

---

## 1. Physical World

### 1.1 Device

A **Device** is a physical entity that produces events. It has:

- a **cryptographic identity** (private key + public key);
- a **stable identifier** (device ID);
- a **manifest** that defines its capabilities and configuration.

The private key **never leaves the device**. All proofs are signed on the device.

### 1.2 Event

An **Event** is a measurable occurrence produced by a Device. Examples:

- generation of 1 MWh of electricity;
- movement of a package through a checkpoint;
- completion of a manufacturing step.

Events are **not transmitted directly**. They are **proved** cryptographically.

---

## 2. Proof Layer

### 2.1 Proof

A **Proof** is a cryptographic statement that a specific Event occurred, produced by a Device.

A Proof contains:

- `device_id` — identifier of the device that produced it;
- `event_data` — structured description of the event;
- `timestamp` — when the event occurred;
- `nonce` — to prevent replay attacks;
- `signature` — cryptographic signature by the device's private key.

The Proof is the **atomic unit of trust** from the physical world.

### 2.2 Verification

A **Verifier** is any entity that checks a Proof:

- signature validity;
- nonce uniqueness;
- timestamp freshness;
- consistency with the device's manifest and registry state.

Verification is **deterministic** and does not require a trusted third party.

---

## 3. Attestation Layer

### 3.1 Attestation

An **Attestation** is a signed statement by a trusted entity (e.g., an Oracle) that a Proof has been verified and is valid.

An Attestation contains:

- `proof_id` — reference to the Proof being attested;
- `decision` — whether the Proof is valid or invalid;
- `oracle_id` — identifier of the attesting entity;
- `timestamp` — when the attestation was issued;
- `signature` — signature by the attesting entity.

The Attestation is the **bridge** from the physical world to the digital world.

### 3.2 Registry

A **Registry** is a verifiable store of device identities, states, and attestations.

The Registry is the **source of truth** for the protocol. It maintains:

- device identity and public keys;
- device lifecycle states;
- attestation history;
- policy definitions.

---

## 4. Digital Trust

### 4.1 Digital Claim

A **Digital Claim** is a statement in the digital world that is backed by an Attestation.

Examples:

- "Device X produced 1 MWh of electricity."
- "Device Y is currently in State Z."

Digital Claims are **cryptographically anchored** to physical events through the Proof → Attestation pipeline.

### 4.2 Trust Graph

Axis Protocol maintains a **Trust Graph** that connects:

- Devices → Proofs → Attestations → Digital Claims → Applications.

Any participant can verify any link in the graph independently.

---

## 5. Core Entities Summary

| Entity | Layer | Description |
| :--- | :--- | :--- |
| **Device** | Physical | A physical entity with cryptographic identity. |
| **Event** | Physical | A measurable occurrence. |
| **Proof** | Proof | Cryptographic evidence of an Event. |
| **Attestation** | Attestation | Signed verification of a Proof. |
| **Registry** | Attestation | Verifiable store of identities and states. |
| **Digital Claim** | Digital | Statement backed by Attestation. |
| **Policy** | Digital | Rules governing trust and verification. |

---

## 6. Trust Flow Example

1. **Device** generates an Event (e.g., produces 1 MWh).
2. **Device** signs a **Proof** containing the Event data.
3. **Proof** is submitted to a **Verifier**.
4. **Verifier** checks the Proof and issues an **Attestation**.
5. **Attestation** is stored in the **Registry**.
6. **Digital Claim** is derived from the Attestation.
7. **Application** uses the Digital Claim to trigger logic (e.g., mint a token, update a ledger, etc.).

All steps are cryptographically linked. Trust is preserved end-to-end.

---

## Relationship to Other Documents

- `wire-format.md` — defines how these entities are serialized on the wire.
- `validation.md` — defines how Proofs and Attestations are validated.
- `lifecycle.md` — defines the lifecycle of entities and trust relationships.
