---
name: HalfP
related:
  - EP
  - EQP
  - Mod_kP
  - RP
  - WPP
---
RP With Exactly Half Acceptance. The class of decision problems solvable by an NP machine such that:
1. If the answer is "yes," exactly 1/2 of computation paths accept.
2. If the answer is "no," all computation paths reject.

The number of candidate witnesses is implicitly restricted to be a power of 2 (which holds automatically if witnesses are binary strings).

Contained in {lang:RP}, {lang:EP}, and Mod_kP for every odd k. Contained in {lang:EQP} by the Deutsch-Jozsa algorithm.

Defined in {ref:bb92}, where it was called C_{==}P[half] (C_{==}P being an alternative name for {lang:WPP} that did not catch on). Shown in {ref:bs00} that HalfP is contained in every similar class where 1/2 is replaced by some other dyadic fraction.
