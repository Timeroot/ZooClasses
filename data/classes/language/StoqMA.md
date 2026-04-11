---
name: StoqMA
related:
  - MA
  - QMA
properties:
  - quantum
  - protocol
---
Stoquastic Merlin-Arthur. The class of decision problems solvable by a Merlin-Arthur protocol where the verifier is a polynomial-size stoquastic quantum circuit: gates from {X, CX, CCX} with ancillae prepared in |0⟩ and |+⟩ states, with a final measurement in the Hadamard basis.

Merlin sends a polynomial-size proof such that:
1. If the answer is "yes," there exists a proof that Arthur accepts with probability at least α.
2. If the answer is "no," for all proofs Arthur accepts with probability at most β.

where 1/2 ≤ β < α ≤ 1 and α - β ≥ 1/poly(n).

The 2-local stoquastic Hamiltonian problem is StoqMA-complete. The transverse field Ising model is also StoqMA-complete.

There is no known strong error reduction for StoqMA; it is conjectured that StoqMA with strong error reduction is equivalent to {lang:MA}.
