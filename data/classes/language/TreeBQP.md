---
name: TreeBQP
related:
  - BPP
  - BQP
  - PH
properties:
  - quantum
---
BQP Restricted to Tree States. The class of languages accepted by a BQP machine subject to the constraint that at every time step t, the machine's state is exponentially close to a tree state — a state expressible by a polynomial-size tree of additions and tensor products (together with complex constants and |0⟩ and |1⟩ leaf nodes).

More formally: a uniform classical poly-time algorithm generates a sequence of quantum gates and measurements. The measurement must accept with probability ≥ 2/3 for yes instances and ≤ 1/3 for no instances. If at any intermediate step the state is more than 2^{-Ω(n)} away from the nearest tree state of polynomial tree size, the outcome is chosen adversarially.

Contains {lang:BPP} and is contained in {lang:BQP}.

Defined in {ref:aar03b}, where it was also shown that TreeBQP is contained in the third level of PH, providing weak evidence that TreeBQP ≠ BQP.
