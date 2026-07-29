# Axis Protocol Governance and ADR/RFC Process

This document describes how changes to Axis Protocol and Domain Profiles are proposed, discussed, and accepted.

---

## 1. Scope

Axis distinguishes between:

- **Axis Protocol** – the normative specification of the trust standard.
- **Axis Core** – a platform-agnostic reference implementation of the protocol.
- **Domain Profiles** – domain-specific extensions built on top of the protocol.

Governance MUST clearly separate:

- changes that affect **Axis Protocol** (the standard),
- changes that affect only a specific **Domain Profile**,
- changes that affect the **reference implementation** (Axis Core) — these are outside the scope of this document.

---

## 2. Design Records: ADR and RFC

Axis uses two complementary document types:

- **ADR (Architecture Decision Record)** – a focused document capturing a specific protocol-level architecture decision.
- **RFC (Request for Comments)** – a broader proposal that may include multiple decisions, discussion, and migration paths.

Conventions:

- ADRs are stored under `adr/` in this repository (Axis Protocol ADRs).
- Domain Profiles maintain their own ADR/RFC documents in their repositories.
- Implementation-specific ADRs (e.g., Axis Core) MUST live outside this repository.

Each ADR:
- has a unique ID (e.g., `ADR-0009`),
- has a status (`Proposed`, `Accepted`, `Rejected`, `Superseded`),
- references related ADRs/RFCs and protocol artifacts.

---

## 3. Axis Protocol Governance

Axis Protocol Governance is responsible for:

- Core terminology and concepts.
- Core trust model and entities (Device, Proof, Attestation, Registry).
- Core schemas and registries.
- Core conformance definitions.
- Protocol-level security and trust assumptions.
- Protocol evolution and compatibility rules.

Changes to Axis Protocol MUST:

- Follow the ADR/RFC process.
- Be accompanied by updated specifications.
- Be reviewed by the community.
- Preserve the chain of trust.

---

## 4. Domain Profile Governance

Domain Profiles MAY define their own governance processes, but MUST:

- Follow Axis Protocol terminology and schemas.
- Not conflict with Axis Protocol specifications.
- Document any deviations or extensions clearly.
- Preserve the chain of trust.

---

## 5. ADR/RFC Process

### 5.1 Proposal

1. Create an RFC or ADR document in the appropriate repository.
2. Fill in the required sections:
   - **Context** – why is this change needed?
   - **Decision** – what is the proposed change?
   - **Consequences** – how does this affect trust, compatibility, and implementations?
   - **Related** – links to related ADRs/RFCs.
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
