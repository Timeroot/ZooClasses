---
name: BH
related:
  - NP
  - PH
  - QH
  - coNP
  - DP or D^p
  - Δ_2P
---
Boolean Hierarchy over NP. The smallest class that contains NP and is closed under union, intersection, and complement. Defined in {ref:ww85}.

The levels are defined inductively: BH_1 = NP; BH_{2i} = BH_{2i-1} ∩ coNP languages; BH_{2i+1} = BH_{2i} ∪ NP languages. BH is the union of all BH_i.

Contained in Δ_2P and in P^{NP[log]}. If BH collapses at any level, then PH collapses to Σ_3P {ref:kad88}.
