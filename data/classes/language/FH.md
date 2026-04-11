---
name: FH
related:
  - FH^1
  - FH^2
  - BQP
---
FH^k is the class of problems solvable by a uniform family of polynomial-size quantum circuits, with k levels of Hadamard gates and all other gates preserving the computational basis. (Conditional phase flip gates are fine, for example.) FH is the union of FH^k across all k, in other words, problems solvable by a uniform family with O(1) Hadamard layers. FH^0 is definitionally equal to {lang:P}, and {lang:FH^1}={lang:BPP} -- see {thm:FH^1=BPP}. The first "quantum" class is {lang:FH^2}, which includes factoring.
It is an open problem to show that the Fourier hierarchy is infinite relative to an oracle (that is, FHk is strictly contained in FHk+1).
Defined in {ref:Shi03}.
