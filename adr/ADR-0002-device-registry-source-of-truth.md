# ADR-0002: Device Registry as the Single Source of Truth

**Status:** Accepted  
**Date:** 2025-06-28 (revised 2026-07-27)  
**Authors:** Axis Protocol Team  

---

## Context

In the Axis Protocol, device state (active, quarantine, maintenance, etc.) could potentially be stored in multiple places: Oracle, SQLite, cache, Dashboard. This creates a risk of desynchronization and complicates diagnostics.

## Decision

The **Device Registry** is the **single source of truth** for device state. All components (Oracle, Dashboard, Provisioning Service) query the Registry to obtain the current state. The Registry stores:

- Current device state.
- Owner (wallet).
- Trust Level.
- Capabilities.
- Timestamp of the last heartbeat.
- Firmware version.
- State history (Audit Log).

## Rationale

- **Single point of control** for state simplifies diagnostics and auditing.
- **Eliminates the risk of desynchronization** between components.
- **Enables easy scaling:** new components simply query the Registry.
- **Ensures data integrity.**

## Consequences

- The Oracle **does not store** device state — it only verifies signatures and calls mint.
- The Policy Engine makes decisions based on data from the Registry.
- The Dashboard displays state obtained from the Registry.
- The Registry must have **high availability** (replication, backups).

## Alternatives Considered

- **Storing state separately in each component** — rejected due to the risk of desynchronization.
- **Using the blockchain as the source of truth** — rejected due to latency and cost.

---

## Related ADRs

- ADR-0001: Private Key Never Leaves the Device
- ADR-0003: Oracle and Policy Engine
- ADR-0005: Device Lifecycle States

---

## Implementation Notes

- This decision is **protocol-level** and must be respected by all implementations.
- Implementation details (database schema, API design) are defined in the Axis-core repository.
