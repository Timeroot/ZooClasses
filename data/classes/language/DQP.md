---
name: DQP
related:
  - BQP
properties:
  - quantum
---
Dynamical Quantum Polynomial-Time. The class of decision problems solvable by a BQP machine with oracle access to a dynamical simulator. When given a polynomial-size quantum circuit, the simulator returns a sample from the distribution over "classical histories" induced by the circuit. The simulator can adversarially choose any history distribution that satisfies the axioms of "symmetry" and "locality" -- so that the DQP algorithm has to work for any distribution satisfying these axioms. Defined in {ref:Aar05}.
