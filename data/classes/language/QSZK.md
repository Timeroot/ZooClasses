---
name: QSZK
related:
  - SZK
  - HVSZK
  - QIP
  - PSPACE
  - UP
properties:
  - quantum
  - protocol
---
Quantum Statistical Zero-Knowledge. A quantum analog of HVSZK. The verifier is a BQP algorithm who can exchange quantum messages with Merlin; their states may become entangled. The zero-knowledge requirement: each mixed state in Arthur's view must have trace distance ≤ 1/10 from a state Arthur could prepare himself (in BQP), without help.

Defined in {ref:wat02}, where it was shown that:
- QSZK ⊆ PSPACE.
- QSZK is closed under complement.
- Any protocol can be parallelized to two messages; QSZK ⊆ QIP[2].
- Protocols can be assumed public-coin (as for SZK).
- Complete promise problem: Quantum State Distinguishability (QSD) — given circuits Q_0, Q_1 producing states ρ_0, ρ_1, decide whether their trace distance is ≤ α or ≥ β (where α < β²).

Honest-verifier QSZK equals general-verifier QSZK {ref:wat09b}. There exist oracles relative to which QSZK does not contain UP ∩ coUP or UP {ref:mw18}.
