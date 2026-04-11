---
name: 3SUM-hard
related:
  - P
---
Problems Hard for 3SUM. Defined in {ref:go95}: a problem P is 3SUM-hard if 3SUM (given n integers, do three of them sum to zero?) is reducible to a constant number of instances of P with additional time o(n^2) using the real RAM model.

Known to contain many computational geometry problems, including:
- 3-Points-On-Line: given a set of points in the plane, does any line connect three of them?
- Sorting X + Y, triangle identification, etc.

A lower bound of Ω(n^2) has been shown in weaker models of computation, but for the real RAM the conjecture remains open. Recent work suggests that some 3SUM-hard problems may admit sub-quadratic solutions.
