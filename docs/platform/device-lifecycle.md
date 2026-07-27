# Device Lifecycle Specification

**Status:** Draft v0.1

## Introduction

This document describes the complete lifecycle of a device within the Axis Protocol ecosystem. All devices go through a sequence of states, each of which defines their behavior, rights, and available actions.

The goal is to ensure transparency, manageability, and security across the entire network.

---

## Device States

### 1. UNREGISTERED
The device is unknown to the system. It has no cryptographic identity within Axis.

**Actions:**
- Generate a key pair (private/public key).
- Send a registration request with the public key.

### 2. REGISTERED
The device has a cryptographic identity but is not yet linked to an owner.

**Actions:**
- Wait for owner linking via Claim Code.
- Send heartbeat (periodic status signals).

### 3. CLAIMED
The device is linked to a specific owner (wallet) but not yet configured for operation.

**Actions:**
- Receive configuration (Device Manifest).
- Configure network, synchronize time.

### 4. PROVISIONED
The device is fully configured and ready for operation, but not yet active.

**Actions:**
- Wait for activation command.
- Perform self-test of all systems.

### 5. ACTIVE
The device is operational, signing and sending Proofs to the Oracle.

**Actions:**
- Send Proofs.
- Send heartbeat.
- Participate in pools (if applicable).

### 6. QUARANTINE
The device is suspected of malfunction or compromise.

**Actions:**
- Diagnostics.
- Investigation.
- Possible restoration or revocation.

### 7. MAINTENANCE
The device is undergoing maintenance (firmware update, hardware check, etc.).

**Actions:**
- Firmware update.
- Hardware diagnostics.
- Return to ACTIVE or transition to REVOKED.

### 8. REVOKED
The device is permanently decommissioned.

**Actions:**
- No further actions allowed.

---

## State Transitions

| From | To | Trigger |
|------|----|---------|
| UNREGISTERED | REGISTERED | Registration request with valid public key |
| REGISTERED | CLAIMED | Claim Code entered by owner |
| CLAIMED | PROVISIONED | Device configured and self-test passed |
| PROVISIONED | ACTIVE | Activation command from owner or system |
| ACTIVE | QUARANTINE | Suspicious activity, policy violation |
| ACTIVE | MAINTENANCE | Scheduled or unscheduled maintenance |
| ACTIVE | REVOKED | Owner or system revocation |
| QUARANTINE | ACTIVE | Diagnostics passed, issue resolved |
| QUARANTINE | REVOKED | Issue cannot be resolved or device compromised |
| QUARANTINE | MAINTENANCE | Maintenance required |
| MAINTENANCE | ACTIVE | Maintenance complete |
| MAINTENANCE | REVOKED | Device cannot be restored |
| REVOKED | (terminal) | No transitions out |

---

## Normative Requirements

- **State Authority:** The Device Registry is the single source of truth for device state (see ADR-0002).
- **State Changes:** All state transitions MUST be authorized and logged.
- **Auditability:** State transitions MUST be auditable for compliance and security review.

---

## Related Documents

- [ADR-0002: Device Registry as the Single Source of Truth](../../adr/ADR-0002-device-registry-source-of-truth.md)
- [ADR-0005: Device States and Lifecycle](../../adr/ADR-0005-device-states.md)
- [Provisioning Specification](./provisioning.md)
