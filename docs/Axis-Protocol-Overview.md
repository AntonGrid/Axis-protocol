# Axis Protocol: Web4 Architecture

## 1. From Web3 to Web4

Web3 answers the question:

> "How can ownership and operations on **digital objects** (tokens, NFTs, smart contract states) be decentralized and verifiable?"

Web3 blockchains see the world through:

- addresses (accounts),
- digital assets (balances, tokens),
- smart contract state.

Everything that happens **outside the blockchain** is, by default:

- either non-existent,
- or exists as "data in a transaction" that cannot be trusted without external infrastructure (oracles, API gateways, etc.).

**Axis Protocol** adds another layer:

> "How can **real-world events** become part of decentralized consensus with the same rigorous verifiability as balances and hashes?"

That is:

- **Web3:** decentralized **digital states**.
- **Axis (Web4 level):** decentralized **verifiable physical-world events** + digital states and the economy around them.

---

## 2. Axis Architecture as a Web4 Layer

Axis introduces primitives that are not available "out of the box" in Web3:

### 2.1. Real-World Actors (Devices and Processes)

In Web3, everything revolves around:

- users (keys, wallets),
- smart contracts.

Axis adds a separate class of first-class entities:

- devices (meters, inverters, sensors, controllers),
- industrial control systems,
- and any physical actors with cryptographic identity.

They become **full participants in the protocol**, not just sources of "data in comments."

### 2.2. From Measurements to Proofs

Traditional systems: device measures → sends data → server trusts it.

Axis Protocol: device measures → generates cryptographic proof → system verifies proof independently.

This shift transforms:

- **Trust** from "I trust this server" to "I trust this proof"
- **Security** from "the data is correct because we say so" to "the data is correct because it's cryptographically provable"

---

### 2.3. Device Lifecycle as a First-Class Citizen

Devices in Axis have a **full lifecycle**:

| Stage | Description |
|-------|-------------|
| **UNREGISTERED** | Device is unknown to the system. |
| **REGISTERED** | Device has a cryptographic identity. |
| **CLAIMED** | Device is linked to an owner. |
| **PROVISIONED** | Device is configured and ready. |
| **ACTIVE** | Device is fully operational. |
| **QUARANTINE** | Device is suspected of malfunction. |
| **MAINTENANCE** | Device is undergoing maintenance. |
| **REVOKED** | Device is permanently decommissioned. |

This lifecycle is enforced by the protocol, not by external systems.

---

### 2.4. Domain-Agnostic Trust Layer

Axis Protocol does not know about:

- energy,
- tokens,
- supply chains,
- finance.

It knows only about:

- actors,
- claims,
- attestations,
- proofs,
- policies.

This makes it a **foundational layer** for any domain that requires trust between physical and digital worlds.

---

### 2.5. Governance as Protocol

Axis Protocol includes built-in governance:

- ADR/RFC process for changes
- Hybrid governance model (token holders + guardians)
- On-chain anchoring of critical decisions

This ensures the protocol can evolve without relying on a single entity.

---

## 3. Comparison: Web3 vs Axis (Web4)

| Aspect | Web3 | Axis Protocol (Web4) |
|--------|------|----------------------|
| **Focus** | Digital assets | Physical + digital trust |
| **Actors** | Wallets, contracts | Devices, organizations, services |
| **Data** | On-chain state | Proven physical events |
| **Trust** | Cryptographic consensus | Cryptographic identity + proof |
| **Lifecycle** | Token lifecycle | Device lifecycle |
| **Domain** | Finance, DeFi | Any domain (energy, mobility, etc.) |
| **Governance** | Token voting | ADR/RFC + hybrid governance |

---

## 4. Why This Matters

Axis Protocol bridges the gap between:

- **The physical world** (devices, energy, people)
- **The digital world** (blockchains, tokens, smart contracts)

It enables:

- **Verifiable trust** — no central authority needed
- **Decentralized infrastructure** — devices can participate directly
- **Cross-domain interoperability** — the same protocol works for energy, mobility, supply chain, and more

This is the foundation for a **Web4** where physical and digital worlds are equally verifiable, equally decentralized, and equally trusted.
