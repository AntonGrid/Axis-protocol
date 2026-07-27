# ADR-0007: Security & Key Management

**Status:** Draft (Approved)  
**Date:** 2026-07-17 (revised 2026-07-27)  
**Authors:** Axis Protocol Team  
**Related:** ADR-0001, ADR-0008, ADR-0009

---

## Context

Axis Protocol connects physical devices and blockchain layers (reference implementation uses Solana). The repository contains firmware/, oracle/, programs/, registries/, and other components. To ensure system security, it is critical to define a unified, documented, and verifiable approach to key management and signing: which keys are used by whom and where, how they are generated, how the root of trust is stored, how device attestation is performed, how key rotation/revocation is handled, and how firmware signatures are linked to on-chain registries and governance.

Without a formalized ADR, different subsystems (firmware production, oracle operators, contracts, registration services) would have incompatible or insecure procedures.

---

## Decision

### 1. Root of Trust

A single root of trust for each manufacturing/supply chain is stored and managed through a **Governance-managed Root Key Registry** (on-chain or off-chain registry with on-chain anchoring).

### 2. Key Types

| Key Type | Algorithm | Purpose |
|----------|-----------|---------|
| **On-chain keys** | ED25519 | Transactions, program upgrades (multisig), oracle node on-chain signatures |
| **Device signing keys** | ED25519 | Signing device manifests and messages |
| **Device attestation keys** | ED25519 | Stored in Secure Element; attestation format: COSE/CBOR (primary), X.509 (optional) |
| **Firmware signing keys** | ED25519 | Offline, cold key — signing firmware images |
| **Transport keys (TLS)** | ECDSA P-256 or x25519 | Secure connection (OTA, provisioning) |

### 3. Root-of-Trust Model

- **Chain of trust:** Root CA / Root Public Key (Governance-managed) → Manufacturer CA (or signing authority) → Device attestation key.
- **Alternative (lightweight deployments):** Root public key directly signs device public keys (acceptable with documented production process).

### 4. Key Lifecycle

- **Generation:** Private keys **MUST** be generated in a secure environment (HSM / Secure Element / TPM). Device keys **MUST** be generated in the device secure element when possible; otherwise, generated in a provisioning environment with a documented secure transfer to the device.
- **Storage:** Private keys **MUST** be stored in a secure hardware module on the device (Secure Element / eFuse / TPM). For reference hardware, a secure element is the recommended configuration.
- **Provisioning:** Devices are enrolled with a signed Device Enrollment Certificate / Manifest containing `device_id`, public keys, and provisioning metadata. This manifest is anchored in the Manifest Registry.
- **Rotation:** Keys **MUST** support rotation. The rotation process **MUST** produce new key material, submit the new public key and attestation to the registry, and optionally re-sign device manifests. Old keys **MUST** be revocable in the registry.
- **Revocation:** The Registry supports revocation records and reasons; chain-of-trust checks **MUST** validate revocation status.

### 5. Attestation

- Devices **SHALL** produce attestation statements binding device identity to the measured firmware image and device public key.
- **Attestation format:** COSE/CBOR-based (PRIMARY) or optional X.509-based for interoperability. COSE/CBOR is preferred for compactness and ease of parsing on constrained devices.
- **Fields expected in attestation (COSE/CBOR):**
  - `device_id` (UUID)
  - `device_pubkey`
  - `firmware_manifest_hash`
  - `nonce`
  - `timestamp`
  - `attestation_signature` (signed by device attestation key or via TPM/secure element quote)
- **Verifiers** (oracle nodes or on-chain verifiers) **SHALL** validate attestation using manifest registry root keys and firmware signature checks.

### 6. Firmware Signing & OTA

- Firmware images **MUST** be signed by a Firmware Signing Key (cold/offline).
- Signature and firmware manifest (hash, version, allowed device models, minimum attestation policy) are stored in the Manifest Registry and distributed to devices and oracles.
- Devices **MUST** verify firmware signature before installing.

### 7. Anchoring and Registries

- Public keys for root-of-trust and manufacturer authorities **MUST** be publishable in the Manifest Registry and anchored on-chain via periodic Merkle root anchoring.
- **Anchoring policy:** Periodic anchoring once per 24 hours (daily Merkle root anchor) is **REQUIRED**. Emergency revocation anchors **MUST** be supported and performed as needed to record urgent revocations or trust-root changes.

### 8. Governance

- Governance-managed Root Key rotations and trust root changes **MUST** be performed via the protocol governance process (see ADR-0009). Emergency rotation flow with multisig/time-lock is required.

---

## Related ADRs

- ADR-0001: Private Key Never Leaves the Device
- ADR-0005: Device States and Lifecycle
- ADR-0008: Secure Firmware Updates (OTA)
- ADR-0009: Governance Model

---

## Implementation Notes

- This decision is **protocol-level** and must be respected by all implementations.
- Implementation details (specific hardware recommendations, attestation format details) are defined in the Axis-core repository.
