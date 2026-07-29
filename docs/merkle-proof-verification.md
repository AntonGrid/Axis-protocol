# Merkle Proof Verification

## Overview

Merkle Proof Verification is a cryptographic mechanism that allows proving membership of a manifest in a Merkle tree without downloading the entire tree.

In Axis Protocol, Merkle proofs are used as a **trust verification tool**:

1. **Efficient Device Verification** — Devices can prove their manifest is registered without downloading all manifests.
2. **Scalability** — As the number of manifests grows, proof size remains O(log n).
3. **Privacy** — Devices only expose their own manifest content to verifiers, not the full registry.

Axis Protocol uses Merkle proofs as a generic building block for **verifying trust**.

The protocol does not assume any specific blockchain platform, framework, or runtime. Any implementation MAY:
- store Merkle roots on-chain or off-chain;
- implement verification logic in smart contracts, trusted services, or secure enclaves;
- choose any secure hash function family.

---

## Trust Verification Pipeline

Merkle proofs fit into the trust verification pipeline as follows:
Device → Manifest → Merkle Proof → Merkle Root → Trust

text

- **Manifest** — defines what the device is and what it can do.
- **Merkle Proof** — proves that the Manifest is part of the approved set.
- **Merkle Root** — the trusted anchor, published by the Registry.
- **Trust** — established when the Proof is verified against the Root.

---

## Architecture

### Verification Service / Smart Contract

Implementations SHOULD provide a canonical verification interface. One possible abstract model is:
struct MerkleProofVerificationResult {
registry_id: bytes // Identifier of the Manifest Registry
manifest_id: bytes // Identifier of the verified manifest
verified_root: bytes // Root against which proof was checked
verified_at: timestamp // When the proof was verified
proof_length: uint8 // Number of hashes in the proof
verified_by: bytes // Identifier of the verifier
}

text

A generic verification function:
verify_merkle_proof(
manifest_id: bytes,
proof_path: list<bytes>, // Sibling hashes from leaf to root
leaf_hash: bytes, // Computed leaf hash
root: bytes // Expected Merkle root
) -> MerkleProofVerificationResult | Error

text

Concrete implementations MAY:
- expose this as a smart contract function;
- expose it via an API endpoint;
- embed it into a device-side trusted execution environment.

---

## Off-Chain Flow

A typical flow combining off-chain registries and a verification service:

1. **Off-chain registry** maintains manifests and computes a Merkle tree over manifest identifiers or canonical manifest hashes.
2. **Snapshot publisher** periodically creates Merkle snapshots and publishes Merkle roots (e.g., to a blockchain, an audit log, an append-only log, or a registry record).
3. **Device / Verifier** requests a Merkle proof for a specific manifest from the registry.
4. **Device / Verifier** computes or validates the Merkle proof locally.
5. **Device / Verifier** submits the proof and expected root to the verification service.
6. **Verification service** validates the proof and stores the verification result for future reference or auditing.

The protocol **does not** mandate where the verification happens — only that:
- the hashing scheme is well-defined and consistent;
- the tree construction rules are deterministic;
- proofs are verifiable by any conforming implementation.

---

## Usage Example (Off-Chain)

The following example illustrates Merkle tree construction and proof generation off-chain. It is deliberately implementation-agnostic and can be adapted to any language or runtime.

### 1. Create Merkle Tree (Off-chain)

```javascript
import crypto from "crypto";

function hash(data: Buffer): Buffer {
  return crypto.createHash("sha256").update(data).digest();
}

const leaves = [
  Buffer.from("manifest-1"),
  Buffer.from("manifest-2"),
  Buffer.from("manifest-3"),
];

// Build tree bottom-up
let currentLevel = leaves.map((leaf) => hash(leaf));

const levels: Buffer[][] = [currentLevel]; // keep all levels if you need proofs

while (currentLevel.length > 1) {
  const nextLevel: Buffer[] = [];
  for (let i = 0; i < currentLevel.length; i += 2) {
    const left = currentLevel[i];
    const right = i + 1 < currentLevel.length ? currentLevel[i + 1] : left;
    const parent = hash(Buffer.concat([left, right]));
    nextLevel.push(parent);
  }
  currentLevel = nextLevel;
  levels.push(currentLevel);
}

const merkleRoot = currentLevel[0];
console.log("Merkle root:", merkleRoot.toString("hex"));
2. Generate Proof for a Leaf
javascript
type MerkleTreeLevels = Buffer[][]; // levels[0] = leaves, levels[levels.length-1] = root

function getMerkleProof(levels: MerkleTreeLevels, leafIndex: number): Buffer[] {
  const proof: Buffer[] = [];
  let index = leafIndex;

  for (let levelIndex = 0; levelIndex < levels.length - 1; levelIndex++) {
    const level = levels[levelIndex];
    const siblingIndex = index ^ 1; // XOR to get sibling index

    if (siblingIndex < level.length) {
      proof.push(level[siblingIndex]);
    }

    index = Math.floor(index / 2);
  }

  return proof;
}

const leafIndex = 1;
const proof = getMerkleProof(levels, leafIndex);
console.log(`Proof has ${proof.length} nodes`);
3. Verify a Proof (Generic)
javascript
function verifyMerkleProof(
  leaf: Buffer,
  proof: Buffer[],
  expectedRoot: Buffer
): boolean {
  let computedHash = hash(leaf);

  for (const sibling of proof) {
    // The concatenation order (left/right) MUST follow the tree construction rules.
    // This simple example always concatenates [computedHash, sibling],
    // but production implementations should encode the side (left/right) explicitly.
    computedHash = hash(Buffer.concat([computedHash, sibling]));
  }

  return computedHash.equals(expectedRoot);
}

const leafHash = hash(leaves[leafIndex]);
const isValid = verifyMerkleProof(leafHash, proof, merkleRoot);

console.log(`Proof valid: ${isValid}`);
In a concrete Axis-compatible implementation, this verification logic MAY be:

embedded in a smart contract;

provided as an external verification service;

run directly on the device or verifier.

Security Properties
Completeness
Valid proofs are always accepted (assuming the expected root is correct and matches the published Merkle root).

Soundness
Invalid proofs are rejected. An attacker cannot forge a valid proof without:

Knowing the exact leaf value or being able to collide with it under the chosen hash function.

Having valid sibling hashes for the entire path from leaf to root.

The security properties depend on:

the collision resistance and preimage resistance of the hash function;

the integrity of the published Merkle root (e.g., how it is anchored or distributed).

Efficiency
Proof Size: O(log n) hashes (e.g., logarithmic in the number of manifests).

Verification Time: O(log n) hash operations.

Storage: A verification service MAY store a single verification record per manifest and per snapshot.

Testing
Implementations SHOULD provide automated tests that:

Construct Merkle trees from known test vectors.

Generate proofs for specific leaves.

Verify proofs against known roots (both positive and negative cases).

Validate behavior for edge cases (single leaf, odd number of leaves, deep trees).

Integration with Device Lifecycle
Devices use Merkle proofs in several scenarios:

Boot-time Verification — A device proves that its current manifest is included in the approved manifest set.

Firmware Update — Before installing new firmware, a device verifies that the firmware manifest is included in an approved release set.

Attestation — A device presents a Merkle proof to remote verifiers to demonstrate that it runs an approved manifest.

Implementations MAY combine Merkle proofs with:

signed manifests;

attestation tokens;

on-chain or off-chain registries.

Future Enhancements
Batch Proof Verification — Verify multiple proofs in a single request or transaction.

Proof Caching — Cache verified proofs (or their digests) to reduce repeated verification costs.

Negative Proofs — Mechanisms to prove that a manifest is NOT part of a set (e.g., for quarantine or revocation).

Light Client Support — Optimize verification flows for resource-constrained devices
