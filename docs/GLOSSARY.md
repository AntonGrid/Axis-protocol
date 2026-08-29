# Axis Ecosystem — Unified Glossary

> One vocabulary across Axis Protocol, Axis Core, ENRG and ENRG-AI.
> Each term links to its canonical definition.

---

## Trust & identity

| Term | Definition |
|---|---|
| **Device / Actor** | A physical entity (meter, inverter, sensor, controller) with a cryptographic identity. Its private key never leaves it (C-2, ADR-0001). |
| **Proof** | Cryptographic evidence that a physical event occurred (e.g. `device_id ‖ nonce ‖ ts ‖ energy_wh`, Ed25519-signed). |
| **Attestation** | A signed verification of a Proof by a trusted entity (the oracle). The container, signing rules and bridge logic come from Axis; the payload is domain-specific. |
| **Trust Envelope** | The wire container carrying headers + signed payload (canonical JSON), so every message is self-verifiable (C-3). |
| **Claim** | A digital statement backed by an Attestation. |
| **Verifier** | The component that receives proofs, checks signatures, and *executes* Policy Engine decisions. It never decides policy (ADR-0003, L-1). |
| **Oracle** | A service that validates device proofs, aggregates data, and produces oracle-level attestations. The only on-chain writer in the trusted path (ADR-0010). |
| **Registry** | Canonical store of identity/state. Kinds: Device, Manifest, Capability, Event, Error. The Device Registry is the single source of truth for device state (ADR-0002, L-2). |
| **Manifest** | A signed description of what a device is and can do (rated power, capabilities, policy version). Verified before proofs are accepted (ADR-0004). |
| **Lifecycle** | Protocol-defined device states: UNREGISTERED → REGISTERED → CLAIMED → PROVISIONED → ACTIVE → QUARANTINE / MAINTENANCE → REVOKED (ADR-0005, L-3). |
| **device_id** | Deterministic identifier derived from the device public key; base58, 32–64 chars. |

## Policy & governance

| Term | Definition |
|---|---|
| **Policy Engine** | The single decision point (ADR-0003): evaluates proofs, AI signals and trade recommendations against rules; produces `allowed / reason` decisions. Mirrored on-chain (`policy_engine.rs`) and off-chain (`axis_core.policy`). |
| **Domain Profile** | A domain-specific application on the trust standard (ENRG = energy). The core knows nothing about tokens (ADR-0006, L-6). |
| **DAO** | Token-holder governance for parameters and model evolution; part of the hybrid model with Guardians and timelocks (ADR-0009, L-7). |
| **Guardians** | Threshold multisig for emergency operations (root key rotation, freezes) with short timelocks and post-action audit. |
| **Timelock** | Mandatory delay (e.g. 48–72 h) before critical changes execute; shorter only in the emergency flow. |
| **ADR / RFC** | Architecture Decision Records — the protocol's change history and proposal mechanism (10 ADRs and counting). |

## Economy & incentives

| Term | Definition |
|---|---|
| **SRC** | The ENRG domain token: 1 SRC = 1 MWh of verified, attested energy production. A domain-profile concept (ADR-0006), not a core-protocol concept. |
| **ERS** | Energy/Reputation Score — on-chain reputation PDA per producer; rises with quality, drops with misbehavior (C-6). |
| **PoI (Proof of Intelligence)** | The second "mining" channel of the ecosystem: reputation/emission for *quality federated contributions*, not just for production. |
| **Federated contribution** | Ed25519-signed weight update from a gateway (`axis-fed/1`), canonical-JSON serialized, verified before aggregation. |
| **FedAvg / HierFedAvg** | Federated averaging across gateways; hierarchical (L1 → L2 → L3) with weights `f(ERS, samples, loss)` and MAD outlier rejection. |
| **MAD rejection** | Median-absolute-deviation screening that discards outlier ("evil") contributions in aggregation. |
| **Slashing** | Economic penalty for malicious/bad contributions (stake loss) — planned; complements MAD + ERS. |

## Intelligence layer

| Term | Definition |
|---|---|
| **Signal** | A structured observation from the AI layer (forecast, anomaly, market) — never a decision (C-1). |
| **SignalProvider** | Axis-core entry point that evaluates anomaly + forecast + market into one `Signal`. |
| **Recommender** | Ranks market actions `SELL / STORE / BUY / HOLD` with confidence and rationale; it never executes (C-4). |
| **Generation forecast** | Holt-trend (numpy) or zero-shot (TimesFM) forecast of energy output with prediction intervals. |
| **Anomaly detection** | MAD/spike detection over device history (energy, power, nonce gaps) or over forecast residuals. |
| **HFL (Hierarchical FL)** | The multi-level learning hierarchy: L0 devices (inference) → L1 gateways (training) → L2 regional aggregators → L3 global backbone. |
| **Digital twin** | Per-device model of generation (hour-of-day, solar irradiance, rolling window) for plausibility and forecasting. |
| **Trust pipeline** | `Physical Device → Event → Proof → Attestation → Digital Trust` — the end-to-end chain each link of which is verifiable. |
