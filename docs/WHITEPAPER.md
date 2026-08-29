# Axis Protocol — Whitepaper v1

> **Title:** Sovereign Intelligence for the Physical World
> **Status:** draft v1 · **Date:** 2026-08-29
> **License:** Apache 2.0 (spec) — this document is informative.

---

## Abstract

> **The digital world is blind to the physical one.** Blockchains are excellent
> at storing and moving value, but they cannot see a solar panel, verify that a
> megawatt-hour was produced, or tell a real sensor from a simulation.

Axis is an **overlay trust standard** — a domain- and platform-agnostic
language between physical devices and digital systems:

```
Physical Device → Event → Proof → Attestation → Digital Trust
```

On top of this standard we build three things no single project has combined:

1. **ENRG** — the first living domain profile: real hardware (ESP32 with a
   Secure Element) proving energy production on Solana, tokenized as SRC.
2. **Sovereign AI** — a global neural network trained by the devices
   themselves, that by constitution **cannot act**: it proposes, the Policy
   Engine decides, the DAO governs.
3. **Proof-of-Intelligence (PoI)** — reputation and influence earned for
   *quality federated contributions*, screened by MAD, weighted by ERS — a
   second earning channel alongside physical production.

---

## 1. The problem

### 1.1 Web3 is blind to physics

Smart contracts, tokens, and decentralized ledgers are the best tools we have
for coordinating digital value. But they depend on **oracles** — trusted
third parties that tell the chain what happened in the real world. An oracle
can be wrong, bribed, or simply a software simulation. There is no native way
for a chain to know that 1 MWh was *actually* produced.

### 1.2 Existing DePIN: proof, but no intelligence

The DePIN movement ("decentralized physical infrastructure networks")
attacked this with **proof-of-physical-work**: devices sign data, networks
tokenize it. Helium, Hivemapper, DIMO and dozens of energy projects showed the
pattern works. But almost all of them:

- tokenize **raw data**, not **trust**;
- run **no learning** on the device side;
- give **no constitutional limits** to their AI (if they have AI);
- treat each vertical as a silo instead of a composable standard.

The result: a landscape of disconnected "miners", where intelligence — if
present — is either centralized or dangerously empowered.

## 2. The solution

### 2.1 Axis — the trust layer

Axis Protocol (this repository) is the **normative specification** of the
trust pipeline. It is deliberately:

- **domain-agnostic** — works for energy, logistics, climate, mobility;
- **platform-agnostic** — works with Solana, EVM, or a plain append-only log;
- **vendor-agnostic** — any runtime can implement it.

The core concepts (see `spec/protocol/`):

- **Identity** — every device gets a cryptographic identity; the private key
  never leaves it (ADR-0001).
- **Proof** — the device signs an event (`device_id ‖ nonce ‖ ts ‖ payload`).
- **Verification** — an independent party checks the signature and semantics.
- **Attestation** — the oracle issues a signed verification.
- **Policy** — the *only* decision point (ADR-0003): cryptography does not
  decide; policy does.

### 2.2 The four layers

| Layer | Component | Role |
|---|---|---|
| L0 | **Axis Protocol** (this repo) | normative trust standard, ADRs, constitution |
| L1 | **Axis Core** (reference impl.) | policy engine, AI signals, wire, EVM bridge, registry |
| L2 | **ENRG** (domain profile) | energy: Solana program, oracle, ESP32+SE050, SRC/ERS |
| L3 | **ENRG-AI** (intelligence) | HFL, digital feeds, signals, recommender, DAO evolution |

### 2.3 Sovereign AI (constitutional)

The AI layer is powerful but **restrained by construction** (C-1..C-7):

- it produces **signals** (forecast, anomaly, market) — signed, verifiable,
  uncertainty-aware;
- it **cannot sign**, **cannot execute**, **cannot write on-chain**;
- every decision passes the **Policy Engine**; every rule change passes the
  **DAO**; every emergency action is guarded by **Guardians multisig**
  (ADR-0009).

> This is the inverse of the "AI agent with a wallet" trend: instead of giving
> machines power and hoping they behave, we give them none and make their
> influence proportional to **verifiable quality**.

### 2.4 Proof-of-Intelligence

PoI is the economic engine of the intelligence layer:

- gateways train locally, sign contributions (`axis-fed/1`), and send only
  weights — raw data never leaves (C-5);
- the aggregator verifies signatures, screens outliers with **MAD**, and
  averages with **ERS-weighted** samples (C-6: quality has a price);
- accepted contributions **gain** ERS; rejected outliers **decay** toward a
  floor; the next round's influence follows;
- every contribution is reducible to a signed on-chain **commitment digest**
  (oracle-only writes, ADR-0010) — the history of "who contributed what" is
  publicly verifiable.



## 3. The hierarchy (HFL)

The network learns at four levels:

| Level | Hardware | Role | Model size |
|---|---|---|---|
| L0 | ESP32 + SE050 | inference + signing | 10–100 KB |
| L1 | gateway (RPi) | local training + signed contributions | 0.1–10 MB |
| L2 | regional server | FedAvg per region, domain features, market | 10–100 MB |
| L3 | global cluster | HierFedAvg, shared backbone | 100 MB–GB |

**Mathematics (summary).** One FedAvg round over a region:

```
θ_global = Σ_g  (n_g · w_g(ERS_g)) · θ_g  /  Σ_g (n_g · w_g(ERS_g))
```

where `θ_g` is the gateway weights, `n_g` the local sample count, and
`w_g(ERS) = 0.1 + 0.9·ERS^α` a reputation multiplier in `[0.1, 1.0]`.
Outliers are removed first by a **MAD** screen (robust to a malicious gateway
inflating the variance). The global model is **read-only** — it proposes.

## 4. The closed loop

```
measured → signed proof → oracle (policy) → on-chain state
                                        ↓
            signals (forecast · anomaly · market)  ← ENRG-AI observes
                                        ↓
        Recommender ranks SELL/STORE/BUY/HOLD  (a signal, never an action)
                                        ↓
  Policy Engine gates: trading right · volume · DAO approval (ADR-0003)
                                        ↓
             executed action → revenue → ERS → experience → retrain
```

The model learns **economics**, not just physics: if it recommended "sell" and
the price rose, the negative reward corrects the next recommendation
(GLOBAL_AI_ARCHITECTURE §7).

## 5. Economy

- **SRC** — the ENRG domain token: 1 SRC = 1 MWh of verified, attested
  production. A domain-profile concept (ADR-0006); the trust layer knows
  nothing about it.
- **ERS** — on-chain reputation PDA per producer: grows with verified energy
  and uptime, drops with profile anomalies (`report_anomaly`, −5%..−50%).
- **PoI** — the second earning channel: influence and reputation for quality
  federated contributions.
- **Slashing** — economic penalty for malicious contributions (stake-backed),
  complementing MAD + ERS (C-6).

## 6. Security model

| Threat | Mechanism |
|---|---|
| Poisoning the model | signed contributions + MAD screen + ERS weights + slashing |
| Spam contributions | stake per contribution, nonce/frequency limits, min samples |
| Privacy leak | FL: weights only + differential privacy (planned) |
| Oracle compromise | device keys in Secure Elements; on-chain writes oracle-only |
| Model "escape" | no keys, no execution path (C-4) + physical interlocks + DAO kill-switch |
| DAO capture | quadratic voting, timelocks, risk-tiered quorums (ADR-0009) |

## 7. Roadmap

| Phase | Focus | Status |
|---|---|---|
| 0 | One map, constitution, glossary | ✅ done |
| 1 | Living demo: proofs → AI signals → signed attestation → UI | ✅ mostly done (counter paused) |
| 2 | PoI: ERS economy, leaderboard, commitment digests, ERS loop | ✅ done (off-chain) |
| 3 | Closed economic loop: recommender + policy gates + reward | ✅ done (simulation) |
| 4 | Standard: this paper, conformance, second domain, community | 🔄 in progress |

---

*See also:* [ECOSYSTEM.md](./ECOSYSTEM.md) · [CONSTITUTION.md](./CONSTITUTION.md) ·
[GLOSSARY.md](./GLOSSARY.md) · `spec/` · `adr/`.
