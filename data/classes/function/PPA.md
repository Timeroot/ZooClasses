---
name: PPA
related:
  - TFNP
  - PPAD
  - PPP
  - PLS
---
Polynomial Parity Argument. A subclass of {lang:TFNP} for problems guaranteed to have a solution by the lemma that "all graphs of maximum degree 2 have an even number of leaves."

More precisely: there's a polynomial-time algorithm that, given any string, computes its "neighbor" strings (at most two). Given a leaf string (one with only one neighbor), find another leaf string.

Defined in {ref:pap94b}. Contains {lang:PPAD}. There exist oracles relative to which PPA does not contain PLS {ref:bm04} or PPP {ref:bce95}, and PPA is not contained in PPP {ref:bce95}.

Example problems in PPA: finding an Arrow-Debreu equilibrium {ref:pap94b}; computing square roots mod n and finding quadratic nonresidues mod n {ref:jer12}; integer factorization is in PPA under GRH {ref:jer12}. Complete: Sperner's lemma for non-orientable 3-manifolds {ref:gri01}.
