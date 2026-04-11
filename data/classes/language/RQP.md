---
name: RQP
related:
  - coRQP
  - EQP
  - ZQP
  - RBQP
  - RP
properties:
  - quantum
---
One-Sided Randomized Quantum Polynomial-Time. The class of problems solvable by a QTM that:
1. Accepts with probability 0 when the answer is "no."
2. Accepts with probability at least 1/2 when the answer is "yes."

The quantum analog of RP. Since one acceptance probability must exactly vanish, RQP has the same technical caveats as {lang:EQP}. Complement is {lang:coRQP}. ZQP = RQP ∩ coRQP.
