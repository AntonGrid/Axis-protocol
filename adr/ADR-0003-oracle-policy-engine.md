# ADR-0003: Oracle Does Not Make Policy Decisions — Policy Engine Does

**Status:** Accepted  
**Date:** 2025-06-28 (revised 2026-07-27)  
**Authors:** Axis Protocol Team  

---

## Context

In the current implementation, the Oracle performs multiple functions: verifies signatures, accumulates data, mints tokens, and also makes decisions about whether to quarantine a device, allow a Proof, or require an OTA update. This mixes responsibilities and complicates system evolution.

## Decision

The Oracle is responsible **only for**:

- Receiving Proofs from devices.
- Verifying cryptographic signatures.
- Passing verified data to the Policy Engine.
- Executing mint/action commands as instructed by the Policy Engine.

All decisions about device state, Proof admissibility, OTA requirements, and quarantine are made by a separate component — the **Policy Engine**. The Oracle is an **executor**, not a source of policies.

## Rationale

- **Separation of concerns:** Oracle handles cryptography and data transfer; Policy Engine handles logic and policies.
- **Flexibility:** Policies can be changed without rewriting the Oracle.
- **Scalability:** The Policy Engine can be extracted into a separate microservice.
- **Testability:** Each component can be tested in isolation.

## Consequences

- The Oracle **does not store** device state (this is handled by the Registry).
- The Oracle **does not make decisions** about quarantine or OTA.
- The Oracle executes mint/action commands **only after confirmation** from the Policy Engine.
- The Policy Engine interacts with the Device Registry and Oracle via APIs.

## Alternatives Considered

- **Oracle makes all decisions itself** — rejected due to mixing responsibilities.
- **Policy Engine embedded in the Oracle** — rejected as it violates the single responsibility principle.

---

## Related ADRs

- ADR-0002: Device Registry as the Single Source of Truth
- ADR-0004: Device Manifest
- ADR-0005: Device Lifecycle States

---

## Implementation Notes

- This decision is **protocol-level** and must be respected by all implementations.
- Implementation details (Policy Engine API, integration patterns) are defined in the Axis-core repository.
