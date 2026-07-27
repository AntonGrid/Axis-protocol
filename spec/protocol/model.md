# Axis Protocol — Conceptual Model

This document defines the **abstract data model** of the Axis protocol. It is **implementation‑agnostic** and does not assume any specific blockchain, storage layer, or runtime.

It is **domain‑neutral**: concrete domains (e.g., energy, supply chain, identity) define their own **profiles** and schemas on top of this model.

---

## 1. Core entities

### 1.1 Actor

An **Actor** is any entity that can **issue**, **sign**, or **receive** claims.

Examples:

- a human or legal entity;
- a device or gateway;
- a smart contract or service account.

Normative:

- An Actor MUST be represented by at least one **cryptographic identity** (public key or equivalent).
- Implementations MAY support multiple keys per Actor (rotation, multi‑sig, etc.).
- The concrete identity scheme (PKI, DID, etc.) is outside the scope of this document.

### 1.2 Asset

An **Asset** is something about which claims are made.

Examples:

- a physical object (e.g., a solar panel, a meter, a building);
- a right or obligation (e.g., a production right, a consumption obligation);
- a digital object (e.g., a document, a dataset).

Normative:

- Each Asset MUST have a **stable identifier** within a given namespace (see 1.4).
- The core spec does not constrain the semantics of assets; domains MAY define asset types and schemas in their profiles.

### 1.3 Claim

A **Claim** is a structured statement about an Asset, made by an Actor, optionally under a policy.

Examples:

- “Meter X produced 1 kWh between T1 and T2.”
- “Asset Y is owned by Actor A.”
- “This batch of energy is certified as renewable.”

Normative:

- A Claim MUST:
  - reference **one Asset identifier**;
  - have a **type** (e.g., `"production"`, `"ownership"`, `"certificate"`);
  - specify an **issuer** (Actor identity);
  - MAY reference a **subject** Actor (e.g., owner, beneficiary);
  - carry a **payload** structured according to a schema (domain‑defined);
  - MAY reference a **policy** or profile if special rules apply.

- A Claim MAY:
  - be time‑bounded (`valid_from`, `valid_until`);
  - refer to another Claim (e.g., to supersede or revoke it).

The core spec does not prescribe a single schema language; profiles MAY use JSON Schema, protobuf, or other schema systems as long as they can be mapped to this model and the canonical wire format.

### 1.4 Namespace

A **Namespace** defines a scope for identifiers and types.

Examples (non‑normative):

- `axis://protocol` — built‑in protocol namespace;
- `axis://energy` — a domain‑specific profile for energy assets (outside this core spec);
- `axis://example.com/myapp` — arbitrary domain or application.

Normative:

- Type names, asset identifiers, and policy identifiers MUST be qualified by a namespace or resolved via an agreed lookup mechanism.
- The core spec defines only a minimal set of built‑in names in the `axis://protocol` namespace.
- Domains and applications SHOULD define their own namespaces for types, assets, and policies.

---

## 2. Records and logs

### 2.1 Record

A **Record** is the fundamental unit of data on the wire.

Intuitively, a Record is a **signed envelope** that contains one or more **Claims** plus metadata.

Normative:

- A Record MUST contain:
  - a **header** (see 2.2);
  - a **body** (list of Claims and optional domain data);
  - one or more **signatures** (see 2.3).

- A Record MUST be immutable once created. Any change requires a **new Record** that references the previous one.

- A Record MAY carry additional, domain‑ or application‑specific fields as long as they conform to the canonicalization rules defined in `wire-format.md`.

### 2.2 Record header

The header contains protocol‑level metadata.

A minimal header SHOULD include:

- `version` — Axis protocol version;
- `record_id` — canonical identifier (often derived from the hash of the canonical wire format);
- `timestamp` — creation time (issuer‑defined, not necessarily consensus time);
- `issuer` — Actor identity of the primary signer;
- `prev` — optional link to a previous Record (for chains of Records);
- `namespace` — the primary namespace of the Record payload.

Implementations MAY extend the header with additional fields, provided canonicalization rules are respected (see `wire-format.md`).

### 2.3 Signatures

Signatures bind the Record content to one or more Actors.

Normative:

- Each Record MUST carry at least one **cryptographic signature** covering the canonical wire representation of:
  - the header;
  - the body (including all Claims);
  - any declared extensions included in the signature scope.

- Multiple signatures MAY be attached to support:
  - multi‑party agreements;
  - endorsements;
  - countersignatures by validators or auditors.

The concrete signature scheme (e.g., Ed25519, ECDSA) is **not fixed** by this spec; implementations and bindings MUST declare which schemes they support.

### 2.4 Log

A **Log** is an ordered collection of Records related by references.

Examples:

- a per‑asset log (all Records concerning a given asset);
- a per‑actor log (all Records issued by a given actor);
- a chain‑level log (ordering imposed by a blockchain).

The protocol does not prescribe a single global log; it defines how Records relate. Implementations are free to:

- embed Records directly on a blockchain;
- store them off‑chain with cryptographic anchoring;
- combine both approaches.

Bindings to specific chains or ledgers (ordering, inclusion proofs, etc.) are defined outside this document.

---

## 3. Policies and profiles

### 3.1 Policy

A **Policy** is a machine‑readable set of rules that govern:

- which Claims are valid;
- under which conditions;
- how conflicts are resolved.

Policy examples:

- “Only a certified meter can issue `production` claims.”
- “Ownership can only be transferred by the current owner.”

Normative:

- Records and Claims MAY reference a Policy identifier.
- Policy semantics are defined in `validation.md`.
- The core spec does not fix a single policy language; it defines a minimal interface:
  - input: Record(s) + context;
  - output: decision (`valid` / `invalid` / `indeterminate`) plus optional reasons.

Concrete policy languages and execution environments MAY be specified in separate profile or binding documents.

### 3.2 Profile

A **Profile** is a named subset or extension of the Axis protocol tailored for a domain or application.

Examples:

- a profile for energy certificates;
- a supply‑chain profile for product tracking;
- an identity profile for KYC / credential use cases.

Profiles:

- define additional Claim types and schemas;
- may constrain which parts of the core model are allowed or mandatory;
- should remain compatible with the core model and wire format;
- MUST live outside the core spec directory (e.g., in `docs/` or in separate repositories).

---

## 4. Identity and addressing

The Axis model assumes:

- **cryptographic identities** for Actors;
- **content‑addressable identifiers** for Records (typically hashes over canonical wire format);
- **stable logical identifiers** for Assets (which may be mapped to different chains or databases).

Normative:

- Implementations and bindings MUST specify:
  - which identity schemes they support (e.g., X.509, DID methods);
  - how Record identifiers are computed;
  - how Asset identifiers are constructed and resolved within their namespaces.

Details of key management, PKI, DID integration, wallet UX, on‑chain account management, and similar operational concerns are **outside the core model** and may be defined in separate documents or implementations.
