---
name: ZQP
related:
  - EQP
  - RQP
  - BQP
  - ZBQP
properties:
  - quantum
---
Zero-Error Extension Of {lang:EQP}.
The class of questions that can be answered by a QTM that answers yes, no, or maybe. If the correct answer is yes, then P[no] = 0, and vice-versa; and the probability of maybe is at most 1/2. Since some of the probabilities have to vanish, ZQP has the same technical caveats as {lang:EQP}.
Defined independently in {ref:BW03} and in {ref:Nis02}. Equals {lang:RQP} ∩ {lang:coRQP}. There is an oracle such that ZQP^{ZQP} is larger than ZQP {ref:BW03}.
