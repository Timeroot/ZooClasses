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
  - BQP
properties:
  - protocol
---
Statistical Zero Knowledge. The class of decision problems where a "yes" answer can be verified by a statistical zero-knowledge proof protocol: a probabilistic polynomial-time verifier exchanges messages with an unbounded prover, and becomes convinced of "yes" without learning anything else (statistically).

Formally: for each verifier choice of random coins, its "view" of the interaction must be statistically close (trace distance ≤ 1/10) to a distribution the verifier could generate alone (in polynomial time), without the prover.

Graph non-isomorphism is a famous example in SZK. Defined in {ref:gmr89} (for zero-knowledge in general).

SZK is closed under complement {ref:oka96}. Can be assumed constant-round and public-coin {ref:oka96}. Complete promise problem: Statistical Difference (SD) {ref:sv97}. Another complete: Entropy Difference (ED) {ref:gv99}.

Contains {lang:PZK} and {lang:NISZK}. Contained in AM ∩ coAM and {lang:CZK} and {lang:QSZK}.

If any hard-on-average language is in SZK, one-way functions exist {ref:ost91}. There exists an oracle where SZK ⊄ BQP {ref:aar02}. Contained in {lang:DQP} {ref:aar02b}.
