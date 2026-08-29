# Axis Ecosystem — One Map

> **What this is.** The Axis ecosystem is **not "one more DePIN project"**. It
> is a four-layer construction: a domain-agnostic **trust standard**, a
> **reference implementation**, a first living **domain profile** (energy),
> and an **intelligence layer** — plus the interfaces humans use.
>
> ENRG (energy) is the *first* profile and the *living proof* that the stack
> works on real hardware. The standard itself is domain-neutral: the same
> trust pipeline can serve logistics, climate, mobility, or anything physical.

---

## 1. The layers at a glance

```
┌───────────────────────────────────────────────────────────────────────────┐
│  L4  INTERFACES            enrg-landing (web) · Axis-connect (PWA)          │
│      humans read live proof data, AI signals, network state                  │
├───────────────────────────────────────────────────────────────────────────┤
│  L3  INTELLIGENCE          ENRG-AI                                          │
│      digital feeds/train · FL & HFL (Ed25519, MAD) · market · evolution(DAO)│
│      forecast · hybrid AI-oracle signals (sign_bundle) · recommender        │
├───────────────────────────────────────────────────────────────────────────┤
│  L2  DOMAIN PROFILE        ENRG (energy)                                    │
│      Solana enrg-mvp/program · Render oracle (Node) · ESP32+SE050 firmware  │
│      SRC token (1 = 1 MWh) · ERS reputation PDA · manifest/OTA              │
├───────────────────────────────────────────────────────────────────────────┤
│  L1  REFERENCE IMPLEMENT.  Axis-core                                        │
│      policy engine · ai/ (anomaly, forecast, recommender) · wire envelope   │
│      storage (pg/redis/mem) · EVM bridge · oracle registry · SDK            │
├───────────────────────────────────────────────────────────────────────────┤
│  L0  STANDARD              Axis-protocol (spec, Apache-2.0)                 │
│      trust model · wire format · validation · lifecycle · 10 ADRs ·         │
│      constitution (T-1..T-5, C-1..C-7, L-1..L-8)                            │
└───────────────────────────────────────────────────────────────────────────┘
```

## 2. Repositories

| Repo | Layer | Role |
|---|---|---|
| [`Axis-protocol`](https://github.com/AntonGrid/Axis-protocol) | L0 | The **normative specification** of the overlay trust standard: model, wire format, validation, lifecycle, ADRs, constitution. |
| [`Axis-core`](https://github.com/AntonGrid/Axis-core) | L1 | The **reference implementation**: schemas, policy engine, AI signals, trust envelope, storage backends, EVM bridge, oracle registry, SDK. |
| [`ENRG`](https://github.com/AntonGrid/ENRG) | L2 | The **first domain profile** (energy): Solana programs, oracle, ESP32 firmware with Secure Element, SRC/ERS economics. |
| [`ENRG-AI`](https://github.com/AntonGrid/ENRG-AI) | L3 | The **intelligence layer**: federated learning, hierarchical aggregation, market signals, DAO-driven evolution, forecast + AI-oracle. |
| [`enrg-landing`](https://github.com/AntonGrid/enrg-landing) | L4 | Public web landing — live ecosystem data, AI heartbeat, network visualization. |
| [`Axis-connect`](https://github.com/AntonGrid/Axis-connect) | L4 | PWA dashboard — device screen, on-chain proof reconstruction, AI health. |

## 3. The trust pipeline

```
Physical Device → Event → Proof → Attestation → Digital Trust
```

Every link is cryptographically verifiable; no trusted third party is required:

1. An ESP32 with a Secure Element signs a proof of the event
   (`device_id ‖ nonce ‖ ts ‖ energy_wh`, Ed25519) — the key never leaves the chip.
2. The **oracle** validates the signature, consults the **Policy Engine**, and
   stores/mints the verified result (on-chain for the ENRG profile).
3. The **AI layer** observes the resulting stream and produces *signals*
   (forecast, anomaly, market) — observations, never decisions.
4. The **Policy Engine** is the only decision point (ADR-0003); the **DAO**
   governs parameters and model evolution (ADR-0009).

## 4. Constitution & ADR index

- **Constitution** — see [`CONSTITUTION.md`](./CONSTITUTION.md):
  T-1..T-5 (trust standard), C-1..C-7 (ecosystem laws), L-1..L-8 (derived laws).

| ADR | Title | Essence |
|---|---|---|
| 0001 | Key never leaves the device | Proofs are signed on-device; server only verifies |
| 0002 | Device Registry is source of truth | One canonical registry for device state |
| 0003 | Policy Engine decides, not Verifier | Cryptography ≠ policy; single decision point |
| 0004 | Device Manifest | Signed description of what a device is/can do |
| 0005 | Device states & lifecycle | Protocol-defined states and transitions |
| 0006 | Core protocol vs domain profile | Trust layer knows nothing about tokens |
| 0007 | Security & key management | Roots of trust, key types, rotation, revocation |
| 0008 | OTA & secure firmware updates | Signed, atomic, anti-rollback updates |
| 0009 | Governance protocol | Hybrid: token voting + Guardians + timelocks |
| 0010 | ENRG-AI as intelligence layer | 3-layer attach: data bridge → intelligence → ERS loop |

## 5. Device lifecycle

```
UNREGISTERED → REGISTERED → CLAIMED → PROVISIONED → ACTIVE
                                                        │
                        QUARANTINE ← (suspicion/error) ─┤
                        MAINTENANCE ← (planned work)  ──┤
                        REVOKED ← (decommission)      ──┘
```

## 6. Economy at a glance

- **SRC** — domain token of the ENRG profile: 1 SRC = 1 MWh of *verified,
  attested* production.
- **ERS** — on-chain reputation per producer; quality-weighted.
- **PoI (Proof of Intelligence)** — the second earning channel: reputation and
  emission for *quality federated contributions* (signed, MAD-screened,
  ERS-weighted) to the global hierarchical model.

## 7. Roadmap

| Phase | Focus | Status |
|---|---|---|
| 0 | One map: this document, glossary, constitution, README cross-links | **in progress** |
| 1 | Living vertical demo: proofs → AI signals → signed bundle → live UI | planned |
| 2 | PoI in production: contribution economy, leaderboard, on-chain commitments, ERS loop | planned |
| 3 | Closed economic loop: Recommender → Policy gates → DAO → reward → retrain | planned |
| 4 | Standard: whitepaper, conformance suite, second domain demo, community | planned |

