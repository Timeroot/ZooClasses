---
name: Ack
related:
  - DSPACE
  - DTIME
  - ELEMENTARY
  - NTIME
  - PR
  - R
  - TOWER
---
Ackermann Time. Defined in {ref:sch16}. Let F_0(x) = x+1 and F_k(x) = F_{k-1}^x(x), where F_{k-1}^x(x) means F_{k-1}(x) applied to itself x times. For example F_1(x) = 2x+1, F_2(x) = 2^(x+1)(x+1)-1, etc. Then define F_ω(x) = F_x(x), which has the same growth rate as A(x,x) where A is the Ackermann function.

Ack equals DTIME(F_ω(p(n))) over all primitive-recursive functions p(n). The class remains unchanged if DTIME is replaced by NTIME or DSPACE.

Strictly contains {lang:ELEMENTARY}, {lang:TOWER}, and {lang:PR}. Is strictly contained in {lang:R}. The relationship between Ack and PR is analogous to the relationship between Tower and ELEMENTARY: Ack contains problems "barely" outside of PR and, unlike PR, has complete problems.

The reachability problem for Petri nets {ref:ler22} and vector addition systems {ref:co22} are complete for Ack under primitive-recursive reductions.
