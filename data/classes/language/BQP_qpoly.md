---
name: BQP/qpoly
related:
  - CH
  - EESPACE
  - NP
  - P/poly
  - PP
  - YQP
  - BQP/mpoly
properties:
  - quantum
  - nonuniform
---
BQP With Polynomial-Size Quantum Advice. The class of problems solvable by a BQP machine that receives a quantum state ψ_n as advice, depending only on the input length n.

Acceptance probability does not need to be bounded away from 1/2 for bad advice (this is BQP/*Qpoly in {ref:ny03} notation). A strict bound would make quantum advice unusable by a continuity argument.

Does not contain EESPACE {ref:ny03}. BQP/qpoly = YQP/poly {ref:ad14}.

There exists an oracle relative to which BQP/qpoly ⊄ NP {ref:aar04b}. There is a quantum oracle separating BQP/qpoly from BQP/mpoly {ref:ak06}. An unrelativized separation would imply PP ⊄ P/poly.

Contained in PP/poly {ref:aar06} and in CH/poly.
