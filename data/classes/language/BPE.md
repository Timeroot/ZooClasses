---
name: BPE
related:
  - E
  - EE
  - EXP
  - P
---
Bounded-Error Probabilistic Exponential Time with Linear Exponent. The class of decision problems solvable by a probabilistic Turing machine in time 2^O(n) with error probability at most 1/3 on all inputs.

Equivalently, a language L is in BPE if there is a deterministic Turing machine running in time 2^O(n) that, given an input x and a uniformly random string r of length 2^O(n), accepts with probability ≥ 2/3 if x ∈ L, and with probability ≤ 1/3 if x ∉ L.

Contains E, and is contained in EXP. BPP ⊆ BPE since polynomial time is bounded by 2^O(n).
