---
name: IP
related:
  - QIP
  - MIP
  - AM
  - PSPACE
properties:
  - protocol
---
Interactive Proofs. In general, IP[r] means a proof where a player exchanges r rounds with a polynomial time verifier; the verifier has private random coins. The class IP is defined as IP[poly(n)], and it turns out that IP=PSPACE, see {ref:Sha90}. For IP[r] with a constant r, it turns to be equal to AM; see AM for more. {ref:BM88} also proved that IP[f(n)]=IP[c*f(n)].
