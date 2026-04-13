---
name: HeurP
related:
  - P
  - HeurBPP
---
Heuristic P. The class of distributional problems solvable by a P machine. Defined in {ref:imp95} (under the name HP).

Formally ({ref:bt06}): HeurP is the set of pairs (L, D) where L is a language and D is a distribution over instances, such that there exists an algorithm A with: for every δ > 0, for every n and every x in the support of D, A(x; n, δ) runs in time poly(n/δ) and is a heuristic algorithm for (L, D) with error probability at most δ.
