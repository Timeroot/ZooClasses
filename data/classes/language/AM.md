---
name: AM
related:
  - NP
  - MA
  - IP
  - BPP
  - SZK
  - NP/poly
  - coNP
  - PH
properties:
  - protocol
---
Arthur-Merlin. The class of problems for which a "yes" answer can be verified by an Arthur-Merlin protocol: Arthur (a BPP verifier) sends a random challenge (including his coins) to Merlin, Merlin responds, and Arthur decides. Completeness 2/3, soundness 2/3.

Surprisingly, AM is as powerful as private-coin interactive proofs: Arthur never needs to hide his randomness from Merlin {ref:gs86}. Also, AM[k] = AM[2] = AM for any constant k > 2 {ref:bm88}; the class AM is defined as AM[2].

Contains {lang:NP}, {lang:BPP}, and {lang:SZK}. Contained in {lang:NP/poly} and in Π_2P.

If AM contains coNP then {lang:PH} collapses to Σ_2P ∩ Π_2P {ref:bhz87}.

Under a strong derandomization assumption (some language in NE ∩ coNE requires nondeterministic circuits of size 2^Ω(n)), AM = NP {ref:mv99}.
