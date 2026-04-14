---
name: S_2P
related:
  - MA
  - NP
  - O_2P
  - P/poly
  - PH
  - ZPP
  - Delta_2P
  - Sigma_2P
  - Phi_2P
---
Second Level of the Symmetric Hierarchy. The class of problems for which there is a polynomial-time predicate P such that, on input x:
1. If the answer is "yes," then there exists a y such that for all z, P(x,y,z) is true.
2. If the answer is "no," then there exists a z such that for all y, P(x,y,z) is false.

The definition is symmetric: the prover and disprover submit simultaneous moves to a referee. Contrast with {lang:Sigma_2P}, where the prover moves first.

Defined independently in {ref:rs98} and {ref:can96}. Contains {lang:MA} and Δ_2P {ref:rs98}. Contained in ZPP^NP {ref:cai01}.

Φ_2P = S_2P (alternate definition) {ref:can96}. Sometimes written "symP" in the literature (an alternate name, not a distinct definition). If NP ⊆ P/poly then PH = S_2P (Sengupta; see {ref:cai01}), and even PH = O_2P {ref:cr06}.
