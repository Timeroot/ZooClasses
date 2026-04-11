---
name: PH
related:
  - NP
  - coNP
  - Delta_2P
  - Sigma_2P
  - Pi_2P
  - PP
  - PSPACE
  - BPP
---
Polynomial-Time Hierarchy. Let Δ_0P = Σ_0P = Π_0P = P. For i > 0:
- Δ_iP = P with Σ_{i-1}P oracle.
- Σ_iP = NP with Σ_{i-1}P oracle.
- Π_iP = coNP with Σ_{i-1}P oracle.

PH is the union of these classes over all nonneg constants i. Equivalently, PH is the class of problems expressible with alternating polynomial quantifiers.

Defined in {ref:sto76}. Contained in P^PP {ref:tod89}. Contains BPP {ref:lau83}.

Relative to a random oracle, PH is strictly contained in PSPACE with probability 1 {ref:cai86}. The hierarchy is infinite relative to a random oracle (each level strictly contains the previous) with probability 1 {ref:rst15}.

If NP ⊆ P/poly, PH collapses to Σ_2P {ref:kl82} or even O_2P {ref:cr06}. PH is also equal to the set of boolean queries expressible in second-order logic.
