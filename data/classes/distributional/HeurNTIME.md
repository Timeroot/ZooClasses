---
name: HeurNTIME
concrete: false
related:
  - HeurDTIME
---
Heuristic NTIME_δ(f(n)). Parameterized by a time bound f(n) and error rate δ(n).

Defined as HeurDTIME_δ(f(n)), but for non-deterministic heuristic algorithms.

NP is not contained in HeurNTIME_{1/2 + 1/n^a}(n^c) for any constants a, c {ref:Per07}.
