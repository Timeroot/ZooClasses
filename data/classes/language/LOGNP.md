---
name: LOGNP
related:
  - NP
  - P
  - SNP
  - LOGSNP
---
Logarithmically-Restricted NP. The class of decision problems expressible as: the set of inputs I for which there exists a subset S = {s_1,...,s_{log n}} of {1,...,n} of size log n, such that for all x there exists y such that for all j ∈ S, the predicate φ(I, s_j, x, y, j) holds. Here x and y are logarithmic-length strings (or equivalently polynomially bounded numbers), and φ is computable in P.

LOGNP_0 is the subclass where φ is a first-order predicate without quantifiers and x, y are bounded lists of indices of input bits. LOGNP is also the closure of LOGNP_0 under polynomial-time many-one reductions.

See {lang:LOGSNP} for the simpler sibling class.
