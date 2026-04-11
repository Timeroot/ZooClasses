---
name: LWPP
related:
  - AWPP
  - C_eqP
  - FP
  - NP
  - PP
  - SPP
  - WPP
---
Length-Dependent Wide PP. The class of decision problems solvable by an NP machine such that:
1. If the answer is "no," the number of accepting paths equals the number of rejecting paths.
2. If the answer is "yes," the difference (accepting minus rejecting paths) equals a function f(|x|) computable in polynomial time.

Defined in {ref:ffk94}, where it was shown that LWPP is low for {lang:PP} and C_=P (adding LWPP as oracle does not increase their power).

Contains {lang:SPP}. Contained in {lang:WPP} and {lang:AWPP}.

Contains the Graph Isomorphism problem {ref:kst92}, and problems for solvable black-box groups: group intersection, group factorization, coset intersection, and double-coset membership {ref:vin04}.
