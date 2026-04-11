---
name: ZBQP
related:
  - EQP
  - RBQP
  - coRBQP
  - RQP
  - BQP
  - ZQP
  - ZPP
  - FBQP
  - NP_cap_coNP
properties:
  - quantum
---
Strict Quantum ZPP. Defined as RBQP ∩ coRBQP. Equivalently, the class of problems in NP ∩ coNP such that both positive and negative witnesses are in FBQP.

For example, square-free numbers are in ZBQP, because factoring is in FBQP and a factorization certifies a square divisor — certified in P via AKS primality {ref:aks02}.

Unlike EQP or ZQP, ZBQP would generalize ZPP in practice if quantum computers existed, in the sense that it provides proven answers. ZBQP^{ZBQP} = ZBQP.

Contains ZPP. Contained in RBQP and ZQP.
