# Axis Protocol – Validation Specification

This document defines the validation rules for Axis Protocol messages and related entities.  
It is **implementation‑neutral**: it specifies *what* must be validated, not *how* specific runtimes (such as Axis Core or other systems) implement these checks.

Validation is split into layers:

1. **Structural validation** – correctness of the wire format and basic fields.
2. **Semantic validation** – correctness of message content with respect to protocol rules.
3. **State‑dependent validation** – correctness relative to current system state and configuration.

---

## 1. Objectives

Validation in Axis Protocol aims to ensure that:

- Messages are **well‑formed** and **unambiguous**.
- Protocol invariants are upheld across implementations.
- Invalid or malicious inputs are detected early and rejected deterministically.
- Different implementations make **consistent decisions** on the same input.

---

## 2. Validation layers

### 2.1. Structural validation (wire‑level)

Structural validation operates directly on the binary message envelope (see `wire-format.md`).

An implementation MUST perform structural validation **before** attempting semantic or state‑dependent validation.

At minimum, structural validation includes:

1. **Envelope integrity**
   - `envelope_version` is supported.
   - The message length is within allowed bounds.
   - The envelope can be fully parsed without overruns or truncated fields.

2. **Header integrity**
   - `message_type` has a defined numeric value (either base or documented extension).
   - `message_version` is present and properly encoded.
   - Required identifiers (`domain`, `entity_type`, `entity_id`) are present and syntactically valid according to the chosen encoding.
   - `timestamp` is present and correctly encoded.

3. **Payload structure**
   - The payload is parsable according to the encoding rules for the claimed `message_type` and `message_version`.
   - All required fields for the specific message schema are present.
   - Optional fields (if present) comply with encoding rules.

If structural validation fails, the message MUST be rejected.  
Implementations MAY emit a protocol‑level `Error` message if appropriate for their environment.

---

### 2.2. Semantic validation (message‑level)

Semantic validation checks that a structurally valid message is **meaningful** and **internally consistent** according to the Axis Protocol rules and the specific domain schemas.

Semantic validation typically includes:

- Field‑level constraints (ranges, formats).
- Cross‑field constraints within the same message.
- Domain‑specific syntactic validity (e.g. formats of external identifiers if they are treated as non‑opaque).

Each deployment MUST define semantic validation rules for its domains and message schemas, but the following patterns are recommended.

#### 2.2.1. Identifier semantics

While identifiers are opaque at the raw wire level, many deployments will impose semantic requirements, such as:

- `domain` MUST correspond to a configured domain.
- `entity_type` MUST be declared within the given `domain`.
- `entity_id` format MUST conform to the rules of that `entity_type` (e.g. length, allowed characters).

If a deployment defines these constraints, they MUST be enforced consistently across all components that accept Axis messages.

#### 2.2.2. Timestamp semantics

Recommended checks:

- `timestamp` MUST be within a configured acceptable skew relative to the local time source (if the deployment chooses to enforce freshness).
- `timestamp` MUST not be earlier than a configured minimum epoch for the deployment if such a policy exists.

Axis Protocol does not fix global time policies; such rules are deployment‑specific.

#### 2.2.3. Message‑type‑specific semantics

Examples of semantic checks (non‑exhaustive, illustrative only):

- **Command**
  - Required command parameters are present and valid.
  - The command is allowed for the given `entity_type`.

- **Event**
  - Represents a coherent state change or fact.
  - Contains references (if any) that are syntactically valid (e.g. correlation to a prior command ID, if that is part of the domain model).

- **Query / QueryResponse**
  - A `QueryResponse` refers to a known `correlation_id` belonging to a `Query`, according to deployment policies.
  - The response data type matches the query’s expected schema.

- **Error**
  - The error code is part of a defined error catalog for the deployment.
  - If present, `correlation_id` refers to a previous request in a way that makes sense in the specific system.

The exact validation rules for each concrete message schema are part of the domain specification that builds on top of Axis Protocol.

---

### 2.3. State‑dependent validation

State‑dependent validation uses additional context about current system state or configuration.  
This layer is inherently deployment‑specific, but Axis Protocol defines some common patterns and expectations.

Typical examples:

- **Existence checks**
  - `entity_id` MUST refer to an entity that exists (for commands/events that require a pre‑existing entity).
- **Versioning / concurrency control**
  - Messages may carry entity version or revision numbers; these MUST match the current known state if optimistic concurrency is enforced.
- **Authorization / ownership**
  - A message may carry or be associated with an `owner_id` or other authorization context.
  - The sender MUST be authorized to perform the operation on the specified entity.

Axis Protocol itself does not prescribe a specific access‑control or ownership model, but it expects that deployments define and enforce such models consistently.

---

## 3. Protocol‑level invariants

This section describes invariants that should hold across all domains and implementations that claim conformance with Axis Protocol.

### 3.1. Deterministic outcomes

Given:

- the same input message bytes,
- the same configured protocol and domain versions,
- and the same initial system state,

two conforming Axis implementations MUST:

- either both accept or both reject the message, and
- if accepted, produce logically equivalent outcomes (events, state transitions, or responses) according to the shared domain specification.

### 3.2. Idempotence and replay

Axis Protocol does not enforce a particular replay protection strategy, but deployments SHOULD define clear behavior for:

- **Idempotent operations** – commands or messages that can safely be applied multiple times without changing the final result.
- **Non‑idempotent operations** – messages that must not be replayed without explicit intent.

Recommended patterns:

- Use stable identifiers for operations where idempotence is intended, and track whether a given operation ID has been processed.
- Define clear policies for how long replay protection data is retained.

### 3.3. Correlation consistency

If a deployment uses `correlation_id` to link messages (e.g. request‑response, command‑event chains), then:

- `correlation_id` MUST be treated as opaque bytes or string at the wire level.
- Implementations MUST consistently apply their correlation semantics so that:
  - a `QueryResponse` can be reliably matched to its `Query`,
  - an `Error` can be associated with the initial request that caused it, if applicable.

---

## 4. Validation flows

This section describes recommended high‑level flows for message handling.

### 4.1. Inbound message processing

A typical inbound validation pipeline:

1. **Receive raw bytes** from the transport.
2. **Structural validation**
   - Parse envelope and header.
   - Validate envelope version and header fields.
   - Parse payload according to declared schema.
3. **Semantic validation**
   - Apply domain‑specific rules to the parsed message.
4. **State‑dependent validation**
   - Check entity existence, ownership, authorization, concurrency rules, etc.
5. **Decision**
   - If any step fails, reject the message and optionally emit an `Error` or equivalent diagnostic artifact.
   - If all steps pass, proceed to message execution (state transition, query handling, etc.).

Implementations SHOULD ensure that rejected messages cannot cause partial or undefined state changes.

### 4.2. Outbound message generation

Outbound messages (commands, events, responses) MUST also respect validation rules:

1. Construct the logical message in memory (including all required fields).
2. Apply semantic validation locally (before serialization).
3. Serialize to wire format according to `wire-format.md`.
4. Optionally, re‑validate the serialized form structurally (useful in safety‑critical environments).
5. Send over the chosen transport.

This ensures that outbound messages generated by conforming implementations are already valid for receivers.

---

## 5. Domain specifications

Axis Protocol is domain‑agnostic. Each domain that uses Axis Protocol SHOULD provide:

1. **Schema definition**
   - Message schemas for each combination of `domain`, `entity_type`, `message_type`, `message_version`.
   - Field definitions, including types and optionality.

2. **Semantic rules**
   - Allowed value ranges and formats.
   - Relations between fields.
   - Any additional invariants that must hold within a message.

3. **State‑dependent rules**
   - Lifecycle of entities (creation, updates, deletion).
   - Authorization and ownership models.
   - Concurrency and conflict resolution strategies.

4. **Error model**
   - Catalog of error codes and meanings.
   - Mapping from validation failures to error responses (if applicable).

These domain‑level specifications extend this validation document but MUST NOT contradict the core invariants of Axis Protocol.

---

## 6. Relationship to implementations

- **Axis Protocol** defines the abstract validation model and invariants in this document.
- **Implementations** (such as Axis Core or other runtimes) provide:
  - concrete code paths for structural, semantic and state‑dependent validation,
  - integration with storage, transport, authorization systems, and other infrastructure.

An implementation that claims conformance with Axis Protocol MUST:

- Enforce at least the structural validation rules defined here.
- Provide deterministic and consistent behavior for semantic and state‑dependent validation according to its domain specifications.
- Clearly document any deployment‑specific validation policies (e.g. time skew limits, maximum message sizes, authorization rules).

Where this document is silent, implementations are free to define additional validation rules, as long as they do not break interoperability or contradict the protocol‑level invariants.
