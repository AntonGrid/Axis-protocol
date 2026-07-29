# Axis Protocol – Wire Format Specification

This document defines the **on‑wire representation** of Axis Protocol messages.

The wire format is the **carrier of trust** between physical devices and digital systems. It ensures that every message carrying a Proof, Attestation, or Claim is **cryptographically verifiable**, **deterministic**, and **implementation-neutral**.

> Axis Protocol defines *what* is sent over the wire.  
> Concrete implementations define *how* these bytes are produced, transported, and persisted.

---

## 1. Design Goals

The wire format is designed to be:

- **Trust-Carrying** — every message that conveys trust is cryptographically verifiable.
- **Deterministic** — the same logical message always serializes to the same byte sequence.
- **Versioned** — messages are self‑describing and can evolve over time.
- **Binary and Compact** — suitable for constrained networks and devices.
- **Language‑Agnostic** — implementable in any language or runtime.
- **Extensible** — fields and message types can be extended in backward‑compatible ways.

---

## 2. Trust Envelope

Every Axis Protocol message is encoded as a **Trust Envelope**.

The Trust Envelope wraps the message payload and provides:

- **Identity** — who produced the message.
- **Integrity** — the message cannot be modified without detection.
- **Non‑repudiation** — the producer cannot deny having sent the message.

### 2.1 Envelope Structure
+----------------------+----------------------+-----------------------+
| Envelope Header | Message Header | Message Payload |
+----------------------+----------------------+-----------------------+

text

In logical terms:
TrustEnvelope {
envelope_version: u8,
transport_id: TransportId,
correlation_id: CorrelationId,
message_header: MessageHeader,
message_payload: MessagePayload,
signature: Signature, // cryptographic signature over the entire envelope
}

text

### 2.2 Envelope Header

| Field | Type | Description |
| :--- | :--- | :--- |
| `envelope_version` | u8 | Version of the envelope format. |
| `transport_id` | TransportId | Identifies the transport or channel. |
| `correlation_id` | CorrelationId | Opaque identifier for request/response correlation. |

---

## 3. Message Header

The Message Header provides the metadata required to interpret the payload and establish trust context.
MessageHeader {
message_type: MessageType,
message_version: u16,
domain: DomainId,
entity_type: EntityTypeId,
entity_id: EntityId,
timestamp: Timestamp,
issuer_id: IdentityId, // cryptographic identity of the issuer
}

text

| Field | Type | Description |
| :--- | :--- | :--- |
| `message_type` | MessageType | High‑level classification of the message. |
| `message_version` | u16 | Version of the logical message schema. |
| `domain` | DomainId | Application or business domain. |
| `entity_type` | EntityTypeId | Logical type of the entity. |
| `entity_id` | EntityId | Stable identifier of the specific entity. |
| `timestamp` | Timestamp | Time the message was created (UTC). |
| `issuer_id` | IdentityId | Cryptographic identity of the issuer. |

The `issuer_id` is **critical** for trust. It binds the message to a specific cryptographic identity.

---

## 4. Message Types

Axis Protocol defines the following message types:

| Type | Value | Description |
| :--- | :--- | :--- |
| `Proof` | 0x01 | Cryptographic proof of a physical event. |
| `Attestation` | 0x02 | Signed verification of a Proof by a trusted entity. |
| `Claim` | 0x03 | A digital claim backed by an Attestation. |
| `Query` | 0x04 | Request for information. |
| `QueryResponse` | 0x05 | Response to a Query. |
| `Notification` | 0x06 | Out‑of‑band information. |
| `Acknowledgment` | 0x07 | Confirmation of receipt. |
| `Error` | 0x08 | Error indication. |

The **Proof**, **Attestation**, and **Claim** types are the core trust‑carrying messages.

---

## 5. Message Payloads

The payload is defined by the combination of `message_type`, `domain`, `entity_type`, and `message_version`.

### 5.1 Proof Payload

A Proof is the atomic unit of trust from the physical world.
ProofPayload {
device_id: DeviceId,
event_data: EventData,
timestamp: Timestamp,
nonce: Nonce,
signature: Signature, // signed by device private key
}

text

### 5.2 Attestation Payload

An Attestation is a signed verification of a Proof by a trusted entity.
AttestationPayload {
proof_id: ProofId,
decision: Decision, // valid / invalid
oracle_id: IdentityId,
timestamp: Timestamp,
signature: Signature, // signed by oracle private key
}

text

### 5.3 Claim Payload

A Claim is a digital statement backed by an Attestation.
ClaimPayload {
attestation_id: AttestationId,
statement: Statement,
timestamp: Timestamp,
}

text

---

## 6. Primitive Types

This section defines abstract primitive types used throughout the wire format.

| Type | Description | Encoding |
| :--- | :--- | :--- |
| `u8, u16, u32, u64` | Unsigned integers | Fixed‑width, big‑endian |
| `i32, i64` | Signed integers | Fixed‑width, big‑endian |
| `bool` | Boolean | 0x00 = false, 0x01 = true |
| `bytes` | Arbitrary byte sequence | Length (u32) + raw bytes |
| `string` | UTF‑8 text | Length (u32) + UTF‑8 bytes |
| `Timestamp` | UTC timestamp | i64 (seconds since Unix epoch) |
| `Signature` | Cryptographic signature | bytes (algorithm‑specific) |

Identifiers (`DeviceId`, `IdentityId`, `ProofId`, etc.) are represented as `bytes` or `string`.

---

## 7. Framing and Boundaries

Axis Protocol assumes messages are carried by some underlying transport (TCP, message queue, event log, smart contract, etc.).

Two recommended framing strategies:

1. **Length‑Prefixed** — `MessageLength (u32)` + `EnvelopeBytes`
2. **Delimited Records** — message boundaries are defined by the transport.

Each deployment MUST specify which framing strategy is used.

---

## 8. Validation on the Wire

Implementations MUST perform basic validation before accepting a message:

- **Envelope Validation**
  - Check `envelope_version` is supported.
  - Verify structural integrity.
  - Verify `message_type` is known.

- **Header Validation**
  - Ensure required fields are present.
  - Validate `issuer_id` is a known identity.

- **Signature Validation**
  - Verify the signature covers the entire envelope.
  - Verify the signature is valid for the `issuer_id`.

- **Payload Validation**
  - Validate payload conforms to the schema.

---

## 9. Extensibility

The wire format is designed to allow incremental extension:

- **Backward‑Compatible Changes**
  - Adding new message types.
  - Adding new optional fields to payloads.
  - Introducing new domains or entity types.

- **Breaking Changes**
  - Changing meaning or encoding of existing fields.
  - Reusing numeric codes with different semantics.
  - Changing format of identifiers or timestamps.

---

## 10. Relationship to Implementations

Axis Protocol defines the **abstract wire format**. Implementations (e.g., Axis Core) provide concrete encodings, codecs, and transport integrations.

Implementations MUST treat this document as the normative source of truth for on‑wire messages.
