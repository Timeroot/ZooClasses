---
name: TC
related:
  - AC
  - NC
  - TC^0
  - TC^1
properties:
  - circuit
---
Threshold Circuits. TC^i is the class of decision problems solvable by polynomial-size, depth O(log^i n) circuits with unbounded fanin AND, OR, and majority (MAJ) gates. A majority gate returns 1 if at least half of its inputs are 1. Other equivalent gate types include threshold gates (THR) and MOD_{p_n} where p_n is the n-th prime.

A uniformity requirement is sometimes also placed.

Each TC^i contains AC^i (in fact ACC^i) and is contained in NC^{i+1}. Thus NC = AC = TC.
