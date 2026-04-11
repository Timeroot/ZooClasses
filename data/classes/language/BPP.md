---
name: BPP
related:
  - ZPP
  - RP
  - AM
  - NP
  - PH
  - P
  - Σ_2P
---
Bounded-Error Probabilistic Polynomial-Time. The class of decision problems solvable by a randomized polynomial-time Turing machine with error probability at most 1/3 (for both "yes" and "no" instances). All computation paths have the same length.

Often identified as the class of feasible problems for a computer with access to a genuine random-number source. Defined in {ref:gil77}.

Contained in Σ_2P ∩ Π_2P {ref:lau83}, and in ZPP^NP {ref:gz97}. Also contained in P/poly {ref:adl78}.

If any problem in E requires circuits of size 2^Ω(n), then BPP = P {ref:iw97}. Under such a derandomization assumption, BPP can be solved deterministically.

If BPP contains NP, then RP = NP and PH ⊆ BPP {ref:zac88}.

BPP is not known to have complete languages. There exist oracles relative to which P = RP but P ≠ BPP {ref:bf99}.
