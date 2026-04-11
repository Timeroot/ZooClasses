---
name: WAPP
related:
  - "#P"
  - AWPP
  - SBP
  - PP
---
Weak Almost-Wide PP. The class of decision problems for which there exists a #P function f, a polynomial p, and an ε > 0, such that for all inputs x:
1. If the answer is "yes," then 2^{p(|x|)} ≥ f(x) > (1+ε)·2^{p(|x|)-1}.
2. If the answer is "no," then 0 ≤ f(x) < (1-ε)·2^{p(|x|)-1}.

Defined in {ref:bgm02}, where it was also shown that WAPP is contained in {lang:AWPP} and {lang:SBP}.
