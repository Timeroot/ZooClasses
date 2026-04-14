---
name: YQP
related:
  - BPP
  - BQP
  - BQP/qpoly
  - MA
  - QMA
properties:
  - quantum
---
Yaroslav BQP. The quantum analogue of {lang:YPP}: the class of decision problems for which there exists a polynomial-time quantum machine M such that:
1. For all input sizes n, there exists a polynomial-size quantum advice state |ψ_n⟩ such that M(x, |ψ_n⟩) outputs the correct answer with probability ≥ 2/3 for all inputs x of size n.
2. For all inputs x and quantum advice states |ψ⟩, the probability that M(x, |ψ⟩) outputs the incorrect answer is at most 1/3 (it may output "I don't know").

Contains {lang:BQP} and {lang:YPP}, and is contained in QMA and P/poly {ref:ad14}.
