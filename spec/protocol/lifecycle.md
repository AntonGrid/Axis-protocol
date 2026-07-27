
Axis Protocol — Lifecycle and State Transitions
This document describes the lifecycle of Axis Records and Claims: how they are created, evolved, superseded and revoked.

The goal is to provide a transport‑ and chain‑agnostic model that can be mapped to different execution environments (blockchains, off‑chain services, hybrid setups).

1. High‑level lifecycle
At a high level, a Record goes through the following conceptual stages:

Draft — constructed by an issuer but not yet signed or published.
Signed — carries one or more valid signatures from Actors.
Published — made available to other participants (e.g. via a blockchain, message bus, or API).
Validated — accepted or rejected by validators according to validation.md.
Evolved — may be superseded or complemented by later Records.
Finalized (optional) — domain‑specific notion of completion (e.g. settlement, closure, retirement).
The protocol itself only standardizes the representation and semantics of these transitions at the Record level, not the transport or execution mechanics.

Profiles MAY introduce additional lifecycle stages, but MUST NOT contradict the core stages above.

2. Creation
2.1 Drafting
An issuer constructs a draft Record:

fills in the header (version, namespace, issuer, timestamp, etc.);
adds Claims in the body;
optionally references policies or profiles (e.g. by namespace or explicit profile ID).
At this stage:

record_id is not yet final (because signatures may depend on it, and it depends on the canonical form),
the Record is not yet visible to other participants.
2.2 Signing and record ID
A typical flow:

Serialize the draft Record (without record_id) into canonical form.
Compute the hash and derive the Record ID (see wire-format.md).
Add record_id to the header.
Serialize again in canonical form (now including record_id).
Sign this canonical byte sequence and attach signatures.
Implementations MAY optimize this process, as long as the final state satisfies:

record_id equals the hash of the Record (with record_id field) according to the chosen scheme;
signatures cover the final canonical representation;
the canonicalization rules in the wire format spec are respected.
3. Publication
The protocol does not mandate a specific publication mechanism. Common patterns:

On‑chain:
The Record (or its hash plus a pointer) is embedded in a blockchain transaction.
Off‑chain with anchoring:
Full Records live in a distributed storage or API; hashes or commitments are anchored on‑chain.
Pure off‑chain:
Records are exchanged via messaging systems or APIs without any blockchain involvement.
Normative:

L-001: Whatever the publication mechanism, it MUST NOT alter the canonical content of the Record.
L-002: Implementations SHOULD provide a way to retrieve the full Record given its record_id (directly or via an index/registry).
L-003: If publication includes only a hash or commitment, the mapping from record_id to the stored content MUST be well‑defined and verifiable.
4. Evolution, supersession and revocation
Axis is fundamentally append‑only at the Record level: existing Records are never modified or deleted; instead, new Records change how previous ones are interpreted.

4.1 Evolution
A Claim or other domain entity may evolve over time via additional Records.

Patterns:

Append‑only enrichment:
New Records append new Claims or metadata; consumers reconstruct state by folding all Records in order.
State updates:
New Records explicitly supersede or update previous ones for a given entity or claim type.
Policy‑driven evolution:
Policies or profiles describe how certain claim types interact across Records (e.g. accumulating measurements, updating attributes).
Normative:

L-010: Profiles that define evolving entities MUST specify how to interpret sequences of Records affecting the same identifier(s).
L-011: Implementations MUST NOT mutate already published Records; evolution MUST be expressed via new Records.
4.2 Supersession
Supersession expresses that a new Record replaces some aspect of one or more previous Records.

Normative:

L-020: A Record that supersedes another SHOULD:
reference the superseded record_id (or multiple IDs) in a well‑defined field or claim; and
clearly indicate the scope of supersession (e.g. specific claims vs. entire Record).
L-021: Profiles MUST define:
whether supersession is allowed for their entities/claims;
who is authorized to issue superseding Records (e.g. only the original issuer, current holder, or a designated authority);
how to resolve conflicting or chained supersessions.
4.3 Revocation
Revocation expresses that a previously accepted Record or Claim is no longer considered valid for future evaluations.

Normative:

L-030: A revocation Record MUST:
reference the record_id (or claim identifier) it revokes;
be authorized according to profile/policy (e.g. issuer, authority, or governance entity);
be validated like any other Record.
L-031: Effects of revocation are semantic, not mechanical:
Validators and consumers MUST treat revoked content as invalid from the revocation point onward, according to the policy definition.
Historical truth is preserved: the original Record still exists, but its status changes.
Profiles SHOULD define:

how revocation interacts with supersession and expiration;
whether revocation is reversible or itself revocable.
5. Expiration
Claims may have explicit or implicit expiration:

explicit time bounds (e.g. valid_from / valid_until);
profile‑ or policy‑driven timeouts (e.g. “claims older than 1 year are no longer trusted”).
Normative:

L-040: When evaluating a Record at time T, validators MUST consider expiration rules defined by the active profiles/policies.
L-041: Profiles SHOULD specify whether expired content:
is treated equivalently to revoked content, or
remains valid for some limited use cases (e.g. historical reporting).
6. Views and state reconstruction
Because Axis is record‑based, any notion of “current state” is derived from a set of accepted Records under a given policy context.

A view is the result of applying:

all accepted Records (or a defined subset),
under a given profile/policy set,
at a given evaluation time T.
Different implementations may maintain views:

in memory (for online validation),
in databases (materialized state),
implicitly (recomputed on demand from the Record log).
The protocol does not constrain how views are stored; it only constrains:

how Records are represented,
how they can be interpreted in a way that is consistent across implementations using the same profiles.
Normative:

L-050: Profiles MUST define how to derive their domain‑specific views from sequences of Records (e.g. ordering, conflict resolution).
L-051: Implementations that expose views to clients SHOULD document:
which policies/profiles are applied,
which Records are included or excluded (e.g. revoked or expired).
7. Mapping to implementations
While the protocol is transport‑ and chain‑agnostic, typical mappings include:

Smart‑contract implementation:

Each Record is a transaction payload or event;
Contract code enforces a subset of structural and semantic validation rules;
Off‑chain services may perform richer policy evaluation, cross‑Record analysis, and view materialization.
Off‑chain service:

Records are submitted via an API;
The service stores them in a database and exposes views and query APIs;
Optional anchoring to a blockchain (or other audit log) for integrity and timestamping.
Hybrid setups:

Critical invariants are enforced on‑chain or in a consensus system;
Non‑critical or high‑volume logic is handled off‑chain, still using Axis Records and profiles.
Normative:

L-060: Profiles and concrete implementations MUST document:
how lifecycle stages map to their execution environment;
which parts of validation are enforced in which layer (on‑chain / off‑chain / other);
how anchoring, discovery, and retrieval of Records work in practice.
L-061: Implementations that claim conformance to Axis Protocol MUST at least:
preserve the canonical Record content end‑to‑end,
respect the lifecycle semantics defined in this document,
document any additional lifecycle rules they introduce.
