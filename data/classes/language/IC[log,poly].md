---
name: "IC[log,poly]"
related:
  - P
  - P/log
  - P/poly
  - NP
---
Logarithmic Instance Complexity, Polynomial Time. The class of decision problems such that, for every n-bit string x, there exists a program A of size O(log n) that, given x as input, correctly decides the answer on x in polynomial time. Formally, A must:
1. Return "yes", "no", or "I don't know" on any input in polynomial time.
2. Whenever A returns "yes" or "no", it is correct.
3. Return "yes" or "no" (not "I don't know") on x.

Defined in {ref:oks94}; see also {ref:lv97}. Strictly contains {lang:P/log} and is strictly contained in {lang:P/poly}.

If NP ⊆ IC[log,poly], then P = NP {ref:oks94}. Indeed, any self-reducible problem in IC[log,poly] is in P.
