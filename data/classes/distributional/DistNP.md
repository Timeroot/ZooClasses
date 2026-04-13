---
name: DistNP
related:
  - AvgP
  - "(NP,P-samplable)"
---
Distributional NP (also called (NP,P-computable) or RNP). A *distributional problem* consists of a decision problem A and a probability distribution μ over problem instances.

(A, μ) is in DistNP if A is in NP and μ is P-computable (meaning that its cumulative density function can be evaluated in polynomial time).

DistNP has complete problems {ref:Lev86} (see also {ref:Gur87}), although unlike for NP this is not immediate.

Any DistNP-complete problem is also complete for {lang:(NP,P-samplable)} {ref:IL90}.

If {lang:AvgP} = DistNP then EXP = NEXP {ref:BCG92}.
