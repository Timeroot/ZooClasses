---
name: O_2P
related:
  - NP
  - ONP
  - P/poly
  - PH
  - S_2P
---
Second Level of the Oblivious Symmetric Hierarchy. The class of decision problems for which there is a polynomial-time predicate P such that, for each length n, there exist witnesses y* and z* of length poly(n) such that for all x of length n:
1. If the answer is "yes," then for all z, P(x, y*, z) is true.
2. If the answer is "no," then for all y, P(x, y, z*) is false.

Unlike {lang:S_2P}, the witnesses here depend only on the length n and not on the input x itself, so O_2P ⊆ P/poly.

Defined in {ref:cr06}, where it was shown that O_2P is self-low, and that the Karp-Lipton collapse goes all the way to O_2P: if NP ⊆ P/poly then PH = O_2P.

Contains {lang:ONP} and coONP {ref:gm15}. For each k, O_2P contains a language with circuit complexity ≥ n^k {ref:glv24}.
