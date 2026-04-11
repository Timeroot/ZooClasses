---
name: PLS
related:
  - TFNP
  - FBQP
  - PPA
  - PPP
  - PPAD
---
Polynomial Local Search. A subclass of {lang:TFNP} for problems guaranteed to have a solution by the lemma that "every finite directed acyclic graph has a sink."

More precisely: for each input, there is a finite set of solutions, a polynomial-time cost function, and a polynomial-time algorithm finding a lower-cost neighbor if one exists. The problem is to return any local optimum (a solution no worse than all its neighbors).

Defined in {ref:jpy88} {ref:py88}. There exist oracles relative to which PLS is not contained in FBQP {ref:aar03}, PPA {ref:bm04}, or PPP {ref:ghj22}, and PPA and PPP are not contained in PLS {ref:mor01}.
