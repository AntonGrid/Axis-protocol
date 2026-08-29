# Domain Profile: Cold-Chain Logistics (example)

> **Purpose:** prove the Axis trust standard is **domain-agnostic**. This
> profile reuses every core primitive — identity, proof, verification,
> policy, anomaly — with a *different payload*. Nothing in Axis Core changes.

## The device

A cold-chain tracker (IoT asset tracker) signs temperature + location events:

```json
{
  "algo": "ed25519",
  "device_id": "<base64 public key>",
  "nonce": "41",
  "timestamp": "2026-08-29T10:00:00Z",
  "payload": {
    "temperature_c": 4.2,
    "location": "RIGA-WH-01",
    "asset": "pharma_plx-01"
  },
  "signature": "<base64>"
}
```

The signature covers the canonical JSON of the signed fields
(`device_id, nonce, timestamp, algo, payload`) — exactly as for an energy
proof. Only the `payload` shape differs.

## Domain policy (profile-level)

```python
def evaluate_cold_chain(payload):
    t = payload["temperature_c"]
    if t < 2.0 or t > 8.0:
        return {"allowed": False, "reason": "temperature_out_of_range", ...}
    return {"allowed": True, "reason": "ok", ...}
```

The core does not know about temperatures any more than it knows about
energy. The profile declares what a *valid* payload means.

## The pipeline (identical to ENRG)

1. Tracker signs an event (`canonical_proof_message` + Ed25519).
2. Oracle verifies the signature (`verify_ed25519_signature`).
3. Policy engine applies the profile rule (range check).
4. Shared anomaly detector watches the event history (spikes, nonce gaps).
5. Attestation: `allowed / reason / limits`.

## Run the demo

```bash
# from the Axis-core repository
python examples/logistics_profile.py
```

Expected output: three in-range events attested, a 13.4 °C excursion denied
with `temperature_out_of_range`.

## Why this matters

- A **second vertical** (logistics, then climate, mobility, manufacturing…)
  needs **zero changes** to the core trust layer.
- The same HFL, PoI and Sovereign-AI machinery attaches to any profile: the
  devices train a shared backbone with per-domain heads.
- This is what "protocol over project" means: ENRG is the first proof, not the
  only use.
