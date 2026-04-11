---
name: "AW[SAT]"
related:
  - NP
  - PSPACE
  - "W[1]"
  - "W[SAT]"
  - "AW[*]"
  - "AW[P]"
---
Alternating W[SAT]. Has the same relation to {lang:W[SAT]} as PSPACE does to NP.

The class of problems (x, r, k_1, ..., k_r) (with r, k_1, ..., k_r as parameters) that are fixed-parameter reducible to the following problem for some constant h: given a Boolean formula F over disjoint variable sets S_1, ..., S_r, does there exist an assignment to S_1 of Hamming weight k_1 such that for all assignments to S_2 of Hamming weight k_2, ..., (alternating ∃/∀), F is satisfied?

Defined in {ref:df99}. Contains {lang:AW[*]}, and is contained in {lang:AW[P]}.
