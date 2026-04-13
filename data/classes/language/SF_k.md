---
name: SF_k
related:
  - AM
  - BPP
  - Mod_3P
  - NP
  - P
  - PSPACE
  - ParityP
concrete: false
---
Width-k Bottleneck Turing Machines. The class of decision problems solvable by a k-bottleneck Turing machine: a machine that, after a polynomial amount of time, erases everything on the tape except for a single k-valued "safe-storage." There is also a counter recording the number of erasings, which acts as a nondeterministic witness. For example, SF_2 contains both ⊕P and NP by using the counter as a witness.

Defined in {ref:cf91}, where it was also shown that SF_5 = PSPACE.

The complexity of SF_2, SF_3, and SF_4 was studied in {ref:ogi94} and {ref:her97}. Among the results: SF_4 ⊆ BP·⊕P^{Mod_3P^{⊕P^{Mod_3P^{⊕P}}}}.
