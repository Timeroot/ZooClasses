---
name: TOWER
related:
  - ELEMENTARY
  - PR
---
Iterated Exponential Time. Defined in {ref:sch16} as the union of DTIME(F_3(p(n))) over all elementary functions p(n), where F_3 is the third level of the fast-growing hierarchy (the iterated exponential function).

Strictly contains {lang:ELEMENTARY} and is strictly contained in {lang:PR}. Note that the same class is obtained if DTIME is replaced by NTIME or DSPACE.

Unlike ELEMENTARY and PR, which have no complete problems, TOWER has natural complete problems under elementary reductions: Star-Free Expression Equivalence (SFEq) and the satisfiability of Weak Monadic Theory of One Successor (WS1S).
