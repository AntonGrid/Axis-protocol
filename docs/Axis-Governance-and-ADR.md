# Axis Governance and ADR/RFC Process

This document describes how changes to Axis Core and Domain Profiles are proposed, discussed, and accepted.

---

## 1. Scope

Axis distinguishes between:

- **Axis Core** – protocol-wide concepts, terminology, schemas, registries, and reference implementations.
- **Domain Profiles** – domain-specific extensions built on top of Axis Core.

Governance MUST clearly separate:

- changes that affect **Axis Core**,
- changes that affect only a specific **Domain Profile**.

---

## 2. Design Records: ADR and RFC

Axis uses two complementary document types:

- **ADR (Architecture Decision Record)** – a focused document capturing a specific architecture decision.
- **RFC (Request for Comments)** – a broader proposal that may include multiple decisions, discussion, and migration paths.

Conventions:

- ADRs are stored under `adr/` in this repository (Axis Core ADRs).
- Domain Profiles maintain their own ADR/RFC documents in their repositories.
- Each ADR:
  - has a unique ID (e.g. `ADR-0009`),
  - has a status (`Proposed`, `Accepted`, `Rejected`, `Superseded`),
  - references related ADRs/RFCs and implementation artifacts.

---

## 3. Axis Core Governance

Axis Core Governance is responsible for:

- Core terminology and concepts.
- Core schemas and registries (Manifest, Capability, Event, Error).
- On-chain attestation format and verification rules.
- Core conformance definitions and testing strategy.
- Protocol-level security and upgrade strategy.

Changes to Axis Core MUST:

- Follow the ADR/RFC process.
- Be accompanied by updated specifications and tests.
- Be reviewed by the community.

---

## 4. Domain Profile Governance

Domain Profiles MAY define their own governance processes, but MUST:

- Follow Axis Core terminology and schemas.
- Not conflict with Axis Core specifications.
- Document any deviations or extensions clearly.

---

## 5. ADR/RFC Process

### 5.1 Proposal

1. Create an RFC or ADR document in the appropriate repository.
2. Fill in the required sections (Context, Decision, Consequences, Related).
3. Submit as a Pull Request.

### 5.2 Discussion

- Open discussion period (minimum 7 days).
- Feedback from maintainers, domain experts, and community.

### 5.3 Acceptance

- ADR is accepted by the relevant maintainers.
- RFC may require a formal vote or consensus.

### 5.4 Implementation

- Implementation follows the accepted ADR/RFC.
- Updates to specifications and tests are submitted.

### 5.5 Review

- Implementation is reviewed and merged.

---

## 6. Related Documents

- [ADR-0009: Governance Model](../adr/ADR-0009-Governance-Protocol.md)
- [Axis Protocol Specification](./Axis-Protocol-Specification.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
