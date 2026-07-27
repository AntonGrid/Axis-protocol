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

The specific function MUST be declared by the implementation or profile.

Different profiles MAY choose different functions, as long as they are clearly identified.

The choice of hash function is not fixed by the core spec; conformance suites MAY apply stricter requirements.

3.2 Record ID
A Record ID is derived as follows:

Take the canonical byte sequence of the Record without the record_id field (if present).

Compute the hash using the chosen hash function.

Encode the hash in a standard textual form (e.g. hex, base58, base64url) with an optional prefix.

Example (logical):

text
hash = sha256(canonical_bytes(record_without_record_id))
textual ID: axrec:<base58-of-hash>
Normative:

The record_id field, if present, MUST match the computed identifier for the Record.

If a transport or storage layer assigns additional identifiers, they MUST NOT replace the canonical record_id defined here.

4. References and links
Records and Claims MAY reference:

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
