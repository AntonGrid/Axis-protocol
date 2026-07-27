# Axis Protocol — Lifecycle and State Transitions

This document describes the **lifecycle** of Axis Records and Claims: how they are created, evolved, superseded and revoked.

The goal is to provide a chain‑agnostic model that can be mapped to different execution environments (blockchains, off‑chain services, hybrid setups).

---

## 1. High‑level lifecycle

At a high level, a Record goes through the following conceptual stages:

1. **Draft** — constructed by an issuer but not yet signed or published.
2. **Signed** — carries one or more valid signatures from Actors.
3. **Published** — made available to other participants (e.g. via a blockchain, message bus, or API).
4. **Validated** — accepted or rejected by validators according to `validation.md`.
5. **Evolved** — may be superseded or complemented by later Records.
6. **Finalized** (optional) — domain‑specific notion of completion (e.g. settlement, closure).

The protocol itself only standardizes the *representation* of these transitions, not the transport or execution mechanics.

---

## 2. Creation

### 2.1 Drafting

An issuer constructs a draft Record:

- fills in the `header` (version, namespace, issuer, timestamp, etc.);
- adds Claims in the `body`;
- optionally references policies or profiles.

At this stage:

- `record_id` is not yet final (because signatures may depend on it, and it depends on the canonical form).

### 2.2 Signing and record ID

The typical flow:

1. Serialize the draft Record (without `record_id`) into canonical form.
2. Compute the hash and derive the **Record ID** (see `wire-format.md`).
3. Add `record_id` to the header.
4. Serialize again in canonical form (now including `record_id`).
5. Sign this canonical byte sequence and attach signatures.

Implementations MAY optimize this process, as long as the final state satisfies:

- `record_id` equals the hash of the Record (with `record_id` field) according to the chosen scheme;
- signatures cover the final canonical representation.

---

## 3. Publication

The protocol does not mandate a specific publication mechanism. Common patterns:

- **On‑chain**:  
  - The Record (or its hash plus a pointer) is embedded in a blockchain transaction.
- **Off‑chain with anchoring**:  
  - Full Records live in a distributed storage or API; hashes or commitments are anchored on‑chain.
- **Pure off‑chain**:  
  - Records are exchanged via messaging systems or APIs without any blockchain involvement.

Normative:

- Whatever the publication mechanism, it MUST NOT alter the canonical content of the Record.
- Implementations SHOULD provide a way to retrieve the full Record given its `record_id`.

---

## 4. Evolution, supersession and revocation

### 4.1 Evolution

A Claim or Asset state may evolve over time via additional Records.

Patterns:

- **Append‑only**:
  - New Records append new Claims; consumers reconstruct state by folding all Records.
- **State updates**:
  - New Records explicitly supersede previous ones for a given asset or claim type.

### 4.2 Supersession

Supersession expresses that a new Record **replaces** some aspect of a previous one.

Normative:

- A Record that supersedes another SHOULD:
  - reference the superseded `record_id` (or multiple IDs);
  - clearly indicate the scope of supersession (e.g. specific claims vs. entire Record).

Policies may define:

- whether supersession is allowed;
- who is authorized to supersede (e.g. only the original issuer or current owner);
- how conflicting supersessions are resolved.

### 4.3 Revocation

Revocation expresses that a previously accepted Record or Claim is no longer considered valid.

Normative:

- A revocation Record MUST:
  - reference the `record_id` (or claim identifier) it revokes;
  - be authorized according to policy (e.g. issuer, authority, or governance entity);
  - be validated like any other Record.

Effects of revocation are semantic, not mechanical:

- Validators and consumers MUST treat revoked content as invalid from the revocation point onward.
- Historical truth is preserved: the original Record still exists, but its status changes.

---

## 5. Expiration

Claims may have explicit or implicit expiration:

- explicit time bounds (`valid_until`);
- policy‑driven timeouts (e.g. “claims older than 1 year are no longer trusted”).

Normative:

- When evaluating a Record at time `T`, validators MUST consider expiration rules defined by the active policies.

---

## 6. Views and state reconstruction

Because Axis is fundamentally **record‑based**, any notion of “current state” is derived:

- A **view** is the result of applying:
  - all accepted Records,
  - under a given policy set,
  - at a given evaluation time.

Different implementations may maintain views:

- in memory (for online validation);
- in databases (materialized state);
- implicitly (recomputed on demand).

The protocol does not constrain how views are stored; it only constrains how Records are interpreted.

---

## 7. Mapping to implementations

While the protocol is chain‑agnostic, typical mappings include:

- **Smart‑contract implementation**:
  - Each Record is a transaction or event;
  - Contract code enforces a subset of validation rules;
  - Off‑chain services may perform richer policy evaluation.

- **Off‑chain service**:
  - Records are submitted via an API;
  - The service stores them in a database and exposes views;
  - Optional anchoring to a blockchain for auditability.

Profiles and implementations MUST document:

- how lifecycle stages map to their execution environment;
- which parts of validation are enforced on‑chain vs. off‑chain;
- how anchoring and retrieval of Records work in practice.
