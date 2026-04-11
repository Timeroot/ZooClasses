---
name: EQP
related:
  - BQP
  - ZQP
  - RQP
  - LWPP
properties:
  - quantum
---
Exact Quantum Polynomial-Time. Same as BQP except the quantum algorithm must return the correct answer with probability exactly 1, and run in polynomial time with probability 1.

Defined in {ref:bv97}. EQP is in {lang:LWPP} {ref:fr98}. There is an oracle separating EQP from NP {ref:bv97}, and indeed from Δ_2P {ref:gp01}. There is also an oracle relative to which EQP is not in Mod_pP for prime p {ref:gv02}.

See also {lang:EQP_K} for the gate-set-parameterized version.
