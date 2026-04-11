---
name: ALL
related:
  - R
  - RE
---
The class of ALL languages. Literally everything — no restriction on decidability or running time.

Not a useful computational class on its own, but it appears naturally when strong advice is given to certain classes. Aaronson {ref:aar04b} observed that PP/rpoly (PP with polynomial-size randomized advice) equals ALL, as does PostBQP/qpoly. Raz {ref:raz05} showed QIP/qpoly = ALL, and even IP[2]/rpoly = ALL. Also MA_EXP/rpoly = ALL, and PDQP/qpoly = ALL {ref:aar18}.

By contrast, PSPACE/rpoly = PSPACE/poly and EXPSPACE/rpoly = EXPSPACE/poly, which are not ALL. The key distinction is that in the cases giving ALL, computational nondeterminism is applied after the advice, so the prover/post-selector can exploit a description of the advice state.
