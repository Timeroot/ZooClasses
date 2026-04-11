---
name: SZK
related:
  - AM
  - coAM
  - CZK
  - QSZK
  - PZK
  - NISZK
  - DQP
properties:
  - protocol
---
Statistical Zero Knowledge. A promise problem is in SZK if there exists an interactive proof system (a polynomial-time probabilistic verifier interacting with a polynomial-time prover) such that: (1) For YES instances, there exists a polynomial-time prover that causes the verifier to accept with high probability; (2) For NO instances, for any prover, the verifier accepts with low probability; (3) For YES instances, there exists a polynomial-time simulator that, given only the input, can generate a transcript whose distribution is statistically indistinguishable from the verifier's view in the real protocol. That is, the verifier learns nothing beyond the validity of the statement. The protocol may be multi-round, and the zero-knowledge property is statistical (i.e., holds against computationally unbounded verifiers). SZK is closed under complement, has complete promise problems (Statistical Difference, Entropy Difference), and is contained in AM ∩ coAM, as well as CZK and QSZK. Contains PZK and NISZK. There exists an oracle relative to which SZK is not in BQP. Contained in DQP. If any hard-on-average language is in SZK, then one-way functions exist.

## Notes

todo def
