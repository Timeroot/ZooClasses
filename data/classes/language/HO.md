---
name: HO
related:
  - SO
  - PH
---
High-Order Logic. An extension of Second-Order ({lang:SO}) logic with quantification over higher-order variables.

A relation of order o and arity k is a subset of k-tuples of relations of order o-1 and arity k; at order 1, this recovers first-order variables. HO^o is the set of formulae with quantification up to order o. Σ^i_j (resp. Π^i_j) is the set of HO^{i+1} formulae beginning with an existential (resp. universal) quantifier followed by at most j-1 alternations.

Defined in {ref:ht06}, where it was shown that Σ^i_j = the class of problems solvable in time 2_2^{i-1}(n^O(1)) with a Σ^P_{j-1} oracle (the (j-1)-th level of the polynomial hierarchy).
