---
name: HeurBPTIME
concrete: false
related:
  - HeurBPP
  - HeurDTIME
---
Heuristic BPTIME(f(n)). Parameterized by a time bound f(n).

The class of distributional problems (L, D) for which a 1 - 1/poly(n) fraction of instances are solvable by a BPTIME(f(n)) machine.

HeurBPP = ∪_c HeurBPTIME(n^c).

Has the same relationship to BPTIME as HeurDTIME has to DTIME {ref:BT06}.
