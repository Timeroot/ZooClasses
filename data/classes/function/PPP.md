---
name: PPP
related:
  - TFNP
  - PPADS
  - PPA
  - PPAD
  - PLS
  - PWPP
---
Polynomial Pigeonhole Principle. A subclass of {lang:TFNP} for problems guaranteed to have a solution by the Pigeonhole Principle.

More precisely: we are given a Boolean circuit mapping n-bit strings to n-bit strings. Find either an input that maps to 0^n, or two distinct inputs that map to the same output.

Defined in {ref:pap94b}. Contains PPADS. There exist oracles relative to which PPP is not contained in PPA or PPAD {ref:bce95}, PPA is not contained in PPP {ref:bce95}, PPP is not contained in PLS {ref:mor01}, and PLS is not contained in PPP {ref:ghj22}.
