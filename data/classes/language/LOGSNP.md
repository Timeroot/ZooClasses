---
name: LOGSNP
related:
  - DTIME
  - NTIME
  - P
  - QPLIN
  - SNP
  - LOGNP
---
Logarithmically-Restricted SNP. The class of decision problems expressible as: the set of inputs I for which there exists a subset S = {s_1,...,s_{log n}} of {1,...,n} of size log n, such that for all x there exists j ∈ S such that the predicate φ(I, s_j, x, j) holds. Here x is a logarithmic-length string (or polynomially bounded number), and φ is computable in P.

LOGSNP_0 is the subclass where φ is a first-order predicate without quantifiers and x is a bounded list of indices of input bits. LOGSNP is also the closure of LOGSNP_0 under polynomial-time many-one reductions.

See {lang:LOGNP} for the related class with one more quantifier alternation.
