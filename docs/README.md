# Axis Protocol Documentation

This `docs/` tree describes the **Axis Protocol** – an abstract, chain‑agnostic protocol for representing and exchanging attestable events, manifests, and capabilities.

It is intentionally separated from any concrete product or deployment (such as **ENRG**).
Project‑specific and product‑specific materials should live in their own repositories (e.g. [`ENRG`](https://github.com/AntonGrid/ENRG)).

---

## 1. Protocol‑level documentation

Core, protocol‑level documentation that should remain chain‑ and product‑agnostic:

- `protocol/`
  - `README.md` – entry point into the protocol documentation from the `docs/` side
    (narrative overview, links to the formal spec under `spec/`, examples, FAQs, etc.).

- `registry/`
  - `Event_Registry.md` – event types and semantics.
  - `Manifest_Registry.md` – manifest structure and registry.
  - `Capability_Registry.md` – capabilities and their classification.
  - `Error_Registry.md` – protocol‑level error catalogue.
  - `manifest-registry-openapi.yaml` – OpenAPI definition for a manifest registry API.
  - `README.md` – overview of the registry layer.

- `platform/`
  - `device-lifecycle.md` – abstract device lifecycle model.
  - `provisioning.md` – provisioning / onboarding flow.

  These documents are being made **chain‑agnostic** and are intended to describe behavior at the protocol level (not a specific blockchain or product).

- `merkle-proof-verification.md`  
  – Merkle tree / proof verification model used by the protocol.

- `onchain-attestation.md`  
  – On‑chain attestation model and how attestations are represented and verified within Axis.

- `specifications/`
  - `README.md` – placeholder/index for higher‑level specifications that complement the formal `spec/` tree (profiles, registries, best‑practice docs, etc.).

---

## 2. Governance and ADRs

Documents that describe how the protocol evolves and why certain design decisions were made.

- `Axis-Governance-and-ADR.md`  
  – overview of governance processes, ADR process, and how changes to the protocol are managed.

- `adr/`
  - `0002-device-identity-and-registry.md`
  - `0002-part2-architecture.md`
  - `adr-0002-device-architecture-and-trust-model.md`

  These ADRs capture decisions around device identity, registry, and trust model.  
  When they mention specific implementations (e.g. a particular chain or product), the intent is to refactor them into:
  - **protocol‑level parts**, which stay in this repository;
  - **implementation‑specific parts**, which move into implementation or product repositories.

- `rfc/`
  - `README.md` – placeholder for RFC‑style proposals that have not yet become ADRs or formal specification.

---

## 3. Architecture and API (implementation‑oriented)

The following documents are closer to **concrete implementations** and may eventually be moved to other repositories (e.g. `Axis-core` or `ENRG`), or refactored into protocol‑level and implementation‑level parts.

- `architecture.md`
- `axis-architecture.md`

> NOTE: These currently describe particular architecture and deployment models. The goal is to either:
> - extract the protocol‑agnostic parts into the formal Axis Protocol specification and/or `docs/protocol/`, or
> - move purely implementation‑specific content into the corresponding implementation/product repositories.

- `api.md`
- `api/README.md`

> NOTE: These describe specific API shapes/endpoints.  
> If they belong to a particular implementation (e.g. ENRG backend or a specific Axis‑core deployment), they will be moved out of the protocol repository or clearly marked as implementation‑specific.

---

## 4. ENRG‑specific materials

All ENRG‑specific documents currently present in this repository are grouped under `docs/enrg/` for clarity:

- `enrg/Axis-One-Pager.md`
- `enrg/Axis-Terminology.md`
- `enrg/web4-enrg-overview-ru.md`

These documents describe **a specific product and deployment (ENRG)**, including terminology, elevator‑pitch style overviews, and background context.

> Over time, ENRG‑specific documentation will be moved into the dedicated [`ENRG`](https://github.com/AntonGrid/ENRG) repository.  
> This repository (`Axis-protocol`) will remain focused on the abstract protocol and its formal specification.

If additional ENRG materials are added here temporarily (e.g. legacy specs, diagrams, implementation notes),
they SHOULD also live under `docs/enrg/` and be clearly marked as **non‑normative** and **product‑specific**.

---

## 5. Relationship between repositories

- **Axis-protocol** (this repository)  
  Canonical, abstract protocol specification and related registries, ADRs, and governance.

- **Axis-core**  
  Reference (or one of the) implementation(s) of the Axis Protocol:
  smart contracts, services, SDKs, and implementation‑level documentation that is not tied to a particular product.

- **ENRG**  
  A concrete product/platform built on top of Axis:
  ENRG‑specific architecture, deployment guides, business context, user‑facing flows, and all product‑specific documentation.

The intent is to keep the **protocol** stable and reusable, while allowing multiple independent implementations and products to evolve on top of it.
