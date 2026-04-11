---
name: UP
related:
  - NP
  - P
  - PromiseUP
  - RP
  - coUP
---
Unambiguous Polynomial-Time. The class of decision problems solvable by an NP machine such that:
1. If the answer is "yes," exactly one computation path accepts.
2. If the answer is "no," all computation paths reject.

Defined in {ref:val76}.

"Worst-case" one-way functions exist if and only if P ≠ UP {ref:gs88} {ref:ko85}. "Worst-case" one-way permutations exist if and only if P ≠ UP ∩ coUP {ref:ht03}. (These are weaker than cryptographically useful one-way functions/permutations.)

There exists an oracle relative to which P ⊊ UP ⊊ NP {ref:rac82}, and these classes are distinct with probability 1 relative to a random oracle.
