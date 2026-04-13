---
name: AvgP
related:
  - DistNP
  - HeurP
---
Average Polynomial-Time. A *distributional problem* consists of a decision problem A and a probability distribution μ over problem instances.

A function f from strings to integers is *polynomial on μ-average* if there exists ε > 0 such that the expectation of f^ε(x) is finite when x is drawn from μ.

(A, μ) is in AvgP if there exists an algorithm for A whose running time is polynomial on μ-average.

This definition is due to Levin {ref:Lev86}, who showed that simpler definitions lead to classes that fail to satisfy basic closure properties. See also {ref:Gol97}.

If AvgP = {lang:DistNP} then EXP = NEXP {ref:BCG92}.

Strictly contained in {lang:HeurP} {ref:NS05}.
