---
name: LogFewNL
related:
  - FewP
  - ModZ_kL
  - NL
---
Logspace-Bounded Few. The class of decision problems solvable by a nondeterministic logspace Turing machine such that: (1) if the answer is "no," all computation paths reject; (2) if the answer is "yes," the number of accepting paths is bounded by a polynomial in the input size.

This is the logspace analogue of {lang:FewP}: the same few-witnesses condition but with a logspace (NL) machine rather than a polynomial-time machine.

Defined in {ref:bdh92}, where it was also shown that LogFewNL ⊆ ModZ_kL for all k > 1.
