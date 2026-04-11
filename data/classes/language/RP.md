---
name: RP
related:
  - coRP
  - ZPP
  - BPP
  - NP
  - P
---
Randomized Polynomial-Time. The class of decision problems solvable by a probabilistic polynomial-time Turing machine such that:
1. If the answer is "yes," at least 1/2 of computation paths accept.
2. If the answer is "no," all computation paths reject.

Defined in {ref:gil77}. Contains primality testing {ref:ah87}, though primality is now known to be in P {ref:aks02}.

ZPP = RP ∩ coRP. RP and ZPP have the same p-measure (either zero or one); if nonzero, then ZPP = BPP = EXP {ref:im03}.

See also: {lang:coRP}, {lang:ZPP}, {lang:BPP}.
