# Axis Protocol – Entity and Message Lifecycle

This document describes the **logical lifecycle** of entities and messages in systems built on Axis Protocol.  
It is **implementation‑neutral** and does not assume any specific ledger, database, blockchain, or runtime.

Axis Protocol itself defines **messages and invariants**, not a global state model.  
However, most deployments will interpret messages as operations on some notion of *entities* and *state*.  
This document provides a common vocabulary and recommended patterns for such lifecycles.

---

## 1. Concepts

### 1.1. Entity

An **Entity** is any logical object whose state is tracked via Axis messages.

Examples (illustrative only):

- Devices, sensors, meters
- Contracts, agreements, orders
- Accounts, positions, assets

Each entity is identified by:

- `domain` – high‑level application namespace.
- `entity_type` – type of entity within the domain.
- `entity_id` – stable identifier of a specific entity instance.

Axis Protocol does not prescribe how entities are stored or represented internally.

### 1.2. Messages and state transitions

Implementations typically interpret messages as **state transitions** or **state observations**.

Common patterns:

- **Commands** – requests to change state.
- **Events** – records of facts or state changes.
- **Queries / QueryResponses** – read‑only access to current or derived state.
- **Notifications / Errors** – auxiliary messages.

The **lifecycle** of an entity is thus the sequence of valid state transitions driven by messages.

---

## 2. Generic entity lifecycle

Axis Protocol is domain‑agnostic, but most entities follow some variation of the following generic phases:

1. **Non‑existent** – the entity is not yet known to the system.
2. **Pending / Initializing** – the entity is in the process of being created or activated.
3. **Active** – the entity is usable according to domain rules.
4. **Suspended / Disabled** – the entity exists but is not currently active.
5. **Terminated / Retired** – the entity is no longer active and cannot be reactivated (unless the domain explicitly allows it).

Each domain MAY refine or rename these phases, but SHOULD define:

- which messages are allowed in each phase,
- what transitions between phases are valid,
- what invariants must hold in each phase.

---

## 3. Creation

### 3.1. Creation messages

Entity creation is typically initiated by one of the following:

- A **Command** requesting creation (e.g. “CreateDevice”, “OpenAccount”).
- A direct **Event** indicating that an entity now exists (e.g. imported from an external system).

Axis Protocol does not fix which pattern must be used, but deployments SHOULD document:

- The allowed creation messages per `entity_type`.
- Required fields and preconditions for creation.

### 3.2. Preconditions for creation (examples)

Typical state‑independent preconditions:

- `entity_id` is syntactically valid.
- All required initialization fields are present and valid.

Typical state‑dependent preconditions:

- No existing active or pending entity with the same `entity_id` in the same `domain` and `entity_type`, unless the domain explicitly allows this.
- Optional authorization checks (e.g. the creator is allowed to create entities of this type).

If any precondition fails, the creation message MUST be rejected.

---

## 4. Updates

### 4.1. Update messages

Updates are messages that modify or extend an existing entity’s state.  
They are typically modeled as **Commands** and/or **Events**.

Key questions each domain MUST answer:

- Which fields of an entity are mutable vs immutable?
- What lifecycle phase(s) allow updates?
- How are partial updates represented (e.g. patches vs full snapshots)?

### 4.2. Preconditions for updates

Examples of common rules:

- The entity MUST exist and be in a phase that permits updates (e.g. `Active`).
- The update MUST respect domain‑specific constraints (e.g. cannot reduce a counter below zero).
- If optimistic concurrency is used, version or revision numbers MUST match.

If these conditions are not met, the update message MUST be rejected or lead to a defined conflict resolution behavior.

---

## 5. Suspension and resumption

Some domains require temporarily disabling an entity (e.g. maintenance mode for a device, account freeze).

### 5.1. Suspension

A **suspend** operation typically:

- Requires the entity to be in an `Active` phase.
- Transitions the entity to a `Suspended/Disabled` phase.
- May carry a reason code or metadata.

In the `Suspended` phase:

- Certain operations (e.g. usage, billing, external communication) may be blocked.
- Maintenance or administrative operations may still be allowed.

### 5.2. Resumption

A **resume** operation:

- Requires the entity to be in `Suspended` phase.
- Transitions it back to `Active`, if all necessary conditions are satisfied (e.g. resolved issues, valid configuration).

Domains SHOULD specify:

- which operations are allowed in suspended state,
- what validation is required before resuming.

---

## 6. Termination / retirement

Termination (or retirement) marks the logical end of an entity’s active lifecycle.

Characteristics:

- The entity transitions from `Active` or `Suspended` to `Terminated/Retired`.
- No further “normal” operations are allowed unless the domain explicitly supports reactivation.

Domains SHOULD define:

- whether termination is reversible,
- which messages, if any, are permitted after termination (e.g. audits, archival operations, corrections).

Common rules:

- Attempts to perform operations that require an `Active` entity on a `Terminated` one MUST be rejected or treated as invalid according to domain policy.

---

## 7. Message lifecycle and ordering

Axis Protocol itself does not mandate a global ordering mechanism.  
However, many deployments impose ordering at the entity level (e.g. via sequence numbers or timestamps).

### 7.1. Message ordering per entity

Typical strategies:

- **Monotonic sequence numbers**
  - Each entity tracks a `version` or `sequence` field.
  - Messages carry the expected version; mismatches lead to rejections or conflict handling.

- **Time‑based ordering**
  - Timestamps are used for causality hints.
  - Late or out‑of‑order messages are either rejected or reconciled by domain logic.

Implementations SHOULD clearly document:

- whether message ordering is strictly enforced,
- how out‑of‑order messages are handled.

### 7.2. Idempotence and duplication

Deployments SHOULD define which messages are intended to be **idempotent** at the entity level.

Examples:

- Retrying the same “enable feature” command with the same parameters may be treated as idempotent.
- Re‑processing a “decrement balance by X” event may not be idempotent unless carefully designed.

Strategies for handling duplicates:

- Stable operation identifiers within messages.
- Deduplication caches or logs per entity.
- Version checks and explicit conflict resolution.

---

## 8. Error handling in lifecycles

When a message cannot be applied to an entity due to lifecycle violations (e.g. wrong phase, conflicting update), the system SHOULD:

- Reject the message, and
- Optionally emit an `Error` message or equivalent diagnostic record, correlated via `correlation_id` where appropriate.

Examples of lifecycle‑related errors:

- Attempt to update a non‑existent entity.
- Attempt to modify an entity in a forbidden phase (e.g. terminated).
- Version or sequence mismatch under optimistic concurrency.

The exact error catalog is domain‑specific but SHOULD be documented and applied consistently.

---

## 9. Multi‑entity workflows

Many real‑world processes involve multiple entities (e.g. an order referencing multiple devices, or a contract spanning several accounts).

Axis Protocol does not prescribe a specific workflow engine, but recommends:

- Explicit modeling of relationships between entities in messages.
- Clear rules for atomicity or lack thereof (e.g. can partial success occur?).
- Well‑defined compensation patterns where full rollback is not possible.

Lifecycle rules for multi‑entity operations SHOULD specify:

- Which entities must exist and in what phases.
- How partial failures impact overall workflow state.

---

## 10. Relationship to implementations

- **Axis Protocol** defines:
  - how entities are referenced in messages (`domain`, `entity_type`, `entity_id`),
  - general expectations around lifecycles and state transitions,
  - the separation between protocol‑level invariants and domain‑specific lifecycles.

- **Implementations and domain specifications** define:
  - concrete entity lifecycle diagrams and allowed transitions,
  - message schemas that drive those transitions,
  - storage models, indexing strategies and access control.

An implementation that claims conformance with Axis Protocol SHOULD:

- Provide a clear mapping from Axis messages to entity lifecycle transitions.
- Enforce lifecycle rules consistently at validation and execution time.
- Document domain‑specific lifecycle states, allowed transitions, and error conditions.

Where this document is abstract, domain authors are expected to refine and specialize these patterns for their use cases, without contradicting the general expectations described here.
