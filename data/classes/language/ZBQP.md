---
name: ZBQP
related:
  - EQP
  - RQP
  - BQP
  - ZQP
properties:
  - quantum
---
Strict Quantum {lang:ZPP}.
Defined as {lang:RBQP} ∩ {lang:coRBQP}. Equivalently, the class of problems in {lang:NP} ∩ {lang:coNP} such that both positive and negative witnesses are in {lang:FBQP}.
For example, the language of square-free numbers is in {lang:ZBQP}, because factoring is in {lang:FBQP} and a factorization can be certified in ZPP (indeed in P, by {ref:AKS02}).
Unlike {lang:EQP} or {lang:ZQP}, {lang:ZBQP} would generalize {lang:ZPP} in practice if quantum computers existed, in the sense that it provides proven answers. {thm:ZBQP^ZBQP = ZBQP}.
