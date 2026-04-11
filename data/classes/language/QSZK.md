---
name: QSZK
related:
  - SZK
properties:
  - quantum
  - protocol
---
Quantum Statistical Zero Knowledge. A promise problem is in QSZK if there exists a quantum interactive proof system (a polynomial-time quantum verifier interacting with a polynomial-time quantum prover) such that: (1) For YES instances, there exists a polynomial-time quantum prover that causes the verifier to accept with high probability; (2) For NO instances, for any prover, the verifier accepts with low probability; (3) For YES instances, there exists a polynomial-time quantum simulator that, given only the input, can generate a quantum state (or transcript) whose distribution is statistically indistinguishable from the verifier's view in the real protocol. That is, the verifier learns nothing beyond the validity of the statement, even against quantum adversaries.
