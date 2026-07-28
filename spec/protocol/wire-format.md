# Axis Protocol – Wire Format Specification

This document defines the on‑wire representation of Axis Protocol messages.  
It is intentionally **implementation‑neutral** and does not assume any specific runtime, blockchain, or smart‑contract framework.

> Axis Protocol defines *what* is sent over the wire.  
> Concrete implementations (e.g. Axis Core or other runtimes) define *how* these bytes are produced, transported and persisted.

---

## 1. Design goals

The wire format is designed to be:

- **Deterministic** – the same logical message must always serialize to the same byte sequence.
- **Versioned** – messages are self‑describing and can evolve over time.
- **Binary and compact** – suitable for constrained networks and devices.
- **Language‑agnostic** – implementable in any language/runtime.
- **Extensible** – fields and message types can be extended in backward‑compatible ways.

This specification uses an abstract description of fields and types.  
Concrete encodings (e.g. for integers or byte arrays) are defined in the **Primitive Types** section.

---

## 2. Message envelope

Every Axis Protocol message is encoded as a **Message Envelope**. The envelope wraps a concrete message payload (command, event, query, response, etc.) and provides a consistent framing.

### 2.1. Envelope structure

```text
+----------------------+----------------------+-----------------------+
|  Envelope Header     |  Message Header      |  Message Payload      |
+----------------------+----------------------+-----------------------+
In logical terms:

Envelope {
    envelope_version: u8,
    transport_id: TransportId,
    correlation_id: CorrelationId,
    message_header: MessageHeader,
    message_payload: MessagePayload,
}
Fields:

envelope_version (u8)
Version of the envelope format. This document specifies version 1.

transport_id (TransportId)
Identifies the transport or channel over which the message is carried.
The protocol does not require any particular transport; this field allows implementations to:

multiplex messages over multiple logical channels,
support multiple backends in the same deployment.
correlation_id (CorrelationId)
Opaque identifier used to correlate requests and responses, or link related messages in a workflow.

message_header (MessageHeader)
Describes type, version and basic routing information for the payload.

message_payload (MessagePayload)
Type‑specific body of the message (command, event, query, response, notification, etc.).

Implementations MUST validate that envelope_version is supported before attempting to parse the remainder of the message.

3. Message header
The Message Header provides the minimal metadata required to correctly interpret the payload.

Logical structure:

MessageHeader {
    message_type: MessageType,
    message_version: u16,
    domain: DomainId,
    entity_type: EntityTypeId,
    entity_id: EntityId,
    timestamp: Timestamp,
}
Fields:

message_type (MessageType)
High‑level classification of the message. See Section 4.

message_version (u16)
Version of the logical message schema.
This allows evolution of individual message types without changing the envelope version.

domain (DomainId)
Identifies the application or business domain (e.g. “energy”, “asset‑tracking”, “payments”).
Axis Protocol does not prescribe any fixed domains; values are deployment‑specific.

entity_type (EntityTypeId)
Logical type of the entity the message refers to (e.g. “Device”, “MeterReading”, “Contract”).

entity_id (EntityId)
Stable identifier of the specific entity instance (e.g. device serial number or application‑level ID).

timestamp (Timestamp)
Time at which the message was created, in a deployment‑defined time base (see Primitive Types).

4. Message types
MessageType is an enumeration describing the role of the message in the system.

Recommended base set:

enum MessageType (u8) {
    Command        = 0x01,
    Event          = 0x02,
    Query          = 0x03,
    QueryResponse  = 0x04,
    Notification   = 0x05,
    Acknowledgment = 0x06,
    Error          = 0x07,
    ReservedStart  = 0x80, // implementation-specific extensions >= 0x80
}
Semantics:

Command
Asks the system to perform an action that may change state.

Event
Represents a fact that has already occurred; typically emitted as part of state changes.

Query
Request for information that should not change state.

QueryResponse
Response data for a specific Query (correlated via correlation_id).

Notification
Out‑of‑band information that may be delivered without a corresponding request.

Acknowledgment
Lightweight confirmation that a message has been received and accepted for processing.

Error
Indicates that a previous request could not be processed successfully.

Implementations MAY define additional message types using values in the extension range (>= 0x80), but MUST NOT reuse or redefine base values.

5. Message payloads
The payload is defined by the combination of message_type, domain, entity_type and message_version.
This specification describes the envelope and header; concrete deployments define their own message schemas on top of this structure.

5.1. Namespacing and versioning
Each payload schema SHOULD be uniquely identified by:

domain
entity_type
message_type
message_version
Example logical identity:

(domain = "energy.metering",
 entity_type = "Meter",
 message_type = Command,
 message_version = 1)
Implementations MUST ensure:

A given identity maps to exactly one field layout and encoding.
Message consumers validate message_version and reject unsupported schemas.
5.2. Encoding requirements
Payloads MUST obey:

Deterministic field order
Fields are encoded in a predefined, documented order.

No implicit defaults
If a field is required, it MUST appear in the payload encoding; defaulting is a schema‑level concern.

Explicit optionality
Optional fields SHOULD be encoded using:

a presence bitmap, or
a tagged union / variant type, or
nullable semantics, depending on the chosen primitive encoding.
Forward compatibility

Receivers MUST ignore unknown fields that are explicitly allowed by the encoding scheme (e.g. length‑delimited structures).
New fields are typically added at the end of the field order for a given message_version.
The exact rules for field tagging (if any), length prefixes and variant encodings are defined by the chosen serialization within the guidelines of this wire format (see Primitive Types).

6. Primitive types
This section defines abstract primitive types used throughout the wire format.
Concrete implementations MUST document how these map to their chosen binary encodings.

6.1. Integer types
Recommended logical set:

u8, u16, u32, u64 – unsigned integers.
i32, i64 – signed integers where needed.
Encoding rules:

Implementations MAY choose fixed‑width big‑endian or little‑endian encodings.
Alternatively, variable‑length integer encodings (e.g. LEB128) MAY be used, but MUST be applied consistently within a deployment and documented.
6.2. Boolean
Logical type:

bool – encoded as a single byte (0x00 = false, 0x01 = true) or a packed bit in a bitmap.
The chosen representation MUST be consistent across a deployment.

6.3. Byte arrays
Logical type:

bytes – arbitrary byte sequence.
Encoding:

Length (u32 or varint) + raw bytes
The integer type used for Length MUST be documented for each deployment.

6.4. Text strings
Logical type:

string – UTF‑8 encoded text.
Encoding:

Length (u32 or varint) + UTF-8 bytes
Strings MUST be valid UTF‑8; invalid sequences MUST cause validation failure.

6.5. Identifiers
The following logical identifiers are used in the envelope and header:

TransportId
CorrelationId
DomainId
EntityTypeId
EntityId
Each identifier MAY be represented as:

a string (human‑readable, flexible), or
a bytes value (compact, opaque), or
a fixed‑width integer, as defined by the deployment.
Implementations MUST:

Choose and document a specific representation for each identifier type.
Treat identifiers as opaque at the wire level (no semantic parsing is required by the core protocol).
6.6. Timestamp
Logical type:

Timestamp – a point in time.
Recommended representation:

i64 or u64 counting:
seconds since Unix epoch, or
milliseconds/microseconds since Unix epoch.
The exact epoch and time unit MUST be documented by the deployment.
Timestamps MUST be interpreted in UTC at the protocol level.

7. Framing and boundaries
Axis Protocol assumes that messages are carried by some underlying transport (e.g. TCP, message queue, event log, smart‑contract calls, etc.), but does not prescribe any specific one.

There are two recommended approaches to framing:

Length‑prefixed messages

MessageLength (u32 or varint) + EnvelopeBytes
Simple to implement.
Suitable for stream‑oriented transports.
Delimited records

Messages are stored or transmitted as discrete records.
The record boundary implicitly defines the envelope boundary.
Each deployment MUST specify:

Which framing strategy is used.
The integer type used for MessageLength if applicable.
Any maximum message size limits.
8. Error handling and validation on the wire
Implementations MUST perform basic validation before accepting a message for higher‑level processing:

Envelope validation

Check envelope_version is supported.
Verify message length and structural integrity.
Validate that message_type is known or safely ignorable.
Header validation

Ensure that required header fields are present and correctly typed.
Validate that message_version is supported for the given domain, entity_type and message_type.
Payload validation (structural)

Validate that the payload conforms to the encoding rules for the specific schema.
Deep semantic validation rules are defined in the validation layer, not the wire format.
On validation failure, implementations SHOULD:

Reject the message, and
Optionally emit an Error message correlated to the original correlation_id, if that is meaningful for the transport and application.
9. Extensibility
Axis Protocol wire format is designed to allow incremental extension without breaking existing deployments.

9.1. Backward‑compatible changes
The following changes are generally considered backward‑compatible when carefully applied:

Adding new message types in the extension range (>= 0x80).
Adding new optional fields to payloads in a way that older decoders can ignore.
Introducing new domains or entity types.
9.2. Breaking changes
The following changes are breaking and MUST NOT be introduced without coordination and versioning:

Changing the meaning or encoding of existing fields.
Reusing numeric codes for MessageType with different semantics.
Changing the format of identifiers or timestamps without versioning.
When breaking changes are unavoidable, they MUST be accompanied by:

A new envelope_version, or
A new message_version for the affected messages, or
A new domain/entity namespace, as appropriate.
10. Relationship to implementations
Axis Protocol defines the abstract wire format described in this document.
Axis Core (or other runtimes) MAY provide:
concrete binary encodings for all primitive types,
code libraries for serialization/deserialization,
integration with specific transports or ledgers.
Implementations MUST treat this document as the normative source of truth for the structure of on‑wire messages.
Any implementation‑specific optimizations or shortcuts MUST remain compatible with this specification.
