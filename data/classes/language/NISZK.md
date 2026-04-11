---
name: NISZK
related:
  - SZK
properties:
  - protocol
---
Non-Interactive Statistical Zero Knowledge. A promise problem is in NISZK if there exists a polynomial-time probabilistic verifier V and a polynomial-time probabilistic simulator S such that: (1) For YES instances, there exists a polynomial-size message (the 'proof') that, when given to V, causes V to accept with high probability; (2) For NO instances, for any purported proof, V accepts with low probability; (3) For YES instances, the output distribution of V on the real proof is statistically indistinguishable from the output of S on the input alone (i.e., the verifier learns nothing beyond the validity of the statement). The protocol is non-interactive: the verifier receives a single message from the prover and then decides to accept or reject.
