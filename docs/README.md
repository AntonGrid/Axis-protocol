# Axis Protocol Documentation
## 0. Philosophy

The foundational philosophy of the Axis Protocol is captured in the **Architecture Book**:

- [`docs/philosophy/architecture/00_Prologue.md`](philosophy/architecture/00_Prologue.md) — Introduction to the vision
- [`docs/philosophy/architecture/01_The_Birth_of_an_Idea.md`](philosophy/architecture/01_The_Birth_of_an_Idea.md) — How it all began
- [`docs/philosophy/architecture/02_When_a_Token_Was_No_Longer_Enough.md`](philosophy/architecture/02_When_a_Token_Was_No_Longer_Enough.md) — Moving beyond tokens
- [`docs/philosophy/architecture/03_When_the_Protocol_Became_More_Important_than_the_Project.md`](philosophy/architecture/03_When_the_Protocol_Became_More_Important_than_the_Project.md) — Protocol over project
- [`docs/philosophy/architecture/04_Architecture_Is_Born_Before_the_Code.md`](philosophy/architecture/04_Architecture_Is_Born_Before_the_Code.md) — Architecture first
- [`docs/philosophy/architecture/05_The_First_Law_of_Trust.md`](philosophy/architecture/05_The_First_Law_of_Trust.md) — The first law of trust

This `docs/` tree describes the **Axis Protocol** – an abstract, domain-agnostic standard for representing and exchanging verifiable claims, attestations, and asset state.

It is intentionally separated from any concrete product or deployment. Project-specific and product-specific materials live in their own repositories (e.g., [ENRG](https://github.com/AntonGrid/ENRG) for energy tokenization, [Axis-core](https://github.com/AntonGrid/Axis-core) for reference implementation).

---

## 1. Protocol Core

Protocol-level documentation that should remain domain- and product-agnostic:

- **`Axis-Protocol-Specification.md`** — normative protocol specification
- **`Axis-Protocol-One-Pager.md`** — high-level introduction
- **`Axis-Protocol-Overview.md`** — detailed overview
- **`Axis-Protocol-Terminology.md`** — core terminology
- **`Axis-Governance-and-ADR.md`** — governance and ADR/RFC process
- **`merkle-proof-verification.md`** — Merkle proof verification model

- **`platform/`** — abstract device lifecycle and provisioning models
  - `device-lifecycle.md` — device states and transitions
  - `provisioning.md` — device registration and onboarding

---

## 2. Governance and ADRs

Documents that describe how the protocol evolves and why certain design decisions were made:

- **`adr/`** — Architecture Decision Records (legacy, being migrated to root `adr/`)
- **`Axis-Governance-and-ADR.md`** — overview of governance processes

All ADRs are being migrated to the root `adr/` directory for easier access.

---

## 3. Architecture and Implementation

Documents describing concrete implementations and architecture are maintained in:
- **[Axis-core](https://github.com/AntonGrid/Axis-core)** — reference implementation
- **[ENRG](https://github.com/AntonGrid/ENRG)** — energy tokenization application

---

## Relationship Between Repositories

- **Axis-protocol** (this repository) — canonical, abstract protocol specification
- **Axis-core** — reference implementation of the Axis Protocol
- **ENRG** — concrete product/platform built on top of Axis

The intent is to keep the protocol stable and reusable, while allowing multiple independent implementations and products to evolve on top of it.
