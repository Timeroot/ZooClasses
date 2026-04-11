---
name: NP
related:
  - P
  - "#P"
  - coNP
  - MA
  - AM
  - PH
  - NPC
  - NPI
  - BPP
  - PCP
---
Nondeterministic Polynomial-Time. An "NP machine" is a nondeterministic polynomial-time Turing machine. NP is the class of decision problems solvable by an NP machine such that:
1. If the answer is "yes," at least one computation path accepts.
2. If the answer is "no," all computation paths reject.

Equivalently, NP is the class of problems where "yes" answers have polynomial-length proofs verifiable in P (polynomial-time).

Classic NP-complete problems include SAT, 3-Colorability, Hamiltonian Cycle, Traveling Salesperson, Maximum Clique, Subset Sum {ref:coo71} {ref:kar72} {ref:lev73} {ref:gj79}.

There is an oracle separating P from NP {ref:bgs75}; P ≠ NP relative to a random oracle with probability 1 {ref:bg81}. If NP ⊆ coAM (or BPP), PH collapses to Σ_2P {ref:bhz87}. If NP ⊆ P/poly, PH collapses to Σ_2P {ref:kl82}. NP = PCP(log n, O(1)) {ref:alm98}. NP is equal to SO-E (second-order logic with existential second-order quantifiers) {ref:fag74}.
