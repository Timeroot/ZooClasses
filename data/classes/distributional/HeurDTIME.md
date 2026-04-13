---
name: HeurDTIME
concrete: false
related:
  - HeurP
  - HeurNTIME
  - HeurBPTIME
---
Heuristic DTIME_δ(f(n)). Parameterized by a time bound f(n) and error rate δ(n).

For functions f(n) and δ(n), (L, D) ∈ HeurDTIME_δ(f(n)) if there exists a heuristic deterministic algorithm A such that for all x in the support of D, A runs in time bounded by f(n) and fails with probability bounded by δ(n) {ref:BT06}.

HeurP = ∪_c HeurDTIME_{1/poly}(n^c).
