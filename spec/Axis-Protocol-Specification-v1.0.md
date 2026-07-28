# Axis Protocol Specification

**Version:** 1.0 (Draft)

**Status:** Working Draft

**Protocol:** Axis

**License:** MIT

---

## Abstract

Axis is an open protocol that defines how physical devices can cryptographically prove real-world events and how digital systems can independently verify those proofs without trusting manufacturers, centralized servers, or individual organizations.

This specification defines the protocol architecture, component responsibilities, security model, device lifecycle, cryptographic model, and interoperability requirements.

The protocol is blockchain-agnostic.

Reference implementations may use different technologies while remaining protocol-compatible.

---

## Design Principles

The protocol is based on the following immutable principles.

### Open Standard

Axis is an open specification.

Anyone may implement compatible software or hardware.

---

### Blockchain Agnostic

The protocol is independent of any blockchain.

Reference implementations may support multiple networks.

---

### Trust Minimization

No component should require unnecessary trust.

Trust must be established through cryptographic verification.

---

### Architecture Before Implementation

Architecture defines the protocol.

Implementations may differ.

The protocol must remain compatible.

---

### Single Responsibility

Every component has exactly one responsibility.

No component should perform unrelated tasks.

---

### Security First

Convenience must never compromise security.

Every architectural decision must preserve trust.

---

## Protocol Overview

The Axis ecosystem consists of the following logical components.

- Device
- Provisioning Service
- Device Registry
- Device Manifest
- Oracle
- Policy Engine
- Smart Contract
- Dashboard
- SDK
- Applications

The following chapters describe each component in detail.

---

## Table of Contents

1. Introduction  
2. Protocol Philosophy  
3. Architecture Overview  
4. Design Principles  
5. Component Model  
6. Device Identity  
7. Device Lifecycle  
8. Provisioning Service  
9. Device Registry  
10. Device Manifest  
11. Policy Engine  
12. Oracle  
13. Proof-of-Event  
14. Smart Contract  
15. Protocol Economics  
16. Cryptography  
17. API Specification  
18. Dashboard  
19. SDK  
20. Security Model  
21. Reference Implementation  
22. Governance  
23. Mainnet Requirements  
24. Future Extensions  
25. Glossary  

---

## 1. Introduction

### 1.1 Purpose

This document defines the official Axis Protocol Specification.

Its purpose is to provide a complete and implementation-independent description of the Axis protocol.

The specification defines protocol behavior, component responsibilities, security principles, interoperability requirements, and architectural constraints.

This document is the normative reference for all future Axis implementations.

---

### 1.2 Scope

This specification covers:

- Protocol architecture
- Device identity
- Proof-of-Event
- Oracle behavior
- Device Registry
- Policy Engine
- Smart Contract interaction
- Cryptographic model
- Security model
- Protocol economics
- API
- Governance
- Mainnet requirements

User interfaces and implementation-specific details are outside the scope of this specification.

---

### 1.3 Goals

The protocol has four primary goals.

#### 1. Cryptographic Trust

Every event must be independently verifiable.

---

#### 2. Open Interoperability

Any compatible implementation should be able to participate in the Axis ecosystem.

---

#### 3. Decentralization

No single organization should become a mandatory trust anchor.

---

#### 4. Long-Term Stability

The protocol should remain compatible across multiple software generations.

---

### 1.4 Non-Goals

Axis does not attempt to define:

- hardware manufacturing;
- blockchain consensus;
- market regulations;
- domain-specific policies.

These responsibilities remain outside the protocol.

---

### 1.5 Terminology

Throughout this specification the following terms are used.

**MUST**

Indicates an absolute protocol requirement.

**SHOULD**

Indicates a recommended behavior.

**MAY**

Indicates an optional behavior.

These keywords follow RFC 2119 conventions whenever applicable.

---

### 1.6 Reference Implementation

The current reference implementation consists of:

- Smart Contract
- Oracle Server
- Device Firmware
- Dashboard
- Technical Documentation

Future implementations may differ while remaining protocol compatible.

---

### 1.7 Protocol Evolution

The Axis Protocol is designed to evolve.

Future versions may introduce additional components, capabilities, and optimizations.

Backward compatibility SHOULD be preserved whenever technically possible.

Breaking changes MUST be documented through ADRs/RFCs and reflected in future protocol versions.

---

## 2. Protocol Philosophy

### 2.1 Philosophy

Axis is an open protocol that defines how trust is established between physical devices and digital systems.

The protocol is not tied to a specific implementation, blockchain, programming language, company, or hardware manufacturer.

Its primary purpose is to establish common rules that enable independent implementations to interoperate.

---

### 2.2 Open Standard

Axis SHALL remain an open specification.

Any individual or organization MAY implement compatible software or hardware without requesting permission from the protocol authors.

Protocol compatibility SHALL be determined by compliance with this specification rather than by implementation origin.

---

### 2.3 Reference Implementation

The official Axis repositories MAY contain one or more reference implementations.

Each reference implementation demonstrates one correct implementation of the protocol.

It does not define the protocol itself.

The specification always takes precedence over implementation details.

---

### 2.4 Separation Between Protocol and Implementation

The protocol defines:

- required behavior;
- security guarantees;
- message formats;
- component responsibilities;
- interoperability rules.

Implementations define:

- programming language;
- operating system;
- blockchain integration;
- database technology;
- deployment architecture.

Different implementations MAY use different technologies while remaining protocol compatible.

---

### 2.5 Trust Model

The protocol minimizes trust assumptions.

Trust SHALL originate from cryptographic verification rather than centralized control.

No participant is automatically trusted because of ownership, infrastructure, or authority.

Every operation MUST be independently verifiable whenever possible.

---

### 2.6 Device Identity

Every physical device participating in Axis possesses its own cryptographic identity.

The private key MUST remain under the exclusive control of the device.

Only the corresponding public key MAY be distributed through the protocol.

Identity SHALL be independent of manufacturers, network operators, Oracle implementations, and blockchain infrastructure.

---

### 2.7 Architecture Principles

All protocol components SHALL follow the following principles.

#### Single Responsibility

Every component SHOULD perform one clearly defined responsibility.

Responsibilities SHOULD NOT overlap.

---

#### Separation of Concerns

Identity, policy, verification, storage, governance, and execution SHALL remain logically separated.

---

#### Replaceability

Every component SHOULD be replaceable without requiring changes to unrelated protocol components.

---

#### Extensibility

Future protocol versions SHOULD introduce new capabilities without breaking existing implementations whenever technically possible.

---

### 2.8 Interoperability

Independent implementations SHALL be able to exchange protocol messages without prior coordination.

Protocol compatibility SHALL depend exclusively on compliance with this specification.

---

### 2.9 Security Philosophy

Security SHALL always take precedence over convenience.

Architectural decisions SHALL favor verifiable correctness over implementation simplicity.

Whenever a trade-off exists between usability and protocol integrity, protocol integrity SHALL prevail.

---

### 2.10 Neutrality

Axis does not prescribe:

- a particular blockchain;
- a specific Oracle implementation;
- a specific hardware vendor;
- a cloud provider;
- a database engine;
- a commercial business model.

The protocol defines interfaces rather than products.

---

### 2.11 Evolution

The protocol is expected to evolve.

Evolution SHALL occur through documented architectural decisions and protocol proposals.

Breaking changes MUST be carefully evaluated and SHOULD be avoided whenever possible.

Long-term protocol stability is considered one of the primary design objectives.

---

### 2.12 Fundamental Principles

The following principles define the foundation of Axis.

1. Trust is established through cryptography.  
2. Architecture is more important than implementation.  
3. Open standards are more valuable than closed products.  
4. Specifications outlive software.  
5. Components must remain independent.  
6. Private keys never leave devices.  
7. Every proof must be independently verifiable.  
8. Protocol evolution must preserve interoperability whenever possible.  

These principles SHALL remain valid regardless of future protocol versions or implementation technologies.

---

## 3. Architecture Overview

### 3.1 Overview

The Axis Protocol is composed of independent components that collectively establish trust between physical devices and digital systems.

Each component has a clearly defined responsibility.

No component is permitted to perform responsibilities assigned to another component.

This separation enables scalability, maintainability, interoperability, and independent evolution.

---

### 3.2 High-Level Architecture

+----------------------+ | Dashboard | +----------+-----------+ | | REST / WebSocket API | ▼ +----------------------+ | Policy Engine | +----------+-----------+ | +-------+-------------+ | | ▼ ▼ +----------------+ +----------------+ | Device Registry| | Oracle | +--------+-------+ +--------+-------+ | | | | | Proof Verification | | ▼ ▼ +----------------+ +----------------+ | Provisioning | | Smart Contract | | Service | +--------+-------+ +--------+-------+ | | | ▼ ▼ +----------------+ Blockchain Network | Device Manifest| +--------+-------+ | ▼ +----------------+ | Device | +----------------+


---

### 3.3 Component Model

The Axis Protocol consists of the following logical components.

| Component         | Responsibility                  |
|------------------|----------------------------------|
| Device           | Produces Proof-of-Event         |
| Provisioning Service | Registers new devices       |
| Device Registry  | Stores device identity and state|
| Device Manifest  | Delivers signed configuration   |
| Oracle           | Verifies Proofs                 |
| Policy Engine    | Applies protocol policies       |
| Smart Contract   | Executes protocol state changes |
| Dashboard        | User interaction                |
| SDK              | Developer integration           |

---

### 3.4 Component Independence

Each component SHALL operate independently.

Failure of one component SHOULD NOT require redesign of the remaining architecture.

Communication SHALL occur only through defined protocol interfaces.

---

### 3.5 Device

The Device represents a physical source of measurable events.

Responsibilities include:

- measuring data;
- generating Proof-of-Event;
- signing messages;
- protecting private keys;
- communicating with the protocol.

The Device SHALL NOT perform policy decisions.

---

### 3.6 Provisioning Service

Provisioning Service is responsible for onboarding devices.

Responsibilities include:

- registration;
- identity verification;
- claim code generation;
- manifest distribution.

Provisioning SHALL NOT verify Proofs.

Provisioning SHALL NOT manage protocol economics.

---

### 3.7 Device Registry

Device Registry is the authoritative source of device metadata.

Responsibilities include:

- identity;
- ownership;
- lifecycle state;
- capabilities;
- firmware version;
- trust level;
- audit history.

No other component SHALL become the primary source of this information.

---

### 3.8 Device Manifest

The Device Manifest defines operational parameters.

Typical information includes:

- heartbeat interval;
- proof interval;
- Oracle endpoint;
- protocol version;
- capabilities;
- policy version.

The Manifest SHALL be cryptographically signed.

---

### 3.9 Oracle

The Oracle performs cryptographic verification.

Responsibilities include:

- signature verification;
- nonce validation;
- timestamp validation;
- Proof validation;
- Smart Contract invocation.

The Oracle SHALL NOT define protocol policy.

---

### 3.10 Policy Engine

Policy Engine determines whether verified Proofs satisfy protocol rules.

Responsibilities include:

- quarantine decisions;
- trust evaluation;
- anomaly detection;
- OTA requirements;
- Proof acceptance.

Policy Engine SHALL remain independent from Oracle implementation.

---

### 3.11 Smart Contract

The Smart Contract represents the protocol state on-chain (where applicable).

Responsibilities include:

- state management;
- asset minting (if applicable);
- staking (if applicable);
- treasury management (if applicable);
- governance (if applicable).

Domain-specific business logic SHOULD remain off-chain or in separate contracts.

---

### 3.12 Dashboard

Dashboard provides the user interface.

Dashboard SHALL NOT become a protocol component.

It is a client of the protocol.

---

### 3.13 SDK

SDK implementations provide developer access to the protocol.

SDKs MAY exist for multiple programming languages.

SDKs SHALL implement protocol behavior defined by this specification.

---

### 3.14 Communication Principles

Components communicate through well-defined interfaces.

Internal implementation details SHALL remain encapsulated.

Components SHOULD avoid direct database dependencies whenever possible.

---

### 3.15 Architectural Stability

Individual implementations may evolve.

The architectural model defined by this chapter SHALL remain stable across protocol versions unless modified through the formal protocol evolution process.

---

## 4. Device Identity

### 4.1 Overview

Every device participating in the Axis Protocol SHALL possess a unique cryptographic identity.

Device identity forms the foundation of trust throughout the protocol.

Without a valid identity, a device SHALL NOT participate in Proof-of-Event.

---

### 4.2 Objectives

Device Identity provides:

- authentication;
- proof ownership;
- message signing;
- replay protection;
- lifecycle tracking;
- secure provisioning.

Identity SHALL remain stable throughout the operational lifetime of the device.

---

### 4.3 Identity Components

Each device identity consists of:

- Device Identifier (Device ID)
- Ed25519 Key Pair
- Public Key
- Lifecycle State
- Capabilities
- Firmware Information

Additional metadata MAY be introduced by future protocol versions.

---

### 4.4 Device Identifier

Every device SHALL possess a globally unique Device ID.

The Device ID SHALL remain immutable after registration.

The protocol does not mandate a specific generation algorithm.

Possible implementations include:

- UUID
- Secure Random Identifier
- Manufacturer Identifier
- Hardware-derived Identifier

---

### 4.5 Cryptographic Identity

Each device SHALL generate an Ed25519 key pair.

Private keys SHALL be generated on the device.

Private keys SHALL never leave the device.

Only public keys MAY be transmitted through the network.

This requirement is mandatory.

---

### 4.6 Ownership

Device ownership is independent from device identity.

Ownership MAY change.

Identity SHALL NOT.

Ownership records SHALL be maintained by the Device Registry.

---

### 4.7 Public Key Registration

During provisioning the following information SHALL be registered:

- Device ID
- Public Key
- Device Type
- Firmware Version
- Registration Timestamp

The Registry SHALL reject duplicate public keys.

The Registry SHALL reject duplicate Device IDs.

---

### 4.8 Identity Verification

Every protocol message requiring authentication SHALL include a cryptographic signature.

The receiver SHALL verify:

- public key;
- signature;
- timestamp;
- nonce.

Messages failing verification SHALL be rejected.

---

### 4.9 Identity Persistence

Identity SHALL survive:

- reboot;
- power loss;
- firmware update;
- network interruption.

Identity SHALL NOT be regenerated except during explicit factory reset procedures.

---

### 4.10 Factory Reset

A factory reset MAY erase local configuration.

It SHALL NOT automatically preserve protocol registration.

If identity is regenerated, the device SHALL repeat the registration process.

---

### 4.11 Secure Storage

Production devices SHOULD use hardware-backed key storage.

Examples include:

- Secure Element
- TPM
- Hardware Security Module

Software storage MAY be used only for development and testing.

---

### 4.12 Identity Lifecycle

Identity progresses through the following states:

UNREGISTERED │ ▼ REGISTERED │ ▼ CLAIMED │ ▼ PROVISIONED │ ▼ ACTIVE │ ├── → QUARANTINE │ QUARANTINE │ ├── → ACTIVE │ ├── → MAINTENANCE │ ▼ MAINTENANCE │ ├── → ACTIVE │ ▼ REVOKED


The meaning of each state is defined in Chapter 5.

---

### 4.13 Identity Integrity

Identity SHALL NOT depend upon:

- Oracle implementation;
- blockchain implementation;
- database technology;
- cloud provider;
- manufacturer infrastructure.

Identity belongs exclusively to the device.

---

### 4.14 Future Extensions

Future protocol versions MAY support:

- hardware attestation;
- post-quantum cryptography;
- decentralized identity (DID);
- certificate chains;
- multiple authentication methods.

Such extensions SHALL remain backward compatible whenever technically possible.

---

### 4.15 Requirements Summary

A compliant implementation SHALL satisfy the following requirements.

- Every device MUST have a unique identity.
- Every device MUST possess its own Ed25519 key pair.
- Private keys MUST never leave the device.
- Public keys MUST be registered before protocol participation.
- Every authenticated message MUST be signed.
- Identity MUST remain stable throughout the device lifecycle.
- Ownership MAY change independently from identity.

---

## 5. Device Lifecycle

### 5.1 Overview

Every device in the Axis Protocol progresses through a defined lifecycle.

The lifecycle ensures clarity, security, and auditability.

---

### 5.2 Lifecycle States

| State         | Description                               |
|--------------|-------------------------------------------|
| **UNREGISTERED** | Device is unknown to the system.     |
| **REGISTERED**   | Device has cryptographic identity but no owner. |
| **CLAIMED**      | Device is linked to an owner.        |
| **PROVISIONED**  | Device is configured and ready.      |
| **ACTIVE**       | Device is fully operational.         |
| **QUARANTINE**   | Device is suspected of malfunction.  |
| **MAINTENANCE**  | Device is undergoing maintenance.    |
| **REVOKED**      | Device is permanently decommissioned.|

---

### 5.3 State Transitions

| From        | To          | Trigger                 |
|-------------|-------------|-------------------------|
| UNREGISTERED| REGISTERED  | Registration request    |
| REGISTERED  | CLAIMED     | Owner linking           |
| CLAIMED     | PROVISIONED | Configuration complete  |
| PROVISIONED | ACTIVE      | Activation command      |
| ACTIVE      | QUARANTINE  | Suspicious activity     |
| ACTIVE      | MAINTENANCE | Scheduled maintenance   |
| ACTIVE      | REVOKED     | Owner/system revocation |
| QUARANTINE  | ACTIVE      | Issue resolved          |
| QUARANTINE  | REVOKED     | Unresolvable issue      |
| QUARANTINE  | MAINTENANCE | Maintenance required    |
| MAINTENANCE | ACTIVE      | Maintenance complete    |
| MAINTENANCE | REVOKED     | Cannot be restored      |

---

### 5.4 State Authority

The Device Registry is the single source of truth for device state.

All components MUST query the Registry for current state.

No component MAY maintain its own state cache without explicit permission.

---

## 6. Provisioning Service

### 6.1 Overview

The Provisioning Service is the entry point for new devices.

It handles registration, identity verification, and initial configuration.

---

### 6.2 Registration Flow

1. **Key Generation** — device generates Ed25519 key pair.  
2. **Registration Request** — device sends public key and metadata.  
3. **Verification** — service verifies signature and uniqueness.  
4. **Claim Code** — service generates one-time claim code.  
5. **Response** — device receives claim code and Oracle endpoint.  
6. **Owner Linking** — user enters claim code, device transitions to CLAIMED.  

---

### 6.3 API Endpoints

#### POST /identity/register

Register a new device.

**Request:**

```json
{
  "device_id": "dev_9e9c644e1580a83b",
  "public_key": "<base64-encoded-public-key>",
  "signature": "<base64-encoded-signature>",
  "device_type": "Verified",
  "firmware_version": "1.0.0"
}
Response:

{
  "claim_code": "A7F4-K92Q",
  "status": "registered",
  "oracle_endpoint": "https://oracle.axisprotocol.io"
}
POST /identity/claim
Link device to owner.

Request:

{
  "claim_code": "A7F4-K92Q",
  "owner_id": "owner_1234"
}
Response:

{
  "status": "claimed",
  "device_id": "dev_9e9c644e1580a83b"
}
7. Device Registry
7.1 Overview
The Device Registry is the authoritative source of device metadata.

It maintains identity, ownership, state, and history.

7.2 Registry Responsibilities
Store device identity (Device ID, public key)
Track ownership (owner identifiers, e.g., accounts)
Maintain lifecycle state
Record capabilities and trust level
Store firmware version
Maintain audit history
7.3 Registry Integrity
All updates MUST be authorized.

State changes MUST be logged.

History MUST be immutable and auditable.

Registry MUST reject duplicate identities.

8. Device Manifest
8.1 Overview
The Device Manifest is a signed configuration document.

It defines operational parameters for the device.

8.2 Manifest Content
The Manifest contains:

device_id — unique identifier
trust_level — trust classification
capabilities — device capabilities
heartbeat_interval — heartbeat frequency
proof_interval — proof frequency
oracle_endpoint — Oracle URL
policy_version — policy version
signature — cryptographic signature
8.3 Manifest Security
Manifest MUST be signed by the Registry (or another authorized signing authority defined by the protocol deployment).

Device MUST verify signature before use.

Signature MUST be checked using the Registry (or authorized signer) public key.

Manifest MUST be stored securely on device.

9. Oracle
9.1 Overview
The Oracle performs cryptographic verification of device proofs.

It acts as a bridge between devices and the blockchain (where a blockchain is used).

9.2 Oracle Responsibilities
Receive Proofs from devices
Verify cryptographic signatures
Validate nonce and timestamp
Aggregate data (if applicable)
Submit verified data to Smart Contract (if applicable)
9.3 Proof Verification
The Oracle SHALL verify:

Signature — using device public key
Nonce — not previously used
Timestamp — within acceptable window
Payload — well-formed and valid
9.4 Oracle Integrity
Oracle MUST NOT modify Proof content.

Oracle MUST NOT make policy decisions.

Oracle MUST NOT store device lifecycle state as the primary source of truth.

10. Policy Engine
10.1 Overview
The Policy Engine applies protocol policies to verified Proofs.

It determines whether Proofs are accepted or rejected.

10.2 Policy Responsibilities
Evaluate Proofs against defined rules
Make quarantine decisions
Assess trust levels
Detect anomalies
Enforce OTA requirements
10.3 Policy Independence
Policy Engine MUST be independent from Oracle implementation.

Policy decisions MUST be auditable.

Policies MUST be versioned and documented.

11. Smart Contract
11.1 Overview
The Smart Contract represents the protocol state on-chain (for deployments that use a blockchain).

It executes state changes and manages assets where applicable.

11.2 Contract Responsibilities
Store device registrations (if applicable)
Manage protocol state
Execute asset operations (if applicable)
Support governance (if applicable)
11.3 Contract Integrity
Contract MUST be verified and audited.

Contract MUST use checked arithmetic.

Contract MUST validate all inputs.

Contract MUST enforce access controls.

12. Cryptography
12.1 Overview
The Axis Protocol uses Ed25519 for cryptographic operations.

Ed25519 is chosen for its security, performance, and simplicity.

12.2 Key Generation
Private keys SHALL be generated on the device.

Private keys SHALL never leave the device.

Public keys SHALL be registered with the Protocol.

12.3 Signing
Messages SHALL be signed using Ed25519.

The signed message SHALL include:

Device ID
Timestamp
Nonce
Payload
12.4 Verification
Receivers SHALL verify Ed25519 signatures.

Verification SHALL include:

Public key lookup
Signature verification
Nonce check
Timestamp validation
13. Security Model
13.1 Threat Model
The Axis Protocol addresses the following threats:

Threat	Mitigation
Spoofing	Ed25519 signatures
Tampering	Cryptographic integrity
Repudiation	Nonce and timestamp
Information Disclosure	Minimal on-chain data (where used)
Denial of Service	Gas limits / rate limits / throttling
Elevation of Privilege	Contract architecture, authority checks
13.2 Security Layers
Device Layer — Secure Element, signed firmware
Network Layer — TLS, authenticated channels, optionally decentralized oracle networks
Contract Layer — Checked arithmetic, access control, authority checks
Reputation Layer — Trust scoring, anomaly detection
14. Governance
14.1 Overview
The Axis Protocol is governed by the community.

Governance ensures the protocol can evolve while maintaining stability.

The protocol does not mandate the existence of a governance token or a particular voting mechanism. Individual deployments MAY choose their own governance structures.

14.2 Governance Components
ADR/RFC Process — documented changes
Token holders (if a governance token exists) — MAY vote on protocol parameters
Guardians — manage emergency operations
Maintainers — prepare code and tests
14.3 Decision Process
Proposal — submit ADR/RFC
Discussion — community feedback
Voting — decision via the governance mechanism of a given deployment (which MAY include token voting)
Implementation — code and tests
Deployment — protocol update
15. Future Extensions
15.1 Post-Quantum Cryptography
Future versions MAY support post-quantum algorithms.

15.2 Decentralized Identity (DID)
Future versions MAY integrate with DID standards.

15.3 Cross-Chain Interoperability
Future versions MAY support multiple blockchains.

15.4 Hardware Attestation
Future versions MAY support hardware-based attestation.

16. Glossary
Term	Definition
Actor	Entity capable of issuing or receiving claims
Asset	Something about which claims are made
Attestation	Signed statement about a claim or asset
Claim	Structured statement about an asset
Device	Physical source of measurable events
Domain Profile	Domain-specific extension of the core Axis protocol
Oracle	Component that verifies Proofs
Policy	Set of rules governing claims and attestations
Proof	Cryptographic evidence of an event
Record	Fundamental unit of protocol data
Registry	Source of truth for protocol entities
Normative References
RFC 2119: Key words for use in RFCs to Indicate Requirement Levels
Ed25519: High-speed high-security signatures
Document History
Version	Date	Changes
1.0 Draft	2026-07-27	Initial version based on Axis Protocol Specification
