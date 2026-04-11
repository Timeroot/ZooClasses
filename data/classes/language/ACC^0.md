---
name: ACC^0
related:
  - AC^0
  - TC^0
  - CC^0
properties:
  - circuit
---
AC^0 With Arbitrary MOD Gates. Same as AC^0[m] (constant-depth, polynomial-size circuits with MOD m gates), but the circuit can contain MOD m gates for any m simultaneously.

Contained in {lang:TC^0}. Can be simulated by depth-3 threshold circuits of quasipolynomial size {ref:yao90}.

Williams {ref:wil11} showed there are no non-uniform ACC^0 circuits of polynomial size for NTIME[2^n], and no ACC^0 circuit of size 2^(n^O(1)) for E^NP. These are the only known nontrivial lower bounds against ACC^0.

Contains 4-PBP {ref:bt88}. See also: QACC^0 and {lang:CC^0}.
