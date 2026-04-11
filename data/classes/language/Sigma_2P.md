---
name: "Sigma_2P"
related:
  - NP
  - PH
  - coNP
  - Pi_2P
  - Delta_2P
  - S_2P
  - MA
  - AM
---
The second existential level of the Polynomial Hierarchy. NP^NP: problems solvable by NP with an NP oracle. A language L is in Σ_2P if there is a polynomial-time predicate R such that x ∈ L iff ∃y ∀z R(x,y,z).

Contains NP and coNP^NP. If BPP ⊄ Σ_2P then NP ≠ BPP. BPP ⊆ Σ_2P ∩ Π_2P {ref:lau83}.

Σ_2P-complete: minimum circuit size (MCSP) with NP oracle, Succinct SAT.

See {lang:PH} for context.
