---
name: "para-NP"
related:
  - XP
  - NP
  - XNP
---
Parameterized NP. Languages (x,k) with a nondeterministic algorithm running in time f(k)*n^{O(1)}. Equivalently, problems with a deterministic polynomial-time verifier that take a problem and witness, and the witness is of size f(k)*n^{O(1)}. A classic example is k-coloring: it's in NP for any k, and fixing k at a low value (such as 3) leaves it difficult. Since k-coloring is atually para-NP-hard too, it's para-NP-complete. Compare with XNP, where the exponent of the machine is allowed to depend on k.
