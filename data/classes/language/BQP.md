---
name: BQP
related:
  - BPP
  - EQP
  - QMA
  - PP
  - AWPP
properties:
  - quantum
---
Bounded-Error Quantum Polynomial-Time. The class of decision problems solvable in polynomial time by a quantum Turing machine, with at most 1/3 probability of error. Equivalently, solvable by a uniform family of polynomial-size quantum circuits with bounded error {ref:yao93}.

Often identified as the class of feasible problems for quantum computers. Defined in {ref:bv97}, where it was shown BQP contains BPP and is contained in P^{#P}.

Contains integer factoring and discrete logarithm {ref:sho97}. Contained in {lang:PP} {ref:adh97} and {lang:AWPP} {ref:fr98}.

BQP^BQP = BQP {ref:bv97}.

There exist oracles relative to which BQP ≠ BPP; BQP ⊄ MA; BQP ⊄ PH; BQP ⊄ SZK; BQP ⊄ BPP_path; and NP ∩ coNP ⊄ BQP.
