---
name: CZK
related:
  - SZK
  - PZK
  - NP
  - IP
  - PSPACE
  - AVBPP
properties:
  - protocol
---
Computational Zero-Knowledge. Same as {lang:SZK}, except that the two distributions (the verifier's view with the prover, and the simulated view without) are only required to be computationally indistinguishable by any BPP algorithm, rather than statistically close.

Unlike SZK, it is not known if CZK is closed under complement. Assuming one-way functions exist, CZK contains NP {ref:gmw91} and equals IP = PSPACE {ref:bgg90}. If one-way functions do not exist, CZK = {lang:AVBPP} {ref:ow93}.

Contains {lang:PZK} and {lang:SZK}.
