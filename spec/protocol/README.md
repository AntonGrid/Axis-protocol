# Axis Core Protocol

This section defines the **core Axis protocol**. It is **normative**: any
implementation that claims compliance with Axis MUST follow the rules defined
here, unless explicitly stated otherwise.

The core protocol is described in several layers:

- **Conceptual model**  
  The main entities, roles and interactions in Axis: participants, attestations,
  claims, proofs and ledgers.

- **Wire format and messages**  
  How protocol objects are serialized on the wire: message types, fields,
  canonical encoding and versioning.

- **Validation rules and invariants**  
  What makes a protocol object valid, which checks MUST be performed and
  which MAY be relaxed in specific environments.

- **Lifecycle**  
  How protocol objects are created, updated, revoked and archived over time.

---

## Structure of this section

The `spec/protocol/` directory is expected to contain the following documents:

- `model.md` – conceptual and data model
- `wire-format.md` – wire format and message definitions
- `validation.md` – validation rules and invariants
- `lifecycle.md` – lifecycle of protocol objects and interactions

Additional documents may be added as the protocol evolves (for example,
`threat-model.md`, `privacy.md`, or `conformance.md`).

---

## Versioning

The Axis protocol is versioned independently from particular implementations
(such as Axis Core).

- Each **stable version** of the protocol MUST be tagged in this repository
  (for example, `v0.1.0-protocol`).
- Implementations MUST declare which protocol version they implement.
- Backwards‑incompatible changes to the protocol MUST result in a new
  **major** or **minor** protocol version.

Until the first stable release, the protocol is considered **experimental**
and MAY change between minor revisions.

---

## Reading order

If you are new to Axis and want to implement it:

1. Start with `docs/overview.md` and `docs/Axis-One-Pager.md`.
2. Read `spec/overview.md` to understand the structure of the specification.
3. Then follow this order within `spec/protocol/`:
   - `model.md`
   - `wire-format.md`
   - `validation.md`
   - `lifecycle.md`

After that, consult `spec/registry/` and `spec/api/` for concrete registries
and external APIs.
