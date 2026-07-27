# Axis Protocol — Wire Format

This document specifies how Axis Records are **serialized**, **hashed** and **addressed** on the wire.

Goal: the same logical Record must have a **unique canonical representation** and therefore a **stable hash** across implementations.

> NOTE: This is a draft; concrete encoding choices (e.g. JSON vs CBOR) are subject to change as long as the canonicalization rules remain well‑defined.

---

## 1. Canonical representation

### 1.1 Requirements

A canonical representation MUST:

- be **unambiguous** (no two different byte sequences for the same logical Record);
- be **deterministic** (independent of field ordering at the API level);
- be **portable** across languages and platforms.

### 1.2 Encoding

Axis defines a logical JSON‑like structure, but the canonical on‑wire encoding MAY be:

- JSON with strict canonicalization rules; or
- CBOR with deterministic encoding; or
- another self‑describing structured format with deterministic rules.

Normative (for this draft):

- Implementations MUST choose one canonical encoding and document it.
- All hash calculations and signatures MUST use this canonical encoding.
- If multiple encodings are supported for transport, they MUST be losslessly convertible to/from the canonical form.

> A future version of the spec may fix a single mandatory canonical encoding for interoperability test suites.

---

## 2. Canonical JSON (draft baseline)

This section defines a **baseline canonical JSON representation** suitable for early implementations and tests.

### 2.1 Object ordering

- JSON objects MUST have their keys sorted in **lexicographic order**.
- No duplicate keys are allowed.

### 2.2 Numbers

- Integer values MUST be encoded without leading zeros (except zero itself).
- Floating‑point values SHOULD be avoided in canonical data where possible. If used:
  - they MUST be encoded in a normalized decimal representation without trailing zeros, or
  - implementations MAY agree on IEEE‑754 binary representation wrapped in a string.

Domain profiles SHOULD prefer integer or fixed‑point representations for quantities.

### 2.3 Strings and encoding

- Strings MUST be valid UTF‑8.
- Control characters MUST be escaped using standard JSON escapes.
- No insignificant whitespace is allowed outside strings.

### 2.4 Example record (logical)

```json
{
  "header": {
    "issuer": "did:example:issuer1",
    "namespace": "axis://protocol",
    "timestamp": "2025-01-01T00:00:00Z",
    "version": "0.1.0"
  },
  "body": {
    "claims": [
      {
        "asset_id": "asset:example:meter-1",
        "claim_type": "axis://protocol/production",
        "payload": {
          "quantity_wh": 1000,
          "interval": {
            "from": "2025-01-01T00:00:00Z",
            "to": "2025-01-01T01:00:00Z"
          }
        }
      }
    ]
  },
  "signatures": [
    {
      "alg": "Ed25519",
      "kid": "did:example:issuer1#key-1",
      "sig": "<base64-signature>"
    }
  ]
}
The canonical byte sequence is obtained by serializing this structure using the canonical JSON rules above.

3. Hashing and record identifiers
3.1 Hash function
Implementations MUST use a cryptographic hash function (e.g. SHA‑256 or BLAKE3) for record identifiers.
The specific function MUST be declared by the implementation and MAY be part of the profile.
3.2 Record ID
A Record ID is derived as:

Take the canonical byte sequence of the Record without the record_id field (if present).
Compute the hash using the chosen hash function.
Encode the hash in a standard textual form (e.g. hex, base58, base64url) with an optional prefix.
Example (logical):

hash: sha256(canonical_bytes(record_without_record_id))
textual ID: axrec:<base58-of-hash>
Normative:

The record_id field, if present, MUST match the computed identifier for the Record.
If a transport or storage layer assigns additional identifiers, they MUST NOT replace the canonical record_id defined here.
4. References and links
Records and Claims may reference:

other Records (by record_id);
assets (by asset identifier);
policies or profiles (by namespaced identifiers).
Normative:

References MUST be stable, i.e. they MUST NOT depend on mutable off‑chain database primary keys.
When referencing another Record, the canonical Record ID MUST be used.
5. Extensibility
The wire format is designed to be extensible:

Additional fields MAY be added to:
headers,
claims,
signatures,
policy references.
Constraints:

New fields MUST NOT break canonicalization rules.
Unknown fields MUST be ignored by validators that do not understand them, unless a profile explicitly forbids this.
Profiles MAY:

restrict which fields are allowed;
require certain fields to be present;
define additional canonicalization constraints.
Such constraints MUST NOT contradict the core rules in this document.


---

## 4. `spec/protocol/validation.md`

```md
# Axis Protocol — Validation

This document defines how Axis Records are validated at the **protocol level**.

Validation has three layers:

1. **Structural validation** — is the Record well‑formed?
2. **Cryptographic validation** — are signatures correct?
3. **Semantic validation** — is the content acceptable under the active policies?

---

## 1. Structural validation

Structural validation checks that a Record:

- conforms to the core data model (`model.md`);
- respects the wire‑format rules (`wire-format.md`);
- satisfies minimal required fields.

Normative checks (non‑exhaustive):

- `header` is present and contains:
  - `version` — supported Axis version;
  - `issuer` — non‑empty Actor identifier;
  - `namespace` — non‑empty namespace identifier;
  - `timestamp` — valid timestamp format.
- `body` is present and contains:
  - `claims` array (may be empty depending on profile, but MUST be an array if present).
- `signatures` array is present and non‑empty.
- All identifiers (record IDs, asset IDs, policy IDs) conform to the syntax rules of their namespaces.

If any of these fail, the Record MUST be rejected as **structurally invalid**.

Profiles MAY add further structural constraints (e.g. require certain claim types).

---

## 2. Cryptographic validation

Cryptographic validation ensures that:

- the Record has not been tampered with; and
- it is properly authorized by the relevant Actors.

Normative steps:

1. **Canonicalization**  
   Serialize the Record into its canonical byte sequence (see `wire-format.md`).

2. **Signature scope**  
   Determine which parts of the Record are covered by each signature. At minimum:
   - header,
   - body,
   - any explicitly included extensions.

3. **Key resolution**  
   For each signature:
   - resolve the public key from `kid` (key identifier) or from the Actor identity;
   - ensure the key is appropriate for the declared algorithm.

4. **Verification**  
   Verify each signature over the canonical byte sequence according to the declared algorithm.

Outcome:

- If no valid signatures remain after verification, the Record is **cryptographically invalid**.
- A profile MAY require multiple signatures (e.g. issuer + auditor); in that case all required signatures MUST be valid.

The protocol does not define how keys are managed (PKI, DIDs, etc.); that is left to implementations and profiles.

---

## 3. Semantic validation

Semantic validation checks whether the content of a Record is **acceptable** under a given **policy context**.

Inputs:

- the Record under validation;
- zero or more **prior Records** (history);
- a **policy set** (active policies and profiles);
- optional **external context** (e.g. registry data).

Output:

- decision: `valid`, `invalid` or `indeterminate`;
- optional list of reasons or diagnostics.

### 3.1 Policy reference

Records and Claims MAY reference:

- an explicit Policy identifier;
- a Profile that implies a set of policies.

If no explicit policy is referenced, implementations MAY apply:

- a default policy; or
- a “minimal policy” that only checks core invariants.

### 3.2 Typical semantic checks

Examples (not exhaustive):

- **Authorization**:  
  - Is the issuer allowed to make this kind of Claim about this Asset?
- **Consistency**:  
  - Does this Record contradict previously accepted Records without a proper supersession or revocation?
- **Constraints**:  
  - Are quantities within allowed ranges?
  - Are time intervals valid and non‑overlapping where required?
- **Dependencies**:  
  - Does this Claim depend on another Claim that is missing or invalid?

The exact rules are profile‑specific, but the mechanism is general.

### 3.3 Conflict handling

Policies SHOULD define how to handle conflicts, e.g.:

- First‑writer‑wins vs. last‑writer‑wins;
- explicit supersession (a new Record marks an older one as superseded);
- multi‑party consensus (multiple signatures required).

The core spec only requires that:

- conflicts MUST NOT be silently ignored;
- validators MUST be able to classify conflicting Records (e.g. “both valid but incompatible”, “new one invalid because it breaks rule X”).

---

## 4. Validation states

An implementation MAY maintain validation state for Records:

- `pending` — received but not yet fully validated;
- `invalid` — structurally or cryptographically invalid, or rejected by policy;
- `accepted` — successfully validated under the current policy set;
- `superseded` — accepted in the past, but superseded by a newer Record;
- `revoked` — explicitly revoked by an authorized Record.

The protocol does not prescribe storage details; these states are conceptual.

---

## 5. Versioning and compatibility

Validators MUST be aware of the Axis protocol version of each Record.

- If a Record uses a **newer major version** than the validator supports, the validator SHOULD:
  - reject it, or
  - mark it as `indeterminate`, depending on policy.

- If a Record uses a **newer minor version**:
  - unknown fields MUST be ignored unless a policy forbids this;
  - the Record MAY still be considered valid if it passes all known checks.

Profiles MUST document:

- which Axis versions they support;
- whether they allow forward‑compatible unknown fields.
