# Axis Constitution — The Laws of Trust

> **Status:** canonical reference (v1)
>
> The constitution is the set of non-negotiable principles that every layer of
> the ecosystem — protocol, core, domain profiles, intelligence — must obey.
> It is enforced **by architecture** (key placement, policy separation,
> signatures, DAO gates), not by promises.
>
> Sources: `GLOBAL_AI_ARCHITECTURE.md` (ENRG-AI), ADR-0001 … ADR-0010.

---

## Part I — Trust Over Technology (protocol principles)

From the [core specification](../spec/protocol/README.md). These are the laws
of the *trust standard* itself:

| # | Principle | Meaning |
|---|---|---|
| **T-1** | **Trust over technology** | Trust is the primary concern; technology is a means to achieve it. |
| **T-2** | **Identity is cryptographic** | Every device has its own identity; private keys never leave the device. |
| **T-3** | **Proof is verifiable** | Every event is cryptographically proven; verification needs no trusted third party. |
| **T-4** | **Registry is canonical** | Device identity, state and history live in a verifiable registry. |
| **T-5** | **Protocol is neutral** | No dependency on any blockchain, platform, vendor, or domain. |

---

## Part II — Constitution (ecosystem laws)

From the ENRG-AI global architecture. These are the laws of the *intelligence
layer* and its relationship to power:

| # | Law | How it is enforced |
|---|---|---|
| **C-1** | **AI is a source of signals, not decisions** (ADR-0003) | The global model only *proposes*; the Policy Engine decides, by rules |
| **C-2** | **The key never leaves the device** (ADR-0001) | Contributions are Ed25519-signed by the device; private keys are never transmitted |
| **C-3** | **Everything is verifiable** | Every contribution, signal and action → Trust Envelope + signatures + canonical JSON |
| **C-4** | **The model has no power** | The model holds no keys, signs nothing, executes no transactions |
| **C-5** | **Data does not leave the device** | FL: only weights/gradients are shared; raw data stays local |
| **C-6** | **Quality has a price** | Low-quality contribution → MAD rejection, reputation (ERS) loss, stake slashing |
| **C-7** | **Evolution goes through the DAO** | New rules/experiments are adopted by voting, never by model dictate |

---

## Part III — Derived laws (from ADRs)

| # | Law | Source |
|---|---|---|
| **L-1** | The **Verifier does not decide** — the Policy Engine does | ADR-0003 |
| **L-2** | The **Device Registry is the single source of truth** for device state | ADR-0002 |
| **L-3** | The **lifecycle is described by the protocol** (UNREGISTERED → REVOKED), not by proprietary systems | ADR-0005 |
| **L-4** | The **root of trust** is managed via a Governance-managed key registry (multisig/anchored) | ADR-0007 |
| **L-5** | **Firmware updates are signed, atomic (A/B), and anti-rollback** | ADR-0008 |
| **L-6** | **Core protocol knows nothing about tokens** — tokenization belongs to domain profiles | ADR-0006 |
| **L-7** | **Governance is hybrid**: on-chain token voting for parameters, Guardians multisig for emergencies, timelocks for everything critical | ADR-0009 |
| **L-8** | **AI attaches read-only**: data bridge → intelligence → oracle-only ERS loop; AI never gains write authority | ADR-0010 |

---

## Part IV — What this buys us

1. **`ai_anomaly_flagged` can never mint or freeze by itself** — it is a signal
   that reaches the Policy Engine, which decides.
2. **A stolen oracle server cannot impersonate devices** — device keys live in
   Secure Elements (SE050), and on-chain writes stay oracle-only.
3. **A malicious gateway cannot poison the global model** — contributions are
   signed, and MAD-outlier rejection + ERS weights + slashing price the quality.
4. **An "escaped" model cannot act** — it has no keys and no execution path by
   construction (C-4), plus physical interlocks and a DAO kill-switch.

---

*Revision history:* v1 — canonical collection of T-1..T-5, C-1..C-7, L-1..L-8.
