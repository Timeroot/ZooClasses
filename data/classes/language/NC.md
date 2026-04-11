---
name: NC
related:
  - AC
  - TC
  - NC^0
  - NC^1
  - NC^2
  - NL
  - RNC
  - QNC
properties:
  - circuit
---
Nick's Class (named in honor of Nick Pippenger). NC^i is the class of decision problems solvable by a uniform family of Boolean circuits with polynomial size, depth O(log^i(n)), and fan-in 2. NC is the union of NC^i over all nonnegative i.

NC^i is contained in AC^i; thus NC = AC. Contains NL (in fact NL ⊆ NC^2).

NC also equals the union of PT/WK(log^k n, n^k)/poly over all constants k.

For a random oracle A, (NC^i)^A is strictly contained in (NC^{i+1})^A and NC^A is strictly contained in P^A, with probability 1 {ref:mil92}.

In descriptive complexity, NC can be defined by FO[log(n)^{O(1)}].
