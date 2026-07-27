
Axis Protocol – Validation Rules
Status: DRAFT

1. Scope
This document defines normative validation rules for the Axis Protocol at the Record level:

structural validity of Records,
invariants over state as reflected in Records,
preconditions for applying Records to a state machine,
consistency rules between related Records.
These rules MUST hold in any conforming implementation, regardless of blockchain, transport, or runtime.
Profiles MAY define additional, stricter rules, but MUST NOT contradict this document.

2. Terminology and Context
Record – canonical Axis Record as defined in the model and wire format specifications.
Validator – any component that checks a Record against the rules in this document (and optional profile rules).
Profile – a domain- or implementation-specific set of additional constraints (see profile documents).
State machine – abstraction of how Records are applied to some domain state (balances, asset lifecycles, etc.). This document does not fix a global state model, but assumes that Records may be interpreted against some state.
3. Structural Validation
Structural validation ensures that a Record is well-formed before any semantic checks.

3.1 JSON / encoding structure
Given a decoded logical representation of the Record:

V-001: The top-level structure MUST be an object with the following fields:
header (object),
body (object),
signatures (array),
optional record_id (string).
V-002: Unknown additional top-level fields MAY be present but MUST NOT change the meaning of the core fields. Profiles MAY forbid or further constrain unknown fields.
3.2 Header
V-010: header MUST be an object.
V-011: header.version MUST be present and be a string that matches a semantic version or other versioning scheme defined by this specification or a profile.
V-012: header.timestamp MUST be present and MUST be an ISO 8601 UTC timestamp string (e.g. YYYY-MM-DDThh:mm:ssZ).
V-013: header.issuer MUST be present and MUST be a stable identifier (e.g. DID, key ID, or other profile-defined scheme).
V-014: header.namespace MUST be present and MUST be a namespaced identifier (e.g. URI or URN) that indicates which profile or logical namespace this Record belongs to.
V-015: Profiles MAY require additional header fields (e.g. profile_id) and MAY define stricter formats for issuer and namespace.
3.3 Body
V-020: body MUST be an object.
V-021: body.claims MUST be present and MUST be a non-empty array.
V-022: Each element of body.claims MUST be an object with at least:
claim_type (string) – namespaced identifier of the claim semantics,
payload (object) – claim-specific data.
V-023: Profiles MAY define additional required fields for claims (e.g. asset_id, subject, etc.) and additional constraints on payload.
3.4 Signatures
V-030: signatures MUST be a non-empty array.
V-031: Each signature entry MUST be an object with at least:
alg (string) – signature algorithm identifier,
kid (string) – key identifier or reference,
sig (string) – signature value (encoding defined by profile or algorithm registry).
V-032: Profiles MAY define additional fields (e.g. nonce, scope, protected_header) and MUST specify the exact signature scheme and encoding.
3.5 Record ID
V-040: If record_id is present, it MUST be a string and MUST conform to the Record ID format (see wire format and hashing rules).
V-041: If record_id is present, it MUST match the hash computed from the canonical form of the Record with record_id logically removed.
4. Canonicalization and Hash Validation
Given the canonical serialization rules from the wire format specification:

V-050: A validator MUST be able to reconstruct the canonical byte sequence of the Record from its logical representation.
V-051: A validator MUST recompute the hash of the Record from the canonical byte sequence and:
if record_id is present, verify that it matches;
if record_id is absent, it MAY derive the canonical identifier but MUST NOT modify the Record in place.
V-052: If the computed identifier does not match the declared record_id, the Record MUST be rejected with a ValidationError:RecordIdMismatch (or equivalent code defined by the implementation/profile).
5. Signature Validation
Signature validation is algorithm- and profile-dependent but MUST satisfy the following generic rules:

V-060: Validators MUST verify at least one signature that they trust as sufficient for the Record’s declared semantics (e.g. issuer authorization).
V-061: The signed payload MUST be the canonical encoding of the Record, or a precisely defined subset of it, as specified by the signature scheme/profile.
V-062: If no valid signature can be established according to the rules of the active profile, the Record MUST be rejected with a ValidationError:InvalidSignature (or equivalent).
V-063: Validators MAY support multiple algorithms (alg values), but a profile MAY restrict this set.
6. Semantic Validation and Invariants
Semantic validation depends on how Records map to domain state. This specification defines generic patterns; profiles MUST define actual invariants for their domain.

6.1 Generic invariant format
Each invariant SHOULD have:

a unique identifier (e.g. I-001, I-002, …),
a short description,
the set of entities or claim types it applies to,
the condition expressed in terms of:
the current Record,
optionally previously accepted Records and/or state.
6.2 Examples (illustrative, non-normative)
These examples describe the style of invariants; concrete invariants belong in profiles:

I-001 (Non-negative quantity): For any claim that reports a quantitative amount, if the profile defines a field as a quantity (e.g. quantity_wh), its value MUST be greater than or equal to zero.
I-002 (Monotonic interval ordering): For any claim defining a time interval, the from timestamp MUST be strictly less than the to timestamp.
I-003 (No modification after finalization): If a profile defines a terminal or finalized state for an entity (e.g. Retired), then any Record that would modify that entity after it reaches its terminal state MUST be rejected.
Profiles SHOULD publish their invariants using this pattern, referencing claim types and fields by their namespaced identifiers.

7. Operation Preconditions
If an implementation interprets Records as operations on a state machine, it MUST define operation preconditions. This core spec defines the structure of such preconditions; profiles/implementations define the specific rules.

For each logical operation (e.g. “create asset”, “update attribute”, “record measurement”), define:

Inputs:
which claim types and fields are required,
acceptable ranges or formats.
Authorization:
which issuers or keys are allowed to emit such Records,
how authorization is derived from signatures and header fields.
State preconditions:
what must hold in the current state before the Record can be applied (e.g. “asset exists”, “not retired”, “no overlapping interval”).
Effects:
how the accepted Record changes the state (out of scope for this core document, but referenced by profiles).
Normative:

V-070: Profiles that define operations MUST specify their preconditions in a way that can be evaluated from:
the Record contents, and
the state accessible to the validator.
V-071: If any mandatory precondition fails, the Record MUST be rejected with an appropriate validation error.
8. Consistency Between Related Records
When Records reference each other or share identifiers (assets, subjects, policies), validators MAY perform additional consistency checks.

Normative:

V-080: If a Record references another Record by record_id, and the referenced Record is available, validators MUST check that:
the reference uses the canonical record_id,
the referenced Record itself passes validation.
V-081: If the reference is broken (missing or invalid), profiles MUST specify whether:
the Record MUST be rejected, or
the Record MAY be accepted with a weaker trust level or different status.
V-082: Profiles MAY define further cross-Record consistency rules (e.g. “no overlapping intervals for the same asset and metric”).
9. Error Model
Implementations MUST define a clear error model so that clients can distinguish different classes of validation failures.

9.1 Categories
At minimum, the following categories SHOULD be distinguished:

ValidationError.Structure – structural problems (missing fields, wrong types, invalid formats).
ValidationError.Canonicalization – canonicalization or record_id mismatches.
ValidationError.Signature – invalid or missing required signatures.
ValidationError.Semantics – violation of semantic invariants or profile rules.
ValidationError.StatePrecondition – violation of state preconditions when applying the Record.
AuthError – failures related specifically to authorization policies (if separated from signature validity).
StateConflict – conflicts with existing state or Records (e.g. double-spend-like conditions).
Profiles MAY extend this taxonomy with more fine-grained codes.

9.2 Representation
Implementations SHOULD expose errors to clients via:

a machine-readable code (string or numeric),
a human-readable message (for debugging and logging),
optional context (e.g. field path, offending value, related identifiers).
Normative:

V-090: For all normative checks in this document, implementations MUST map failures to at least one error category and expose it in their API or logs.
V-091: Profiles MAY declare some errors as “fatal” (Record MUST NOT be accepted under any circumstances) and others as “soft” (Record MAY be accepted with warnings or reduced trust), but such distinctions MUST be clearly documented.
10. Extensibility
The validation model is designed to be extensible:

New fields and claim types MAY introduce new validation rules.
Profiles MAY:
add new invariants,
tighten structural requirements (e.g. forbid unknown fields),
define domain-specific error codes.
Constraints:

Profile-specific rules MUST NOT contradict the core structural, canonicalization, and basic signature rules defined in this document.
Unknown validation rules (from profiles a validator does not implement) MUST NOT silently turn an otherwise-invalid Record into a valid one; validators SHOULD either:
treat the Record as invalid, or
mark it as “unvalidated under profile X” and handle accordingly.
