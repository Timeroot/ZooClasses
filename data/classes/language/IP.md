---
name: IP
related:
  - QIP
  - MIP
  - AM
  - PSPACE
  - MA
properties:
  - protocol
---
Interactive Proof Systems. The class of decision problems for which a "yes" answer can be verified by an interactive proof: a probabilistic polynomial-time verifier exchanges polynomially many messages with an all-powerful prover. At the end:
1. If the answer is "yes," there must be a prover strategy that causes the verifier to accept with probability ≥ 2/3.
2. If the answer is "no," every prover strategy causes the verifier to reject with probability ≥ 2/3.

Defined in {ref:gmr89}. The Arthur-Merlin (public-coin) model, introduced independently in {ref:bab85}, is equivalent; this equivalence (even round-preserving) is proved in {ref:gs86}.

IP contains {lang:PH} {ref:lfk90}, and equals {lang:PSPACE} {ref:sha90}. Under a random oracle, coNP is not contained in IP {ref:ccg94}. A log-space verifier with read-once randomness can verify exactly P {ref:sha90} {ref:gkr15}.
