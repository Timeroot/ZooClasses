---
name: k-EQBP
related:
  - NC^1
  - k-PBP
  - EQP
properties:
  - quantum
concrete: false
---
Width-k Polynomial-Time Exact Quantum Branching Programs. See k-PBP for the definition of a classical branching program. A quantum branching program is the natural quantum generalization: we have a quantum state in a Hilbert space of dimension k. Each step t consists of applying a unitary matrix U^(t)(x_i) depending on a single bit x_i of the input (these are the quantum analogues of "oblivious" branching programs). In the end we measure to decide whether to accept; there must be zero probability of error.

Defined in {ref:amp02}, where it was also shown that NC^1 is contained in 2-EQBP.
