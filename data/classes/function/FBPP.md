---
name: FBPP
related:
  - BPP
  - NP
---
Function BPP. The class of function problems solvable by a probabilistic polynomial-time algorithm with bounded error: given an input x and a polynomial-time predicate F(x,y), if there exists a y satisfying F(x,y), output any such y with probability ≥ 2/3; otherwise output 'no' with probability ≥ 2/3.

Equivalently, this is the class of search problems whose decision version is in BPP: the machine can use randomness and may err with probability at most 1/3. FBPP contains FP and is contained in FNP.
