---
name: MA
related:
  - NP
  - BPP
  - AM
  - QMA
  - ExistsBPP
  - Sigma_2P
  - Pi_2P
  - MA_E
  - MA_EXP
properties:
  - protocol
---
Merlin-Arthur. The class of decision problems solvable by a Merlin-Arthur protocol: Merlin (unbounded power) sends Arthur a polynomial-size purported proof, and Arthur verifies in BPP (probabilistic polynomial-time):
1. If the answer is "yes," there exists a proof such that Arthur accepts with probability ≥ 2/3.
2. If the answer is "no," for all proofs Arthur accepts with probability ≤ 1/3.

Defined in {ref:bab85}. The one-sided and two-sided error definitions are equivalent {ref:fgm89}.

Contains NP, {lang:BPP}, and {lang:∃BPP}. Contained in {lang:AM} and {lang:QMA}. Also contained in Σ_2P ∩ Π_2P.

MA = NP under derandomization: if E requires exponentially-sized circuits, then PromiseBPP = PromiseP, implying MA = NP {ref:iw97}.

MA/1 (MA with 1 bit of advice) does not have circuits of size n^k for any k > 0 {ref:san07}.

See also: {lang:MA_E}, {lang:MA_EXP}.
