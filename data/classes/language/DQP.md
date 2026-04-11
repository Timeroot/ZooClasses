---
name: DQP
related:
  - BQP
  - EXP
  - SZK
properties:
  - quantum
---
Dynamical Quantum Polynomial-Time. The class of decision problems solvable by a BQP machine with oracle access to a dynamical simulator. When given a polynomial-size quantum circuit, the simulator returns a sample from the distribution over "classical histories" induced by the circuit. The simulator adversarially chooses any history distribution satisfying axioms of "symmetry" and "locality".

Defined in {ref:aar05}. Contains {lang:BQP} and {lang:SZK}. Contained in {lang:EXP}. There exists an oracle relative to which DQP does not contain NP.
