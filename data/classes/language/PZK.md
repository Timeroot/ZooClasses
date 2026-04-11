---
name: PZK
related:
  - SZK
properties:
  - protocol
---
Perfect Zero Knowledge. A promise problem is in PZK if there exists an interactive proof system (a polynomial-time probabilistic verifier interacting with a polynomial-time prover) such that: (1) For YES instances, there exists a polynomial-time prover that causes the verifier to accept with high probability; (2) For NO instances, for any prover, the verifier accepts with low probability; (3) For YES instances, there exists a polynomial-time simulator that, given only the input, can generate a transcript whose distribution is identically (not just statistically) distributed as the verifier's view in the real protocol. That is, the verifier learns nothing beyond the validity of the statement, and the simulation is perfect (the distributions are exactly equal, not just close).
