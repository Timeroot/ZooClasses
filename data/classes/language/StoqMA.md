---
name: StoqMA
related:
  - MA
  - QMA
properties:
  - quantum
  - protocol
---
Stoquastic Merlin-Arthur. The class of decision problems solvable by a Merlin-Arthur protocol where the verifier is a polynomial-size stoquastic quantum circuit (i.e., all off-diagonal elements of the Hamiltonian are non-positive in the computational basis). Merlin sends a polynomial-size quantum proof, and Arthur (the verifier) accepts with probability at least α for YES instances and at most β for NO instances, with α−β ≥ 1/poly(n). The 2-local stoquastic Hamiltonian problem is complete for StoqMA. The transverse field Ising model is also StoqMA-complete. There is no known strong error reduction for StoqMA; it is conjectured that StoqMA with strong error reduction is equivalent to MA.
