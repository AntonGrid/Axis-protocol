# Axis Protocol — Terminology

This document defines core terminology used in the Axis Protocol.

It is **normative** for the protocol and **referential** for implementations and domain profiles.

---

## 1. Axis Protocol

**Axis Protocol** is an **overlay trust standard** — a domain-agnostic language of trust between physical devices and digital systems.

It defines:
- how devices obtain cryptographic identity,
- how identity is registered and verified,
- how devices prove that physical events occurred,
- how proofs are verified by independent parties,
- how trust is transferred from the physical world to the digital world — and back.

Axis Protocol is **not** tied to any specific blockchain, platform, vendor, or domain.

---

## 2. Device

A **Device** is a physical entity that produces events.

It has:
- a **cryptographic identity** (private key + public key),
- a **stable identifier** (device ID),
- a **manifest** that defines its capabilities and configuration.

The private key **never leaves the device**.

---

## 3. Event

An **Event** is a measurable occurrence produced by a Device.

Examples:
- generation of 1 MWh of electricity,
- movement of a package through a checkpoint,
- completion of a manufacturing step.

Events are **not transmitted directly**. They are **proved** cryptographically.

---

## 4. Proof

A **Proof** is a cryptographic statement that a specific Event occurred, produced by a Device.

A Proof contains:
- `device_id` — identifier of the device,
- `event_data` — structured description of the event,
- `timestamp` — when the event occurred,
- `nonce` — to prevent replay attacks,
- `signature` — cryptographic signature by the device's private key.

The Proof is the **atomic unit of trust** from the physical world.

---

## 5. Verifier

A **Verifier** is any entity that checks a Proof:
- signature validity,
- nonce uniqueness,
- timestamp freshness,
- consistency with the device's registry state.

Verification is **deterministic** and does not require a trusted third party.

---

## 6. Attestation

An **Attestation** is a signed statement by a trusted entity (e.g., an Oracle) that a Proof has been verified and is valid.

An Attestation contains:
- `proof_id` — reference to the Proof,
- `decision` — whether the Proof is valid or invalid,
- `oracle_id` — identifier of the attesting entity,
- `timestamp` — when the attestation was issued,
- `signature` — signature by the attesting entity.

The Attestation is the **bridge** from the physical world to the digital world.

---

## 7. Registry

A **Registry** is a verifiable store of device identities, states, and attestations.

The Registry is the **source of truth** for the protocol.

It maintains:
- device identity and public keys,
- device lifecycle states,
- attestation history,
- policy definitions.

---

## 8. Digital Claim

A **Digital Claim** is a statement in the digital world that is backed by an Attestation.

Examples:
- "Device X produced 1 MWh of electricity."
- "Device Y is currently in State Z."

Digital Claims are **cryptographically anchored** to physical events through the Proof → Attestation pipeline.

---

## 9. Trust Graph

The **Trust Graph** connects:
- Devices → Proofs → Attestations → Digital Claims → Applications.

Any participant can verify any link in the graph independently.

---

## 10. Policy

A **Policy** is a set of rules governing trust and verification.

Policies define:
- who can issue which attestations,
- how claims are validated,
- how conflicts are resolved.

---

## 11. Oracle

An **Oracle** is a trusted entity that verifies Proofs and issues Attestations.

The Oracle acts as a bridge between the physical world and the digital world.

---

## 12. Reference Implementation

A **Reference Implementation** is a concrete implementation of Axis Protocol (e.g., Axis Core).

It:
- demonstrates how the protocol works,
- provides libraries, SDKs, and tools,
- serves as a baseline for domain profiles.

Reference implementations are **not** part of the protocol.

---

## 13. Normative vs. Informative

- **Normative** — must be followed for conformance.
- **Informative** — explanatory, non-binding.

The protocol specification is normative.  
Reference implementations and domain profiles are informative.
